---
titulo: REML Vs DL Explicacao
descricao: REML vs DerSimonian-Laird — contexto da decisão metodológica
tags: [academico-e-pesquisa, meta-analise, metodologia]
status: revisado
ultima_atualizacao: 2026-05-14
---

# REML vs DerSimonian-Laird — contexto da decisão metodológica

> Documento explicativo sobre a escolha entre os estimadores **DerSimonian-Laird (DL)** e **Restricted Maximum Likelihood (REML)** no contexto da metanálise multinível desta dissertação.
>
> Gerado em 2026-05-12 para subsidiar a decisão registrada em `tarefas.md` Bloco E (item `[?]` REML vs DL).

---

## 1. O que esses dois métodos fazem

Ambos servem ao mesmo propósito: **estimar τ² — a variância entre estudos** (*between-study variance*). Esse é o número que diz "o quanto a verdadeira eficácia varia de estudo para estudo, além do que dá para explicar por erro amostral".

τ² é o coração da metanálise de efeitos aleatórios. Ele governa:
- a largura do intervalo de confiança do efeito combinado;
- o cálculo do índice I² (proporção da variabilidade total atribuível à heterogeneidade);
- a forma do intervalo de predição.

## 2. DerSimonian-Laird (DL) — o estimador clássico

- **Origem:** DerSimonian & Laird (1986), artigo seminal sobre ensaios clínicos. Mais de 35.000 citações até hoje.
- **Mecânica:** método dos momentos — calcula τ² por fórmula fechada, sem iteração. Roda em milissegundos.
- **Adoção:** padrão da Cochrane Collaboration por décadas; ainda é o default em vários softwares de metanálise médica (RevMan, por exemplo).
- **Funciona bem quando:**
  - os estudos são **independentes** entre si;
  - o tamanho amostral é razoável (k ≥ 20 estudos);
  - a heterogeneidade não é extrema.
- **Limitação central:** só se aplica ao **modelo univariado** — onde cada estudo contribui com **uma única observação independente**. Não suporta estruturas multinível, multivariadas ou com dependência intra-cluster.

## 3. REML (Restricted Maximum Likelihood) — o estimador moderno

- **Mecânica:** baseado em verossimilhança restrita — uma versão refinada da Máxima Verossimilhança (ML) que corrige um viés conhecido da ML em pequenas amostras.
- **Adoção:** padrão dos modelos mistos lineares em estatística moderna (pacotes `lme4`, `nlme` em R); estimador default no `rma()` e no `rma.mv()` do pacote `metafor`.
- **Implementação:** iterativo — precisa convergir (milissegundos a segundos por modelo).
- **Generalizável:** funciona para qualquer estrutura de efeitos aleatórios:
  - univariada (uma observação por estudo);
  - multinível (3+ níveis — observações dentro de estudos dentro de coortes etc.);
  - multivariada (vários desfechos correlacionados por estudo);
  - com covariância arbitrária entre observações.
- **Mais robusto que DL quando:**
  - o número de estudos é pequeno (k < 20);
  - há heterogeneidade complexa;
  - existe dependência entre observações.

## 4. Por que essa "decisão" surge nesta dissertação

A decisão **não é** "DL vs REML qual é melhor em abstrato". É uma consequência direta da **decisão metodológica D3** (registrada em `tarefas.md`):

> *Cada formulação reportada por um artigo vira sua própria linha na METANÁLISE.*

Resultado prático:
- CORDOBA et al. (2023) contribui com **18 linhas** (Tabela 3, 18 misturas com OPC + SCMs nas 4 classes C25/C30/C35/C45).
- JAYASINGHE et al. (2021) contribui com **2 linhas** (C30/37 e C32/40, para sistemas estruturais distintos).
- BHAGAT et al. (2021) contribui com várias linhas (formulações M1–M8).
- Outros estudos: 1 ou poucas linhas cada.

As linhas que vêm do mesmo artigo **não são estatisticamente independentes** — compartilham laboratório, materiais brutos, equipe, equipamento, protocolo, calibração. Tratá-las como se fossem estudos separados:

- infla artificialmente o `k` efetivo;
- subestima a heterogeneidade real;
- produz intervalos de confiança falsamente estreitos;
- viola o pressuposto de independência da metanálise clássica.

## 5. Solução adotada — modelo multinível de 3 níveis

A solução padrão da literatura moderna (Cheung 2014; Assink & Wibbelink 2016; Konstantopoulos 2011) é o **modelo multinível** (3-level meta-analysis):

- **Nível 1:** erro amostral de cada observação (formulação);
- **Nível 2:** variância entre formulações dentro do mesmo artigo (`τ²₂`);
- **Nível 3:** variância entre artigos (`τ²₁`).

A implementação é feita pela função `rma.mv()` do pacote `metafor` em R, com fator aninhado tipo `random = ~ 1 | autor/formulacao` (ou `random = ~ 1 | study/effect`).

## 6. O conflito que gera a decisão

A função `rma.mv()` **não suporta DerSimonian-Laird como estimador** — DL é restrito ao modelo univariado `rma()`. Os estimadores disponíveis em `rma.mv()` são essencialmente ML e REML, com REML sendo o padrão recomendado.

Por outro lado, o documento `Justificativa_Modelo_Efeitos_Aleatorios.md` (anterior à decisão D3) cita DL como o estimador da metanálise. Esse documento descreve o modelo univariado, que foi a abordagem inicial — antes da decisão de tratar cada formulação como observação separada.

## 7. As duas opções reais

Não é uma escolha entre dois estimadores equivalentes. É uma escolha entre dois caminhos metodológicos:

### Opção 1 — Manter D3, aceitar REML (recomendada)
- **O que muda:** reescrever `Justificativa_Modelo_Efeitos_Aleatorios.md` explicando a transição DL → REML; atualizar o `[MUST]` E.1 do `tarefas.md` trocando "DerSimonian-Laird" por "REML"; ajustar comando R para `rma.mv(..., method="REML")`.
- **Vantagens:**
  - Preserva todas as 70 linhas da METANÁLISE (CORDOBA contribui com 18, JAYASINGHE com 2 etc.);
  - Modela corretamente a dependência intra-artigo (essencial pra validade estatística);
  - Estimador padrão da literatura moderna de metanálise;
  - Robusto quando k < 20 — útil porque, mesmo com 70 linhas, o número de **artigos distintos** com `ci` válido continua sendo apenas 22.
- **Desvantagens:**
  - Inconsistência narrativa com a justificativa anterior (mitigada pela reescrita);
  - Requer texto extra explicando a transição na metodologia.

### Opção 2 — Abandonar D3, manter DL univariado
- **O que muda:** descartar as observações extras por artigo (escolher uma única formulação representativa por estudo); voltar para `rma()` univariado com DL.
- **Vantagens:**
  - Mantém consistência com a `Justificativa_Modelo_Efeitos_Aleatorios.md` existente;
  - Modelo mais simples e familiar à literatura clínica clássica.
- **Desvantagens:**
  - Joga fora ~48 linhas adicionais (passa de 70 → 22 estudos);
  - Introduz **viés de seleção** ("qual formulação escolher por artigo?"); critério arbitrário (formulação ótima? controle? mediana?);
  - Perde a riqueza informacional dos estudos com múltiplas formulações (justamente os mais informativos da literatura);
  - Não modela a dependência intra-artigo de forma alguma — torna-se um modelo intencionalmente subdimensionado.

## 8. Recomendação

**Opção 1 (REML + reescrever a justificativa).**

A "transição DL → REML" se justifica metodologicamente em meia página de texto: começamos pelo estimador clássico (DL) como base conceitual didática, mas a decisão D3 — necessária pra capturar a variabilidade intra-estudo de forma honesta — exige modelo multinível, onde REML é o padrão recomendado pela literatura moderna (Viechtbauer, 2010; Assink & Wibbelink, 2016; Cheung, 2014).

DL permanece relevante na seção como referência histórica do estimador clássico, mas REML é o estimador efetivamente utilizado na execução da metanálise.

## 9. Referências

- ASSINK, M.; WIBBELINK, C. J. M. Fitting three-level meta-analytic models in R: a step-by-step tutorial. **The Quantitative Methods for Psychology**, v. 12, n. 3, p. 154–174, 2016. DOI: 10.20982/tqmp.12.3.p154.
- CHEUNG, M. W.-L. Modeling dependent effect sizes with three-level meta-analyses: a structural equation modeling approach. **Psychological Methods**, v. 19, n. 2, p. 211–229, 2014. DOI: 10.1037/a0032968.
- DERSIMONIAN, R.; LAIRD, N. Meta-analysis in clinical trials. **Controlled Clinical Trials**, v. 7, n. 3, p. 177–188, 1986. DOI: 10.1016/0197-2456(86)90046-2.
- KONSTANTOPOULOS, S. Fixed effects and variance components estimation in three-level meta-analysis. **Research Synthesis Methods**, v. 2, n. 1, p. 61–76, 2011. DOI: 10.1002/jrsm.35.
- VIECHTBAUER, W. Conducting meta-analyses in R with the metafor package. **Journal of Statistical Software**, v. 36, n. 3, p. 1–48, 2010. DOI: 10.18637/jss.v036.i03.

---

*Documento auxiliar à seção 4.2.3 do `DISSERTAÇÃO_KIÊ_v13.docx` e à justificativa metodológica em `METODOLOGIA_ESTATÍSTICA/Justificativa_Modelo_Efeitos_Aleatorios.md`. Última atualização: 12 maio 2026.*
