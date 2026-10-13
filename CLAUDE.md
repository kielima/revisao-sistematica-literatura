# Instruções para o Claude — Vault REVISÃO SISTEMÁTICA DE LITERATURA

Quando esta pasta for usada como Projeto Claude, leia este arquivo primeiro. Ele orienta a navegar com eficiência e economizar tokens.

## ⚠️ Este repositório NÃO contém os PDFs — acesso via Google Drive

Este repositório GitHub (`REVISÃO SISTEMÁTICA DE LITERATURA`) é um espelho desta pasta **sem os PDFs de artigos** (excluídos via `.gitignore` — `*.pdf`). Motivo: tamanho (7GB+, ~1.900 PDFs) e direitos autorais de artigos de editoras (Elsevier, Springer, MDPI etc.) — inviável e arriscado versionar no GitHub, mesmo em repo privado.

**Todo o resto está aqui normalmente:** notas `.md`, scripts `.py`, planilhas de controle (`articles_final.xlsx`, `meta_analysis_base.xlsx`, `GRÁFICOS DA RSL.xlsx`), logs de auditoria, PNGs de figuras extraídas.

**Quando a tarefa exigir ler o conteúdo de um PDF específico** (ex.: continuar triagem C1–C8, extrair dados de LCA/CO₂, verificar um artigo citado), use o **conector do Google Drive** (ferramentas `mcp__*` de Drive — `search_files`, `read_file_content`, `download_file_content`) em vez de procurar o arquivo neste repositório. Ele lê o texto completo do PDF (testado e confirmado em 2026-08-03).

**Atenção — existem duas pastas com o nome "REVISÃO SISTEMÁTICA DE LITERATURA" no Google Drive, com propósitos diferentes (não é duplicata acidental):**
- Uma fica na área de **PESQUISA** e contém a **fundamentação teórica** sobre RSL como método (aula, conceitos, PICO, PRISMA genérico) — não tem os PDFs nem o banco de dados desta dissertação.
- A pasta abaixo é a de **execução prática** desta RSL específica (dissertação UHPC) — é aqui que estão o banco de dados e os PDFs. **Use sempre esta para acessar os PDFs dos artigos.**

```
REVISÃO SISTEMÁTICA DE LITERATURA/          (folder id: 1xwwyHNp9VCX1fc4855Ll8IkOAogm-_w5)
└── 00_REFERENCIAS/
    └── ARTIGOS ACEITOS APÓS REMOÇÃO DAS DUPLICATAS/   (folder id: 1R63Q4Lzz6JRRLpwES1Ngyod04q0-r9YP)
        └── ~1.605 PDFs, padrão "SOBRENOME et al., ANO.pdf"
```

Query de busca útil (tool `search_files`):
```
parentId = '1R63Q4Lzz6JRRLpwES1Ngyod04q0-r9YP' and fullText contains 'termo'
```
ou para achar um artigo específico por título/autor:
```
parentId = '1R63Q4Lzz6JRRLpwES1Ngyod04q0-r9YP' and title contains 'SOBRENOME'
```

O Excel `articles_final.xlsx` (versionado neste repo) também é mantido sincronizado na mesma pasta do Drive — mudanças feitas aqui via Claude Code devem ser replicadas lá (upload manual ou `copy_file`/`create_file` do conector) para não perder o trabalho feito do celular, e vice-versa.

<!-- AUTO:BEGIN -->

## Sobre este vault

- **Nome:** REVISÃO SISTEMÁTICA DE LITERATURA
- **Tipo:** Projeto RSL (Revisão Sistemática de Literatura) + Projeto Claude híbrido
- **Total de notas .md:** 16 (11 com frontmatter, 5 sem)
- **PDFs de artigos:** 1.798 (em `00_REFERENCIAS/ARTIGOS ACEITOS APÓS REMOÇÃO DAS DUPLICATAS/`)
- **Banco principal:** `articles_final.xlsx` — 5.093 entradas, coluna `pdf` com caminhos/hyperlinks
- **Metodologia:** Zettelkasten + MOCs + frontmatter (aplicado às notas de metodologia estatística; notas operacionais não seguem o padrão)
- **Última varredura de organização:** 2026-06-04 pela skill `avaliacao-critica-vault` — desatualizada (não cobre a auditoria de dados abaixo); nenhuma rodada nova da skill desde então.
- **Downloads:** ✅ CONCLUÍDO (2026-06-05) — 480/480 Elegíveis com PDF; 60 Sem acesso (era 68 até 2026-08-03; 7 resolvidos na auditoria, 1 seguiu rejeitado por outro motivo).
- **Triagem PDF:** C1 ✅ C2 ✅ C3 ✅ C4 ✅ C5 ✅ C6 ✅ | ~~C7 REMOVIDO (2026-06-22)~~ | C8 ✅ — cascata fechada desde 2026-06-22. Os totais "Aceito/Rejeitado" registrados durante a execução original de cada critério (jun/2026) ficaram levemente desatualizados por correções pontuais linha-a-linha feitas em jul–ago/2026; não recalcular a partir deles sem checar a auditoria abaixo.
- **✅✅ ESTADO VIVO (medido em 2026-09-26 — usar este, os blocos de estado mais abaixo são históricos).** `status_triagem`: Duplicado 2.628 | Rejeitado 1.879 | Elegível 521 | Revisao 58 | Sem acesso 7 — total 5.093 (medido 2026-10-04, depois da 2833 OLIVEIRA). **Funil das 4 etapas** (mesmo cálculo do painel kielima.com/metanalise): universo 5.093 → E1 2.193 (os 4 critérios E1 = Aceito, excluindo linhas `Duplicado` — desde 2026-09-27; antes 2.199 contava 6 duplicatas) → E2 597 (`E2_resistencia` e `E2_co2` = Aceito) → E3 579 (521 Elegível + 58 Revisao) → **E4 521 pontuados: 409 principal (≥4,0/7) + 112 sensibilidade** (2026-10-04: 2833 OLIVEIRA rejeitada em E2 — o único fck era a categoria «4 ksi» do BEES extrapolada às vigas, decisão da Kiê) (2026-10-04: 4200 ONYELOWE rejeitada em E2 — 330 misturas de 5 fontes externas, só estatísticas globais de Fc com idades misturadas, mesmo caso da 4173) (2026-10-02: 4583 PUSHKAR rejeitada em E2 — só faixas de fc das fontes, misturas adaptadas; 4152 SANAL rejeitada em E2 — C35/C45 sem atribuição a Site 5/6, decisão da Kiê) (2026-09-30: 4173 ONYELOWE e 4817 NOUHOUN rejeitadas em E2 — sem fck por mistura; QD corrigido em 27 artigos, ver abaixo) (3917 UNGUREANU rejeitada em E2 a 2026-09-29) (3309 DADD subiu a 2026-09-29 com o CoV do fc-28) (3543 MAHAPATRA passou a Duplicado da 3542 a 2026-09-27). ✅ **E3/E4 fechadas a 2026-09-28 para as duas revisões de 14/09:** 3001 ONSONGO Rejeitado em E3 (enquadramento explícito 'for the African Region' + escala de RHA/SCBA); 3163 NASIR E3 Aceito, QA–QG = 0 → `Revisao`. **Subprodutos industriais revistos (2026-09-28):** fosfogesso 3217 DONG e 4552 BUMANIS confirmados Aceito (categoria global, 200–300 Mt/ano); escória de cobre 4495 ZHANG Rejeitado (MGCS modificada em laboratório a 1550 °C, uma fundição Boliden + uma fábrica em Changsha, sem mercado); **Escória de cobre decidida pela Kiê (2026-09-28), com fontes verificadas:** passa a escala (40–48 Mt/ano = 10–15% da escória de alto-forno, que a USGS MCS 2025 dá em 330–390 Mt — o ~530 Mt antigo da tabela estava inflacionado, e a cinza volante ficou marcada como NÃO VERIFICADA); 4301 DE PEDRO Aceito; 4813 ARREDONDO Rejeitado pelo enquadramento (Codelco/Chile, benefício amarrado à proximidade da fonte). Tabela de referência corrigida em `CRITERIOS_E_NUANCES_RSL.md` (Etapa 3). **Metanálise:** 1.492 pares fck×CO2 em kg/m3 no painel (→ 1.492 a 2026-10-04 com a revarredura das famílias e do betão armado — 43 lotes com leitura integral, famílias por par segundo as regras D1–D8 e correcções de valor E1–E3 em `metanalise/DECISOES_METANALISE.md`, `lotes_familia/`; → 1.524 a 2026-10-04 com a rejeição da 2833 OLIVEIRA; → 1.530 a 2026-10-04 com o desdobramento da 3017 CUNNINGHAM em 9 misturas; → 1.522 a 2026-10-04 com as 4 misturas do caso de Ohio da 4076 BUFFENBARGER; → 1.518 a 2026-10-04 com os fck medidos de YASEEN e SANDANAYAKE; → 1.511 a 2026-10-04 com a rejeição da 4200 ONYELOWE; → 1.512 a 2026-10-04 com o desdobramento da 2672 SPOSITO; → 1.507 a 2026-10-02 com a 3802 DEHGHANI; → 1.505 a 2026-09-29 com a rejeição da 3917; → 1.506 a 2026-09-29 com KOCAK 4855 e as resistências medidas; 1.169 → 1.164 com a revisão dos suspeitos de CO2; → 1.481 com a leitura integral dos Elegíveis sem par; → 1.485 com a via só-fundação da 4792 STUDZINSKI; → 1.498 com as figuras pendentes de SAHMENKO, BOUKHELF, LV e ARYAN — SAHMENKO com fck aos 28 d em ensaio seco, decisão da Kiê —, tudo a 2026-09-27; → 1.500 com a 2720 LI a 2026-09-28; → 1.495 com a rejeição da 4813 ARREDONDO em E3; → 1.501 com a separação das linhas legadas multi-traço, 2026-09-28); artigos Elegíveis com par: 406 de 528 (desde 2026-09-26 o `metanalise-export.py` só exporta artigos `Elegível` — antes 34 pares de 6 artigos rejeitados a 21/09 continuavam no gráfico); 577 linhas de `dados_fck` com volume do corpo de prova.
  - ✅ **Os 14 achados + o bloqueado LYRA de `ACHADOS_PENDENTES_CI_MPA.md` estão todos fechados (2026-09-26)**, PRs #237–#251. Regra que ficou: um CO2 publicado como TOTAL absoluto (edifício, sistema estrutural) com o volume de betão impresso no próprio artigo grava-se como taxa por m3 (total ÷ volume) + `vol_corpo_prova_m3` = esse volume (`medido_elemento_real`) — `co2 × vol` devolve o total publicado; se o total inclui aço, a linha vai para a família `concreto_armado` (MEDEIROS 5040, KONTRA 4931). Madeira estrutural (glulam) = família `biobase` (ASCIONE 4820).
  - ⭐ **Etapa 3 — rejeitos de mineração revistos (2026-09-26, decisões da Kiê, leitura integral dos PDFs).** Critério aplicado: como o próprio estudo ENQUADRA o material (mina/região concreta vs categoria) e que aplicação propõe. **Rejeitados em E3:** 4125 EL BERDAI (estéril de fosfato de Ben Guerir, uso local), 3181 GARCIA-TRONCOSO (rejeito de ouro GoldMins, Zaruma), 3201 VEMBU (magnesite de Salem, "locally accessible"), 3522 NIU (Siilinjärvi, ACV "limited to Finland"), 2724 LI (Mo de Jilin como ligante — passa comércio, falha escala: ~4–5% do cimento). **Mantidos Aceito:** 3222 ZHANG (Mo da China enquadrado como categoria nacional — a Kiê: a China, maior economia comercial do planeta e com a Belt and Road, passa o teste do comércio) e 4037 MULLER (rejeito de carvão como categoria, sistema transnacional; fck de fonte externa del Galdo 2022 aceite e registado). As duas regras novas estão no fim de `lotes_etapa2/PROMPT_E2.md`. **Outros rejeitos de mineração/subprodutos NÃO revistos:** fosfogesso (3217, 4552) e escória de cobre (4301, 4495, 4813) — subprodutos industriais, não rejeito de mina.
  - ✅ **Revisão dos 29 valores de CO2 marcados SUSPEITO/DIVERGE em `co2_conversao` (2026-09-27)**, com pré-leitura de 4 subagentes, leitura integral dos PDFs e figuras, e confirmação pessoal de cada caso. **Corrigidos:** LARSEN 3911 NSC 1.602 → 801 (os 81,7 t são de 2 pontes; vol 51 m3 e vida útil 100 anos = 1 ponte); VITALE 4475 → 513,0/450,5 (CO2 é da amassadura EN 196-1 = 3 prismas, vol 0,000768); DI MARIA 2653 → −110,8/−140,7/−122,4 (os "−1,09 kg" do texto são razão saldo/bruto, reconstruído com a absorção de 8,5 kg); MOMOTAZ 4689 R100C/CTr/RTr → bruto sem créditos de carga evitada 222,4/377,5/385,8; ZHAO 3305 CFFT 334,2 → 334,9; BACELAR 4106 fck 60 → 50 (gralha da Tab.8). **NÃO CONVERTIDO (fora do gráfico):** PASSONI 4706 (o numerador era energia PERT em MJ; o CO2 do betão só por leitura de gráfico e ~1.000 kg/m3, incoerente), VAN BELLEGHEM 4461 (laje sem dimensões), ASENSIO 2891 TRC (total inclui guarda-corpo de aço galvanizado; o único % do texto é incoerente com a Tab.6), ROSSI 2780 (só a brita), HAN 3881 (63.000 kg CO2/ano não é kg/m3). **Confirmados** (só notas): KINA, MIRDAD, HORÁKOVÁ, SAMPAIO. **Família `concreto_armado`** (totais com armadura): LARSEN, ASENSIO REF/TRS, HORÁKOVÁ, MIRDAD. TOSIC 4625 mantido tal como impresso ("g") pela decisão da Kiê de 12/09. Os relatórios dos subagentes não foram versionados. ⭐ **Preferência nova da Kiê (2026-09-27): aplicar directamente a recomendação sempre que for clara; só lhe perguntar quando não houver recomendação clara.**
  - ✅ **Leitura integral dos 202 Elegíveis sem par (2026-09-27, pedido da Kiê: "leitura completa do PDF por lotes, não por script").** 26 lotes de subagentes + ronda de figuras com PDFs reduzidos; auditoria pessoal de todos os casos incomuns. 317 pares gravados (116 linhas actualizadas, 201 novas; outras 19 novas com fck < 20 MPa retiradas pela regra da purga de 08/09, arquivadas em `lotes_sem_par/RETIRADAS_FCK_MENOR_20_2026-09-27.csv`), 283 linhas marcadas NAO CONVERTIDO com motivo; artigos com par 331 → 401; painel 1.164 → 1.481 pares. Tudo em `lotes_sem_par/` (relatório `REVISAO_ELEGIVEIS_SEM_PAR_2026-09-27.md`, resultados JSON por lote, `aplicar.py`). **Decididos pela Kiê (2026-09-27):** 4792 STUDZINSKI entra pela via só-fundação (4 pares C35/45, 279–322 kg/m3, família `concreto_armado`; substitui a exclusão de 12/09); 3543 MAHAPATRA marcada `Duplicado` da 3542. **Figuras pendentes vistas (2026-09-27):** SAHMENKO 4455, BOUKHELF 4500, LV 4516 e ARYAN 4768 gravados (+12 pares); DE FILIPPIS 4387 confirmado NAO CONVERTIDO — ver o fim do relatório. ✅ **2720 LI fechada (Kiê, 2026-09-28):** a UF impressa "1 L" é erro de digitação do artigo — assumida 1 m3 (o traço da Tab.3 soma 2.359,5 kg); pares nativos 449,06/59,18 e 325,07/56,71 kg CO2-eq/m3, famílias opc/scm. A pedido da Kiê, `QA_unidade_funcional` 1 → 0,5 (UF não inequívoca), E4 4,0 → 3,5, estrato principal → sensibilidade. ⚠️ A nota de 08/09 diz que foi enviado email ao autor (tarefa #1488), mas não há rasto dele no Gmail da Kiê. ⚠️ **Nunca enviar o email da Kiê a serviços externos** — dois subagentes fizeram-no numa consulta ao Unpaywall cada um (lotes 1 e 5); as instruções dos lotes passaram a proibi-lo. ⚠️ Downloads do Drive acima de ~6 MB falham sempre com "session expired" — usar o `shrink-drive-pdf.yml` (compressão /screen do ficheiro inteiro resolve).
  - ⭐ **Base do ligante por traço + filtro «Só cimento Portland» no painel (Kiê, 2026-09-28).** `dados_fck` col 40 `base_portland` (`sim`/`nao`/`misto`) e col 41 `base_portland_nota`, escritas por **`classificar_base_portland.py`** (regras + decisões manuais por linha; correr depois de mexer em material/família). `sim` = cimento Portland como ligante principal (inclui cimentos compostos, SCM em substituição parcial, LC3, UHPC, betão armado, agregado reciclado); `nao` = sem clínquer Portland como ligante principal (geopolímero/álcali-ativado incl. híbridos com OPC minoritário, CSA, magnésio, belite-ye'elimite, gesso, madeira, escória carbonatada, compósito polimérico); `misto` = linha que junta os dois (2966, 3095). No painel: 1.273 pares Portland, 227 não-Portland, 1 misto. O exportador passa o 6.º campo por par (`P`/`N`/`M`) e o site tem uma barra fixa no topo que filtra KPI de pares, dispersão, legenda, forest, curva de progresso e estratos (funil, curvas de volume/IC e gráfico de unidades não mudam — contam artigos ou a base inteira). **Correcções feitas na mesma ronda:** (1) 6 linhas legadas multi-traço (3112, 3114, 3118, 3218, 3221 separadas num traço por linha; 3095 sem par válido → NAO CONVERTIDO) — o exportador lia só o primeiro número da célula e punha pares falsos no gráfico (1 MPa / 35 kg; 180 MPa que eram dias; 1 / 1); (2) famílias no `metanalise-export.py`: regex alcalino alargado (`alcali-activado`, `alcalinamente`, acentos — o antigo `\bAAM\b` em maiúsculas nunca casava) e **40 traços Portland de referência de artigos de geopolímero deixaram de cair na família «geopolímero» só pelo título**; CSA/magnésio/BYC → `ligantes`. Por classificar (fora do gráfico): 14 linhas, quase todas de artigos Rejeitado.
  - ✅ **Lacunas vida útil / IC / volume preenchidas (2026-09-29, pedido da Kiê «pontos 1 a 3»).** 79 artigos Elegíveis relidos por 10 lotes de subagentes (`lotes_lacunas/`: worklist, resultados JSON, `aplicar.py`), com leitura pessoal das barras de erro que os subagentes não conseguiram ver (HAIGH 4849, NASSAR 2755, SIRICO 2895) via recortes do `shrink-drive-pdf.yml`. Em `dados_fck`: volume do provete 708 → 863 linhas; `ic_fck_valor` 106 → 185; vida útil 452 → 461 (as restantes 18 dos 27 artigos pedidos não declaram vida útil como premissa própria — só citam literatura); idade corrigida para 28 d em 4696 (linha 1691), 3225 e 3203. `aplicar.py` só preenche células vazias (excepções explícitas no script). QG: 3309 DADD 0 → 0,5 (E4 3,5 → 4,0, passa a principal) e 3477 HAIGH 0,5 → 1,0. Pares do gráfico inalterados (1.501). ✅ **Fechados a 2026-09-29 (Kiê: «pode aplicar o KOCAK e verificar os PDFs»):** **4855 KOCAK** — totais da Tab.3 lidos em toneladas → 264,62 (RAC) e 273,18 (NAC) kg CO2-eq/m3 (÷ 3.411,38 m3 impressos; coerente com 309 kg cimento/m3), vol = 3.411,38 `medido_elemento_real`, QA 1 → 0,5, E4 3,5 → 3,0 (sensibilidade), indicador GWP20. **fck de projecto trocado pelo medido, com leitura pessoal das figuras:** 2951 ALI 65 → 71,3 (Fig.9a; 65 era o alvo de dosagem); 3132 OYEBISI C25/C30/C40 → 29,1/34,5/45,9 (Fig.5, V0); 3413 BATUECAS AAS 110 → 101,2 (Fig.1; o «up to 110» do texto não é a média) e o híbrido de escória (linha 995) ganhou fck 42,0 da mesma figura; 3519 NGUYEN forno 37,5 → 38,8 e as linhas de prensagem a quente separadas por temperatura (100/120 °C × 2/3 h = 33,3/35,5/38,1/36,9, Fig.13b; a ACV não distingue temperatura, o CO2 de cada tempo vale para as duas — linhas novas 2099/2100); 3731 BAYKARA 42 → 40,0 (Fig.2; os 42 eram da ficha técnica do cimento). Painel 1.501 → 1.506 pares (1.275 Portland, 230 não-Portland, 1 misto); volume 866 linhas, IC fck 190. ✅ **Fechados a 2026-09-29 (recomendação clara, aplicada directamente):** 3477 HAIGH CO2 → Tab.7 (GWP100 370/360/343; o Monte Carlo 572/1023/997 é a análise de sensibilidade do próprio artigo e soma energia de máquinas de laboratório), IC do CO2 removido, QG 1,0 → 0,5, E4 5,5; 4698 `tipo_corpo_prova` 'cubo' retirado (sem ensaio no artigo); 3281 NATH mantida a vida útil do recobrimento de 35 mm (a incoerência da Tab.6 só afecta as taxas anuais, que são calculadas por nós). ✅ **3917 UNGUREANU Rejeitado em E2 (decisão da Kiê, 2026-09-29):** o único par era um factor genérico da biblioteca do EcoDesigner (Tab.6, 'Pre-cast concrete C20/25' 120,5 g/kg, sem fonte) e os autores excluem explicitamente o betão armado da contabilização de CO2; `E2_co2` → Rejeitado, `etapa_saida` 2. Regra registada no fim de `lotes_etapa2/PROMPT_E2.md`.
  - ✅ **Elegíveis só com CO2 e QD sem vida útil (2026-09-30, pedido da Kiê).** Os 5 Elegíveis com CO2 e sem fck relidos na íntegra: **4173 ONYELOWE** (192 misturas de base externa, só estatísticas globais de Fc) e **4817 NOUHOUN** (classes C20/25–C35/45 sem atribuição a LC/NC/SC) → Rejeitado em E2_resistencia. **4152 SANAL Rejeitado em E2_resistencia (decisão da Kiê, 2026-10-02)** depois de ver as 11 páginas com todas as tabelas e figuras: C35/C45 citados sem dizer que site é qual; a atribuição pela dosagem seria dedução nossa — regra nova no fim de `lotes_etapa2/PROMPT_E2.md`. **4583 PUSHKAR Rejeitado em E2_resistencia (decisão da Kiê, 2026-10-02):** sem ensaio próprio, só as faixas de fc28 de Kadam & Patil 2017 e Kim & Lee 2011; a regra MULLER não se aplica porque os níveis de substituição das Tabelas não batem com os que o próprio artigo descreve para as fontes (misturas adaptadas) — extensão registada em `PROMPT_E2.md`. ✅ **3802 DEHGHANI fechada (2026-10-02):** a Kiê enviou a versão publicada (T&F); fck aos 28 d lido por píxel da Fig.5(b) — W22-R 51,2 MPa (DP 9,3), W22-T20 65,7 MPa (DP 6,2), n=3, prisma 200×100×60 mm (vol 0,0012 m3); a nota antiga «nenhuma mistura atinge 55 MPa» estava errada. Mantém-se Elegível (+2 pares). ✅ PDF publicado posto no Drive a 2026-10-04 (relay pelo `push-to-drive.yml` com `repo_path`, autorizado pela Kiê), por cima do `DEHGHANI et al., 2024.pdf` (mesmo nome/fileId; era a versão White Rose sem figuras). Ramo `scratch/pdf-relay-2026-10-04` limpo depois do envio (o proxy da sessão não deixa apagar ramos remotos). **QD (vida útil):** regra aplicada = 1 só se o artigo adopta um número de anos como premissa própria, senão 0 (era a prática em 490 dos 525 Elegíveis). 3 lotes de releitura integral (`qd_resultado_lote*.json`, não versionados) confirmaram as notas de 29/09: 23 artigos QD → 0 (4138, 4267, 4290, 4483, 2586, 2624, 2696, 4758, 2755, 2801, 3068, 3112, 3152, 3225, 3251, 3331, 3404, 3443, 3449, 3456, 3477, 3896, 3915); HAFEZ 3539 mantém 1 (50 anos declarados no cenário de betão armado; os pares gravados são do cenário 1); **4617 ZENISEK QD 0 → 1** (50 anos EN 1990 declarados); **2879 BOROS** (100 anos só na introdução) e **4706 PASSONI** (50 anos = vida nominal do edifício de 1970) perderam a vida útil gravada e ficam com QD 0. Passaram a sensibilidade: 4138, 2624, 3443, 3449. Pares do gráfico inalterados (1.505).
  - ✅ **Idade do ensaio (2026-10-04, pedido da Kiê «pela idade do ensaio, em lotes»).** 565 pares de 188 artigos Elegíveis com `idade_dias` vazia, 19 lotes de subagentes com leitura integral (`lotes_idade/`: worklist, `PROMPT.md`, resultados JSON, `aplicar.py`, que só preenche células vazias e carimba `observacoes` com `[idade 2026-10-04: tipo; citação]`). **232 pares gravados**: 46 de ensaio próprio (31 aos 28 d; 11 da 3105 ABDEL-GAWWAD aos 35 d — não há ensaio aos 28 d; 2 da 4779 ROUX aos 7 d; 2 da 3356 TEIXEIRA aos ~90 d) e 186 de classe/resistência de projecto com 28 d (65 com a idade escrita no próprio artigo, 121 só pela norma citada — EN 206/EN 1992, ACI 318, NBR 6118/8953, AS 1379, EHE-08, KS). **332 ficam vazios**: 270 classes sem norma citada (`classe_sem_idade`) e 62 sem idade declarada. **Correcções na mesma ronda (leitura pessoal):** 2672 SPOSITO — a linha legada de faixa (fck 23,07 = NH aos 7 d com CO2 93,5 = mínimo da Tabela 12) desdobrada nas 7 pastas da Sec.4.1.3, fck aos 28 d da Fig.25/Tabela 13 e CO2 CC+biogénico da Tabela 12 (+5 pares, linhas 2101–2105); 4608 PALUMBO EPD7/EPD8 40/35 → 32/28 (a coluna da Table 3 trazia o valor de cubo de C32/40 e C28/35); 4463 SAMEER linha 1380 `tipo_corpo_prova` cubo → cilindro 150×300 (o volume já era o do cilindro). Volume 868 → 873 linhas, IC fck 191 → 196. ⭐ **Regra da notação de norma (decisão da Kiê, 2026-10-04):** classe escrita no artigo na notação de uma norma que a define aos 28 d — Cxx/yy da EN 206 (incl. «Cast in Situ 25/30») ou HA-xx da EHE-08 — recebe idade 28 d mesmo sem a norma citada; valores soltos em MPa e «C30» sem barra ficam vazios. Aplicada por `lotes_idade/aplicar_notacao.py` a 29 pares (excluídos 950/951 da 3263 SKULLESTAD: o fck gravado é o valor assumido/médio, não o da classe). Total da ronda: 261 pares com idade, 303 vazios. Tarefa Supabase **#1583** para escrever a hierarquia de atribuição da idade nos métodos da dissertação. ✅ **2703 KIM 2016e (decisão da Kiê, 2026-10-04):** casos 1/4/5 da ACV passam do fck de projecto 24 MPa ao medido aos 28 d da Tabela 4 (29,6 / 38,6 / 33,2 MPa, cilindro 100×200, vol 0,0015708), correspondência pelo ligante com alerta (o traço da Tabela 11 remete para refs. externas); casos 2/3 (10%, não ensaiados) ficam com 24 MPa e sem idade. Volume 873 → 876 linhas. ✅ **3356 TEIXEIRA (decisão da Kiê, 2026-10-04):** mantido o fck aos ~90 d (35 / 37,5 MPa), porque a unidade funcional do artigo compara B300 e FA pela resistência equivalente aos ~90 d; os valores aos 28 d da Fig.3 (~32,2 / ~27,8) ficam só em nota. ✅ **Cinco casos residuais da idade, lidos pessoalmente (2026-10-04, «pode avançar com os cinco»):** **3327 YASEEN** — fck medido aos 28 d das Figs.4/6 lido por píxel no recorte pp.5–11 (`shrink-drive-pdf.yml`): controlo 28 → 29,3 MPa e 6 misturas que tinham CO2 sem fck ganham fck (FA10 27,9, FA20 26,3, FA30 25,1, SF05 26,9, SF10 28,2, SF15 24,4), cilindro 150×300, +6 pares; **3419 SANDANAYAKE** — Fig.3(a): controlo 25 (projecto) → 20,5 e mistura com 10% de resíduo de copo 16,0 MPa (78% do controlo, como no texto), idade não declarada, +1 par; **3828 MOSTAFAEI** linha 1108 96 → 95 MPa (Fig.8, resumo e conclusões; o 96 do texto é gralha); **4064 JIANG** linha 1170 anotada como previsão do modelo (não ensaio); **4076 BUFFENBARGER** sem alteração (Tabela 7 = fcr′ teórico da ACI 301 aos 28 d). ✅ **4076 BUFFENBARGER — caso de Ohio (decisão da Kiê, 2026-10-04: «se forem diferentes, acrescente os 4 pares e use a média da obra»):** as 4 misturas da Tabela 3 são traços diferentes (fundação 4000 psi e pilares 5000 psi reais; duas ternárias «reasonably designed») e entraram como linhas 2106–2109. **Revisto pela Kiê no mesmo dia («vamos padronizar os dados de um mesmo artigo»):** fck = ensaio aos 28 d de aprovação do traço nas quatro (47,5 / 61,7 / 45,7 / 51,2 MPa), única resistência medida para as 4; a média em obra (37,3 / 54,7 / 35,9 / 45,4) fica só em nota. CO2 lido por píxel na Fig.3(b): 250,2 / 310,7 / 222,1 / 245,7 kg CO2e/m3 (as diferenças 28,1 e 65,0 conferem com o texto). Motivo: a «Field data» das duas ternárias é estimada pelos autores (mesma diferença laboratório–obra da mistura real: −21,4% / −11,4%), não medida. Painel 1.511 → 1.518 pares.
  - ✅ **Revarredura das famílias e do betão armado (2026-10-04, pedido da Kiê «corrija todas as inconsistências» + «revarredura completa do concreto armado»).** 43 lotes de subagentes (`lotes_familia/`: worklist, `PROMPT.md`, resultados JSON, `mapear.py`, `aplicar.py`, `aplicar_valores.py`), quatro perguntas por par (aço no CO2, tipo de ligante, papel do material, resíduo/UHPC). A família passa a ser a da própria mistura (controlos → `opc`; resíduo a substituir cimento → `scm`; resíduo como agregado/fibra → `reciclado`; álcali → `geopolimero`; CO2 com aço inseparável → `concreto_armado`), em `lotes_familia/familias_revarredura.json`, que o `metanalise-export.py` lê antes do OVERRIDE antigo; `classificar_base_portland.py` segue-a. 362 mudanças de família; 32 pares saem do gráfico (valores que não são o CO2 do betão, duplicados, fck sem apoio) e ~60 valores corrigidos (CO2 só do betão quando o artigo o dá; PUSHKAR 4580 estava em kg/(m3·MPa)). Painel 1.524 → 1.492 pares, 394 estudos. ⭐ **Decisão registada (Kiê, 2026-10-04): «nunca se esqueça de registrar todas decisões»** — tudo em `metanalise/DECISOES_METANALISE.md` (secções D, D′ e perguntas abertas em C). **8 perguntas à Kiê em aberto** (créditos, cimentos compostos, PUSHKAR proxy, TOSIC, OH, publicações com os mesmos números, DI SUMMA, ISAIA ≠ UHPC).
  - ✅ **CO2 sem e com desconto (2026-10-07, pedido da Kiê: «quero ter uma opção para poder ver os dois cenários com o desconto e sem o desconto […] reabrir todos os PDFs»).** 44 lotes (`lotes_creditos/`: worklist, `PROMPT.md`, resultados JSON, `ACHADOS_2026-10-07.md`, `aplicar.py`), releitura dos 394 estudos / 1.492 pares do painel. Colunas novas em `dados_fck`: **44 `co2_kg_m3_com_desconto`**, **45 `co2_desconto_tipo`** (carga_evitada, carbonatacao, biogenico, modulo_D…), **46 `co2_desconto_citacao`**, **47 `co2_bruto_disponivel`**. `co2_kg_m3` (col 37) passa a ser o bruto sempre que o artigo o dá (83 valores trocados de líquido para bruto); 173 pares têm valor com desconto; 49 só têm o valor publicado com desconto. Painel: grupo «CO₂ dos artigos» (Sem desconto / Com desconto) na barra fixa; o modelo em R ganha as sensibilidades «com desconto» e «só pares com bruto». Decisões F1–F8 em `metanalise/DECISOES_METANALISE.md`. Achados colaterais (erros de valor por verificar pessoalmente: HUANG 4458 custo em vez de CO2, SAMEER cenário errado, GUO, OYEBISI, JEONG, DU, MENNA BARRETO volume, GARCES, GRENGG, HABIBI l.11, REZENDE) em `lotes_creditos/ACHADOS_2026-10-07.md`.
  - ✅ **Erros de valor de CO2 corrigidos (2026-10-07, pedido da Kiê) + F9.** Os pares só com CO2 com desconto (49) saem do cenário «Sem desconto» e só entram em «Com desconto» (F9, painel e modelo). 4 lotes de releitura (`lotes_creditos/correcoes/`) com verificação pessoal no PDF: 27 linhas corrigidas (HUANG custo→CO2, SAMEER caso base, GUO, OYEBISI, MENNA BARRETO vol 1,64, JEONG, DU 651, GARCES SHGPC, GRENGG A-SA, DACIC, REZENDE 214,9) e 2 NAO CONVERTIDO (KANAGARAJ, HABIBI l.11) — decisão F10 em `metanalise/DECISOES_METANALISE.md`. Painel 1.490 pares (1.441 sem desconto). MOSTAFAEI 4263 → NAO CONVERTIDO (F11, Kiê 2026-10-09: Fig.11 sem fronteira identificável); painel 1.486 pares, 392 estudos. Filtro de qualidade passou para a barra fixa do painel.
  - ✅ **Cimento comercial = `opc` com subfamílias (F12, Kiê 2026-10-10).** 30 lotes de releitura integral (`lotes_cimento/`, 291 estudos, 914 pares opc+scm) gravaram em `dados_fck` col 48 `cimento_subfamilia`, 49 `cimento_designacao`, 50 `cimento_norma`, 51 `cimento_citacao`. Cimento tal como vendido (mesmo composto: CP II, CP III, CEM II/III…) → `opc`; adição juntada pelo próprio estudo → `scm` (41 opc→scm, 9 scm→opc). O corte de 20% foi abandonado: a NBR 16697:2018 Tabela 2 (p. 5) não o tem. No painel, a família «cimento Portland» abre em subfamílias com botão (i); só a NBR 16697 tem tabela/página verificadas — a 2026-10-11 confirmaram-se também ASTM C150-07, IS 8112/12269:2013 e GB 175-2023 (fontes legítimas gratuitas); EN 197-1, ASTM C595/C1157, AS 3972 e NC 95/96 continuam por confirmar (só à venda ou inacessíveis). Referências exactas em `metanalise/NORMAS_CIMENTO_REFERENCIAS.md`; decisões F12/F12-a/F12-b em `metanalise/DECISOES_METANALISE.md`.
  - ✅ **Releitura dos 129 Elegíveis sem par (F14, Kiê 2026-10-11).** 26 lotes (`lotes_sem_par_revisao/`), 127 artigos relidos na íntegra: 112 confirmados NAO CONVERTIVEL. Aplicados, com verificação pessoal: 3222 ZHANG (linha legada desdobrada em 5), 3095 TEFA (4 ligantes cimentícios), 3170 SAMUVEL (6 misturas), 3237 KANAGARAJ (6 misturas ECA0) — painel 1.486 → 1.507 pares, 396 estudos, KPI 76 %. Excluídos por mim (por confirmar): HABTE, MAHAPATRA, KROMOSER, EK, ASSUNÇÃO, McDONALD, YARDIMCI, HORA. **Perguntas abertas à Kiê, uma a uma:** 4511, 3414, 2731, 3285, 3852, 5017 — ver F14 em `metanalise/DECISOES_METANALISE.md`.
  - ✅ **País do autor de correspondência (F15, Kiê 2026-10-13)** para o mapa de publicações: `articles_final.xlsx` col 57 `pais_correspondencia`, 58 `pais_iso3`, 59 `pais_fonte` (wos_correspondencia 386 / bdtd 26 / crossref_primeiro_autor 39 / pdf_correspondencia 63 / pdf_primeiro_autor 7), 60 `pais_citacao`. Os 521 Elegíveis têm país (61 países). Script `lotes_paises/aplicar.py`; `lotes_paises/crossref.json` guarda, por DOI, autores/afiliações e a lista de referências do Crossref (base da linha temporal de citações). Regras de desempate marcadas «por confirmar» em F15.
  - 📌 **Colunas novas em `dados_fck` (2026-09-26, pedido da Kiê):** 34 `co2_original` (valor+unidade tal como publicado), 35 `co2_original_local` (tabela/figura/página), 36 `co2_conversao` (método e conta; "nenhuma - publicado em kg CO2-eq/m3" quando nativo; "NAO CONVERTIDO - ..." quando não há divisor), 37 **`co2_kg_m3` — a base de TODOS os gráficos de emissões** (o `metanalise-export.py` lê daqui), 38 `ci_kgco2_mpa` = co2_kg_m3 × vol / fck, 39 `cit_kgco2_mpa_ano` = ci / vida_util (definições do `PROTOCOLO_CI_MPA_2026-09-08.md`). **38–39 são calculadas por `recalcular_ci.py` — correr sempre depois de mexer em co2_kg_m3, fck, volume ou vida útil.** `co2_valor`/`co2_unidade` (14–15) ficam como estavam, por rastreabilidade.
  - ✅ **Volume pela norma, IC dos 11 artigos com QG > 0 e coluna primário/secundário (2026-10-04, pedido da Kiê «1. Pode corrigir. 2. … 3. … 4. …»).** (1) **3802 DEHGHANI** QD 1 → 0 (E4 6,5 → 5,5, continua principal). (2) **Volume do provete pela norma citada** — 674 pares sem volume de 184 artigos Elegíveis, 19 lotes de subagentes com leitura integral (`lotes_volnorma/`: worklist, `PROMPT.md`, resultados JSON, `aplicar.py`). ⭐ **Regra estrita da Kiê (2026-10-04): «não vamos assumir nada»** — volume só quando o artigo dá as dimensões, quando a relação é directa, ou quando a norma citada define um único provete: notação de classe EN 206 / EN 1992 / EHE-08 / fib MC2010 / BS 8500 → cilindro 150×300 (valor de cilindro) ou cubo 150 (valor de cubo); GB 50010 / GB/T 50081 e IS 456 → cubo 150; ASTM C109 → cubo 50; EN 196-1 e EN 998-2 (via EN 1015-11) → prisma 40×40×160. Normas que admitem mais de um provete (ASTM C39/C31, ACI 318, NBR, AS 1012/1379, KS, JIS, IS 516, EN 12390-3 sem tamanho, normas de dosagem) e «sem norma» → volume em branco com a justificação em `vol_corpo_prova_citacao` (`vol_corpo_prova_fonte` = `indisponivel`). Resultado: **125 volumes gravados, 549 em branco justificados**; coluna nova **`dados_fck` col 43 `norma_ensaio`** (243 linhas). Volume 876 → **1.009 linhas**. `tipo_corpo_prova` limpo onde não tinha apoio no PDF (2836 ALMEIDA, 2841 RIGON, 4408 NASR, 4479 KOCI, linha 571 ELTANTAWI); fck corrigidos por leitura pessoal: 3568 BERNDT linhas 1047/1049 → 38,6/45,4 (Tab.3 p.611). (3) **IC dos 11 artigos com QG > 0 e sem intervalo** (`lotes_ic/`: resultados JSON e `aplicar.py`), com leitura pessoal das figuras em alta resolução (recortes do `shrink-drive-pdf.yml` com `first_page`/`last_page`): 3203 VACLAVIK 28 DP medidos por pixel (Figs.7/8, n=6) e **8 fck corrigidos pelos rótulos em alta resolução** (estavam lidos na versão /screen; ex.: C-3 fina 47,9 → 47,5, C-4 fina 35,2 → 36,2); 4512 SKIBICKI CoV 17,4/7,2/13,0 % (Fig.11b); 2999 RATHNARAJAN 24 DP (Fig.2, n=3) e 5 fck corrigidos (1905 → 44,8; 1906 → 42,0; 1912 → 45,7; 1913 → 43,6; 1921 → 50,8 — médias FW/SW trocadas ou mal lidas); 2714 KUL ±6 MPa como `desvio_maximo_global` (a Fig.6 não tem barras de erro); 3758 RAVEENDRAN meias-barras como `barra_erro_nao_definida`; 3399 DEROUSSEAU e 4416 ASDRUBALI CO2 como `intervalo_interquartil` (Monte Carlo / caixas de EPD); 3685 MALAMI IC de CO2 30,5 removido (era da coluna PC, total a 100 anos). **3017 CUNNINGHAM desdobrada**: a linha legada juntava o fck da 5%M-RHA com o CO2 do CTRL; agora 9 misturas com fck aos 28 d ± DP da Fig.3b (n=5) e CO2 «Measured» da Fig.9 por pixel (linhas 259 e 2110–2117). IC do fck 196 → **268 linhas**. (4) **Primário/secundário:** `articles_final.xlsx` col 56 `tipo_fonte` (`primario` nos 522 Elegíveis) e `dados_fck` col 42 `origem_dado` (`primario` em todas as linhas); os estudos secundários (ONSONGO, NASIR, SCOPE…) ficam para extracção futura. **Decididos pela Kiê no mesmo dia** (`lotes_ic/aplicar_decisoes_2026-10-04.py`): 4321 ALMULHIM → fck = «Factory Mix Fcr (28 Days)» da Tab.6 (38,27/48,82/59,82/70,82/81,82); 4416 ASDRUBALI → `co2_kg_m3` = média de cada caixa da Fig.5; 2833 OLIVEIRA → pares retirados e artigo Rejeitado em E2_resistencia. Texto original das dúvidas: 4321 ALMULHIM (os rótulos C40–C80 são Fcr′ aproximado; a Tab.6 dá Fc de projecto 30–70 e Fcr de fábrica 38,27–81,82 aos 28 d — o fck gravado 40–80 não é nenhum deles), 4416 ASDRUBALI (o `co2_kg_m3` gravado mistura medianas e médias das caixas da Fig.5), 2833 OLIVEIRA (27,58 MPa do BEES atribuído por extrapolação às vigas A/B/C).
- **(Histórico) Estado real (medido em 2026-08-23, depois da retriagem por PDF):** `status_triagem`: Duplicado 2.622 | Inconclusivo 1.138 | Rejeitado 903 | Elegível 370 | Sem acesso 60 — total 5.093. **1.618 linhas têm alguma decisão `P:`**. **4.297 linhas têm DOI** (eram 4.250). **2.042 células têm ficheiro PDF, todas com hyperlink coerente.** **91 linhas vivas estão sem ficheiro PDF.**

  🔢 **O funil: 1.259, não 1.397.** *(Era 1.248 antes da retriagem de 16 artigos feita a 23/08; ver `RETRIAGEM_PDF_2026-08-23.md`.)* O número 1.397 que aqui esteve publicado estava inflacionado por duas vias, ambas medidas e confirmadas a 2026-08-23:
  1. **Contava linhas mortas** — a definição não filtrava `status_triagem`, incluindo 12 linhas `Duplicado`/`Rejeitado`/`Sem acesso`. Só linhas vivas: **1.385**.
  2. **Contava `R:` como decisão** — contra a regra do próprio projecto («células com apenas `R:` são consideradas NÃO triadas»). Exigindo `P:Aceito` em C1 e C3–C6: **1.248**.

  O backup anterior às alterações de 23/08 dá exactamente 1.385 pela segunda definição, o que prova que a aplicação dos registos **não mexeu no funil** — só se tocou em linhas sem decisões `P:`. *(Medições anteriores, todas pela definição inflacionada: 2026-08-22, 1.397; 2026-08-16, 1.383; 2026-08-13, 1.401; 2026-08-03, 1.333.)*

  ⚠️ **O C2 é o que falta.** Dentro do funil de 1.259, **só 98 têm o C2 confirmado por PDF; faltam 1.161** — é exactamente o trabalho da tarefa #7. Nenhuma dessas 1.248 linhas está sem ficheiro: o material para continuar está todo lá.

  ⚠️ **Ao contar «linhas sem PDF», não basta ver se a célula `pdf` está vazia.** As 60 linhas `Sem acesso` têm a célula **preenchida com uma nota** («Sem acesso — Taylor & Francis», «sem download disponível via CAPES (2026-06-04)») ou com o próprio URL do DOI. Um filtro por «célula preenchida» conta-as como tendo ficheiro. Exigir que o valor **termine em `.pdf` e não comece por `http`**. Contando assim, são **144** as linhas vivas sem ficheiro: 84 Inconclusivo + 60 Sem acesso.
- **✅✅ CONFERÊNCIA PDF × BANCO CONCLUÍDA (2026-08-19):** os **1.422** ficheiros foram todos abertos e conferidos em título, primeiro autor e DOI. **1.379 CONFERE · 34 PDF_ERRADO · 4 ILEGIVEL · 4 NAO_ENCONTRADO · 1 INDETERMINADO.** Registo linha a linha em `VERIFICACAO_TITULO_AUTOR_DOI.csv`; atribuição e resultado de cada lote em `lotes_verificacao/` (lotes 1–99).
- **✅✅✅ SEGUNDA CONFERÊNCIA — 100% DOS PDFs DO BANCO VERIFICADOS (2026-08-31).** A Kiê pediu para fechar a lacuna: todo PDF ligado a uma linha do banco, não só os 1.422 da primeira ronda, conferido por leitura completa contra DOI+publisher+autor+resumo (protocolo reforçado — a conferência original só exigia título+autor+DOI). Reconciliação por script encontrou **530 ficheiros** (415 nunca cobertos pela primeira conferência + 115 do lote de 117 PDFs de 30/08 e de PDFs integrados no início desta sessão) que nunca tinham passado por nenhum protocolo formal — processados em **36 lotes** de subagentes (lotes 1–36), cada um a abrir e ler os PDFs de verdade via `mcp__Google_Drive__read_file_content`, com amostragem pessoal entre lotes. `VERIFICACAO_TITULO_AUTOR_DOI.csv` fica agora com **1.952 linhas** (colunas novas `publisher_bate`/`resumo_bate`), cobrindo as **2.185 linhas do banco com PDF, sem excepção** — confirmado por reconciliação final (0 residuais). Totais: **1.907 CONFERE · 35 PDF_ERRADO (34 da primeira ronda + 1 novo) · 5 ILEGIVEL · 4 NAO_ENCONTRADO · 1 INDETERMINADO.**

  🚨 **Achado real desta ronda — linha 3855 (KANE et al., 2025, biochar/CDR), Elegível, já tinha saído da Etapa 2 rejeitada:** o ficheiro tinha capa de metadados eScholarship correcta (título/DOI/autor do artigo certo) mas o **corpo inteiro** (124.838 caracteres) era outro artigo (Pinheiro et al., "Short-term electricity load forecasting") — confirmado por leitura directa, "biochar" só ocorre 1x, no cabeçalho da capa. **Corrigido em duas fases**: primeiro (2026-08-31) PDF solto (célula esvaziada) e decisões `P:` em C1/C3/C4/C5/C6 anuladas (mantido só o histórico `R:`), deixando por decidir se `E1_moldavel`/`E1_construcao`/`E2_resistencia`/`etapa_saida`/`criterio_saida` também tinham sido tomadas sobre o PDF errado. A Kiê confirmou que sim e formulou a regra geral abaixo; segunda fase (mesmo dia) limpou também esses cinco campos.

  ⭐ **Regra geral nova (Kiê, 2026-08-31): "Quando tiver um lugar com PDF errado, anule TODAS as decisões, principalmente as das etapas E2."** Não basta anular as decisões legadas C1–C8 — qualquer campo derivado da leitura do PDF errado tem de ser limpo, incluindo os migrados para a Etapa 1 (`E1_moldavel`, `E1_construcao`, quando a nota de comentário mostra que vieram de "migrados das decisoes P:") e qualquer decisão da Etapa 2 tomada directamente por leitura do PDF (`E2_resistencia`, `E2_co2`), mais `etapa_saida`/`criterio_saida` se a saída do funil dependia de alguma dessas. Aplicar esta regra de imediato, sem esperar confirmação, em qualquer PDF_ERRADO futuro — a linha fica então sem decisão nenhuma além do histórico `R:`, à espera de nova leitura quando o PDF certo aparecer.

  ⭐ **Regra de auditoria (Kiê, 2026-08-31): erro de subagente apanhado por amostragem → auditar TODO o lote desse subagente, não só continuar a amostrar.** Aplicado ao lote 14 (que produziu o falso positivo 2700/2704 abaixo, mas também o achado genuíno da 3855): os 12 ficheiros restantes desse lote foram todos reverificados pessoalmente — vieram limpos, confirmando que o erro do subagente foi isolado àquela alegação, sem outra contaminação.

  ⚠️ **Um subagente produziu um falso positivo, apanhado pela amostragem pessoal:** alegou troca de ficheiro entre as linhas 2700 e 2704 (ambas Kim et al., 2016); a leitura directa de ambos os ficheiros mostrou que **os dois estão correctos**, cada um na sua linha — não houve troca nenhuma. Reforça por que a auditoria por amostragem (não só confiar no relato do subagente) continua obrigatória mesmo com o protocolo reforçado.

  📌 **Novo padrão de armadilha — título alterado entre "Journal Pre-proof" e versão final (caso DUGGAN, 10.1016/j.jclepro.2020.122540):** o PDF (um pre-proof Elsevier) imprime "Factors affecting the carbonation depth in stabilised peat"; o banco tem "Stabilisation for peat improvement: Extent of carbonation and environmental implications". Consulta directa a `api.crossref.org/works/<doi>` confirmou que esse DOI resolve exactamente para o título do banco — mesmos 4 autores, mesmo DOI, só o título foi alterado entre o pre-proof e a versão publicada. Não é obra diferente; CONFERE.

  📌 **Achado de metadado sem acção no PDF (linha 3963, KAPUR et al., 2008):** o campo `abstract` do banco descreve um estudo de LCA de alimentos, sem nenhuma relação com o artigo real (dinâmica de estoques de cimento nos EUA) — DOI, título e autores batem perfeitamente na frente do PDF. Defeito isolado de preenchimento do campo `abstract`, não do PDF nem da atribuição da linha; fica registado para a Kiê corrigir esse campo separadamente.

  ILEGÍVEL novo (linha 3788, LANZA et al., 2022, `(asce)st.1943-541x.0003201.pdf`): confirmado pessoalmente com `download_file_content`+PyMuPDF — texto genuinamente cifrado em todas as páginas (fonte com mapeamento quebrado), precisa de OCR. NAO_ENCONTRADO da rodada (linha 4998, SILVA et al., 2013) foi **revertido para CONFERE** após verificação pessoal — é o mesmo caso já documentado no vault de páginas 0–5 com defeito de stream PDF; páginas 6–9 extraem texto real e confirmam o artigo certo.

  ✅ **4 dos 5 ILEGIVEL resolvidos por OCR local (2026-08-31), a pedido da Kiê.** `tesseract` instalado na máquina da sessão; PDF descarregado via `download_file_content` (ou, quando >10MB, via o novo workflow `shrink-drive-pdf.yml` — ver infra abaixo), páginas renderizadas a 250dpi com PyMuPDF e OCR local. **LANZA (3788)**, **ASDRUBALI (4416)**, **BRUCE (3951)** e **DRIESSEN (1029)** — todos CONFERE: título, autores e DOI (quando impresso) lidos directamente da caixa de citação da p.1, batendo com o banco. **ARROYO (5022) continua ILEGIVEL** — o ficheiro (93MB) é o volume inteiro de um proceedings da Springer, não só o capítulo; a compressão via Ghostscript no runner ficou presa mais de 12 minutos sem progredir (provavelmente centenas de páginas de imagem em alta resolução) e foi cancelada. Seria preciso primeiro isolar o intervalo de páginas do capítulo (via TOC) antes de comprimir/OCRizar só essas páginas — não tentado, por ser a única linha das 5 já `Rejeitado` (fora do funil activo). `VERIFICACAO_TITULO_AUTOR_DOI.csv` actualizado nas 4 linhas resolvidas.

  🚨🚨 **Achado grave — dois PDF_ERRADO da primeira ronda (2026-08-17) nunca chegaram a ser corrigidos no banco**, descobertos ao investigar os 35 PDF_ERRADO a pedido da Kiê (2026-08-31). Ao contrário das outras 33 linhas (todas já resolvidas por soltura, troca ou novo download antes desta sessão — conferido programaticamente: célula actual ≠ nome do ficheiro que o CSV mestre marcou como errado, ou comentário documenta a correcção), estas duas mantinham **o mesmo ficheiro errado desde jun/2026**, com o histórico `P:` de C1-C6 inteiro construído sobre ele e, mais grave, **avaliações E2 por PDF (lotes de 25 e 28/08) feitas sobre o conteúdo errado** sem que o veredito PDF_ERRADO alguma vez tivesse sido aplicado à linha — exactamente o cenário que a regra geral da Kiê de 2026-08-31 (anular tudo, sobretudo E2) foi criada para cobrir.
  - **Linha 4459 (HADIZADEH-BAZAZ, jmse11020433):** a célula continuava a apontar para `HADIZADEH-BAZAZ et al., 2023.pdf`, que contém o artigo irmão jmse11091656 (o mesmo dos mesmos três autores, correctamente ligado à linha 4460 desde 30/08). O ficheiro certo (jmse11020433, DOI confirmado na frente) estava **órfão no Drive desde 23/08** sob o nome `...2023b.pdf` — tinha sido solto da linha 4460 nessa data por se presumir, erradamente, que a 4459 já tinha uma cópia sua. Corrigido: ficheiro órfão renomeado para a convenção e religado à 4459; anulados C1/C3/C4/C5/C6 (`P:` removido), `E1_moldavel`, `E1_construcao`, `E2_resistencia`, `E2_co2`, `etapa_saida`, `criterio_saida`.
  - **Linha 4173 (ONYELOWE, CEJ-2022-08-11-03):** a célula apontava para `ONYELOWE et al., 2022.pdf`, que contém o artigo irmão CEJ-2022-08-12-018 (auto-citação entre artigos do mesmo grupo — mesmo padrão catalogado noutros casos — já correctamente ligado à linha 4174 desde 30/08). O artigo certo **não existia em nenhum ficheiro do Drive**; localizado como gold OA via Unpaywall (`civilejournal.org`) e despachado para o Drive pelo `push-to-drive.yml`, conferido por leitura antes de ligar à linha. Mesma anulação aplicada.
  - Ambas encontradas por um varrimento programático que compara, para cada uma das 35 linhas PDF_ERRADO, o nome do ficheiro actual na célula contra o nome que o CSV mestre marcou como errado **e** procura por marcadores de correcção no comentário (`pdf solto`, `PDF ERRADO`, `pdf reatribuido`, etc.) — as únicas duas sem nenhum marcador e com o mesmo nome de ficheiro desde então. As outras 33 (contando cada linha do grupo ZHOU como uma) estão todas ou já corrigidas (a maioria pelo lote de 117 PDFs de 30/08) ou correctamente soltas à espera do PDF certo (`3692`, `3233`, `300`, `2880`, `4991`, `3612`, `678`, `1273`, `1900`, `4131`, mais a `3855` já fechada nesta sessão) — nenhuma delas tem histórico `P:`/E2 pendente de anulação.

  ✅ **Achado colateral FECHADO em 2026-08-31 — Terceira Leva da Conferência.** A lacuna descrita acima (45 ficheiros integrados depois do corte de 31/08, nunca passados pelo protocolo reforçado) foi fechada a pedido da Kiê no mesmo dia: worklist `VERIFICACAO_PENDENTE3_2026-08-31.csv` (45 ficheiros), 3 subagentes em lotes de 15, cada um a abrir os PDFs de verdade via `mcp__Google_Drive__read_file_content`. **45/45 CONFERE** — nenhum PDF_ERRADO novo. `VERIFICACAO_TITULO_AUTOR_DOI.csv` fica com 1.999 linhas, cobrindo **100% dos 1.970 nomes de ficheiro distintos ligados a linhas vivas do banco**, confirmado por reconciliação programática (0 residuais). Dois lotes confirmaram de forma independente que a correcção da linha 4459 (HADIZADEH-BAZAZ) feita mais cedo nesse dia está correcta.

  ✅✅ **CSV MESTRE LIMPO — sem entradas duplicadas, substituídas em vez de acumuladas (2026-08-31).** A Kiê reparou que a contagem de `PDF_ERRADO` continuava em 35 mesmo depois de a maioria já estar corrigida — porque cada correcção acrescentava uma entrada nova ao CSV sem remover a antiga (que descrevia o ficheiro errado histórico). Pediu para o CSV ficar com o estado actual apenas, e o histórico preservado à parte. Feito: reconciliação linha a linha entre o CSV e a coluna `pdf` do banco encontrou **38 entradas obsoletas** (removidas), **12 entradas corrigidas/reconstruídas** (10 delas reaproveitando prova já obtida em auditorias anteriores — o DOI descrito na nota do registo errado batia exactamente com o `doi` que a linha certa já tinha no banco, sem precisar reabrir o ficheiro; a 11ª e 12ª são os achados HADIZADEH-BAZAZ/ONYELOWE já descritos acima) e **3 entradas estendidas** para cobrir uma linha `Duplicado` irmã que partilha legitimamente o mesmo PDF. Resultado: **1.972 entradas, 1.970 CONFERE, 0 PDF_ERRADO, 0 NAO_ENCONTRADO**, só os 2 casos genuinamente por resolver (ARROYO ILEGÍVEL, PACHECO-TORGAL INDETERMINADO). Confirmado por reconciliação final: 0 linhas do banco sem entrada, 0 linhas com mais de uma entrada válida, 0 lixo obsoleto. **Achado extra desta limpeza:** a linha 4999 (AGUIAR) tinha o mesmo problema do 4459/4173 mas disfarçado — o PDF errado foi substituído no MESMO nome de ficheiro em 22/08 (não renomeado), por isso o casamento automático por nome não detectava que a entrada antiga (PDF_ERRADO, 18/08) já não descrevia o conteúdo actual; corrigida manualmente. Histórico completo (o que estava errado, o que substituiu, quando) preservado em `RELATORIO_LIMPEZA_CSV_MESTRE_2026-08-31.md` — é agora o documento de referência para esta limpeza; o CSV mostra só o estado vivo.

  ✅ **Investigação dos PDF_ERRADO ainda abertos — 2 casos fechados, 4 documentados com o link certo.** A pedido da Kiê, dois subagentes investigaram (via Unpaywall + WebSearch) os 11 linhas vivas que continuavam sem PDF por terem sido soltas de um ficheiro errado. Primeiro, 2 dessas 11 revelaram-se não precisar de nada: **linhas 3233 e 300 são `Duplicado`** de outras linhas (3232 e 3389) que já têm o ficheiro certo — Duplicado não precisa de ficheiro próprio. Dos 9 casos genuínos restantes:
  - **Linha 3855 (KANE, biochar/CDR) e linha 4991 (OSORTO, dissertação UnB) — FECHADAS.** Links de acesso aberto confirmados por leitura completa do conteúdo (não só metadados) e integrados de imediato via `push-to-drive.yml`: Kane via OSTI (`osti.gov/servlets/purl/2545759`, repositório do DOE — DOI e os 10 autores conferem exactamente); Osorto via repositório institucional da UnB (`repositorio.unb.br`, handle `10482/49254` — ficha catalográfica, orientadora e banca confirmam ser a tese genuína, não o artigo derivado MDPI já identificado como obra diferente).
  - **✅ Linhas 678/1273/1900/4131 (Riofrio, bamboo/bagaço geopolímero), 3612 (Polo-Mendoza, warm mix asphalt) e 3692 (Chen/Yuan, asfalto) — RESOLVIDAS (2026-09-05/06), nota abaixo corrigida em 2026-09-19 (ficou desactualizada meses sem ninguém reparar).** Os três PDFs (`RIOFRIO et al., 2022 - j.cscm.2022.e01150.pdf`, `POLO-MENDOZA et al., 2023 - j.rineng.2023.100984.pdf`, `CHEN et al., 2023 - j.trd.2023.103874.pdf`) estão no Drive desde 05-06/09 e já ligados às respectivas linhas; todas as três com `E2_resistencia=Rejeitado` (já lidas e triadas na Etapa 2, saída por falta de relevância estrutural, não por falta de ficheiro). 678/1273/1900 são `Duplicado` da 4131 e nunca precisaram de ficheiro próprio. **Nota histórica (só para registo):** o bloqueio original era o ScienceDirect devolver 403 a pedidos automatizados da sessão interactiva (WebFetch e `curl`) mesmo sendo Gold Open Access confirmado via Unpaywall — contornado nalgum momento entre 31/08 e 05/09, provavelmente pelo IP diferente do runner do `push-to-drive.yml` não estar bloqueado do mesmo jeito.
  - **⚠️ Linha 2880 (Meshram, blast furnace slag, DOI `10.1002/ep.14503`) — AINDA em falta (confirmado 2026-09-19).** Unpaywall confirma `is_oa: false` (Wiley, sem repositório com cópia). Os dois ficheiros no Drive com "Meshram" no nome (`MESHRAM, 2024i.pdf` e `MESHRAM et al., 2024.pdf`) são **a mesma obra errada** (`10.1007/s42452-024-06253-x`, "red mud paving blocks") — nenhum é o artigo certo. Só resta CAPES ou pedir directamente aos autores; a Kiê vai enviar o PDF directamente. **Linha 3692 (Chen/Yuan) NÃO está neste grupo** — ver acima, já resolvida.

  📌 **Infra nova — `shrink-drive-pdf.yml` (2026-08-31):** complementa o `push-to-drive.yml` para o caso inverso — um PDF do Drive grande demais para `download_file_content` (teto de 10MB). Busca o ficheiro por `fileId` via rclone (`rclone backend copyid`), comprime com Ghostscript (perfil `/ebook` ou `/screen`) e reenvia para o Drive com outro nome. Usado com sucesso em `BRUCE, 2022.pdf` (13,5MB→582KB); falhou por lentidão (não por erro) em `ARROYO et al., 2025.pdf` (93MB, cancelado após 12min sem progresso) — para volumes deste tamanho seria preciso primeiro isolar o intervalo de páginas do capítulo alvo antes de comprimir o livro inteiro.

  ✅ **Extensão — `first_page`/`last_page` opcionais no `shrink-drive-pdf.yml` (2026-09-22, PR #225).** Resolve exactamente o caso "livro inteiro" que a nota acima previa: dois inputs novos (retrocompatíveis, vazio = comportamento antigo) fazem o Ghostscript isolar só um intervalo de páginas do PDF original (`-dFirstPage`/`-dLastPage`) antes de comprimir — o recorte fica minúsculo, muito abaixo do teto de 10MB, e sem o truncamento silencioso da armadilha nº7 (que corta por número de caracteres, não por página). Validado no caso **ISAIA 2021** (linha 5055, 10,6MB — nem a compressão `/ebook` do ficheiro inteiro, 8,39MB, bastava, porque `download_file_content` continuava a falhar "session expired" na armadilha nº8): dois recortes (`cap5 vidautil pp230-240`, 546KB; `cap6 co2 pp277-323`, 2,06MB) descarregaram sem problema e deram a Tabela 5.16 (vida útil) e a Tabela 6.5 (CO2) completas, fechando as 12 linhas de `dados_fck` que faltavam vida útil (row_id 2847/LYRA, já fechada por outra via) e CO2 (row_id 5055/ISAIA). Ficheiros temporários dos recortes movidos para o lixo do Drive depois de extraídos.
- **🔴 Tarefa #7 — confirmação C2 por PDF e extração de metanálise: PARADA, e é o que falta fazer.** Medido a 2026-08-23: dentro do funil de 1.248, **1.161 linhas ainda têm o C2 só com `R:`**, e nenhuma delas está sem ficheiro PDF. Estava em «1.325 linhas pendentes, próxima a 2688» quando a conferência a interrompeu. **Não retomar do ponto onde ficou sem antes ler `PENDENTES_DECISAO_KIE_2026-08-17.csv`**: a conferência mostrou que parte das decisões `P:` anteriores tinham sido tomadas sobre o ficheiro errado. `meta_analysis_base.xlsx` tem 1.694 linhas na aba `dados_fck`. **Não há contaminação numérica** — das 41 linhas afectadas, 20 têm linha própria em `dados_fck` e **todas as 20 têm `fck_mpa` vazio** —, mas 11 têm `fonte_no_pdf` com texto citado do PDF errado.
- **🚨 PRIORIDADE ABERTA — colisões de PDF (descoberta 2026-08-13):** a convenção `SOBRENOME et al., ANO.pdf` **não é única**, e por isso **67 linhas estão associadas ao PDF de outro artigo — 49 delas já com decisão `P:` tomada sobre o artigo errado**. Inventário completo em `AUDITORIA_COLISOES_2026-08-13.csv`. **Anuladas em 2026-08-15** (69 linhas, incluindo 2 indeterminadas); lista de PDFs a rebaixar em `PDFS_A_REBAIXAR_COLISOES.html`.
- **🚨🚨 SEGUNDA FRENTE — as 80 linhas `A_VERIFICAR` (fechada em 2026-08-16):** eram as linhas em que o DOI do banco não aparecia no texto do PDF. Abertas **uma a uma** a pedido da Kiê. Resultado: **54 PDF_ERRADO, 23 CONFERE, 2 ilegíveis, 1 pendente** — ver `VERIFICACAO_80_A_VERIFICAR_2026-08-16.csv`. Das 54 erradas, **18 já tinham decisão `P:` tomada** sobre o artigo errado e **8 alimentaram 14 valores de `fck` na `meta_analysis_base.xlsx`** que vieram do artigo trocado. **✅ Anuladas em 2026-08-16** (a Kiê autorizou; 36 das 54 já tinham sido anuladas a 15/08 pela outra via, o que as confirmou por dois caminhos independentes). Nota metodológica: o grupo A_VERIFICAR tem taxa de erro de **68%**, contra **0%** nos 375 pares já confirmados; "DOI ausente do texto" é, portanto, um sinal forte de ficheiro trocado, não um artefacto de extração.
- **🔤 Convenção de nome nova (autorizada pela Kiê, 2026-08-16):** `SOBRENOME et al., ANO - sufixo-do-DOI.pdf`. Aplica-se aos PDFs novos e, retroactivamente, aos existentes. **Só é seguro renomear pares já confirmados** — renomear pelo DOI do banco um ficheiro que não foi conferido carimba o erro no nome. Estado: **✅ 307 de 307 renomeados (concluído 2026-08-16)** — Drive + `articles_final.xlsx` (valor da célula e alvo do hyperlink) em sincronia, verificado célula a célula; nenhum nome novo colide com outro. Registo completo em `RENOMEACAO_PDFS_2026-08-16.csv` e script `renomear_local.py` (lê esse CSV) para a Kiê aplicar o mesmo na pasta local, que o Drive não alcança. Os PDFs **fora** deste conjunto mantêm o nome antigo de propósito — são os pares por confirmar. **+7 renomeados em 2026-08-16** depois da Opção A (2616, 2689, 2912, 2951, 2986, 3208, 3213), que estavam retidos pela partilha de nome e deixaram de estar. Restam **1.338 ficheiros de dono único ainda com o nome antigo**: são os pares que ninguém conferiu, e renomeá-los pelo DOI do banco carimbaria o erro no nome — não fazer sem confirmar primeiro. **✅ +52 renomeados em 2026-08-16**, os nomes que a auditoria da Terceira Frente tornou seguros — Drive sem nenhum nome antigo do lote, banco sincronizado (60 células, contando as linhas `Duplicado` da mesma obra). Total na convenção nova: **366 ficheiros**. Ficam de fora, de propósito: `SILVA, 2013i.pdf` (dissertação sem DOI, nada para sufixar) e `WU et al., 2014.pdf` (não pertence a nenhuma linha — é cópia do artigo da 3621; não apagar sem a Kiê autorizar).

  ⚠️ **Armadilha nº3 — hyperlink codificado em URL (descoberta e corrigida em 2026-08-16):** o alvo do hyperlink guarda o caminho com os espaços em `%20` (`.../BATUECAS%20et%20al.,%202021a.pdf`), enquanto o valor da célula tem espaços normais. Um `target.replace(nome_antigo, nome_novo)` **falha em silêncio** — não levanta erro, apenas não substitui nada, e a célula fica com o nome novo a apontar para o ficheiro antigo. Foi o que aconteceu a **249 linhas** (189 da leva dos 307, 60 da dos 52); todas corrigidas. A verificação que deixou passar o problema comparava o valor da célula com o alvo **sem descodificar o URL** — comparar sempre com `urllib.parse.unquote(target)`. A correcção segura é substituir a última componente do caminho (depois do último `/`) e repor os espaços como `%20` se o segmento original os tinha assim.

  ✅ **Defeito dos hyperlinks desalinhados — FECHADO em 2026-08-23.** Eram 30 linhas (`HYPERLINKS_DESALINHADOS_2026-08-16.csv`) em que o valor da célula tem sufixo de desambiguação (`BARBHUIYA et al., 2024c.pdf`) e o hyperlink aponta para o nome base (`BARBHUIYA et al., 2024.pdf`). Ficou meses em aberto por se supor que resolver exigia ir ao Drive verificar cada nome. **Não exigia:** os 28 valores de célula estavam **todos na lista mestra da conferência, todos `CONFERE` e todos atribuídos exactamente à linha em questão** — logo o ficheiro existe e é o certo, e era o hyperlink que estava preso ao nome antigo. Em metade dos casos o nome antigo pertence a *outra linha do banco*, pelo que seguir o link abria o artigo errado. Mais 5 casos apanhados numa varredura ao banco inteiro (2 com caminho absoluto do Windows, 3 sem hyperlink). **Auditoria final: das 2.042 células com ficheiro, zero desalinhadas.** Registo em `HYPERLINKS_REALINHADOS_2026-08-23.csv`.

  💡 **Lição a reter:** antes de mandar uma verificação ao Drive, ver se a `VERIFICACAO_TITULO_AUTOR_DOI.csv` já responde. Um ficheiro que lá está foi aberto e lido — a sua existência e a sua atribuição já estão provadas, de graça.

  ⚠️ **Armadilha do conector Drive nº1 (descoberta 2026-08-16):** `search_files` devolve **no máximo 10 resultados por página**. Uma query com 12 títulos em `or` devolve 10 e cala-se sobre os outros 2 — parece que os ficheiros não existem. Manter os lotes em ≤8 títulos, ou conferir sempre o número de resultados contra o número de títulos pedidos.

  ⚠️⚠️ **Armadilha do conector Drive nº2 (descoberta 2026-08-16) — a mais perigosa das duas:** `fullText contains 'frase de várias palavras'` **NÃO faz correspondência exacta de frase**. Devolve acertos por tokens soltos, e portanto dá **falsos positivos**. Verificado: `PITTAU, 2019i.pdf` acertou na sonda `'Massive timber building'`, que não existe no texto (a leitura mostrou que o ficheiro é o artigo 296/012037); e `SILVA, 2013i.pdf` acertou em `'Influence of service life'`, que tem **zero** ocorrências no ficheiro. **Só usar sondas de token único e distintivo** — o sufixo do DOI (`su16020484`, `j.eti.2024.103857`) é o ideal. Para decidir de quem é um ficheiro, sonda de frase não serve; ou é DOI, ou é abrir e ler.

  ⚠️ **Armadilha do conector Drive nº6 — `pageSize: 100` não pagina** (medida 2026-08-24). O parâmetro `pageSize` existe e aceita valores acima de 10 (a nota da armadilha nº1 descrevia o valor por omissão, não um limite). Mas com `pageSize: 100` **as páginas sobrepõem-se e o avanço colapsa**: página 1 dá 100 ficheiros novos, a 2 dá 69, a 3 dá 59, a 4 dá **3**. A esse ritmo seriam centenas de chamadas para varrer a pasta.

  ✅ **A receita certa é `pageSize: 1000`:** a pasta inteira sai em **2 chamadas** (1.000 + 903). E tem um efeito colateral que vale ouro: com 1.000 o resultado excede o limite de tokens, pelo que o harness **grava-o num ficheiro** e devolve só o caminho — um script Python lê daí e escreve o CSV, e **o conteúdo nunca entra no contexto**. Foi assim que as 1.900 entradas do `DRIVE_FILEID_MAP.csv` foram capturadas a custo praticamente zero.

  📌 **`DRIVE_FILEID_MAP.csv` — o mapa `nome de ficheiro → fileId` da pasta dos PDFs** (criado 2026-08-24, 1.900 entradas, 1.898 delas PDFs). Cobre **os 1.591 nomes da lista de trabalho da Etapa 2 com correspondência exacta**, acentuados incluídos. Usar sempre este mapa em vez de `search_files` por título: poupa uma chamada por artigo e **elimina de raiz a falha das buscas com diacríticos** (`title = 'GALÁN-MARÍN et al., 2015.pdf'` não encontra nada). Zero `fileId` repetidos e zero títulos repetidos — não há colisão de nome dentro da pasta do Drive. A cobertura foi provada por **dupla travessia independente**, não presumida.

  💡 **Truque para ler PDF grande sem rebentar o contexto:** `read_file_content` num PDF de artigo devolve 80–260 mil caracteres e falha por excesso de tokens, mas **grava o resultado num ficheiro** e dá o caminho. Ler daí só os primeiros ~1.200 caracteres basta para identificar título e autores; e dá para contar ocorrências de um termo no texto todo com um script, que é como se apanham os falsos positivos da armadilha nº2.

  ⚠️⚠️ **Armadilha do conector Drive nº7 — `read_file_content` trunca documentos longos SEM AVISO** (descoberta 2026-09-06, casos BILAR 2016, WASKOW 2019, SPOSITO 2024, LUVIZAO 2023): para teses/dissertações de +100 páginas, `read_file_content` corta o texto num ponto fixo (medido entre ~135.000 e ~182.000 caracteres, independente do tamanho do PDF) sem qualquer sinal de corte — o resultado parece um documento completo. Já escondeu o **capítulo de resultados inteiro** (BILAR: 135.206 de 304.522 caracteres reais, perdendo ~56%; LUVIZAO: só chegou à p.79 de 288, ainda na revisão bibliográfica) e por pouco não inverteu uma decisão de Etapa 2 (SPOSITO: os valores de resistência que salvavam a linha estavam só na parte cortada). **Nunca concluir Rejeitado por "ausência de valor" num documento longo sem confirmar por texto completo primeiro.** Comprimir o PDF (`shrink-drive-pdf.yml`) não resolve — `read_file_content` trunca no mesmo ponto de caracteres independentemente da compressão (testado explicitamente no caso LUVIZAO, três compressões sucessivas, mesmo corte).

  ⚠️⚠️ **Armadilha do conector Drive nº8 — `download_file_content` pode falhar "session expired" de forma determinística, independente do tamanho do ficheiro** (casos COSTA 2026-08-31 e LUVIZAO 2026-09-06): mesmo um PDF bem abaixo do limite de 10MB (testado a 7,57MB) pode falhar sempre, em toda tentativa, sem nunca recuperar sozinho — não é o mesmo problema da armadilha de tamanho, é uma instabilidade por ficheiro/sessão. **Contorno que funcionou no caso LUVIZAO nessa altura:** um `mcp__Toolkit__googledrive_download_file` que devolvia uma URL S3 temporária assinada. ⚠️ **Correcção (2026-09-22, caso ISAIA): esse tool já não existe na instalação actual do servidor Toolkit** — confirmado por `toolkit_info`, que só lista os adaptadores whatsapp/youtube/credito/mercado/googletasks, nenhum Drive. Não tentar mais este canal. **O contorno que funciona hoje é o `shrink-drive-pdf.yml` com `first_page`/`last_page`** (ver a entrada "Extensão" mais abaixo) — isola só o intervalo de páginas necessário antes de comprimir, o que evita ao mesmo tempo o teto de 10MB desta armadilha nº8 e o corte por caracteres da armadilha nº7, porque o PDF resultante nunca atinge nenhum dos dois limites.

  ⚠️ **O scratchpad é partilhado entre lotes — não confiar em nada que já lá esteja** (constatado 2026-08-18, lote 86): o subagente encontrou um `rows.json` com as 15 entradas do lote 80 ainda lá. Não contaminou o resultado, mas podia. Duas defesas: dar aos ficheiros de trabalho um nome que inclua o número do lote, e **nunca** reutilizar um ficheiro do scratchpad sem o reescrever primeiro. A verificação que apanha isto na integração é comparar `doi_pdf` com `doi_banco` linha a linha — dados de outro lote quase nunca batem com o DOI do banco deste.

  💡 **MD5 do texto extraído como detector de cópias:** dois dumps com o mesmo md5 são o mesmo documento. Foi assim que se provou que `YU, 2024i.pdf` e `YU et al., 2024.pdf` são duas cópias físicas da mesma obra. ✅ **A linha 3508 já não está sem PDF próprio** — a Kiê descarregou-o e foi integrado a 2026-08-21 como `YU et al., 2024 - j.jobe.2024.110929.pdf`; relido e triado por PDF a 2026-08-23 (C1–C6 = P:Aceito).

  📌 **O campo `Title` mentiroso da *Ambiente Construído* é do gabarito da revista, não do ficheiro** (2026-08-18): três ficheiros distintos — `SILVA, 2018e.pdf`, `BORGES, 2014.pdf` e `PASSUELLO et al., 2014.pdf` — trazem no metadado interno, no offset 0, o mesmo título alheio: «VANTAGENS E DESVANTAGENS DA UTILIZAÇÃO DE PELES-VERDES EM EDIFICAÇÕES RESIDENCIAIS EM PORTO ALEGRE SEGUNDO SEUS MORADORES». É o modelo de PDF da revista que arrasta esse título. **Não é quimera em nenhum dos casos** — o teste é sempre o mesmo: se o título do offset 0 não reaparecer no corpo, é lixo de metadado. Contar com que volte a aparecer noutros ficheiros da mesma revista.

  📌 **O campo `doi` vazio do banco não é informação em falta — é defeito de preenchimento** (medido em 2026-08-18): dos 34 artigos sem `doi`, **32 têm o DOI dentro do campo `url`**; verificado em 28 ficheiros (lotes 91 e 92) que o DOI do `url` é exactamente o impresso na frente do PDF, sem uma única excepção. As 59 teses são o caso oposto: 57 não têm DOI no `url`, mas têm o *handle* do repositório institucional, que é o identificador certo para esse tipo de obra. ⚠️ O DOI tirado do `url` é **metadado do banco, não prova sobre o ficheiro** — serve para dar a hipótese a testar (está impresso na frente?), nunca para dispensar a abertura do PDF.
- **✅ TERCEIRA FRENTE — nomes de ficheiro partilhados (fechada em 2026-08-16):** o banco tinha **255 nomes a servir mais do que uma linha**. Separando o joio: **196 são duplicados legítimos** (as várias linhas são a mesma obra, o ficheiro está certo para todas) e **54 eram atribuição ambígua** — obras diferentes a disputar o mesmo ficheiro. Todos os 54 resolvidos, por três vias: 31 pelo cruzamento com o `VERIFICACAO_DOI_PDF_WORKLIST.csv` (que já tinha testado a presença do DOI no texto), 17 por sonda de DOI nova no Drive, e 6 abrindo o ficheiro. Resultado: **73 linhas ficaram sem PDF** pela Opção A (56 Inconclusivo, 9 Duplicado, 8 Rejeitado) — registo em `SOLTURA_PDF_OPCAOA_2026-08-16.csv`. **Hoje há zero nomes ambíguos no banco.**

  Achados que vale a pena reter: **em 7 casos o dono era o oposto do que a ordem do banco sugeria** (LIU 2024→4541, PUSHKAR 2022b→4483, XU 2024→3777, ZHOU 2023→4863, KARLSSON→4377, MOSTAFAEI→4263, SILVA→2850) — nos dois últimos a presença do DOI do outro candidato era **auto-citação entre artigos do mesmo grupo**, que só a leitura desfaz. E **um ficheiro não era de nenhuma das linhas que o reclamavam**: `WU et al., 2014.pdf` é o artigo 10.1016/j.rser.2014.04.070 da linha 3621, que já tem PDF próprio — é uma cópia redundante, e as duas linhas que apontavam para ele (3314, 4882) ficaram sem PDF.

  Nota que continua válida: em vários dos casos errados o PDF «errado» é afinal o PDF *certo de outra linha do banco* (2951/4128, 2986/4028, 2912/3499, 2689/4790) — os ficheiros não se perderam, foram mal atribuídos.
- **Auditoria de qualidade dos dados (12/07/2026 → 03/08/2026):** ✅ CONCLUÍDA — ver `PENDENCIAS_AUDITORIA_2026-07-12.md`. 10 achados (cascata quebrada, C8 sem prefixo `R:`/`P:`, 596 resíduos de C7, linhas "Sem acesso" com PDF já disponível, status_triagem dessincronizado de decisões já tomadas por PDF etc.) — todos resolvidos, **incluindo a última pendência**: linha 2897 (di Summa et al., 2023, *Structural Concrete*, DOI `10.1002/suco.202300645`), cujo PDF chegou no lote de 2026-08-30 (ver bullet "🆕 Integração de 117 PDFs" abaixo).

- **🆕 Integração de 117 PDFs baixados manualmente/automaticamente por DOI (2026-08-30):** a Kiê colocou (manual + via script automático de download por Unpaywall/mdpi-res.com/Sci-Hub) 117 PDFs na pasta `BAIXADOS MANUALMENTE` do Drive — muito mais do que os "vários" inicialmente pedidos: um lote de 10 com nomes manuais (`3_Jesaun_...`, `10.1155_2022_...` etc.) e um lote automático de 107 nomeados pelo próprio DOI (barra→underscore), documentado em `_STATUS_download_pdfs_20260830.md` e `_NOTA_metodo-download-pdf-openaccess.md` (ambos dentro da própria pasta do Drive). Fluxo aplicado: casar cada ficheiro com a linha do banco por normalização do DOI (contra as colunas `doi` **e** `url`, já que 2 das linhas tinham o DOI só no `url` — ver a nota "campo `doi` vazio" mais acima) → conferir por leitura completa (título/autor/DOI impressos) → renomear para a convenção `SOBRENOME et al., ANO - sufixo-do-doi.pdf` → mover da pasta de entrada para a pasta principal. Os 10 do lote manual e o caso da 4293 (redundante, já resolvido antes) verifiquei eu directamente; os outros 106 foram verificados por 8 subagentes em lotes de ~14, **todos CONFIRMA, zero PROBLEMA** — a âncora por DOI (ficheiro pedido exactamente por aquele DOI, não achado por busca de título) faz deste lote um caso de risco muito mais baixo do que a conferência título+autor+DOI de 2026-08-16→19.

  **Achado de bónus:** duas linhas (4119 e 4120) eram um par de duplicados nunca detectados — mesmo título, mesmos quatro autores, mesmo ano, uma delas sem DOI preenchido — ambas `Sem acesso`, ambas casaram com o mesmo ficheiro (`jwarm.22.00012`). Atribuí o mesmo PDF às duas; **não mudei o `status_triagem` de nenhuma para `Duplicado`** — a decisão de qual é a canónica é da Kiê, fica como achado registado, não como correção aplicada.

  **Dois ficheiros ficaram sem casamento seguro por DOI**, movidos para `PARA VERIFICAR` no Drive sem tocar no banco: `2996-ENARC2023.pdf` (Santos/Cila/Ribeiro, artigo de conferência sobre RCA em clínquer — título próximo mas não idêntico ao da linha 2790, a dissertação FRG+RCA de Tiago Assunção Santos já documentada na "armadilha da obra derivada pelo mesmo autor") e `Avaliacao_do_ciclo_de_.pdf` (Aguiar/Mattos/Esteves, DOI `10.6008/CBPC2179-6858.2021.006.0031` — título de "coprocessamento" parecido com o das linhas 4127 e 4999, mas nenhum bate exactamente; esta família de autores já tinha o mesmo problema documentado). Precisam de decisão da Kiê antes de atribuir a uma linha.

  ✅ **Investigação fechada (2026-09-22) — confirma-se que nenhum dos dois pertence a linha nenhuma do banco; falta só a decisão de criar linha nova ou descartar.**
  - **`2996-ENARC2023.pdf`** (ainda em `PARA VERIFICAR`, fileId `1yp40dUPUBzueiAryJiagCiyzxA5uiD4Q`): lido por completo. É "Utilização de resíduo de cimento de amianto (RCA) na produção de clínquer Portland..." de Tiago Assunção Santos (UEFS) + Marcelo Strozzi Cila (UFBA) + Daniel Véras Ribeiro (UFBA), trabalho do 8º ENARC 2023, **sem DOI impresso**. Confirmado que **não é a linha 2790** (essa é a tese UFBA do mesmo Santos, mas sobre FRG+RCA, autor único, já correcta e fechada desde 2026-08-31 como `SANTOS, 2022 - ufba.34967.pdf`). Busca por título e pelos apelidos Cila/Ribeiro nas 5.093 linhas: zero correspondência. Não reporta ACV/CO2 próprio (só cita um valor de terceiros na introdução) — teria dificuldade a passar C5 mesmo que ganhasse linha.
  - **`Avaliacao_do_ciclo_de_.pdf`**: já não está em `PARA VERIFICAR` — uma sessão anterior (2026-08-22) já o tinha renomeado e movido para a pasta principal como `AGUIAR et al., 2021 - CBPC2179-6858.2021.006.0031.pdf` (fileId `1YwrgNcQsX0Jk8_UdBpkmciFm6XCjCDCg`), mas **sem o ligar a nenhuma linha** — ficheiro órfão. É "Avaliação do ciclo de vida da cadeia no coprocessamento de resíduos industriais", David Barreto de Aguiar + Ubirajara Aluizio de Oliveira Mattos + Victor Paulo Peçanha Esteves, *Revista Ibero-Americana de Ciências Ambientais* v.12 n.6 (2021), DOI `10.6008/CBPC2179-6858.2021.006.0031` impresso na p.1 (via 1). Confirmado que é uma **terceira obra distinta** do mesmo grupo de autores: a linha 4127 (mesmos 3 autores) já tem o seu próprio PDF certo (`1980-5160.2021.v16n2.1712.pdf`, *Sistemas & Gestão*, sobre blendagem) e a linha 4999 (só David Barreto de Aguiar) já tem o seu próprio PDF certo (`AGUIAR, 2021.pdf`, tese UERJ) — nenhuma das duas é este artigo. Busca pelo DOI nas colunas `doi`/`url` e pelo nome do ficheiro na coluna `pdf`: zero correspondência.
  - ✅ **Decisão da Kiê (2026-09-23): descartar os dois.** Ambos movidos para o lixo do Drive (`trash_file`) — `2996-ENARC2023.pdf` (fileId `1yp40dUPUBzueiAryJiagCiyzxA5uiD4Q`) e `AGUIAR et al., 2021 - CBPC2179-6858.2021.006.0031.pdf` (fileId `1YwrgNcQsX0Jk8_UdBpkmciFm6XCjCDCg`, era o `Avaliacao_do_ciclo_de_.pdf`). Recuperáveis no lixo se for preciso reverter; nenhuma linha do banco foi tocada (não havia nenhuma a tocar). Item fechado.

  118 linhas ganharam PDF pela primeira vez; `status_triagem` promovido de `Sem acesso` para `Inconclusivo` nessas que estavam nesse estado (25 `Sem acesso` restam no banco, eram 60 no início da sessão). PR #31.

- **🆕 Etapa 2 — ciclo de dúvidas de critério "uma por vez" (em curso desde 2026-08-28):** a Kiê decidiu resolver as dúvidas de critério acumuladas da Etapa 2 uma de cada vez, em texto corrido no chat — **nunca com a ferramenta de múltipla escolha** (regra já registada em "Preferências de interação da Kiê" abaixo, reconfirmada nesta sessão). Fluxo por dúvida: apresentar → discutir → decidir → aplicar em `articles_final.xlsx` (colunas `E2_resistencia`=39, `E2_co2`=40, `etapa_saida`=43, `criterio_saida`=44) → se a decisão for generalizável, registar a regra nova em `lotes_etapa2/PROMPT_E2.md` (o ficheiro-mestre de critérios que os subagentes de cada lote seguem) → remover a linha de `lotes_etapa2/DUVIDAS_DE_CRITERIO.csv` → commit+push. **Três regras gerais novas ficaram vigentes** (todas já escritas em `PROMPT_E2.md`, não repetir aqui o texto completo):
  1. **"Total + divisor impresso no artigo" → CALCULAR e ACEITAR** (Kiê, 2026-08-28: *"sempre que for possível nós mesmos realizarmos os cálculos para chegar nos números que precisamos é aceito"*) — substitui a orientação anterior de registar DUVIDA. Se o artigo imprime o total (ex.: CO2 do edifício inteiro) e, em qualquer lugar do mesmo artigo — mesmo noutra tabela/figura do mesmo objeto — o divisor que normalizaria esse total (área, massa, volume), a divisão deve ser feita por nós, resultado marcado `[ALERTA ETAPA4: valor derivado por divisao total/divisor impresso no artigo, nao publicado como tal pelo autor]`, `confianca=media/baixa`. Aplicada à família de 8 linhas do lote 209 (2026-08-28).
  2. **"Catálogo comparativo sem atribuição a um sistema específico" → ACEITO**, não DUVIDA — uma tabela/faixa de classes de resistência apresentada como catálogo compilado da literatura (ou como os *bins*/variáveis de decisão do próprio modelo interno do artigo) conta como classe declarada mesmo sem estar amarrada a um sistema estudado específico. Fonte externa citada → registar `fonte_externa_resistencia` (ramo de citação do PRISMA); modelo interno do próprio artigo → aceitar sem registo de fonte externa. Aplicada a 7 linhas (lote 211, 2026-08-29).
  3. **Exceção 5b (Kiê, 2026-08-30): massa específica padrão do cimento Portland (3,15 t/m³)** pode reconstituir massa a partir de um resultado de CO2 dado por volume — **só** depois de investigação completa do artigo confirmar o mecanismo da inconsistência dimensional (caso HAN, linha 3881: a Kiê rejeitou uma primeira resposta minha por não ter lido o artigo inteiro antes de aplicar — "Você tem certeza absoluta de que a unidade é erro do autor... Você leu o artigo inteiro?"). Nunca aplicar por analogia sem reconfirmar o mesmo mecanismo noutro artigo. Sempre `confianca=baixa` + `[ALERTA ETAPA4: valor reconstituido assumindo massa especifica padrao do cimento (3,15 t/m3) nao publicada pelo artigo]`.

  Dúvidas resolvidas nesta sessão (2026-08-28→30): 2771 (SCOPE, 3671 — os 80 estudos revistos por essa RSL entram como fontes externas no PRISMA), a família "catálogo comparativo" (7 linhas), a família "total+divisor" (8 linhas), 3881 (HAN), 3923 (SHEN — mantida a rejeição, confirma que as regras 6/7 continuam vigentes), 4015 (LABAR), **4293** (colisão de PDF, não dúvida de critério — ver bullet de infraestrutura abaixo), 4323 (ZIVKOVIC — nova regra 9, figura motivacional agregando literatura = Rejeitado), 4327 (ILGIN — nova regra 10, classe só como exemplo de factor = Rejeitado), 4334 (YARDIMCI — resolvida por aplicação directa da regra "total+divisor", não era dúvida nova), 4403 (SAMUDRALA — Aceito após abrir o PDF: é revisão que compila o próprio tipo de mistura estudado, "kg/m3" no eixo era erro de rótulo copiado do eixo vizinho), 4425 (LATAWIEC — Rejeitado após abrir o PDF: fonte nomeada mas nenhum valor de MPa é impresso em lado nenhum do texto, nova regra distinguindo "fonte nomeada com valor" de "fonte nomeada sem valor"), 4535 (MADDALENA — Rejeitado, nova regra 11: compressão de um componente de reforço não cimentício, mesmo central ao dispositivo, não conta), 4550 (RAJAGOPAL — Rejeitado, nova regra 12: kg CO2-eq absoluto impresso mas sem a quantidade/unidade funcional de referência em lado nenhum do artigo, confirmado por leitura de texto **e** renderização visual das páginas), 4855 (KOCAK — CO2 Aceito com alerta forte: unidade funcional e inventário estão declarados, mas o valor contradiz os próprios inputs por ~1000×, provável erro de escala dos autores — diferente da regra 12, aqui não falta o dado, é preciso a Kiê reler com calma), 4741 (CHENG — Rejeitado, nova regra 13: cenário hipotético de "e se trocássemos de material" numa secção de estratégias futuras, extensão da regra 9 à resistência), 4883 (RAJAGOPALAN 2010 — Rejeitado, extensão do "teste operável" a estudos de LCA primários que modelam com processos genéricos de base de dados sem classe) e **4951 (SANZ-CALCEDO — Rejeitado, nova regra: figura sem escala numérica no eixo, valor existe mas é irrecuperável, confirmado por comparação com a figura ao lado que tinha escala normal — a última dúvida da fila desta ronda).**

  ✅✅ **Fila de dúvidas de critério zerada em 2026-08-30** — `lotes_etapa2/DUVIDAS_DE_CRITERIO.csv` tem **0 linhas em aberto**. As 12 dúvidas (11 genuínas + a 4293, que era colisão de PDF) foram todas resolvidas nesta sessão, uma a uma em texto corrido, seguindo a regra "abrir sempre o PDF completo — texto e imagem — antes de apresentar" (adoptada a meio da ronda depois de duas correcções da Kiê). Seis regras novas ficaram registadas em `PROMPT_E2.md` (regras 9–13, mais a nota do contraste KOCAK/RAJAGOPAL), prontas para os próximos lotes da Etapa 2 aplicarem directamente sem reabrir a mesma dúvida.

- **✅ Tarefa Supabase #1383 — revisão dos 69 rejeitados de CO2 por percentagem/índice sem conversão: CONCLUÍDA em 2026-09-14.** Das 69 linhas originais, 57 continuavam `Rejeitado` (12 já tinham virado `Elegível` por outra via, fora de escopo). Processadas em 6 lotes de subagentes (~10 cada) com leitura de texto completo + renderização visual das figuras quando necessário (não confiar só no texto extraído). Resultado: **52 CONFIRMA_REJEICAO** (nenhuma ação — a rejeição original estava correta, sem valor absoluto de CO2 recuperável em lugar nenhum do artigo) e **5 candidatas a reversão**, decididas uma a uma com a Kiê (regra: nunca em múltipla escolha):
  - **Linha 2687 (HAJIESMAEILI, UHPFRC para reforço de ponte) — ACEITE.** Figura 6 declara literalmente "100% stands for 151.3 t CO2eq" para o cenário-base, com S-UHPFRC e PE-UHPFRC lidos no mesmo gráfico normalizado (~65% e ~32%) — Regra 7 forma 1 (equivalência explícita impressa), valor próprio do estudo (SimaPro/Ecoinvent/IPCC2013), não citação externa. `status_triagem`→Elegível; 3 misturas extraídas para `dados_fck` (P-RC 151.300 kg CO2-eq direto, S-UHPFRC e PE-UHPFRC derivados por leitura gráfica, confiança média).
  - **⭐ Regra nova (Kiê, 2026-09-14): quando o CO2 reportado é citado de outro estudo mas o artigo é ele próprio uma REVISÃO alinhada ao propósito da metanálise, é ACEITO.** Esses artigos caem na Etapa 4 como "artigo de revisão", e os estudos secundários citados ficam pendentes de extração como entradas externas no fluxograma do PRISMA — mesmo tratamento já dado ao SCOPE et al. 2021 (linha 3671, ver `lotes_etapa2/SCOPE_2021_ESTUDOS_LCA_TAB_A1.csv`). Aplicada às **linhas 3001 (ONSONGO, revisão de cinzas agrícolas — cita baseline OPC por continente) e 3163 (NASIR, revisão de ligantes álcali-ativados — cita fator do NaOH)**, ambas com `document_type=Review` confirmado e `E2_resistencia` já aceite pelo mesmo padrão de compilação de terceiros. `status_triagem`→Elegível em ambas. **✅ Extração dos estudos secundários CONCLUÍDA para ONSONGO/NASIR (2026-09-22)** — `lotes_etapa2/ONSONGO_2025_ESTUDOS_SECUNDARIOS.csv` (13 estudos: os três pares que fundamentam o baseline OPC por continente — Ásia [18]/[19], América+Europa [20]/[21], África [29] — mais reduções de CO2 por substituição de clínquer e resistência) e `lotes_etapa2/NASIR_2024_ESTUDOS_SECUNDARIOS.csv` (22 estudos: as 18 linhas da Tabela 4 "Summary of LCA of AAMs" do próprio artigo, mais a fonte-base que essa tabela declara actualizar [193] e as citações directas no corpo do texto que fundamentaram a aceitação em E2_co2 — [206] Patrisia et al. 2022 é a citação central do "fator do NaOH", com [192]/[208] ao lado). Leitura completa dos dois PDFs via `mcp__Google_Drive__read_file_content`; 5 DOIs ficaram em branco por a referência do próprio artigo não os trazer impressos (nenhum inventado). Para o SCOPE, **catalogação fechada em 2026-09-22: 73 entradas** (69 códigos catalogados + 4 `NAO_ENCONTRADO_NO_ARTIGO`, ver abaixo) — `lotes_etapa2/SCOPE_2021_ESTUDOS_LCA_TAB_A1.csv`.

  ✅ **Os 4 códigos que faltavam (`Don19`, `Far17`, `Pet17`, `Rie19`) — investigados e fechados (2026-09-22).** A armadilha nº8 não se reproduziu desta vez (`download_file_content` funcionou de primeira); leitura de 100% do texto (23 páginas, inclui o corrigendum) + inspecção visual a 250dpi de Fig.5/Table A1 confirmam: **os 4 códigos genuinamente não têm entrada na lista de referências deste PDF** — não é lacuna de extracção. O próprio artigo (p.310 do texto) diz que a lista completa e definitiva dos ~71 estudos da amostra final vive num **material suplementar externo (OSM1, Mendeley Data/ScienceDirect, ligado ao DOI 10.1016/j.spc.2020.12.022)**, não embutida no PDF principal — a "Table A2" que a legenda da Fig.5 promete como glossário de abreviaturas acaba por ser, dentro deste PDF, uma tabela diferente (hotspots/drivers). Confirmado também que `Far17`/`Fra17` (Frangopol et al. 2017) e `Pet17`/`Pet18` (Petit-Boix et al. 2018) são pares visualmente distintos na figura, não erro de OCR/transposição — e que `Rie19` não corresponde a Rieradevall como primeiro autor (só aparece como último coautor de Pet18, e a convenção do artigo é sempre primeiro-autor+ano). Se a Kiê quiser mesmo os dados destes 4 estudos, o único caminho é obter o OSM1 externo — não está em lado nenhum do PDF.
  - **Os 2 casos restantes, decididos pela Kiê em 2026-09-14 depois de perguntas de clarificação:**
    - **Linha 4881 (SILGADO) — confirmado Rejeitado.** Pergunta da Kiê: "o resultado percentual dele é conversível?" Resposta: não — os resultados próprios (SimaPro/ReCiPe2016H) só saem em percentagem normalizada ao PC100-RHA0=100%, sem valor absoluto próprio do traço de 21 MPa em lado nenhum do artigo; a citação de Hu et al. (157/801,6 kg CO2-eq/tonelada) é unidade funcional diferente (produção de cimento/RHA, não o betão específico) e não está pareada no mesmo gráfico/base normalizada — sem divisor/equivalência impressa que permita converter.
    - **Linha 4931 (KONTRA) — ACEITE.** Pergunta da Kiê: "qual o sistema estrutural?" Resposta: parede de contraventamento (shear wall) de betão armado (RC), sistema lateral de um edifício de ensaio à escala real de 6 pisos (NHERI TallWood, Seattle), 34,4 MPa, com o total de CO2 (5,0E+04 kg CO2eq, Fig.5, ferramenta Athena IE4B) a cobrir betão+fundação+armadura sem decomposição por material. Decisão da Kiê: aceitar mesmo sem isolar só o betão — "ele vai entrar na família concreto armado". `status_triagem`→Elegível; 1 linha extraída para `dados_fck` (fck=34,4 MPa, co2=50.000 kg CO2-eq, confiança média, nota explícita de que é total do sistema RC completo).
  - Registo linha a linha (as 57, com decisão e motivo, já actualizado com estas 2 decisões finais) em `lotes_etapa2/REVISAO_CO2_PERCENTAGEM_RESULTADO_2026-09-14.csv`.

- **🚨🚨 REGRA E2 MAIS RESTRITIVA + REJEIÇÃO RETROATIVA DE 58 ARTIGOS (Kiê, 2026-09-21).** Durante a extração de vida útil, ao investigar a linha NEHDI et al. 2020 (4469, sem `fck`/`co2` extraído em `dados_fck` apesar de `E2_resistencia`/`E2_co2` = Aceito), a Kiê perguntou por que uma linha sem par extraível não tinha sido rejeitada logo em E2. Auditoria confirmou: havia **72 linhas de `dados_fck` (59 artigos distintos) com `fck_mpa` E `co2_valor` ambos vazios**, quase todas aceites em E2 pela "Regra 2" do `PROMPT_E2.md` (catálogo/citação/compilação sem dados próprios = Aceito, decisão de 2026-08-28). Isso era **≈10% de todo o funil Elegível** (598 artigos). A Kiê decidiu apertar o critério: **E2_resistencia/E2_co2 só podem ser Aceito se o artigo tiver, no próprio texto, um par fck+CO2 pareável a uma mistura/sistema específico** — citação/catálogo sozinho já não basta.
  - **58 dos 59 artigos rejeitados retroativamente** (`status_triagem`→Rejeitado, `E2_resistencia`/`E2_co2`→Rejeitado, `etapa_saida`=2, `criterio_saida`=E2_resistencia, comentário com a razão específica de cada um). `status_triagem` Elegível: 598→540. O único excluído da rejeição foi a linha 4350 (PAVLŮ) — não é caso de "sem dado", é linha legada de rastreabilidade cujos dados reais vivem noutras 14 linhas do mesmo artigo.
  - **2 dos 58 (Li Jiaqi 4081, Costantino 4804) tinham, além disso, um erro de leitura na aceitação original** — valores citados como "resistência/CO2 próprios" que a releitura integral confirmou serem lidos de eixo de gráfico sem rótulo numérico (Costantino) ou não existirem em lado nenhum do artigo (Li Jiaqi). Corrigidos pela mesma via.
  - **Regra 2 do `PROMPT_E2.md` foi revogada** (texto histórico preservado no ficheiro, marcado como superado) — não vale mais sozinha para `Aceito`; passa a exigir também um CO2 próprio pareável à mesma classe/mistura.
  - Nota de método: o veredito de cada um dos 58 já vinha **inteiramente documentado** por sessões anteriores (releituras completas de PDF já feitas em 2026-09-07/08 para a tarefa #7/metanálise, coluna `observacoes` de `dados_fck`) — não foi preciso reabrir nenhum PDF nesta rodada, só cruzar o achado com o critério novo.
  - `dados_fck` **não foi limpo** — as 72 linhas destes 58 artigos continuam lá (já sem `fck_mpa`/`co2_valor`, portanto sem contaminar nada), como registo histórico; decisão de as remover fica para a Kiê pedir se quiser.
  - Duas linhas ficam com achados adicionais por resolver, independentes da regra nova: **4125 (El Berdai)** — a sessão de 2026-09-07 não confirmou leitura completa (só resumo/introdução), pode ter valor de resistência algures no corpo não verificado; **4974 (Luvizão)** — investigação encontrou que a decisão `E2_resistencia=Aceito` original pode ter confundido **módulo de resiliência** (ensaio de pavimento, ordem de centenas/milhares de MPa) com `fck` (resistência à compressão) — sinalizado para revisão futura independentemente desta rodada.

- **🆕 Infra nova — push directo para o Drive via GitHub Actions + rclone (2026-08-30):** resolve a limitação de as ferramentas MCP do Drive (`create_file`, `googledrive_upload_file`) só aceitarem conteúdo colado inline no próprio tool call, com um teto de 5 MB — inviável para a maioria dos PDFs (um de 5,6 MB vira uma string base64 de ~1,85 milhões de tokens, muito acima do limite de saída de uma única resposta). Detalhe técnico completo, incluindo a armadilha do secret RCLONE_CONFIG, na secção **"Camada 5"** de "Processo de download de PDFs" mais abaixo. **Primeiro uso real (2026-08-30): fechou a linha 4293**, que desde a auditoria de colisões (2026-08-13) tinha o ficheiro errado no Drive (outro artigo de Onyelowe, `10.28991/CEJ-2022-08-11-03`, duplicata segura já ligada à linha 4173) — o PDF certo (`10.3390/buildings12070948`, obtido via CDN mdpi-res.com, ver `como_contornamos_o_akamai.md`) foi colocado no Drive pelo workflow, sobrescrevendo o ficheiro errado com o mesmo nome/fileId (não foi preciso mexer na célula nem no hyperlink). Retriada por leitura completa: `E2_resistencia`=Aceito (Tabela 1, Fc28 em MPa até 53), `E2_co2`=Rejeitado (único indicador ambiental é "environmental impact potential (P)" em percentagem, sem nenhum valor absoluto de CO2 no artigo inteiro — mesma família das rejeições por percentagem).

## Conferência PDF x banco por titulo+autor+DOI (em curso desde 2026-08-16)

A Kiê decidiu que cada PDF é aberto e conferido em **título, primeiro autor e DOI**, os três a bater. Registo em `VERIFICACAO_TITULO_AUTOR_DOI.csv` (1.422 ficheiros de nome antigo). Trabalho em lotes de 15 por subagente, um de cada vez, com auditoria minha entre lotes; atribuição e resultado de cada lote em `lotes_verificacao/`.

**Hierarquia de prova aceite para `CONFERE`** (da mais forte para a mais fraca; usar a primeira que se aplique):

1. **DOI do banco impresso na FRENTE do documento** + título e autor a bater. É a regra normal.
1b. **Bloco de auto-identificação do artigo, onde quer que esteja no documento** (aceite 2026-08-17): alguns periódicos imprimem o DOI **no colofão da última página**, num bloco do tipo `Recebido / Aprovado / DOI: … / Como citar: <autores>, <revista>, <volume>, <páginas>`. Isso **não é uma entrada da lista de referências** — é o próprio artigo a dizer como deve ser citado, o que é a afirmação de autoria mais forte que um documento pode fazer. Vale como via 1, mas registar como `via colofao` para não se confundir com a posição na frente. Caso ARAUJO PRADO 2022 (*Revista Tecnologia e Sociedade*, UTFPR): o cabeçalho da p. 1 traz só o URL do periódico, e o DOI está na p. 166.
   ⚠️ **Não usar isto como brecha.** A via 1b exige que o bloco seja de auto-citação — com "Como citar" ou equivalente e os dados do próprio artigo. Um DOI solto no fim do ficheiro, dentro de uma lista de referências, continua a não provar nada. Confirmar sempre que a lista de referências é distinta desse bloco.
2. **Crossref** (aceite 2026-08-16): quando o ficheiro é versão de autor sem DOI impresso, resolver o DOI do banco em `https://api.crossref.org/works/<doi>` e exigir que **título e lista completa de autores, pela mesma ordem**, batam com o PDF. É prova mais forte do que a nº3 — identifica a obra inteira, não só um sufixo. Verificado por mim no AREHART 2020 e no ARMSTRONG 2023.
3. **Manuscript ID** (aceite 2026-08-16): versão aceite cujo `Manuscript ID` é o próprio sufixo do DOI (ex.: `cjce-2015-0431.R1` para `10.1139/cjce-2015-0431`), com título, autor e revista a bater. Caso ALSHAMRANI 2016i.

➕ **Reforço por ISBN, para livros** (aceite 2026-08-16): quando a entrada é um **livro** e não um artigo, o DOI raramente vem impresso. Além do Crossref, exigir que o **ISBN do registo Crossref bata com o ISBN impresso na página de copyright do PDF**. Caso JOLLIET 2015i: `10.1201/b19138` devolve `type=book`, *Environmental Life Cycle Assessment*, CRC Press, cinco autores pela ordem da capa, ISBN 9781439887707 — o mesmo impresso no ficheiro. Não é uma quarta via, é um reforço que torna a via 2 praticamente inatacável para livros.

A coluna `doi_bate` guarda **qual** das vias foi usada (`sim`, `via colofao`, `via Crossref`, `via Manuscript ID`) para a natureza da prova não se dissolver num «confirmado» indistinto.

📌 **Divergência de idioma do título não é divergência** (2026-08-17): revistas bilingues registam o título numa língua e imprimem o PDF noutra. O banco pode ter o título em inglês e o ficheiro estar em português, e ser o mesmo artigo — confirmar por DOI, autor, revista, volume e paginação, não pela língua. Caso ARAUJO PRADO 2022. O mesmo vale para variação redaccional entre versão de autor e versão publicada (caso AJAYI 2015, post-print do Leeds Beckett).

📌 **Errata apensa ao mesmo ficheiro não é quimera** (2026-08-17): a Elsevier apende ao PDF do artigo, no fim, um bloco «Update» seguido do *corrigendum* do próprio artigo — com DOI próprio (o do corrigendum) e uma linha explícita «DOI of original article: <DOI do artigo>». São dois DOIs no mesmo ficheiro, mas **uma só obra**: não aplicar a regra da quimera. O que decide é essa linha de ligação e o facto de o DOI do banco estar na frente da p.1. Caso SCOPE et al., 2021 (`10.1016/j.spc.2020.12.022`, 21 páginas de artigo + pp. 22–23 de corrigendum `10.1016/j.spc.2021.05.014`), auditado por mim.

🆕 **Classe nova de PDF_ERRADO — a obra derivada pelo mesmo autor** (descoberta 2026-08-18, caso AGUIAR 2021, verificada por mim). O banco pede a **tese** (fonte BDTD, autor único) e o ficheiro é um **artigo de revista de 10 páginas** saído dessa tese, com DOI próprio e **três** autores. Não é colisão de nome, não é duplicado, não é ficheiro de outra pessoa: é outra entidade bibliográfica da mesma investigação. Sinais que a denunciam:
  - o **resumo impresso é texto diferente** do resumo do banco (comparar sempre, e sempre banco↔PDF);
  - **não há folha de rosto, ficha catalográfica nem página de banca** — uma tese tem-nas todas;
  - o corpo arrasta restos da estrutura de origem («o detalhamento da blendagem já foi realizada em capítulo anterior»);
  - o título impresso pode bater com o do `url` do banco e **não** com o `title` — foi o que aconteceu aqui.

  Esperar mais casos destes no grupo das teses: publicar artigos derivados da dissertação é a norma, e quem descarregou o PDF pode ter apanhado o artigo em vez da tese. **Previsão confirmada** — o segundo caso (OSORTO 2023, artigo na *Sustainability* da MDPI) apareceu dois lotes depois.

  ✅ **O teste mais barato e mais decisivo** (validado nos lotes 96 e 97): contar as ocorrências de «Dissertação», «Tese», «Ficha catalográfica», «Banca», «Orientador», «Mestre em», «Doutor em» e do **nome da universidade que o banco indica**. Numa tese brasileira genuína aparecem; num artigo derivado dão **zero**. Foi o que desmascarou o OSORTO e o SANTOS et al., 2022.

  ⚠️ **Duas ressalvas ao teste, ambas capazes de produzir um falso «não é tese»:**
  - **`grep -i` não dobra maiúsculas acentuadas.** Verificado por mim: num ficheiro com «FICHA CATALOGRÁFICA» e «ficha catalográfica», `grep -ic` devolve **1** e o `casefold()` do Python devolve **2**. Usar `casefold()` em Python, ou `grep -i` com as duas grafias.
  - **O vocabulário varia por universidade.** A USP usa «FOLHA DE APROVAÇÃO» em vez de «Banca» e «Mestrado — Programa de Pós-Graduação em…» em vez de «Mestre em» (caso SILVA 2013i, onde esses dois termos deram zero num ficheiro perfeitamente correcto); a UNIOESTE usa «Dados Internacionais de Catalogação-na-Publicação (CIP)» em vez de «ficha catalográfica»; a UnB/FAU vincula à Faculdade e não a um PPG nomeado. Zero em **alguns** termos não é sinal; zero em **todos**, incluindo o nome da universidade, é que é.
  - **A tese pode estar escrita em inglês.** Caso VERGARA 2019i (USP/Poli): «dissertação», «banca», «orientador» e «ficha catalográfica» deram **zero** porque o documento usa *Thesis*, *Doctoral advisor* e «Catalogação-na-publicação». Salvou-a o nome da universidade, com 8 ocorrências — é o caso que a regra do parágrafo anterior prevê, e a prova de que ela é necessária.
  - **Sondas de apelido curto colidem com palavras comuns.** «Sposto: 2 ocorrências» era substring de «di**sposto**s» (caso SPOSITO 2024i). Contar **palavras inteiras**, não substrings.

  📌 **O resumo do banco pode ser outra VERSÃO do mesmo resumo** (2026-08-19, caso ZUCARATO 2020): 66,6% de semelhança, primeira frase idêntica, mesma substância — é o resumo do registo do repositório contra o impresso, mais detalhado. **Não confundir com a obra derivada:** ali o resumo é outro texto sobre conteúdo diferente; aqui é o mesmo resumo condensado. O discriminador é a **substância**, não a coincidência literal.

  📌 **Alguns repositórios atribuem DOI à tese** — a UnB usa o prefixo `10.26512` (caso SOMBRIO 2015, `10.26512/2015.01.D.18503` no campo `url`) — e esse DOI **não é impresso no documento**. Para teses, a ausência do DOI no ficheiro é normal mesmo quando o banco tem um; não é indício de ficheiro trocado.

  📌 **O apelido do nome do ficheiro pode não existir dentro dele** (caso SCHMIDT 2015): a folha de rosto assina **Raquel Petry Brondani** e «Schmidt» tem **zero** ocorrências no PDF. Título, programa, instituição, ano, orientador e resumo batiam todos. Uma sonda por apelido nunca encontraria este ficheiro.

  **É a mesma pessoa, e a prova está no próprio banco:** o campo `author` da linha 5016 diz **«Schmidt, Raquel Petry Brondani»** — o registo da UFSM traz o nome completo, que contém exactamente os nomes da folha de rosto. É um nome com mais um apelido, não duas pessoas.

  ⚠️ **Não afirmar o mecanismo.** Uma versão anterior desta nota dizia «apelido adquirido depois da defesa», dando a entender casamento. **Isso não foi verificado e não se deve afirmar:** pode ter sido casamento, retificação de nome, ou correcção de registo — não há prova de qual. A distinção não é cosmética: se foi retificação, o nome do repositório é o nome da pessoa e a forma da folha de rosto está superada.

  ✅ **Regra que daqui sai:** quando o registo do repositório e a folha de rosto divergem no nome da mesma pessoa, **o banco segue o registo do repositório**, que é a forma actual. Não repor a forma impressa. A linha 5016 **não tem nada a corrigir** — foi retirada da lista de pendências em 2026-08-23.

⚠️ **DOI presente no texto não prova autoria** — pode ser citação nas referências, incluindo auto-citação do mesmo grupo. A posição no documento é que decide. E apelido + ano não chega; apelido + ano + revista também não (caso PUSHKAR 2019: mesma autora, revista, ano e tema, e ainda assim outro artigo).

⚠️⚠️ **A auto-citação entre artigos do mesmo grupo é sistemática, não excepcional** (constatado ao longo dos lotes 39–48). Apareceu em VEGA (três artigos da mesma autora a citarem-se em cadeia), AL-NAJJAR, ABD RASHID, BISWAS e BURCHART-KOROL. O problema é que **a sonda por DOI e a colisão de nomes de ficheiro falham nos mesmos casos**: são precisamente os artigos do mesmo grupo que partilham apelido e ano no nome *e* se citam uns aos outros no texto. Um método barato erra duas vezes no mesmo sítio; só a posição do DOI na frente os separa.

  🧾 **Demonstração fechada, verificada por mim no Drive (2026-08-18, caso VAN ROIJEN):** a sonda `fullText contains 's41467-024-48965-z'` devolve **dois** ficheiros — o `VAN ROIJEN et al., 2024.pdf`, que é o dono, e o `VAN ROIJEN, 2025.pdf`, que o cita nas referências a 84,6% do documento (auto-citação: Van Roijen/Kendall/Miller nos dois). A sonda inversa (`5c00080`) devolve só o de 2025. **Uma sonda por DOI, sozinha, devolve dois candidatos e não sabe decidir qual é o dono.** É o exemplo mais limpo de por que a conferência por abertura do ficheiro não podia ser substituída pela sonda.

⚠️ **Armadilha nº4 do extractor — DOI partido pelo markup do hiperlink** (descoberta 2026-08-17, caso BUCIO-SISTOS 2022): quando o DOI impresso está dentro de uma hiperligação, a extracção pode devolvê-lo em dois pedaços (`10.3989/ic` + `.87813`), e uma busca literal pelo DOI completo dá **ausente**. Pior: nesse ficheiro o *href* do link é `10.3989/ic.79082`, resto de um clipboard de InDesign do editor — ou seja, o `conferir_pdf.py` lista um DOI errado como se fosse o da frente. O texto impresso estava certo, confirmado pela caixa «Cómo citar este artículo» e pelo rodapé corrido. Perante um `ausente` inesperado, procurar o DOI aos pedaços antes de concluir seja o que for.

  📌 **Correcção (2026-08-17):** a armadilha **não** é propriedade da *Informes de la Construcción* nem do prefixo CSIC, como eu tinha escrito. O `MEL, 2015.pdf` (mesma revista) e o `MEJIA-ARCILA, 2020.pdf` (*Materiales de Construcción*, mesmo prefixo `10.3989`) foram conferidos e saíram **limpos** — DOI inteiro em todas as ocorrências e *href* correcto em todos os links. Era defeito do ficheiro do BUCIO-SISTOS em concreto, do InDesign de quem o paginou. Faltam `VIDAL et al., 2019.pdf` e `ARGUELLOMENDEZ et al., 2008.pdf` para fechar a questão.

  ✅ **`VIDAL et al., 2019.pdf` conferido (2026-08-18): limpo.** 13 ocorrências do DOI `10.3989/ic.60982`, **todas inteiras**, e todos os 33 *href* das referências a apontar para o DOI que o texto anuncia. Os dois únicos textos partidos são por hifenização de quebra de linha, com o *href* completo e certo. Falta só o `ARGUELLOMENDEZ et al., 2008.pdf`.

  🔁 **Reformulação da causa (2026-08-18):** partir o DOI pelo markup do hiperlink **não é raro nem editorial** — apareceu no `VIJERATHNE et al., 2024.pdf`, que é **MDPI**, e no `TRABUCCO, 2025.pdf`, idem. É um efeito comum da extracção. O que fazia do BUCIO-SISTOS um caso à parte **não era o texto partido, era o *href* errado** (resto de clipboard do InDesign a apontar para outro DOI). Ou seja: texto partido = frequente e benigno, resolve-se normalizando; *href* a apontar para outro DOI = raro e perigoso, porque um script que confie no *href* regista um DOI alheio como se fosse o da frente.

  🔁 **Duas causas distintas, e o *href* tanto mente como salva:**
  - **Markup do hiperlink** — o DOI impresso sai em pedaços (caso BUCIO-SISTOS e outros).
  - **Hifenização na quebra de linha** — `10.1111/j.1530- 9290.2011.00445.x`, com o extractor a listar `10.1111/j.1530` como se fosse um DOI (caso MOHAREB 2012).
  - **Hífen não-quebrável U+2011 em vez do hífen ASCII** (descoberto 2026-08-18, caso TEH 2018i, *Journal of Economic Structures*/Springer): o DOI da p.1 é `10.1186/s40008‑018‑0115‑1` com **U+2011 NON-BREAKING HYPHEN** nos três hífens, pelo que uma busca literal com hífen ASCII devolve **ausente** num ficheiro que está perfeitamente correcto. Verificado por mim, carácter a carácter. Normalizar os hífens (`‑`, `‐`, `‒`–`―`, U+00AD) antes de qualquer comparação de DOI.
  - **Injecção de espaços dentro do DOI pela justificação do texto** — no mesmo ficheiro TEH, a lista de referências imprime `https ://doi.org/10.1186/s4000 8-017-0072-0`. Retirar todos os espaços antes de comparar.
  - **Escape markdown do underscore, feito pelo próprio conector** (descoberto 2026-08-18, caso TIRTH 2019): o `read_file_content` rende o PDF em markdown e escapa o `_`, devolvendo `10.15666/aeer/1705\_1211112126`. **Esta é diferente das outras: não é defeito de um ficheiro nem de um editor — é do conector, e portanto é sistemática e previsível.** Atinge **todo** DOI que contenha underscore (`10.15666/aeer/...`, `10.1007/978-...-..._N`, etc.). Retirar as barras invertidas antes de comparar. Verificado por mim no ficheiro.

  📌 **Rotina de normalização a aplicar sempre, às duas pontas, antes de comparar DOIs:** minúsculas → retirar `\` → substituir `‑ ‐ ‒ – — ­` por `-` → retirar todos os espaços. Só depois procurar. E, perante um `ausente` inesperado, procurar ainda o prefixo e o sufixo isolados.

  📌 **A posição do DOI mede-se com folga** (2026-08-18): «na frente» não quer dizer «nos primeiros 2% do texto extraído». Blocos que o editor põe antes do rodapé da p.1 — *Highlights*, *Graphical Abstract*, caixas de copyright da margem — empurram o DOI para 3–5% do documento (casos TONIOLO 2023, TOSIC 2020, TUPENAITE 2023). Uma regra de corte por percentagem fixa produziria falsos `PDF_ERRADO`. O que conta é **em que página e em que bloco** o DOI está, não a que fracção do dump aparece.

  📌 **Embrulho de repositório não é quimera:** a folha de rosto de um repositório institucional (Manchester Research Explorer, caso TOMATIS 2020) antes do artigo, e o painel «You may also like» da capa IOP a listar artigos alheios (caso TRAN 2020), são embrulho do editor ou do repositório — não um segundo artigo.
  - No **BUCIO-SISTOS** o *href* estava **errado** (resto de clipboard do editor) e o texto impresso certo. No **MÜLLER 2021** dá-se o inverso: o texto impresso vem partido (`https://doi.org/10.3390/` + `su13168715`) e o DOI completo **só sobrevive dentro do *href***. Ou seja, nenhuma das duas fontes é fiável sozinha — é preciso cruzá-las.

  📌 **Correcção adicional (2026-08-18):** o `SILGADO et al., 2024.pdf` — *Materiales de Construcción*, prefixo `10.3989` — tem as **37** ocorrências do DOI inteiras, sem quebra por markup nem por hifenização. Terceiro ficheiro do mesmo prefixo a sair limpo. A questão fica praticamente fechada: era defeito do ficheiro do BUCIO-SISTOS.

⚠️ **Armadilha nº5 — cabeçalho corrido com os autores errados** (descoberta 2026-08-18, caso STOIBER 2022d): a *Acta Polytechnica CTU Proceedings* imprimiu neste artigo, no cabeçalho corrido das páginas **pares**, «J. Anderson, M. Hammerl, B. Kromoser» — quando a assinatura da p.1 é «Nadine Stoiber, Mathias Hammerl, Benjamin Kromoser». As páginas ímpares trazem o título corrido correcto. É erro de paginação do editor.

  ⚠️ **Esta armadilha corre ao contrário de todas as outras.** As anteriores produzem falsos `CONFERE`; esta produz um falso **`PDF_ERRADO`** — quem olhe para o cabeçalho corrido rejeita um ficheiro que está certo. Regra: a **assinatura da p.1** é a autoridade sobre autoria, nunca o cabeçalho corrido. Perante uma divergência entre os dois, é o cabeçalho que se despreza.

## Preferências de interação da Kiê

- **⭐ Perguntas: sempre no texto do chat, nunca em componente de escolha múltipla** (pedido explícito, 2026-08-12). Não usar a ferramenta de perguntas com opções — escrever a pergunta diretamente na resposta, em texto corrido, e aguardar. Vale para dúvidas de triagem, decisões de critério e qualquer outra escolha.
- **⭐⭐ Abrir sempre o PDF completo antes de trazer uma dúvida à Kiê** (pedido explícito, 2026-08-30). Quando um lote/subagente da Etapa 2 traz uma dúvida de critério, o passo obrigatório antes de a apresentar é abrir e ler o artigo inteiro pessoalmente — não confiar no resumo do subagente. **Só levar a dúvida à Kiê se, depois dessa leitura, a dúvida genuína persistir.** Se a leitura resolver o caso (encaixa numa regra já decidida, ou o contexto adicional torna a decisão óbvia), aplicar directamente e só reportar o resultado, sem perguntar. Validado no mesmo dia: a 4403 (SAMUDRALA) foi decidida com muito mais confiança depois de descobrir por leitura que era uma revisão a compilar dados do próprio tipo de mistura estudado; a 4425 (LATAWIEC) resolveu-se sozinha ao ler que a fonte é nomeada mas o valor nunca é impresso.
  - ⚠️ **"Ler" inclui ver as imagens, não só o texto extraído** (a Kiê apanhou esta lacuna, 2026-08-30: "Você viu imagens, tabelas e gráficos?" — a resposta era não, só tinha lido o texto do conector do Drive). O `read_file_content` do conector devolve texto/markdown; tabelas normalmente vêm bem, mas notas de rodapé, diagramas de fronteira de sistema e detalhes só visuais podem faltar. Antes de dar uma dúvida por confirmada só por texto, **descarregar o PDF (`download_file_content`, vem em base64) e renderizar as páginas relevantes como imagem** (`pymupdf`, `get_pixmap(dpi=200)`) para inspeccionar visualmente — sobretudo a secção de metodologia e as tabelas/figuras centrais à dúvida. Caso RAJAGOPAL (linha 4550): o texto extraído já não tinha unidade funcional nenhuma, mas só a inspecção visual das páginas (incluindo por baixo das tabelas, à procura de nota de rodapé) provou de forma definitiva que não havia nada a escapar à extracção de texto.
- **⭐⭐ Registar SEMPRE todas as decisões** (pedido explícito, 2026-10-04: «nunca se esqueça de registrar todas decisões»). Cada decisão — da Kiê ou de implementação minha — fica escrita no repositório com data, autor e onde está aplicada: no ficheiro de decisões da frente em causa (`metanalise/DECISOES_METANALISE.md` para a metanálise estatística, `lotes_etapa2/PROMPT_E2.md` para critérios da E2, script `aplicar*.py` + `observacoes`/`comments` para dados) e no resumo deste CLAUDE.md. Decisões minhas ainda não validadas ficam marcadas «por confirmar».
- **Idioma:** português europeu nas respostas; os dados e carimbos nas planilhas ficam sem acentos (ver regra de `clean_str`).

## Como navegar economizando tokens

Hierarquia recomendada:

0. **⭐⭐ `PROMPT_RETOMADA_2026-08-24.md` primeiro, numa sessão nova**, para entender a **reestruturação da triagem em 4 etapas** (2026-08-24) e como se chegou até aqui. ⚠️ **Desactualizado no ponto de retoma** — descreve a Etapa 2 como travada por "duas decisões em falta"; isso já foi resolvido, a Etapa 2 está em execução por lotes desde então. Para o estado vivo da Etapa 2, ir direto a `lotes_etapa2/PROMPT_E2.md` (regras de critério vigentes) e `lotes_etapa2/DUVIDAS_DE_CRITERIO.csv` (fila de dúvidas por resolver com a Kiê) — ambos referenciados na tabela "Notas operacionais" abaixo. O `PROMPT_RETOMADA_2026-08-22.md` fica como história da conferência PDF × banco — o seu ponto de retoma já não existe.
1. **MOC mestre.** Leia `_MOC.md` na raiz para visão geral de todas as áreas.
2. **MOC da área.** Antes de ler arquivos individuais, consulte `<AREA>/_MOC.md`.
3. **RSL_PROGRESSO.md.** ⚠️ **Histórico, não estado actual** — a última entrada datada é 2026-06-22 e as contagens já não valem. Serve como referência de método (formato das células, cascata, regras C5/C6) e como registo da execução original de cada critério.
4. **Frontmatter das notas.** Antes do corpo, leia o frontmatter (campos `titulo`, `descricao`, `tags`, `status`).
5. **articles_final.xlsx.** Não é diretamente legível pelo Claude; use scripts Python + openpyxl para extrair dados quando necessário.

## Áreas raiz

- **`00_REFERENCIAS/`** (catálogo) — 7 notas .md + ~1.630 PDFs. Contém notas de metodologia estatística e documentação PRISMA. MOC: [[00_REFERENCIAS/_MOC]]
- **`01_BUSCAS NAS BASES/`** (temporal) — 4 buscas sequenciais (BUSCA 01–04). Arquivos .bib/.ris/.csv das buscas originais. MOC: [[01_BUSCAS NAS BASES/_MOC]]
- **`02_ARQUIVOS ANTERORES/`** (arquivo) — Backups e versões obsoletas. Não avaliar como área ativa.
- **`04_EXTERNAL SOURCES/`** (catálogo) — 8 PDFs de fontes externas (Celik, Costa, Mohammadi…). MOC: [[04_EXTERNAL SOURCES/_MOC]]

## Notas operacionais na raiz

| Nota | Propósito |
|---|---|
| `CRITERIOS_E_NUANCES_RSL.md` | **⭐ Ler antes de qualquer triagem C1–C8.** Consolida num único arquivo o texto literal dos critérios + todos os refinamentos/decisões acumulados (RSL_PROGRESSO.md + CLAUDE.md + `claude/memoria/rsl-*.md`), o protocolo vigente de confirmação por PDF e o processo de extração para `meta_analysis_base.xlsx` (tarefa #7). Criado 2026-08-14. |
| `PROMPT_RETOMADA_AUDITORIA_COLISOES_PDF.md` | **⭐ PRIORITÁRIO (criado 2026-08-13).** Prompt para retomar a auditoria de colisões de PDF (67 linhas com ficheiro errado, 49 já com decisão tomada), as 7 linhas revistas à espera de confirmação, e só depois a triagem C2. Contém as regras novas da sessão de 2026-08-13. |
| `AUDITORIA_COLISOES_2026-08-13.csv` | Veredito linha a linha das 131 afetadas por colisão: DOI do banco vs DOI realmente no PDF. Lista de trabalho da correção. |
| `SOLTURA_PDF_OPCAOA_2026-08-16.csv` | **Registo da Opção A (2026-08-16).** As 73 linhas que ficaram sem PDF porque o ficheiro que reclamavam é de outra linha: número da linha, nome do ficheiro retirado, linha a que pertence, status. Cada uma tem também o motivo por extenso no carimbo (`comments`) do `articles_final.xlsx`. |
| `COLISOES_PDF_2026-08-13.csv` | Inventário bruto das linhas que partilham nome de ficheiro com DOIs diferentes; mantido por rastreabilidade. |
| **`PROMPT_RETOMADA_2026-08-24.md`** | **⭐⭐ LER PRIMEIRO NUMA SESSÃO NOVA.** A triagem em 4 etapas, a Etapa 1 concluída (2.206 sobreviventes), o piloto da Etapa 2 e as duas decisões em falta. |
| `PROMPT_RETOMADA_2026-08-22.md` | ⚠️ **História, não estado actual** — descreve o desenho antigo em cascata C1–C8. Vale pelo relato da conferência PDF × banco. |
| `DRIVE_FILEID_MAP.csv` | **⭐ O mapa `nome de ficheiro → fileId` da pasta dos PDFs**, 1.900 entradas. Usar sempre em vez de `search_files` por título. |
| `lotes_etapa2/UNIVERSO_E2.csv` | Os 1.591 sobreviventes da Etapa 1 que têm ficheiro — a lista de trabalho da Etapa 2. |
| `lotes_etapa2/PILOTO_RESULTADO.csv` | Os 12 artigos do piloto da Etapa 2, com resistência e CO₂ extraídos. |
| `OA_ETAPA1_2026-08-24.csv` | Varrimento Unpaywall dos 571 sobreviventes sem ficheiro: 546 em acesso aberto, mas só 404 com ligação directa ao PDF. |
| `DESCARGA_POR_EDITORA_2026-08-24.txt` | Taxa de sucesso da descarga automática por alojamento. As editoras comerciais bloqueiam; repositórios e revistas pequenas entregam. |
| `DOWNLOAD_OA_2026-08-24.html` | Lista clicável dos 571, em quatro grupos por esforço de obtenção. |
| `PROMPT_RETOMADA_CONFIRMACAO_PDF_METANALISE.md` | ~~Prompt da tarefa #7~~ — **desactualizado**, escrito a 2026-08-14 antes da conferência. O ponto de retoma que indica já não é válido. Ver o prompt de 2026-08-22. |
| `VERIFICACAO_TITULO_AUTOR_DOI.csv` | **Lista mestra da conferência** — 1.972 entradas, **estado vivo do banco** (limpa em 31/08, sem duplicados: cada linha do banco tem no máximo uma entrada, sempre a que descreve o ficheiro actualmente ligado). Veredito, título impresso, via de prova (`doi_bate`/`publisher_bate`/`resumo_bate`), nota e data. |
| `RELATORIO_LIMPEZA_CSV_MESTRE_2026-08-31.md` | **Histórico completo da limpeza de 31/08** — as 38 entradas obsoletas removidas (o que estava errado, quando foi corrigido, para que ficheiro), as 12 reconstruídas e as 3 estendidas. Consultar aqui, não no CSV, para o rasto histórico de uma correcção. |
| `lotes_verificacao/` | Atribuição e resultado de cada um dos 99 lotes da conferência, por rastreabilidade. |
| `PENDENTES_DECISAO_KIE_2026-08-17.csv` | **⭐ As 46 linhas com veredito não-CONFERE**, com as decisões `P:` afectadas e o cruzamento com a metanálise. **✅ 34 tratadas em 2026-08-23** (3 pares de troca fechados, 5 ficheiros devolvidos a linhas vivas, 5 nomes com diacríticos corrigidos, 22 ficheiros soltos). Restam 12: 4 `ILEGIVEL`, 1 `INDETERMINADO` e 7 anuladas à espera do PDF certo. |
| `ANULACAO_PDF_ERRADO_2026-08-19.csv` | As 9 linhas cujas 38 decisões `P:` foram anuladas por terem sido tomadas sobre o PDF errado — com o antes e o depois de cada célula. |
| `DOIS_RECUPERADOS_2026-08-18.csv` | 47 DOIs que faltavam ao banco, recuperados na conferência. **✅ APLICADOS ao banco em 2026-08-23** — todas as 47 células `doi` estavam vazias, sem conflito. Ver `APLICACAO_DOIS_2026-08-23.csv`. |
| `CORRECOES_METADADOS_2026-08-16.csv` | 35 defeitos de metadado do banco (autores truncados, anos errados, nomes mal formados, `url` a apontar para a obra errada). **✅ 15 APLICADOS em 2026-08-23** (`APLICACAO_METADADOS_2026-08-23.csv`); 3 ficaram por decidir (4951, 5016, 4999) e os restantes são renomeações de ficheiro, que exigem mexer no Drive. |
| `OBRAS_PERDIDAS_E_RECUPERADAS_2026-08-16.csv` | 24 casos de obras que se pensava perdidas e afinal estão na pasta, ou recuperáveis por reatribuição. |
| **`RETRIAGEM_PDF_2026-08-23.md`** | **⭐ A releitura por PDF dos 16 artigos com ficheiro novo ou decisão anulada** (23/08). Resultado critério a critério, as duas regras novas que daí saíram, os avisos de metanálise por linha e o que ficou à espera da Kiê. |
| **`APLICACAO_REGISTOS_2026-08-23.md`** | **⭐ O que foi escrito no banco a 23/08/2026**, com a prova de cada operação, o estado medido depois e a lista do que ficou por aplicar. Lê-se a seguir ao prompt de retomada. |
| `APLICACAO_DOIS_2026-08-23.csv` | Os 47 DOIs aplicados, linha a linha. |
| `APLICACAO_METADADOS_2026-08-23.csv` | As 15 correcções de metadado aplicadas, com o valor antigo e o novo. |
| `REATRIBUICAO_PDF_2026-08-23.csv` | Os pares de troca ZHANG e LI, a reatribuição SANTOS→3028 e os 5 nomes com diacríticos. |
| `SOLTURA_E_REATRIBUICAO_2026-08-23.csv` | O par PARK, as 4 devoluções a linhas vivas e as 22 solturas. |
| `HYPERLINKS_REALINHADOS_2026-08-23.csv` | Os 33 hyperlinks corrigidos, com o alvo antigo e a prova. |
| `OA_DISPONIVEL_2026-08-22.csv` | Os 57 DOIs das linhas `Sem acesso` passados pelo Unpaywall: **46 têm cópia legal em acesso aberto**, 11 não. |
| `SEM_PDF_WORKLIST_2026-08-21.csv` | As 144 linhas vivas sem ficheiro, com DOI ou handle. |
| `RSL_PROGRESSO.md` | ⚠️ **Histórico até 2026-06-22, não estado actual** — carrega no topo um aviso a apontar para o `PROMPT_RETOMADA_2026-08-22.md`. Vale pelo método (formato das células, cascata, regras C5/C6) e pelo registo da execução original de cada critério; as contagens (480 Elegíveis, 1.347 Inconclusivos) já não valem. |
| `PENDENCIAS_AUDITORIA_2026-07-12.md` | Auditoria de qualidade de dados do funil C1-C8 — concluída 2026-08-03; a última pendência (linha 2897) fechou-se 2026-08-30 com a chegada do PDF |
| `DOWNLOAD_MANUAL.html` | ~~Apagado~~ — download concluído (2026-06-05) |
| `DOWNLOAD_LESSONS_LEARNED.md` | Documentação de lições aprendidas no processo de download |
| `RELATORIO_VERIFICACAO_BD_RSL.md` | Relatório de verificação do banco de dados |
| `EXTERNAL_SOURCES_DOIs.md` | Lista de DOIs de fontes externas |
| `FASE5_LOG_PROBLEMAS.md` | Log de problemas da Fase 5 (meta-análise) |
| `RSL_COL_R_LOG.md` | Log de coleta R (análise estatística) |
| `PROMPT_RETOMADA_VERIFICACAO_RSL.md` | Prompt de retomada para verificação RSL |
| `PROMPT_RETOMADA_C5.md` | ~~ARQUIVADO~~ — C5 concluído 2026-06-21 |
| ~~`PROMPT_RETOMADA_C6.md`~~ | ⚠️ **Referenciado aqui mas o ficheiro não existe mais no repo nem em `02_ARQUIVOS ANTERORES`** (constatado 2026-08-03) — as regras C6 sobrevivem em `RSL_PROGRESSO.md` (seção C6) e neste ficheiro (seção "Regra C6 — refinamentos consolidados"), então nada foi perdido, mas a linha da tabela ficou órfã. Remover esta entrada quando alguém confirmar que o ficheiro nunca vai voltar. |
| `PROMPT_RETOMADA_C7.md` | ~~ARQUIVADO~~ — C7 REMOVIDO da RSL (2026-06-22); ver nota no ficheiro |
| `como_contornamos_o_akamai.md` | Documentação técnica de contorno anti-bot — Chrome CDP (original) **+ método alternativo sem browser via CDN `mdpi-res.com`** (2026-08-30). |
| **`lotes_etapa2/PROMPT_E2.md`** | **⭐ Ficheiro-mestre de critérios da Etapa 2** — o texto que os subagentes de cada lote seguem para decidir `E2_resistencia`/`E2_co2`. Todas as regras gerais (incluindo as três novas de 2026-08-28→30 — cálculo total/divisor, catálogo comparativo, excepção da massa específica do cimento) vivem aqui; ler antes de aplicar qualquer lote ou dúvida nova. |
| **`lotes_etapa2/DUVIDAS_DE_CRITERIO.csv`** | **Fila de dúvidas de critério da Etapa 2 por resolver com a Kiê, uma a uma.** ✅ **Zerada em 2026-08-30** — as 11 dúvidas genuínas que aqui estavam foram todas resolvidas nesta sessão (ver bullet "Fila de dúvidas de critério zerada" acima). Continua a ser o ficheiro para onde os próximos lotes despejam dúvidas novas; cada uma resolvida é removida do CSV e, se generalizável, vira regra no `PROMPT_E2.md`. |
| `lotes_etapa2/REVISAO_CO2_PERCENTAGEM_2026-08-30.csv` | Lista de trabalho da tarefa Supabase #1383 — os 69 artigos rejeitados em `E2_co2` pelo padrão "percentagem/índice sem dados para converter", por rever um a um com leitura completa do PDF. Ainda não iniciada. |
| `lotes_etapa2/SCOPE_2021_ESTUDOS_LCA_TAB_A1.csv` | Subconjunto de 52 estudos-ACV (de 70 catalogados) extraído da Tabela A1 do SCOPE et al. 2021 (linha 3671) — ramo de citação do PRISMA para essa revisão. |
| **`EXTRACAO_IC_QG_2026-09-12.md`** | Infraestrutura do intervalo de confiança por estudo — pedido da Kiê (2026-09-12) depois de reparar que o forest plot do site não tem barra de erro. Colunas novas em `dados_fck` (`ic_fck_*`/`ic_co2_*`, col 26-33) e em `articles_final.xlsx` (`QG_intervalo_confianca`, col 55). **✅ EXTRAÇÃO CONCLUÍDA (2026-09-12, PRs #186-198)** — as 651 linhas avaliadas na Etapa 4 têm `QG_intervalo_confianca` preenchido (557×0, 93×0,5, 1×1,0), `E4_qualidade_total`/`E4_estrato` recalculados com os sete itens (cutoff 4,0/7,0: 466 principal, 128 sensibilidade). **Verificado de novo em 2026-09-22**: cobertura 651/651 sem falhas em nenhuma direção, distribuição e exemplos batem com a rubrica, corte de estratificação sem inconsistências, PRs #186/#198 confirmados no GitHub. Esta nota (que dizia "extração ainda não começou") estava desatualizada havia dias — corrigida. ⚠️ **Ressalva nova (22/09):** dos 651, **58 foram rejeitados retroativamente** pela regra E2 mais restritiva (ver bullet "REGRA E2 MAIS RESTRITIVA" acima) — o `QG`/`E4_qualidade_total`/`E4_estrato` desses 58 continuam preenchidos nas células (não apagados) mas ficam órfãos, presos a artigos fora do funil activo. Qualquer recálculo futuro da estratificação (466/128) precisa de excluir esses 58 — o funil Elegível vivo é 540, não 598. |
| `IC_QG_WORKLIST_2026-09-12.csv` | As 651 linhas avaliadas na Etapa 4 com `QG_intervalo_confianca` — worklist original, hoje só de valor histórico (a extração já terminou, ver acima). |

## Convenções deste vault

### Frontmatter padrão (notas de metodologia)

```yaml
titulo: ...
descricao: ...
tags: [academico-e-pesquisa, meta-analise, metodologia]
status: revisado | em-andamento | rascunho | arquivado
ultima_atualizacao: YYYY-MM-DD
```

**Cobertura:** 11/16 notas (68,75%) — as notas operacionais na raiz não têm frontmatter.

### Tags mais frequentes

- `academico-e-pesquisa` (11 notas)
- `revisao-sistematica` (5)
- `UHPC` (4)
- `meta-analise` (4)
- `metodologia` (4)
- `engenharia-e-construcao` (2)
- `tecnologia-da-informacao` (2)
- `PRISMA` (1)

### Nomenclatura de PDFs

Padrão: `SOBRENOME et al., ANO.pdf` (sem caracteres especiais: ç→c, ã→a, ł→l, š→s).

### Banco de triagem (articles_final.xlsx)

- Coluna `pdf`: nome do ficheiro + hyperlink `file:///` para o caminho completo
- Fundo amarelo na célula `pdf` = PDF pendente de download
- Coluna `status_triagem`: Elegível | Inconclusivo | Duplicado | Sem acesso | Rejeitado (valor `Recusado` foi migrado para `Rejeitado` em 2026-06-21 — não existe mais)
- Colunas C1–C6, C8 com prefixo `R:` (triagem por resumo) ou `P:` (triagem por PDF). **C7 REMOVIDO** — coluna existe no xlsx mas ficou vazia (critério eliminado da RSL em 2026-06-22).

## Atalhos comuns

- **Metodologia estatística** → `00_REFERENCIAS/METODOLOGIA_ESTATÍSTICA/`
  - Modelos de efeitos: [[Metanalise_Efeitos_Fixos_vs_Aleatorios]], [[Justificativa_Modelo_Efeitos_Aleatorios]]
  - Estimadores: [[REML_vs_DL_explicacao]]
  - Cálculos: [[CÁLCULO DO P ESTATÍSTICO]]
- **Estado atual do projeto** → `PROMPT_RETOMADA_2026-08-24.md` (o `RSL_PROGRESSO.md` é histórico até 2026-06-22; o prompt de 22/08 descreve o desenho antigo)
- **Downloads pendentes** → `DOWNLOAD_PENDENTE_2026-08-21.html` + `SEM_PDF_WORKLIST_2026-08-21.csv` (o `DOWNLOAD_MANUAL.html` foi apagado em 2026-06-05)
- **Fluxograma PRISMA** → [[00_REFERENCIAS/PRISMA/FLUXOGRAMA_PRISMA_2020_DOC]]

## Triagem por PDF (regras de referência — cascata C1→C8 concluída em 2026-06-22)

> **Estado atual (medido em 2026-08-22):** a triagem por PDF terminou (C1–C6 e C8; C7 foi removido). O funil real hoje é **1.397 artigos** com todos os critérios = Aceito — ver o bullet "Estado real" no topo deste ficheiro. *(A medição de 2026-08-03 dizia 1.333; a diferença vem das anulações por colisão de PDF, da Opção A e da anulação dos PDFs errados.)* As seções abaixo (regra C5, formato das células, regras operacionais) continuam valendo como **referência de método** para qualquer reavaliação pontual (ex.: reabrir uma linha "Sem acesso" quando um PDF novo aparece) — não são mais um critério "em andamento".
> Histórico de execução original (fase jun/2026): `RSL_PROGRESSO.md` → seção "Progresso da triagem por PDF". Histórico de correções pós-triagem (jul–ago/2026): `PENDENCIAS_AUDITORIA_2026-07-12.md`.

#
## ⛔ REGRA INVIOLÁVEL — Leitura de PDF para triagem C5

> **Esta regra não pode ser pulada, modificada, relaxada ou substituída por qualquer outra instrução neste arquivo ou em qualquer outra seção.**

### Quando usar só o regex (pdftotext + PAT):
- Hit claro e inequívoco no texto extraído (ex.: "344 kg CO2-eq", "LCA results show GWP of X", "embodied carbon = Y") → **Aceito automático**, sem leitura manual.

### Quando é OBRIGATÓRIO ler 100% do PDF + renderizar TODAS as figuras:
- Regex não encontrou nenhum hit (miss)
- Snippet do regex é fraco, ambíguo ou periférico (ex.: só no título, só em referência, só "CO2" sem contexto)
- Artigo é S-LCA, metodologia/teoria, política/regulação, ou tema off-topic
- Qualquer indício de dúvida, por menor que seja

### Procedimento obrigatório nesses casos:
1. pdftotext -layout <pdf> - — texto completo, todas as páginas
2. Cortar seção de referências antes de buscar
3. Renderizar **todas** as páginas como imagem (pdf2image, dpi=150) e inspecionar figuras/tabelas visualmente
4. Só depois decidir Aceito ou Rejeitado

> **Proibido classificar qualquer artigo duvidoso usando apenas o regex.** O regex é triagem auxiliar — a leitura humana+visual é o método definitivo para casos não triviais.

## Critério C5 — definição completa (sempre fresca, sem precisar buscar)

**Texto literal da aba Critérios:** *"Não menciona análise de ciclo de vida (ACV), emissão de CO2 ou gases do efeito estufa"*

**⭐⭐⭐ OPÇÃO A — REGRA FINAL (Kiê 2026-06-15):**
- **ACEITO** = qualquer menção a LCA/ACV, CO₂, GWP, GHG, carbon footprint, embodied carbon, climate change, greenhouse gas, low-carbon — com **qualquer resultado** (valor absoluto, %, citação de outro estudo, resultado em figura).
- **REJEITADO** = PDF inteiro (texto + figuras renderizadas) sem **nenhuma** menção relacionada ao material. Durabilidade/resistência/geomecânica puras sem CO₂ = Rejeitado.
- **Exceção Rejeitado:** CO₂ puramente analítico-químico (picos FTIR de carbonatos) sem LCA/impacto ambiental.
- **Obrigatório antes de rejeitar:** ler 100% das páginas + renderizar figuras/gráficos.
- **S-LCA:** verificar se o corpo menciona CO₂/GHG no contexto/motivação — se sim, Aceito. Se LCA é 100% social sem nenhuma menção ambiental = Rejeitado.

**PAT regex (pdftotext):** lca|life.cycle.assess|carbon.footprint|embodied.carbon|gwp|global.warming.potential|co2.eq|co2eq|kgco2|greenhouse.gas|ghg|carbon.emission|climate.change|co2|embodied.emission|carbon.intensi|low.carbon
## Regras operacionais (sempre vigentes)

- **⭐ Indicador correto (reconfirmado 2026-08-03, corrige nota conflitante de 2026-06-06):** progresso medido por presença de `P:` nas células (P:Aceito / P:Rejeitado), NÃO por ter qualquer conteúdo. **Células com apenas `R:` são consideradas NÃO triadas, mesmo que título/resumo pareçam suficientes para decidir.** Toda linha `R:Aceito` precisa ser confirmada com `P:` antes de ser considerada definitiva — não é permitido aceitar um critério só com base em título/resumo. Uma nota anterior (`claude/memoria/rsl-marcacao-R-vs-P.md`, sessão 2026-06-06) permitia manter `R:` quando "título/resumo resolvia" — **essa permissão foi revogada pela Kiê em 2026-08-03**; a nota de memória foi corrigida.
- **Verificação PDF × artigo:** para **cada artigo** do lote, conferir título e primeiro autor na primeira página do PDF antes de avaliar. Obrigatório, sem exceção.
- **⭐ Páginas a ler (reconfirmado 2026-08-03):** desconsiderar resumo/título — ler as **primeiras 5 páginas do corpo do artigo**. Se essas 5 páginas não forem suficientes para decidir `P:Aceito` ou `P:Rejeitado`, continuar lendo até conseguir decidir. (Substitui a orientação anterior de "primeiras 2 páginas".)
- **Colisões de PDF:** nunca pular. Claude para, reporta DOI/título/autor e aguarda a Kiê baixar o PDF correto antes de continuar essa linha.
- **Parar entre critérios:** ao concluir um critério, parar e aguardar confirmação da Kiê antes de iniciar o próximo.
- **Lotes de 50 artigos:** salvar e reportar ao final de cada lote.
- **Casos ambíguos:** parar e tirar dúvida com a Kiê antes de classificar.

### Formato das células C1–C8

Preservar `R:` existente e acrescentar `P:` separado por ` | `.
- Com R:: `R:Aceito | P:Aceito`
- Sem R:: `P:Aceito` ou `P:Rejeitado`
- Colisão sem PDF correto: aguardar resolução — não registrar `P:` até ter o PDF certo.

### Coluna material_C2

Preencher para todos os artigos com `P:Aceito` em C2. Formato descritivo: material principal + contexto (ex: `"geopolímero para impressão 3D (revisão de materiais precursores)"`). Artigos rejeitados em C2 não preenchem esta coluna.

## Último relatório de avaliação

Nenhum — o relatório de 2026-06-04 foi removido em 2026-08-03 (todas as suas 5 pendências em aberto já haviam se resolvido organicamente; ver histórico de commits). Rodar a skill `avaliacao-vault` quando quiser um novo diagnóstico.

<!-- AUTO:END -->

<!-- USER:BEGIN -->
<!-- conteúdo original preservado — CLAUDE.md manual encontrado sem marcadores em 2026-06-04; backup em _AVALIACOES/_backups/CLAUDE_backup_2026-06-04.md -->

# Convenções da pasta REVISÃO SISTEMÁTICA DE LITERATURA

## Regra de arquivamento — backups e versões obsoletas

**Manter na raiz APENAS os arquivos ativos e mais atualizados.**

Sempre que surgir um arquivo obsoleto, backup, ou versão anterior, mover imediatamente para:

```
07_ANÁLISES DE DADOS/REVISÃO SISTEMÁTICA DE LITERATURA/02_ARQUIVOS ANTERORES/
```

### O que vai para 02_ARQUIVOS ANTERORES

- Backups automáticos gerados por scripts (`*_backup_*.xlsx`, `*_backup_*.csv`)
- Versões anteriores de planilhas (`articles_final_new.xlsx` → `articles_final_old.xlsx`)
- Arquivos corrompidos ou descartados
- Qualquer arquivo com sufixo `_old`, `_bak`, `_backup`, `_pre-*`, `_v[0-9]*` que não seja a versão corrente

### O que fica na raiz

| Arquivo | Descrição |
|---|---|
| `articles_final.xlsx` | Banco de triagem ativo (todas as 5.093 entradas, PDFs linkados) |
| `GRÁFICOS DA RSL.xlsx` | Gráficos da meta-análise |
| `BANCO DE DADOS DA RSL.xlsx` | Banco principal da RSL (já na pasta 02_ARQUIVOS ANTERORES — versão de trabalho migrou para o Excel do vault) |
| Scripts `.py` | Scripts de análise ativos |

### Convenção de nomenclatura ao arquivar

Ao mover, renomear descritivamente se necessário:
- `articles_final_new.xlsx` → `articles_final_old.xlsx` (arquivado em 2026-05-28)
- `*_backup_YYYYMMDD_HHMMSS.xlsx` → manter nome original

---

*Nota criada em 2026-05-28 para evitar confusão entre versões de arquivos.*

---

## Processo de download de PDFs — arquitetura em 5 camadas

> Documentado em 2026-06-02 após sessão de integração de PDFs manuais.

A pasta de destino de todos os PDFs é:
```
00_REFERENCIAS\ARTIGOS ACEITOS APÓS REMOÇÃO DAS DUPLICATAS\
```
O banco de triagem que regista os caminhos é `articles_final.xlsx`, coluna `pdf`.

---

### Camada 1 — Unpaywall automático (`download_pdfs_win.py`)

**Quando usar:** primeira execução; roda sem supervisão, processa todos os registros com `is_oa=true` no scan Unpaywall.

**Inputs:**
- `unpaywall_scan_results.json` — resultado do scan OA (gerado previamente)
- `articles_final_backup_*.xlsx` — versão de entrada do banco

**Checkpoint:** `download_checkpoint.json` — guarda `done`, `ok`, `fail`, `ok_rows`

**O que faz:** tenta descarregar o `pdf_url` de cada registo OA. Domínios bloqueados (Elsevier, Wiley, T&F, MDPI, ACS, ASCE…) são ignorados de imediato sem fazer pedido HTTP. Se o download tiver sucesso, grava o caminho completo na coluna `pdf` do Excel de saída e remove o fundo amarelo da célula.

**Outputs gerados:** `articles_final_new_YYYYMMDD_HHMMSS.xlsx` + `articles_final_backup_YYYYMMDD_HHMMSS.xlsx` (mover ambos para `02_ARQUIVOS ANTERORES/` após integrar).

---

### Camada 2 — MDPI via Chrome CDP (`mdpi_batch_dl.py` / `mdpi_resume.py`)

**Quando usar:** após Camada 1; para os artigos MDPI que ficaram pendentes (MDPI bloqueia automação simples com 403).

**Inputs:** `mdpi_todo.json` — lista de registos MDPI com campos `row`, `pdf_url`, `filename`

**Checkpoint:** `chrome_dl_checkpoint.json` — campos `processed`, `downloaded`, `failed`

**O que faz:** lança Chrome em modo depuração remota (CDP porta 9224 para `mdpi_batch_dl.py`, 9222 para `mdpi_resume.py`), injeta script anti-detecção, visita a página do artigo como warm-up, depois navega para o URL do PDF e aguarda o ficheiro em `C:\Temp\mdpi_dl\`. Após validar assinatura `%PDF`, move para a pasta de destino com o nome `filename` do `todo.json`.

**Diferença entre os dois scripts:** `mdpi_resume.py` é idêntico em lógica mas usa perfil Chrome diferente (`chrome_resume_profile`) — usar se o perfil principal ficar corrompido ou travar.

---

### Camada 3 — IOP Publishing + repositórios Handle (`iop_hdl_dl.py`)

**Quando usar:** para artigos IOP (10.1088) e artigos em repositórios institucionais com URL `hdl.handle.net/…`.

**Inputs:** `iop_todo.json` + `hdl_todo.json` — combinados internamente; campos `row`, `pdf_url`, `filename`, `_type` (`iop` ou `hdl`)

**Checkpoint:** `iop_hdl_checkpoint.json`

**Estratégias:**
- `dl_iop`: mesma lógica do MDPI — warm-up na página do artigo, depois navega para URL direto do PDF (CDP porta 9223).
- `dl_hdl`: navega ao handle (redireciona para repositório), executa JS para encontrar links com `.pdf` ou texto "PDF/Download/Full text", navega ao link encontrado e aguarda download.

---

### Camada 4 — Downloads manuais via CAPES / listas HTML

**Quando usar:** para Elsevier e quaisquer artigos que as camadas 1–3 não conseguiram.

**Ficheiros de apoio (na raiz da pasta RSL):**
- `ELSEVIER_DOWNLOAD.html` — lista clicável dos artigos Elsevier pendentes
- `DOWNLOAD_MANUAL.html` — lista de todos os outros artigos pendentes de download manual

Abrir no browser conectado ao proxy CAPES (VPN ou rede da instituição). Clicar nos DOIs e guardar os PDFs para a pasta `00_REFERENCIAS\ARTIGOS ACEITOS APÓS REMOÇÃO DAS DUPLICATAS\BAIXADOS MANUALMENTE\` (ver abaixo).

#### ⚠️ Formato CORRETO do link proxy CAPES (validado em 2026-06-05)

O acesso só é liberado com o **host reescrito** (pontos→hífens) + sufixo `.ezNNN.periodicos.capes.gov.br`, usando a **página do artigo** (não o caminho `content/pdf`):

```
https://link-springer-com.ez128.periodicos.capes.gov.br/article/10.1007/{DOI-suffix}
https://www-sciencedirect-com.ez128.periodicos.capes.gov.br/science/article/pii/{PII}
```

Regras aprendidas:
- **NÃO usar** `ezl` (ex.: `doi-org.ezl.periodicos.capes.gov.br`) — host inexistente, dá `ERR_CONNECTION_TIMED_OUT`. O número do proxy é `ezNNN` (ex.: `ez128`), **atribuído por sessão pelo CAPES** — pode mudar; confirmar com a Kiê a sessão ativa.
- Usar a **página do artigo** (`/article/...`), não `content/pdf` — a página é que renderiza o botão "Download PDF" com "Access provided by CAPES".
- Unpaywall pode marcar `is_oa=true` incorretamente para artigos Springer/Elsevier que na prática estão atrás de paywall — não confiar; ir direto pelo proxy CAPES.

---

### Integração de PDFs baixados manualmente

**Pasta de entrada:** `00_REFERENCIAS\ARTIGOS ACEITOS APÓS REMOÇÃO DAS DUPLICATAS\BAIXADOS MANUALMENTE\`

**Regra:** após integração, a pasta deve ficar vazia — os ficheiros são **movidos** para o destino (não copiados). A pasta serve apenas como área de entrada temporária.

### ⚠️ REGRA CRÍTICA — NUNCA APAGAR FICHEIROS DE BAIXADOS MANUALMENTE

> Adicionado em 2026-06-03 após incidente de deleção acidental de 44 PDFs.

**PROIBIDO:** apagar qualquer ficheiro de `BAIXADOS MANUALMENTE` automaticamente, sem autorização explícita da Kiê, mesmo que não haja match no banco.

**O que fazer com ficheiros sem match:**
1. Tentar matching por DOI (extraído do PDF)
2. Se falhar: tentar matching por título, autor e ano (metadados do PDF via pypdf / crossref)
3. Se ainda sem match: **MOVER** para `BAIXADOS MANUALMENTE\PARA VERIFICAR\` e **reportar** à Kiê quais foram movidos, com os dados encontrados (DOI extraído, título, autor)
4. **Nunca apagar** sem confirmação explícita

**Protocolo de matching correto (em ordem de prioridade):**
1. DOI exato no banco (`doi` column)
2. DOI limpo (remover sufixos de journal, corrigir ligaduras tipográficas)
3. DOI por prefixo (ex: `10.1016/j.jclepro.2019.1` → buscar `startswith`)
4. Título normalizado (lowercase, sem pontuação) — comparar com `title` column
5. Autor + ano + journal (combinação)
6. Se todos falharem → PARA VERIFICAR, nunca deletar

**Fluxo de integração:**

1. Renomear os PDFs para o padrão `SOBRENOME et al., ANO.pdf` (sem caracteres especiais: ç→c, ã→a, ł→l, š→s) — ver convenção em "Notas sobre nomenclatura" no `RSL_PROGRESSO.md`.
2. **Mover** para `00_REFERENCIAS\ARTIGOS ACEITOS APÓS REMOÇÃO DAS DUPLICATAS\`.
3. Abrir `articles_final.xlsx` e localizar a linha correspondente ao artigo (por DOI, título ou autor).
4. Na coluna `pdf`: **valor da célula = nome do ficheiro** (`SOBRENOME et al., ANO.pdf`) + **hyperlink = URI `file:///` apontando para o caminho completo**. NÃO preencher o caminho completo como texto — usar `cell.hyperlink` via openpyxl ou inserir hiperlink manual no Excel (Ctrl+K).
5. Remover o fundo amarelo da célula `pdf` se estiver marcada.
6. Re-gerar `DOWNLOAD_MANUAL.html` directamente (Claude faz isso, não há script standalone).

**Nota (2026-06-03):** os scripts de download automático (Camadas 1–3) foram removidos. O download é agora exclusivamente manual via `DOWNLOAD_MANUAL.html` + CAPES. O HTML é gerado directamente pelo Claude quando solicitado.

---

### Camada 5 — Push directo para o Drive via GitHub Actions + rclone (2026-08-30)

**Quando usar:** sempre que o Claude tiver um PDF (obtido por qualquer via — CDN aberto tipo mdpi-res.com, download manual entregue no chat, etc.) e precisar de o colocar no Drive **sem** passar pelas ferramentas MCP do Drive, que só aceitam conteúdo colado inline no próprio tool call com um teto de ~5 MB — tecnicamente inviável para a maioria dos PDFs (5,6 MB ≈ 1,85 milhões de tokens em base64, muito acima do limite de saída de uma resposta). Foi exactamente esta limitação, encontrada ao tentar corrigir a colisão de PDF da linha 4293, que motivou a construção desta camada.

**Ficheiro:** `.github/workflows/push-to-drive.yml`, disparado manualmente (`workflow_dispatch`) com três inputs: `download_url` (de onde descarregar o ficheiro), `drive_folder_id` (pasta de destino no Drive) e `filename` (nome final no Drive).

**Como funciona:** um runner descartável do GitHub Actions (1) descarrega o ficheiro do `download_url` para o próprio disco via `curl`, (2) instala o `rclone`, (3) configura-o com o secret `RCLONE_CONFIG` do repositório, e (4) envia o ficheiro para o Drive via `rclone copyto --drive-root-folder-id <pasta>`. Nada fica no repositório git — o runner é destruído no fim. Se já existir um ficheiro com o mesmo nome na pasta de destino, o `rclone copyto` **sobrescreve o conteúdo mantendo o mesmo `fileId`** (comportamento útil: corrigir um PDF errado sem ter de atualizar célula/hyperlink no banco, como aconteceu na linha 4293).

**Pré-requisito:** secret `RCLONE_CONFIG` no repositório (Settings → Secrets and variables → Actions), com o conteúdo completo do `rclone.conf` gerado localmente por `rclone config` depois de autorizar o rclone a aceder ao Drive (fluxo OAuth com cliente próprio, criado dentro do projeto Google Cloud `app-produtividade` da Kiê — o client_id partilhado do rclone está a ser descontinuado durante 2026). Guia passo a passo (instalação do rclone, criação do cliente OAuth, autorização, secret) foi feito interactivamente com a Kiê nesta sessão; não há ainda um documento dedicado — se for preciso repetir o processo (ex.: token expirado), pedir para o Claude reconstruir o guia a partir do histórico desta conversa.

**⚠️ Armadilha grave, já corrigida — secret com aspas duplas parte a substituição literal do GitHub Actions:** o passo "Configurar rclone" **não pode** colar o secret directamente dentro de uma string do script via `${{ secrets.RCLONE_CONFIG }}`. Essa substituição é **literal e acontece antes de o bash correr o script**. O `token` OAuth dentro do `rclone.conf` é um JSON com aspas duplas (`{"access_token":"...",...}`), e essas aspas partem a string do `printf` a meio, corrompendo o ficheiro de configuração escrito em disco — o rclone falha depois a decodificar o JSON truncado/reordenado, com um erro enganador (`invalid character 'a' looking for beginning of object key string`) que não aponta para a causa real. **A correcção é sempre passar qualquer secret que possa conter aspas por uma variável de ambiente (`env:`)**, nunca por interpolação directa `${{ }}` dentro do corpo do `run:` — uma variável de ambiente não sofre a substituição literal, o valor chega intacto ao script via `$NOME_DA_VAR`. Confirmado ao vivo: o primeiro disparo real do workflow falhou exactamente assim (run #1), a correcção (PR #16) resolveu no disparo seguinte (run #2, sucesso).

**Teste real que validou a camada (2026-08-30):** linha 4293 — PDF certo (`10.3390/buildings12070948`, obtido via CDN mdpi-res.com) enviado para a pasta `1R63Q4Lzz6JRRLpwES1Ngyod04q0-r9YP`, sobrescrevendo o ficheiro errado que lá estava desde a auditoria de colisões de 2026-08-13.

**⚠️ Caminho abandonado antes deste: bucket Cloudflare R2 `rsl-uhpc-pdfs`.** Durante a discussão desta infraestrutura, chegou a criar-se um bucket R2 (conta Cloudflare da Kiê, criado 2026-08-30T02:17:55Z) como possível armazém intermédio de PDFs. Foi abandonado a favor da solução GitHub Actions+rclone (mais simples, grátis, e escreve directamente no Drive — que já tem a pesquisa full-text e a navegação que um R2 isolado não teria sem trabalho extra de sincronização). **O bucket ficou criado mas vazio e não é usado por nada** — apagar quando a Kiê confirmar, ou ignorar (não tem custo relevante vazio).

---

### Ficheiros de estado / checkpoint — referência rápida

| Ficheiro | Pertence a | Descrição |
|----------|-----------|-----------|
| `unpaywall_scan_results.json` | Camada 1 | Resultados do scan OA (input) |
| `download_checkpoint.json` | Camada 1 | Estado do download Unpaywall |
| `mdpi_todo.json` | Camada 2 | Lista de artigos MDPI pendentes |
| `chrome_dl_checkpoint.json` | Camada 2 | Estado do Chrome CDP (MDPI) |
| `iop_todo.json` | Camada 3 | Lista de artigos IOP pendentes |
| `hdl_todo.json` | Camada 3 | Lista de artigos Handle/repositório |
| `iop_hdl_checkpoint.json` | Camada 3 | Estado do Chrome CDP (IOP/hdl) |
| `ELSEVIER_DOWNLOAD.html` | Camada 4 | Lista clicável Elsevier pendentes |
| `DOWNLOAD_MANUAL.html` | Camada 4 | Lista clicável outros pendentes |

---

*Secção adicionada em 2026-06-02.*
## articles_final.xlsx — Índices de colunas verificados ⚠️

> Adicionado 2026-06-15 após bugs causados por índices errados em C4/C5.

Usar **sempre** estes índices ao escrever scripts openpyxl (`ws.cell(row, column)`, 1-based). **MAPA COMPLETO RE-VERIFICADO pelo cabeçalho em 2026-06-21:**

| Campo | col openpyxl | Excel | Nota |
|-------|-------------|-------|------|
| `pdf` | **11** | K | Caminho/nome do PDF |
| `url` | **12** | L | URL do artigo |
| `status_triagem` | **20** | T | Elegível/Inconclusivo/Rejeitado/Duplicado/Sem acesso |
| `C1` | **21** | U | Triagem C1 |
| `C2` | **22** | V | Triagem C2 |
| `material_C2` | **23** | W | Material identificado (⚠️ FICA ENTRE C2 e C3!) |
| `C3` | **24** | X | Triagem C3 |
| `C4` | **25** | Y | Triagem C4 |
| `C5` | **26** | Z | Triagem C5 |
| `C6` | **27** | AA | Triagem C6 |
| ~~`C7`~~ | **28** | AB | ~~Triagem C7~~ — **REMOVIDO (2026-06-22), coluna vazia** |
| `C8` | **29** | AC | Triagem C8 |
| `comments` | **32** | AF | Carimbo / justificativa |
| `rastreio_potencial_futuro` | **33** | AG | Tags de rastreio |

> ⚠️⚠️ **ARMADILHA FATAL (causou bug em 2026-06-21):** a coluna `material_C2` (23) fica ENTRE C2 e C3. NÃO usar `zip(range(21,29), ["C1".."C8"])` — isso pula material_C2 e desloca C3–C8 em 1 coluna! Sempre usar o dict explícito: `COL={"C1":21,"C2":22,"C3":24,"C4":25,"C5":26,"C6":27,"C7":28,"C8":29}`.

### ❌ Armadilha — filtro errado para universo C5

```python
# ERRADO: captura R:Aceito-only e C4-Rejeitados (719 linhas a mais)
'Aceito' in str(c4_val)

# CORRETO: apenas linhas com P:Aceito explícito no C4
'P:Aceito' in str(c4_val)   # col 25
```

### ❌ Armadilha — IllegalCharacterError no openpyxl

PDFs podem conter caracteres de controle nos snippets extraídos por pdftotext. Antes de qualquer escrita no xlsx:

```python
import re
def clean_str(s):
    return re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', str(s))
# Aplicar em TODA string antes de ws.cell(...).value = ...
```

### PDF cid-encoded / garbled

Quando pdftotext retorna texto cifrado (fonte não-padrão, padrão ROT), usar OCR via pdf2image + tesseract. Nunca classificar REJEITADO sem ter lido o conteúdo real.

## ⭐ Lógica R: vs P: e regras de cascata (fonte: aba Critérios, lida 2026-06-21)

**Prefixos (aba Critérios, linhas 14–15):**
- **`R:`** = decisão tomada pela triagem de **título/resumo** (sem PDF). Valores: `R:Aceito | R:Rejeitado | R:A revisar`.
- **`P:`** = decisão pela leitura do **PDF completo**. Valores: `P:Aceito | P:Rejeitado | P:A revisar`.
- O C8 é decidido por **metadado (`document_type`)** → usa prefixo `R:` (disponível sem PDF).

**Regras de cascata (confirmadas com a Kiê 2026-06-21):**
1. **`P:` é o histórico de quem foi triado por PDF.** Um artigo rejeitado por PDF num critério (ex.: `P:Rejeitado` em C4) MANTÉM o histórico P: (o `P:Rejeitado` + os `P:Aceito` dos critérios anteriores). NÃO apagar esse histórico.
2. **Rows FORA-DA-CASCATA não recebem P: em critério nenhum.** Fora-da-cascata = `status_triagem` ∈ {`Duplicado`, `Sem acesso`, `Rejeitado`-por-resumo}. Esses já foram decididos por R:/metadado e nunca entram na triagem-PDF.
3. **Não existe mais `status_triagem = Recusado`.** Padronizado: usar só `Rejeitado`. (Era 1 row — 2897 — migrado em 2026-06-21.)
4. **Ao fim de cada lote, atualizar `status_triagem` → `Rejeitado`** para todo row que recebeu `P:Rejeitado` no critério do lote (regra Kiê 2026-06-21).
5. **Vazamento de cascata** = artigo com `P:Rejeitado` em Cn que recebeu `P:` em Cm>n. É erro; remover os P: posteriores ao P:Rejeitado.

**Universo correto da triagem-PDF de um critério Cn:**
rows na cascata (`status` ∈ {Elegível, Inconclusivo}) **E** `P:Aceito` em C(n-1) **E** sem `P:Rejeitado` em nenhum critério anterior **E** Cn ainda sem `P:`.
- ⚠️ Filtrar só por `"P:Aceito" in C(n-1)` NÃO basta — pega falsos-positivos sem PDF/fora-da-cascata. Cruzar SEMPRE com `status_triagem`.

## Correções de base 2026-06-21 (antes de retomar o C6)

Durante o C6 detectaram-se inconsistências herdadas + um bug de coluna. Tudo corrigido (backups em `02_ARQUIVOS ANTERORES/`):
- **Grupo A** — 4 rows `Duplicado`/`Sem acesso` com `P:` indevido → P: removido (3258, 3261, 3262, 3454).
- **Grupo B** — 3 vazamentos de cascata → P: posteriores ao `P:Rejeitado` removidos (3259, 3273, 3291).
- **Grupo C** — `Recusado`→`Rejeitado` (2897, +remoção P:C1); 100 `Inconclusivo` com `P:Rejeitado` em C1–C5 → `status=Rejeitado`.
- **Grupo D** — 1.705 células C8 sem prefixo → prefixadas `R:` (só rows na cascata).
- **Retro C6** — 8 rejeitados C6 dos Lotes 1–2 → `status=Rejeitado` (2581, 2753, 2790, 2805, 3016, 3120, 3159, 3254).

**status_triagem após correções:** Duplicado 2.624 · Inconclusivo 1.246 · Rejeitado 676 · Elegível 479 · Sem acesso 68.

## Regra C6 — refinamentos consolidados (Kiê 2026-06-21)

- **C6 NÃO avalia função estrutural** — isso já foi filtrado em C2 (não-estrutural) e C3 (não-moldável). C6 trata só de restrição geográfica/escalabilidade do MATERIAL.
- **Glossário:** *taipa* (rammed earth) = terra úmida socada/compactada em fôrmas, formando paredes monolíticas portantes — é material ESTRUTURAL; *adobe* = tijolo de terra crua; *cob* = mistura de terra+palha modelada à mão; *bahareque* = estrutura de bambu/madeira preenchida com terra (pau-a-pique).
- **Fibra natural** (sisal, juta, cânhamo/hemp, kenaf, linho, agave, coco): NÃO há regra automática — **parar e perguntar caso a caso**. Princípio emergente já aplicado: *fibra natural como REFORÇO incidental num material global (concreto) = Aceito; fibra natural REGIONAL como material-foco do estudo = Rejeitado.*
- **⭐ Material de terra** (rammed earth/taipa, adobe, cob, earthen, terra estabilizada/álcali-ativada) = **ACEITO** (REGRA REVISADA Kiê 2026-06-21: terra/solo é material UNIVERSAL e escalável, disponível em toda parte; a restrição da taipa/adobe é de TÉCNICA/mão-de-obra, NÃO de disponibilidade do material). Palha (straw bale) idem = resíduo universal. **Revertidos para Aceito em 2026-06-21:** 2581, 3016, 3120, 3159, 3498, 3896. ⚠️ EXCEÇÃO: **bahareque** (2805) = estrutura de BAMBU preenchida com terra → Rejeitado pelo BAMBU (bambu ≠ terra; é geograficamente restrito).
- **Cut-stone** (pedra de cantaria) = **Rejeitado** (row 4938 De Toldi); **pedra natural estrutural** como foco = Rejeitado (4707).
- **Resíduo agrícola/vegetal como SCM/agregado em concreto:** UNIVERSAL = Aceito (bagaço de cana, casca de arroz, aguapé/water hyacinth invasor, lignina kraft, palha de cereais, plantas invasoras); REGIONAL CONCENTRADO = Rejeitado (cinza de açaí amazônico, row 4720). O divisor é a disponibilidade global do resíduo.
- **Cortiça** como material relevante do estudo = **Rejeitado** (produção concentrada).
- **Materiais costeiros naturais** (coir/juta/concha de ostra para living shorelines) fora do escopo de concreto urbano = **Rejeitado** + rastreio `outra`.
- **Decisões registradas:** 3348 hemp-reforço=Aceito; ~~2790~~/3254 fibras regionais foco=Rejeitado; 3284 adobe-vs-concreto=Aceito (metade concreto armado).
  - 🚨 **A decisão sobre a 2790 está contaminada (descoberto 2026-08-19, lote 96).** Foi tomada a ler o PDF errado. A linha 2790 é a dissertação de Tiago Assunção Santos (UFBA) sobre **clínquer Portland com fino de rocha granítica e resíduo de telha de cimento-amianto** — não tem fibras nenhumas. O ficheiro que lá estava (`SANTOS et al., 2022.pdf`) é o artigo amazónico de fibras vegetais da **linha 3028** (`10.1016/j.clcb.2022.100034`, cinco autores, UFAM/UFRJ/Aveiro), que está sem PDF. Colisão do apelido «Santos». A justificação «fibras regionais» descreve o artigo da 3028, não a obra da 2790. **A 3254 não foi reverificada — a menção acima continua a valer só para ela.** Ver `PENDENTES_DECISAO_KIE_2026-08-17.csv`, linha 2790.
- **Lotes de 200**; ao fim do lote: salvar + atualizar status dos rejeitados + reportar.

## Regra C5 — OPÇÃO A (vigente 2026-06-15, SUPERA todas as anteriores)

**ACEITO** = qualquer artigo que conduza LCA *ou* mencione GWP/CO₂/GHG com *qualquer* resultado — mesmo % relativo, mesmo valor citado de outro estudo, mesmo em figura não extraível por texto.

**REJEITADO** = PDF inteiro (texto + todas as páginas renderizadas) sem **nenhuma** menção a CO₂/GWP/GHG/LCA/climate change relacionada ao material. Exceção: CO₂ puramente analítico-químico (picos FTIR de carbonatos) sem ACV ou impacto ambiental.

**OBRIGATÓRIO antes de qualquer REJEITADO:** ler 100% das páginas + renderizar figuras visualmente (pdf2image).

**PAT regex (pdftotext -layout):**
`lca|life.cycle.assess|carbon.footprint|embodied.carbon|gwp|global.warming.potential|co2.eq|co2eq|kgco2|greenhouse.gas|ghg|carbon.emission|climate.change|co2|embodied.emission|carbon.intensi|low.carbon`

**Carimbo C5:** `[C5 Aceito 2026-06-15: <evidência>]` ou `[C5 Rejeitado 2026-06-15: <motivo>]`

**Pending list:** `c5_pending_correto.json` em outputs — 1.100 rows gerados com filtro correto (`P:Aceito in C4`). Após Lote 6 restam 1.050. Ao retomar, pular row 3002 (aguarda PDF de capítulo de livro).

<!-- USER:END -->
