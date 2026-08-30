# Reauditoria dos rejeitados por resistencia (lotes 1-12)

## Porque existe esta passagem

Os lotes 1-12 da Etapa 2 correram com um padrao de busca **incompleto**. Quatro
formas de declarar resistencia escapavam-lhe, e qualquer uma delas pode ter feito
rejeitar um artigo que na verdade declara resistencia:

1. **Classe chinesa de um so numero** — `C45`, `C30`, `C60`. O padrao antigo so
   apanhava a forma europeia de dois numeros (`C25/30`).
2. **A unidade por extenso** — `20 megapascals`, `megapascal`.
3. **A classe sem prefixo** — `25/30`, `30/37`.
4. **A classe com espacos** — `C 25/30`, `C 30`.

A tua tarefa e **so** correr o padrao corrigido sobre estes artigos e dizer se
algum deles tem, afinal, uma declaracao de resistencia que o padrao antigo perdeu.

## O que NAO e esta tarefa

- **Nao e retriar o artigo.** Nao releias o artigo todo, nao julgues o CO2, nao
  mexas na decisao de nenhum outro criterio.
- **Nao reverter rejeicoes por valor baixo.** Muitos destes artigos foram
  rejeitados nao por falta de resistencia mas porque **nenhuma mistura chega aos
  20 MPa** (ex.: um solo estabilizado com maximo de 2,27 MPa). Essa rejeicao esta
  certa e nao se toca. A coluna `motivo_original` diz-te qual foi o caso.

## Metodo

Para cada linha da lista:

1. Obtem o PDF. Procura o nome do ficheiro em
   `/home/user/revisao-sistematica-literatura/DRIVE_FILEID_MAP.csv` para tirar o
   `fileId`, depois `mcp__Toolkit__googledrive_download_file`, e descarrega o
   `downloaded_file_content.s3url` com `curl`. Se o descarregador falhar com
   `token expired`, e definitivo dentro da sessao: passa a
   `mcp__Google_Drive__download_file_content` (base64, grava e descodifica) e,
   para ficheiros acima de ~6 MB, `mcp__Google_Drive__read_file_content`.

2. Extrai o texto com `pymupdf` (o modulo chama-se `pymupdf`, nao `fitz`).

3. Corre exactamente este padrao:

```python
import re
SIGLA = r"MPa|Mpa|mPa"                     # SEM re.I, NUNCA com re.I
NOVOS = (r"megapascals?|"                  # unidade por extenso
         r"\bC\s?\d{2}\b|"                 # classe de um numero, com ou sem espaco
         r"\bC\s?\d{2}\s?/\s?\d{2}\b|"     # classe europeia, com ou sem espacos
         r"\b\d{2}\s*/\s*\d{2}\b")         # classe sem prefixo
hits  = [(m.group(), m.start()) for m in re.finditer(SIGLA, texto)]
hits += [(m.group(), m.start()) for m in re.finditer(NOVOS, texto, re.I)]
```

⚠️ A sigla `MPa` procura-se **sensivel a maiusculas**. Com `re.I` apanha `compa`
de *comparison* e `impact`, e ja mediu-se um ficheiro com 463 falsos positivos.

4. **Filtra os falsos positivos** — o padrao dos novos e largo de proposito e vai
   apanhar muito lixo. Descarta:
   - numeros de pagina, anos, volumes e paginacao de referencias (`45/50` de um
     intervalo de paginas, `C 20` de uma cota bibliografica);
   - `C\d{2}` que seja rotulo de amostra, de cenario ou de composto quimico
     (C25 pode ser uma cadeia de carbono);
   - qualquer acerto dentro da lista de referencias;
   - qualquer acerto que descreva **outro estudo citado** e nao o material deste
     artigo.

5. Se sobrar um acerto genuino, **abre o contexto e confirma**: e uma classe ou
   resistencia **do material estudado neste artigo**? Regista a pagina.

## Antes de tudo: confirma que o texto extraido e texto

Descoberto na parte 2, e e grave. O ficheiro `FELICIONI et al., 2023` extrai
**inteiramente como cifra** - as 15 paginas saem em fontes sem `ToUnicode` valido, dando
52.116 caracteres de controlo e zero palavras reconheciveis. O «zero ocorrencias de MPa»
que a triagem original registou **nao media o artigo, media o ruido**: teria dado zero fosse
qual fosse o conteudo do PDF.

So atinge as rejeicoes - um artigo aceite encontrou valores, logo o texto lia-se.

**O teste e barato e corre-se sempre, antes do padrao:**

```python
ctrl = sum(1 for c in texto if ord(c) < 32 and c not in '\n\r\t')
```

Milhares de `ctrl` com nenhuma palavra comum reconhecivel quer dizer que o texto nao presta.
Nos 13 ficheiros saos do mesmo lote o `ctrl` era **zero**.

**Se o texto nao presta, nao decidas por texto:** renderiza as paginas e le-as como imagem.
Foi o que se fez, e a rejeicao manteve-se - mas passou a assentar em prova visual em vez de
numa contagem vazia. Regista na `nota` que o ficheiro e ilegivel por extracao e que a decisao
veio da leitura das paginas.

**Outra armadilha do padrao, da mesma parte:** o `\s` casa a **mudanca de linha**. Numa tabela
de temperatura e pressao, `50 grausC` no fim de uma linha e `30 bar` no inicio da seguinte
produziram um `C 30` fantasma. Confirma sempre o contexto de um acerto antes de o dar por bom.

## Saida

Escreve `REAUDITORIA_RESISTENCIA_RESULTADO.csv` com estas colunas:

```
linha,pdf,veredito,valor_encontrado,unidade,pagina,trecho,nota
```

`veredito` e um de:
- `MANTEM` — o padrao novo nao encontrou nada de novo, a rejeicao esta certa.
- `MANTEM_VALOR_BAIXO` — encontrou resistencia mas confirma-se abaixo de 20 MPa.
- `REABRIR` — encontrou uma declaracao genuina de resistencia do material deste
  artigo que o padrao antigo perdeu. Preenche `valor_encontrado`, `unidade`,
  `pagina` e `trecho` (a frase impressa, tal e qual).
- `SEM_ACESSO` — nao foi possivel obter ou ler o ficheiro. Diz porque.

`trecho` e sempre **texto impresso copiado**, nunca uma parafrase e nunca um
valor calculado.

## Regras que nao podes quebrar

- Escreves **apenas** este CSV. Nunca escrevas em `articles_final.xlsx` (podes
  le-lo). Nunca facas commit.
- **Nunca calcules um valor que o artigo nao imprime.** Nem somar, nem aplicar
  factores, nem converter percentagem em absoluto. So e permitida conversao de
  unidade (psi, N/mm2, kPa, kgf/cm2 para MPa) — e nesse caso escreve na `nota`
  qual foi o valor original impresso.
- Perante duvida, `veredito` fica `REABRIR` e explicas na `nota`. Mais vale
  devolver-me um caso para eu olhar do que fechar um artigo por engano.
