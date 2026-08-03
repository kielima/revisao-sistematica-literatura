---
titulo: Como Contornamos o Bloqueio do MDPI com Chrome CDP
descricao: Documentação técnica da solução usada para bypass do Akamai Bot Manager no download automático de PDFs do MDPI via Chrome DevTools Protocol
tags: [academico-e-pesquisa, revisao-sistematica, tecnologia-da-informacao]
status: revisado
ultima_atualizacao: 2026-05-27
---

# Como contornamos o bloqueio do MDPI com Chrome CDP

## O problema: Akamai Bot Manager

O MDPI usa o **Akamai Bot Manager**, uma das proteções anti-automação mais sofisticadas da web. Quando um script tenta baixar um PDF diretamente, o Akamai responde com `403 Forbidden` antes mesmo de chegar ao servidor do MDPI.

### Por que scripts normais falham

Um pedido HTTP normal feito por Python (`requests`) ou PowerShell (`Invoke-WebRequest`) tem características que o Akamai reconhece imediatamente como automação:

| Característica | Script normal | Browser real |
|---|---|---|
| Headers HTTP | Mínimos e genéricos | Dezenas de headers específicos do browser |
| TLS fingerprint | Biblioteca Python/PowerShell | Fingerprint do Chrome/Firefox |
| JavaScript | Não executa | Executa completamente |
| Cookies de sessão | Ausentes ou fabricados | Gerados pelo próprio Chrome |
| Tempo de resposta | Milissegundos exatos | Variação humana |
| Canvas/WebGL | Não existe | Renderização real da GPU |

O Akamai analisa **tudo isso em conjunto** e gera um "bot score". Se o score passar de um limiar, bloqueia com 403.

Mesmo com `User-Agent: Mozilla/5.0...` e cookies copiados, o Akamai detecta a diferença no **TLS handshake** (o "aperto de mão" criptográfico inicial). Python usa uma biblioteca TLS diferente do Chrome, e essa diferença é suficiente para identificar automação.

---

## A solução: Chrome DevTools Protocol (CDP)

O **CDP** é uma interface de depuração que o Google Chrome expõe internamente — é o mesmo mecanismo que as DevTools usam quando você pressiona F12. Em vez de simular um browser, controlamos o **Chrome real** diretamente.

```
[Script Python no sandbox Linux]
        |
        | WebSocket (porta 9222)
        v
[Chrome real no Windows — já aberto, com sessão, cookies, GPU]
        |
        | HTTPS (browser real, TLS real, fingerprint real)
        v
[Servidores do MDPI / Akamai]
```

### Como funciona na prática

#### 1. Ativar o modo de depuração no Chrome

O Chrome foi iniciado com a flag `--remote-debugging-port=9222`, que abre um WebSocket local:

```powershell
Start-Process "chrome.exe" --remote-debugging-port=9222 --remote-allow-origins=*
```

#### 2. Conectar ao Chrome via WebSocket

O script Python liga-se ao Chrome como se fosse as DevTools:

```python
import websocket, json, requests

# Descobrir qual tab está aberta
tabs = requests.get("http://localhost:9222/json").json()
ws_url = tabs[0]["webSocketDebuggerUrl"]

ws = websocket.create_connection(ws_url)
```

#### 3. Navegar para o URL do PDF

O script envia um comando CDP para o Chrome navegar ao URL:

```python
def send(ws, method, params={}):
    cmd = json.dumps({"id": 1, "method": method, "params": params})
    ws.send(cmd)
    return json.loads(ws.recv())

# Navegar ao PDF do MDPI
send(ws, "Page.navigate", {"url": "https://www.mdpi.com/2073-4395/12/3/581/pdf"})
```

#### 4. Interceptar o conteúdo da resposta

Em vez de deixar o Chrome guardar o ficheiro na pasta Downloads (o que criaria problemas de renomeação), usamos `Network.getResponseBody` para capturar o PDF diretamente como base64:

```python
# Ativar monitorização de rede
send(ws, "Network.enable")

# Quando a navegação terminar, capturar o corpo da resposta
send(ws, "Page.navigate", {"url": pdf_url})

# Aguardar evento de carregamento
while True:
    msg = json.loads(ws.recv())
    if msg.get("method") == "Network.loadingFinished":
        request_id = msg["params"]["requestId"]
        break

# Obter o conteúdo em base64
response = send(ws, "Network.getResponseBody", {"requestId": request_id})
pdf_bytes = base64.b64decode(response["result"]["body"])

# Guardar com o nome correto
with open("CZUBASZEK et al., 2022.pdf", "wb") as f:
    f.write(pdf_bytes)
```

Do ponto de vista do Akamai, **foi o Chrome que fez o pedido** — com o TLS fingerprint correto, os cookies de sessão reais, o User-Agent autêntico e todos os headers exatos que o Chrome enviaria. Não há forma de distinguir isso de um utilizador a clicar "Download PDF".

---

## Por que este método é robusto

- **TLS fingerprint real**: O Chrome usa o seu próprio motor TLS (BoringSSL), impossível de replicar por fora.
- **Cookies de sessão**: Qualquer cookie que o Chrome tenha acumulado (incluindo cookies de consentimento GDPR, sessões anteriores, etc.) está disponível automaticamente.
- **JavaScript executado**: O Akamai injeta JavaScript para medir comportamento. Como estamos no Chrome real, esse JS executa normalmente e retorna resultados "humanos".
- **Sem processo separado**: Não há nenhum "robot browser" a abrir janelas — usamos a instância do Chrome que já está aberta no computador.

---

## Limitações

Este método **não** contorna:
- **Paywalls reais** (Elsevier, Wiley sem acesso institucional) — o conteúdo simplesmente não está disponível, independentemente do método.
- **CAPTCHAs manuais** — se o site pedir ao utilizador para resolver um puzzle.
- **Rate limiting agressivo** — se o MDPI detetar muitos pedidos seguidos do mesmo IP, pode bloquear temporariamente. Por isso usamos um delay de ~2s entre pedidos.

---

## Implicações para a dissertação

Esta abordagem foi usada exclusivamente para **artigos em acesso aberto** (open access), onde o PDF é legalmente gratuito mas o publisher bloqueia automação para forçar o uso do site. O conteúdo foi identificado via **Unpaywall API** (`api.unpaywall.org`), que certifica que cada artigo tem licença OA. Não foram contornados paywalls.

Para registar na seção de métodos da RSL: *"Os PDFs dos artigos classificados como open access via Unpaywall foram recuperados programaticamente através do Chrome DevTools Protocol (CDP), que permite automação do browser real sem simular agentes HTTP, contornando restrições de acesso automatizado mantidas pelos publishers para conteúdo legalmente gratuito."*
