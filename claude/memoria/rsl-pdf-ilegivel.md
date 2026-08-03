---
name: rsl-pdf-ilegivel
description: "Na RSL, nenhum PDF pode ficar ilegível; se a extração falhar, resolver (OCR/re-download) antes de classificar"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 765c97a3-90ca-4417-87d0-42553152c8a7
---

Na triagem da RSL, **nenhum PDF deve ficar ilegível** — não é aceitável classificar um artigo por título/metadados porque o PDF não pôde ser lido. Isso é considerado problema grave pela Kiê.

**Why:** classificar sem conseguir ler o PDF compromete a verificação (o PDF pode ser colisão/corrompido/conteúdo diferente do título) e a rastreabilidade da RSL.

**How to apply:** quando a extração com `pdfplumber` vier vazia, corrompida ou **cid-encoded** (texto sai como `(cid:NN)` — fonte embutida sem mapeamento Unicode), NÃO decidir pelo título. Resolver assim:
1. **OCR** — renderizar as páginas em imagem e rodar reconhecimento de texto (`pdf2image`/`pdftoppm` + `pytesseract`/`tesseract`). Resolve a maioria dos cid-encoded sem re-download.
2. Se o OCR falhar ou o arquivo estiver realmente corrompido → rebaixar uma versão limpa via CAPES (ScienceDirect ez128; ACS usar busca no Portal CAPES).
3. Registrar nos comments como foi lido (`[Validação PDF: lido por OCR]`).

PDFs cid-ilegíveis identificados em 2026-06-06 (resolver): 2888, 3351, 3641, 3633, 3721. Ver [[rsl-validacao-pdf-rejeitados]] e [[rsl-marcacao-R-vs-P]].
