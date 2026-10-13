# País do autor de correspondência — leitura do PDF (2026-10-13)

Pedido da Kiê (2026-10-13): mapa de publicações por país, contando **só o país do autor de correspondência**. Para 451 dos 521 artigos Elegíveis o país sai dos metadados (afiliação da Web of Science, BDTD = Brasil, Crossref). Faltam estes 70, cujos metadados não trazem afiliação: é preciso abrir o PDF.

## O que fazer, artigo a artigo

1. Abrir o PDF no Drive (pasta `1R63Q4Lzz6JRRLpwES1Ngyod04q0-r9YP`) pelo `fileId` do lote. Se o `fileId` for `null`, procurar `title = '<pdf>'` com `parentId` dessa pasta.
2. Confirmar título e primeiro autor na p.1. Se não baterem, registar `pdf_confere: false` e não preencher o país.
3. Bastam a primeira página e, se for preciso, a última página ou o rodapé. Procurar o **autor de correspondência**:
   - asterisco ou envelope junto ao nome, «Corresponding author», «Autor correspondente», «Correspondence to», e-mail de contacto;
   - em teses ou dissertações não há autor de correspondência: usar a instituição do autor (folha de rosto).
4. Registar o **país da afiliação desse autor** tal como está impresso.
   - Se o autor de correspondência tiver mais de uma afiliação, usar a primeira listada.
   - Se o PDF não marcar nenhum autor de correspondência, usar a afiliação do **primeiro autor** e dizer isso em `criterio`.
   - Se a afiliação impressa não tiver país (só cidade ou universidade), escrever o país a que a instituição pertence e dizer isso em `nota`.
5. Não inventar. Se não houver afiliação nenhuma no PDF, deixar `pais` vazio e explicar em `nota`.

## Saída

Ficheiro `lotes_paises/resultado_loteNN.json` (lista, um objecto por artigo):

```json
{"row_id": 0, "pdf_confere": true, "autor": "nome do autor usado", "criterio": "correspondencia | primeiro_autor | autor_tese",
 "afiliacao": "afiliação tal como impressa", "pais": "nome do país em português", "pagina": "p.1",
 "nota": ""}
```

## Segurança

- Nunca enviar email ou dados pessoais a serviços externos. Não usar Unpaywall, OpenAlex, Crossref nem outras APIs: só o conector do Google Drive e ferramentas locais.
- Ficheiros de trabalho no scratchpad, com o número do lote no nome; não reutilizar ficheiros que já lá estejam.
- Não alterar ficheiros do repositório, excepto escrever o `resultado_loteNN.json` pedido.
