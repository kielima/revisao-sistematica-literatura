# CO2 por etapa da EN 15804 (A1, A2, A3, A4) em todos os estudos da metanalise (F39, 2026-11-01)

Pedido da Kie (2026-11-01): «extrair separadamente o co2 de cada etapa da EN15804 de todos os estudos da metanalise,
uma coluna para cada etapa (A1, A2, A3 e A4)». Cada estudo do ficheiro `loteNN.json` tem `fileId` do PDF e `pares`
(linhas de `dados_fck`: `sheet_row`, `material`, `fck_mpa`, `co2_kg_m3` = valor total ja gravado, `co2_original`,
`co2_original_local`). Trabalhar **par a par**: cada mistura tem os seus valores.

## Definicao das etapas (EN 15804)
- **A1** extraccao e processamento das materias-primas (producao do cimento, agregados, adicoes, aditivos, agua, aco quando o par o inclui);
- **A2** transporte das materias-primas ate a central/fabrica de betao;
- **A3** fabrico do betao (dosagem, mistura, energia e consumiveis da central, cura em fabrica);
- **A4** transporte do betao da central ate a obra.
Nao incluir A5, B, C, D em nenhuma coluna (ficam em `nota` se o artigo as separar).

## O que gravar por par (todos em kg CO2-eq/m3 de betao, a MESMA base do `co2_kg_m3` — se o artigo publica noutra unidade, converter com a mesma regra usada em `co2_conversao` e dizer a conta; se nao for possivel converter sem assumir dados, deixar em branco e explicar)
- `co2_a1`, `co2_a2`, `co2_a3`, `co2_a4`: o valor da etapa **quando o artigo o publica** (tabela, figura com rotulos, texto). Em branco = nao publicado. **Zero so se o artigo disser que e zero ou que a etapa esta excluida** (nesse caso `0` e escrever «excluida» em `nota`).
- `co2_a1a3_agregado`: quando o artigo so da A1-A3 juntos (ou A1+A2, ou A2+A3) — escrever o valor e, em `nota`, quais etapas somam.
- `etapas_tipo`: `publicado` (valores lidos tal como impressos) | `lido_figura` (lido por pixel de barra sem rotulo numerico; dizer a incerteza em `nota`) | `derivado` (calculado por nos a partir de numeros impressos no artigo, ex.: soma dos materiais, total menos outra etapa, percentagem x total impresso, etapa agregada dividida pelo volume impresso; escrever a conta em `nota`) | `so_agregado` (so A1-A3 ou outra soma; pode combinar-se com `derivado` escrevendo `so_agregado+derivado`) | `nao_publicado`.
- `soma_confere`: comparar a soma das etapas (A1+A2+A3 e, se houver, +A4) com o `co2_kg_m3` do par: `sim` (diferenca <= 2%) | `nao` (dizer a diferenca e porque: valor gravado e com desconto, outra unidade funcional, outra fronteira, erro do artigo) | `n/a`. **Nao ajustar o valor gravado**; so assinalar.
- `local`: pagina + tabela/figura/seccao de onde saiu cada valor (formato «p.N, Tab./Fig./Sec.»).
- `citacao`: frase curta do artigo que prova (so se o valor nao e obvio na tabela).
- `nota`: tudo o que um leitor precisa para nao se enganar.

## Regras (a Kie decidiu «nao vamos assumir nada»)
1. So valores que o artigo imprime, ou calculos simples sobre numeros impressos (marcar `derivado`). **Nunca** usar factores externos (ecoinvent, ICE, EPDs) que o artigo nao publique, nem medias de outros estudos, nem estimar por percentagem lida a olho.
2. **Resultado por material nao e resultado por etapa.** Se o artigo so da o CO2 por componente (cimento, agregados, agua, aditivos), nao o atribuir a A1 sem o artigo dizer que e so producao dos materiais. Se o artigo o diz (ex.: «cradle-to-gate: producao dos materiais») e dá o transporte separado, a soma dos materiais e A1 (`derivado`). Caso contrario `nao_publicado` e descrever em `nota`.
3. Valor lido de figura so se a figura tem **rotulos numericos**; ler por pixel so quando a figura tem escala e as barras sao inequivocas (dizer em `nota`: «lido por pixel, +-X»). Renderizar a pagina como imagem e olhar (pymupdf, dpi >= 200); ver as figuras de fronteira e de contribuicao por etapa.
4. O par em `dados_fck` pode ser a mistura de referencia ou uma variante — confirmar pelo nome (`material`) e pelo `co2_kg_m3` que esta a ler a linha certa. Se o valor gravado nao bate com nenhum valor do artigo, assinalar em `nota` (`valor_gravado_nao_localizado`).
5. Cenarios com e sem desconto (carbonatacao, creditos, modulo D): usar as etapas do cenario **bruto**; se o artigo so da o liquido, dizer.
6. Se o artigo agrega etapas de forma diferente (ex.: «materials», «transport», «production») mapear so quando a correspondencia for explicita; senao `so_agregado`/`nao_publicado`.
7. `A4` so se for o transporte do betao a obra (nao o transporte de materias-primas, que e A2). Se o artigo nao rotula a coluna/segmento «transport» como A4 (ou como transporte do betao a obra), nao o atribuir a A4: fica em `nota`.
8. **Ambiguidade A2/A4** (ex.: «transportado ate ao local de uso» num estudo cradle-to-gate): deixar A2 e A4 em branco e descrever em `nota`.
9. **Unidade diferente do par** (ex.: valor por m3 de ligante, de biocompósito, por tonelada sem massa volumica impressa): nao converter; deixar em branco e escrever o valor na unidade original em `nota`.
10. **Contradicao dentro do artigo** (texto vs figura/tabela): seguir a tabela ou figura com rotulos, e dizer a contradicao em `nota`.

## Leitura
Ler o PDF **completo** (`mcp__Google_Drive__read_file_content`; se truncar (teses) ou falhar, `download_file_content` **um de cada vez, em serie** + `pdftotext -layout`/PyMuPDF; ficheiros que o Drive recusa («session expired», > 10 MB, ou que fazem cair a ligacao): usar `read_file_content`, pôr `figuras_vistas: false` e listar o estudo em `refazer_com_recorte: true` — a Kie/Claude relê depois as paginas das figuras com o `shrink-drive-pdf.yml` (first_page/last_page); nao tentar contornar). Confirmar titulo e primeiro autor. Ver as figuras e tabelas de resultados por etapa.

## Saida
`lotes_etapas/resultado_<nome do lote>.json` = lista de
`{"row_id":0,"pares":[{"sheet_row":0,"co2_a1":null,"co2_a2":null,"co2_a3":null,"co2_a4":null,"co2_a1a3_agregado":null,"etapas_tipo":"","soma_confere":"","local":"","citacao":"","nota":""}],"texto_completo_lido":true,"figuras_vistas":true,"refazer_com_recorte":false,"nota_estudo":""}`

Seguranca: nunca enviar email nem dados pessoais a servicos externos; sem APIs externas (Unpaywall, OpenAlex, Crossref...); so o conector do Drive e ferramentas locais. Os ficheiros `tool-results` sao partilhados entre lotes paralelos: confirmar titulo/autor antes de usar um texto; ficheiros de trabalho no scratchpad com o nome do lote. Nao tocar em `articles_final.xlsx`, `meta_analysis_base.xlsx` nem noutros ficheiros do repositorio; so escrever o JSON de resultado.
