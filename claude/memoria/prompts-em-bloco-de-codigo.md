---
name: prompts-em-bloco-de-codigo
description: "Sempre que a Kiê pedir um prompt, entregá-lo dentro de um bloco de código (fenced), para aparecer o botão de copiar"
metadata:
  node_type: memory
  type: feedback
---
Pedido da Kiê em 2026-10-23: «sempre que eu pedir um prompt, entrega de uma forma que eu consiga copiar facilmente».

**Regra:** todo prompt (para Dispatch, sessão local, outro Claude, etc.) vai **inteiro dentro de um único bloco de código** (``` … ```) na própria resposta do chat, que mostra o botão de copiar. Nada de o entregar só como texto corrido, citação ou ficheiro anexo; o ficheiro no repositório pode existir também, mas o prompt tem de estar no chat em bloco de código. Não pôr texto meu dentro do bloco (explicações ficam fora, antes ou depois). Se o prompt tiver blocos de código dentro, usar uma cerca exterior maior (````).
