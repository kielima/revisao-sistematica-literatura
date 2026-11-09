---
titulo: Coordenação entre agentes no vault da RSL
descricao: Regras para vários agentes/sessões Claude trabalharem no mesmo repositório sem conflitos nem decisões duplicadas
tags: [academico-e-pesquisa, metodologia, governanca]
status: rascunho — por confirmar pela Kiê
ultima_atualizacao: 2026-11-09
---

# Coordenação entre agentes — vault REVISÃO SISTEMÁTICA DE LITERATURA

> **Ler antes de começar qualquer frente de trabalho.** Proposta de 2026-11-09 (pedido da Kiê: «um markdown centralizando todo o fluxo de operações entre diferentes agentes»). Tudo o que está marcado **«por confirmar»** é proposta minha, ainda sem decisão da Kiê.

## 1. Porque existe este ficheiro (o incidente que o motivou)

Medido a 2026-11-09: **dois agentes trabalhavam em paralelo na mesma frente (transporte A4) sem saberem um do outro.**

| | Sessão «Metanálise» (F40) | Agente da tarefa #0619 (F41–F43) |
|---|---|---|
| Ramo | `claude/f40-a4-extracao` (32 commits, **não** integrado no `main`) | `claude/rsl-619-*`, `claude/gifted-lovelace-dv478n` → `main` (#336–#338) |
| Selecção | 152 estudos com `a4_somavel=sim` (26 lotes + releituras) | 146 estudos com pares `indeterminado` (14 lotes, ainda sem resultados) |
| Pasta de trabalho | `lotes_a4/` | `lotes_transporte/` |
| Regra da massa volúmica | só impressa ou soma do traço; «não vamos assumir nada» | impressa > soma do traço > **2.400 kg/m³** como premissa nossa (F43, Kiê 09/11) |

**60 estudos estão nas duas listas** (leitura dupla dos mesmos PDFs) e as duas regras de massa volúmica divergem. Nenhum conflito de Git (pastas diferentes), mas trabalho duplicado e critérios incompatíveis — o tipo de erro que o Git **não** detecta (conflito semântico). Resolução em §7.

## 2. Princípios (e de onde vêm)

Resumo das pesquisas de 2026-11-09; as fontes são de blogues/fornecedores e preprints, **indicativas, não normativas**.

1. **Uma tarefa, um ramo, um agente, um clone.** Isolar o diretório de trabalho de cada agente evita sobrescritas ([Augment](https://augmentcode.com/guides/git-worktrees-parallel-ai-agent-execution), [DEV](https://dev.to/jsmanifest/parallel-ai-coding-with-git-worktrees-run-multiple-agents-without-conflicts-11na)). Aqui: cada sessão em nuvem tem o seu clone; **o ramo é a unidade de posse**.
2. **Dividir por fronteira de domínio, não por ficheiro** — evitar que dois agentes toquem nos mesmos ficheiros por ângulos diferentes ([Augment](https://www.augmentcode.com/guides/how-to-run-a-multi-agent-coding-workspace)). Aqui: cada frente tem a sua pasta `lotes_*/` e o seu `aplicar*.py`.
3. **Ficheiros-ponto-quente** (configuração, registos, migrações) são onde os conflitos nascem mesmo com tarefas independentes ([Verdent](https://www.verdent.ai/guides/answers/how-parallel-agents-avoid-codebase-conflicts)). Aqui: `meta_analysis_base.xlsx`, `articles_final.xlsx`, `DECISOES_METANALISE.md`, `CLAUDE.md`, `PROMPT_E2.md`.
4. **Reivindicar antes de editar** (claim de ficheiros/globs) ([Befall](https://mcpmarket.com/server/befall)). Aqui: o **registo de frentes** da §4.
5. **Um autor por transição de estado**: agentes-trabalhadores propõem, **um só escreve** no registo/estado partilhado ([taxonomia de falhas, Zartis](https://www.zartis.com/the-distributed-systems-playbook-for-multi-agent-ai/), relato em [Reddit](https://reddit.sentinel-team.org/posts/1t49k7p/snapshots/2026-05-08T19%3A17%3A52.632086Z) — anedótico). Aqui: **só o integrador escreve nos `.xlsx`** (§5).
6. **Escritas com verificação de versão** (compare-and-swap): só gravar se a versão lida ainda for a actual ([DEV](https://dev.to/mrvlad/the-write-your-agents-lost-and-why-nothing-errored-k1n)). Aqui: antes de gravar, `git fetch` e confirmar que o `.xlsx` não mudou no `main` nem em ramo aberto desde o clone.
7. **Falhas de passagem de testemunho** são a causa mais frequente: «entregue» confundido com «feito», dois agentes a repetir a mesma acção ([Zartis](https://www.zartis.com/the-distributed-systems-playbook-for-multi-agent-ai/), [CodeWave](https://codewave.com/insights/the-agent-harness/)). Aqui: o formato de entrega da §6 e o campo `texto_completo_lido`/`figuras_vistas` só `true` se verdadeiro.
8. **Binários não se fundem** (`.xlsx`): só bloqueio/posse única resolve; no Git simples o bloqueio é só convenção ([Git LFS locking](https://github.com/git-lfs/git-lfs/blob/prove/docs/proposals/locking.md)). Aqui: convenção da §5.
9. **Rastreabilidade**: cada acção liga a um identificador de tarefa ([Tian Pan](https://tianpan.co/blog/2025-10-14-why-multi-agent-llm-systems-fail)). Aqui: o **id da tarefa** (`#0619`, `#1583`…) e o **id F-nn** em todo commit e entrada de decisão.
10. **Limite prático de 2–3 sessões em paralelo por revisor** — o gargalo é a revisão humana ([MindStudio](https://www.mindstudio.ai/blog/parallel-agentic-development-git-worktrees/)). Aqui: **máx. 2 frentes de escrita em simultâneo** (por confirmar).

## 3. Mapa de posse (quem pode escrever o quê)

| Recurso | Dono (único escritor) | Os outros |
|---|---|---|
| `meta_analysis_base.xlsx` (`dados_fck`) | **Integrador** da frente activa (§5) | só entregam JSON + `aplicar*.py` |
| `articles_final.xlsx` | sessão da triagem/E2 em curso | idem |
| `metanalise/DECISOES_METANALISE.md` | cada frente acrescenta **só no fim**, com id F-nn reservado (§4) | não reescrever entradas alheias |
| `lotes_etapa2/PROMPT_E2.md` | sessão da E2 | só propõem regra nova |
| `CLAUDE.md` (resumo de estado) | **uma entrada por frente fechada**, no PR dessa frente | não editar entradas de outras frentes |
| `lotes_<frente>/` | agente da frente | só leitura |
| PDFs (Drive) | só Drive; escrita via `push-to-drive.yml` / `shrink-drive-pdf.yml`; recortes temporários → lixo no fim | nunca no repo (público, direitos de autor) |
| Dissertação (Word) | sessão local «Texto Dissertação» (skill `dissertacao-tracked-changes`) | pedem por `SendMessage`/tarefa, não editam |
| Supabase (tarefas #nnnn) | quem tem a tarefa; comentário ao fechar | não fechar tarefa alheia |
| Site (`kielima-site`) | repositório próprio, PRs próprios | — |

## 4. Registo de frentes activas (reservar ANTES de começar)

Regra: antes de uma frente nova, **ler esta tabela, correr o §8.1, e acrescentar uma linha por PR pequeno** (só este ficheiro). Se já houver linha para a mesma pasta/ficheiro/tema, **parar e perguntar à Kiê** quem fica com ela.

| Frente | Id F | Tarefa | Ramo | Pasta | Ficheiros partilhados que vai escrever | Estado |
|---|---|---|---|---|---|---|
| A4 fase 2 — extracção por estudo (a4_somavel=sim) | F40 | — | `claude/f40-a4-extracao` | `lotes_a4/` | `dados_fck` (por gravar) | extracção feita (152 estudos + 35 relidos), **gravação em espera** |
| A4 fases 1–3 — classificação/lotes/motor | F41–F43 | #0619 | `claude/rsl-619-*` | `lotes_transporte/`, `metanalise/` | `dados_fck` (por gravar) | F41–F43 no `main`; 14 lotes sem resultados |
| _próximo id livre_ | **F44** | | | | | |

Ids F-nn: reservar o seguinte na tabela **antes** de o usar em commit ou em `DECISOES_METANALISE.md` (evita duas frentes com o mesmo número).

## 5. Ficheiros binários (`.xlsx`) — padrão «JSON paralelo, integrador único»

É o que o projecto já faz (resultados em JSON + `aplicar*.py`); passa a ser regra explícita:

1. Agentes em paralelo produzem **só artefactos de texto** (JSON/CSV/`.py`/`.md`) na pasta da sua frente — fundem-se bem em Git.
2. **Um integrador por vez** corre o `aplicar*.py` e faz **um só commit** do `.xlsx` no fim do lote/etapa (menos histórico: cada commit guarda ~6 MB).
3. Antes de gravar: `git fetch`; clone/ramo novo a partir do `main` actual; confirmar que nenhum ramo aberto alterou o `.xlsx` (§8.2); gravar; rodar os scripts de recálculo (`recalcular_ci.py`, `classificar_base_portland.py`…) conforme a frente; PR; **só então** o próximo integrador começa.
4. `aplicar*.py` só preenche células vazias (ou usa lista explícita de excepções) e é idempotente; correr `aplicar.py` seguido de `aplicar_verif.py` quando existirem os dois.
5. Nunca resolver conflito de `.xlsx` «escolhendo um lado»: refazer o `aplicar` sobre o `main` actual.
6. Backups: não commitar (`02_ARQUIVOS ANTERORES/` está no `.gitignore`); o commit anterior é o backup.

## 6. Formato de entrega de um agente (testemunho)

Ao terminar, cada agente deixa **no ramo da frente** (e não só no chat):

- ficheiro(s) de resultado em `lotes_<frente>/resultado_*.json` (nomes com o nº do lote, nunca reutilizar ficheiros do scratchpad);
- o que **não** fez (estudos com leitura parcial, figuras não vistas) em campo explícito;
- entrada no `DECISOES_METANALISE.md` com **data, autor, id F-nn, id de tarefa, onde está aplicada** e «por confirmar» se for decisão minha;
- commit + push (o hook de paragem recusa ficheiros por commitar);
- depois do push, PR para o `main` (criado pronto para revisão) e subscrição dos eventos do PR.

«Concluído» só vale com o ficheiro no repositório. Erro apanhado por amostragem → auditar o lote inteiro desse agente (regra da Kiê, 2026-08-31).

## 7. Regras de decisão entre frentes

1. **Critério de dados: decide a Kiê, uma pergunta de cada vez, em texto no chat.** Sem decisão escrita, vale a regra mais restritiva («não vamos assumir nada»).
2. **Duas regras em conflito: vale a mais recente aprovada pela Kiê e a mais antiga é marcada «superada por Fnn»** (como a F30 superou a F29). A F43 (massa volúmica 2.400 kg/m³ como premissa «nossa») é posterior à regra estrita do F40 → **vale a F43**; os valores do F40 com massa volúmica de outra origem mantêm-se, com a origem registada por par (impressa / soma do traço / premissa). **Por confirmar** que isto não contradiz a intenção da Kiê.
3. **Trabalho duplicado:** o segundo agente a descobrir a duplicação para, regista-a no §4 e comunica à Kiê; não apaga nem reescreve o trabalho do outro.
4. Decisões minhas ainda não validadas ficam «por confirmar» (regra de 2026-10-04).

## 8. Checklists

### 8.1 Antes de começar (30 segundos)
```bash
git fetch origin
git branch -r                                   # ramos abertos
git log origin/main --since="7 days ago" --format='%h %ad %s' --date=short
git diff --name-only origin/main...origin/<ramo> # o que cada ramo aberto toca
```
Ler o §4. Se alguém já toca na mesma pasta/ficheiro/tema → parar.

### 8.2 Antes de escrever num `.xlsx`
```bash
git fetch origin
for b in $(git branch -r | grep -v HEAD); do git diff --name-only origin/main...$b | grep -E '\.xlsx$' && echo "  ^ $b"; done
```
Resultado vazio = livre. Qualquer linha = esse ramo é o integrador activo; esperar ou combinar com a Kiê.

### 8.3 Ao fechar
Resultados no ramo → decisão registada → `CLAUDE.md` (uma linha de estado) → PR → §4 actualizado (estado «feito»).

## 9. Regras permanentes do repositório (resumo, vigentes desde 2026-11-02)

- Clone **novo** a partir do `main`; nunca fazer push de cópia anterior à reescrita de 2026-11-02.
- Ramos existentes: apagar só com autorização; branches `scratch/*` para transportar PDFs **não** se usam.
- PDFs só no Drive; nunca dados pessoais da Kiê (email) a serviços externos.
- Convenção de nomes, índices de colunas e armadilhas do conector do Drive: ver `CLAUDE.md`.

## 10. Por confirmar / perguntas à Kiê

1. Quem fica com a **extracção A4**: manter os 152 estudos já lidos (F40) e usar o F42 só para os 86 estudos que o F40 não cobre, ou unificar numa única lista? (a recomendação está no chat.)
2. **Máx. 2 frentes de escrita** em simultâneo — aceite?
3. O registo da §4 vive neste ficheiro (PR pequeno por linha) — ou prefere que viva na tarefa do Supabase?
4. Quem é o **integrador** por defeito do `meta_analysis_base.xlsx`: a sessão «Metanálise»?
