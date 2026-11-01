# Releitura com recortes (F39, fase 1b)

Contexto: `lotes_etapas/PROMPT.md` (versão 2) define a extração do CO2 por etapa EN 15804 (A1–A4). Os estudos de `recorteNN.json ou recorteBNN.json` ficaram na 1ª passagem com `refazer_com_recorte: true` (PDF >10 MB ou ligação do conector caída; figuras não vistas). Cada entrada traz `nota_anterior` (o que faltou ver) e `pares` (sheet_row, co2 gravado).

Tarefa por estudo: 
1. Ler `nota_anterior` e o resultado anterior em `resultado_loteNN.json` (campo `resultado_anterior`) para o row_id.
2. Obter as páginas em falta: disparar o workflow `shrink-drive-pdf.yml` (mcp__github__actions_run_trigger, repo kielima/revisao-sistematica-literatura, ref main) com `source_file_id`=fileId, `drive_folder_id`=1R63Q4Lzz6JRRLpwES1Ngyod04q0-r9YP, `filename`="RECORTE_<row_id>_<n>.pdf", `pdfsettings`=/ebook, `first_page`/`last_page` das páginas das figuras/tabelas de resultados (descobrir o número da página pelo texto lido com read_file_content), aguardar (mcp__github__actions_get / actions_list), procurar o recorte no Drive com search_files e descarregá-lo com download_file_content (um de cada vez, em série). Renderizar as páginas como imagem (PyMuPDF, dpi 200) e olhar.
3. Aplicar as regras do PROMPT.md v2 (só valores impressos/rótulos legíveis; nunca factores externos; sem assumir nada). Actualizar apenas as etapas que as figuras trouxerem; manter o resto.
4. Escrever `lotes_etapas/recorte_resultadoNN.json` no mesmo esquema do PROMPT.md, só para os estudos do ficheiro, com `figuras_vistas` real e `refazer_com_recorte` false (true só se de novo impossível, com motivo). Não alterar mais nada. Não enviar dados pessoais da Kiê para serviços externos. Os recortes temporários do Drive: mover para o lixo depois de lidos.
Resposta final: máx. 6 linhas.
