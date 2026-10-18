---
name: dissertacao-tracked-changes
description: Passa para o texto da dissertação da Kiê (Word, na máquina local) o que se decide ou calcula na metanálise, como alterações controladas (tracked changes) no ficheiro original. Usar sempre que uma decisão, resultado, número, método ou figura da metanálise afetar o texto da dissertação — ou quando a Kiê pedir "passa isto para a dissertação".
---

# Dissertação: edição direta com tracked changes

Objetivo (Kiê, 2026-10-18): tudo o que se faz na metanálise vai sendo escrito no ficheiro da dissertação, para não sobrar trabalho de escrita no fim.

## O que se pode e não se pode fazer
- A sessão na nuvem **não alcança** o ficheiro: ele vive na máquina Windows da Kiê. Não tentar editar nem procurar o .docx aqui.
- A ponte é um **cartão de tarefa** (`spawn_task`) que a Kiê inicia **na máquina dela**; abre uma sessão local, que edita o Word. Eu não posso iniciar o cartão nem escolher o modo da sessão nova (o padrão dela é «Aceitar edições», que é o que evita a retenção das mensagens).
- A sessão local responde a esta sessão com `SendMessage` (funciona local → nuvem; nuvem → local não funciona). Se a resposta ficar retida, o modo de permissão difere: a Kiê põe a sessão local em «Aceitar edições» e pede o reenvio.

## Regras de edição (fixas)
1. Ficheiro: pasta `C:\Users\ttibu\Documents\03_PROFISSIONAL\PESQUISA\MINHAS_PRODUÇÕES\04_DISSERTAÇÃO\02_DOCUMENTO_PRINCIPAL`. O documento principal é a versão mais recente `DISSERTAÇÃO_KIÊ_vNN.docx` (em 2026-10-18: v20); a sessão local confirma qual é, e pergunta se houver dúvida.
2. Editar **diretamente o original**, **sem criar cópias**. Tudo em **tracked changes**, autor «Claude», com um comentário curto a justificar e à origem do dado (ex.: «F33, DECISOES_METANALISE.md»). Nunca escrever texto sem controlo de alterações e nunca aceitar/rejeitar revisões existentes.
3. Usar as skills `docx` e `escrita científica`. Se uma não existir na máquina local, avisar e seguir com a outra.
4. Verificar antes de guardar que o Word não tem o ficheiro aberto em conflito; depois, validar que as revisões aparecem e que o resto ficou intacto (parágrafos, tabelas, figuras).
5. Localizar o sítio certo no texto (capítulo/secção) pelo conteúdo. Se não houver secção óbvia, **não inventar**: propor o local na resposta e esperar a Kiê.
6. Texto novo no registo da dissertação: português, impessoal, voz académica, números com a mesma precisão e unidades da fonte; nada que não esteja nos dados. Sinalizar «por confirmar» o que ainda não foi validado.

## Fluxo (cada vez que a metanálise produz algo escrevível)
1. Fechar e registar a decisão como de costume (`metanalise/DECISOES_METANALISE.md`, CLAUDE.md).
2. Escrever o **pedido de edição** em `dissertacao/EDICOES_DISSERTACAO.md` (id E-nnn, data, origem, secção alvo, texto proposto com números exatos, estado `pendente`).
3. **Juntar em lote** os pedidos pendentes (um cartão por sessão de trabalho, não por mudança pequena) e criar o cartão com `spawn_task`. O prompt tem de ser autónomo: contexto da dissertação, as regras de edição acima, os pedidos E-nnn com o texto completo, o ID desta sessão para a resposta, e o pedido «responde com SendMessage; se falhar, copia o erro e a mensagem para o chat».
4. Dizer à Kiê, em texto corrido, que o cartão está pronto e que o inicie na máquina dela.
5. Quando a resposta chegar, marcar os E-nnn como `aplicado (tracked, data)` ou `por resolver (motivo)` no registo. Se não chegar, perguntar à Kiê; não assumir que foi aplicado.

## O que nunca fazer
- Dar uma edição por aplicada sem resposta da sessão local ou confirmação da Kiê.
- Enviar o conteúdo da dissertação ou o email da Kiê a serviços externos.
- Editar outros ficheiros da pasta da dissertação além do principal.
