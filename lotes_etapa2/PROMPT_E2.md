# Instrução dos lotes da Etapa 2 — análise quantitativa do PDF

> Versão de 2026-08-24, já com as duas decisões da Kiê fechadas e testadas.
> **Ler isto todo antes de tocar em nada.** O teu lote é indicado na mensagem que te lançou.

## O que a Etapa 2 decide

Dois critérios, aplicados **em cascata** e **só sobre o corpo do PDF** — o título e o resumo
são para desconsiderar, já foram usados na Etapa 1.

1. **`E2_resistencia`** — o artigo declara resistência **convertível para MPa** (força por
   área) e **alguma** mistura atinge **20 MPa**? Se não declara, ou se nenhuma atinge 20,
   **Rejeitado**.
   📌 **Não é restrito à sigla `MPa`.** O critério diz «convertível para MPa», não «impresso em
   MPa». `N/mm²`, `psi`, `ksi` e **`kgf/cm²`** são força por área e convertem-se — e também
   não é restrito a betão: bambu, madeira e solo estabilizado servem, o que conta é a
   grandeza. Caso medido e verificado: um artigo coreano sem uma única ocorrência de «MPa»,
   cuja designação de betão pronto `25-210-12` é em kgf/cm² — 210 kgf/cm² dá **20,6 MPa**, e o
   próprio artigo confirma ao listar as mesmas entradas como `25-21-12` noutra tabela, com
   valores de impacto idênticos. Converte e regista a unidade original em
   `unidade_resistencia`.
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

📌 O `fileSize` do mapa (terceira coluna, em bytes) continua a valer a pena olhar, para
saberes o que esperar — mas com o caminho do Toolkit o tamanho deixou de ser um problema.

✅ **ESTADO ACTUAL (2026-08-25, reconfirmado): o descarregador do Toolkit está a FUNCIONAR.**
Esteve fora durante algumas horas, com `requires re-authorization (token expired)`, e voltou.
Se voltar a dar esse erro, **é determinístico e não recupera dentro da sessão** — nesse caso vai
directo ao plano C mais abaixo, sem gastar chamadas a tentar, e marca com `FIGURA INACESSIVEL:`
o que ficar por ler.

⭐⭐⭐ **USA SEMPRE O DESCARREGADOR DO TOOLKIT, seja qual for o tamanho.** Era só para os
ficheiros grandes, passou a ser o caminho normal a 2026-08-24, por duas razões: não tem tecto
de tamanho (testado até 17,7 MB) e **não passa por nenhum ficheiro partilhado**.

🚨 **Porque isso importa:** o `download_file_content` grava a resposta num ficheiro comum a
toda a sessão, em `tool-results/`. Os nomes trazem um carimbo em milissegundos e são
distintos, portanto **não há sobreposição de um caminho concreto** — mas com vários lotes a
correr ao mesmo tempo aquela pasta enche-se de descargas de outros lotes, e **basta procurar
«o ficheiro mais recente» em vez de usar o caminho exacto que a chamada devolveu para se
apanhar o PDF de outro artigo**. Foi o que quase aconteceu num lote. Se usares este caminho,
usa **sempre o caminho exacto que a mensagem de erro te deu**, nunca um `ls -t | head -1`.

O caminho do Toolkit não tem este problema: devolve um URL só teu.

```
mcp__Toolkit__googledrive_download_file  com  file_id = <o mesmo fileId>
```

🚨 **O descarregador pode devolver o ficheiro ERRADO para o `file_id` pedido.** Medido no
lote 51: uma chamada por um artigo devolveu com sucesso um PDF de outro autor completamente
diferente, sem erro nenhum reportado. **Confirma sempre título e primeiro autor na p.1 do PDF
que abriste contra o que esperavas do CSV do lote — antes de leres uma linha de conteúdo.** Se
não bater, não uses esse resultado: repete a chamada.

⚠️ **Um de cada vez, e isso inclui não lançar chamadas em paralelo.** A chamada em lote, com
`file_ids`, rebenta com um **Cloudflare 520** — mas três chamadas individuais lançadas ao mesmo
tempo também falham (uma devolveu `session expired` enquanto as outras duas passaram).
Sequencial nunca falhou.
E mesmo individualmente aparece por vezes um **502** transitório — esse **repete-se**, ao fim
de um minuto ou dois, e passa. É o oposto do «session expired», que é determinístico e nunca
vale a pena repetir.
Individualmente funciona sempre — testado até 17,7 MB, muito acima do tecto do outro caminho.

🚨🚨 **Este caminho NÃO TEM TECTO DE TAMANHO, e isso é decisivo.** O que ele devolve é um
**endereço**, não o ficheiro: o tamanho do PDF é irrelevante para a chamada, porque quem o
transporta é o `curl`. Um artigo de 23 MB descarrega-se por aqui tão bem como um de 2 MB.

⚠️ **Não transportes o tecto de ~6 MB para este caminho.** Ele pertence **só** ao Plano C, mais
abaixo. Durante a paragem do descarregador, vários artigos foram fechados com «FIGURA
INACESSÍVEL — ficheiro acima do tecto»; esse veredito só era válido enquanto o Plano C era o
único caminho disponível. **Com o descarregador a funcionar, nenhum ficheiro é inacessível por
ser grande.** Se estiveres a pensar escrever que uma figura não se pôde renderizar por causa do
tamanho, pára e tenta primeiro este caminho.

A resposta **não traz o ficheiro**: traz um **URL de descarga directa**, no campo
`downloaded_file_content.s3url`. Puxa-o com `curl` e ficas com o PDF em disco:

```bash
curl -sS -o r<linha>.pdf --max-time 120 "<s3url>"
head -c 5 r<linha>.pdf     # tem de dizer %PDF-
```

Isto é **melhor** que o caminho normal: o conteúdo nunca passa pelo teu contexto, nem sequer
em base64 — só o URL. E como ficas com um PDF verdadeiro, **o passo 5 continua disponível**,
figuras incluídas. O URL expira ao fim de uma hora; puxa-o logo.

### Plano C — quando o descarregador do Toolkit perde a autorização

Acontece, e é **determinístico**: passa a devolver `requires re-authorization (token expired)` e
**não recupera** (medido: oito tentativas ao longo de meia hora). Não insistas. A partir daí:

| Tamanho | O que usar |
|---|---|
| até ~6 MB | `mcp__Google_Drive__download_file_content` → descodificas → PDF local, **com figuras** |
| acima de ~6 MB | `mcp__Google_Drive__read_file_content` → **só texto**, sem passo 5 |

📌 **O tecto medido com precisão, em dois lotes independentes:** 5,42 · 5,73 · 5,85 · 5,91 MB
passam; 6,74 · 6,78 · 6,83 MB não. O corte é no tamanho
da resposta em base64 (~8 milhões de caracteres), não no ficheiro — por isso vale a pena tentar
qualquer coisa abaixo de ~6 MB em vez de assumir que falha. Num lote, dois artigos só entraram
por causa disto.
📌 E o `read_file_content` **também grava em ficheiro** em vez de despejar no contexto, na
maioria dos casos — é mais barato do que parece.

⚠️ **Com o `read_file_content` não há fronteiras de página, e as colunas de página ficam em
risco.** Recupera-as segmentando pelo **cabeçalho corrido** do editor — e **valida o método**
sempre que tiveres o PDF verdadeiro de outro artigo do mesmo lote para comparar. Quando o
cabeçalho falhar, a incerteza é de ±1 página.

⚠️ **E o extractor perde fólios.** Num artigo faltava o «5» do cabeçalho, o que fundia duas
páginas numa; só se apanhou medindo o deslocamento do valor contra o fólio em falta. **Diz
sempre na nota que a página foi derivada e não lida** — quem auditar precisa de saber a
diferença. E quando tiveres, no mesmo lote, um ficheiro com as duas coisas (PDF verdadeiro e
dump com rodapés), **valida o mapeamento contra ele**: foi assim que se estabeleceu que o
número de rodapé cai **dentro da sua própria página**.

Escreve **`p.N (+/-1)`** quando houver incerteza, e dá **sempre uma âncora
exacta ao lado** (secção, número de tabela, número de figura), que é o que permite conferir.

⭐ **E há aqui um achado que vale ouro para as páginas:** o `read_file_content` insere no
markdown **marcadores de página explícitos, `[**Page N**]()`**. Isso é uma âncora *mais* segura
do que contar `d[i]` com o `pymupdf`, porque vem do próprio extractor. Quando aparecerem, usa-os
e di-lo na nota. Quando não aparecerem, o **cabeçalho corrido** do editor (`Journal of CO2
Utilization 90 (2024) 102986 5`, `Environments 2022, 9, 6 — N of 10`) dá a página impressa de
graça, e também é âncora directa e não interpolação.

📌 Fora deste plano C, **não uses `read_file_content`**: mata o passo 5 e é imprevisível no
contexto — já devolveu 10 mil tokens inline de um artigo curto.

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

⚠️ **Trabalha num subdirectório teu**, `scratchpad/l<NN>/`, e dá aos ficheiros um nome que
inclua o número da linha (`r3752.pdf`). O scratchpad é partilhado entre lotes e já houve
contaminação por reutilização; o prefixo da linha sozinho não chega, porque dois lotes podem
tocar na mesma linha — um lote de recuperação, por exemplo.

### 2. Confirmar que o ficheiro é do artigo certo

Extrai a p. 1 e confirma que o **DOI do banco** ou o **título** lá estão. Se não estiverem,
não avalies: regista `DUVIDA` com a nota a dizer o que o ficheiro é. Não é o teu trabalho
resolver a atribuição.

⚠️ **Ficheiro truncado é outra coisa, e diz-se.** Acontece o ficheiro ser mesmo da obra certa
mas estar incompleto — só as páginas pré-textuais de um livro, sem corpo. Regista `DUVIDA` e
**começa a nota com `FICHEIRO INCOMPLETO:`**, para se distinguir de uma dúvida de critério.
Uma é falta de material, a outra é falta de regra, e resolvem-se por caminhos diferentes.

### 3. Procurar a resistência no texto

```python
import pymupdf, re
d = pymupdf.open('r<linha>.pdf')
full = re.sub(r'\s+', ' ', ' '.join(d[i].get_text() for i in range(d.page_count)))
```

🚨 **Duas formas que o padrão antigo não via, e que teriam rejeitado artigos bons** —
medidas no lote 15, as duas em artigos com **zero** ocorrências de `MPa`:
- **a unidade escrita por extenso**: «the compressive strength … exceeds **20 megapascals**».
  É um aceite, e ainda por cima em cima do limiar;
- **a classe sem o prefixo `C`**: «Cast in Situ **25/30**», que é como a base HBERT nomeia o
  C25/30. `\bC\d{2}/\d{2}\b` exige a letra e passa ao lado.

O padrão acima já as inclui. ⚠️ Mas `\d{2}/\d{2}` sozinho tem um sinal/ruído **péssimo** neste corpus: num lote deu 247
acertos num artigo e 138 noutro, e **nenhum verdadeiro em 15 artigos** — são intervalos de
páginas das referências, anos e rácios. Fica no padrão por causa do «Cast in Situ 25/30», mas
**a contagem bruta de acertos não diz nada**; só o contexto de cada um. Falsos positivos
medidos: espessuras de isolamento (`100/60/30 mm`), anos, intervalos de páginas.
⚠️ E `\bC\s?\d{2}\b` tem o seu: acertou em **`Case C 65.00`**, a altura de um edifício, que
a olho desatento parece uma classe C65. ⚠️ E tanto ele como `\bf'?ck?\b` acertam dentro de
**URLs e DOIs das referências** (`C21.8243`, `10/11/114017`, `17/17-1`) — a mesma família, mas
vinda de links e não de paginação. Antes de avaliar, vale a pena **cortar a lista de
referências** ou, pelo menos, verificar em que página cai cada acerto.

⚠️ **A classe de número único (`C45`, `C30`) é a notação chinesa e é frequente** — o padrão
do Eurocódigo `C30/37` não a apanha. Um artigo com «C45 strength grade» quase passou
despercebido num lote; só apareceu por busca da palavra `grade`, e sem isso teria sido decidido
pelo glulam, que estava exactamente no limiar. Inclui `\bC\d{2}\b` **e confirma sempre o
contexto**, porque sozinho dá falsos positivos (`C25` de compostos químicos).
⚠️ E cuidado com `grade`: num artigo as três ocorrências eram **«Belgrade»**, na filiação dos
coautores. Na mesma família, num artigo bibliométrico **17 das 20 ocorrências de `strength`
eram `total link strength`**, a métrica do VOSviewer, com valores plausíveis como 139 e 456.
E `kg/cm²` tanto pode ser resistência como **unidade de CO₂** — apareceu um artigo com
`13,15 kg/cm²` de emissão.

🚨🚨 **`re.I` sobre `MPa` destrói a contagem — e a magnitude é muito maior do que parece.**
Medido no lote 17: em **10 dos 15 artigos** a busca insensível devolveu entre 13 e 122
acertos que eram **todos** `compa` de *comparison* e *compared*, com **zero** MPa verdadeiros.
⚠️ E o falso positivo dominante nem é esse: é **`impact`** — a palavra mais comum de um corpus
de ACV. Num artigo deu **123** acertos num ficheiro com zero MPa reais.
Dois artigos que davam 122 e 75 acertos não tinham um único MPa. Um lote que confiasse na
contagem tê-los-ia aceitado.

Noutros lotes o mesmo erro deu 463, 128 e 25 falsos positivos. **Nunca corras `re.I` sobre uma
sigla de três letras que é substring de palavras comuns.** Por isso o código abaixo tem dois
padrões separados — a separação não é estilo, é o que impede o erro:

```python
# 🚨 DOIS padroes, e a separacao NAO e opcional (ver aviso a seguir)
SIGLA = r"MPa|Mpa|mPa"                       # SEM re.I. Nunca com re.I.
RESTO = (r"megapascal|N/mm2|N/mm²|newtons?\s+per|kgf/cm|pounds?\s+per\s+square|"
         r"\bC\s?\d{2}\s?/\s?\d{2}\b|\bC\s?\d{2}\b|\b\d{2}\s*/\s*\d{2}\b|"
         r"\bf'?ck?\b|\bpsi\b|\bksi\b|strength\s+(?:grade|class)|grade\s+C?\d{2}")

hits  = re.findall(SIGLA, full)                 # maiusculas respeitadas
hits += re.findall(RESTO, full, re.I)           # aqui re.I e seguro
```

⚠️⚠️ **Notação científica: `0,243` está impresso como `2,43E-01`.** Uma busca literal por um
valor decimal **falha em silêncio** em qualquer artigo ou tese que use notação científica nas
tabelas de avaliação de impacto — e são muitos. Procura sempre também a forma `\d[,.]\d+E[+-]?\d+`
e, quando procurares um valor concreto, tenta as duas formas antes de concluir que não existe.

⚠️⚠️ **Sinais de menos e vírgulas decimais tipográficos.** O menos pode ser **U+2212**
(`−`) e não o hífen ASCII, e o decimal pode ser **vírgula**. A busca literal falha em
silêncio nos dois casos. Normaliza sempre: substitui `−` por `-` e experimenta as duas formas
do decimal antes de concluir que o valor não existe.

⚠️ **E o número pode estar separado da unidade por uma quebra de linha** — «12» numa linha e
«MPa» na seguinte. Mais uma razão para normalizar antes de procurar.

⚠️ **Normaliza `\s+` para espaço antes de procurar.** O texto extraído tem quebras de linha a
meio das frases e o contexto do valor cai sempre na linha seguinte; sem normalizar perdes-o.

### 4. Julgar o que encontraste — o regex não decide

**Ter «MPa» não chega.** Casos medidos em que a ocorrência não é resistência do material:
- **pressão** de transporte de CO₂ supercrítico (10 MPa) — foi a única ocorrência em 131 mil
  caracteres do ZAJAC 2022, que é um artigo sem resistência nenhuma; e pressão de gás de
  carbonatação (1,5 MPa) noutro;
- ⚠️ **a armadilha inversa: `MPa` no denominador de uma métrica.** Um artigo com `GWI/MPa` e
  `CED/MPa` — impacto normalizado pela resistência — enche-se de ocorrências de «MPa» sendo um
  artigo para rejeitar. Deu 12 acertos num caso em que nenhuma mistura chegava a 20. Um
  contador ingénuo sugeriria aceitação;
- ⚠️ **`f.c` no regex acerta no fim de «speci*fic*».** Deu 7 falsos positivos num artigo e 3
  noutro. Para procurar `f'c` ou `fck` usa `\bf.?ck\b` ou `f'c` com o apóstrofo literal —
  nunca `f.c` com ponto de regex;
- **«class» que não é classe de resistência** — num artigo as Classes A–D eram de desempenho
  de sustentabilidade das *empresas*;
- 🚨 **`total link strength` do VOSviewer, nas revisões bibliométricas** — merece destaque
  próprio porque **imita bem um MPa**: os valores vêm na casa das centenas (234, 307, 242) e
  num artigo **as 39 ocorrências de `strength` eram todas isso**. Um contador ingénuo aceita-o;
- módulo de elasticidade (GPa), tensão de aderência, pressão de compactação;
- valores citados da literatura em introdução, que **contam** se o artigo os assume como a
  classe do seu material, mas **não** se são só contexto de outro estudo.

Lê o contexto de cada ocorrência antes de decidir.

⚠️ **Designação comercial com sufixo numérico: `DUVIDA`, não decidas.** Um cimento cubano
«P-35» é, pela norma NC 95, uma classe de 35 MPa — mas se o artigo nunca o disser, aceitá-lo
exige conhecimento que o documento não dá. E o sufixo é ambíguo dentro do próprio artigo:
no mesmo par de designações, `LC3-50` quer dizer **teor de clínquer**, não resistência.

⚠️ **Impacto climático quantificado só em unidade normalizada, sem massa: `DUVIDA`.** Já
apareceu em seis sabores — pontos Eco-Indicator (`Pt`), **DALY**, **eco-point** com factor de
normalização coreano, **mPEW/10 MN** do ReCiPe Europe, o **Environmental Cost Indicator em
euros por litro** (EPD segundo a EN 15804, com o `kg CO₂-eq` só na tabela metodológica de
ponderação) e o **índice normalizado por OPC** de um radar. Nestes casos há ACV a sério, com
unidade funcional e categoria de impacto, e a menção a `kg CO₂-eq` só aparece na tabela
metodológica que descreve a categoria — nunca num resultado. **Não é percentagem** nem facto
sectorial: é um valor de impacto real, mas irrecuperável para massa sem factores que o artigo
não publica. Apareceu 2 vezes num lote de 15, logo é comum. Marca `DUVIDA`.

📌 **«Mistura» não quer dizer «traço dosado» — não deixes que a palavra crie uma brecha.**
A compressão de um **compósito existente** caracterizado in situ (alvenaria de pedra por macaco
plano, taipa, solo natural) **é** compressão do material que o artigo estuda, e decide
normalmente: se der 0,14 MPa, rejeita. O que vai para dúvida é a grandeza errada, não o material
não-dosado.

⚠️ **Regra geral: qualquer grandeza que não seja COMPRESSÃO DA MISTURA vai para `DUVIDA`.**
Isto engloba, e substitui, os casos que se foram somando um a um: **flexão** da própria mistura,
**tracção por compressão diametral** (*splitting tensile*), tracção de **fibra de reforço**,
tracção de **chapa metálica**, classe de resistência do **cimento**. Todas são força por área;
nenhuma é comparável a um limiar de 20 MPa calibrado para compressão. Regista o valor e a
unidade real, e explica na nota qual é a grandeza.
📌 **E continua `DUVIDA` mesmo quando o valor de flexão está muito abaixo de 20.** Pode
parecer que 6,6 MPa à flexão rejeita à mesma — mas a flexão é sempre **menor** que a
compressão, pelo que um valor baixo à flexão **não permite inferir nada** sobre a compressão.
Rejeitar ali seria decidir por uma grandeza que não é a do critério.

✅ **O discriminador entre as duas regras vizinhas — «classe de projecto conta» e «classe na
tabela de factores é dúvida» — é este: o artigo diz, ou não diz, QUAL classe cada sistema usa.**

- **Diz** → conta, mesmo que o nome venha de um processo de base de dados (`Concrete, 35 MPa`
  do ecoinvent, `RC 40/50` do ICE Hammond & Jones). Se o artigo escreve «o pavimento usa
  Concrete 35 MPa» com a quantidade ao lado, a classe é do sistema que ele modela.
- **Não diz** → dúvida. Uma tabela que lista C20 a C50 entre 26 materiais, sem nunca atribuir
  nenhuma a nenhum edifício, é catálogo e não declaração.

⚠️ **Classe que só existe na tabela de factores de emissão: `DUVIDA`.** Um artigo lista
C20–C50 como linhas de uma tabela «factores de emissão de 26 materiais de construção» e
**nunca diz qual delas cada edifício usa**. O máximo é do *inventário*, não do material do
estudo — é a mesma objecção do benchmark de cimento Portland. Tabelas de factores por classe
são padrão na literatura chinesa, por isso vai repetir-se.

🚨🚨 **Antes de concluir «zero ocorrências», confirma que o texto extraído é texto.** Medido
na reauditoria: um ficheiro de 15 páginas que extrai inteiramente como cifra — fontes sem
`ToUnicode` válido, 52.116 caracteres de controlo, zero palavras reconhecíveis. Uma contagem
feita sobre isso **daria zero fosse qual fosse o conteúdo**. O teste é uma linha:

```python
ctrl = sum(1 for c in texto if ord(c) < 32 and c not in '\n\r\t')
```

Milhares de `ctrl` com nenhuma palavra comum reconhecível = texto imprestável. Nos ficheiros
sãos o `ctrl` é **zero**. Se acontecer, **renderiza as páginas e lê-as como imagem** — nunca
rejeites por ausência sobre um texto que não se lê, e di-lo na `nota`.

🚨🚨 **Um segundo tipo de texto ilegível, distinto e RECUPERÁVEL: fonte cifrada por
deslocamento ASCII fixo.** Medido duas vezes em lotes diferentes, mesma família editorial
(Elsevier/Procedia) — cada carácter da fonte (`TimesNewRomanPSMT` nos dois casos) está
deslocado em +29 no código, incluindo os dígitos, que saem como caracteres de controlo. Ao
contrário do caso do `ToUnicode` ausente, este **decodifica-se**: um deslocamento fixo é
reversível. Antes de decidir por ausência num ficheiro com `ctrl` alto, testa se um
deslocamento simples (experimenta de +1 a +40) produz texto inglês reconhecível — conta
palavras comuns antes e depois de cada deslocamento candidato e usa o que maximiza esse
número. **Auto-testa sempre antes de aplicar**: um ficheiro com nome de fonte estranho mas
texto já legível não deve ser "decodificado" às cegas — isso corrompe-o. Se a decodificação
não aumentar a contagem de palavras reconhecíveis, o texto já estava bom.

🚨🚨 **O eixo diz «kg CO₂ eq.» e a escala é 0–100%.** Medido no lote 34, em **três** artigos
do mesmo corpus: são ACV comparativas que normalizam o pior caso a 100 e mantêm o rótulo da
grandeza no eixo. Quem leia só a legenda ou o título do eixo regista como absoluto um número
que é percentagem. Num deles o próprio título da tabela diz *«(Percentage relative to the worst
option)»* — mas nos outros dois não dizia nada, e só a leitura da figura o revelou.

**A defesa é olhar para a escala, não para o rótulo.** Se o máximo do eixo é exactamente 100, ou
se a melhor opção dá exactamente 100 e as outras são fracções dela, desconfia. E se o conjunto
dos valores de todas as alternativas parece uma repartição de 100, é percentagem. Confirma
sempre com o texto: um artigo que só normaliza nunca escreve um kg em lado nenhum.

⚠️ Isto é **sistemático num certo tipo de revista**, não acidental — apareceu três vezes em
quinze artigos. Conta com ele.

🚨 **Valor declaradamente FICTÍCIO não é valor declarado: `Rejeitado`.** Aconteceu — uma
tabela com classes (C25/30, C40/50) e CO₂ (110, 100, 85, 65 kg CO₂-eq/m³) e uma nota de rodapé
a dizer *«Fictitious data is used due to confidentiality constraints prohibiting disclosure of
actual numbers»*. O artigo diz ele próprio que os números não são reais. Isto **não é dúvida de
critério**: é ausência de valor, e rejeita nos dois critérios. O mesmo vale para números
apresentados como meramente ilustrativos ou de exemplo.

📌 **Betão estrutural sem classe declarada é `Rejeitado`, e não é caso especial.** Vai
aparecer muito em ACV de edifícios: dezenas de m³ de betão armado inventariados e nem uma
classe em lado nenhum. É a aplicação directa do critério — «se não declara, Rejeitado». Não
inventes a classe a partir do uso estrutural. (O CO₂ do mesmo artigo pode perfeitamente
passar; são critérios independentes.)

✅ **Excepto quando o cimento É o produto que o artigo estuda — aí conta.** Uma ACV de
clínquer e cimento, com unidade funcional de 1 tonelada de cimento, em que `CEM-I 42.5 N`
descreve o próprio produto avaliado: a classe é do material do estudo e **aceita**, com 42,5
MPa. A regra abaixo foi escrita para artigos de *betão*, em que a classe descreve o ligante e
não a mistura.

⚠️ **Classe de resistência do CIMENTO (`CEM I 42.5`, `Rck 32.5`) não é a do betão: `DUVIDA`.**
É força por área e é uma designação normalizada da EN 197-1 — mas descreve o **ligante**, não a
mistura. Apareceu em três artigos de um só lote, e num deles era a única força por área do
documento. Mesma família da fibra de reforço.

🚨 **CONTA COM ISTO: artigos de UHPC sem um único «MPa» são frequentes, não excepção.** Já
aconteceu várias vezes — num, zero ocorrências de «MPa» e zero de «strength» em 77,7 mil
caracteres; noutro, um painel sanduíche de UHPC projectado com **zero** MPa reais e **146**
falsos positivos com `re.I`, todos `compa` de *comparative*, *compared* e *company*. Um
contador ingénuo aceita-o.
**Não o aceites por «UHPC é por definição >120 MPa»** — é exactamente o que a regra do «P-35»
proíbe: conhecimento externo que o documento não fornece.

⚠️ **Resistência de um componente de reforço não é resistência da mistura.** Tracção de 3.690
MPa de uma fibra de carbono é força por área, mas o limiar de 20 MPa está calibrado para a
compressão de uma mistura. Marca `DUVIDA` e explica.

⚠️✅ **Total da obra com o divisor impresso ao lado: CALCULA e ACEITA (decisão da Kiê,
2026-08-28).** Um artigo dá 1,44×10⁶ kg CO₂e do edifício e nenhuma forma normalizada — mas
imprime o **volume de betão (4.177,26 m³) na tabela ao lado**. Divide os dois e regista o
resultado (aqui, 344,6 kg CO₂e/m³) como `Aceito`, com `confianca=media` ou `baixa` e
`[ALERTA ETAPA4: valor derivado por divisao total/divisor impresso no artigo, nao publicado
como tal pelo autor]`. Regra geral da Kiê: «sempre que for possível nós mesmos realizarmos os
cálculos para chegar nos números que precisamos é aceito» — cobre esta família inteira (total +
divisor impresso, ainda que em tabelas/figuras diferentes do documento, desde que ambos sejam
do MESMO objecto/material).
- Se o total agrega MAIS do que o material do estudo (ex.: betão + aço + transporte + aditivos
  numa ponte, ou obra inteira incluindo movimento de terras) e o divisor é só do material do
  estudo (ex.: só o volume de betão), o valor dividido não isola limpamente o material — calcula
  na mesma, mas acrescenta ao alerta `valor pode incluir CO2 de outros materiais/fases, nao
  isolado ao [material]` para a Etapa 4 saber que a atribuição não é limpa.
- Se não houver um par claro (total, divisor) do MESMO objecto — ex.: um gráfico com N pontos
  de um Pareto front e um intervalo de totais/volumes sem correspondência 1-para-1 impressa —
  não inventes o pareamento. Isso continua `DUVIDA`, mas por falta de dado emparelhado, não por
  proibição de calcular.

⚠️ **Força por área sem mistura nenhuma: `DUVIDA`.** Um artigo de soldadura com 199 MPa de
tracção de chapa de alumínio é força por área e está muito acima de 20, mas **não há mistura
de todo** — não é o caso do componente de reforço dentro de uma mistura, é outra coisa.

⚠️ **Limite inferior aberto: `DUVIDA`.** «>10 N/mm²» e mais nada não prova que atinge 20 nem
que não atinge. A regra só prevê «atinge» e «nenhuma atinge».
✅ **Excepto quando o artigo não ensaia resistência de todo — aí a ausência decide,
`Rejeitado`.** Um `>` numa especificação de projecto não transforma a especificação numa
declaração de resistência. Caso medido: painel de isolamento cuja secção de ensaios só tem
condutibilidade térmica, e cujo «more than 1,2 MPa» é um requisito, não uma medição.

⚠️ **Classe que só aparece no título de uma referência: `DUVIDA`.** «Optimum usage of hybrid
fibers on **M30 grade** of concrete», na bibliografia, sendo M30 = 30 MPa pela norma indiana e
sendo esse o traço de referência que o artigo importa. Cruza a regra da designação com sufixo
(→ dúvida) com a da resistência medida por terceiros (→ aceitar). Vai repetir-se.

⚠️ **Um caso que a regra ainda não cobre — marca `DUVIDA` e não decidas.** Quando o material
que o artigo estuda **não tem resistência nenhuma declarada** e a única resistência do
documento é a do **betão de referência com que ele se compara** (um OPC de benchmark, com o
valor tirado de outro estudo). Comparar com um OPC de referência é praxe na ACV de ligantes
alternativos, por isso isto vai repetir-se. Regista `DUVIDA`, explica na nota qual é o
material do estudo e qual é o benchmark, e avalia o CO₂ à mesma.

✅ **Classe/faixa de resistência apresentada como catálogo comparativo, sem atribuição a um
sistema/mistura específico: ACEITA (decisão da Kiê, 2026-08-28), não `DUVIDA`.** Uma tabela
que lista C30 a C80 como *linhas* de fatores de emissão de várias fontes da literatura, ou uma
faixa geral (C20/25 a C35/45) que caracteriza a prática de um país/sector sem dizer qual classe
o próprio caso de estudo usa, ou uma classe que é só a variável de decisão de um modelo/algoritmo
sem o resultado final atribuído — tudo isto conta como classe declarada, `Aceito`, mesmo sem
ligação a um edifício/mistura específico. Substitui a orientação anterior desta secção (que
mandava `DUVIDA` nestes casos por «catálogo, não declaração»).
- Se a tabela compila dados de fontes externas citadas (uma revisão, um catálogo normativo como
  o Código Técnico espanhol, uma base de dados nacional) — regista essas fontes em
  `fonte_externa_resistencia`, para entrarem no ramo de busca por citação do fluxograma PRISMA.
- Se é um modelo/cálculo próprio do artigo sem fonte externa citável (variável de decisão de
  optimização, modelo estatístico interno, LCI de campo) — aceita na mesma, sem preencher
  `fonte_externa_resistencia` (não há nada externo para citar).

📌 **Numa revisão, distingue «compila» de «menciona».** A regra de baixo aceita a revisão que
**compila valores de resistência** dos estudos primários. Não cobre a revisão que **menciona
resistência de passagem** ao discutir método — «Braga et al. usaram C50/60» dentro de uma
tabela sobre escolha de unidade funcional é contexto de outro estudo, não compilação. As
revisões de ACV de betão fazem isto quase sempre, por isso a distinção conta.

✅ **Teste operável**, e é o melhor que temos: **conta se o valor é de uma mistura do tipo que a
revisão estuda; não conta se é de um material de contexto.** Uma revisão de agregado reciclado
que dá 39,28 / 38,46 / 39,74 MPa de misturas de RCA está a compilar o seu próprio objecto; a
mesma revisão a citar «27,6 MPa» para ilustrar como um estudo escolheu a unidade funcional
está a dar contexto. Em dúvida genuína, `DUVIDA`.

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

🚨 **E cuidado com o título que promete ACV e o corpo que não a faz.** Num artigo, «LCA»
aparecia cinco vezes — no título, no cabeçalho corrido e numa referência — e o corpo não tinha
unidade funcional, categoria de impacto nem um único valor de emissão. O padrão acerta no
**título do próprio artigo**. É prima da armadilha seguinte, com outra causa.

🚨 **Cuidado com «life-cycle assessment» que é ESTRUTURAL e não ambiental.** Nos artigos de
fiabilidade estrutural — as actas *Life-Cycle of Structures and Infrastructure Systems* são um
poço destes — «ciclo de vida» refere-se à vida da estrutura, não a ACV ambiental. O padrão
acerta em `lca` e devolve dezenas de acertos **sem um único valor de emissão**. Foram 8 de 15
artigos num lote. Confirma sempre que existe unidade funcional e categoria de impacto.

Este padrão pode correr sem distinguir maiúsculas — ao contrário do `MPa`, nenhum destes
termos é substring de palavras comuns.

⭐ **Regra da Kiê, 2026-08-24 — todas as unidades servem, incluindo o total da obra desde que
haja também um valor normalizado.** «Se tem os dois pode aceitar; rejeitar só se o CO₂ vier
apenas por edifício e não tiver mais nada além disso.» Aceites: kg CO₂/m³, /m², /t, /kg,
/m de túnel, por elemento, por viga. Rejeita quando **só** existe o total de um edifício
inteiro e nenhuma forma normalizada.

⭐ **O que decide NÃO é o tamanho do objecto — é haver ou não haver forma normalizada.**
Isto tem sido mal lido, e a formulação da Kiê é clara: rejeitar «somente se o CO₂ só vier por
edifício **e não tiver mais nada além disso**». A parte operativa é a segunda.

Não percas tempo a decidir se uma fundação, um sistema de laje ou um troço de túnel é «obra
inteira» ou «subsistema» — essa fronteira não existe na regra e não é preciso traçá-la.
Pergunta só: **há algum valor por m², por m³, por metro, por tonelada, por elemento?** Se há,
aceita. Se o único número é um total agregado, seja de que objecto for, rejeita. Um sistema de
laje com kg CO₂/m² aceita; uma fundação com um total de 52.000 kg CO₂eq e mais nada rejeita —
e a diferença entre eles não é serem subsistemas, é um estar normalizado e o outro não.

📌 **A mesma leitura para «edifício» vs «obra inteira».** A razão da exclusão é não haver como normalizar,
não a palavra *edifício*. Um total de uma **ponte**, de um viaduto ou de uma intervenção de
reforço, sem nenhuma forma por metro, por m² ou por elemento, cai na mesma regra e rejeita.
Caso medido: 151,3 t CO₂eq para o reforço de uma ponte de 34 m de vão, sem valor normalizado.

⚠️ **Distingue isto de «o total existe mas há também um normalizado»** — nesse caso aceita,
que é a regra da Kiê. O que rejeita é a ausência de qualquer forma normalizada, não a
presença do total.

🚨 **Facto sectorial genérico NÃO é valor de emissão do artigo.** É a regra gémea da que o
passo 4 já tem para a resistência. «A produção de uma tonelada de clínquer liberta cerca de
uma tonelada de CO₂», ou «a indústria do vidro emite 86 Mt de CO₂ por ano», são factores e
contextos de literatura — normalizados, absolutos, e **nada a ver com o material que o artigo
estuda**. Se é isso que o artigo tem, e não faz ACV nem declara unidade funcional, é
`Rejeitado`.

📌 **Balanço líquido negativo aceita, mas com aviso.** Um valor como −567,8 kg CO₂-eq por
unidade funcional, em que o sequestro excede a emissão, **é** um valor de emissão declarado e
passa o critério. Mas põe `balanco liquido negativo` em `aviso_metanalise`: uma metanálise de
emissões não pode somá-lo com os positivos sem tratar o sinal. Já apareceu duas vezes em cinco
lotes, não é excepção rara.

⚠️⚠️ **Uma REDUÇÃO expressa em massa (`95 kg CO₂-e/m³ a menos`) não está decidida: `DUVIDA`.**
Não é o mesmo que uma percentagem — é um valor absoluto, em unidade normalizada — mas também
não é um **nível** de emissão, e a metanálise precisa de níveis para calcular o indicador.
🚨 **Isto gerou uma inconsistência entre lotes** (um aceitou um delta de 120 kg/m³, outro
rejeitou um de 95 kg/m³), por isso passa a ser `DUVIDA` até a Kiê decidir. Regista o valor e a
página na mesma.

📌 **Percentagem de redução NÃO é valor de emissão.** Medido: o SUMMA 2023 (linha 2858) faz
ACV com dez indicadores e a Fig. 5 é um radar de **percentagens**, eixo de 0% a 80%, sem um
único valor absoluto. Rejeitado. Se o artigo só diz «reduziu 30%», é `Rejeitado`.

Se suspeitares que o valor absoluto está numa figura, **renderiza e olha** — o mesmo
procedimento do passo 5. O teste corre nos dois sentidos: no RO salvou o artigo, no SUMMA
condenou-o.

### 6b. ⚠️ Armadilha grave — cabeçalho de tabela repetido sobre as colunas erradas

Medida no lote 8. Um PDF repetia o cabeçalho `CC kg CO2 eq / OD / IR / PO` no topo das
páginas 19 e 21, **sobre blocos que continuavam outras colunas** (LU/WU/RF/RM e PM/HT/AC).
Quem lesse o texto achatado tirava dali «Total 273.474» como se fosse CC — **e enganava-se por
um factor de 5**. Os totais verdadeiros eram 54,5 / 63,6 / 63,8 kg CO₂eq por metro de viga.

**Só se apanha extraindo página a página** (`d[p].get_text()`), nunca do `full` normalizado.
Quando um valor de uma tabela grande te parecer alto de mais, vai à página de origem e
confirma que a coluna é mesmo a que o cabeçalho promete.

É prima da armadilha do cabeçalho corrido com os autores errados, já documentada no
`CLAUDE.md`: o editor arrasta um cabeçalho estagnado de uma página para outra.

📌 **Teste de sanidade que vale sempre a pena, e que apanhou dois casos num só lote:**
confronta o CO₂ com a dosagem de cimento do próprio artigo. 780 kg/m³ de cimento não podem
dar 410 kg CO₂eq/m³ — só o cimento daria mais de 600. E uma tabela intitulada «per m²» que dá
57.215 kg CO₂eq está a dar 57 toneladas por metro quadrado, que é a ordem de grandeza da obra
inteira. Nesses casos o valor existe e o critério passa: regista `escala suspeita` em
`aviso_metanalise`.

### 6b-bis. 🚨 NUNCA CALCULES UM VALOR QUE O ARTIGO NÃO IMPRIME

Esta é das regras mais importantes de todas, e foi escrita porque **já se violou duas vezes**,
apanhadas pela conferência de páginas:

- Num artigo, o valor registado de CO₂ (`134,6`–`247,8`) **não existe em lado nenhum do PDF**:
  era a **soma das parcelas de uma coluna de tabela**, feita por quem extraiu. E o artigo
  publica os seus próprios totais **noutra figura** — 139,4 e 252,0, maiores, porque incluem
  fases que a soma parcial deixou de fora. Ou seja: o valor reconstruído **contradizia** o valor
  publicado, e ninguém teria dado por isso.
- Noutro, os `40,8` MPa vinham de multiplicar `37,8 × 1,08`, a partir de uma frase que dizia
  «o teor óptimo melhora até 8%».

🚨 **E não confundas o LIMITE de uma variável de optimização com um RESULTADO.** Apanhado na
conferência: num artigo o valor registado eram 50 MPa — que é o **tecto do espaço de busca**
declarado numa tabela de parâmetros, quando **todas as optimizações devolveram 25 MPa**. Noutro,
40 MPa era o limite e os projectos usavam fck 25. É a mesma família do requisito de projecto:
o número existe, está impresso, e **não é o desempenho de nada**. Antes de registar um valor
tirado de uma tabela de parâmetros, verifica se há uma tabela de *resultados* logo a seguir.

**A regra:** regista **o que está impresso**, com a página onde está. Se o artigo só publica
parcelas e não o total, escreve a parcela mais alta que serve para o critério e diz na nota que
o total não é publicado. Se só há uma percentagem de melhoria sobre um valor base, isso é uma
percentagem — aplica-se-lhe a regra das percentagens, não a multiplicação.

Somar, multiplicar ou interpolar produz um número que **parece** um dado e não é: ninguém o pode
conferir contra o artigo, e pode contradizer o que o artigo de facto diz. A única aritmética
permitida é a **conversão de unidades** (kgf/cm² → MPa, t → kg), que é reversível e verificável.

### 6c. Quando o artigo se contradiz a si próprio

📌 **O rótulo do próprio gráfico manda sobre a prosa que o descreve.** Apareceu um artigo cujo
eixo diz «per m² of wall» e cujo texto, na página seguinte, diz «per linear metre of wall».
Regista o do eixo, e põe aviso. É a mesma lógica da armadilha do cabeçalho corrido, já
documentada no `CLAUDE.md`: entre o que a página imprime sobre si mesma e o que outra página
diz sobre ela, ganha a primeira.

📌 **`MPa` só no denominador, com o numerador nunca impresso, é ausência de valor.** Um artigo
com `GWI/MPa` e `fc28` em todas as fórmulas mas **sem uma única resistência impressa** não
declara resistência nenhuma — é `Rejeitado`. Não confundir com o caso em que o artigo usa a
métrica normalizada **e** declara o valor absoluto, que passa.

### 7. Outras armadilhas já medidas

- **O corte da secção de referências quase nunca funciona** — o cabeçalho «References»
  raramente aparece isolado numa linha (acertou em 1 de 10 ficheiros). Conta com títulos de
  referências a poluir a contagem e confirma sempre onde no documento está a ocorrência.
- **Tabelas sobrevivem à extracção** em ~10 de 12 ficheiros — achatadas numa linha, mas com
  valores e cabeçalhos pela ordem certa. Procura-as antes de assumir que precisas da figura.

## Decisões da Kiê (2026-08-25) — regras fixas, aplicar sempre

Estas oito regras fecham dúvidas de critério que se repetiam. Substituem qualquer instrução
anterior que as contradiga.

**1. Grandeza errada é REJEITADO, sempre.** Flexão (MOR, LOP), tração (do material ou de um
componente de reforço — fibra, aço, chapa), rigidez elástica (módulo resiliente) — nenhuma
destas é compressão do material em estudo, e nenhuma conta, seja qual for o valor. Não vai
para DUVIDA: `Rejeitado` directo. Isto inclui a classe de madeira (`C24` na EN 338 é FLEXÃO,
não compressão).

**2. Classe do CIMENTO como ligante, ou cimento como produto isolado sem mistura de betão/
argamassa no estudo — REJEITADO.** Não conta mesmo que o número esteja impresso (32,5 / 42,5 /
52,5 EN 197-1). O critério pede resistência de um material moldável estrutural; cimento puro,
mesmo como objecto central de uma ACV própria (ex.: ACV de produção de clínquer, UF = 1
tonelada de cimento), não é essa coisa. **Distinção que importa:** isto é diferente de uma
designação que descreve a MISTURA DE BETÃO do próprio estudo (ver regra 3) — a pergunta a
fazer é sempre "o número descreve o cimento como produto, ou a mistura de betão/argamassa que
o artigo estuda?". Só no segundo caso passa à regra 3.

**3. Designação normativa com sufixo numérico (M30, P-35, S275, "mesma classe conforme
ASTM X") que descreve a MISTURA DE BETÃO/ARGAMASSA do próprio estudo (não cimento como
produto — regra 2) — ACEITO se houver tabela normativa numérica real que converta o código
num MPa (M30 → IS 456, indiano, 30 MPa; C25/30 → EN 206). REJEITADO se a norma citada não tiver
tabela de classes numéricas (ex.: ASTM C1856 é norma de ensaio/cura, não define classes — não
há nada para converter). Regista sempre a via da conversão na nota, e marca `confianca=media`
com aviso para a Etapa 4.

**4. Limite inferior aberto (">X", "at least X") sem tecto — só conta se X sozinho já for
≥20.** Um "at least 10 MPa" não prova nada; um "at least 25 MPa" prova. Abaixo de 20 não é
estrutural — Rejeitado sem hesitar quando o limiar não chega lá sozinho.

**5. Idade de referência são os 28 dias.** Quando há valor aos 28 dias, usa-o sempre — não
importa se há valores a outras idades também. Quando só há dados a 7 dias, **é permitido
estimar os 28 dias** — única excepção à regra de nunca calcular o que o artigo não imprime.
Usa o modelo ACI 209R-92: `f'c(28) ≈ f'c(7) / 0,70` (razão típica de ganho de resistência para
cimento Portland comum, moist-cured). ⚠️ Esta razão é calibrada para **cimento Portland
convencional** — em geopolímeros, activados alcalinos ou ligantes sem cimento, a curva de
ganho de resistência é diferente e pode ser mais lenta, o que faria a estimativa ser
**conservadora de mais** (subestimar os 28 dias). Aplica-a mesmo assim quando não houver
alternativa, mas **regista sempre**: o valor aos 7 dias, o cálculo, o resultado estimado, e o
aviso `[ESTIMADO 7→28d, material nao-OPC: verificar]` quando o material não for cimento
Portland convencional. `confianca=baixa` sempre que este mecanismo for usado.

**5b. Segunda excepção autorizada (Kiê, 2026-08-30): massa específica padrão do cimento
(3,15 t/m³) para reconstituir massa a partir de volume.** Caso medido: um artigo publica uma
fórmula própria `CO2 = Vcement[m³] × Cclinker × EFclinker[t CO2/t clínquer]` sem nunca converter
o volume de cimento em massa antes de aplicar o factor massa/massa — o resultado herda m³ em vez
de toneladas, e não há densidade nenhuma impressa no artigo para desfazer isto. Antes de aplicar
esta excepção, investiga a fundo (lê o artigo inteiro, procura fórmulas, definições de variável,
notas de rodapé) — não presumas erro do autor sem procurar primeiro a explicação real. Só depois
de confirmada a causa exacta é que se aplica a massa específica padrão do cimento em dosagem por
volumes absolutos, **3,15 t/m³** (valor de engenharia universal, não um dado inventado — mesma
categoria da conversão psi→MPa), multiplicando pelo volume em m³ para obter a massa real.
`confianca=baixa` sempre, `[ALERTA ETAPA4: valor reconstituido assumindo massa especifica padrao
do cimento (3,15 t/m3) nao publicada pelo artigo]`. Não generalizes esta excepção a outras
densidades por analogia sem confirmar primeiro que o mesmo raciocínio dimensional se aplica.

**6. Revisão ou ensaio que só reporta variação percentual de resistência — ACEITO só se houver
um valor ABSOLUTO impresso em algum lugar do artigo** (mesmo que seja para ilustrar a escolha
de unidade funcional de um estudo citado, ou um limiar/excepção de norma tipo "except for
C50/60"). Se não houver nenhum valor absoluto em lado nenhum do documento, REJEITADO.

**7. CO₂ em unidade normalizada sem massa (mPt, Eco-indicator, DALY, kg CO₂/MPa, % de
contribuição) — ACEITO só se for possível converter para kg CO₂eq usando dados **impressos no
próprio artigo** (nunca um factor externo de outro método LCIA, nunca uma constante que não
esteja no texto). Duas formas válidas de conversão:
   - o artigo declara uma equivalência explícita entre a unidade normalizada e kg CO₂ (ex.:
     "50.000 kg CO₂ ≈ 12.500.000 mPt" para um caso de comparação) — usa essa razão, mas
     confirma que a base de normalização é a MESMA para o valor que estás a converter; se for
     um benchmark sectorial citado só para comparação, e não a mesma escala do resultado do
     estudo, isso é um risco a registar, não uma razão para recusar liminarmente — regista o
     cálculo e marca `confianca=baixa` com aviso para a Etapa 4;
   - o artigo dá, para o MESMO ponto/mistura, tanto o valor normalizado quanto a grandeza que
     o normaliza (ex.: Ci = kg CO₂/MPa E a resistência fc dessa mistura específica) — multiplica
     os dois, mas só se estiverem emparelhados no mesmo ponto de dados, nunca inferindo um fc
     genérico da curva para multiplicar por um Ci de outro ponto.
   Se nenhuma das duas formas se aplicar (não há equivalência impressa, não há par
   fc-Ci/massa-normalizado para a mesma mistura), REJEITADO — "irrecuperável sem factores que
   o artigo não publica" é razão suficiente.

**8. Redução expressa em massa (ex.: "41 kg CO₂/ton reduzidos por 5% de substituição") sem o
valor de base (baseline) impresso — REJEITADO**, pela mesma regra 7: sem o par completo
(base + reduzido, ou pelo menos a base), o número isolado não é um nível de emissão.

**9. Figura/dado motivacional de introdução, compilando literatura de forma não individualizável
e sem ligação ao objeto efetivamente estudado — REJEITADO** (caso ZIVKOVIC, linha 4323,
2026-08-30). Diferente da regra 6 (que aceita valor absoluto citado de outro estudo, DESDE QUE
seja um valor impresso e identificável): aqui o problema não é só a ausência de número — é a
figura ser **ilustração de fundo** ("olha como X é mais eficiente que Y segundo a literatura"),
com dados de várias referências agregadas numa mesma barra/ponto sem que se saiba de qual delas
vem cada valor, e sem que a figura descreva o material efetivamente ensaiado/medido pelo
próprio artigo. Três sinais, todos precisam de estar presentes para rejeitar por esta regra
(não bastam um ou dois — ver a distinção com a regra do "catálogo comparativo aceito" abaixo):
  - não é dado do próprio artigo (citação de revisões/refs externas);
  - não é rastreável a uma fonte única dentro dessas refs (agregação opaca);
  - a figura não é sobre o objeto que o artigo estuda, é comparação genérica de técnicas/
    materiais para motivar a escolha, na introdução ou discussão, desligada da mistura/sistema
    que o artigo efetivamente mediu.
  **Não confundir com a regra do "catálogo comparativo sem atribuição" (Etapa 2, 2026-08-29),
  que ACEITA:** aquela regra serve para uma tabela/faixa usada como especificação de PROJETO do
  próprio sistema estudado (a classe é o que o estudo adota, mesmo sem estar amarrada
  formalmente a "este é o sistema X"). Aqui não — a figura nem chega a ser a especificação de
  nada do que o artigo estuda, é só pano de fundo motivacional.

**Regra do material substituído (nova, caso recorrente em ACV de encargo evitado):** quando o
material do próprio estudo não tem resistência declarada e a única força por área do
documento pertence ao material que ele SUBSTITUI (ex.: pás de turbina reaproveitadas vs. o
betão que deixam de precisar), REJEITADO — a resistência do substituto não é a resistência do
material do estudo, mesmo que a quantidade de CO₂ evitado esteja emparelhada com essa classe
na mesma tabela.

**Alerta de qualidade obrigatório:** toda a decisão que resulte de estimativa (regra 5),
conversão indirecta (regras 3 e 7 na sua forma «equivalência impressa») ou qualquer inferência
que não seja leitura directa de um valor impresso deve levar, no carimbo da célula
`comments`, a marca `[ALERTA ETAPA4: <motivo curto>]` — é o sinal que a Etapa 4 usa para dar
nota baixa de qualidade a essa linha no controlo de qualidade. Cada decisão destas tem de vir
justificada por extenso na nota, nunca só "aceite por conversão" sem mostrar a conta.

## O que escreves

**Só** o ficheiro `lotes_etapa2/LOTE_<NN>_RESULTADO.csv`, com `QUOTE_ALL`, **sem acentos** nos
dados (a regra do `clean_str` do projecto) — ⚠️ **com uma excepção: a coluna `pdf`**, que é
chave de junção com o CSV do lote e tem de bater **exactamente**, acentos incluídos, com estas colunas:

```
linha,pdf,E2_resistencia,E2_co2,valor_resistencia_max,unidade_resistencia,
n_misturas_abaixo_20,valor_co2,unidade_co2,pagina_resistencia,pagina_co2,
fonte_resistencia,fonte_co2,fonte_externa_resistencia,fonte_externa_co2,
aviso_metanalise,confianca_resistencia,confianca_co2,nota
```

- ⭐⭐ `pagina_resistencia` e `pagina_co2`: **OBRIGATÓRIAS sempre que houver valor.** O
  **número da página impressa do PDF** onde o valor está, mais a localização exacta dentro
  dela. Exemplos: `p.9, Tab.4` · `p.14, Fig.11 (eixo)` · `p.7, texto, sec.3.2` ·
  `p.62, Grafico 15 (rotulo)`. Se o valor aparecer em mais do que um sítio, dá o mais
  autoritativo (tabela antes de texto, texto antes de figura) e menciona o outro na nota.

  🚨 **Isto é para a Kiê poder conferir sem reler o artigo, e é inegociável.** Não escrevas
  «62% do documento», nem «na secção de resultados», nem «na Tabela 4» sem a página: quem vai
  verificar abre o PDF numa página, não numa percentagem. Usa a numeração de páginas do
  ficheiro tal como o `pymupdf` as conta (`d[i]` → página i+1) e, se a paginação impressa do
  artigo for diferente da do ficheiro, **dá as duas**: `p.9 do ficheiro (p.1043 impressa)`.

  Na `confianca_*` de uma rejeição **por ausência de valor**, escreve `alta` se procuraste bem
  e tens a certeza de que não há nada — é confiança na rejeição, não no valor. Deixa-a **vazia**
  nos `nao avaliado` da cascata.

  Quando o critério é `Rejeitado` por ausência de valor, deixa a coluna de página **vazia** — não há
  página para apontar. Quando é `Rejeitado` porque o valor existe mas é insuficiente (todas as
  misturas abaixo de 20), **preenche na mesma**: é preciso poder conferir a rejeição.

- `fonte_resistencia` e `fonte_co2`: **duas colunas separadas**, porque os dois valores vêm
  muitas vezes de sítios diferentes — no lote 3 houve um artigo com a resistência em tabela e o
  CO₂ em figura renderizada. Valores: `texto` · `tabela` · `classe declarada` · `classe de
  projecto` · **`figura (rotulo extraido)`** quando o valor vive numa figura mas o extractor
  apanhou o rótulo · **`figura (renderizada)`** quando tiveste de olhar para a imagem e **ler o
  valor contra o eixo** · **`figura (rotulo impresso)`** quando renderizaste mas o número
  estava escrito sobre a barra, sem estimativa nenhuma — esta merece `confianca=alta`, ao
  contrário da anterior.
  ⚠️ Não confundas as duas últimas: a primeira é barata e de confiança alta, a segunda é uma
  leitura contra o eixo, com confiança média.
- ⭐ `valor_co2`: **preenche-o mesmo quando `E2_co2` é `nao avaliado` pela cascata**, se por
  acaso já viste o valor ao verificar o ficheiro. O veredito fica `nao avaliado` — a cascata
  mantém-se —, mas o número fica pesquisável por coluna em vez de enterrado na nota. Num lote,
  três dos cinco rejeitados na resistência tinham CO₂ que passaria; se a regra for recalibrada,
  isso poupa reabrir três PDFs.
- `aviso_metanalise`: **vazio** na esmagadora maioria. Preenche quando o valor existe mas a
  metanálise não o pode usar sem cuidado — **e também quando o valor existe e o critério
  falha**, porque essa informação é útil se a regra vier a ser recalibrada e poupa reabrir o
  PDF. Casos já vistos:
  `sem dados proprios` · `captacao e nao emissao` (o número é *uptake* por carbonatação) ·
  `balanco liquido negativo` · `escala suspeita` · `normalizado pela resistencia` ·
  `sem amostras proprias` · `escala ambigua` (quando o referente do valor é que é dúbio — por
  exemplo um total de 417 kg CO₂eq que tanto pode ser por viga como pelas três vigas — o que é
  diferente de `escala suspeita`, em que o número é implausível) · `unidade nao declarada`.
  Descreve em texto livre se for caso novo, e explica na nota.
- `unidade_co2`: se o artigo dá os números e **nunca declara a unidade** (acontece), escreve
  **`nao declarada`** e põe `unidade nao declarada` em `aviso_metanalise`. **Não infiras a
  unidade pela ordem de grandeza** — regista o que lá está e deixa a inferência para quem
  extrair, com o aviso à vista.
  📌 **Unidade sem prefixo de massa é outro caso**: um eixo que diz `GWP (CO₂eq/m³)` tem a
  normalização declarada e falta-lhe só a massa. Escreve a unidade **tal como está impressa** e
  põe `prefixo de massa nao declarado` em `aviso_metanalise` — é diferente de não haver unidade
  nenhuma, e a metanálise resolve-o pela ordem de grandeza com o aviso à vista.
  📌 **Mas há uma inferência legítima, e distingue-se bem da outra: a que vem da cadeia de
  unidades.** Se os factores estão em impacto **por kg** e a unidade funcional declarada é
  **1 m³**, o resultado é kg CO₂eq/m³ por construção, não por parecença de tamanho. Nesse caso
  escreve a unidade com a marca **`derivada da unidade funcional`** e explica a cadeia na nota.
  A inferência por ordem de grandeza é adivinhar; esta é aritmética.
- `n_misturas_abaixo_20`: o número quando as misturas são contáveis, `todas` quando nenhuma
  atinge 20 — **`todas` tem precedência sobre o número**, mesmo quando as misturas são
  contáveis e são poucas, e **vazio** quando o artigo não declara resistência nenhuma. Quando o intervalo
  declarado prova que há pelo menos N mas o texto só transcreve algumas, escreve **`>=N`** e
  explica na nota — não arredondes para o número que conseguiste ver. Quando o artigo não tem misturas de todo — trabalha com
  classes de projecto de um edifício — escreve **`sem misturas`**, e se **alguma dessas classes
  estiver abaixo de 20** (um betão de regularização a 16 MPa, por exemplo) escreve
  **`sem misturas; N classes abaixo`**, para a informação não se perder, que não é o mesmo que `0`
  (o `0` diz que houve contagem). E quando o que fica abaixo de 20 é uma **idade** e não uma
  composição (7 dias abaixo, 28 e 90 acima), conta **`0`**: a coluna conta misturas, não pares
  mistura×idade — mas di-lo na nota. E quando o artigo
  trabalha sobre uma **faixa contínua** ou uma base de dados de traços (por exemplo «~1.000
  traços entre 18 e 80 MPa»), em que há seguramente misturas abaixo de 20 mas o artigo nunca
  diz quantas, escreve **`nao contavel`** — que serve também para revisões que transcrevem
  valores de vários estudos primários sem os totalizar.
  📌 **Numa tabela em matriz, conta proporções de mistura, não combinações.** Três resistências
  × três teores de adição dá 9 proporções — que são as colunas da tabela de traços —, e não as
  ~30 combinações que se obteriam multiplicando também pelos tipos de cimento e de adição. A
  coluna conta o que o artigo dosou, não o espaço de desenho.
  📌 Com o veredito em `DUVIDA`, escreve **`nao aplicavel (duvida)`** — a pergunta «quantas
  ficam abaixo de 20» pressupõe justamente o que ficou por decidir, e escrever `todas` ali
  lê-se como uma rejeição já tomada.
  ⚠️ **Distingue a queda com a idade da composição fraca.** Uma mistura que vai de 22–36 MPa
  aos 35 dias para 11–12 MPa aos 90 é um facto substantivo — perda de resistência ao longo do
  tempo —, não é o mesmo que uma mistura pobre. A contagem continua a ser `0` (a coluna conta
  misturas e o valor de referência é o dos 28 dias), mas põe **`perda de resistencia com a
  idade`** em `aviso_metanalise`: é informação que a metanálise precisa de ver.
    🚨 **Antes de contar, verifica se a tabela mistura idades.** É o erro mais fácil de cometer e
  apareceu **três vezes num só lote de 15**: seis valores entre 15,9 e 19,7 MPa que eram todos
  aos 7 dias, com o mínimo aos 28 dias a ser 24,8. A coluna conta **misturas**, e o valor de
  referência é o dos 28 dias.
  📌 **Uma mistura exactamente sobre os 20 MPa não conta como «abaixo»** — 20 não está abaixo
  de 20, pela mesma razão que faz um C20/25 entrar. Se a leitura da figura te deixar em dúvida
  sobre se a barra está em cima ou abaixo da marca, escreve `N (1 no limiar)` e explica.
  ⚠️ **O `0` está a fazer dois trabalhos**, e convém distingui-los: «medi todas as N misturas e
  nenhuma fica abaixo» escreve-se `0`; «o artigo tem N misturas mas só declara resistência de
  uma, e essa está acima» escreve-se **`0 (so 1 de N declarada)`**. A segunda diz à metanálise
  que faltam dados; a primeira não.
- `fonte_externa_resistencia` e `fonte_externa_co2`: **duas colunas**, pela mesma razão que
  `fonte_resistencia` e `fonte_co2` — é comum a resistência ser classe de projecto (campo vazio)
  e o CO₂ vir de uma base de dados. Cada uma segue a regra abaixo, aplicada ao seu valor.
  **Vazio** quando os valores são do próprio artigo, **e também** quando são
  uma classe nominal ou de projecto — não há estudo primário para citar; nesse caso põe
  `sem amostras proprias` em `aviso_metanalise`. Só se preenche quando o artigo aponta uma obra
  concreta como origem do valor (por exemplo «our previous study [55]»): a citação ou o DOI,
  ou `nao identificada` se o artigo não a identificar. Separa várias com `;`.
  📌 Quando a origem é um **factor de emissão citado de um artigo** (Turner & Collins, IPCC,
  uma referência numerada), escreve **`factores de emissao de literatura: <refs>`**. Foi a
  origem mais frequente de todas num lote — metade dos artigos. **Estes entram no ramo de busca
  por citação do PRISMA**: são a fonte original do dado, que é exactamente o que a regra da Kiê
  manda capturar.
  📌 Quando a origem é uma **base de dados de inventário** (AusLCI, ecoinvent, BEDEC, LCI
  nacional), escreve **`base de dados de inventario: <nome>`**. Não é um estudo primário, não
  tem DOI e **não entra no ramo de busca por citação do PRISMA** — mas convém ficar registado,
  porque diz à metanálise que o valor não é uma medição do artigo.
- `confianca_resistencia` e `confianca_co2`: **duas colunas**, `alta` · `media` · `baixa`.
  Pela mesma razão das outras que já se desdobraram — é comum a resistência vir de ensaio
  próprio no texto (alta) e o CO₂ de uma leitura contra o eixo de um gráfico (média).
- `nota`: o raciocínio nos casos não triviais. A localização vai nas colunas de página; a nota
  serve para o que elas não cabem — porque escolheste um valor e não outro, o que a figura
  mostrava, que armadilha evitaste. É isto que
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
