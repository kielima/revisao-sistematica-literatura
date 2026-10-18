---
name: skills-visiveis-no-menu-e-ponte-nuvem-local
description: "Skills criadas na nuvem só aparecem no / do app se estiverem no clone local ou instaladas no perfil (.skill); ponte nuvem→local só por cartão de tarefa; modo Aceitar edições evita mensagens retidas"
metadata:
  node_type: memory
  type: feedback
---
Aprendido em 2026-10-18 (sessão Metanálise na nuvem + sessões locais no Claude Desktop da Kiê).

**Skills no menu `/`**
- Uma skill escrita em `.claude/skills/<nome>/SKILL.md` numa sessão na nuvem fica só na branch do PR. O menu `/` do app lê o clone local, por isso ela NÃO aparece até haver merge e atualização do clone.
- Solução que funcionou: empacotar com `python -m scripts.package_skill` (skill-creator), entregar o `.skill` com SendUserFile e a Kiê instala no perfil («Guardar skill»). Depois apareceu no `/`. Uma skill nova pode só aparecer em sessões novas.
- Criar skills com `anthropic-skills:skill-creator` (validação `quick_validate`, descrição «pushy»), não à mão.
- Skill atual: `dissertacao-tracked-changes` (passa o que sai da metanálise para o Word da dissertação em tracked changes; registo em `dissertacao/EDICOES_DISSERTACAO.md`).

**Ponte nuvem ↔ sessão local**
- Nuvem → local: NÃO há envio direto (`cannot message other sessions yet`; ListAgents não lista as locais). O único caminho é `spawn_task`: cartão que a Kiê inicia na máquina dela e que abre uma sessão NOVA (nunca continua uma existente; o cartão iniciado já não se pode retirar com `dismiss_task`).
- Local → nuvem funciona via SendMessage com o ID da sessão na nuvem (no prompt do cartão). A mensagem fica retida se o modo de permissão for diferente; com o padrão «Aceitar edições» (bypass desativado nas definições do app) chega sem retenção.
- Eu não escolho o modo da sessão nova; vem das definições do app.
- Nada é dado como aplicado na dissertação sem resposta da sessão local ou confirmação da Kiê. Feedback à Anthropic sobre isto já foi enviado pela Kiê (`FEEDBACK_ANTHROPIC_MENSAGENS_ENTRE_SESSOES.md`).

**Testes 3 e 4 (2026-10-18) — sessões locais entre si e arquivamento**
- Teste 3: mensagens para sessões locais ficaram retidas (modo diferente) e nenhuma respondeu por SendMessage; três arquivadas mesmo assim por outra via.
- Teste 4 (sessão em «Aceitar edições»): 3 mensagens entregues e respondidas sem retenção; as sessões antigas responderam só em texto no chat; concluídas foram arquivadas pela sessão local (que tem ferramenta de arquivar).
- Endereçamento: enviar à sessão na nuvem pelo ID `session_...` falhou («No agent named … is reachable»); pelo NOME da sessão («Metanálise») funcionou. Usar o nome nos prompts dos cartões.
- Resultado da edição de teste: 3 tracked changes na Introdução do `DISSERTAÇÃO_KIÊ_v20.docx` (relato da sessão local; Kiê confirma no Word). A cópia `_TESTE_TRACKED` foi um engano do 1.º cartão e pode ser apagada.
