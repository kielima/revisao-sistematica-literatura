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

## C. Pendências que não bloqueiam a análise

- Extracção dos estudos secundários (ONSONGO, NASIR, SCOPE…) — adiada pela Kiê (2026-10-04); `origem_dado` = `primario` em todas as linhas.
- PDF da 2880 MESHRAM (a Kiê vai enviar).
