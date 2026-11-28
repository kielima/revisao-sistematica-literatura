---
titulo: Linha crítica — metanálise completa com resultados até quarta-feira 02/12/2026
descricao: Varredura do vault e das tarefas a 26/11 e caminho crítico para congelar os resultados da metanálise
tags: [academico-e-pesquisa, meta-analise, planeamento]
status: arquivado
ultima_atualizacao: 2026-11-28
---

# Linha crítica até quarta-feira, 02/12/2026

> ✅ **CONCLUÍDA a 28/11/2026 (F65).** A Kiê antecipou a rodada final para 28/11: números congelados em `metanalise/RESULTADOS_CONGELADOS_2026-11-28.md`; a tarefa agendada de 01/12 foi apagada. O que resta é escrita (§5) — lista em `dissertacao/EDICOES_DISSERTACAO.md`.

Pedido da Kiê (26/11): «varredura completa do vault e da metanálise e linha crítica de tarefas para entregar a metanálise completa com os resultados até quarta-feira». Fontes da varredura: `main` em `b4f8dc4` (F44–F58 integradas), `metanalise/DECISOES_METANALISE.md`, `COORDENACAO_AGENTES.md`, tarefas abertas do projecto «Concluir RSL com Meta-análise» (33) e do projecto «Dissertação» no app.

## 1. Onde estamos (medido a 26/11)

| Componente | Estado | Falta |
|---|---|---|
| Funil / PRISMA (F56) | 5.093 → 466 Elegíveis → **362 principal** + 104 sensibilidade; fluxograma refeito | só regularizações de `etapa_saida` (não mudam contagens) |
| Pares fck × CO₂ (painel e modelo) | **1.498 pares, 398 estudos** (F47, limiar 20 MPa como filtro) | nada bloqueante |
| Modelo v5 (F57, provisório) | principal **μ 10,54 [9,87–11,20]**, k 1.113, 302 estudos; LOO 10,30–10,58 (23/11); famílias, Portland, desconto, CV, Egger, `ci_t` 0,195 | **rodada final** com os dados congelados |
| Sensibilidades já feitas | transporte A2 (F57), base do fck cilindro/cubo/prisma (#1454) | correr de novo na rodada final |
| A4 — leitura e gravação | fases 1–2b feitas (F41–F46, F51–F55, F58); massa lida em 645 pares; motor (F48) e validação (F49) feitos | **sensibilidade A4 no modelo e no painel (#1808) — não começada** |
| Estratificação por terços (#1333) | **verificado agora:** com os 466 escores e «empates sobem», o p33 cai em **4,0** → os 104 abaixo de 4,0 = exactamente o estrato `sensibilidade` actual (22 %, não 33 %, por causa dos 63 empates em 4,0) | **nada a recalcular**; só escrever a justificativa (o F56 dizia que a regra dos terços «ainda não foi executada» — os números coincidem) |
| Intervalos de confiança (#1812) | potencial contado e lote IC-C aplicado (F54) | nada bloqueante |
| Idade do ensaio (#1810) | fechada (F53) | — |
| Estudos secundários (#1811) | rastreio dos 65: 9 prováveis, 6 duvidosos, 50 improváveis; BIANCO lido (+9 pares, ainda fora do modelo) | decidir âmbito (§3, D2) |
| Buscas actualizadas (#1971) | não começada | inviável até 02/12 (§3, D3) |

## 2. Caminho crítico (ordem e datas)

O pedido da Kiê antecipa o corte de dados da F57 (03/12) e a rodada final (04/12) em dois dias. Proposta: **corte de dados segunda 30/11 às 23:59; rodada final terça 01/12; congelamento quarta 02/12.**

| Dia | Tarefa | Quem | Depende de | Duração |
|---|---|---|---|---|
| **Sex 27/11** | **Decisões D1–D4** (§3) | Kiê | — | 15 min |
| Sex 27 → Sáb 28 | **#1808 parte R**: `metanalise/sensibilidade_a4.R` sobre `transporte_a4_motor.csv` (grupo `sim`, modo padrão; 50/100/300 km; factor SIDAC ×1 / ×1,5 / ×2,5 da F49; «prováveis» como opção à parte se D1 = sim) + linha no `exportar_forest_site.R` | agente RSL | D1 | ~1 dia |
| Sáb 28 → Dom 29 | **#1808 parte painel** (`kielima-site`, /metanalise): controlo distância × modo, `ci` com A4 onde somável; números marcados provisórios até 02/12 | agente do site | parte R | ~1 dia |
| Sex 27 → Dom 29 (paralelo) | **#1811** — só o que D2 permitir (ex.: os 8 prováveis restantes, como sensibilidade) | agente RSL (2.º subagente) | D2 | 1–2 dias |
| **Seg 30/11** | **Corte de dados 23:59.** Fechar o que estiver pronto; o resto → «em andamento» (limitações). Integrador único grava os `.xlsx` (COORDENACAO §5) | agente RSL | — | — |
| **Ter 01/12** | **Agendada para 9h (Brasília), sessão nova automática — tarefa `trig_01TCMzFyqjHAFQ2y7KNWiZRR`.** **Rodada final (#1976): `bash metanalise/rodada_final.sh --site ../kielima-site --recalcular`** (script único, 28/11): recálculo das colunas derivadas → PRISMA → `preparar_dados.py` → motor A4, A2, corpo de prova → v5 com LOO → 4 sensibilidades → forest → superfície do A4 → painel (DATA, funil, KPI, MODELO, A4, mapa, banco) → conferência de 22 pontos em `resultados/CONFERENCIA_RODADA.md` (pára se falhar). Depois: `npm run testar` no site, PRs dos dois repositórios. **Ensaio de 28/11 com os dados de 21/11: tudo confere, ~30 min com a superfície do A4 (3 min sem ela).** | agente RSL | corte | ~1 h |
| **Qua 02/12** | **Congelamento:** copiar `metanalise/resultados/RESULTADOS_RODADA.md` (gerado pela rodada de terça por `gerar_resultados.py`: PRISMA, corpus, principal, todas as análises do v5, famílias, moderadores, Egger, LOO, 4 sensibilidades) para `metanalise/RESULTADOS_CONGELADOS_2026-12-02.md`; tag/release do repositório (#1970), entrada F-nn, `CLAUDE.md`, registo do `COORDENACAO_AGENTES.md` | agente RSL | rodada final | ~1 h |

Folga: o corte de segunda deixa terça e quarta para refazer a rodada se a conferência falhar. Se #1808 não estiver pronta no sábado à noite, a sensibilidade A4 entra só como tabela da grelha (`transporte_a4_grelha.csv`, já existente) e o painel fica para depois — **não atrasa o congelamento**.

## 3. Decisões que bloqueiam (uma de cada vez, no chat)

- ✅ **D1 — DECIDIDA (Kiê, 27/11: «Aceito»; registada na F59). #1809/F49:** A4 na opção principal só no grupo `sim`; os «prováveis» como opção à parte; sensibilidade de factor ×1,5 e ×2,5 sobre o SIDAC betoneira. **Recomendação: sim às três.**
- ✅ **D2 — DECIDIDA (Kiê, 27/11: «Sim»; F60). #1811 âmbito:** os pares dos estudos secundários entram **só como sensibilidade** (não no principal, para não contar duas vezes estudos que já estão no corpus) e só os 9 prováveis (BIANCO + 8). **Recomendação: sim**; o resto → limitação.
- ✅ **D3 — DECIDIDA (Kiê, 27/11: «Aceito, pode colocar como limitação»; F61). #1971 buscas actualizadas:** fora do prazo (7 bases + triagem E1–E4); passa a limitação/trabalho futuro. **Recomendação: adiar.**
- ✅ **D4 — DECIDIDA (Kiê, 27/11: «Aceito»; F62). Corte de dados antecipado para seg 30/11 23:59** (substitui o 03/12 da F57). **Recomendação: sim.**

## 4. Não bloqueia os números (vale a regra mais restritiva até haver decisão)

Ficam como estão no congelamento e podem ser decididos depois sem mudar o resultado principal:
- F47 — excepção para o par 3419 l.1002 (16,0 MPa): fica fora (filtro 20 MPa).
- F51 — 35 pares `premissa_do_artigo`, densidades de EPD, 5 DERIVADA, ASARE; F58 — QA 1 → 0,5 em BAYKARA/RABIE; 24 pares retidos «aguarda #1832»; CUNNINGHAM l.1093 (Na₂SO₄): efeito nulo ou mínimo no motor (premissa F43).
- Regresso em vazio do SIDAC (F40/F48): não aplicado; declarar na limitação.
- #1712 (perguntas de famílias restantes), #1851 (dependências órfãs), regularizações de `etapa_saida` da F56, `F40` obsoleto no registo de frentes.

## 5. Depois de 02/12 (fora da linha crítica da metanálise)

Escrita com os números congelados: Resultados #1937, Discussão #1938, Conclusão #1939, Resumo #1940 (prazo 11/12), #1942 ([N] do corpus), #1333/#1332/#1331/#1583 (justificativas no método), #1970 (DOI Zenodo), entrega 18/12.
