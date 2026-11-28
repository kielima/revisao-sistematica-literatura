# Registo de edições da dissertação (tracked changes)

Gerido pela skill `dissertacao-tracked-changes`. Uma linha por pedido; estados: `pendente`, `enviado (cartão, data)`, `aplicado (tracked, data)`, `por resolver (motivo)`.

| id | data | origem | secção alvo | texto proposto | estado |
|---|---|---|---|---|---|
| — | 2026-10-18 | teste do canal (sessões locais) | introdução/metodologia (parágrafo livre) | teste de edição com tracked changes no `v20`; **por confirmar** se as revisões estão no ficheiro | aplicado e confirmado (2026-10-23, workflow `ler-revisoes-docx.yml`, run 39678132534): 3 alterações em tracked changes (autor Claude, 18/10) numa frase da Introdução do v20.docx — vírgula removida, oração redundante «, principal ligante do concreto,» removida, «insubstituível» → «dificilmente substituível» — com 3 comentários |

## Perguntas de agosto/2026 ainda abertas no v20.docx (comentários do autor «Claude», 19/08)
Respostas propostas em 2026-10-23; **nenhuma aplicada ao Word** — dependem da Kiê (e, quando aprovadas, de um cartão para a sessão local).

| id | origem | pergunta | resposta proposta | estado |
|---|---|---|---|---|
| E-001 | glossário vs. secção ABCIC/SNIC (capítulo «Desmaterialização da Construção Civil») | MRV: «Monitoramento» ou «Mensuração»? E o resto da frase | **APROVADO pela Kiê em 2026-10-23.** Fonte lida por completo: SNIC (SEGS, 01/12/2020), p. 2: «um sistema de Monitoramento, Relato e Verificação (MRV) robusto e confiável seja implementado» antes de uma política de precificação de carbono. Penna (2025, página ABCIC, 100%) e Roadmap Net Zero 2025 (PDF ABCP, 44 p.) NÃO têm MRV, RenovaCalc nem EPD. Reescrever a frase «A ABCP e a ABCIC recomendam a adoção de EPDs setoriais, o uso da ferramenta RenovaCalc e a construção, no médio prazo, de um sistema de mensuração, relato e verificação (MRV) robusto, considerado pré-requisito para a eventual implantação do mercado regulado de carbono brasileiro (SNIC, 2015; Penna, 2025).» por: **«O setor defende que, antes da entrada em vigor de uma política de precificação de carbono, seja implementado um sistema de Monitoramento, Relato e Verificação (MRV) robusto e confiável (SNIC, 2020).»** EPDs setoriais e RenovaCalc saem (sem fonte lida). Pendentes à parte: ano da referência SNIC (2015 → 2020 pelo documento) e «ABCIC» (a fonte nomeia SNIC e ABCP). | aprovado, por aplicar no Word |
| E-002 | correções da banca #1100 | «Simplificar» as strings de busca: (a) apagar o relato das 3 tentativas ou (b) só cortar redundância? | **Recomendação (b)**, com o relato condensado numa frase («testaram-se strings de maior e menor abrangência; a final recuperou N documentos») e as strings intermédias movidas para apêndice. Mantém o rigor do processo iterativo (PRISMA) e atende à banca. | pendente |
| E-003 | correções da banca #1105 | Origem de fck = 29 MPa (CC) e 121 MPa (UHPC) no fim de «Unidade Funcional» | **UHPC 121 MPa: coincide com a mediana do fck das 39 observações UHPC da metanálise (121,5 MPa; `metanalise/dados_metanalise.csv`, família `uhpc`).** **CC 29 MPa: não coincide com nenhuma mediana atual** (opc 35,0; concreto armado 34,5; reciclado 34,1; todos 39,4) — pode vir de uma versão anterior do banco ou de um estudo específico. **Por confirmar** antes de citar; sugestão: citar a mediana da metanálise para ambos e atualizar o valor de CC. | pendente (por confirmar) |
| E-004 | correções da banca #1126 | IPCC/ONU nas referências: expandir a sigla? | **Sim, expandir** — pedido da banca (Renata), a ABNT permite as duas formas e a expansão não custa nada: «INTERGOVERNMENTAL PANEL ON CLIMATE CHANGE (IPCC).» e «ORGANIZAÇÃO DAS NAÇÕES UNIDAS (ONU).» nas 3 entradas. | pendente |

## Pendentes do congelamento de 28/11/2026 (F65) — para a sessão do Word

**Fonte única dos números:** `metanalise/RESULTADOS_CONGELADOS_2026-11-28.md` (todos com vírgula decimal, prontos a copiar). **Decisões:** `metanalise/DECISOES_METANALISE.md` (F-id ao lado de cada item). Nenhum destes itens foi ainda aplicado ao Word; estado inicial `pendente`. Aplicar com a skill `dissertacao-tracked-changes` (alterações controladas no original) e actualizar o estado aqui.

| id | secção alvo | o que entra | fonte | estado |
|---|---|---|---|---|
| D-001 | Resultados — corpus e PRISMA (#1937, #1942) | Fluxograma e números: 5.093 → 2.630 duplicados → 2.463 → 272 (E1) → 2.191 → 6 sem texto → 2.185 → 1.643 (E2) → 542 → 18 (E3) → 524 → 58 revisões → **466 corpus** → 104 sensibilidade → **362 principal**; 1.498 pares de 398 estudos; [N] do corpus = 466 | congelado §1–2; `00_REFERENCIAS/PRISMA/FLUXOGRAMA_PRISMA_2020_DOC.md`; F56 | pendente |
| D-002 | Resultados — resultado principal (#1937) | **ci = 10,54 [9,87–11,20] kg CO₂-eq/(m³·MPa)**, k 1.113, 302 estudos; IP 0,32–20,75; τ² 23,17 / 3,88; I² 99,95 %; Q e p | congelado §3 | pendente |
| D-003 | Resultados — análises do modelo (#1937) | principal + sensibilidade 10,19; CV assumido 5/10/15 %; com desconto 10,38; só Portland 10,78; **ci_t 0,195 [0,181–0,209]** kg CO₂-eq/(m³·MPa·ano) | congelado §4; F33, F57 | pendente |
| D-004 | Resultados — famílias e moderadores (#1937) | 7 famílias (concreto armado 15,53 … geopolímero 5,16); moderadores família e base Portland p < 0,001; idade do ensaio p = 0,729 | congelado §5; D2/D5–D8 | pendente |
| D-005 | Resultados — viés e robustez (#1937) | Egger multinível (declive 0,803, p < 0,001); leave-one-out 10,30–10,58 | congelado §6 | pendente |
| D-006 | Resultados — sensibilidades (#1937) | A2 (10,72 vs 10,54, moderador p = 0,482); corpo de prova (cubo vs cilindro p = 0,268); **A4 como tabela** (sem A4 10,54 → 100 km 10,80 → pior caso 12,42, +17,9 %); secundários 10,46 (31 pares, 6 estudos) | congelado §7; `metanalise/resultados/tabela_a4_dissertacao.md`; F57, #1454, F59/F63, F60 | pendente |
| D-007 | Método — modelo | `rma.mv` (metafor), REML, efeitos aleatórios estudo/formulação, **matrizes esparsas** (F64); vi publicado + híbrido (A3–A5); `ci` = desfecho primário, `ci_t` secundário (F57) | F64, A3–A6, F57 | pendente |
| D-008 | Método — estratificação por qualidade (#1333) | 7 itens E4; corte 4,0/7 = percentil 33 com empates a subir; 104 abaixo (22 %, não 33 %, por 63 empates em 4,0) | `metanalise/LINHA_CRITICA_2026-12-02.md` §1; F56 | pendente |
| D-009 | Método — idade do ensaio (#1583) | hierarquia: ensaio próprio > idade escrita no artigo > norma citada > notação de norma (Cxx/yy, HA-xx) > vazio | CLAUDE.md (idade, 04/10); F53 | pendente |
| D-010 | Método — vida útil do `ci_t` | hierarquia declarada > citada > norma pela aplicação > 50 anos (premissa nossa, explícita) | F33 | pendente |
| D-011 | Método — transporte A4 | fórmula A4 = factor SIDAC × massa volúmica × distância; só grupo `sim` (prováveis à parte); factores ×1,5/×2,5; painel interactivo com superfície 0–300 km | F38, F40, F43, F59, F63 | pendente |
| D-012 | Limitações | buscas até 15/04/2025 (F61); secundários só como sensibilidade, 6 de 9 lidos — FERNANDO 2021 e SALAS 2018 em falta (F60); A4 sem regresso em vazio e massa 2.400 kg/m³ quando não declarada (F43/F48); 886 pares sem formato de corpo de prova escrito (#1454) | F60, F61, F48, #1454 | pendente |
| D-013 | Método — #1331 e #1332 | justificativas pedidas nessas tarefas (o enunciado está no app de tarefas, não no vault) | tarefas #1331/#1332 | por resolver (ler a tarefa) |
| D-014 | Discussão, Conclusão, Resumo (#1938–#1940, prazo 11/12) | escrever a partir de D-001…D-012 | congelado | pendente |
