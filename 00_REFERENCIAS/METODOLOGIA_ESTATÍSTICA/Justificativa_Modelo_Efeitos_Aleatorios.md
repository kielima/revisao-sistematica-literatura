---
titulo: Justificativa Modelo Efeitos Aleatorios
descricao: Justificativa para Adoção do Modelo Multinível de Efeitos Aleatórios com Estimador REML na Meta-Análise
tags: [academico-e-pesquisa, meta-analise, metodologia]
status: revisado
ultima_atualizacao: 2026-05-14
---

# Justificativa para Adoção do Modelo Multinível de Efeitos Aleatórios com Estimador REML na Meta-Análise

> **Nota sobre a evolução metodológica deste documento.** A versão original deste arquivo justificava a adoção do modelo univariado de efeitos aleatórios de DerSimonian & Laird (1986). A presente versão preserva essa argumentação como base didática (seções 2 a 5) e adiciona, a partir da seção 6, a justificativa para a transição ao **modelo multinível de três níveis** com estimador **REML (*Restricted Maximum Likelihood*)**. A transição decorre da decisão metodológica D3 da RSL — que trata cada formulação de concreto como observação independente —, a qual introduz dependência intra-estudo e torna o modelo univariado clássico inadequado. DerSimonian-Laird permanece referenciado como o estimador clássico do método dos momentos, contextualizando a evolução metodológica.

---

## 1. Contexto da decisão

A meta-análise desta pesquisa tem por objetivo combinar os resultados de múltiplos estudos que quantificaram as emissões de CO₂-eq do Concreto de Ultra Alto Desempenho (UHPC) em comparação ao concreto convencional, utilizando a Avaliação do Ciclo de Vida (ACV) como ferramenta de análise. A escolha do modelo estatístico de combinação dos resultados — efeitos fixos, efeitos aleatórios univariado ou efeitos aleatórios multinível — é uma decisão metodológica fundamental, com impacto direto na validade das inferências produzidas.

Duas decisões prévias orientam o desenho estatístico adotado:

- **Decisão D3 (banco da RSL, 2026):** cada formulação de concreto reportada por um estudo primário é registrada como uma observação separada na aba METANÁLISE do banco. Estudos com múltiplos traços contribuem, portanto, com múltiplas linhas (e múltiplos valores de ci e ci_t).
- **Decisão de desfecho primário (13/05/2026):** o desfecho primário da meta-análise é ci_t (kg CO₂eq/(m³·MPa·ano)), que normaliza emissões por resistência *e* vida útil. ci (kg CO₂eq/(m³·MPa)) é a análise de sensibilidade, conduzida sobre os estudos sem vida útil declarada. ci_t = ci ÷ vida_útil (taxa anual; quanto menor, mais eco-eficiente). Fórmula corrigida em 12/05/2026 — era erroneamente ci × vida_útil.

A consequência estatística direta da decisão D3 é que as observações deixam de ser independentes — formulações oriundas de um mesmo estudo compartilham método de ACV, banco de inventário, matriz energética e equipe de pesquisa. Esse fato, ausente do modelo univariado clássico, motiva a adoção do modelo multinível detalhada nas seções 6 a 8.

---

## 2. Diferença conceitual entre os modelos univariados

### 2.1 Modelo de Efeitos Fixos

O modelo de efeitos fixos assume que **todos os estudos incluídos estimam um único efeito real e verdadeiro**, e que as diferenças observadas entre eles decorrem exclusivamente de erro amostral (variação aleatória dentro de cada estudo). Matematicamente, o peso de cada estudo na média ponderada é proporcional ao inverso de sua variância interna:

$$w_i = \frac{1}{\sigma_i^2}$$

Esse modelo é adequado quando os estudos são virtualmente idênticos em termos de população, intervenção, comparação e desfecho — uma condição raramente atendida em revisões de materiais de construção.

### 2.2 Modelo de Efeitos Aleatórios univariado (DerSimonian & Laird)

O modelo de efeitos aleatórios univariado assume que **cada estudo estima um efeito verdadeiro próprio**, e que esses efeitos verdadeiros variam em torno de uma distribuição (normalmente uma distribuição normal). O objetivo é estimar a média dessa distribuição. O peso de cada estudo é calculado como:

$$w_i = \frac{1}{\sigma_i^2 + \tau^2}$$

onde **τ² (tau-quadrado)** é o parâmetro de variância entre estudos — representa o quanto os efeitos verdadeiros diferem entre si. A presença de τ² torna o modelo mais conservador (intervalos de confiança mais amplos), o que reflete de forma mais honesta a incerteza real quando os estudos são heterogêneos.

O estimador clássico de τ² nesse modelo é o **método dos momentos de DerSimonian & Laird (1986)**, frequentemente abreviado como **DL**. Trata-se do estimador histórico mais difundido em meta-análises clínicas e ambientais e foi, por décadas, o padrão de pacotes como o `meta` e a função `rma()` do `metafor` em R (VIECHTBAUER, 2010).

---

## 3. Fontes de heterogeneidade esperadas

No contexto desta RSL sobre ACV do UHPC, são esperadas diferenças substanciais entre os estudos incluídos nas seguintes dimensões:

| Fonte de heterogeneidade | Exemplos observados na literatura |
|---|---|
| Traço e composição do UHPC | Variação no teor de cimento, sílica ativa, metacaulim, fibras de aço |
| Fronteira do sistema na ACV | Berço ao portão (*cradle-to-gate*), berço ao uso (*cradle-to-use*), berço ao túmulo (*cradle-to-grave*) |
| Unidade funcional adotada | Por kg de material, por m³, por elemento estrutural, por desempenho equivalente |
| Banco de dados de ICV utilizado | ecoinvent, GaBi/Sphera, SimaPro, bases nacionais |
| Intensidade de carbono da matriz energética local | Varia significativamente entre países e regiões |
| Método de avaliação de impacto | CML, ReCiPe, TRACI, entre outros |

Essas diferenças indicam que cada estudo não está estimando um único efeito universal, mas sim um efeito específico ao seu contexto metodológico e geográfico. Portanto, a premissa do modelo de efeitos fixos é violada.

---

## 4. Indicadores estatísticos de heterogeneidade

A heterogeneidade entre os estudos será avaliada pelos seguintes indicadores, a serem reportados nos resultados:

### 4.1 Teste Q de Cochran

Testa a hipótese nula de que toda a variabilidade entre os estudos é explicada pelo acaso. Um **p-valor < 0,05** indica heterogeneidade estatisticamente significativa. Limitação: baixo poder estatístico com poucos estudos e excesso de poder com muitos.

### 4.2 Estatística I² de Higgins

Expressa a proporção da variabilidade total que é atribuída a diferenças reais entre os estudos (e não ao erro amostral). Não depende do número de estudos. Interpretação convencional (HIGGINS et al., 2003):

| I² | Interpretação |
|---|---|
| < 25% | Heterogeneidade baixa |
| 25% – 75% | Heterogeneidade moderada |
| > 75% | Heterogeneidade alta |

Em revisões de ACV de materiais de construção, valores de I² superiores a 75% são frequentemente reportados, o que é consistente com a natureza metodologicamente diversa dos estudos primários.

### 4.3 τ² (Tau-quadrado)

Estimativa da variância entre os efeitos verdadeiros dos estudos. Um valor de τ² > 0 confirma a existência de variabilidade real entre os efeitos, reforçando a adequação do modelo de efeitos aleatórios. No modelo multinível adotado nesta meta-análise (seção 7), τ² é decomposto em dois componentes — τ²₁ (entre estudos) e τ²₂ (entre formulações intra-estudo) —, conforme detalhado adiante.

---

## 5. Justificativa formal para adoção do modelo de efeitos aleatórios univariado

A adoção de um **modelo de efeitos aleatórios** — em oposição ao modelo de efeitos fixos — nesta meta-análise justifica-se pelos seguintes argumentos:

1. **Heterogeneidade metodológica esperada:** os estudos incluídos diferem substancialmente em traço do UHPC, fronteira do sistema, unidade funcional, banco de dados e contexto geográfico — condições que violam a premissa de homogeneidade do modelo de efeitos fixos.

2. **Generalização dos resultados:** o modelo de efeitos aleatórios permite generalizar os achados para uma população mais ampla de condições (diferentes traços, contextos e metodologias de ACV), sendo mais adequado quando o objetivo é produzir uma estimativa de efeito médio generalizável, e não restrito às condições específicas dos estudos incluídos.

3. **Conservadorismo e honestidade científica:** ao incorporar o parâmetro τ² na estimativa de incerteza, o modelo de efeitos aleatórios produz intervalos de confiança mais amplos e, portanto, mais realistas diante da diversidade metodológica dos estudos.

4. **Prática consolidada na literatura de ACV:** revisões sistemáticas com meta-análise em sustentabilidade de materiais de construção adotam consistentemente o modelo de efeitos aleatórios (e.g., MARINKOVIĆ et al., 2023; PACHECO; DE BRITO; LAMPERTI TORNAGHI, 2023).

> Caso os indicadores I² e Q de Cochran indiquem heterogeneidade baixa (I² < 25% e p > 0,10), o modelo de efeitos fixos poderá ser considerado como análise de sensibilidade, mas o modelo de efeitos aleatórios permanecerá como análise principal.

Essa justificativa, contudo, **resolve apenas a primeira camada do problema** — a heterogeneidade entre estudos. Resta a heterogeneidade *dentro* de cada estudo, introduzida pela decisão D3, que é tratada na seção seguinte.

---

## 6. Por que a transição para o modelo multinível?

A decisão metodológica D3 da RSL — registrar cada formulação de concreto como observação independente na aba METANÁLISE — produz um banco em que **as observações não são todas independentes entre si**. Formulações oriundas de um mesmo estudo compartilham, por construção, um conjunto de fatores não observados: laboratório, equipe de pesquisa, método de ACV, banco de inventário, matriz energética local, premissas de fronteira do sistema e período de coleta de dados.

A magnitude dessa dependência foi quantificada no banco atual (101 observações, 22 estudos, atualizado em 13/05/2026 com incorporação do CELIK 2015):

- **68% dos estudos (15 de 22) contribuem com múltiplas formulações** para a meta-análise.
- **Maioria das observações pertence a clusters multi-formulação**, a estudos que aportam mais de uma linha.
- Os quatro maiores clusters concentram parcela expressiva das observações: **CORDOBA (18 formulações), COELHO (21 formulações), CELIK (13 formulações), BHAGAT (5), SANCHEZ-PANTOJA (5) e DYNAN (4)**.

Esses números demonstram que a dependência intra-estudo **não é uma anomalia marginal a ser ignorada**, e sim a estrutura predominante dos dados. Tratar todas as 101 observações como independentes em um modelo univariado clássico violaria o pressuposto central da meta-análise — inflando artificialmente o tamanho efetivo da amostra, subestimando a variância e produzindo intervalos de confiança falsamente estreitos (CHEUNG, 2014; ASSINK; WIBBELINK, 2016).

A literatura metodológica é convergente: quando há *múltiplos tamanhos de efeito por estudo*, a abordagem estatisticamente correta é o **modelo multinível de três níveis** (KONSTANTOPOULOS, 2011; CHEUNG, 2014). Estratégias alternativas — como agregar formulações em uma média por estudo, sortear uma formulação por estudo ou utilizar correções *ad hoc* de variância — desperdiçam informação ou introduzem viés. O modelo multinível, por sua vez, modela explicitamente a dependência, preserva toda a informação disponível e permite particionar a variância em componentes interpretáveis.

---

## 7. Modelo multinível de três níveis e REML como estimador

### 7.1 Estrutura hierárquica do modelo

O modelo adotado nesta meta-análise organiza os dados em três níveis hierárquicos:

- **Nível 1 — variância amostral:** erro de estimação dentro de cada formulação (σ²ᵢⱼ, conhecida a partir da ACV reportada).
- **Nível 2 — variância entre formulações dentro do mesmo estudo:** capturada por τ²₂, reflete diferenças de traço, idade do concreto, classe de fck e cura entre formulações de um mesmo grupo de pesquisa.
- **Nível 3 — variância entre estudos:** capturada por τ²₁, reflete diferenças de laboratório, contexto geográfico, banco de inventário e premissas de fronteira.

Formalmente, o tamanho de efeito da j-ésima formulação no i-ésimo estudo é modelado como:

$$y_{ij} = \mu + u_i + v_{ij} + \varepsilon_{ij}$$

onde μ é o efeito médio global, $u_i \sim \mathcal{N}(0, \tau^2_1)$ é o efeito aleatório do estudo, $v_{ij} \sim \mathcal{N}(0, \tau^2_2)$ é o efeito aleatório da formulação dentro do estudo, e $\varepsilon_{ij} \sim \mathcal{N}(0, \sigma^2_{ij})$ é o erro amostral.

### 7.2 Implementação em R

A meta-análise será conduzida no R com o pacote `metafor` (VIECHTBAUER, 2010), por meio da função `rma.mv()`, que admite múltiplos fatores aleatórios aninhados. O comando central é:

```r
rma.mv(yi, vi,
       random = ~ 1 | Estudo/ID_observacao,
       data   = banco_metanalise,
       method = "REML")
```

A notação `~ 1 | Estudo/ID_observacao` declara o aninhamento das observações dentro dos estudos, instruindo o `metafor` a estimar simultaneamente τ²₁ e τ²₂. Esse desenho corresponde diretamente ao tutorial passo a passo de Assink & Wibbelink (2016) — referência prática adotada como guia de execução.

### 7.3 Por que REML, e não DerSimonian-Laird?

O estimador adotado para os componentes de variância é o **REML (Restricted Maximum Likelihood)**, por três razões:

1. **Restrição técnica do `rma.mv`:** a função multinível do `metafor` **não admite o estimador DerSimonian-Laird**. DL é um método dos momentos desenvolvido para o modelo univariado, e não generaliza naturalmente para múltiplos componentes de variância. Forçar o uso de DL nesta meta-análise implicaria abandonar o modelo multinível — voltando ao problema de dependência intra-estudo descrito na seção 6.

2. **Padrão recomendado pela literatura metodológica:** REML é o estimador padrão recomendado por Viechtbauer (2010) para meta-análises multinível e é o estimador adotado nos tutoriais canônicos de modelos de três níveis (KONSTANTOPOULOS, 2011; ASSINK; WIBBELINK, 2016). Em comparação com o método dos momentos, o REML produz estimativas de τ² menos enviesadas em amostras finitas e é mais robusto a desbalanceamento entre clusters — característica relevante dado o forte desbalanceamento do banco (CORDOBA contribui com 18 observações; outros estudos, com apenas uma).

3. **Equivalência conceitual:** REML é uma generalização natural da lógica de DL para a estrutura multinível. Ambos buscam estimar a variância dos efeitos verdadeiros descontando o efeito da variância amostral conhecida; REML faz isso via máxima verossimilhança restrita, o que é matematicamente preferível quando há mais de um componente de variância a estimar.

### 7.4 Análises de sensibilidade

Para verificar a estabilidade dos resultados frente à dependência intra-estudo, será conduzida análise de sensibilidade do tipo **leave-one-out por cluster**, com remoção sucessiva dos quatro maiores estudos (CORDOBA, BHAGAT, SANCHEZ-PANTOJA, DYNAN). Espera-se que o efeito combinado μ permaneça dentro do IC 95% da estimativa principal em todos os cenários.

---

## 8. DerSimonian-Laird como referência histórica e didática

Embora **REML seja o estimador efetivamente utilizado** na meta-análise desta dissertação, o método de **DerSimonian & Laird (1986)** permanece citado neste documento por três motivos didáticos e historiográficos:

1. **Origem do modelo de efeitos aleatórios em meta-análise:** o artigo de 1986 é o marco fundador da meta-análise de efeitos aleatórios em ciências da saúde e, por extensão, em meta-análises ambientais. Ignorá-lo desconectaria a presente dissertação da tradição metodológica em que se inscreve.

2. **Base do modelo univariado:** caso a meta-análise viesse a ser conduzida ignorando a estrutura intra-estudo (decisão D3), o estimador de DL seria o padrão de partida. Compreender DL é, portanto, pré-requisito para compreender por que REML é necessário.

3. **Diálogo com a literatura aplicada:** muitas meta-análises de ACV publicadas até 2024 utilizam DL com agregação prévia por estudo. Citá-lo permite que o leitor compare os resultados desta dissertação com a literatura prévia em termos metodologicamente equivalentes.

**Em síntese:** DL é o ancestral conceitual, REML é o estimador operacional. A dissertação reporta a transição explicitamente em vez de omitir uma das duas referências.

---

## 9. Possibilidade de extensão: meta-regressão

Caso a heterogeneidade entre estudos seja alta (I² > 75% no nível 3, ou τ²₁ elevado em termos absolutos), poderá ser conduzida uma **meta-regressão multinível** com variáveis moderadoras — como fronteira do sistema, teor de cimento, classe nominal de fck ou país de origem do estudo — para investigar quais fatores explicam as diferenças entre os resultados. Esse procedimento, ainda implementado via `rma.mv()` com adição do argumento `mods = ~ ...`, corresponde ao **modelo multinível de efeitos mistos** e permite decompor a heterogeneidade em componentes explicados e não explicados em cada nível da hierarquia.

---

## 10. Referências

- ASSINK, M.; WIBBELINK, C. J. M. Fitting three-level meta-analytic models in R: A step-by-step tutorial. **The Quantitative Methods for Psychology**, v. 12, n. 3, p. 154–174, 2016. DOI: 10.20982/tqmp.12.3.p154.
- CHEUNG, M. W.-L. Modeling dependent effect sizes with three-level meta-analyses: A structural equation modeling approach. **Psychological Methods**, v. 19, n. 2, p. 211–229, 2014. DOI: 10.1037/a0032968.
- DERSIMONIAN, R.; LAIRD, N. Meta-analysis in clinical trials. **Controlled Clinical Trials**, v. 7, n. 3, p. 177–188, 1986.
- HIGGINS, J. P. T. et al. Measuring inconsistency in meta-analyses. **BMJ**, v. 327, p. 557–560, 2003.
- KONSTANTOPOULOS, S. Fixed effects and variance components estimation in three-level meta-analysis. **Research Synthesis Methods**, v. 2, n. 1, p. 61–76, 2011. DOI: 10.1002/jrsm.35.
- MARINKOVIĆ, S. et al. Environmental assessment of recycled aggregate concrete structures. **Journal of Cleaner Production**, 2023.
- PACHECO, J.; DE BRITO, J.; LAMPERTI TORNAGHI, M. Life-cycle assessment of recycled aggregate concrete. **Construction and Building Materials**, 2023.
- PAGE, M. J. et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. **BMJ**, v. 372, p. n71, 2021.
- VIECHTBAUER, W. Conducting meta-analyses in R with the metafor package. **Journal of Statistical Software**, v. 36, n. 3, p. 1–48, 2010. DOI: 10.18637/jss.v036.i03.
