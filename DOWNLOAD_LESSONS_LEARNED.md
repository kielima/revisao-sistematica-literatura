---
titulo: Lições Aprendidas — Download de PDFs da RSL
descricao: Documentação de lições aprendidas no processo de download de PDFs via acesso institucional PUC-Campinas / Portal Periódicos CAPES
tags: [academico-e-pesquisa, revisao-sistematica, tecnologia-da-informacao]
status: em-andamento
ultima_atualizacao: 2026-06-01
---

# Lições Aprendidas — Download de PDFs da RSL

**Última atualização:** 2026-06-05 (conclusão do processo)
**Contexto:** Download de PDFs via acesso institucional PUC-Campinas / Portal Periódicos CAPES.
**Status:** ✅ PROCESSO CONCLUÍDO — todos os 480 Elegíveis têm PDF vinculado em `articles_final.xlsx`.

---

## 1. Infraestrutura CAPES

- **Domínio proxy:** `ez128.periodicos.capes.gov.br`
- **Autenticação:** CAFe (Comunidade Acadêmica Federada)
- **URL proxied:** substituir `publisher.com` → `publisher-com.ez128.periodicos.capes.gov.br`
  - Elsevier: `www-sciencedirect-com.ez128.periodicos.capes.gov.br`
  - Springer: `link-springer-com.ez128.periodicos.capes.gov.br`
  - Wiley: `onlinelibrary-wiley-com.ez128.periodicos.capes.gov.br`
- **Confirmação de acesso:** "Você está acessando esse portal por: PUC-CAMPINAS"

---

## ⛔ REGRA CRÍTICA — NUNCA USAR PYTHON/SERVIDOR PARA O QUE FUNCIONA NO BROWSER

Se um publisher retorna 403 via Python → **não tentar outras abordagens Python**. Abrir o link no Chrome e usar o workflow do browser (Navigate → Snapshot → clicar download → Salvar).

O CDN bloqueia IPs de datacenter. O browser funciona porque tem cookies de sessão, proxy CAPES ativo e IP de usuário real.

| Publisher | O que fazer |
|-----------|-------------|
| Hindawi (10.1155) | OA — abrir `downloads.hindawi.com/...` no Chrome direto |
| MDPI (10.3390) | OA — abrir `mdpi.com/.../pdf` no Chrome direto |
| ACS (10.1021) | OA via Unpaywall — abrir URL OA no Chrome |
| SAGE (10.1177) | OA → Chrome direto; institucional → proxy CAPES no Chrome |
| PNAS (10.1073) | OA — abrir URL OA no Chrome direto |
| Wiley (10.1002/10.1111) | Proxy CAPES no Chrome: `onlinelibrary-wiley-com.ez128.periodicos.capes.gov.br/doi/{doi}` |
| T&F / ASCE | Proxy CAPES no Chrome |

---

## 2. Por Publisher

### ✅ Elsevier/ScienceDirect (10.1016) — WORKFLOW PRINCIPAL

**Estado:** Limite diário ~20-25 artigos/dia. Reset à meia-noite local.
**Popup de limite:** "You have reached the daily bulk download limit" — pressionar Escape para fechar.
**Pasta de destino:** Chrome lembra a última pasta salva → aponta automaticamente para `NOVOS BAIXADOS MANUALMENTE`.
**Nome do arquivo:** Diálogo mostra `1-s2.0-{PII}-main` por padrão — substituir pelo nome correto.

**Resolução DOI → PII (PowerShell):**
```powershell
$r = [System.Net.WebRequest]::Create("https://doi.org/$doi")
$r.AllowAutoRedirect = $true
$resp = $r.GetResponse()
$pii = [regex]::Match($resp.ResponseUri, '/pii/(S\w+)').Groups[1].Value
$resp.Close()
```

**⚠️ O que NÃO funciona:**
- `fetch()` via JavaScript → Cloudflare intercepta, retorna HTML
- Ctrl+S → salva HTML wrapper (64 KB), não o PDF binário
- Download da URL S3 via Python/PowerShell → 403 (restrição de IP)
- Chrome MCP em domínio `*.ez128.periodicos.capes.gov.br` → "Permission denied" (sem hostPermissions)

---

### ✅ Springer (10.1007) — FUNCIONA VIA PYTHON

```python
doi = '10.1007/...'
url = f'https://link-springer-com.ez128.periodicos.capes.gov.br/content/pdf/{doi}.pdf'
# fetch + salvar blob
```
Batch de até 8 por chamada de 45s.

---

### ✅ IOP Science — FUNCIONA VIA PYTHON (quirk no Accept)

```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Accept': 'text/html,*/*',   # ← OBRIGATÓRIO: NÃO usar 'application/pdf'!
    'Referer': 'https://iopscience.iop.org/'
}
url = f'https://iopscience.iop.org/article/{doi}/pdf'
```
Batch máximo 8 por chamada (400 KB–4 MB cada).

---

### ✅ Repositórios BR (USP, UnB, UFRGS, PUC-RS etc.)

```python
html = requests.get(handle_url, headers={'User-Agent': '...'}).text
pdf_links = re.findall(r'href="([^"]*bitstream[^"]*\.pdf[^"]*)"', html)
```

---

### ✅ SciELO / J-STAGE — GET direto com User-Agent de browser

- SciELO: `https://www.scielo.br/j/{journal}/a/{id}/?lang=pt&format=pdf`
- J-STAGE: `https://www.jstage.jst.go.jp/article/{pub}/{vol}/{issue}/{art}/_pdf`

---

### ❌ Wiley — CLOUDFLARE (browser manual)

Cloudflare bloqueia automação. Download manual no Chrome com proxy CAPES.

### ❌ MDPI — CLOUDFLARE NO SERVIDOR (browser manual)

OA mas CDN bloqueia IPs de servidor. Download manual no Chrome direto.

### ❌ IWA Publishing — 403 FORBIDDEN

Sem autenticação institucional acessível.

---

## 3. Workflow Elsevier — Validado (Sessão 10)

**Pré-requisito:** CAPES logado no Chrome. Chrome em janela primária.

### Foco do Chrome (obrigatório antes de qualquer ação)

```powershell
Add-Type @"
using System.Runtime.InteropServices;
public class WF {
    [DllImport("user32.dll")] public static extern bool ShowWindow(IntPtr h, int n);
    [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr h);
}
public class MC {
    [DllImport("user32.dll")] public static extern bool SetCursorPos(int x, int y);
    [DllImport("user32.dll")] public static extern void mouse_event(int f, int x, int y, int d, int e);
}
"@
$h = (Get-Process chrome | Where-Object {$_.MainWindowHandle -ne [IntPtr]::Zero} | Sort-Object MainWindowHandle | Select-Object -Last 1).MainWindowHandle
[WF]::ShowWindow($h, 9) | Out-Null         # SW_RESTORE
Start-Sleep -Milliseconds 200
[WF]::SetForegroundWindow($h) | Out-Null
Start-Sleep -Milliseconds 500
[MC]::SetCursorPos(875, 63) | Out-Null     # Barra de endereço — garante foco real
Start-Sleep -Milliseconds 150
[MC]::mouse_event(2, 0, 0, 0, 0)           # LEFTDOWN
Start-Sleep -Milliseconds 100
[MC]::mouse_event(4, 0, 0, 0, 0)           # LEFTUP
```

**⚠️ CRÍTICO — flags de mouse_event:**
- `2` = MOUSEEVENTF_LEFTDOWN
- `4` = MOUSEEVENTF_LEFTUP
- `1` = MOUSEEVENTF_MOVE relativo → **NÃO USAR para posicionamento absoluto**
- Sempre usar `SetCursorPos(x, y)` antes de `mouse_event(2/4)`.

### Passos por artigo

```
1. [Foco Chrome conforme acima]

2. Windows MCP Snapshot → obter label da barra de endereço
   (label 14 com 2 abas; label 16/18/22 com mais abas)

3. Windows MCP Type(label=<addr_bar>, text=URL_CAPES, clear=True, press_enter=True)
   URL: https://doi-org.ez128.periodicos.capes.gov.br/{doi}
   (redirect aceito mesmo que o destino CAPES não seja navegável direto)

4. Wait 5s

5. Windows MCP Snapshot → encontrar label do "View PDF"
   Extração: $c -split '\\n' | Where-Object { $_ -match 'Link\|View PDF\. Opens in a new window' }
   
6. Windows MCP Click(label=<view_pdf>) → nova aba PDF abre

7. Wait 4s

8. PowerShell: SetCursorPos(1816, 115) + mouse_event(2) + mouse_event(4)
   ← "Baixar" SEMPRE em (1816, 115) no PDF viewer — 100% fixo

9. Wait 2.5s

10. Windows MCP Snapshot → confirma dialog aberto
    label 17 = campo Nome: (SEMPRE quando dialog está aberto)
    Extração Salvar: $c -split '\\n' | Where-Object { $_ -match '\|Salvar como\|Bot.*\|Salvar\|' }

11. Windows MCP Type(label=17, text="AUTOR et al., ANO.pdf", clear=True)
    ← NÃO clicar no campo Nome antes de digitar (fecha/desestabiliza o dialog)
    ← NÃO usar SendKeys para digitar o nome (falha com vírgulas e caracteres especiais)

12. Windows MCP Click(label=<SALVAR_LABEL>)
    Coords sempre ~(792, 848)

13. Wait 2s

14. Se aparecer "Confirmar Salvar como":
    SetCursorPos(1009, 526) + mouse_event(2/4)  ← "Sim" (focus fica em "Não" — clicar "Sim" explicitamente)
```

### Coordenadas fixas (monitor 1936×1048)

| Elemento | Coordenada | Obs |
|---------|-----------|-----|
| Barra de endereço Chrome | (875, 63) | label 14 com 2 abas |
| "Baixar" PDF viewer | (1816, 115) | SEMPRE — 100% fixo |
| Campo "Nome:" dialog | label 17 | quando dialog aberto |
| Botão "Salvar" dialog | ~(792, 848) | label varia |
| "Sim" (confirmar overwrite) | (1009, 526) | |

**⚠️ Coordenadas de screenshot ≠ coordenadas de tela.** Converter: `screen = screenshot × 1.33`. Sempre usar coordenadas de tela (Snapshot ou tabela acima) no PowerShell.

**"View PDF" NÃO tem coordenada fixa** — varia por layout. Sempre usar Snapshot para obter o label correto.

---

## 4. Re-login CAFe (sessão expirada)

**Como identificar:** URL `doi-org.ez128...` redireciona para `periodicos.capes.gov.br` (homepage) em vez do artigo.

```
1. Snapshot → confirmar página portal CAPES
2. Click(label=<Acesso CAFe button>)
3. Wait 500ms → Snapshot → Click(label=<Acesso CAFe link interno>)
4. Wait 4s → página CAFe com campo de busca
5. Click(label=<campo>) → digitar "PUC-CAMPINAS"
6. Wait 2s → Click(label=<opção PUC-CAMPINAS - PONTIFÍCIA...>)
7. Wait 500ms → Click(label=<Enviar>)
8. Wait 5s → popup PUC-Campinas com login/senha PRÉ-PREENCHIDOS
9. Click(label=<Entrar>)
10. Wait 5s → portal recarrega com "Você está acessando esse portal por: PUC-CAMPINAS"
```

---

## 5. Renomeação em Lote (arquivos PII)

Quando salvos com nome padrão `1-s2.0-S{PII}-main.pdf`:

```powershell
# Resolver DOIs → PIIs (paralelo, ~20s para 15 DOIs)
$jobs = $dois | ForEach-Object {
    $doi = $_
    Start-Job {
        $r = [System.Net.WebRequest]::Create("https://doi.org/$using:doi")
        $r.AllowAutoRedirect = $true
        $resp = $r.GetResponse()
        $pii = [regex]::Match($resp.ResponseUri, '/pii/(S\w+)').Groups[1].Value
        $resp.Close()
        @{doi=$using:doi; pii=$pii}
    }
}
$map = $jobs | Receive-Job -Wait

# Renomear
$map | ForEach-Object {
    $src = "...\1-s2.0-$($_.pii)-main.pdf"
    $dst = "...\AUTOR et al., ANO.pdf"
    Rename-Item $src $dst -Force
}
```

`pii_map.json` salvo na pasta RSL pode ser reutilizado entre sessões.

---

## 6. Estado Final (após sessão 05/06/2026) ✅ CONCLUÍDO

**Resultado:** Processo de download 100% concluído.

| Métrica | Valor |
|---------|-------|
| Elegíveis com PDF | **480 / 480** ✅ |
| Inconclusivos com PDF | **1.347** |
| Sem acesso (embargado/bloqueado) | **68** |
| PDFs na pasta destino | **1.798** |
| `DOWNLOAD_MANUAL.html` | Apagado |

### Causa raiz identificada — ciclo de re-download

O principal motivo pelo qual os mesmos arquivos eram baixados repetidamente:

1. **Arquivos Elsevier salvos com nome PII** (`1-s2.0-S...-main.pdf`) em vez do nome ABNT. A integração não renomeava automaticamente, deixando o link no Excel com URL em vez de filename.
2. **Excel actualizado em cópia temporária** (`articles_final_new_YYYYMMDD.xlsx`) em vez do `articles_final.xlsx` principal — a cópia ia para `02_ARQUIVOS ANTERORES` e os itens voltavam como pendentes.
3. **Regra actual (correcta):** a integração actualiza sempre o `articles_final.xlsx` directamente e renomeia os arquivos para ABNT antes de mover para a pasta destino.

### Nota sobre arquivos com acesso bloqueado

Servidores que bloqueiam IPs externos (datacenter e browser fora da rede deles):
- **koreascience.or.kr** (Korean journal) — bloqueia IPs externos mesmo para artigos OA; usar link KCI viewer: `https://www.kci.go.kr/kciportal/ci/sereArticleSearch/artiPreView.kci`
- **NDSL/KISTI** — bloqueia conexões remotas
- Repositórios com **acesso embargado** (ex: UEPB) — contatar autor ou aguardar fim do embargo

---

## 7. Ferramentas — Limites e Restrições

| Ferramenta | Limite / Comportamento |
|-----------|----------------------|
| Python sandbox | Timeout 45s; BATCH=8 recomendado; sem acesso a `C:\Users\ttibu\Downloads\` |
| Chrome MCP | Bloqueado em `*.ez128.periodicos.capes.gov.br` (sem hostPermissions) |
| Windows MCP | Funciona para Snapshot, Type, Click, FileSystem, PowerShell |
| Unpaywall API | `https://api.unpaywall.org/v2/{doi}?email=kly@sapo.pt` — ~8-10 req/45s |
| Elsevier | Limite diário ~20-25 downloads; reset à meia-noite local |
| MONITOR_DOWNLOADS.ps1 | Não existe — foi documentado mas nunca criado; integração feita manualmente via Claude/Cowork |
