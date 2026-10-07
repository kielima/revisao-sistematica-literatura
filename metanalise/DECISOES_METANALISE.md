---
titulo: Decisões da metanálise estatística (rma.mv REML)
descricao: Registo datado de todas as decisões metodológicas da metanálise da intensidade de carbono por resistência, quem as tomou e como foram implementadas.
tags: [academico-e-pesquisa, meta-analise, metodologia, revisao-sistematica]
status: em-andamento
ultima_atualizacao: 2026-10-04
---

# Decisões da metanálise estatística

> ⭐ **Regra da Kiê (2026-10-04): «nunca se esqueça de registrar todas as decisões».** Toda decisão metodológica — dela ou de implementação minha — entra aqui, com data, autor e onde está implementada. Uma decisão de implementação que eu tome sem ela fica marcada **[IMPLEMENTAÇÃO — por confirmar]** até ela a validar.

Ficheiros: `metanalise/preparar_dados.py` (entrada), `metanalise/metanalise_rma_mv_REML_v5.R` (modelo), `metanalise/resultados/` (saídas).

## A. Decisões fechadas pela Kiê

| # | Data | Decisão | Onde |
|---|---|---|---|
| A1 | 2026-05-13 | Modelo multinível `metafor::rma.mv`, estimador **REML**, estrutura aleatória `~ 1 \| estudo / obs_id` (formulações aninhadas nos estudos); heterogeneidade em τ²₁ (entre estudos) e τ²₂ (entre formulações do mesmo estudo). | v5, secção 3 |
| A2 | 2026-05-13 | Efeito `ci` = kg CO₂-eq/(m³·MPa) = `co2_kg_m3 / fck` (Damineli et al. 2010). | `preparar_dados.py` |
| A3 | 2026-05-13 (v3) | `vi` híbrido: variância de `ci` dentro da classe de resistência quando a classe tem ≥ 4 observações; senão `(0,05·ci)²` (CV 5 %). | v5, secção 2 |
| A4 | 2026-10-04 | **`vi` publicado tem prioridade**: quando o artigo publica a dispersão (DP ou CoV) do fck e/ou do CO₂ do próprio par, `vi` vem dela; a regra híbrida (A3) só se aplica aos pares sem dispersão publicada. | v5, secção 2 |
| A5 | 2026-10-04 | **Sensibilidade do CV assumido**: repetir o modelo com `vi = (k·ci)²` para todos os pares sem dispersão publicada, k = 5 %, 10 % e 15 %. | v5, secção 5 |
| A6 | 2026-10-04 | **Indicador principal = `ci`** (cobre todos os pares). **`ci_mpa`** (kg CO₂-eq/MPa, com o volume real do provete — `PROTOCOLO_CI_MPA_2026-09-08.md`) é **análise secundária**, só nos pares com volume. | v5, secções 4 e 6 |
| A7 | 2026-09-12 | Estratificação pela Etapa 4: **análise principal só com o estrato `principal`** (score ≥ 4,0/7); o estrato `sensibilidade` entra numa análise de sensibilidade. | v5, secções 4–5 |
| A8 | 2026-08-13 | Heterogeneidade explicada por **moderadores**, não por exclusão (`MODERADORES_UCS_METANALISE.md`). | v5, secção 7 |
| A9 | 2026-09-26 | Base dos pares = `co2_kg_m3` (col 37) e só artigos `Elegível`; a selecção de pares é a mesma do painel (`metanalise-export.py`, incluindo os limites plausíveis fck 1–300 MPa e CO₂ −1.000 a 5.000 kg/m³). | `preparar_dados.py` |
| A10 | 2026-10-04 | R instalado no contentor da sessão (Debian, pacotes `r-cran-*`), em vez de correr na máquina da Kiê. | — |

## B. Decisões de implementação (minhas) — por confirmar pela Kiê

| # | Data | Decisão | Porquê |
|---|---|---|---|
| B1 | 2026-10-04 | **[IMPLEMENTAÇÃO — por confirmar]** Conversão da dispersão publicada em `vi` (A4), pelo método delta: `CV_fck = DP/fck` (ou CoV/100), idem para o CO₂; `vi = ci² · (CV_fck²/n_fck + CV_co2²/n_co2)`. Sem `n` declarado, usa-se n = 1 (conservador). Sem dispersão publicada do CO₂ (quase sempre — a ACV é determinística), o termo do CO₂ é zero. | `vi` deve ser a variância de amostragem da **média** reportada (DP²/n), prática corrente (Borenstein et al. 2009). |
| B2 | 2026-10-04 | **[IMPLEMENTAÇÃO — por confirmar]** Só os tipos `desvio_padrao` e `cv_percentual` entram em A4. `barra_erro_nao_definida`, `desvio_maximo_global`, `intervalo_min_max`, `ic_declarado` e `intervalo_interquartil` caem na regra híbrida (A3), por não serem convertíveis em DP sem suposição. | Regra «não assumir nada» (Kiê, 2026-10-04). |
| B3 | 2026-10-04 | **[IMPLEMENTAÇÃO — por confirmar]** As classes de A3 passam a ser intervalos do **fck numérico** (o banco novo não tem a coluna «Classe nominal» do banco de maio): ≤ 22,5 → C≤20; (22,5; 27,5] → C25; … de 5 em 5 MPa até C55; (57,5; 90] → C60-C90; > 90 → UHPC. Mesmos grupos do script v4. | Reproduzir A3 no banco actual. |
| B4 | 2026-10-04 | **[IMPLEMENTAÇÃO — por confirmar]** `vi` mínimo de 1e-8 para pares com `ci` = 0 (o CV daria `vi` = 0 e o REML falha). | Estabilidade numérica. |
| B5 | 2026-10-04 | **[IMPLEMENTAÇÃO — por confirmar]** Moderadores testados um a um (meta-regressão `mods = ~ moderador`) no estrato principal: família do ligante (`metanalise-export.classify`), base Portland, idade do ensaio (28 d / outra / não declarada). | Explicar a heterogeneidade (A8). |
| B6 | 2026-10-04 | **[IMPLEMENTAÇÃO — por confirmar]** Viés de publicação: funil e teste de Egger multinível (`rma.mv` com `mods = ~ sqrt(vi)`), no estrato principal. | Protocolo PRISMA. |

## D. Famílias de material (moderador) — revarredura de 2026-10-04

Pedido da Kiê (2026-10-04): «corrija todas as inconsistências» e «faça a revarredura completa do concreto armado». Inconsistências encontradas ao listar as famílias: 3377 ESPUELAS (misturas activadas por álcali em «outros ligantes» por override antigo), «base biológica» com três betões Portland (aditivo de cato, fibra de sisal, ECC com lignina), 4822 (compósito areia-policarbonato em «reciclado» com base não-Portland), misturas de controlo classificadas pela família do material novo do artigo, e o mesmo tipo de resíduo (pó de vidro, pó cerâmico) ora em «SCM» ora em «reciclado». A família `concreto_armado` nunca teve varredura completa (só a de 10/09, sobre os 1.069 pares de então).

Revarredura: 43 lotes (`lotes_familia/`), leitura integral de cada PDF, quatro perguntas por par (`PROMPT.md`). Regras de atribuição, por ordem de precedência:

| # | Data | Regra | Estado |
|---|---|---|---|
| D1 | 2026-09-10 (Kiê) | `concreto_armado` **só** quando o CO₂ gravado inclui o aço de armadura/pré-esforço sem o artigo permitir separar; se o artigo dá o CO₂ só do betão, a linha fica na família química (com o valor só do betão). | fechada |
| D2 | 2026-09-28 (Kiê) | A família segue a **composição da própria mistura**, não o título do artigo (precedente: 40 traços Portland de referência saíram de «geopolímero»). Logo, misturas de **controlo** sem o material novo → `opc`. | aplicação nova **[por confirmar]** |
| D3 | 2026-09-28 (Kiê) | Activado por álcali (incl. híbridos com OPC minoritário) → `geopolimero`. | fechada |
| D4 | 2026-09-28 (Kiê) | Sem clínquer Portland e sem activação alcalina (CSA, magnesianos, belite-ye'elimite, gesso, escória carbonatada, polímero) → `ligantes`. | fechada |
| D5 | 2026-10-04 | `biobase` só para material estrutural de origem biológica (madeira/glulam). Betão Portland com aditivo ou fibra natural → família química (C6: «fibra natural como reforço incidental num material global»). | **[por confirmar]** |
| D6 | 2026-10-04 | UHPC/UHPFRC assim chamado pelo artigo → `uhpc` (depois de D1, D3, D4). | **[por confirmar]** |
| D7 | 2026-10-04 | Resíduo/subproduto **a substituir cimento** (papel de ligante: cinzas, escórias, pó de vidro, pó cerâmico, filer) → `scm`; resíduo/reciclado **como agregado ou fibra** → `reciclado`. É a divisão que as regex do `metanalise-export.py` já fazem (pó de vidro e CWP estão na lista de SCM); os overrides que a contrariavam são corrigidos. | **[por confirmar]** |
| D8 | 2026-10-04 | Restante (Portland sem material distintivo, aditivos químicos, fibras virgens) → `opc`. | **[por confirmar]** |

Ficheiro de aplicação: `lotes_familia/aplicar.py` (escreve os overrides no `metanalise-export.py` e regista cada mudança). Depois: `classificar_base_portland.py`, exportação, painel e nova corrida do modelo v5.

**Aplicada a 2026-10-04** (43/43 lotes, 1.524 pares respondidos):
- `lotes_familia/mapear.py` (regras D1–D8 sobre as quatro respostas) + `lotes_familia/aplicar.py` → `lotes_familia/familias_revarredura.json`, que o `metanalise-export.py` consulta **antes** do OVERRIDE antigo e das regex; registo par a par em `lotes_familia/MUDANCAS_FAMILIA_2026-10-04.csv` (362 mudanças).
- Ajustes manuais **[IMPLEMENTAÇÃO — por confirmar]**: 2827 ZHANG 2023e (tubos/umbilicais desmantelados embebidos) → `reciclado`; 2946 (cinza de cal que substitui o filer calcário, não o cimento) → `reciclado`; 3073 ABU-ENNAB → `ligantes` (CSA, valor passado ao nível do material).
- Linhas com o aço separável **só por subtracção de barras/percentagens de figura com outras parcelas misturadas** ficam com o total em `concreto_armado` **[por confirmar]**: HAJIESMAEILI 1855, HAVERKAMP 645, COLANGELO 804, DI SUMMA 1004/1005, BACKES 4753 (1740–1742); STUDZINSKI 2085–2088 mantém a via só-fundação decidida pela Kiê a 27/09.
- `classificar_base_portland.py` passa a seguir a família da revarredura (geopolímero/ligantes/biobase = `nao`; resto = `sim`), depois das decisões manuais por linha. Corrigiu 324, 328, 396 (referências Portland marcadas `nao`), 3354 GRIST NHL5 e 4836 CHO (sem cimento, marcadas `sim`).
- Resultado: 1.492 pares no painel (−32), 394 estudos; famílias opc 535, scm 384, reciclado 209, geopolímero 205, betão armado 102, UHPC 34, ligantes 22, biobase 1.

### D′. Correcções de valor da revarredura — `lotes_familia/aplicar_valores.py`

Cada entrada diz se foi verificada por mim no PDF (`pessoal`) ou é leitura do subagente com citação exacta (`subagente`, **por confirmar**). Regras **[IMPLEMENTAÇÃO — por confirmar]**:

| # | Regra | Casos |
|---|---|---|
| E1 | Valor que não é o CO₂ do betão (só a brita, só o gasóleo, sem o cimento, sem os activadores, soma de factores, dividido por ciclos de durabilidade, outra categoria de impacto, escala incoerente) → `NAO CONVERTIDO` | BACKES 4, CONG 90, MARTÍNEZ-MUÑOZ 177, YOUNES 793/794, SAMUVEL 880, GOPALAKRISHNA 423, PEDNEAULT 991, MAURY-RAMÍREZ 1743/1744, HORA 1836–1841 |
| E2 | Linha que repete o traço/par de outra linha do mesmo artigo → `NAO CONVERTIDO` (duplicado); no ISAIA fica o par aos 28 d e saem os aos 91 d (mesmo traço, mesmo CO₂) | 2703 KIM 151–153, FARIDMEHR 1418/1423, YE 1106, MA 1761, BRAGA 63, ISAIA 66/68/70/72/74/76 |
| E3 | Valor por m³ normalizado à resistência gravado como kg/m³ → × fck (regra total+divisor) | PUSHKAR 4580 (20 pares; o RELABEL de 08/09 estava errado) |
| D1 | CO₂ só do betão impresso/calculável com números do artigo → substitui o total com aço | HAFEZ 135–138 (Fig.5, pessoal), INMAN 646–650, SOMBRIO 234, GALAN-MARIN 331, NEIMARK 1150, HABERT 821, MEL 1826, BENTO 51, REZENDE 43 |
| — | Erros de valor/fck | ALSALMAN 298/300/303, GLANZ 1222/1223 (m³-eq → m³), LEMESRE 1494, ABDULKAREEM 976–980 (CO₂ Fig.3 e fck Tab.1, pessoal), THORNE 312, ABU-ENNAB 305, MORO 1748/1752/1756 (sílica activa 3,4E-3), LOS SANTOS 1478/1479 (fck sem apoio no PDF → apagado), rótulo ISAIA «cal hidratada» |

## B (cont.)

| # | Data | Decisão | Porquê |
|---|---|---|---|
| B7 | 2026-10-04 | **[IMPLEMENTAÇÃO — por confirmar]** Leave-one-study-out em paralelo (`mclapply`), com os `vi` do modelo completo e os σ² do modelo completo como valores iniciais; desliga-se com `LOO=0`. | A corrida sequencial passava dos 30 min. |

**Leave-one-study-out (2026-10-04, 1.492 pares, estrato principal 308 estudos):** retirando qualquer estudo, a média de `ci` fica entre 10,00 (sem 2849) e 10,32 (sem 3413), contra 10,27 do modelo completo; 0 falhas de convergência. Nenhum estudo isolado determina o resultado. `metanalise/resultados/leave_one_study_out.csv`.

## E. CO2 com e sem desconto (créditos) — 2026-10-07

| # | Data | Decisão | Estado |
|---|---|---|---|
| F1 | 2026-10-07 (Kiê) | Em vez de escolher uma regra única para os créditos (carga evitada, carbonatação, biogénico, módulo D), o painel passa a ter **uma opção para ver os dois cenários — sem desconto (bruto) e com desconto** —, como o filtro «Só cimento Portland». Nova coluna para o CO2 com desconto. | fechada |
| F2 | 2026-10-07 (Kiê) | **Reabrir todos os PDFs** com pares no painel (394 estudos, 1.492 pares) para saber quais declaram CO2 com desconto e quais só o bruto. Lotes em `lotes_creditos/` (44 lotes, `PROMPT.md`). | em curso |
| F3 | 2026-10-07 | **[IMPLEMENTAÇÃO — por confirmar]** Colunas novas em `dados_fck`: `co2_kg_m3_com_desconto` (kg CO2-eq/m3 com todos os descontos que o próprio artigo aplica; vazia se o artigo não declara desconto), `co2_desconto_tipo` e `co2_desconto_citacao`. `co2_kg_m3` (col 37) passa a guardar o **bruto** quando o artigo o publica ou permite calculá-lo com números impressos. | em curso |
| F4 | 2026-10-07 | **Aplicado** (`lotes_creditos/aplicar.py`, 44 lotes, 1.492 pares): 1.262 pares sem desconto declarado; 203 com desconto declarado (106 com o gravado já líquido, 97 com o gravado bruto); 22 indeterminados. **83 valores de `co2_kg_m3` passaram de líquido a bruto** (o líquido foi para `co2_kg_m3_com_desconto`), 173 pares têm valor com desconto e **49 não têm bruto disponível** (o artigo só publica o valor com desconto ou não deixa decidir). Valores derivados por nós (contas com números impressos ou leitura por píxel) ficam marcados `derivado: sim` em `co2_desconto_citacao`. | aplicada |
| F5 | 2026-10-07 | **[IMPLEMENTAÇÃO — por confirmar]** ARYAN 4768 (linha 594): o valor com desconto conta só a carbonatação do próprio betão (375,6); o albedo (−69,6 t) não é crédito do material e fica de fora. | aplicada |
| F6 | 2026-10-07 | **[IMPLEMENTAÇÃO — por confirmar, pergunta à Kiê]** Os 49 pares sem bruto disponível aparecem nos dois cenários com o valor publicado (no painel e no modelo «sem desconto»); o modelo tem também uma sensibilidade «só pares com CO2 bruto publicado». | aplicada |
| F7 | 2026-10-07 | **[IMPLEMENTAÇÃO — por confirmar]** Painel: barra fixa com dois grupos — «Base do ligante» e «CO₂ dos artigos» (Sem desconto / Com desconto, `?co2=com`); o cenário troca o CO2 em todos os gráficos que leem `currentData()`. Exportador: 7.º campo = CO2 com desconto (null = sem desconto), 8.º = 1 quando não há bruto. | aplicada |
| F8 | 2026-10-07 | A pergunta aberta 1 (créditos: bruto vs líquido) fica **resolvida pela F1**: os dois cenários coexistem; o «sem desconto» é a análise principal. **[por confirmar]** | — |

## C. Pendências que não bloqueiam a análise

**Perguntas abertas à Kiê (2026-10-04, revarredura):**
1. ~~Créditos~~ — resolvida pela F1/F8 (dois cenários). Proposta antiga: valor bruto sem créditos sempre que publicado (LEE 4028, BATUECAS 3413, MOMOTAZ 3497, MASI 4039, BERTOLDO 4251, VITALE 4475, GARCIA-TRONCOSO 4497, KVOCKA 4731, MARIAKOVA 4691, MORO 4758), líquido só quando a carbonatação é a função do produto (DI MARIA 2653).
2. Cimentos compostos comerciais (CP III/CEM III, CP II/CEM II): `opc` ou `scm`? (hoje segue a resposta do subagente: substituição → `scm`).
3. PUSHKAR 4267/4580: proxy «cement mortar, at plant» para o cimento (~88 kg/m³) — manter com alerta ou retirar.
4. TOSIC 4625 (~0,34 kg/m³, «g» impresso): manter (decisão de 12/09) ou retirar.
5. OH 4930 (3.532 kg/m³, linhas Concrete/Rebar provavelmente trocadas): gravar 259 com alerta ou retirar.
6. Mesmos números em artigos diferentes (FILHO 2854 = 2744; TEH 4026/4027; JANG 2694/2695): contar uma vez?
7. DI SUMMA 3424: manter o total em `concreto_armado`?
8. ISAIA 2021: deixa de ser `uhpc` (a tese não o chama UHPC) — confirmar.
- Também por fazer: desdobrar COLANGELO 804 nas 8 misturas (Fig.5).

- Extracção dos estudos secundários (ONSONGO, NASIR, SCOPE…) — adiada pela Kiê (2026-10-04); `origem_dado` = `primario` em todas as linhas.
- PDF da 2880 MESHRAM (a Kiê vai enviar).
