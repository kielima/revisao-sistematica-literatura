"""Exporta dados_fck (meta_analysis_base.xlsx) para o dataset compacto usado em
kielima.com/metanalise (public/assets/metanalise.js no repositório kielima-site).

Uso:
    python3 metanalise-export.py > metanalise_compact.json

Saida: {"pairs": [...], "unit_stats": [...]}.

`pairs`: cada ponto e [fck_MPa, co2_kg_m3, categoria_1_letra, estrato_1_letra,
citacao_curta_ou_null, base_portland, co2_com_desconto_ou_null, sem_bruto, subfamilia_cimento_ou_null,
vida_util_anos_ou_null].
O 10.o (2026-10-16, F25): vida util de projecto declarada pelo proprio artigo (dados_fck col 19), para o
botao ci / ci_t do forest por familia (ci_t = ci / vida util, F22); null = sem vida util.
O 9.o (2026-10-11, F12): subfamilia do cimento comercial dos pares da familia opc (dados_fck col 48,
escrita por lotes_cimento/aplicar.py); null nas outras familias. Os dois anteriores
(2026-10-07): CO2 com os descontos do proprio artigo (null = sem desconto) e 1 quando o artigo so publica o valor
com desconto. `base_portland` (2026-09-28, pedido da Kie:
filtro 'so cimento Portland' vs 'tudo' no painel) e 'P' (ligante principal cimento
Portland), 'N' (sem clinquer Portland: geopolimero/alcali-ativado, CSA, magnesio,
gesso, madeira...) ou 'M' (linha mista) -- ver classificar_base_portland.py. `citacao_curta` (2026-09-12, pedido da Kie: forest
plot por familia com os estudos individuais, no expand de cada barra do
grafico "ci por familia de material") e uma citacao curta tipo "Sobrenome et
al., Ano" derivada de dados_fck.autores+ano -- ver short_label() abaixo para
a heuristica (o campo autores nao tem um formato unico: mistura
"Sobrenome, N.; Sobrenome, N." (';'), "Sobrenome, Nome and Sobrenome, Nome"
(bibtex 'and'), listas soltas de sobrenomes sem nome proprio separadas so por
virgula, e ate valores legados ja no proprio formato "Sobrenome et al., Ano").
null quando autores esta vazio -- o site mostra um rotulo generico nesse caso.
Puramente informativo (rotulo de UI), nao um identificador -- nunca usar para
casar com outra linha.

Filtra a pares comparaveis por m3 (exclui totais de estrutura inteira, que nao
tem a mesma unidade de analise) e classifica o material por palavras-chave no
campo `material`+`titulo`, com um dicionario OVERRIDE por row_id para os casos
que nao seguem um padrao regex generico (julgamento caso a caso feito sobre a
amostra completa dos 381 materiais que caiam em "outros" ate 2026-09-08 -- ver
CLAUDE.md / conversa da sessao 2026-09-08: a Kie pediu para zerar "outros",
classificando cada um na familia certa e confirmando que agregado de pneu
triturado entra em "reciclado").

⚠️ SO entram em `pairs` linhas cujo co2_unidade (dados_fck col 15) ja foi
confirmado como kg CO2-eq/m3 -- nativo (publicado assim pelo artigo, tag
[RELABEL] inclusive) ou derivado (convertido por nos, tag [DERIVADO]). Linhas
cuja unidade ainda esta na forma original do estudo (por m2, por tonelada,
por kg, por elemento inteiro, por metro linear, indice ja normalizado por
MPa, ou nao classificada) ficam de fora de `pairs` -- entravam antes sem
filtro nenhum e contaminavam o grafico (achado de 2026-09-08: a linha
argamassa row_id 2582 tinha co2_valor=0.176, que e o indice kg/(m3.MPa)
publicado pelo autor, nao um valor em kg/m3 -- estava plotado tal e qual como
se fosse 0.18 kg CO2/m3, um numero fisicamente impossivel para concreto).
Essas linhas continuam contadas em `unit_stats`, para o grafico de
transparencia de unidades no site nao perder o panorama completo -- ver
CO2_UNIDADE_PENDENTE_2026-09-08.csv para o worklist de conversao.

`unit_stats`: [{"kind": "nativo"|"derivado"|"pendente", "cat": <slug>, "n": N}, ...]
-- kind distingue "unidade normalizada em kg/m3, como o artigo publicou" de
"convertida por nos para a analise" de "ainda na unidade original do estudo,
por converter". cat so importa dentro de "pendente" (a familia de unidade:
m2/tonelada/kg/elemento/metro_linear/ja_mpa/outro); nativo e derivado tem
cat="m3" sempre. Recalculado a cada corrida deste script -- nao precisa de
manutencao manual conforme novos lotes forem confirmando mais linhas.

Depois de gerar o JSON, injectar manualmente em public/assets/metanalise.js
(substituir os arrays `var DATA = [...]` e `var UNIT_STATS = [...]`) e
reconferir os textos que citam contagens (KPI de pares, tier-n-p/tier-n-s) no
mesmo ficheiro.
"""
import json
import os
import re
import sys
import unicodedata

import openpyxl

BASE = 'meta_analysis_base.xlsx'

CATCODE = {
    'geopolimero': 'g', 'uhpc': 'u', 'scm': 's', 'reciclado': 'r', 'opc': 'o',
    'ligantes': 'l', 'alvenaria': 'a', 'biobase': 'b', 'concreto_armado': 'c',
}
TIERCODE = {'principal': 'p', 'sensibilidade': 's'}
# base do ligante (dados_fck col 40, escrita por classificar_base_portland.py, 2026-09-28)
PORTLANDCODE = {'sim': 'P', 'nao': 'N', 'misto': 'M'}

# Domínio "plausível" por m³ de material -- exclui totais de estrutura inteira
# (edifício, ponte), que aparecem em kg absolutos muito acima da escala por m³
# e não são a mesma unidade de análise dos demais pares.
FCK_MIN, FCK_MAX = 1, 300
CO2_MIN, CO2_MAX = -1000, 5000

# Overrides explicitos por (row_id, material) -- NAO pela linha da folha
# dados_fck, que desloca sempre que uma linha e inserida/apagada (armadilha
# descoberta 2026-09-08: a purga de linhas fck<20 e da familia
# tijolo/bloco/paver/telha deslocou os indices e fez varios overrides
# apontarem para a linha errada, caindo em "outros" ou pior, classificando
# o material errado). (row_id, material) e estavel porque row_id referencia
# articles_final.xlsx (nao muda) e o texto do material nao muda com a
# posicao da linha. Julgamento caso a caso feito sobre a amostra completa
# dos 381 materiais que caiam em "outros" ate 2026-09-08 -- ver
# classify_v2.py da sessao. Entradas cujo (row_id, material) ja nao existe
# em dados_fck (por a linha ter sido removida por outro motivo, ex. tijolo
# rejeitado por E1_moldavel) ficam mortas no dict, sem efeito -- inofensivo.
#
# Familia 'concreto_armado' (adicionada 2026-09-10, decisao da Kie): reforco
# estrutural de aco e uma dimensao ORTOGONAL a quimica do material (um
# concreto geopolimerico ou um SHCC podem estar armados ou nao -- ver
# discussao completa na tarefa Supabase #1487, criada 2026-09-08 durante a
# separacao concreto/vergalhao da linha 3416). A Kie resolveu a tensao de
# desenho ali registada optando pela família nova, mutuamente exclusiva com
# as outras (nao um campo booleano ortogonal) -- mais simples de mostrar no
# grafico atual. Usar esta familia SO quando o co2_valor da linha inclui
# necessariamente o CO2 do aco de armadura junto com o do concreto, sem
# como separar os dois a partir dos dados do proprio artigo. Primeiro caso
# candidato foi ALMIRALL et al. 2019 (linha 3301, onde o CO2 e funcao de
# Vs=Vsteel/Vconcrete) -- mas essa linha acabou REJEITADA (2026-09-10, ver
# observacoes da linha), nao por causa da familia, mas porque a Eq.(2) do
# artigo tem um erro tipografico/exportacao confirmado por duas vias
# independentes (nao bate com a fisica nem com o eixo do proprio grafico).
# Primeiro caso REAL confirmado (varredura 2026-09-10, tarefa #1487 parte 1):
# linha 3818 (YE et al. 2024, "RC", Tabela 5) -- co2_unidade diz
# explicitamente "inclui armadura de aco 1,01%", e o proprio artigo tem a
# comparacao interna RC (885.13, com aco) vs RC-0 (318.13, sem aco, familia
# quimica normal) que confirma a diferenca. Quando o artigo permite separar
# concreto de aco (ex.: linha 3416, LI et al. 2022; linha 3818's RC-0), a
# linha fica na familia quimica normal (o concreto/SHCC sozinho), nao aqui.
# A varredura completa (regex por sinais de armadura em material+titulo, 207
# candidatos, cruzados com os 1069 pares entao visiveis no grafico -> 96
# candidatos prioritarios, triados por plausibilidade fisica do valor ->
# 8 suspeitos, verificados um a um contra as observacoes ja existentes na
# linha, sem precisar reabrir PDF) fechou com 1 caso confirmado (3818), 2
# achados colaterais fora do escopo desta familia mas corrigidos na mesma
# sessao (bug de negacao em classify_unidade, ver _NEGACAO_M3_PAT acima; a
# linha 3102/row_id 843 tinha unidade "por laje", nao m3, mal classificada) e
# 1 outlier extremo nao resolvido (linha 1839, row_id 4930, 3532 kg CO2/m3 --
# parece erro de escala na fonte EPD citada pelo artigo, nao relacionado a
# armadura, fica para a Kie decidir). A varredura dos restantes ~111
# candidatos fora de `pairs` (nao afetam o grafico hoje) fica de fora desta
# rodada por prioridade -- retomar quando a Kie pedir.
OVERRIDE = {
    (2609, 'Classe 1A (20-35 MPa) - traco max. impacto: (Artigo 01) 550C-50CR-MK'): 'opc',
    (2609, 'Classe 1A (20-35 MPa) - traco min. impacto: (Artigo 07) CFL 25-50-25 (CV+po de calcario substituindo cimento)'): 'opc',
    (2609, 'Classe 1B (35-50 MPa) - traco max. impacto: (Artigo 01) 550C-30CR-MK'): 'opc',
    (2609, 'Classe 2 (50-80 MPa) - traco max. impacto: (Artigo 11) M6'): 'opc',
    (2628, 'Argila solidificada com cal virgem (grupo L20-OC, cura mista)'): 'ligantes',
    (2628, 'Argila solidificada com magnesia reativa (grupo M20-OC, cura mista)'): 'ligantes',
    (2688, 'Carbon-reinforced concrete (CRC) — painel de fachada, 4000x3600x40mm (~0.576 m3)'): 'opc',
    (2693, 'Viga BFRP pre-tensionada, 1200x200x200mm (Beams 1.1/1.2)'): 'opc',
    (2693, 'Viga BFRP pre-tensionada, 2000x200x200mm (Beams 2.1/2.2/2.3)'): 'opc',
    (2693, 'Viga BFRP pre-tensionada, 2700x200x200mm (Beams 3.1/3.2)'): 'opc',
    (2693, 'Viga BFRP pre-tensionada, 3860x200x200mm (Beams 4.1/4.2)'): 'opc',
    (2698, 'Pasta/argamassa de cimento de oxicloreto de magnesio (MOC-9, razao molar 9) - via humida (sintetizado a partir de agua do mar)'): 'ligantes',
    (2698, 'Pasta/argamassa de cimento de oxicloreto de magnesio (MOC-9, razao molar 9) - via seca (calcinacao de magnesita)'): 'ligantes',
    (2710, 'Pasta de cimento com 20% de HCP calcinada carbonatada (M20)'): 'ligantes',
    (2724, 'Argamassa composita de rejeitados de molibdenio calcinados (MTCM-3, calcinacao 1350C)'): 'reciclado',
    (2739, 'Tabuleiro de ponte PCBG (vigas pre-esforcadas, HP-40)'): 'opc',
    (2739, 'Tabuleiro de ponte PCLS (pre-esforcado, laje aligeirada, HP-40)'): 'opc',
    (2739, 'Tabuleiro de ponte PCSS (pre-esforcado, laje maciça, HP-40)'): 'opc',
    (2741, 'Tabuleiros de ponte (S-LCA), fatores de emissao genericos citados do estudo companheiro (Martinez-Munoz et al. 2021)'): 'opc',
    (3115, 'LWCM LT5S0 (argamassa leve com FAC + 0.05% MWCNTs, sem nanosilica) - melhor desempenho mecanico entre as LWCM'): 'scm',
    (3132, 'concreto de cimento composto com cinza de Vitellaria Paradoxa (VPA) - mistura de controlo (V0, 100% PLC)'): 'scm',
    (3133, 'Biowall - composito 3D-impresso de particulas de madeira + amido + lignosulfonato de sodio (BW1, sem reciclagem)'): 'biobase',
    (3146, 'concreto com mucilagem de Opuntia ficus-indica (Ofim) como bio-aditivo — comparativo nivelado (APCR) Ofim-15/10 (15% Ofim + 10% reducao de cimento)'): 'biobase',
    (3152, 'argamassa com borracha de pneu triturado (CR) — mistura M_10 (10% CR)'): 'reciclado',
    (3152, 'argamassa com borracha de pneu triturado (CR) — mistura M_15 (15% CR)'): 'reciclado',
    (3152, 'argamassa com borracha de pneu triturado (CR) — mistura M_20 (20% CR)'): 'reciclado',
    (3152, 'argamassa com borracha de pneu triturado (CR) — mistura M_25 (25% CR)'): 'reciclado',
    (3152, 'argamassa com borracha de pneu triturado (CR) — mistura M_30 (30% CR)'): 'reciclado',
    (3152, 'argamassa com borracha de pneu triturado (CR) — mistura M_35 (35% CR)'): 'reciclado',
    (3152, 'argamassa com borracha de pneu triturado (CR) — mistura M_40 (40% CR)'): 'reciclado',
    (3152, 'argamassa com borracha de pneu triturado (CR) — mistura M_REF (0% CR, controlo)'): 'reciclado',
    (3182, 'concreto com agregado graudo de plastico de e-waste (e-plastic), cenario E2 (20% agregado graudo substituido por e-plastic)'): 'reciclado',
    (3201, 'SCC com 30% residuo de mina de magnesita como agregado grosso (30MWCA)'): 'reciclado',
    (3201, 'SCC de controlo (CC) - sem residuo de mina'): 'reciclado',
    (3221, 'concreto pronto com SCMs, classe C30 (media dos tracos C30 da base de 440 tracos chineses)'): 'scm',
    (3221, 'concreto pronto com SCMs, classe C80 (media dos tracos C80 da base de 440 tracos chineses)'): 'scm',
    (3118, 'argamassa de referencia REF (sem cinza volante de biomassa)'): 'opc',
    (4471, 'SCUHPC - concreto ultra-alto-desempenho autoadensavel convencional (base OPC, comparador)'): 'uhpc',
    (3151, 'LC3 (Limestone Calcined Clay Cement) concreto — classe M40 (normal strength)'): 'scm',
    (3151, 'LC3 (Limestone Calcined Clay Cement) concreto — classe M70 (high strength, HSC)'): 'scm',
    (3615, 'concreto com po de vidro 20% (glass powder)'): 'scm',
    (2653, 'Bloco carbonatado (escoria de aco inoxidavel, SSS) - Cenario S1 (recuperacao CO2)'): 'ligantes',
    (2653, 'Bloco carbonatado (escoria de aco inoxidavel, SSS) - Cenario S2 (recuperacao CO2 por membrana, menor impacto)'): 'ligantes',
    (2653, 'Bloco carbonatado (escoria de aco inoxidavel, SSS) - Cenario S3 (recuperacao CO2)'): 'ligantes',
    (3105, 'ASS/N3 (100% AS, 3% Na2O) - rede'): 'geopolimero',
    (3105, 'ASS-Q50/N3 grid / renew'): 'geopolimero',
    (3105, 'ASS-Q50/N1 grid / renew'): 'geopolimero',
    (3105, 'ASS-Q25/N3 grid / renew'): 'geopolimero',
    (3105, 'ASS-Q50/N2 grid / renew'): 'geopolimero',
    (3105, 'ASS-Q75/N3 grid / renew'): 'geopolimero',
    (3105, 'ASS-L50/N1 grid / renew'): 'geopolimero',
    (3105, 'ASS-L50/N2 grid / renew'): 'geopolimero',
    (3105, 'ASS-L25/N3 grid / renew'): 'geopolimero',
    (3105, 'ASS-L50/N3 grid / renew'): 'geopolimero',
    (3105, 'ASS-L75/N3 grid / renew'): 'geopolimero',
    (3162, "Aduela CSA/GFRP - so a coluna 'Concrete' (betao A-CSA-CEM II, sem armadura)"): 'ligantes',
    (5012, 'Concreto base cimento Portland vs concreto AAM (material ativado alcalinamente)'): 'opc',
    (3099, 'geopolymer concrete auto-reparavel (SHGPC) vs GPC vs OPCC de referencia, com microcapsulas de self-healing'): 'opc',
    (3225, 'argamassa de baixo carbono (PC, CSA, LC3, CSA-C, AAS) selecionadas para igual classe de resistencia'): 'opc',
    (4027, 'Concreto OPC 50 MPa vs geopolimero (90% FA/10% GGBFS) 50 MPa -- decomposicao de inventarios hibridos (mesmo caso de estudo do artigo companheiro, linha 4026)'): 'opc',
    (3280, 'argamassa cal hidraulica natural NHL2 (carbonatada)'): 'ligantes',
    (3280, 'argamassa cal hidraulica natural NHL3.5 (carbonatada)'): 'ligantes',
    (3280, 'argamassa cal hidraulica natural NHL3.5 (nao-carbonatada)'): 'ligantes',
    (3280, 'argamassa cal hidraulica natural NHL5 (carbonatada)'): 'ligantes',
    (3280, 'argamassa cal hidraulica natural NHL5 (nao-carbonatada)'): 'ligantes',
    (3311, 'Bloco de pavimento (paving block) com sedimento marinho estabilizado/solidificado com cimento - cenario Sc10'): 'reciclado',
    (3311, 'Bloco de pavimento (paving block) com sedimento marinho estabilizado/solidificado com cimento - cenario Sc11'): 'reciclado',
    (3311, 'Bloco de pavimento (paving block) com sedimento marinho estabilizado/solidificado com cimento - cenario Sc8'): 'reciclado',
    (3311, 'Bloco de pavimento (paving block) com sedimento marinho estabilizado/solidificado com cimento - cenario Sc9'): 'reciclado',
    (3346, 'concreto existente reutilizado (blocos de parede cast-in-place)'): 'reciclado',
    (3353, 'cimento CEM I/CEM III B 42.5, portfolio medio da fabrica Cluster West (CEMEX) em 1997'): 'scm',
    (3353, 'cimento CEM I/CEM III B 42.5, portfolio medio da fabrica Cluster West (CEMEX) em 2009'): 'scm',
    (3367, 'cimento P-35 (Cuban Standard NC-95:2011, 5% zeolito) -- Cementos Cienfuegos S.A., Cuba'): 'scm',
    (3367, 'cimento PC (ASTM, sem zeolito) -- Cementos Cienfuegos S.A., Cuba'): 'scm',
    (3367, 'cimento PP-25 (Cuban Standard NC-96:2011, 19% zeolito) -- Cementos Cienfuegos S.A., Cuba'): 'scm',
    (3377, 'ligante alcali-activado FA 100% (ativador NaOH 6M)'): 'ligantes',
    (3377, 'ligante alcali-activado GGBS25:FA75 (ativador NaOH 6M)'): 'ligantes',
    (3377, 'ligante alcali-activado GGBS50:FA50 (ativador NaOH 6M)'): 'ligantes',
    (3377, 'ligante alcali-activado GGBS75:FA25 (ativador NaOH 6M)'): 'ligantes',
    (3479, 'FRC (fiber-reinforced concrete) com residuo bruto triturado de pa de turbina eolica (RCWTB) ate 10% vol. - Espanha, mix W2 (2% RCWTB)'): 'reciclado',
    (3497, 'concreto de meio-fio (kerb) com agregado natural (NA) e agregado de pneu triturado (TDA) 0-20%, mistura CC-25 (controlo, 100% NA, 0% TDA)'): 'reciclado',
    (3497, 'concreto de meio-fio, NA + 10% TDA (CTr-c10-25)'): 'reciclado',
    (3497, 'concreto de meio-fio, NA + 15% TDA (CTr-c15-25)'): 'reciclado',
    (3497, 'concreto de meio-fio, NA + 20% TDA (CTr-c20-25)'): 'reciclado',
    (3497, 'concreto de meio-fio, NA + 5% TDA (CTr-c05-25)'): 'reciclado',
    (3512, 'SHCC imprimivel 3D com diatomite (DE) — mistura DE-10 (10% substituicao)'): 'scm',
    (3512, 'SHCC imprimivel 3D com diatomite (DE) — mistura DE-20 (20% substituicao)'): 'scm',
    (3512, 'SHCC imprimivel 3D com diatomite (DE) — mistura DE-30 (30% substituicao, pior mecanicamente)'): 'scm',
    (3529, 'argamassa de alta resistencia com 10% po de basalto residual (10BT)'): 'reciclado',
    (3529, 'argamassa de alta resistencia com 15% po de basalto residual (15BT) - mistura otima'): 'reciclado',
    (3529, 'argamassa de alta resistencia com 20% po de basalto residual (20BT)'): 'reciclado',
    (3529, 'argamassa de alta resistencia com 25% po de basalto residual (25BT)'): 'reciclado',
    (3529, 'argamassa de alta resistencia com 5% po de basalto residual (5BT)'): 'reciclado',
    (3787, 'Concreto com ligante MgO reativo (RMC), cura R90T60C10 (90% UR, 60C, 10% CO2 - melhor desempenho)'): 'ligantes',
    (3787, 'Concreto com ligante dolomita calcinada a 800C (D800), cura R90T30C10 (90% UR, 30C, 10% CO2 - melhor desempenho)'): 'ligantes',
    (3818, 'CR-ECC (Engineered Cementitious Composite, chromium resin, 40% subst. areia, impressao 3D)'): 'reciclado',
    (2720, 'Betao convencional, referencia (w/b=0,4, 0% cinza MSWI)'): 'opc',
    (2720, 'Betao com cinza MSWI (w/b=0,4, 20%)'): 'scm',
    (3818, 'IBA-ECC (Engineered Cementitious Composite, incineration bottom ash, 40% subst. areia, impressao 3D)'): 'reciclado',
    (3818, 'LP-ECC (Engineered Cementitious Composite, lignina/50% vol. fibra PE, impressao 3D)'): 'biobase',
    (3828, 'HPC com 50% borracha de pneu (substituindo areia de silica)'): 'reciclado',
    (3864, 'TR1: concreto autoadensavel (SCC) com 0% de agregado fino substituido por cinza de lagoa (pond ash)'): 'reciclado',
    (3864, 'TR2: concreto autoadensavel (SCC) com 10% de agregado fino substituido por cinza de lagoa (pond ash)'): 'reciclado',
    (3864, 'TR3: concreto autoadensavel (SCC) com 15% de agregado fino substituido por cinza de lagoa (pond ash)'): 'reciclado',
    (3864, 'TR4: concreto autoadensavel (SCC) com 20% de agregado fino substituido por cinza de lagoa (pond ash)'): 'reciclado',
    (3864, 'TR5: concreto autoadensavel (SCC) com 25% de agregado fino substituido por cinza de lagoa (pond ash)'): 'reciclado',
    (3864, 'TR6: concreto autoadensavel (SCC) com 30% de agregado fino substituido por cinza de lagoa (pond ash)'): 'reciclado',
    (4086, 'Argamassa traco 10R (traco rico, 10% de po de agata em substituicao ao cimento, em massa)'): 'scm',
    (4090, 'Concreto com residuo de borracha de pneu para laje trelicada (capa CPII-Z32 + sapatas CPV-ARI) - Ilha Solteira, Brasil'): 'reciclado',
    (4160, 'Argamassa de alta resistencia (HSM) com 30% CWP (residuo de po de ceramica) moido 15 min -- GT15CWP30, melhor desempenho mecanico do estudo'): 'reciclado',
    (4160, 'Argamassa de alta resistencia (HSM), mistura controlo 0% CWP (residuo de po de ceramica)'): 'reciclado',
    (4244, 'Concreto com 20% de substituicao de cimento por po de vidro moido (GP2-20)'): 'reciclado',
    (4251, 'Concreto com cinza de casca de arroz (rice husk ash, RHA) 10% substituicao de agregado fino'): 'reciclado',
    (4292, 'Concreto estrutural (portais e fundacoes de portico industrial), classe de projeto C30/37 (EN 206)'): 'reciclado',
    (4328, 'Concreto reforcado com Fibra de sisal'): 'biobase',
    (4408, 'concreto autoadensavel (SCC) M1 - 0% substituicao de cimento por po de residuo de tijolo ceramico (CBWP)'): 'reciclado',
    (4408, 'concreto autoadensavel (SCC) M2 - 12.5% substituicao de cimento por po de residuo de tijolo ceramico (CBWP)'): 'reciclado',
    (4408, 'concreto autoadensavel (SCC) M3 - 25% substituicao de cimento por po de residuo de tijolo ceramico (CBWP)'): 'reciclado',
    (4408, 'concreto autoadensavel (SCC) M4 - 37.5% substituicao de cimento por po de residuo de tijolo ceramico (CBWP)'): 'reciclado',
    (4408, 'concreto autoadensavel (SCC) M5 - 50% substituicao de cimento por po de residuo de tijolo ceramico (CBWP)'): 'reciclado',
    (4500, 'Argamassa CEM I + GP (po de vidro, 50% substituicao de cimento em massa)'): 'scm',
    (4500, 'Argamassa CEM III + GP (po de vidro, 50% substituicao de cimento em massa)'): 'scm',
    (4557, 'Concreto com po de calcario como substituto parcial de cimento - mistura Alpha-10'): 'scm',
    (4557, 'Concreto com po de calcario como substituto parcial de cimento - mistura Alpha-20'): 'scm',
    (4557, 'Concreto com po de calcario como substituto parcial de cimento - mistura Alpha-30'): 'scm',
    (4557, 'Concreto com po de calcario como substituto parcial de cimento - mistura Beta-10'): 'scm',
    (4557, 'Concreto com po de calcario como substituto parcial de cimento - mistura Beta-20'): 'scm',
    (4557, 'Concreto com po de calcario como substituto parcial de cimento - mistura Beta-30'): 'scm',
    (4557, 'Concreto com po de calcario como substituto parcial de cimento - mistura Control'): 'scm',
    (4557, 'Concreto com po de calcario como substituto parcial de cimento - mistura Gamma-10'): 'scm',
    (4557, 'Concreto com po de calcario como substituto parcial de cimento - mistura Gamma-20'): 'scm',
    (4557, 'Concreto com po de calcario como substituto parcial de cimento - mistura Gamma-30'): 'scm',
    (4580, 'Concreto CON-fix-SLUMP-0-10, FBA0 (substituicao de areia por cinza de fundo de forno FBA)'): 'reciclado',
    (4580, 'Concreto CON-fix-SLUMP-0-10, FBA100 (substituicao de areia por cinza de fundo de forno FBA)'): 'reciclado',
    (4580, 'Concreto CON-fix-SLUMP-0-10, FBA30 (substituicao de areia por cinza de fundo de forno FBA)'): 'reciclado',
    (4580, 'Concreto CON-fix-SLUMP-0-10, FBA50 (substituicao de areia por cinza de fundo de forno FBA)'): 'reciclado',
    (4580, 'Concreto CON-fix-SLUMP-0-10, FBA70 (substituicao de areia por cinza de fundo de forno FBA)'): 'reciclado',
    (4580, 'Concreto CON-fix-SLUMP-30-60, FBA0 (substituicao de areia por cinza de fundo de forno FBA)'): 'reciclado',
    (4580, 'Concreto CON-fix-SLUMP-30-60, FBA100 (substituicao de areia por cinza de fundo de forno FBA)'): 'reciclado',
    (4580, 'Concreto CON-fix-SLUMP-30-60, FBA30 (substituicao de areia por cinza de fundo de forno FBA)'): 'reciclado',
    (4580, 'Concreto CON-fix-SLUMP-30-60, FBA50 (substituicao de areia por cinza de fundo de forno FBA)'): 'reciclado',
    (4580, 'Concreto CON-fix-SLUMP-30-60, FBA70 (substituicao de areia por cinza de fundo de forno FBA)'): 'reciclado',
    (4580, 'Concreto CON-fix-W/C-0.45, FBA0 (substituicao de areia por cinza de fundo de forno FBA)'): 'reciclado',
    (4580, 'Concreto CON-fix-W/C-0.45, FBA100 (substituicao de areia por cinza de fundo de forno FBA)'): 'reciclado',
    (4580, 'Concreto CON-fix-W/C-0.45, FBA30 (substituicao de areia por cinza de fundo de forno FBA)'): 'reciclado',
    (4580, 'Concreto CON-fix-W/C-0.45, FBA50 (substituicao de areia por cinza de fundo de forno FBA)'): 'reciclado',
    (4580, 'Concreto CON-fix-W/C-0.45, FBA70 (substituicao de areia por cinza de fundo de forno FBA)'): 'reciclado',
    (4580, 'Concreto CON-fix-W/C-0.55, FBA0 (substituicao de areia por cinza de fundo de forno FBA)'): 'reciclado',
    (4580, 'Concreto CON-fix-W/C-0.55, FBA100 (substituicao de areia por cinza de fundo de forno FBA)'): 'reciclado',
    (4580, 'Concreto CON-fix-W/C-0.55, FBA30 (substituicao de areia por cinza de fundo de forno FBA)'): 'reciclado',
    (4580, 'Concreto CON-fix-W/C-0.55, FBA50 (substituicao de areia por cinza de fundo de forno FBA)'): 'reciclado',
    (4580, 'Concreto CON-fix-W/C-0.55, FBA70 (substituicao de areia por cinza de fundo de forno FBA)'): 'reciclado',
    (4584, 'Laje maciça ordinária (ORC) - Caso 1 (pavimento acima do solo)'): 'opc',
    (4584, 'Laje maciça ordinária (ORC) - Caso 2 (estacionamento subterrâneo)'): 'opc',
    (4584, 'Laje vazada (VDS) - Caso 1 (pavimento acima do solo)'): 'opc',
    (4584, 'Laje vazada (VDS) - Caso 2 (estacionamento subterrâneo)'): 'opc',
    (4605, 'Muro de contenção RC com contrafortes - Analyses 2 e 3 (fator Paya et al.)'): 'opc',
    (4605, 'Muro de contenção RC com contrafortes - Analysis 1 (fator Yeo & Potra)'): 'opc',
    (4671, '3DPSCC com 100% de particulas de borracha (RP-100)'): 'reciclado',
    (4671, '3DPSCC com 20% de particulas de borracha (RP-20)'): 'reciclado',
    (4671, '3DPSCC com 40% de particulas de borracha (RP-40)'): 'reciclado',
    (4671, '3DPSCC com 60% de particulas de borracha (RP-60)'): 'reciclado',
    (4671, '3DPSCC com 80% de particulas de borracha (RP-80)'): 'reciclado',
    (4671, 'Controlo (0% substituicao de areia por particulas de borracha, RP-0)'): 'reciclado',
    (4689, 'Concreto CTr-c20-25 (agregado natural + 20% TDA - agregado derivado de pneu, 5-10mm)'): 'reciclado',
    (4724, 'Concreto REF com agregado natural (NAC1, w/c=0.50, Caso 1)'): 'reciclado',
    (4724, 'Concreto com 100% RFA (RAC1-5, w/c=0.50, Caso 1)'): 'reciclado',
    (4750, 'Concreto W2 (111.11 kg/m3 de vidro de carro triturado)'): 'reciclado',
    (4753, 'Painel de fachada CRC (reforcado com grelha de fibra de carbono), variante F2C1 (melhor caso), cenario 50% reciclagem'): 'opc',
    (4753, 'Painel de fachada CRC, variante F1C3 (pior caso), cenario 50% reciclagem'): 'opc',
    (4753, 'Painel de fachada SRC (reforcado com aco), variante SRC 2.2 (aco de alto-forno primario)'): 'opc',
    (4768, 'Pavement Quality Concrete (PQC), mix design indiano M20, camada de rolamento do pavimento rigido (MDR)'): 'concreto_armado',  # 2026-09-27: total do sistema com aco (Tab.11)
    (4800, 'Ligante BG - gesso (Knauf BAUGIPS hemihydrate)'): 'ligantes',
    (4800, 'Ligante CSA - cimento sulfoaluminato de calcio (calcium sulphoaluminate)'): 'ligantes',
    (4800, 'Ligante MOC - cimento oxicloreto de magnesio (magnesium oxychloride cement)'): 'ligantes',
    (4800, 'Ligante MPC - cimento fosfato de magnesio (magnesium phosphate cement)'): 'ligantes',
    (4820, 'Edificio alto hibrido madeira/GLT (projeto original, caso de estudo Mjostarnet), classe GL30h (fc,0,k)'): 'biobase',
    # achado CI_MPA 13 (2026-09-26): material reescrito, mesma familia (madeira glulam = bio-base)
    (4820, 'Madeira lamelada-colada (glulam) GL30h, estrutura do edificio alto Mjostarnet (projeto original, caso de estudo) - familia madeira'): 'biobase',
    (4855, 'concreto C25 com agregado natural (NAC) - comparativo do mesmo estudo'): 'reciclado',
    (4879, 'pasta ativada alcalinamente FA/GBFS-RN (70/30, ativador cinza de casca de arroz + NaOH) - 28 dias'): 'ligantes',
    (4879, 'pasta ativada alcalinamente FA/GBFS-RN (70/30, ativador cinza de casca de arroz + NaOH) - 360 dias'): 'ligantes',
    (4927, 'concreto de cimento — modelo estatístico global de carbonatação/captação de CO2 (1930-2019), classes C15/C16-C23/C24-C35/>C35 usadas como bins'): 'scm',
    (3818, 'RC (concreto armado convencional, referencia com armadura, impressao 3D vs. betonagem)'): 'concreto_armado',
    # 2026-09-26: duas misturas do mesmo estudo (10% borracha de pneu + fio de arame residual) caiam em
    # 'outros' e partiam o export -- mesma familia da mistura de 50% borracha ja em OVERRIDE (pneu = reciclado)
    (3828, 'HPC com 0% fio de arame residual (base 10% borracha)'): 'reciclado',
    (3828, 'HPC com 3% fio de arame residual (base 10% borracha, maximo do artigo)'): 'reciclado',
    # LYRA 2023i (2026-09-26): argamassa de referencia sem substituicao -- o titulo (cinzas/pozolanas) arrastava-a para scm
    (2847, 'Argamassa de referencia (cimento Portland + areia)'): 'opc',
    # KONTRA (2026-09-26, decisao Kie): total do sistema RC normalizado por m3 de concreto, inclui aco
    (4931, 'Parede de contraventamento (shear wall) de betao armado (RC), sistema lateral de edificio de ensaio a escala real de 6 pisos (NHERI TallWood, Seattle); ACI 318-19/ASCE 7-16, elementos de fronteira reforcados nos 2 primeiros pisos'): 'concreto_armado',
    # achado CI_MPA 14 (2026-09-26): total do sistema estrutural inclui aco CA-50 (precedente KONTRA)
    (5040, 'Concreto armado 25MPa - sistemas Fundacao+Superestrutura de edificio real (UFMT, 4.347,57 m2) - familia concreto armado'): 'concreto_armado',
    # LARSEN 3911 (2026-09-26, revisao suspeitos CO2, decisao Kie): totais das pontes incluem aco/fibra/transporte
    (3911, 'Concreto de resistência normal NSC — C30/37 (ponte pedonal, Noruega)'): 'concreto_armado',
    (3911, 'Concreto UHPC (Ultra High Performance Concrete, ponte pedonal, Noruega)'): 'concreto_armado',
    # revisao suspeitos CO2 (2026-09-27): totais de sistema com armadura -> concreto_armado
    (2891, 'Concreto convencional REF (C30/37, moldado in-situ)'): 'concreto_armado',
    (2891, 'Concreto TRS (laje/elemento pre-fabricado, C35/45)'): 'concreto_armado',
    (3882, 'Variante 1: laje de parking house, betao C35/45 (Praga, Republica Checa)'): 'concreto_armado',
    (3882, 'Variante 2A: laje de parking house, betao C90/105 (laje mais fina) (Praga, Republica Checa)'): 'concreto_armado',
    (3882, 'Variante 2B: laje de parking house, betao C90/105 (menos armadura) (Praga, Republica Checa)'): 'concreto_armado',
    (4007, 'Concreto 35 MPa (assumido) em sistema misto madeira-concreto (TCC), CLT-315 + laje de concreto 100mm'): 'concreto_armado',
    # leitura integral dos Elegiveis sem par (2026-09-27): totais de sistema com armadura
    (2687, 'P-RC (concreto armado pos-tensionado, Method 1, classes C30/37 e C20/25) - baseline/demolicao e reconstrucao'): 'concreto_armado',
    (2693, 'Viga BFRP pre-tensionada, 1200x200x200mm (Beams 1.1/1.2)'): 'concreto_armado',
    (2693, 'Viga BFRP pre-tensionada, 2000x200x200mm (Beams 2.1/2.2/2.3)'): 'concreto_armado',
    (2693, 'Viga BFRP pre-tensionada, 2700x200x200mm (Beams 3.1/3.2)'): 'concreto_armado',
    (2693, 'Viga BFRP pre-tensionada, 3860x200x200mm (Beams 4.1/4.2)'): 'concreto_armado',
    (2693, 'Viga com armadura de aco convencional, 1250x200x189mm (Beams 5.1/5.2/5.3) - comparador simetrico'): 'concreto_armado',
    (2739, 'Tabuleiro de ponte PCSS (pre-esforcado, laje maciça, HP-40)'): 'concreto_armado',
    (2739, 'Tabuleiro de ponte PCLS (pre-esforcado, laje aligeirada, HP-40)'): 'concreto_armado',
    (2739, 'Tabuleiro de ponte PCBG (vigas pre-esforcadas, HP-40)'): 'concreto_armado',
    (2751, 'Encontros e pilares (abutments and piers) em betao armado C30/37 da ponte madeira-betao WCB (elemento so de betao armado: 65,160 m3 betao + 7,2 t de armadura B500B)'): 'concreto_armado',
    (2751, 'Vigas de coroamento (capping beam) em betao armado C30/37, ponte WCB (3,507 m3 betao + 0,172 t armadura)'): 'concreto_armado',
    (2751, 'Muros de testa (abutment wall) em betao armado C30/37, ponte WCB (3,163 m3 betao + 0,047 t armadura)'): 'concreto_armado',
    (2769, 'Concreto para muro de contencao tipo cantilever (consola) - ACV comparativa de muros de 4m altura'): 'concreto_armado',
    (2828, 'Concreto para edificio de portico (4 pavimentos) - esquema inicial de projeto, otimizacao multi-objetivo emissao/custo por harmony search'): 'concreto_armado',
    (3117, 'Concreto de encamisamento (RC jacketing) para reforco sismico de pilares - edificio de 4 pisos'): 'concreto_armado',
    (3117, 'Concreto de encamisamento (RC jacketing) para reforco sismico de pilares - edificio de 7 pisos'): 'concreto_armado',
    (3117, 'encamisamento de betao armado (RC) de pilar - edificio 10 pisos (3a linha do dossie, sheet_row provavelmente 319 - nao vista no lote)'): 'concreto_armado',
    (3301, 'Viga BA pre-fabricada L=8 m, 0,3x0,6 m, fck=35, desenho de menor armadura (EHE-08, LL1=3 kN/m, Vs~6,4e-3)'): 'concreto_armado',
    (3301, 'Viga BA pre-fabricada L=8 m, 0,3x0,6 m, fck=35, desenho de maior armadura (MC-2010, LL1=15 kN/m, Vs~20e-3)'): 'concreto_armado',
    (3409, 'concreto (tabuleiro de ponte, CD — comparacao com tabuleiro de aluminio AD)'): 'concreto_armado',
    (3424, 'Concreto C35/45 (Wall_Ref, parede de referencia de betao armado sem SAP)'): 'concreto_armado',
    (3424, 'Concreto C30/37 (Wall_SAP, parede de betao armado com polimero superabsorvente)'): 'concreto_armado',
    (3449, 'Laje de concreto armado convencional macica (comparador de referencia, C30/37)'): 'concreto_armado',
    (3449, 'Laje macica de betao armado convencional C30/37, vao 6 m, 20 cm (caso de estudo, Genebra)'): 'concreto_armado',
    (3653, 'concreto com vidro reciclado (agregado parcial) - pavimento'): 'concreto_armado',
    (3653, 'pavimento de betao continuamente armado, sem reciclados, 150 mm'): 'concreto_armado',
    (3653, 'pavimento de betao armado com 20% RCG (vidro reciclado) na areia, 100 mm'): 'concreto_armado',
    (3653, 'pavimento de betao armado com 20% RCG, 150 mm'): 'concreto_armado',
    (3653, 'pavimento de betao armado com 100% aco reciclado (RCS), 100 mm'): 'concreto_armado',
    (3653, 'pavimento de betao armado com 100% RCS, 150 mm'): 'concreto_armado',
    (3653, 'pavimento de betao armado com 20% RCG + 100% RCS, 100 mm'): 'concreto_armado',
    (3653, 'pavimento de betao armado com 20% RCG + 100% RCS, 150 mm'): 'concreto_armado',
    (4298, 'Concreto pre-moldado (precast) para painel estrutural de piso, 5000 psi, 0% cinza volante, reforco 28 kg/m3'): 'concreto_armado',
    (4298, 'Laje/painel de piso de betao armado - precast 100 mm, 5000 psi, 25% FA, arm. 28 kg/m3'): 'concreto_armado',
    (4298, 'Laje/painel de piso de betao armado - precast 100 mm, 5000 psi, 30% FA, arm. 28 kg/m3'): 'concreto_armado',
    (4298, 'Laje/painel de piso de betao armado - precast 100 mm, 5000 psi, 50% FA, arm. 28 kg/m3'): 'concreto_armado',
    (4298, 'Laje/painel de piso de betao armado - precast 125 mm, 5000 psi, 0% FA, arm. 28 kg/m3'): 'concreto_armado',
    (4298, 'Laje/painel de piso de betao armado - precast 125 mm, 5000 psi, 25% FA, arm. 28 kg/m3'): 'concreto_armado',
    (4298, 'Laje/painel de piso de betao armado - precast 125 mm, 5000 psi, 30% FA, arm. 28 kg/m3'): 'concreto_armado',
    (4298, 'Laje/painel de piso de betao armado - precast 125 mm, 5000 psi, 50% FA, arm. 28 kg/m3'): 'concreto_armado',
    (4298, 'Concreto betonado in loco (cast-in-place) para piso, 3000 psi, 0% cinza volante, reforco baixo 43.62 kg/m3 — caso base/referencia do estudo'): 'concreto_armado',
    (4298, 'Laje/painel de piso de betao armado - cast-in-place 100 mm, 3000 psi, 25% FA, arm. 43,62'): 'concreto_armado',
    (4298, 'Laje/painel de piso de betao armado - cast-in-place 100 mm, 3000 psi, 30% FA, arm. 43,62'): 'concreto_armado',
    (4298, 'Laje/painel de piso de betao armado - cast-in-place 100 mm, 3000 psi, 50% FA, arm. 43,62'): 'concreto_armado',
    (4298, 'Laje/painel de piso de betao armado - cast-in-place 100 mm, 3000 psi, 50% FA, arm. moderada 87,24'): 'concreto_armado',
    (4298, 'Laje/painel de piso de betao armado - cast-in-place 100 mm, 3000 psi, 50% FA, arm. alta 130,86'): 'concreto_armado',
    (4298, 'Concreto betonado in loco (cast-in-place) para piso, 5000 psi, 0% cinza volante, reforco baixo 44.40 kg/m3'): 'concreto_armado',
    (4298, 'Laje/painel de piso de betao armado - cast-in-place 100 mm, 5000 psi, 25% FA, arm. 44,40'): 'concreto_armado',
    (4298, 'Laje/painel de piso de betao armado - cast-in-place 100 mm, 5000 psi, 30% FA, arm. 44,40'): 'concreto_armado',
    (4298, 'Laje/painel de piso de betao armado - cast-in-place 100 mm, 5000 psi, 50% FA, arm. 44,40'): 'concreto_armado',
    (4298, 'Laje/painel de piso de betao armado - cast-in-place 100 mm, 5000 psi, 50% FA, arm. moderada 88,80'): 'concreto_armado',
    (4298, 'Laje/painel de piso de betao armado - cast-in-place 100 mm, 5000 psi, 50% FA, arm. alta 133,2'): 'concreto_armado',
    (4349, 'concreto (sistema estrutural completo do edificio Bakers Place, classes de projeto por pavimento/elemento)'): 'concreto_armado',
    (4498, 'Concreto referencia com agregado natural (NAC IA)'): 'concreto_armado',
    (4498, 'Concreto com agregado fino reciclado de alvenaria (fRMAC IA)'): 'concreto_armado',
    (4498, 'Concreto com agregado fino reciclado de concreto (fRCAC1 IA)'): 'concreto_armado',
    (4498, 'Concreto referencia com agregado natural (NAC IIA) - alta dosagem'): 'concreto_armado',
    (4498, 'Concreto com agregado fino reciclado de alvenaria (fRMAC IIA) - alta dosagem'): 'concreto_armado',
    (4498, 'Concreto com agregado fino reciclado de concreto (fRCAC1 IIA) - alta dosagem'): 'concreto_armado',
    (4560, 'Mesma ponte - so fase de fabrico (materiais, cradle-to-gate)'): 'concreto_armado',
    (4789, 'Concreto estrutural (colunas/vigas, piso, fundacao, paredes interiores) do edificio mid-rise reforcado vs MTC — Melbourne, Australia'): 'concreto_armado',
    (5018, 'Estrutura de concreto armado (ECA) vs light steel framing (ELSF)'): 'concreto_armado',
    (5041, 'Concreto armado classe C25'): 'concreto_armado',
    (5041, 'estrutura de betao armado do edificio (9 pav.), classe C30, cimento CP III'): 'concreto_armado',
    (5041, 'estrutura de betao armado do edificio (9 pav.), classe C35, cimento CP III'): 'concreto_armado',
    (5041, 'Concreto armado classe C40 (melhor desempenho)'): 'concreto_armado',
    (5041, 'estrutura de betao armado do edificio (9 pav.), classe C45, cimento CP III'): 'concreto_armado',
    (5041, 'Concreto armado classe C50'): 'concreto_armado',
    # figuras vistas em PDF reduzido (2026-09-27): SAHMENKO GCP = ligante gesso-cimento-pozolana; LV pasta com 30% SSA
    (4455, 'argamassa de referência PC mortar (cimento Portland + areia + fíler calcário) para impressão 3D'): 'opc',
    (4455, 'composto GCP1 (gesso-cimento-pozolana, 100% gesso de construção BG) para 3DCP'): 'ligantes',
    (4455, 'composto GCP2 (gesso-cimento-pozolana, 50% BG + 50% gesso reciclado RG) para 3DCP'): 'ligantes',
    (4455, 'composto GCP3 (gesso-cimento-pozolana, 100% gesso reciclado RG) para 3DCP'): 'ligantes',
    (4455, 'composto GCP4 (gesso-cimento-pozolana, 100% fosfogesso PG) para 3DCP'): 'ligantes',
    (4455, 'composto GCP5 (gesso-cimento-pozolana, 50% RG + 50% PG) para 3DCP'): 'ligantes',
    (4500, 'Argamassa CEM I 52.5N (referencia, sem substituicao)'): 'opc',
    (4516, 'Pasta cimento com 30% SSA calcinada a 800C/2h moida 1min (P-800/2/1) - otimo'): 'scm',
    (4516, 'Pasta SSC 30% SSA 800C/2h, moagem 10 min (P-800/2/10) - optimo TOPSIS/radar'): 'scm',
    (4516, 'Pasta de referencia P-20/0/1 (lama seca ao ar, 30%)'): 'scm',
    # STUDZINSKI 4792 (decisao da Kie 2026-09-27): via so-fundacao, betao C35/45 + armadura
    (4792, 'Fundacao em 4 sapatas isoladas F2 (2,0x2,0x0,6 m), betao C35/45 + armadura, materiais de emissao media (A1-A3)'): 'concreto_armado',
    (4792, 'Fundacao em 4 sapatas isoladas F1 (1,5x1,5x0,6 m), C35/45 + armadura (sistema J)'): 'concreto_armado',
    (4792, 'Fundacao em placa PL1 (7,0x7,0x0,5 m), C35/45 + armadura (sistema M)'): 'concreto_armado',
    (4792, 'Fundacao em placa PL2 (7,0x7,0x0,7 m), C35/45 + armadura (sistema N)'): 'concreto_armado',
    # leitura integral dos Elegiveis sem par (2026-09-27): materiais que o regex nao apanha
    (4033, 'D5-P5: argamassa de cimento ternaria com 5% lama de tingimento calcinada (DS) + 5% lama de fabrico de papel (PS)'): 'scm',
    (4033, 'D10-P5'): 'scm',
    (4033, 'D15-P5'): 'scm',
    (4033, 'D10-P10'): 'scm',
    (4033, 'D20-P10'): 'scm',
    (4033, 'D10-P15'): 'scm',
    (4505, 'CFG12_MIN - fibra de vidro 12 mm 2,83 kg/m3'): 'opc',
    (4505, 'CFG36_MIN - fibra de vidro 36 mm 2,83 kg/m3'): 'opc',
    (4505, 'CFP_MIN - fibra de poliolefina 2,78 kg/m3'): 'opc',
}


ALKALI = (r'geopolim|geopolym|alcali[- ]?a[ct]{1,2}iv|alcalino-?a[ct]{1,2}iv|alcalinamente|alkali[- ]?a[ct]{1,2}iv|ativad[oa]s? por alcali|'
          r'\baam\b|\baas\b|\baac\b|\baab\b|\baacm\b|aafa|\bgpc\b')
PORTLAND_EXPLICITO = r'\bopcc?\b|portland|\bcem [iv]|\bcp ?i|convencional|conventional'


def _fold(s):
    s = unicodedata.normalize('NFKD', s or '')
    return ''.join(c for c in s if not unicodedata.combining(c)).lower()


def _carregar_revarredura():
    try:
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lotes_familia', 'familias_revarredura.json'),
                  encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


# 2026-10-04: revarredura das familias e do betao armado (43 lotes, leitura integral dos PDFs, regras D1-D8
# de metanalise/DECISOES_METANALISE.md). Tem precedencia sobre o OVERRIDE antigo e as regex.
FAMILIA_REVARREDURA = _carregar_revarredura()


def classify(row_id, material, titulo):
    rev = FAMILIA_REVARREDURA.get(f'{row_id}|{material}')
    if rev:
        return rev
    key = (row_id, material)
    if key in OVERRIDE:
        return OVERRIDE[key]
    # 2026-09-28: o traco Portland de referencia de um artigo sobre
    # geopolimero caia na familia 'geopolimero' so por causa do TITULO
    # (ex.: 2611 OPC-A, 2836 CC-CPI). Quando o proprio material se declara
    # Portland/OPC/convencional e nao tem marcador alcalino, classifica-se so
    # pelo material.
    m = _fold(material)
    if (titulo and not re.search(ALKALI, m) and re.search(PORTLAND_EXPLICITO, m)
            and re.search(ALKALI, _fold(titulo))):
        return classify(row_id, material, '')
    t = ((material or '') + ' ' + (titulo or '')).lower()
    # 2026-09-28: regex alcalino alargado (ALKALI, texto sem acentos) -- o
    # antigo falhava em 'alcali-activado', 'ativado por alcalis',
    # 'alcalinamente', 'geopolímero' com acento e siglas (tinha \bAAM\b em
    # maiusculas contra texto em minusculas, nunca casava).
    if re.search(ALKALI, _fold(t)):
        return 'geopolimero'
    # ligantes sem clinquer Portland que nao sao alcali-ativados
    if re.search(r'sulfoaluminat|\bkcsc\b|magnesi|\bm-s-h\b|belite-ye|\bbyc\b', m):
        return 'ligantes'
    if re.search(r'\buhpc\b|\buhpfrc\b|ultra[- ]high[- ]performance|ultra[- ]alta[- ]resist', t):
        return 'uhpc'
    if re.search(
        r'reciclad|recycled aggregate|\brca\b|residuo de construcao|'
        r'construction (and demolition )?waste|\brcd\b|debris aggregate|\bgcba\b|\bcba\b|'
        r'e-waste|residuo de mina|residuo de pa de turbina|'
        r'vidro (triturado|moido) como agregado|concreto existente reutilizado',
        t,
    ):
        return 'reciclado'
    if re.search(
        r'cinza volante|fly ash|escoria|slag|silica ativa|silica fume|metacaulim|metakaolin|'
        r'argila calcinada|calcined clay|pozolan|pozzolan|\blc3\b|\bscm\b|\bggbs\b|\bggbfs\b|'
        r'cinza co-queimada|co-fired ash|cinza de casca de arroz|rice husk ash|'
        r'residuo de po de ceramica|\bcwp\b|po de vidro|glass powder|palm oil clinker|\bpoc\b',
        t,
    ):
        return 'scm'
    # NAO ha mais fallback generico "alvenaria|masonry|tijolo" aqui -- revogado
    # 2026-09-08 (Kie: nenhum tijolo/bloco/paver/telha e moldavel conforme
    # projeto, falha o passo 1 do E1_moldavel; ver PROTOCOLO_CI_MPA e
    # CRITERIOS_E_NUANCES_RSL.md). Todo o material cujo produto final e
    # tijolo/bloco de alvenaria/paver/telha foi removido de dados_fck. As
    # unicas linhas que ainda mencionam "alvenaria"/"tijolo"/"masonry" no
    # texto sao concreto/grout legitimos que so citam alvenaria como
    # contexto/comparador (ex. "grout de alvenaria pre-fabricada", "edificio
    # com tijolo de barro") -- devem cair nos testes de OPC abaixo, nao
    # aqui. Se um caso genuino de alvenaria REAPARECER no futuro (nao
    # deveria, dada a regra), tratar por OVERRIDE explicito, nao por regex.
    # Referencia/OPC: nome explicito OU classe normativa de concreto convencional
    # (europeia C##/##, espanhola HA-##) OU descricao generica "concreto armado/estrutural"/
    # "betao"/"concreto"/"argamassa" -- a maioria dos concretos convencionais no banco
    # esta descrita assim, nao por "OPC"/"portland".
    if re.search(r'\bopc\b|portland|\breferencia\b|\bcontrole\b|\bcontrolo\b|convencional|conventional concrete', t):
        return 'opc'
    if re.search(r'\bc\d{2}\s*/?\s*\d{0,2}\b|\bha[- ]?\d{2}\b', t):
        return 'opc'
    if re.search(
        r'\bconcreto (armado|estrutural)\b|\bbetao\b|\bconcreto\b|\bbeton\b|'
        r'ready-?mix|usinado|pronto|pre-?fabricad|pre-?moldad|precast',
        t,
    ):
        return 'opc'
    if re.search(r'\bargamassa\b|\bmortar\b|\bpasta\b', t):
        return 'opc'
    return 'outros'


def tofloat(v):
    if v is None:
        return None
    if isinstance(v, (int, float)):
        return float(v)
    s = str(v).strip().replace(',', '.')
    m = re.search(r'-?\d+\.?\d*', s)
    return float(m.group()) if m else None


# --------------------------------------------------------------------------
# Classificacao de co2_unidade -- nativo (kg/m3 como publicado) vs derivado
# (convertido por nos) vs pendente (ainda na unidade original do estudo).
# Mesma logica da investigacao de 2026-09-08 (ver CO2_UNIDADE_PENDENTE.csv),
# agora vivendo aqui para nao precisar de manutencao manual a cada onda.

_M3_OK_PAT = re.compile(r'(kg\s*co2[\-\s]?e?q?\.?\s*/\s*m\s*3\b)|(/\s*m\^?3\b)|(por\s*metro\s*cubico)|(por\s*m3\b)')
# ARMADILHA (encontrada 2026-09-10, varredura "concreto armado disfarcado"):
# _M3_OK_PAT casa "por m3" mesmo dentro de uma NEGACAO explicita do autor da
# nota, tipo "NAO por m3" ou "NAO e CO2 por m3" -- 9 linhas (row_id 2683,
# 2684, 3328, 3102) estavam classificadas 'nativo'/m3 e CONTAMINANDO pairs
# apesar de o proprio texto dizer que nao e por m3. Checar negacao ANTES de
# confirmar m3.
#
# ARMADILHA Nº2 (mesma varredura): a negacao dispara falso-positivo quando o
# "nao e kg CO2/m3" esta ENTRE ASPAS -- convencao do vault para citar o texto
# ORIGINAL do artigo (ou do rotulo problematico ja corrigido), nao para
# descrever o estado atual da propria linha (ex. row_id 3178: "kg CO2-eq/m3
# [DERIVADO: multiplicacao do indice CII (...), explicitamente marcado no
# texto original como \"nao e kg CO2/m3 absoluto\") pelo fck...]" -- a unidade
# JA FOI corrigida para m3 genuino, a citacao entre aspas so explica o que
# tinha de errado ANTES da correcao). Retirar o conteudo entre aspas antes de
# procurar a negacao.
_ASPAS_PAT = re.compile(r'["“”].*?["“”]')
_NEGACAO_M3_PAT = re.compile(r'\bnao\b.{0,40}?\bm[\^]?3\b|\bnot\b.{0,40}?\bm[\^]?3\b')
# ARMADILHA Nº3 (encontrada 2026-09-11, lote 5): _JA_MPA_PAT tambem dispara
# falso-positivo quando o padrao "/(m3.MPa)" aparece dentro da nota
# [DERIVADO ...] entre colchetes que EXPLICA a conversao ja feita -- ex.
# row_id 3178: "kg CO2-eq/m3 [DERIVADO 2026-09-08: multiplicacao do indice
# CII (kg CO2-eq/(m3.MPa), explicitamente marcado no texto original como
# ...) pelo fck=21.94 MPa da propria linha]" -- a unidade REAL e a que vem
# ANTES do colchete ("kg CO2-eq/m3"), o "(m3.MPa)" dentro do colchete e so a
# descricao do indice ORIGINAL que foi multiplicado para chegar la. Retirar
# o conteudo entre colchetes antes de procurar _JA_MPA_PAT (mesmo tratamento
# que _ASPAS_PAT ja da a aspas para _NEGACAO_M3_PAT). Bug pre-existente
# desde a introducao do proprio padrao [DERIVADO], so agora corrigido.
_COLCHETES_PAT = re.compile(r'\[.*?\]')
# ARMADILHA Nº4 (encontrada 2026-09-11, lote 6): a mesma logica da nº3 vale
# tambem para _M3_OK_PAT (nao so para _JA_MPA_PAT) -- uma nota [ALERTA ...]
# ou [leitura visual ...] entre colchetes pode conter, incidentalmente, a
# palavra "nao" perto de "m3" (ex. row_id 3207: "[ALERTA - especie de gas
# nao declarada] kg/m3 ...") ou o texto "por m3" dentro de uma negacao de
# OUTRA unidade (ex. row_id 3406: "g CO2-eq/(MPa.ano) [indice normalizado
# ..., NAO e CO2 absoluto por m3]" -- aqui a unidade real, fora do
# colchete, nem e m3, e o "por m3" dentro do colchete so aparece porque a
# nota EXPLICA que a unidade nao e essa). Sem retirar o colchete antes de
# checar _M3_OK_PAT, a nota do 3207 acionava um falso-negativo por via da
# negacao (colchete continha "nao"+"m3" sem relacao gramatical nenhuma
# entre os dois), e simetricamente uma nota que citasse "/m3" dentro do
# colchete por outro motivo poderia acionar um falso-positivo. Verificado
# por diff completo do dataset: aplicar a mesma extracao do colchete tambem
# a _M3_OK_PAT corrige exactamente 4 linhas (921-923, 930) sem alterar mais
# nenhuma (em particular preserva 413-418, que continuam corretamente
# pendentes -- a unidade real deles, fora do colchete, nunca foi m3).
_JA_MPA_PAT = re.compile(r'/\s*\(?\s*m3\s*[\.\*]\s*mpa|/\s*mpa\b|\.\s*mpa\)|\bkg\s*co2[\-\s]?e?q?\.?\s*/\s*\(m3\s*mpa\)')
_TONELADA_PAT = re.compile(r'\btonelada|/\s*t\b|\btco2|/\s*ton\b|/\s*tonne|\bper\s+(metric\s+)?ton')
_KG_PAT = re.compile(r'/\s*kg\b')
_M2_PAT = re.compile(r'\bm2\b|\dm2\b|metro quadrado')
# 2026-10-13 (Kie: «"outro / nao classificado" nao e para ter nenhuma unidade de CO2 nao relatada»): as 48
# linhas que caiam em "outro" tinham todas unidade declarada que estas regex nao apanhavam -- por pilar/coluna/
# casa, por tonelada escrita «/ton», por MJ, indice por MPa.ano e totais sem divisor. Padroes acrescentados:
_ELEMENTO_EXTRA_PAT = re.compile(r'/\s*(pilar|coluna|column|casa|elemento|viga|laje|segmento|anel)\b|\bcasa\b')
_JA_MPA_EXTRA_PAT = re.compile(r'mpa\s*[\.\*\u00b7]\s*ano')
_ENERGIA_PAT = re.compile(r'/\s*mj\b')
_METRO_LINEAR_PAT = re.compile(r'metro linear|\bml\b|/\s*m\b(?!2|3)|\bkm\b')
_ELEMENTO_PAT = re.compile(
    r'\btotal\b|por peca|por unidade|por painel|por bloco|por viga|por pilar|por laje|'
    r'elemento estrutural|demonstrador|por edificio|por construcao|por segmento|por coluna|'
    r'whole element|per unit|per element|per piece'
)
_ESPECIME_PAT = re.compile(r'por corpo de prova|por especime|per specimen|por amostra')
_DERIVADO_TAG_PAT = re.compile(r'\[derivado\b', re.I)


def _norm(s):
    s = (s or '').strip().lower()
    s = unicodedata.normalize('NFKD', s)
    return ''.join(c for c in s if not unicodedata.combining(c))


# 2026-10-13: artigos cuja unidade nao se deixa classificar pelo texto -- categoria decidida pela leitura
# (motivo em co2_conversao de cada linha).
UNIDADE_OVERRIDE = {
    4718: 'sem_referencia',  # kg CO2-eq sem unidade de referencia impressa em lado nenhum (Tab.1 p.4)
    3215: 'm3',              # UF 1 m3; valor incoerente com o proprio inventario (10.300 kg/m3)
    5016: 'elemento',        # t CO2eq do edificio inteiro
    4037: 'elemento',        # UF = 1 painel pre-fabricado + gestao de 1 t de residuo
    2687: 'elemento',        # totais da intervencao na ponte (Fig.6)
}


def classify_unidade(u_raw):
    """Devolve (kind, cat). kind em {'nativo','derivado','pendente'}; cat so
    e informativo dentro de 'pendente' (a familia de unidade original).

    ARMADILHA (encontrada 2026-09-08, apos a 1a versao desta funcao): a tag
    '[DERIVADO]' e usada em dados_fck desde sessoes anteriores para marcar
    QUALQUER numero computado/derivado -- nao so os ja convertidos para
    kg/m3 (ex. '[DERIVADO] kg CO2-eq/t' continua sendo por TONELADA, so que
    calculado). Verificar primeiro se o texto confirma /m3 -- so DEPOIS
    perguntar se tambem carrega a tag, para decidir nativo vs derivado
    dentro do bucket m3. Checar a tag antes do padrao /m3 (como a v1 fazia)
    classificava esses ~44 casos como 'derivado:m3' por engano -- nao
    contaminava o grafico principal (a maioria tem co2_valor fora da faixa
    plausivel, filtrado por FCK_MIN/MAX+CO2_MIN/MAX), mas inflava o balde
    errado no grafico de transparencia de unidades."""
    u = _norm(u_raw)
    if not u:
        return 'nativo', 'm3'  # legado: linhas antigas sem co2_unidade preenchido, kg/m3 implicito
    u_sem_colchetes = _COLCHETES_PAT.sub(' ', u)
    u_sem_aspas_colchetes = _ASPAS_PAT.sub(' ', u_sem_colchetes)
    if _M3_OK_PAT.search(u_sem_colchetes) and not _JA_MPA_PAT.search(u_sem_colchetes) and not _NEGACAO_M3_PAT.search(u_sem_aspas_colchetes):
        return ('derivado', 'm3') if _DERIVADO_TAG_PAT.search(u) else ('nativo', 'm3')
    if _JA_MPA_PAT.search(u_sem_colchetes) or _JA_MPA_EXTRA_PAT.search(u):
        return 'pendente', 'ja_mpa'
    if _ELEMENTO_EXTRA_PAT.search(u):
        return 'pendente', 'elemento'
    if _ENERGIA_PAT.search(u):
        return 'pendente', 'energia'
    if _TONELADA_PAT.search(u):
        return 'pendente', 'tonelada'
    if _KG_PAT.search(u):
        return 'pendente', 'kg'
    if _M2_PAT.search(u):
        return 'pendente', 'm2'
    if _METRO_LINEAR_PAT.search(u):
        return 'pendente', 'metro_linear'
    if _ELEMENTO_PAT.search(u):
        return 'pendente', 'elemento'
    if _ESPECIME_PAT.search(u):
        return 'pendente', 'especime'
    if '/' not in u_sem_colchetes and re.search(r'co2', u_sem_colchetes):
        # kg CO2-eq sem divisor: total do sistema/cenario estudado (a unidade funcional
        # vem descrita noutra coluna ou e o proprio objecto do estudo)
        return 'pendente', 'total'
    return 'pendente', 'outro'


# --------------------------------------------------------------------------
# Citacao curta (autores+ano -> "Sobrenome et al., Ano") para o forest plot
# por estudo dentro de cada familia (pedido da Kie, 2026-09-12). O campo
# dados_fck.autores nao segue um formato unico -- amostrado sobre as 585
# variantes distintas em uso ate 2026-09-12, aparecem pelo menos 4 padroes:
# "Sobrenome, N.; Sobrenome, N." (';'), "Sobrenome, Nome and Sobrenome, Nome"
# (separador bibtex ' and '), listas soltas de sobrenomes sem nome proprio
# separadas so por virgula (ex. "Yoris-Nobile, Lizasoain-Arteaga, ..."), e
# valores legados que ja guardam a citacao pronta (ex. "Taherkhani et al.,
# 2023"). A heuristica abaixo cobre os quatro casos sem tentar ser perfeita
# -- e um rotulo de UI (hover/expand), nao um identificador citavel.
#
# ARMADILHA (encontrada 2026-09-12, checagem visual do forest plot recem-
# criado): o formato bibtex " and " tambem carrega, ocasionalmente, um
# sobrenome composto protegido entre chavetas -- convencao do bibtex para
# impedir que o normalizador de citacoes quebre um sobrenome de mais de uma
# palavra (ex. "Samuvel {Raj R}", "Nele {De Belie}", "Natalia {Pires
# Martins}"). Sem tratar isso, surname_of() pegava so a ULTIMA palavra do
# nome completo (ex. "R}", com a chaveta a mais) em vez do sobrenome real.
# O conteudo entre chavetas, quando existe, E o sobrenome -- usar
# directamente, nunca dividir por espaco dentro dele.
_BRACE_SURNAME_PAT = re.compile(r'\{([^{}]+)\}')


def surname_of(tok):
    tok = tok.strip()
    brace = _BRACE_SURNAME_PAT.findall(tok)
    if brace:
        surname = brace[-1].strip()
    elif ',' in tok:
        surname = tok.split(',', 1)[0].strip()
    else:
        parts = tok.split()
        surname = parts[-1] if parts else tok
    # defesa contra erro de capitalizacao na propria planilha (ex. "Jing
    # zhang" em vez de "Jing Zhang") -- nao mexe em nomes ja bem formados.
    return surname[:1].upper() + surname[1:] if surname else surname


def _finish_label(first_surname, n_authors, has_et_al, ano, second_surname=None):
    if n_authors == 1:
        label = first_surname + (' et al.' if has_et_al else '')
    elif n_authors == 2 and not has_et_al and second_surname:
        label = first_surname + ' & ' + second_surname
    else:
        label = first_surname + ' et al.'
    ano_f = tofloat(ano)
    ano_s = str(int(ano_f)) if ano_f is not None else ''
    return (label + ', ' + ano_s) if ano_s else label


def short_label(autores, ano):
    if not autores:
        return None
    s = str(autores).strip()
    if not s:
        return None
    has_et_al = bool(re.search(r'et\s*al\.?\s*$', s, re.I))
    s = re.sub(r'\s*et\s*al\.?\s*$', '', s, flags=re.I).strip().rstrip(';,').strip()
    if not s:
        return None
    if re.search(r'\s+and\s+', s, re.I):
        tokens = re.split(r'\s+and\s+', s, flags=re.I)
    elif ';' in s:
        tokens = s.split(';')
    elif s.count(',') > 1:
        # lista solta de sobrenomes sem nome proprio -- cada token JA e um
        # sobrenome isolado, nao um par "Sobrenome, Nome" para desmembrar.
        tokens = [t.strip() for t in s.split(',') if t.strip()]
        return _finish_label(surname_of(tokens[0]), len(tokens), has_et_al, ano) if tokens else None
    else:
        tokens = [s]
    tokens = [t.strip() for t in tokens if t.strip()]
    if not tokens:
        return None
    n_authors = len(tokens)
    second_surname = surname_of(tokens[1]) if n_authors == 2 else None
    return _finish_label(surname_of(tokens[0]), n_authors, has_et_al, ano, second_surname)


def main():
    wb = openpyxl.load_workbook(BASE)
    ws = wb['dados_fck']
    # 2026-09-26: so entram artigos com status_triagem=Elegivel em
    # articles_final.xlsx (linha = row_id). Sem este filtro, 39 pares de
    # artigos ja rejeitados (6 da regra E2 de 2026-09-21 e 4 da Etapa 3 de
    # 2026-09-26) continuavam no grafico, porque as linhas de dados_fck sao
    # mantidas por rastreabilidade quando um artigo sai do funil.
    status = {}
    af = openpyxl.load_workbook('articles_final.xlsx', read_only=True)['Articles']
    for i, row in enumerate(af.iter_rows(min_row=2, max_col=20, values_only=True), start=2):
        status[i] = row[19]

    compact = []
    excluded = []
    unit_counts = {}  # (kind, cat) -> n
    for r in range(2, ws.max_row + 1):
        row_id = ws.cell(r, 1).value
        titulo = ws.cell(r, 3).value
        autores = ws.cell(r, 4).value
        ano = ws.cell(r, 5).value
        material = ws.cell(r, 7).value
        fck = tofloat(ws.cell(r, 8).value)
        co2 = tofloat(ws.cell(r, 14).value)
        unidade = ws.cell(r, 15).value
        # 2026-09-26 (Kie): a base de TODOS os graficos de emissoes passa a ser
        # a coluna co2_kg_m3 (col 37) -- resultado ja convertido, com o dado
        # original, o local e o metodo de conversao em colunas proprias (34-36).
        # co2 (col 14) continua a decidir se a linha tem CO2 extraido.
        co2_kg_m3 = tofloat(ws.cell(r, 37).value)
        conversao = str(ws.cell(r, 36).value or '')
        estrato = ws.cell(r, 22).value  # e4_estrato: "principal" | "sensibilidade"

        if fck in (None, 0) or co2 is None:
            continue
        if status.get(row_id) != 'Elegível':
            continue
        if estrato not in TIERCODE:
            # dados_fck só deve conter linhas Elegível (ver LEGENDA); um
            # estrato em falta aqui é sinal de que apply_e4_estrato.py
            # precisa de correr de novo antes de exportar.
            print(f'AVISO: linha {r} (row_id={row_id}) sem e4_estrato, ignorada', file=sys.stderr)
            continue

        if co2_kg_m3 is None:
            kind, ucat = 'pendente', UNIDADE_OVERRIDE.get(row_id) or classify_unidade(unidade)[1]
            if ucat == 'm3':
                # 2026-10-13 (Kie): unidade ja em kg/m3 mas excluida da analise (valor incoerente ou
                # sem par valido). Barra propria no site, clicavel, com cada linha e o motivo.
                kind = 'excluido'
                excluded.append({'row_id': row_id, 'estudo': short_label(autores, ano),
                                 'material': str(material or '')[:160], 'fck': round(fck, 2),
                                 'co2': co2, 'unidade': str(unidade or '')[:160],
                                 'motivo': re.sub(r'^NAO CONVERTIDO\s*-\s*', '', conversao)[:600]})
        elif conversao.startswith('nenhuma'):
            kind, ucat = 'nativo', 'm3'
        else:
            kind, ucat = 'derivado', 'm3'
        unit_counts[(kind, ucat)] = unit_counts.get((kind, ucat), 0) + 1
        co2 = co2_kg_m3

        if kind in ('pendente', 'excluido'):
            # unidade ainda na forma original do estudo, nao convertida para
            # kg/m3 -- fora de `pairs` (ver nota no topo do ficheiro), mas ja
            # contado em unit_counts acima.
            continue
        if not (FCK_MIN <= fck <= FCK_MAX and CO2_MIN <= co2 <= CO2_MAX):
            continue

        cat = classify(row_id, material, titulo)
        if cat == 'outros':
            print(f'AVISO: linha {r} (row_id={row_id}) caiu em outros -- material={material!r}', file=sys.stderr)
        base = PORTLANDCODE.get(ws.cell(r, 40).value)
        if base is None:
            print(f'AVISO: linha {r} (row_id={row_id}) sem base_portland -- correr classificar_base_portland.py', file=sys.stderr)
            base = 'M'
        # 2026-10-07 (Kie): cenario com desconto. 7.o campo = co2 com os descontos que o proprio artigo
        # aplica (dados_fck col 44; null = o artigo nao declara desconto -> igual ao bruto); 8.o campo = 1
        # quando o artigo so publica o valor com desconto (col 47 = nao): o 2.o campo e entao esse valor.
        com = tofloat(ws.cell(r, 44).value)
        com = round(com, 2) if com is not None and CO2_MIN <= com <= CO2_MAX else None
        sem_bruto = 1 if str(ws.cell(r, 47).value or '') == 'nao' else 0
        sub = (ws.cell(r, 48).value or 'nao_declarado') if cat == 'opc' else None
        vida = tofloat(ws.cell(r, 19).value)
        vida = round(vida, 2) if vida else None
        compact.append([round(fck, 2), round(co2, 2), CATCODE[cat], TIERCODE[estrato], short_label(autores, ano), base,
                        com, sem_bruto, sub, vida])

    unit_stats = [
        {'kind': kind, 'cat': ucat, 'n': n}
        for (kind, ucat), n in sorted(unit_counts.items())
    ]

    json.dump({'pairs': compact, 'unit_stats': unit_stats, 'excluded': excluded}, sys.stdout, separators=(',', ':'))


if __name__ == '__main__':
    main()
