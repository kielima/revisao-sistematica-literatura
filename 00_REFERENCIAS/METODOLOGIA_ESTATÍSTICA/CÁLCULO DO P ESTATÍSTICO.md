---



titulo: 
descricao: 
status: 
tags:
  - academico-e-pesquisa
  - engenharia-e-construcao
  - tecnologia-da-informacao
ultima_atualizacao: 2025-05-08
---


# CÁLCULO DO P ESTATÍSTICO

Status: Não iniciada
Última edição: 26 de março de 2025 16:13

# INDICE

# DADOS NECESSÁRIOS

Na tabela, o **"n"** representa o **tamanho da amostra** de cada grupo. Ou seja:

- **n = número de participantes ou observações** em cada grupo analisado.
- A **variância** ($s^2$) é o **quadrado do desvio padrão (SD)**. Ela mede a **dispersão** dos dados em torno da média.

| Grupo | Média | Desvio Padrão (SD) | n | Variância ($SD^2$) |
| --- | --- | --- | --- | --- |
| Tratamento | 120 | 10 | **30** | 100 |
| Controle | 130 | 12 | **30** | 144 |

| Grupo | Média | Desvio Padrão (SD) | n | Variância ($SD^2$) |
| --- | --- | --- | --- | --- |
| CC (Convencional) | 120 | 10 | **30** | 100 |
| UHPC | 130 | 12 | **30** | 144 |
| GPC (geopolimero) |  |  |  |  |

Nesse caso:

- O grupo **Tratamento** tem 30 pessoas.
- O grupo **Controle** também tem 30 pessoas.

Esse valor é essencial para o cálculo do **erro padrão**, **teste t** e **p-valor**, porque quanto maior o tamanho da amostra, **menor a incerteza** e **mais preciso o resultado**.

## **HIPÓTESES**

A **hipótese nula** é uma **afirmação inicial** que fazemos em um teste estatístico, assumindo que **não há efeito, diferença ou relação** entre os grupos ou variáveis que estamos analisando.

$$
H_0: \mu_1 = \mu_2 \\H_1: \mu_1 \ne \mu_2
$$

# PASSO A PASSO

## 1. **Calcular o erro padrão da diferença de médias**

$$
EP = \sqrt{ \frac{SD_1^2}{n_1} + \frac{SD_2^2}{n_2} } = \sqrt{ \frac{10^2}{30} + \frac{12^2}{30} } = \sqrt{ 3{,}33 + 4{,}8 } = \sqrt{8{,}13} \approx 2{,}85
$$

## 3. **Calcular o valor do teste t**

O **valor de teste t** (ou simplesmente **t**) é uma **estatística calculada para comparar médias** em um teste t (como o teste t de Student). Ele mede **quantos erros padrões** a diferença observada entre dois grupos está **afastada da hipótese nula**. O valor de t mostra **quão "surpreendente" é a diferença observada** entre dois grupos, assumindo que **não existe diferença real (H₀: média₁ = média₂)**.

$$
t = \frac{ \bar{x}_1 - \bar{x}_2 }{EP} = \frac{120 - 130}{2{,}85} \approx -3{,}51
$$

## 4. **Obter o valor-p com base na distribuição t** (*two-tailed*)

Bicaudal ( do inglês *two-tailed*) significa que estamos testando **para os dois lados** da distribuição. Queremos saber **se as médias são diferentes**, **sem saber previamente** se uma é maior ou menor que a outra.

Então olhamos tanto:

- Para o caso de a média do grupo 1 ser maior que a do 2
- Quanto para o contrário

Por isso, o p-valor final é:

$$
p = 2 \times P(Z > |t|)
$$

- $p$ = p-valor, é a probabilidade de observar um valor tão extremo quanto o seu resultado (ou mais), assumindo que a hipótese nula ( $H_0$ ) seja verdadeira.
    - Se **p < 0,05** → rejeita-se a hipótese nula (evidência significativa).
    - Se **p ≥ 0,05** → não há evidência suficiente para rejeitar a hipótese nula.
- $P$ = função de probabilidade, mede a **área sob a curva da distribuição normal ou t** correspondente à probabilidade de obter um valor **mais extremo** que o valor do teste.
- $Z$ = Representa a **variável aleatória padronizada** da **distribuição normal padrão** (média 0, desvio 1).
    - Em testes t com amostras grandes, usamos a normal padrão para calcular o p-valor.
    - Em amostras pequenas, **usa-se a distribuição t de Student**, mas a ideia é a mesma.
- $t$ = valor do teste

O valor $P(Z > |t|)$ não é calculado diretamente com uma fórmula simples, mas encontrado usando uma **tabela da distribuição normal padrão** ou uma **calculadora estatística/software**. Essas tabelas são chamadas de **"Tabela Z"**. Elas mostram a área **à esquerda** do valor Z. Como queremos a área à direita, precisamos **subtrair da área total (1).**

Procuramos o valor Z=3,51Z = 3,51Z=3,51 na tabela (área à esquerda):

| Z | 0,00 | 0,01 | ... | 0,50 | 0,51 |
| --- | --- | --- | --- | --- | --- |
| 3,4 | 0,9997 | 0,9997 | ... | ... | ... |
| **3,5** | 0,9998 | 0,9998 | ... | 0,9998 | **0,9998** |

Para $Z = 3{,}51$, essa tabela indicaria algo próximo de **0,9998** (área à esquerda).

Portanto, a área à direita é:

$$
P(Z > 3{,}51) = 1 - 0{,}9998 = 0{,}0002
$$

**No Excel:**

```
=1 - DIST.NORMP(3,51; 0; 1; VERDADEIRO)
```

Resultado exato ≈ **0,000224**

**No Python:**

```python
from scipy.stats import norm
1 - norm.cdf(3.51)
```

Resultado exato ≈ **0,000224**

**No R:**

```
R

1 - pnorm(3.51)
```

Resultado exato ≈ **0,000224**

No nosso exemplo:

$$
t = -3{,}51 \Rightarrow |t| = 3{,}51 \Rightarrow p \approx 0{,}0009
$$

## 5. Calcular os graus de liberdade

**gl** significa **graus de liberdade**, e é um valor usado para determinar qual distribuição t (ou outra distribuição estatística) devemos usar para calcular o **p-valor**.

Em testes t, os graus de liberdade determinam o "formato" da curva da distribuição. Quanto maior o **gl**, mais parecida com a normal padrão ela fica.

1. Se as **variâncias** são iguais (teste t padrão para duas amostras com variância homogênea):
    
    $$
    gl = n_1 + n_2 - 2
    $$
    
    $$
    gl = 30 + 30 - 2 = 58
    $$
    
2. Se as **variâncias** são diferentes ou os tamanhos dos grupos forem **desiguais** (teste t de Welch):
    
    $$
    gl = \frac{\left( \frac{s_1^2}{n_1} + \frac{s_2^2}{n_2} \right)^2}{\frac{\left( \frac{s_1^2}{n_1} \right)^2}{n_1 - 1} + \frac{\left( \frac{s_2^2}{n_2} \right)^2}{n_2 - 1}}
    $$
    

| Aspecto | t padrão (Student) | t de Welch |
| --- | --- | --- |
| Supõe variâncias iguais? | ✅ Sim | ❌ Não |
| Fórmula de gl | gl=n1+n2−2gl = n_1 + n_2 - 2gl=n1+n2−2 | Fórmula de Welch (complexa) |
| Robusto para variâncias diferentes? | ❌ Não | ✅ Sim |
| Uso mais seguro? | Quando SDs e ns são parecidos | Sempre que há dúvida |

## **6. Como usar os graus de liberdade (gl) na tabela tabela t de Student: passo a passo**

Vamos usar nosso exemplo com clareza:

- **t calculado**: t=−3,51t = -3,51t=−3,51
- **gl calculado (Welch)**: aproximadamente 565656

### Passo 1: **Identifique seu valor de gl na tabela**

- **Procure na coluna (ou linha inicial)** o valor dos graus de liberdade mais próximo ao seu (56 no nosso exemplo).
- Se não houver exatamente o valor 56, pegue o valor mais próximo que for menor, por segurança.

Exemplo (simplificado):

| gl | 0,10 | 0,05 | 0,025 | 0,01 | 0,005 |
| --- | --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... | ... |
| 50 | 1,676 | 2,009 | 2,403 | 2,678 | 2,937 |
| **56** (aprox.) | 1,673 | 2,003 | 2,396 | 2,670 | 2,920 |
| 60 | 1,671 | 2,000 | 2,390 | 2,660 | 2,915 |
| ... | ... | ... | ... | ... | ... |

---

### Importar p-value direto no Python

```python
from scipy.stats import t

# t = -3.51, gl = 56, teste bicaudal (two-tailed)
t_value = -3.51
gl = 56
p_valor = 2 * t.sf(abs(t_value), gl)

print(p_valor)
```

### Passo 2: **Compare o valor t calculado com os valores críticos da tabela**

- Como seu teste é **bicaudal** (quer saber diferenças em qualquer direção), você primeiro **ignora o sinal negativo** e considera só o valor absoluto: ∣t∣=3,51|t|=3,51∣t∣=3,51.
- Agora, compare esse valor com os valores da linha dos seus graus de liberdade (56):

Por exemplo, veja os valores críticos (gl=56):

- para α=0,05 \alpha = 0,05 α=0,05 (nível de confiança 95%): valor crítico = **2,003**
- para α=0,01 \alpha = 0,01 α=0,01 (nível de confiança 99%): valor crítico = **2,670**
- para α=0,005 \alpha = 0,005 α=0,005 (nível de confiança 99,5%): valor crítico = **2,920**

Você encontrou um valor de ∣t∣=3,51|t| = 3,51∣t∣=3,51, que é **maior** que todos esses valores críticos.

### Passo 3: **Interprete o resultado**

Como ∣t∣=3,51|t|=3,51∣t∣=3,51 supera até o valor crítico mais alto mostrado (2,920), você conclui que o seu p-valor é **menor que 0,005**. Isso significa que sua diferença é estatisticamente significativa no nível mais rigoroso (mais de 99,5% de confiança).

> **Conclusão**: Você **rejeita a hipótese nula** com forte evidência estatística.
> 

# REFERÊNCIAS

PAGE, M. J. *et al.* PRISMA 2020 explanation and elaboration: updated guidance and exemplars for reporting systematic reviews. **BMJ**, v. 372, p. n160, 2021.