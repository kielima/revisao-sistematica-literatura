# Instrução dos lotes da Etapa 2 — análise quantitativa do PDF

> Versão de 2026-08-24, já com as duas decisões da Kiê fechadas e testadas.
> **Ler isto todo antes de tocar em nada.** O teu lote é indicado na mensagem que te lançou.

## O que a Etapa 2 decide

Dois critérios, aplicados **em cascata** e **só sobre o corpo do PDF** — o título e o resumo
são para desconsiderar, já foram usados na Etapa 1.

1. **`E2_resistencia`** — o artigo declara resistência **convertível para MPa** (força por
   área) e **alguma** mistura atinge **20 MPa**? Se não declara, ou se nenhuma atinge 20,
   **Rejeitado**.
2. **`E2_co2`** — o artigo declara **valor de emissão** de CO₂? Se não, **Rejeitado**.
   Só se avalia se o artigo passou no critério 1.

Estados possíveis: `Aceito` · `Rejeitado` · `DUVIDA` · `nao avaliado`
(este último **só** para o `E2_co2` de um artigo já rejeitado na resistência).

## Passo a passo, por artigo

### 1. Obter o ficheiro — sem procurar no Drive

O `DRIVE_FILEID_MAP.csv` já tem o `fileId` de cada nome de ficheiro. **Nunca uses
`search_files` por título** — falha em nomes acentuados e gasta uma chamada por artigo.

```bash
grep -F '"<nome exacto do ficheiro>"' /home/user/revisao-sistematica-literatura/DRIVE_FILEID_MAP.csv
```

Depois chama `mcp__Google_Drive__download_file_content` com esse `fileId`. A resposta excede o
limite de tokens e **é gravada num ficheiro** — o erro diz-te o caminho. Isso é o que queremos:
o base64 nunca entra no teu contexto. Descodifica-o para um PDF local:

```python
import json, base64
d = json.load(open('<caminho que o erro indicou>'))
open('r<linha>.pdf','wb').write(base64.b64decode(d['content']))
```

⚠️ **Dá aos ficheiros de trabalho um nome que inclua o número da linha** (`r3752.pdf`,
`r3752.txt`). O scratchpad é partilhado entre lotes e já houve contaminação por reutilização.

### 2. Confirmar que o ficheiro é do artigo certo

Extrai a p. 1 e confirma que o **DOI do banco** ou o **título** lá estão. Se não estiverem,
não avalies: regista `DUVIDA` com a nota a dizer o que o ficheiro é. Não é o teu trabalho
resolver a atribuição.

### 3. Procurar a resistência no texto

```python
import pymupdf, re
d = pymupdf.open('r<linha>.pdf')
full = re.sub(r'\s+', ' ', ' '.join(d[i].get_text() for i in range(d.page_count)))
```

⚠️⚠️ **Procura `MPa` com as maiúsculas respeitadas.** Nunca uses `re.I` numa sigla de três
letras: `compa` de *comparison* e *compared* dá falsos positivos, e foi medido — 3 falsos
numa única página do RO 2024. Procura as variantes explicitamente:

```python
re.findall(r'MPa|Mpa|mPa|N/mm2|N/mm²|\bC\d{2}/\d{2}\b|\bpsi\b|\bksi\b', full)
```

⚠️ **Normaliza `\s+` para espaço antes de procurar.** O texto extraído tem quebras de linha a
meio das frases e o contexto do valor cai sempre na linha seguinte; sem normalizar perdes-o.

### 4. Julgar o que encontraste — o regex não decide

**Ter «MPa» não chega.** Casos medidos em que a ocorrência não é resistência do material:
- **pressão** de transporte de CO₂ supercrítico (10 MPa) — foi a única ocorrência em 131 mil
  caracteres do ZAJAC 2022, que é um artigo sem resistência nenhuma;
- módulo de elasticidade (GPa), tensão de aderência, pressão de compactação;
- valores citados da literatura em introdução, que **contam** se o artigo os assume como a
  classe do seu material, mas **não** se são só contexto de outro estudo.

Lê o contexto de cada ocorrência antes de decidir.

### 5. Se o texto não der a resistência — **renderiza a figura**

⭐ **Decisão da Kiê, 2026-08-24: valor só em figura extrai-se da figura, não se rejeita.**
Zero ocorrências de «MPa» **nunca** é motivo para rejeitar sozinho.

```python
for i in range(d.page_count):
    if d[i].get_images(): print(i+1, len(d[i].get_images()))
d[<pagina>].get_pixmap(dpi=200).save('r<linha>_p<n>.png')
```

Depois **abre a imagem com a ferramenta Read e olha para ela**. Procura o eixo rotulado em
MPa e lê as barras contra as marcas. Foi assim que o RO 2024 (linha 3752) se resolveu:
44,5 MPa e 37,8 MPa lidos de um gráfico de barras, num artigo com zero «MPa» no texto.

Regista na nota que o valor veio de figura e qual, e põe `confianca=media`.

Se depois de olhar continuares sem conseguir ler um valor, aí sim: `DUVIDA`, com a nota a
dizer que figura é e porque não se lê.

### 6. O CO₂

Procura `kg CO2`, `kgCO2`, `CO2-eq`, `CO2 eq`, `GWP`, `tCO2`, `kt CO2`, `global warming`.

⭐ **Regra da Kiê, 2026-08-24 — todas as unidades servem, incluindo o total da obra desde que
haja também um valor normalizado.** «Se tem os dois pode aceitar; rejeitar só se o CO₂ vier
apenas por edifício e não tiver mais nada além disso.» Aceites: kg CO₂/m³, /m², /t, /kg,
/m de túnel, por elemento, por viga. Rejeita quando **só** existe o total de um edifício
inteiro e nenhuma forma normalizada.

📌 **Percentagem de redução NÃO é valor de emissão.** Medido: o SUMMA 2023 (linha 2858) faz
ACV com dez indicadores e a Fig. 5 é um radar de **percentagens**, eixo de 0% a 80%, sem um
único valor absoluto. Rejeitado. Se o artigo só diz «reduziu 30%», é `Rejeitado`.

Se suspeitares que o valor absoluto está numa figura, **renderiza e olha** — o mesmo
procedimento do passo 5. O teste corre nos dois sentidos: no RO salvou o artigo, no SUMMA
condenou-o.

### 7. Outras armadilhas já medidas

- **O corte da secção de referências quase nunca funciona** — o cabeçalho «References»
  raramente aparece isolado numa linha (acertou em 1 de 10 ficheiros). Conta com títulos de
  referências a poluir a contagem e confirma sempre onde no documento está a ocorrência.
- **Tabelas sobrevivem à extracção** em ~10 de 12 ficheiros — achatadas numa linha, mas com
  valores e cabeçalhos pela ordem certa. Procura-as antes de assumir que precisas da figura.

## O que escreves

**Só** o ficheiro `lotes_etapa2/LOTE_<NN>_RESULTADO.csv`, com `QUOTE_ALL`, **sem acentos** nos
dados (a regra do `clean_str` do projecto), com estas colunas:

```
linha,pdf,E2_resistencia,E2_co2,valor_resistencia_max,unidade_resistencia,
n_misturas_abaixo_20,valor_co2,unidade_co2,fonte_do_valor,confianca,nota
```

- `fonte_do_valor`: `texto`, `tabela`, `figura` ou `classe declarada`.
- `confianca`: `alta`, `media`, `baixa`.
- `nota`: onde no documento está cada valor, e o raciocínio nos casos não triviais. É isto que
  permite auditar-te sem reabrir o PDF — escreve-a a pensar em quem vai conferir.

## O que NÃO fazes

- **Não escreves no `articles_final.xlsx`.** Podes lê-lo, nada mais.
- **Não fazes commits.**
- **Não decides casos de fronteira sozinho** — se uma regra não cobre o que encontraste,
  regista `DUVIDA` e explica na nota. A calibração é feita entre lotes, não dentro deles.
- **Não reutilizas nenhum ficheiro do scratchpad** sem o reescreveres primeiro.

## O que reportas no fim

Além do CSV: quantos aceites e rejeitados, quantos precisaram de figura, quanto tempo/chamadas
custou, e **qualquer coisa que te tenha feito hesitar**. Se uma regra te pareceu ambígua ou
contradita pelos dados, diz — é assim que os critérios se afinam.
