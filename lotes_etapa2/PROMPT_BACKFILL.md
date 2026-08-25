# Recuperação das páginas em falta — Etapa 2

Estes artigos **já foram triados**. O veredito está tomado e **não é para rever**. O que falta é
uma coisa só: **a página onde cada valor está**, para a Kiê poder conferir sem reler o artigo.

A instrução antiga pedia «onde no documento está o valor» e produziu registos inconsistentes —
uns com a página, outros com «62% do documento» ou só o número da tabela. Isso não serve.

## O que fazes, por artigo

1. Obtém o PDF pelo caminho normal: `grep` no `DRIVE_FILEID_MAP.csv` para o `fileId`, depois
   `mcp__Toolkit__googledrive_download_file` e `curl` ao `s3url`. **Um de cada vez** (a chamada
   em lote rebenta com Cloudflare 520).
2. Procura **o valor que já está registado** no teu CSV de entrada — não procures outro, não
   reavalies o critério.
3. Localiza-o e regista **a página impressa do PDF mais a localização exacta dentro dela**:
   `p.9, Tab.4` · `p.14, Fig.11 (eixo)` · `p.7, texto, sec.3.2` · `p.62, Grafico 15 (rotulo)`.
   Usa a numeração do `pymupdf` (`d[i]` → página i+1) e, se a paginação impressa do artigo for
   diferente da do ficheiro, **dá as duas**: `p.9 do ficheiro (p.1043 impressa)`.

```python
import pymupdf, re
d = pymupdf.open('r<linha>.pdf')
alvo = '34.01'                      # o valor que ja esta registado
for i in range(d.page_count):
    t = re.sub(r'\s+', ' ', d[i].get_text())
    if alvo in t:
        print('pagina', i+1, '->', t[max(0,t.find(alvo)-150):t.find(alvo)+80])
```

⚠️⚠️ **Antes de concluíres que não está lá, tenta a notação científica.** `0,243` costuma
estar impresso como **`2,43E-01`**, e a busca literal falha em silêncio. Tenta também o número
sem a unidade — «12» e «MPa» podem estar separados por uma quebra de linha.

📌 **Para ficheiros grandes, `read_file_content` resolve sem gastar contexto** — e os
**cabeçalhos e rodapés correntes** dão-te a página impressa de graça: `Environments 2022, 9, 6
— N of 10`, `Journal of CO2 Utilization 90 (2024) 102986 5`, ou os marcadores `[**Page N**]`.
São âncoras directas, não interpolação. Diz na nota que foi por essa via.

Se o valor não aparecer no texto, é porque veio de figura: procura pela legenda, renderiza a
página (`d[i].get_pixmap(dpi=200)`) e confirma visualmente qual é.

## ⚠️ Se o valor não bater

Pode acontecer não encontrares o valor registado em lado nenhum. **Não o corrijas nem o
apagues** — regista `NAO LOCALIZADO` na coluna da página e explica na nota o que procuraste e
o que encontraste. Isso é um achado importante, não uma falha: significa que a extracção
anterior pode ter tido um problema, e é exactamente o que esta passagem serve para apanhar.

## O que escreves

**Só** o ficheiro que te for indicado, com `QUOTE_ALL` e sem acentos (excepto na coluna `pdf`,
que é chave de junção e tem de bater exactamente):

```
linha,pdf,pagina_resistencia,pagina_co2,nota_backfill
```

`nota_backfill` só se houver algo a dizer: valor não localizado, valor que aparece em vários
sítios, paginação impressa diferente da do ficheiro.

## O que NÃO fazes

- **Não revês o veredito.** Não é essa a tarefa, e mudá-lo aqui destruiria a rastreabilidade.
- Não escreves no `articles_final.xlsx`, não fazes commits.
- Trabalha em subdirectório próprio do scratchpad e não reaproveites nada do que lá esteja.
