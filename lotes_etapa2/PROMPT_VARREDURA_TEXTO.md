# Varredura de texto ilegivel nas rejeicoes por ausencia

## Porque existe

Uma rejeicao por ausencia diz «zero ocorrencias de MPa no documento». Mas se o PDF extrai
como cifra - fontes sem `ToUnicode` valido -, a contagem **daria zero fosse qual fosse o
conteudo**. Nao mede o artigo, mede o ruido.

Aconteceu, e foi medido: o `FELICIONI et al., 2023` sai em 52.116 caracteres de controlo e
zero palavras reconheciveis nas suas 15 paginas. Nos 13 ficheiros saos do mesmo lote o
mesmo contador dava **zero**.

Isto so ameaca **rejeicoes**. Um artigo aceite encontrou valores, logo o texto lia-se.

## O que esta varredura E, e o que NAO e

**E:** medir, para cada ficheiro, se o texto extraido presta. Nada mais.

**NAO e:** retriagem. Nao julgas resistencia, nao julgas CO2, nao lês o artigo, nao mexes em
decisao nenhuma. Se o texto prestar, escreves `TEXTO_OK` e passas ao seguinte - **sem sequer
procurar valores**. E de proposito que e tao pouco: assim cabem centenas de artigos.

## Metodo

Para cada linha:

1. Procura o nome do ficheiro em `/home/user/revisao-sistematica-literatura/DRIVE_FILEID_MAP.csv`
   para tirar o `fileId`; depois `mcp__Toolkit__googledrive_download_file` (uma chamada de cada
   vez, **nunca em paralelo**; nao tem tecto de tamanho) e `curl` do `downloaded_file_content.s3url`.

2. Extrai o texto com `pymupdf` (o modulo chama-se `pymupdf`, nao `fitz`).

3. Corre o contador:

```python
ctrl = sum(1 for c in texto if ord(c) < 32 and c not in '\n\r\t')
n = len(texto)
palavras = sum(texto.lower().count(w) for w in (' the ',' and ',' of ',' de ',' da ',
                                                ' concrete ',' cimento ',' betao '))
```

4. Classifica. **Le o limiar como RACIO, nao como valor absoluto** - calibracao medida na
   parte 1, sobre 30 ficheiros:

   - `TEXTO_OK`: `palavras >= 50` **e** `ctrl/n < 0,5%`.
   - `TEXTO_ILEGIVEL`: `palavras <= 10` **e** (`ctrl >= 1000` **ou** `ctrl/n > 5%`).
   - Entre os dois, ou duvida: `SUSPEITO`.

   Porque assim: nos 29 ficheiros saos da parte 1 o `ctrl` foi de 0 a 29, em documentos de 17
   mil a 176 mil caracteres - racio maximo de 0,045%. Um deles tinha 16 caracteres de controlo
   em 52 mil, que e ruido tipografico normal e nao cifra. O unico ilegivel tinha **72,5%**.
   A separacao e de quase quatro ordens de grandeza, pelo que na pratica nao ha casos de
   fronteira - mas mantem a categoria `SUSPEITO` para o caso de aparecer um.

5. Classificacao antiga (mantida por referencia):
   - `ctrl` perto de zero **e** `palavras` numa ordem de grandeza normal → **`TEXTO_OK`**.
   - `ctrl` na ordem dos milhares **e** `palavras` perto de zero → **`TEXTO_ILEGIVEL`**.
   - qualquer coisa entre as duas, ou duvida → **`SUSPEITO`**, e explicas.

5. **So para os `TEXTO_ILEGIVEL` e `SUSPEITO`:** renderiza as paginas e confirma pela imagem
   se ha ou nao declaracao de resistencia ou de emissao. Diz o que viste. Nao decidas o
   criterio - descreve o que esta impresso e deixa a decisao para quem integra.

## Saida

`VARREDURA_TEXTO_RESULTADO.csv`, com:

```
linha,pdf,veredito,ctrl,n_caracteres,palavras,paginas,achado_visual,nota
```

`achado_visual` so se preenche nos casos nao-OK: o que as paginas renderizadas mostram - ha
tabela de resistencia? ha valor de emissao? em que pagina?

## Regras que nao podes quebrar

- Escreves **apenas** este CSV. Nunca escrevas em `articles_final.xlsx`. Nunca facas commit.
- Nao decidas criterio nenhum, nem sequer nos casos ilegiveis. Descreve.
- Nao te deixes tentar a «aproveitar» que ja tens o texto para conferir valores. A varredura
  vale pela rapidez; se cada artigo virar uma releitura, deixa de caber.
