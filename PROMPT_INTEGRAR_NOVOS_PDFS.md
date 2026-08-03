---
titulo: "PROMPT INTEGRAR NOVOS PDFS"
descricao: ""
tags: []
status: rascunho
ultima_atualizacao: 2026-06-04
---

# Prompt — Integrar novos PDFs baixados e actualizar planilha + HTML

> Usar este prompt no início de uma nova sessão de integração.

---

Veja os arquivos de suporte desse projeto e entenda como está sendo feito o processo de download dos PDFs, o banco de dados e o HTML dos downloads. Leia em especial: `CLAUDE.md`, `RSL_PROGRESSO.md` e `DOWNLOAD_LESSONS_LEARNED.md`.

Depois, execute as seguintes tarefas:

---

## Tarefa 1 — Integrar os PDFs em `NOVOS BAIXADOS MANUALMENTE`

A pasta de entrada é:
```
00_REFERENCIAS\ARTIGOS ACEITOS APÓS REMOÇÃO DAS DUPLICATAS\NOVOS BAIXADOS MANUALMENTE\
```

Para cada PDF nessa pasta:

1. Extrair o DOI do PDF (via pdfplumber, primeiras 2 páginas).
2. Fazer matching no banco `articles_final.xlsx` (coluna `doi`) — normalizar o DOI removendo prefixos `https://doi.org/` antes de comparar.
3. Se encontrar match:
   - Gerar o nome ABNT: `SOBRENOME et al., ANO.pdf` (ou `SOBRENOME, ANO.pdf` se autor único). Sem caracteres especiais: ç→c, ã→a, ł→l, š→s, etc.
   - Se houver conflito de nome (dois artigos com mesmo sobrenome+ano), usar sufixos `a`, `b`, `c`.
   - **Mover** o PDF para `00_REFERENCIAS\ARTIGOS ACEITOS APÓS REMOÇÃO DAS DUPLICATAS\` com o nome ABNT.
   - Actualizar a coluna `pdf` no Excel: valor da célula = nome do ficheiro ABNT + hyperlink `file:///` apontando para o caminho completo. Remover fundo amarelo da célula.
4. Se **não** encontrar match por DOI, tentar por título normalizado (lowercase, sem pontuação) e depois por autor + ano.
5. Se ainda sem match: **MOVER** para `NOVOS BAIXADOS MANUALMENTE\PARA VERIFICAR\` e reportar quais foram movidos com os dados extraídos (DOI, título, autor). **NUNCA apagar sem confirmação explícita.**

### ⚠️ Regra crítica sobre duplicados

- Se o PDF corresponder a uma linha com `status_triagem = 'Duplicado'` **ou** se já existir um ficheiro com o mesmo nome ABNT na pasta de destino: **NÃO apagar**. Integrar normalmente e **reportar** quais são os casos duplicados no final.
- Nunca apagar qualquer ficheiro sem autorização explícita.

---

## Tarefa 2 — Verificar marcações "sem acesso" no HTML (opcional)

Se houver um ficheiro `rsl_dl.json` na raiz da pasta RSL (exportado pelo botão "Exportar JSON" do `DOWNLOAD_MANUAL.html`):

- Ler os itens com `"unavail": true`.
- Para cada um, localizar no banco `articles_final.xlsx` e actualizar `status_triagem` → `"Sem acesso"` (apenas linhas com status `Elegível` ou `Inconclusivo`; não alterar linhas `Duplicado`).
- ⚠️ Se algum item estava marcado como `unavail` mas o PDF foi integrado nesta sessão, **não** alterar o status — o PDF existe, não é sem acesso.
- Reportar quais eram `Elegível` antes de serem marcados como `Sem acesso` (impacto PRISMA).

---

## Tarefa 3 — Regenerar o `DOWNLOAD_MANUAL.html`

Após actualizar o Excel, regenerar o `DOWNLOAD_MANUAL.html` com:

- Apenas artigos com `status_triagem` ∈ `{Elegível, Inconclusivo}` **e** sem ficheiro na coluna `pdf` (ou com URL na coluna `pdf`, não nome de ficheiro).
- Excluir artigos com `status_triagem = 'Sem acesso'`.
- Para cada linha, gerar dois links:
  - **CAPES** (vermelho): `https://doi-org.ez128.periodicos.capes.gov.br/{doi}` — link proxiado validado.
  - **DOI** (azul): `https://doi.org/{doi}` — fallback directo.
  - **URL extra** (cinza): coluna `url` do banco, se disponível (handle, Scopus, etc.).
- Manter checkboxes, filtros (Todos / Pendentes / Elegíveis / Baixados / Sem acesso) e botão "Exportar JSON".
- O estado anterior (checkboxes marcados) é preservado via `localStorage` com chave `rsl_dl_state_v4`.

---

## Relatório final esperado

Ao concluir, reportar:

| Item | Valor |
|------|-------|
| PDFs integrados com sucesso | N |
| PDFs movidos para PARA VERIFICAR (sem match) | N |
| Duplicados encontrados (não apagados) | lista |
| Linhas Excel actualizadas | N |
| Artigos marcados como Sem acesso | N (incluir quais eram Elegível) |
| Pendentes no novo HTML | N (Elegível: X, Inconclusivo: Y) |
