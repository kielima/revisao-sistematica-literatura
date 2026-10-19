# Lotes de rastreio de citacoes (F35, 2026-10-17)

Pedido da Kie: todas as citacoes dos artigos da metanalise tem de entrar no mapa de citacoes. Estes lotes cobrem os
artigos sem lista de referencias no Crossref. Para cada artigo do lote (`lotes_citacoes/loteNN.json`, com `fileId`):

1. Ler o PDF **completo** (`mcp__Google_Drive__read_file_content`; se vier truncado (teses) ou falhar, `download_file_content`
   + `pdftotext -layout`/PyMuPDF; paginas escaneadas -> OCR local). Confirmar titulo e primeiro autor antes de seguir.
2. Localizar a lista de referencias (e as citacoes no corpo, quando a lista for por numeros).
3. **Ligacoes a estudos:** comparar cada referencia com `lotes_citacoes/ALVO_466.json` (os 466 Elegiveis: row_id, rotulo, ano, titulo).
   Registar so ligacoes em que titulo (ou autores + ano + revista) coincidem sem duvida; ano do citado <= ano do citante.
   Nao deduzir.
4. **Fontes externas:** bases de dados e inventarios (ecoinvent, KEITI, ICE, EPD, ...), relatorios institucionais,
   normas e softwares de ACV de onde vem o CO2 ou a resistencia/vida util usada. Para cada uma: nome completo, tipo
   (base_de_dados | relatorio | norma | software | epd), local no artigo (tabela/pagina/numero da referencia) e a frase.
   Mesma fonte em varios artigos -> usar o mesmo `id_fonte` curto em minusculas (ex.: `ecoinvent_3_8`, `keiti_lci`, `ice_v3`).
5. Escrever `lotes_citacoes/resultado_loteNN.json` = lista de
   `{"row_id":0,"lista_refs_encontrada":true,"n_refs":0,"ligacoes":[{"para":0,"citacao":"...","local":"..."}],
     "externas":[{"id_fonte":"","nome":"","tipo":"","local":"","citacao":""}],"nota":""}`.

Regras: nao inventar; seguranca: nunca enviar email nem dados pessoais a servicos externos, nao usar APIs externas
(Unpaywall, OpenAlex, Crossref...), so o conector do Drive e ferramentas locais. Ficheiros de trabalho no scratchpad com
o numero do lote no nome; os ficheiros de `tool-results` sao partilhados entre lotes paralelos - confirmar titulo/autor
antes de usar o texto. Nao alterar mais nenhum ficheiro do repositorio.
