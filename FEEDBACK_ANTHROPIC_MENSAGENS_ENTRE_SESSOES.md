# Feedback para a Anthropic — mensagens entre sessões (rascunho, 2026-10-18)

**Ainda NÃO enviado.** Rascunho para a Kiê rever e enviar (Claude Code: `/feedback`; ou suporte em support.claude.com).

## Resumo
Mensagens entre sessões funcionam só num sentido: sessão local → sessão na nuvem (claude.ai/code). De nuvem → local falha, mesmo com a sessão local ligada e a aceitar mensagens.

## O que se observou
- Sessão na nuvem «Metanálise» (Claude Code, ferramentas `ListAgents`/`SendMessage`) e sessão local no Claude Desktop «Teste de mensagem entre agentes» (`session_01T2sYmtdRLKLHzNwqibGwfA`, `environment_kind: bridge`, `cross_session_inbound` disponível, estado ligado).
- Local → nuvem: entrega com sucesso depois de a sessão local ficar em «Aceitar edições».
- Nuvem → local: `SendMessage` devolve `auth: this cloud session cannot message other sessions yet`; por nome: `No agent named … reachable`.
- `ListAgents` na sessão na nuvem não mostra a sessão local, mesmo a aparecer em `list_sessions` como ligada.

## Problemas
1. **Sem credencial de envio na nuvem:** a sessão na nuvem só consegue receber, não enviar. A documentação diz que as sessões na nuvem «podem receber», mas a interface sugere troca bidirecional.
2. **Sem descoberta dos pares locais:** `ListAgents` na nuvem não lista sessões locais do mesmo utilizador.
3. **Mensagens retidas por modo de permissão:** o remetente em modo «ignorar permissões» e o destinatário em «aceitar edições» → mensagem retida (hold). As sessões na nuvem do Desktop não têm os modos «ignorar permissões»/«manual», por isso o utilizador não consegue alinhar os modos.
4. **Desktop não mostra o diálogo de aprovação** (expira em 5 min), por isso a mensagem retida fica sem forma visível de a libertar.

## Pedido
- Envio nuvem → local (e nuvem → nuvem) com a mesma conta.
- `ListAgents` a listar as sessões locais/Remote Control do utilizador a partir da nuvem.
- Diálogo de aprovação visível no Desktop e aviso claro no remetente quando a mensagem fica retida e porquê.
- Regra de retenção que não dependa de modos que a sessão na nuvem não pode escolher.

Caso de uso: pesquisa (revisão sistemática) com uma sessão na nuvem a processar dados e outra local com acesso a ficheiros/PDFs da máquina.
