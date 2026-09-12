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

**Decisão da Kiê:** "Pode continuar" — extração completa autorizada na mesma sessão, seguida de
"Pode recalcular" para o passo de `E4_qualidade_total`/`E4_estrato`. Ambos concluídos em
2026-09-12.

## ✅ CONCLUÍDO (2026-09-12) — extração completa + recálculo de qualidade

- **As 651 linhas do worklist têm `QG_intervalo_confianca` preenchido.** Processadas em 65 lotes
  de subagentes (~10 artigos cada, 8 lotes por onda), com verificação obrigatória do mapeamento
  `dados_fck_linha↔row_id` antes de cada escrita (apanhou 1 erro real de subagente — linha 4560,
  citação de `dados_fck_linha` errada, corrigida por cross-check antes de aplicar) — mais 1 lote
  (`lote_005`, 10 linhas) que tinha sido processado numa onda muito anterior mas nunca chegou a
  ser aplicado ao banco, descoberto e fechado ao verificar a cobertura total do CSV.
- **Resultado: 557 QG=0 (86%) · 93 QG=0,5 (14%) · 1 QG=1,0 (0,2%, linha 2684, HAFEZ 2024b).**
  Confirma a previsão do piloto: rendimento baixo, e nenhum achado positivo surgiu só por busca
  de texto — todos exigiram renderizar o PDF (barra de erro visual) ou ler o texto corrido com
  atenção às armadilhas (dispersão agregada entre misturas, dispersão de estudo citado, Monte
  Carlo sobre input assumido vs. sobre o próprio output).
- **`E4_qualidade_total`/`E4_estrato` recalculados com os sete itens** (autorização explícita da
  Kiê). Sobre os 594 artigos Elegível: cutoff de terços = 4,0/7,0 → **466 principal, 128
  sensibilidade**. Só 4 linhas mudaram de estrato face à estratificação de seis itens (2628,
  3155, 3852, 4813) — todas no limite exato do corte anterior (QA-QF=3,5), que o QG=0,5 recém-
  pontuado empurrou para 4,0. Ver `CRITERIOS_E_NUANCES_RSL.md`, secção "Extração completa", para
  o detalhe.
- Ver PRs #186-198 no repositório para o histórico lote a lote (waves 1-7 + gap-fill).

## O que ainda falta (não bloqueado, trabalho à parte)

- **Transcrever com precisão os valores visuais aproximados** — dezenas de achados QG=0,5 desta
  extração registaram só a existência de dispersão (barra de erro confirmada visualmente ou por
  texto) sem o valor numérico exato, porque a leitura de pixel/OCR fina não fazia parte do
  escopo desta tarefa. `ic_fck_citacao`/`ic_co2_citacao` em `dados_fck` documentam onde cada
  valor pendente está (figura, página) para quem quiser fazer essa transcrição depois.
- **Implementar o cálculo do IC real** no site — bootstrap ao nível agregado por família (não
  precisa de QG); IC por linha/estudo só é possível para as linhas cujo QG ≥ 0,5 e com valor
  numérico transcrito (não aproximado).

## Ficheiros desta sessão

| Ficheiro | Conteúdo |
|---|---|
| `EXTRACAO_IC_QG_2026-09-12.md` | Este ficheiro |
| `IC_QG_WORKLIST_2026-09-12.csv` | As 651 linhas a rever, uma vez a rubrica QG confirmada |
| `CRITERIOS_E_NUANCES_RSL.md` | Secção "QG — Dispersão/intervalo de confiança declarado" |
