# Resultados da metanálise — todos os números

Gerado por `metanalise/gerar_resultados.py` em 2026-11-28 14:49, commit `dcc047f`. Fonte de cada número: os ficheiros de `metanalise/resultados/` e `00_REFERENCIAS/PRISMA/FUNIL_PRISMA.csv` dessa versão. Unidade do `ci`: kg CO₂-eq/(m³·MPa); do `ci_t`: kg CO₂-eq/(m³·MPa·ano). IC = intervalo de confiança de 95 %; IP = intervalo de predição de 95 %.

## 1. Fluxo PRISMA

| Caixa | n | Filtro |
|---|---|---|
| Registos identificados nas bases | 5.093 | todas as linhas de articles_final.xlsx; por base: Web of Science 1917 / Scopus 1427 / Engineering Village 763 / MDPI 475 / Science Direct 411 / BDTD 72 / SciELO 28 |
| Duplicados removidos antes da triagem | 2.630 | status_triagem = 'Duplicado' (remocao pre-triagem, nao e criterio de exclusao) |
| Registos triados por metadados | 2.463 | status_triagem <> 'Duplicado' |
| Excluidos na Etapa 1 | 272 | primeiro criterio E1 (ano, tipo_doc, moldavel, construcao) <> 'Aceito'; E1_ano 1 / E1_tipo_doc 9 / E1_moldavel 72 / E1_construcao 190; inclui 1 registo(s) SEM decisao (celula vazia), ver regularizacoes |
| Textos completos procurados | 2.191 | os quatro criterios E1 = 'Aceito' |
| Texto completo nao obtido | 6 | E1 completo e E2_resistencia vazia (sem PDF): status_triagem = 'Sem acesso' 6 |
| Textos completos avaliados | 2.185 | E1 completo e E2_resistencia preenchida (leitura integral do PDF) |
| Excluidos na Etapa 2 - falta de dado extraivel | 1.643 | E2_resistencia <> 'Aceito' (1303: sem fck proprio pareavel a um CO2 proprio, ou fck < 20 MPa) ou, com fck, E2_co2 <> 'Aceito' (340: sem CO2 absoluto) |
| Artigos aceites na Etapa 2 | 542 | E2_resistencia = 'Aceito' e E2_co2 = 'Aceito' |
| Excluidos na Etapa 3 - material geograficamente restrito | 18 | E3_regional <> 'Aceito': 14 com E3_regional = 'Rejeitado' + 4 com E3_regional vazio e status 'Rejeitado' (rejeitados por restricao geografica na triagem antiga C6, linhas [2805, 4707, 4720, 4938]; a regularizar) |
| Artigos que passam a Etapa 3 | 524 | E3_regional = 'Aceito' (466 Elegível + 58 Revisao) |
| Revisoes sem ACV propria - ramo de citacao | 58 | status_triagem = 'Revisao' (nao pontuam; as fontes primarias que citam entram pelo ramo 'outros metodos', aba estudos_secundarios) |
| Artigos incluidos na revisao (corpus) | 466 | status_triagem = 'Elegível'; E4_estrato: principal 362, sensibilidade 104 |
| Estrato de sensibilidade - fora do RESULTADO PRINCIPAL, dentro do corpus | 104 | E4_estrato = 'sensibilidade' (E4_qualidade_total < 4,0 de 7; notas: 0 (1), 1 (2), 1.5 (3), 2 (7), 2.5 (12), 3 (40), 3.5 (39)). Exclusao do resultado principal, nao do corpus: entra na analise de sensibilidade |
| Estudos no resultado principal | 362 | E4_estrato = 'principal' (E4_qualidade_total >= 4,0 de 7) |
| Registos identificados por busca de citacoes nas revisoes catalogadas | 108 | aba estudos_secundarios (F36): SCOPE et al., 2021 73 / NASIR et al., 2024 22 / ONSONGO et al., 2025 13 |
| Ja estavam no banco (contados no fluxo principal) | 17 | estado_extracao = 'ja_no_banco' |
| Relatorios a procurar/avaliar (pendentes, tarefa #1811) | 91 | estado_extracao = 'pendente' (65) ou 'sem_doi' (26) |

## 2. Corpus da metanálise

- Pares fck × CO₂ no painel e no modelo: **1.498**, de **398** estudos.
- Estrato principal: 1.158 pares, 311 estudos.
- Estrato sensibilidade: 340 pares, 87 estudos.
- Pares só com CO₂ publicado com desconto (fora do cenário «sem desconto», F9): 49.

## 3. Resultado principal

Estrato principal, CO₂ sem desconto, `rma.mv` REML (metafor) com efeitos aleatórios estudo/formulação, matrizes esparsas (F64).

| Medida | Valor |
|---|---|
| k (pares) / estudos | 1.113 / 302 |
| ci médio [IC 95 %] | **10,54 [9,87–11,20]** |
| IP 95 % | 0,32 – 20,75 |
| τ² entre estudos / entre formulações | 23,17 / 3,88 |
| I² total | 99,95 % |
| Q (gl = 1.112) | 2.635.855, p < 0,001 |

## 4. Todas as análises do modelo v5

| Análise | k | Estudos | Estimativa [IC 95 %] | IP 95 % | I² |
|---|---|---|---|---|---|
| principal (ci, vi publicado + hibrido) | 1.113 | 302 | 10,54 [9,87–11,20] | 0,32 – 20,75 | 99,95 % |
| principal + sensibilidade (A7) | 1.449 | 388 | 10,19 [9,64–10,75] | 0,54 – 19,84 | 99,93 % |
| principal, CV assumido 5% (A5) | 1.113 | 302 | 10,96 [10,30–11,61] | −0,84 – 22,75 | 99,98 % |
| principal, CV assumido 10% (A5) | 1.113 | 302 | 10,75 [10,13–11,38] | −0,33 – 21,84 | 99,96 % |
| principal, CV assumido 15% (A5) | 1.113 | 302 | 10,49 [9,89–11,09] | 0,08 – 20,90 | 99,96 % |
| principal, CO2 com desconto (F1, F9: inclui os pares so com desconto) | 1.158 | 311 | 10,38 [9,71–11,05] | −0,09 – 20,86 | 99,96 % |
| principal, so cimento Portland | 930 | 272 | 10,78 [10,22–11,33] | 2,86 – 18,69 | 99,91 % |
| ci_t (kg CO2-eq/(m3.MPa.ano)), principal com vida util | 1.113 | 302 | 0,195 [0,181–0,209] | −0,017 – 0,407 | 99,95 % |
| ci no mesmo subconjunto com vida util (comparacao com ci_t) | 1.113 | 302 | 10,54 [9,87–11,20] | 0,32 – 20,75 | 99,95 % |

## 5. Famílias de material (subgrupos)

| Família | k | ci [IC 95 %] |
|---|---|---|
| concreto_armado | 82 | 15,53 [13,48–17,58] |
| ligantes | 17 | 11,67 [8,46–14,87] |
| reciclado | 131 | 11,40 [10,29–12,51] |
| opc | 401 | 11,16 [10,39–11,93] |
| scm | 302 | 9,70 [8,83–10,58] |
| uhpc | 14 | 7,50 [3,75–11,26] |
| geopolimero | 166 | 5,16 [3,80–6,52] |

**Moderadores** (teste omnibus QM):

| Moderador | k | QM | p |
|---|---|---|---|
| familia | 1.113 | 111,11 | < 0,001 |
| base_portland | 1.113 | 54,75 | < 0,001 |
| idade_cat | 1.113 | 0,63 | 0,729 |

<details><summary>Coeficientes de cada moderador</summary>

| Moderador | Termo | Estimativa [IC 95 %] | p |
|---|---|---|---|
| familia | intrcpt | 11,16 [10,39–11,93] | < 0,001 |
| familia | familiaconcreto_armado | 4,37 [2,17–6,56] | < 0,001 |
| familia | familiageopolimero | −6,00 [−7,39 a −4,62] | < 0,001 |
| familia | familialigantes | 0,51 [−2,74 a 3,75] | 0,760 |
| familia | familiareciclado | 0,24 [−0,78 a 1,26] | 0,647 |
| familia | familiascm | −1,46 [−2,16 a −0,76] | < 0,001 |
| familia | familiauhpc | −3,66 [−7,47 a 0,15] | 0,060 |
| base_portland | intrcpt | 11,28 [10,58–11,98] | < 0,001 |
| base_portland | base_portlandnao | −4,90 [−6,20 a −3,60] | < 0,001 |
| idade_cat | intrcpt | 10,42 [9,67–11,18] | < 0,001 |
| idade_cat | idade_catnao_declarada | 0,56 [−0,91 a 2,03] | 0,454 |
| idade_cat | idade_catoutra | −0,25 [−2,76 a 2,26] | 0,845 |

</details>

## 6. Viés de publicação e robustez

- Egger multinível (moderador = erro-padrão): declive 0,803 (EP 0,133), p < 0,001; intercepto 7,32.
- Leave-one-study-out (302 estudos): μ entre 10,30 (sem o estudo 2849) e 10,58 (sem o estudo 4476).

## 7.1. Transporte das matérias-primas (A2, F57)

| Análise | k | Estudos | ci [IC 95 %] |
|---|---|---|---|
| principal, todos os pares (referencia) | 1.113 | 302 | 10,54 [9,87–11,20] |
| principal, A2 incluido (F57) | 648 | 177 | 10,72 [9,78–11,66] |
| principal, A2 incluido ou parcial (F57, extra) | 787 | 212 | 10,53 [9,71–11,36] |
| principal, A2 nao incluido (excluido/parcial/nao_declarado) | 465 | 128 | 10,22 [9,35–11,09] |

**Moderador** (diferença no ci): moderador A2 incluido (vs resto), principal: 0,47 [−0,85 a 1,80], p 0,482 (k 1.113).

## 7.2. Base de medição do fck (#1454)

| Análise | k | Estudos | ci [IC 95 %] |
|---|---|---|---|
| principal, todos os pares (referencia) | 1.113 | 302 | 10,54 [9,87–11,20] |
| principal, so cilindro | 128 | 34 | 10,42 [8,75–12,09] |
| principal, so cubo | 191 | 38 | 9,44 [7,97–10,90] |
| principal, so prisma | 53 | 11 | 9,49 [6,80–12,17] |
| principal, formato declarado (cil+cubo+prisma) | 372 | 83 | 10,00 [8,94–11,05] |
| principal, sem formato escrito (indeterminado/outro/misto) | 741 | 225 | 10,74 [9,91–11,58] |

**Moderador** (diferença no ci): cubo vs cilindro: −1,29 [−3,58 a 0,99], p 0,268 (k 372); prisma vs cilindro: −0,66 [−3,99 a 2,67], p 0,699 (k 372).

## 7.3. Transporte até à obra (A4, F59)

| Análise | k | Estudos | ci [IC 95 %] | Δ vs sem A4 |
|---|---|---|---|---|
| principal, sem A4 (referencia) | 1.113 | 302 | 10,54 [9,87–11,20] | 0,0 % |
| principal, A4 grupo sim, 50 km, SIDAC x1 | 1.113 | 302 | 10,67 [10,00–11,33] | 1,2 % |
| principal, A4 grupo sim, 100 km, SIDAC x1 | 1.113 | 302 | 10,80 [10,13–11,47] | 2,5 % |
| principal, A4 grupo sim, 200 km, SIDAC x1 | 1.113 | 302 | 11,06 [10,38–11,73] | 5,0 % |
| principal, A4 grupo sim, 300 km, SIDAC x1 | 1.113 | 302 | 11,31 [10,63–12,00] | 7,4 % |
| principal, A4 grupo sim, 100 km, SIDAC x1.5 | 1.113 | 302 | 10,93 [10,26–11,60] | 3,7 % |
| principal, A4 grupo sim, 100 km, SIDAC x2.5 | 1.113 | 302 | 11,19 [10,51–11,86] | 6,2 % |
| principal, A4 grupo sim, 300 km, SIDAC x2.5 (pior caso) | 1.113 | 302 | 12,42 [11,68–13,17] | 17,9 % |
| principal, A4 grupos sim+provavel, 100 km, SIDAC x1 (opcao a parte, F38) | 1.113 | 302 | 10,93 [10,26–11,59] | 3,7 % |
| so grupo sim, sem A4 | 528 | 126 | 10,55 [9,43–11,67] | — |
| so grupo sim, A4 100 km, SIDAC x1 | 528 | 126 | 11,16 [10,03–12,28] | — |

## 7.4. Estudos secundários (F60)

| Análise | k | Estudos | ci [IC 95 %] |
|---|---|---|---|
| principal (referencia) | 1.113 | 302 | 10,54 [9,87–11,20] |
| principal + secundarios (F60) | 1.144 | 308 | 10,46 [9,81–11,12] |
| so secundarios | 31 | 6 | 7,16 [5,13–9,19] |
