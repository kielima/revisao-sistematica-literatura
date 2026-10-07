# Verificação dos erros de valor de CO2 apontados pela releitura dos créditos (2026-10-07)

Pedido da Kiê (2026-10-07): «corrigir os valores de CO2 errados que a releitura encontrou». Os achados estão em `lotes_creditos/ACHADOS_2026-10-07.md`. Cada caso tem de ser confirmado pela leitura integral do PDF (texto + tabelas + figuras renderizadas) antes de se corrigir.

Para cada caso do lote:
1. Localizar o PDF no Google Drive (pasta `1R63Q4Lzz6JRRLpwES1Ngyod04q0-r9YP`; o `fileId` está em `DRIVE_FILEID_MAP.csv`, coluna `title` = nome do ficheiro). Ler o texto (`read_file_content`) e, quando o número está numa figura, descarregar (`download_file_content`) e renderizar as páginas com pymupdf a 200 dpi; guardar os PNG das páginas decisivas no scratchpad com nome `<sheet_row>_p<pagina>.png` e indicar o caminho.
2. Ver os valores gravados em `meta_analysis_base.xlsx`, aba `dados_fck` (linha = sheet_row; col 7 material, 8 fck, 13 observacoes, 34 co2_original, 35 local, 36 conversao, 37 co2_kg_m3, 44 com desconto).
3. Responder: o achado confirma-se? Qual o valor correcto de `co2_kg_m3` (bruto, kg CO2-eq/m3, para a mesma mistura do fck gravado) e, se houver, `co2_kg_m3_com_desconto`? Citação exacta (página, tabela/figura, frase) e a conta. Se o fck também estiver errado, dizê-lo. Se não houver valor válido, `NAO CONVERTIDO` com motivo.

Regras: não inventar; leitura por píxel só com eixo numérico e indicando-a; não alterar ficheiros do repositório.
Segurança: nunca enviar email ou dados pessoais a serviços externos; não usar Unpaywall nem APIs externas; só o conector do Google Drive e ferramentas locais. Se descarregar um PDF grande demais (>~6 MB falha), dizer e seguir com o texto.

Saída: escrever `<scratchpad>/correcoes_loteN.json` = lista de {sheet_row, row_id, autor, confirma (sim/nao/parcial), co2_kg_m3_correcto, co2_com_desconto_correcto, fck_correcto, citacao, conta, imagens:[...], nota} e devolver um resumo curto.
