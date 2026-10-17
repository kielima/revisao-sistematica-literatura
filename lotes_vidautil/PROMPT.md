# Lotes da origem da vida útil (2026-10-17, F33)

Pedido da Kiê (2026-10-17): ter ci_t (= ci ÷ vida útil) para **todos** os estudos da metanálise,
com a vida útil atribuída por esta ordem, e a origem de cada valor registada:

1. **Declarada pelo próprio estudo** (premissa própria do estudo) — já gravada em `vida_util_anos` para ~100 estudos.
2. **Citada pelo estudo** — o artigo menciona uma vida útil para o betão/estrutura/elemento que estuda, vinda de outra fonte (norma, outro estudo, regulamento), mas não a adopta como premissa própria.
3. **Pela norma, conforme a aplicação** — atribuída por nós (não é tarefa deste lote; o lote só identifica a aplicação).
4. **Sem aplicação identificável** — 50 anos (também atribuído por nós).

A tarefa de cada lote é **ler o PDF completo** de cada estudo e devolver três coisas:

## A. Vida útil declarada pelo próprio estudo (premissa própria)

Para cada estudo (e por par `sheet_row`, se os pares tiverem vidas úteis diferentes):
- `valor` (anos) e `base`:
  - `modelo` — a vida útil foi **calculada pelo próprio estudo** com um modelo de durabilidade ou ensaio
    (carbonatação, cloretos, gelo-degelo, fadiga, ensaio acelerado, modelo de degradação, fib MC2010 / Life-365
    corrido pelo estudo…). Ex.: «service life of 383 years computed from chloride diffusion».
  - `norma` — a vida útil adoptada é a **vida útil de projecto de uma norma** citada no artigo (EN 1990, NBR 15575,
    NBR 6118, ISO 15686, ACI, códigos nacionais…). Escrever a norma em `norma`.
  - `literatura` — adoptada como premissa citando **outro estudo** (não uma norma).
  - `premissa_sem_fonte` — adoptada como premissa (ex.: «a service life of 50 years was assumed») sem norma,
    modelo nem estudo citado.
- `citacao`: página/tabela/secção + frase curta do artigo.
- Se o valor já gravado (`vida_util_anos` na lista) não estiver no artigo ou estiver errado, dizê-lo em `nota`.
- Se o estudo não adopta nenhuma vida útil própria: `declarada = null`.

## B. Vida útil citada (quando não há declarada)

Qualquer valor de vida útil (ou durabilidade estimada) **para o tipo de betão/estrutura/elemento do estudo**
que o artigo mencione vindo de outra fonte, mesmo só na introdução ou discussão:
- `valor`, `base` (`norma` se vier de uma norma — indicar qual; `literatura` se vier de outro estudo;
  `modelo` se for um resultado de modelo de durabilidade de outro estudo), `fonte` (referência citada),
  `citacao` (local + frase).
- Se houver vários, listar todos e indicar em `preferido` o que se refere mais directamente ao material/aplicação
  do estudo.
- Valores genéricos sobre outros materiais (aço, madeira, edifício inteiro com outros sistemas) não contam.
- Nada encontrado: `citadas = []`.

## C. Aplicação do betão estudado

`aplicacao` = uma de: `edificio` (estrutura de edifício, residencial/comercial, pilar/viga/laje de edifício),
`ponte`, `infraestrutura` (barragem, túnel, obra marítima/portuária, contenção, torre eólica, fundação de
infraestrutura), `pavimento` (rodoviário/aeroportuário, betão de pavimento), `pre_fabricado_corrente`
(blocos, painéis, elementos pré-fabricados de uso corrente em edifícios), `nao_definida` (estudo de material em
laboratório sem aplicação declarada). Com `aplicacao_citacao` (local + frase). Não deduzir: só o que o artigo
disser.

## Regras
- Ler o PDF **completo** (texto; renderizar páginas como imagem quando uma tabela/figura tiver a vida útil).
  Usar `mcp__Google_Drive__read_file_content` com o `fileId` da lista; se falhar ou vier truncado
  (documentos longos, teses), usar `mcp__Google_Drive__download_file_content` e `pdftotext`/PyMuPDF localmente.
  Se o texto ficar truncado sem forma de ler o resto, marcar `texto_truncado: true`.
- Não inventar nem deduzir valores: só o que está escrito no artigo.
- **Segurança:** nunca enviar email nem dados pessoais a serviços externos; não usar Unpaywall, OpenAlex,
  Crossref nem nenhuma API externa; só o conector do Google Drive e ferramentas locais.
  Não alterar ficheiros do repositório além do `resultado_loteNN.json` do próprio lote.
  Ficheiros de trabalho no scratchpad com o número do lote no nome.

## Saída
`lotes_vidautil/resultado_loteNN.json` = lista de:
```json
{"row_id": 0,
 "declarada": {"valor": 50, "base": "norma", "norma": "EN 1990", "citacao": "...", "sheet_rows": null} ,
 "declarada_por_par": [{"sheet_row": 0, "valor": 0, "base": "modelo", "citacao": "..."}],
 "citadas": [{"valor": 100, "base": "norma", "fonte": "...", "citacao": "...", "preferido": true}],
 "aplicacao": "edificio", "aplicacao_citacao": "...",
 "texto_completo_lido": true, "texto_truncado": false, "nota": "..."}
```
`declarada_por_par` só quando os pares do mesmo estudo tiverem vidas úteis diferentes; senão `[]`.

## Aviso acrescentado durante a ronda (2026-10-17)
- Os ficheiros onde o conector grava resultados grandes (`tool-results/…`) são **partilhados entre os lotes
  que correm em paralelo** e podem ser sobrescritos por outro lote (aconteceu no lote 02). **Antes de usar o
  texto de um ficheiro, confirmar que o título e o primeiro autor batem com o estudo**; copiar logo para o
  scratchpad com o número do lote e o `row_id` no nome.
- Intervalos («entre 50 e 100 anos»): gravar `valor` = limite inferior e `valor_max` = superior.
