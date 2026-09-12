# Infraestrutura de intervalo de confiança por estudo — 2026-09-12

## Origem

A Kiê perguntou, no painel `kielima.com/metanalise`, por que o forest plot "ci por família de
material" mostra um ponto por mistura sem barra de erro. Resposta curta: **não há de onde tirar
um** — `dados_fck` só guardava valores pontuais de `fck_mpa`/`co2_valor`, nenhuma medida de
dispersão. Ao nível agregado por família dava (e dá) para calcular um IC por bootstrap com o que
já existe (proposta feita, ainda não implementada no site). Ao nível de cada linha/estudo, não —
seria preciso voltar ao PDF.

A Kiê decidiu que vale a pena fazer essa extração e pediu explicitamente (2026-09-12): criar a
coluna, e tornar isto um critério da Etapa 4 de qualidade.

## O que foi feito nesta sessão (infraestrutura, sem extração real ainda)

1. **`meta_analysis_base.xlsx`, aba `dados_fck`** — 8 colunas novas (26–33), todas vazias:
   `ic_fck_valor`, `ic_fck_tipo`, `ic_fck_n`, `ic_fck_citacao`, `ic_co2_valor`, `ic_co2_tipo`,
   `ic_co2_n`, `ic_co2_citacao`. Ver descrição completa em `CRITERIOS_E_NUANCES_RSL.md`, secção
   "QG — Dispersão/intervalo de confiança declarado".
2. **`articles_final.xlsx`** — 1 coluna nova (55): `QG_intervalo_confianca`, vazia em todo o
   banco. `E4_qualidade_total`/`E4_estrato` (col 53–54) **não foram tocadas** — continuam no
   checklist de seis itens, exactamente como estavam.
3. **`CRITERIOS_E_NUANCES_RSL.md`** — rubrica proposta para QG (0/0,5/1,0), com o aviso explícito
   de que é uma proposta pendente de confirmação da Kiê antes de pontuar qualquer linha (segue a
   própria regra de pré-especificação já escrita neste ficheiro para a estratificação por
   terços) e o alerta de não recalcular `E4_qualidade_total`/`E4_estrato` até QG estar pontuado
   nas 651 linhas já avaliadas.
4. **`IC_QG_WORKLIST_2026-09-12.csv`** — as 651 linhas de `articles_final.xlsx` já pontuadas na
   Etapa 4 (as mesmas que têm `E4_qualidade_total` preenchido), com título/autor/ano/DOI/PDF e
   uma coluna `QG_intervalo_confianca` vazia para preencher lote a lote — mesmo formato dos
   outros worklists do vault (`DUVIDAS_DE_CRITERIO.csv`, `SEM_PDF_WORKLIST_2026-08-21.csv` etc.).
5. **kielima.com/metanalise** — o gráfico "Progresso da extração" passou a mostrar três frentes
   separadas: resistência×CO₂ (histórico existente, inalterado), volume do corpo de prova
   (`vol_corpo_prova_m3`, 79 linhas já extraídas até hoje) e intervalo de confiança (0 linhas —
   a coluna acabou de ser criada). Ver PR do site para o detalhe.

## ✅ Piloto de 9 artigos concluído (2026-09-12)

Amostra deliberadamente diversa (artigos experimentais, dissertações, revisão, modelo
estatístico, várias editoras) lida e pontuada por completo, incluindo renderização visual das
figuras — ver a tabela e a análise completa em `CRITERIOS_E_NUANCES_RSL.md`, secção QG. Já
aplicado ao banco: `QG_intervalo_confianca` preenchido nas 9 linhas (`articles_final.xlsx`), e
`ic_fck_tipo`/`ic_fck_citacao` preenchidos nas 3 linhas de HAIGH 2024b (`dados_fck`, linhas
420-422 — dispersão confirmada só visualmente, valor exato ainda por transcrever).

**Resultado: 0/9 chegou a QG=1,0, 1/9 (11%) a QG=0,5, 8/9 (89%) ficou em QG=0.** Três achados
metodológicos confirmados (STDEV agregada ≠ dispersão por linha; dispersão citada de outro
estudo não conta; dispersão pode existir só em figura, nunca em texto — precisa sempre
renderizar, nunca só regex).

**Decisão pendente da Kiê:** com a rubrica validada e o rendimento esperado conhecido (baixo),
falta decidir se vale a pena reabrir os ~640 artigos restantes agora, sabendo que a maioria
provavelmente vai dar QG=0, ou se isto fica para depois de outras pendências (tarefa #7,
Supabase #1383). Ver a recomendação completa em `CRITERIOS_E_NUANCES_RSL.md`.

## O que falta (trabalho de releitura, não de infraestrutura)

- **Decidir a priorização acima** antes de continuar a extração das ~640 linhas restantes.
- **Extrair, artigo a artigo, o resto do worklist**: reabrir o PDF (texto **e** figuras
  renderizadas — o piloto confirmou que a dispersão pode existir só visualmente), procurar
  desvio-padrão/CoV/IC nas tabelas e gráficos de resultados (resistência e, mais raramente,
  CO₂), preencher as colunas `ic_fck_*`/`ic_co2_*` em `dados_fck` para cada mistura, e o
  `QG_intervalo_confianca` em `articles_final.xlsx` para o artigo.
- **Transcrever com precisão o valor visual pendente de HAIGH 2024b** (linhas 420-422) — leitura
  de pixel da Fig. 3, não feita no piloto (só confirmada a existência).
- **Só depois de QG estar pontuado nas 651 linhas**, recalcular `E4_qualidade_total`/`E4_estrato`
  com sete itens (correr uma versão actualizada de `apply_e4_estrato.py`) e reavaliar se a
  estratificação por terços muda.
- **Implementar o cálculo do IC real** no site — bootstrap ao nível agregado por família (não
  precisa de QG); IC por linha/estudo só é possível para as linhas cujo QG ≥ 0,5.

## Ficheiros desta sessão

| Ficheiro | Conteúdo |
|---|---|
| `EXTRACAO_IC_QG_2026-09-12.md` | Este ficheiro |
| `IC_QG_WORKLIST_2026-09-12.csv` | As 651 linhas a rever, uma vez a rubrica QG confirmada |
| `CRITERIOS_E_NUANCES_RSL.md` | Secção "QG — Dispersão/intervalo de confiança declarado" |
