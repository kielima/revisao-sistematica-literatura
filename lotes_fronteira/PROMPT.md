# Lotes da fronteira do sistema e do transporte (F37, 2026-10-18)

Pedido da Kie (2026-10-18): saber, em todos os estudos da metanalise, se o CO2 gravado (`co2_kg_m3`, A1-A3) ja inclui o
transporte dos materiais (matérias-primas até à central/fabrica) ou nao — para acrescentar o transporte A4
(fabrica -> obra) no grafico de parametrizacao sem contar o transporte duas vezes, e para usar isto como criterio de
qualidade. Para cada estudo de `lotes_fronteira/loteNN.json` (com `fileId`, `pares` = linhas de dados_fck):

1. Ler o PDF **completo** (`mcp__Google_Drive__read_file_content`; se truncar (teses) ou falhar, `download_file_content` + `pdftotext -layout`/PyMuPDF). Confirmar titulo e primeiro autor. **Ver as figuras** da fronteira do sistema (diagramas «system boundary»): renderizar essas paginas como imagem e olhar.
2. Responder, com base **so no que o artigo escreve** (nada de deduzir):
   - `fronteira`: `A1-A3` | `A1-A4` | `A1-A5` | `A1-A3+C+D` | `outra` | `nao_declarada` (usar o termo do artigo em `fronteira_texto`: cradle-to-gate, cradle-to-grave...).
   - `transporte_materiais_a1a3` (transporte das matérias-primas ao fabricante/central de betão, A2): `incluido` | `excluido` | `parcial` (dizer o que inclui) | `nao_declarado`.
   - `transporte_concreto_a4` (betao da central a obra): `incluido` | `excluido` | `nao_declarado`.
   - `transporte_dados`: distancias (km) dos materiais e do betao, modal, tipo/carga do camiao, factor de emissao usado — so se impressos.
   - `base_dados_processos`: processos/bases citados (ecoinvent «market for» inclui transporte, «production» nao — transcrever o nome do processo tal como no artigo, nao interpretar).
   - `por_par`: so se pares do mesmo estudo diferirem (ex.: cenarios com e sem transporte): lista `{sheet_row, ...mesmos campos}`.
   - `citacao`: pagina/tabela/figura + frase curta que prova cada resposta.
3. Se o artigo nao fala de transporte, `nao_declarado` (nao `excluido`).

Escrever `lotes_fronteira/resultado_loteNN.json` = lista de
`{"row_id":0,"fronteira":"","fronteira_texto":"","transporte_materiais_a1a3":"","transporte_materiais_nota":"","transporte_concreto_a4":"","transporte_dados":{"dist_materiais_km":null,"dist_betao_km":null,"modal":"","camiao":"","factor":""},"base_dados_processos":"","por_par":[],"citacao":"","texto_completo_lido":true,"nota":""}`.

Seguranca: nunca enviar email nem dados pessoais a servicos externos; sem APIs externas (Unpaywall, OpenAlex, Crossref...); so o conector do Drive e ferramentas locais. Os ficheiros `tool-results` sao partilhados entre lotes paralelos: confirmar titulo/autor antes de usar um texto; ficheiros de trabalho no scratchpad com o numero do lote no nome. PDFs que o Drive recusa («session expired», >10 MB): marcar `nao_lido` na nota e seguir. Nao alterar mais nenhum ficheiro do repositorio.
