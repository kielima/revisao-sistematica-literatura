# Convenções da pasta REVISÃO SISTEMÁTICA DE LITERATURA

## Regra de arquivamento — backups e versões obsoletas

**Manter na raiz APENAS os arquivos ativos e mais atualizados.**

Sempre que surgir um arquivo obsoleto, backup, ou versão anterior, mover imediatamente para:

```
07_ANÁLISES DE DADOS/REVISÃO SISTEMÁTICA DE LITERATURA/02_ARQUIVOS ANTERORES/
```

### O que vai para 02_ARQUIVOS ANTERORES

- Backups automáticos gerados por scripts (`*_backup_*.xlsx`, `*_backup_*.csv`)
- Versões anteriores de planilhas (`articles_final_new.xlsx` → `articles_final_old.xlsx`)
- Arquivos corrompidos ou descartados
- Qualquer arquivo com sufixo `_old`, `_bak`, `_backup`, `_pre-*`, `_v[0-9]*` que não seja a versão corrente

### O que fica na raiz

| Arquivo | Descrição |
|---|---|
| `articles_final.xlsx` | Banco de triagem ativo (todas as 5.093 entradas, PDFs linkados) |
| `GRÁFICOS DA RSL.xlsx` | Gráficos da meta-análise |
| `BANCO DE DADOS DA RSL.xlsx` | Banco principal da RSL (já na pasta 02_ARQUIVOS ANTERORES — versão de trabalho migrou para o Excel do vault) |
| Scripts `.py` | Scripts de análise ativos |

### Convenção de nomenclatura ao arquivar

Ao mover, renomear descritivamente se necessário:
- `articles_final_new.xlsx` → `articles_final_old.xlsx` (arquivado em 2026-05-28)
- `*_backup_YYYYMMDD_HHMMSS.xlsx` → manter nome original

---

*Nota criada em 2026-05-28 para evitar confusão entre versões de arquivos.*

---

## Processo de download de PDFs — arquitetura em 4 camadas

> Documentado em 2026-06-02 após sessão de integração de PDFs manuais.

A pasta de destino de todos os PDFs é:
```
00_REFERENCIAS\ARTIGOS ACEITOS APÓS REMOÇÃO DAS DUPLICATAS\
```
O banco de triagem que regista os caminhos é `articles_final.xlsx`, coluna `pdf`.

---

### Camada 1 — Unpaywall automático (`download_pdfs_win.py`)

**Quando usar:** primeira execução; roda sem supervisão, processa todos os registros com `is_oa=true` no scan Unpaywall.

**Inputs:**
- `unpaywall_scan_results.json` — resultado do scan OA (gerado previamente)
- `articles_final_backup_*.xlsx` — versão de entrada do banco

**Checkpoint:** `download_checkpoint.json` — guarda `done`, `ok`, `fail`, `ok_rows`

**O que faz:** tenta descarregar o `pdf_url` de cada registo OA. Domínios bloqueados (Elsevier, Wiley, T&F, MDPI, ACS, ASCE…) são ignorados de imediato sem fazer pedido HTTP. Se o download tiver sucesso, grava o caminho completo na coluna `pdf` do Excel de saída e remove o fundo amarelo da célula.

**Outputs gerados:** `articles_final_new_YYYYMMDD_HHMMSS.xlsx` + `articles_final_backup_YYYYMMDD_HHMMSS.xlsx` (mover ambos para `02_ARQUIVOS ANTERORES/` após integrar).

---

### Camada 2 — MDPI via Chrome CDP (`mdpi_batch_dl.py` / `mdpi_resume.py`)

**Quando usar:** após Camada 1; para os artigos MDPI que ficaram pendentes (MDPI bloqueia automação simples com 403).

**Inputs:** `mdpi_todo.json` — lista de registos MDPI com campos `row`, `pdf_url`, `filename`

**Checkpoint:** `chrome_dl_checkpoint.json` — campos `processed`, `downloaded`, `failed`

**O que faz:** lança Chrome em modo depuração remota (CDP porta 9224 para `mdpi_batch_dl.py`, 9222 para `mdpi_resume.py`), injeta script anti-detecção, visita a página do artigo como warm-up, depois navega para o URL do PDF e aguarda o ficheiro em `C:\Temp\mdpi_dl\`. Após validar assinatura `%PDF`, move para a pasta de destino com o nome `filename` do `todo.json`.

**Diferença entre os dois scripts:** `mdpi_resume.py` é idêntico em lógica mas usa perfil Chrome diferente (`chrome_resume_profile`) — usar se o perfil principal ficar corrompido ou travar.

---

### Camada 3 — IOP Publishing + repositórios Handle (`iop_hdl_dl.py`)

**Quando usar:** para artigos IOP (10.1088) e artigos em repositórios institucionais com URL `hdl.handle.net/…`.

**Inputs:** `iop_todo.json` + `hdl_todo.json` — combinados internamente; campos `row`, `pdf_url`, `filename`, `_type` (`iop` ou `hdl`)

**Checkpoint:** `iop_hdl_checkpoint.json`

**Estratégias:**
- `dl_iop`: mesma lógica do MDPI — warm-up na página do artigo, depois navega para URL direto do PDF (CDP porta 9223).
- `dl_hdl`: navega ao handle (redireciona para repositório), executa JS para encontrar links com `.pdf` ou texto "PDF/Download/Full text", navega ao link encontrado e aguarda download.

---

### Camada 4 — Downloads manuais via CAPES / listas HTML

**Quando usar:** para Elsevier e quaisquer artigos que as camadas 1–3 não conseguiram.

**Ficheiros de apoio (na raiz da pasta RSL):**
- `ELSEVIER_DOWNLOAD.html` — lista clicável dos artigos Elsevier pendentes
- `DOWNLOAD_MANUAL.html` — lista de todos os outros artigos pendentes de download manual

Abrir no browser conectado ao proxy CAPES (VPN ou rede da instituição). Clicar nos DOIs e guardar os PDFs para a pasta `00_REFERENCIAS\ARTIGOS ACEITOS APÓS REMOÇÃO DAS DUPLICATAS\NOVOS BAIXADOS MANUALMENTE\` (ver abaixo).

---

### Integração de PDFs baixados manualmente

**Pasta de entrada:** `00_REFERENCIAS\ARTIGOS ACEITOS APÓS REMOÇÃO DAS DUPLICATAS\NOVOS BAIXADOS MANUALMENTE\`

**Regra:** após integração, a pasta deve ficar vazia — os ficheiros são **movidos** para o destino (não copiados). A pasta serve apenas como área de entrada temporária.

### ⚠️ REGRA CRÍTICA — NUNCA APAGAR FICHEIROS DE NOVOS BAIXADOS MANUALMENTE

> Adicionado em 2026-06-03 após incidente de deleção acidental de 44 PDFs.

**PROIBIDO:** apagar qualquer ficheiro de `NOVOS BAIXADOS MANUALMENTE` automaticamente, sem autorização explícita da Kiê, mesmo que não haja match no banco.

**O que fazer com ficheiros sem match:**
1. Tentar matching por DOI (extraído do PDF)
2. Se falhar: tentar matching por título, autor e ano (metadados do PDF via pypdf / crossref)
3. Se ainda sem match: **MOVER** para `NOVOS BAIXADOS MANUALMENTE\PARA VERIFICAR\` e **reportar** à Kiê quais foram movidos, com os dados encontrados (DOI extraído, título, autor)
4. **Nunca apagar** sem confirmação explícita

**Protocolo de matching correto (em ordem de prioridade):**
1. DOI exato no banco (`doi` column)
2. DOI limpo (remover sufixos de journal, corrigir ligaduras tipográficas)
3. DOI por prefixo (ex: `10.1016/j.jclepro.2019.1` → buscar `startswith`)
4. Título normalizado (lowercase, sem pontuação) — comparar com `title` column
5. Autor + ano + journal (combinação)
6. Se todos falharem → PARA VERIFICAR, nunca deletar

**Fluxo de integração:**

1. Renomear os PDFs para o padrão `SOBRENOME et al., ANO.pdf` (sem caracteres especiais: ç→c, ã→a, ł→l, š→s) — ver convenção em "Notas sobre nomenclatura" no `RSL_PROGRESSO.md`.
2. **Mover** para `00_REFERENCIAS\ARTIGOS ACEITOS APÓS REMOÇÃO DAS DUPLICATAS\`.
3. Abrir `articles_final.xlsx` e localizar a linha correspondente ao artigo (por DOI, título ou autor).
4. Na coluna `pdf`: **valor da célula = nome do ficheiro** (`SOBRENOME et al., ANO.pdf`) + **hyperlink = URI `file:///` apontando para o caminho completo**. NÃO preencher o caminho completo como texto — usar `cell.hyperlink` via openpyxl ou inserir hiperlink manual no Excel (Ctrl+K).
5. Remover o fundo amarelo da célula `pdf` se estiver marcada.
6. Re-gerar `DOWNLOAD_MANUAL.html` directamente (Claude faz isso, não há script standalone).

**Nota (2026-06-03):** os scripts de download automático (Camadas 1–3) foram removidos. O download é agora exclusivamente manual via `DOWNLOAD_MANUAL.html` + CAPES. O HTML é gerado directamente pelo Claude quando solicitado.

---

### Ficheiros de estado / checkpoint — referência rápida

| Ficheiro | Pertence a | Descrição |
|----------|-----------|-----------|
| `unpaywall_scan_results.json` | Camada 1 | Resultados do scan OA (input) |
| `download_checkpoint.json` | Camada 1 | Estado do download Unpaywall |
| `mdpi_todo.json` | Camada 2 | Lista de artigos MDPI pendentes |
| `chrome_dl_checkpoint.json` | Camada 2 | Estado do Chrome CDP (MDPI) |
| `iop_todo.json` | Camada 3 | Lista de artigos IOP pendentes |
| `hdl_todo.json` | Camada 3 | Lista de artigos Handle/repositório |
| `iop_hdl_checkpoint.json` | Camada 3 | Estado do Chrome CDP (IOP/hdl) |
| `ELSEVIER_DOWNLOAD.html` | Camada 4 | Lista clicável Elsevier pendentes |
| `DOWNLOAD_MANUAL.html` | Camada 4 | Lista clicável outros pendentes |

---

*Secção adicionada em 2026-06-02.*
