# Instrução dos lotes da Etapa 2 — análise quantitativa do PDF

> Versão de 2026-08-24, já com as duas decisões da Kiê fechadas e testadas.
> **Ler isto todo antes de tocar em nada.** O teu lote é indicado na mensagem que te lançou.

## O que a Etapa 2 decide

Dois critérios, aplicados **em cascata** e **só sobre o corpo do PDF** — o título e o resumo
são para desconsiderar, já foram usados na Etapa 1.

1. **`E2_resistencia`** — o artigo declara resistência **convertível para MPa** (força por
   área) e **alguma** mistura atinge **20 MPa**? Se não declara, ou se nenhuma atinge 20,
   **Rejeitado**.
   📌 **«Atinge 20» inclui exactamente 20.** A regra da Kiê é «abaixo de 20 MPa, exclui», e 20
   não está abaixo de 20. Uma classe **C20**/25 declarada **entra**.
   📌 **A classe de projecto conta e não é fonte externa.** Quando a classe (C30/37, f'c 35 MPa)
   não é medida nem citada de um estudo, mas é a especificação de projecto do edifício ou vem
   dos desenhos originais, **conta como classe declarada** — a regra da Kiê diz «classe
   declarada conta», sem exigir ensaio. Não há estudo primário para citar, por isso
   `fonte_externa` fica **vazia**; regista `classe de projecto` em `fonte_resistencia`.
2. **`E2_co2`** — o artigo declara **valor de emissão** de CO₂? Se não, **Rejeitado**.
   Só se avalia se o artigo passou no critério 1.

Estados possíveis: `Aceito` · `Rejeitado` · `DUVIDA` · `nao avaliado`
(este último **só** para o `E2_co2` de um artigo já **rejeitado** na resistência).

📌 **Com `E2_resistencia = DUVIDA`, avalia o CO₂ na mesma.** A cascata só poupa trabalho
quando a rejeição é certa. Avaliar o CO₂ de uma dúvida custa pouco e mostra quais das dúvidas
mudam mesmo o desfecho — no lote 1, duas das três dúvidas eram irrelevantes porque o CO₂ já
rejeitava de qualquer maneira.

## Passo a passo, por artigo

### 1. Obter o ficheiro — sem procurar no Drive

O `DRIVE_FILEID_MAP.csv` já tem o `fileId` de cada nome de ficheiro. **Nunca uses
`search_files` por título** — falha em nomes acentuados e gasta uma chamada por artigo.

```bash
grep -F '"<nome exacto do ficheiro>"' /home/user/revisao-sistematica-literatura/DRIVE_FILEID_MAP.csv
```

⚠️⚠️ **Olha primeiro para o `fileSize` do mapa — a terceira coluna, em bytes.** O
`download_file_content` tem um tecto de tamanho, medido a 2026-08-24:

| Tamanho | O que acontece | O que fazes |
|---|---|---|
| **até ~5 MB** | descarrega bem | `download_file_content` → descodificas → PDF local, **com figuras** |
| **acima de ~5 MB** | falha (ver abaixo) | **`mcp__Toolkit__googledrive_download_file`** → PDF local, **também com figuras** |

⭐⭐ **Para os ficheiros grandes usa o descarregador do Toolkit — resolve o problema por
inteiro** (testado a 2026-08-24 num ficheiro de 6,4 MB que o outro caminho recusava):

```
mcp__Toolkit__googledrive_download_file  com  file_id = <o mesmo fileId>
```

⚠️ **Um de cada vez.** A chamada em lote, com `file_ids`, rebenta com um **Cloudflare 520**.
Individualmente funciona sempre — testado até 17,7 MB, muito acima do tecto do outro caminho.

A resposta **não traz o ficheiro**: traz um **URL de descarga directa**, no campo
`downloaded_file_content.s3url`. Puxa-o com `curl` e ficas com o PDF em disco:

```bash
curl -sS -o r<linha>.pdf --max-time 120 "<s3url>"
head -c 5 r<linha>.pdf     # tem de dizer %PDF-
```

Isto é **melhor** que o caminho normal: o conteúdo nunca passa pelo teu contexto, nem sequer
em base64 — só o URL. E como ficas com um PDF verdadeiro, **o passo 5 continua disponível**,
figuras incluídas. O URL expira ao fim de uma hora; puxa-o logo.

📌 **Não uses `read_file_content` para contornar o tamanho.** Dá só texto, mata o passo 5, e é
imprevisível no contexto — já devolveu 10 mil tokens inline de um artigo curto. Só o usa se o
descarregador do Toolkit também falhar.

🚨 **A mensagem de erro do `download_file_content` mente.** Entre ~5 e 10 MB devolve
**`MCP server "Google_Drive" session expired`** — e a sessão **está viva**: verificado com
`get_file_metadata` no mesmo instante e com outra descarga a funcionar a seguir. Acima de
10 MB o erro já é honesto (`File too large`). Em qualquer dos casos **não repitas a chamada**:
é determinístico e é de tamanho. Vai directo ao descarregador do Toolkit.

São **369 dos 1.591** ficheiros acima de 5,2 MB — 23% do universo. Antes de se descobrir o
contorno, um lote perdeu 27% dos artigos por isto.

Para os ficheiros até ~5 MB, chama `mcp__Google_Drive__download_file_content` com o `fileId`.
A resposta excede o limite de tokens e **é gravada num ficheiro** — o erro diz-te o caminho.
Isso é o que queremos: o base64 nunca entra no teu contexto. Descodifica-o para um PDF local:

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

⭐ **Resistência medida por terceiros: ACEITA** (decisão da Kiê, 2026-08-24). Se o artigo
reporta valores de resistência que não mediu — uma revisão que compila estudos primários, um
artigo que assume o inventário de outro, uma classe atribuída por semelhança — **conta como
declarar resistência**. O artigo entra.

Em contrapartida, **tens de registar de onde vêm os valores**, na coluna `fonte_externa`: a
citação ou o DOI do estudo de origem, tal como o artigo o identifica. Esses estudos vão entrar
no fluxograma PRISMA pelo **ramo da busca por citação**, para o mesmo ensaio não ser contado
duas vezes. Se o artigo não identificar a fonte, escreve `nao identificada` — isso também é
informação.

📌 E põe na nota que a linha **não tem dados próprios**, para a metanálise saber que não pode
extrair dali.

### 5. Se o texto não der a resistência — **renderiza a figura**

⭐ **Decisão da Kiê, 2026-08-24: valor só em figura extrai-se da figura, não se rejeita.**
Zero ocorrências de «MPa» **nunca** é motivo para rejeitar sozinho.

**Antes de renderizar seja o que for, lê as legendas.** É muito mais barato e resolve a
maioria dos casos: se as doze legendas de um artigo são todas fluxogramas, GWP por fase e
energia incorporada, está provado que não há figura de resistência para ler, e renderizar
seria deitar contexto fora.

```python
legendas = re.findall(r'(?:Fig(?:ure|\.)?|Tab(?:le|\.)?|Quadro|Tabela)\s*\d+[a-z]?[.:\s-]{1,3}[^.]{0,160}', full)
```

Só se alguma legenda prometer resistência é que renderizas essa página:

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

⚠️ **Não uses uma lista curta.** Uma lista de meia dúzia de padrões deu **zero** ocorrências
num artigo que tinha **52** relevantes. Usa o padrão completo, o mesmo que o projecto já usa:

```
lca|life.cycle.assess|carbon.footprint|embodied.carbon|gwp|global.warming.potential|
co2.eq|co2eq|kgco2|greenhouse.gas|ghg|carbon.emission|climate.change|co2|
embodied.emission|carbon.intensi|low.carbon
```

Este padrão pode correr sem distinguir maiúsculas — ao contrário do `MPa`, nenhum destes
termos é substring de palavras comuns.

⭐ **Regra da Kiê, 2026-08-24 — todas as unidades servem, incluindo o total da obra desde que
haja também um valor normalizado.** «Se tem os dois pode aceitar; rejeitar só se o CO₂ vier
apenas por edifício e não tiver mais nada além disso.» Aceites: kg CO₂/m³, /m², /t, /kg,
/m de túnel, por elemento, por viga. Rejeita quando **só** existe o total de um edifício
inteiro e nenhuma forma normalizada.

📌 **«Edifício» lê-se como «obra inteira».** A razão da exclusão é não haver como normalizar,
não a palavra *edifício*. Um total de uma **ponte**, de um viaduto ou de uma intervenção de
reforço, sem nenhuma forma por metro, por m² ou por elemento, cai na mesma regra e rejeita.
Caso medido: 151,3 t CO₂eq para o reforço de uma ponte de 34 m de vão, sem valor normalizado.

⚠️ **Distingue isto de «o total existe mas há também um normalizado»** — nesse caso aceita,
que é a regra da Kiê. O que rejeita é a ausência de qualquer forma normalizada, não a
presença do total.

📌 **Balanço líquido negativo aceita, mas com aviso.** Um valor como −567,8 kg CO₂-eq por
unidade funcional, em que o sequestro excede a emissão, **é** um valor de emissão declarado e
passa o critério. Mas põe `balanco liquido negativo` em `aviso_metanalise`: uma metanálise de
emissões não pode somá-lo com os positivos sem tratar o sinal. Já apareceu duas vezes em cinco
lotes, não é excepção rara.

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
n_misturas_abaixo_20,valor_co2,unidade_co2,fonte_resistencia,fonte_co2,
fonte_externa,aviso_metanalise,confianca,nota
```

- `fonte_resistencia` e `fonte_co2`: **duas colunas separadas**, porque os dois valores vêm
  muitas vezes de sítios diferentes — no lote 3 houve um artigo com a resistência em tabela e o
  CO₂ em figura renderizada. Valores: `texto` · `tabela` · `classe declarada` · `classe de
  projecto` · **`figura (rotulo extraido)`** quando o valor vive numa figura mas o extractor
  apanhou o rótulo · **`figura (renderizada)`** quando tiveste mesmo de olhar para a imagem.
  ⚠️ Não confundas as duas últimas: a primeira é barata e de confiança alta, a segunda é uma
  leitura contra o eixo, com confiança média.
- `aviso_metanalise`: **vazio** na esmagadora maioria. Preenche quando o valor existe e o
  critério passa, mas a metanálise não o pode usar sem cuidado. Casos já vistos:
  `sem dados proprios` · `captacao e nao emissao` (o número é *uptake* por carbonatação) ·
  `balanco liquido negativo` · `escala suspeita` · `normalizado pela resistencia` ·
  `sem amostras proprias`. Descreve em texto livre se for caso novo, e explica na nota.
- `n_misturas_abaixo_20`: o número quando as misturas são contáveis, `todas` quando nenhuma
  atinge 20, e **vazio** quando o artigo não declara resistência nenhuma. Quando o intervalo
  declarado prova que há pelo menos N mas o texto só transcreve algumas, escreve **`>=N`** e
  explica na nota — não arredondes para o número que conseguiste ver.
- `fonte_externa`: **vazio** quando os valores são do próprio artigo. Quando não são, a
  citação ou o DOI do estudo de origem, ou `nao identificada`. Separa várias com `;`.
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
