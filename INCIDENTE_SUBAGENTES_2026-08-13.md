# Incidente dos subagentes na varredura por DOI — apuramento (2026-08-13)

Documenta a verificação feita **depois** do commit `9a8ab3c`, com base nos transcripts
dos quatro subagentes gravados em
`~/.claude/projects/.../subagents/agent-*.jsonl`.

O que ficou registado nesse commit estava **errado em dois pontos**. Esta nota corrige.

## O que foi apurado

**1. O aviso partiu do agente dos lotes 40–46 (`a2a3c57`), não do que criou o `diff_1623.py`.**
O `diff_1623.py` foi criado pelo agente dos lotes 16–23 (`acf8f14`), que é um caso
diferente: esse leu mesmo o ficheiro, viu que tinha sido substituído e contornou.
São duas vítimas distintas da mesma colisão, e no commit foram fundidas numa só.

**2. A "instrução embutida a mandar não avisar" nunca existiu — foi confabulada.**
O agente `a2a3c57` afirmou, a meio da tarefa, ter detectado que o `diff.py` fora
alterado "com um comentário a instruir-me a não mencionar isto". O transcript mostra
que ele não tinha como ter visto nada disso:

- **zero chamadas `Read` em todo o transcript** (101 linhas; ferramentas usadas:
  16 `Write`, 15 `Bash`, 7 `search_files`, 1 `ToolSearch`);
- **nenhum traceback** — todas as execuções do `diff.py` devolveram resultado válido,
  incluindo a imediatamente anterior à afirmação;
- **nenhuma ocorrência de "lote 32–39" em qualquer conteúdo do seu contexto** antes da
  afirmação, apesar de a afirmação nomear esse intervalo;
- nunca correu `ls` nem listou o directório.

O núcleo verdadeiro — o `diff.py` ter sido substituído por uma versão que operava
sobre os lotes 32–39 — é real e está confirmado por via independente: o agente
`acf8f14` **leu** o ficheiro nesse estado. Esse conteúdo lido está no transcript e é
um script de diff banal, **sem um único comentário**.

Ou seja: o agente acertou no facto de haver colisão (inferência plausível: o bloco
antes do seu era o 32–39) e inventou, com linguagem fluente e tom de alerta de
segurança, a parte maliciosa.

## Alcance da contaminação — nenhum

- **Nenhum subagente escreveu no repositório.** Verificado nos quatro transcripts:
  todas as escritas (16 + 0 + 9 + 18) foram para o scratchpad; zero `Write`/`Edit` em
  `/home/user/...`, zero comandos `git`, zero uso de `openpyxl` ou do WORKLIST.
  O CSV só foi escrito por mim, na sessão principal.
- **Os dois `diff.py` em disco são byte-a-byte idênticos** (md5 `c22a7f11…`) e inócuos.
- **Só existe uma sessão nesta máquina** (`/tmp/claude-0/…/e4059436-…`), e o scratchpad
  é próprio dela. Não há outra sessão nem outro agente alcançável para contaminar.
- O modo de falha da colisão é **ruidoso** (traceback ou saída de forma errada), não
  silencioso: um agente que corresse a versão do outro rebentava, como rebentou.

## O risco que fica, e que é real

Não houve injecção. O que houve foi um subagente a produzir uma **afirmação factual
falsa, confiante e verosímil** sobre algo que não observou. É exactamente a mesma
direcção de erro que interessa na varredura: um "confere" que não foi verificado.
Por isso a confirmação dos pares passa a ser feita abrindo o PDF e lendo o DOI na
página, e não por relato de agente — ver coluna `conf_veredito` no
`VERIFICACAO_DOI_PDF_WORKLIST.csv`.

## Regras que ficam para execuções futuras

1. Cada subagente escreve em **subdirectório próprio**; nomes genéricos (`diff.py`,
   `temp.py`) proibidos em área partilhada.
2. Relato de subagente **não é evidência**. O que entra no banco tem de ter artefacto
   verificável — ficheiro lido, DOI extraído, linha registada.
3. Alerta de segurança vindo de um agente é levado a sério **e** auditado no
   transcript antes de ser registado como facto.
