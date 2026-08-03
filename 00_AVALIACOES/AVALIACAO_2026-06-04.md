---
titulo: Avaliação crítica — REVISÃO SISTEMÁTICA DE LITERATURA — 2026-06-04
data: 2026-06-04
vault: REVISÃO SISTEMÁTICA DE LITERATURA
total_notas_md: 16
total_anexos: 1713
score_geral: 7.5/10
tipos_areas: {00_REFERENCIAS: catalogo, 01_BUSCAS_NAS_BASES: temporal, 02_ARQUIVOS_ANTERORES: arquivo, 04_EXTERNAL_SOURCES: catalogo}
tags: [avaliacao, vault, claude-readiness]
status: ativo
---

# Avaliação crítica — REVISÃO SISTEMÁTICA DE LITERATURA — 2026-06-04

## Sumário executivo

Esta pasta é um projeto de Revisão Sistemática de Literatura (RSL) sobre impacto ambiental de UHPC, que serve simultaneamente como Projeto Claude. O foco primário é operacional — gerenciar ~1.630 PDFs de artigos científicos, um banco de triagem com 5.093 entradas, e a meta-análise em andamento — não um vault Zettelkasten típico. Por isso, critérios como conectividade entre notas e atomicidade não se aplicam diretamente; a avaliação é calibrada para um projeto documental-operacional. O estado geral é **sólido**: convenções de nomenclatura bem definidas, CLAUDE.md detalhado (embora sem marcadores antes desta execução), e notas de metodologia estatística com frontmatter consistente. Os principais pontos a melhorar são: higiene da raiz (arquivos residuais e backup em pasta ativa), ausência de frontmatter em 5 notas operacionais, e legibilidade limitada do banco Excel pelo Claude.

<!-- AUTO:BEGIN -->

## Progresso

- **Total de propostas:** 13
- **Concluídas:** 8
- **Pendentes:** 5
- **Última atualização de progresso:** 2026-06-04 (2ª passagem)

> Marque `[x]` ao concluir uma proposta. A próxima execução da skill também detectará automaticamente itens resolvidos.

## Inventário

- **Notas .md:** 16 (9 na raiz, 7 em 00_REFERENCIAS)
- **Anexos:** ~1.713 (PDFs: ~1.634 | xlsx: 59 | bib: 66 | ris: 12 | py: 6 | html: 4 | outros)
- **Áreas raiz:** 00_REFERENCIAS (catálogo), 01_BUSCAS NAS BASES (temporal), 02_ARQUIVOS ANTERORES (arquivo), 04_EXTERNAL SOURCES (catálogo)
- **Sub-vaults aninhados:** 0
- **Frontmatter:** 15/16 notas (93,75%) — após adição de FM em 4 notas operacionais
- **Links internos:** 0 (esperado para este tipo de vault)
- **MOCs manuais antes desta execução:** nenhum
- **MOCs criados nesta execução:** 4 (_MOC.md raiz + 00_REFERENCIAS + 01_BUSCAS NAS BASES + 04_EXTERNAL SOURCES)

## Diagnóstico por área

### Raiz — notas operacionais (tipo: operacional)

**Inventário rápido.** 9 notas .md, 0 links internos, frontmatter em ~33% (3/9 estimado).

**👁️ Como você vê (Obsidian, uso humano).**
A raiz concentra documentação operacional do projeto: logs de processo, relatórios de verificação, prompts de retomada. Funciona bem como arquivo de referência rápida. A mistura de .md, .xlsx, .html, .py, .ps1 e .json na mesma pasta pode criar confusão visual.

**🤖 Como o Claude vê (Projeto, contexto carregado).**
As notas operacionais carregam bem como contexto, especialmente RSL_PROGRESSO.md (estado atual) e CLAUDE.md (convenções). Os arquivos .xlsx (articles_final.xlsx com 4,5 MB) e .html são carregados como metadados mas não como conteúdo legível diretamente — o Claude precisa de Python/openpyxl para acessar os dados do banco.

**Pontos fortes.**
- CLAUDE.md muito detalhado: documenta arquitetura de download, convenção de nomenclatura, protocolo de matching, regras críticas.
- RSL_PROGRESSO.md centraliza estado atual com timestamps e aritmética PRISMA verificável.

**Achados.**

- [x] **[médio — D5.3]** `<id:d5.3-claude-md-sem-marcadores>` CLAUDE.md não tinha marcadores AUTO/USER (Situação C). → *Resolvido nesta execução:* backup salvo em `_AVALIACOES/_backups/CLAUDE_backup_2026-06-04.md`; novo CLAUDE.md gerado com estrutura de marcadores; conteúdo original preservado no bloco USER.

- [ ] **[leve — D4.4]** `<id:d4.4-elsevier-html-obsoleto>` `ELSEVIER_DOWNLOAD.html` (140 KB, modificado em Jun 2) ainda está na raiz, mas RSL_PROGRESSO.md registra que "ELSEVIER_DOWNLOAD.html foi eliminado — tudo num único DOWNLOAD_MANUAL.html" em 03/06/2026. → *Proposta:* mover para `02_ARQUIVOS ANTERORES/` ou deletar, de acordo com o que foi decidido em 03/06.

- [ ] **[leve — D4.3]** `<id:d4.3-test-tmp>` `test_write.tmp` (arquivo vazio, criado 03/06) é resíduo de teste e não pertence à raiz. → *Proposta:* deletar `test_write.tmp`.

- [x] **[leve — D2.3]** `<id:d2.3-notas-sem-frontmatter>` 5 notas operacionais na raiz não têm frontmatter: `DOWNLOAD_LESSONS_LEARNED.md`, `EXTERNAL_SOURCES_DOIs.md`, `FASE5_LOG_PROBLEMAS.md`, `PROMPT_RETOMADA_VERIFICACAO_RSL.md`, `como_contornamos_o_akamai.md`. Dado seu caráter operacional (logs, prompts), o frontmatter não é crítico — mas facilita filtragem por status. → *Proposta (baixa prioridade):* adicionar frontmatter mínimo com `titulo`, `status`, `ultima_atualizacao`. Opcionalmente deixar como está se as notas não são de referência.

- [ ] **[leve — D4.3]** `<id:d4.3-pii-map-json>` `pii_map.json` (checkpoint de PII — 15 KB, modificado 31/05) está na raiz. Se os scripts que o geravam foram "removidos" conforme CLAUDE.md nota de 03/06, é resíduo. → *Proposta:* verificar se ainda é usado por algum script ativo; se não, mover para `02_ARQUIVOS ANTERORES/`.

---

### 00_REFERENCIAS (tipo: catálogo)

**Inventário rápido.** 7 notas .md, todas com frontmatter, 0 links internos, ~1.630 PDFs em subpastas.

**👁️ Como você vê (Obsidian, uso humano).**
Área bem organizada: PDFs em subpastas temáticas claras, notas de metodologia com frontmatter consistente e conteúdo de alta qualidade. A presença de um arquivo de backup (`_backup_pre-REML`) em pasta ativa é a única irregularidade.

**🤖 Como o Claude vê (Projeto, contexto carregado).**
As 7 notas .md carregam completamente e têm frontmatter — Claude consegue filtrar por `tags` e `status` eficientemente. Os ~1.630 PDFs não são carregados como contexto (corretamente — não há `[[link]]` para eles). Sem qualquer nota de índice antes desta execução, o Claude não tinha mapa navegacional desta subpasta.

**Pontos fortes.**
- Todas as notas têm frontmatter completo e `status: revisado`.
- Notas de metodologia estatística são auto-suficientes e detalhadas.
- Estrutura de subpastas clara e intuitiva.

**Achados.**

- [x] **[médio — D1.5]** `<id:d1.5-moc-00referencias>` Área-catálogo 00_REFERENCIAS sem MOC-índice. → *Resolvido nesta execução:* `00_REFERENCIAS/_MOC.md` criado.

- [x] **[leve — D4.4]** `<id:d4.4-backup-pre-reml>` `00_REFERENCIAS/METODOLOGIA_ESTATÍSTICA/Justificativa_Modelo_Efeitos_Aleatorios_backup_pre-REML.md` é explicitamente um backup (`_pre-*`) e viola a convenção CLAUDE.md de "qualquer arquivo com sufixo `_pre-*` que não seja a versão corrente vai para 02_ARQUIVOS ANTERORES". → *Proposta:* mover para `02_ARQUIVOS ANTERORES/Justificativa_Modelo_Efeitos_Aleatorios_backup_pre-REML.md`.

- [ ] **[leve — D2.1]** `<id:d2.1-artigos-meta-analise-vazio>` Subpasta `ARTIGOS ACEITOS PARA A META-ANÁLISE/` está vazia (0 PDFs). Se serve para um subset específico dos artigos aceitos, deveria ter ao menos uma nota explicando o critério de inclusão. → *Proposta:* ou popular a pasta com os PDFs dos 69 estudos incluídos na meta-análise, ou criar uma nota `_LEIA_ME.md` explicando o estado/propósito, ou remover a pasta se não estiver sendo usada.

---

### 01_BUSCAS NAS BASES (tipo: temporal)

**Inventário rápido.** 0 notas .md, 4 pastas de busca com arquivos de exportação das bases.

**👁️ Como você vê (Obsidian, uso humano).**
Área de arquivo dos dados brutos das buscas bibliográficas. Serve principalmente como backup de rastreabilidade PRISMA — confirmar quais bases foram buscadas, com quais strings. A ausência de notas .md é esperada para este tipo de conteúdo.

**🤖 Como o Claude vê (Projeto, contexto carregado).**
Os arquivos .bib, .ris, .csv são parcialmente legíveis (texto bruto), mas volumosos. Sem nota explicativa nas pastas, o Claude não consegue inferir contexto das buscas sem ler os arquivos.

**Pontos fortes.**
- Buscas organizadas cronologicamente com nomes descritivos.
- Arquivo VOS Viewer na BUSCA 01 indica análise bibliométrica foi feita.

**Achados.**

- [x] **[médio — D1.6]** `<id:d1.6-moc-01buscas>` Área-temporal 01_BUSCAS NAS BASES sem nota-índice cronológica. → *Resolvido nesta execução:* `01_BUSCAS NAS BASES/_MOC.md` criado com linha do tempo das 4 buscas.

---

### 04_EXTERNAL SOURCES (tipo: catálogo)

**Inventário rápido.** 0 notas .md, 8 PDFs de fontes externas.

**👁️ Como você vê (Obsidian, uso humano).**
Coleção pequena e bem delimitada. Os PDFs têm nomenclatura padrão do projeto.

**🤖 Como o Claude vê (Projeto, contexto carregado).**
Sem nota de índice, o Claude não sabia que estes são fontes externas com status RSL específico (FE001 incorporado, FE002 rejeitado). A MOC criada resolve isso.

**Achados.**

- [x] **[médio — D1.5]** `<id:d1.5-moc-04external>` Área-catálogo 04_EXTERNAL SOURCES sem MOC-índice. → *Resolvido nesta execução:* `04_EXTERNAL SOURCES/_MOC.md` criado com tabela de fontes e status RSL.

---

## Achados transversais

- [ ] **[leve — D5.2]** `<id:d5.2-relatorio-948-linhas>` `RELATORIO_VERIFICACAO_BD_RSL.md` tem 948 linhas e 114 KB. Abaixo do threshold crítico de 2.000 linhas, mas é a maior nota do vault. Como relatório técnico, o tamanho é justificado; mencionar para ciência. → *Proposta (opcional):* se houver seções que ficaram obsoletas, arquivar partes em `02_ARQUIVOS ANTERORES/`.

- [ ] **[médio — D5.1]** `<id:d5.1-xlsx-nao-legiveis>` `articles_final.xlsx` (4,5 MB) e outros 58 arquivos .xlsx são parcialmente legíveis pelo Claude — Claude vê metadados mas não os dados das células diretamente. O banco principal da RSL vive num arquivo que o Claude não pode ler sem Python. → *Proposta:* para consultas frequentes ao banco (ex.: "quantos artigos com pdf?", "quais elegíveis sem pdf?"), usar scripts Python + openpyxl e reportar em Markdown. Documentado implicitamente no CLAUDE.md — tornar explícito no bloco USER do CLAUDE.md se necessário.

- [ ] **[leve — D4.1]** `<id:d4.1-scripts-removidos-presentes>` Scripts `.py` e `.ps1` que foram "removidos" segundo a nota de 03/06 no CLAUDE.md ainda existem na raiz: `download_pdfs_win.py`, `mdpi_batch_dl.py`, `mdpi_resume.py`, `iop_hdl_dl.py`, `AUTO_DOWNLOAD_ELSEVIER.ps1`, `MONITOR_DOWNLOADS.ps1`. Se foram descontinuados, deveriam estar em `02_ARQUIVOS ANTERORES/` ou deletados. → *Proposta:* confirmar quais scripts estão definitivamente descontinuados e mover para `02_ARQUIVOS ANTERORES/` conforme convenção.

## Saúde dos sub-vaults aninhados

Detectados 0 sub-vaults aninhados — nenhuma atenção identificada nos 5 checks.

## Plano de ação sugerido (top 5)

1. [x] `<id:plano-1>` **Gerar CLAUDE.md com marcadores AUTO/USER** — impacto imediato na usabilidade Claude (contexto estruturado, bloco USER preservado em execuções futuras). (esforço: baixo — resolvido nesta execução)

2. [x] `<id:plano-2>` **Mover backup `_pre-REML` para 02_ARQUIVOS ANTERORES** — viola a convenção documentada no próprio CLAUDE.md; 1 minuto de esforço. (esforço: baixo)

3. [ ] `<id:plano-3>` **Limpar raiz: deletar test_write.tmp, verificar ELSEVIER_DOWNLOAD.html e scripts descontinuados** — higiene básica; reduz ruído ao carregar o vault como Projeto Claude. (esforço: baixo)

4. [ ] `<id:plano-4>` **Definir propósito de `ARTIGOS ACEITOS PARA A META-ANÁLISE/`** — pasta vazia; ou popular com os 69 PDFs incluídos na meta-análise, ou criar nota explicativa, ou remover. (esforço: médio)

5. [x] `<id:plano-5>` **Adicionar frontmatter mínimo às 5 notas operacionais sem FM** — baixo impacto mas melhora filtragem por status no Obsidian e legibilidade pelo Claude. (esforço: baixo)

## Scores por dimensão

| Dimensão | Score | Comentário |
|---|---|---|
| D1. Estrutura | 8,5/10 | Nomenclatura e hierarquia bem definidas; MOCs ausentes antes desta execução (resolvido) |
| D2. Qualidade | 8,5/10 | Frontmatter em 15/16 notas (93,75%); backup removido; D2.1 pasta meta-análise vazia ainda pendente |
| D3. Conectividade | N/A* | 0 links internos é esperado para vault RSL operacional; critério não se aplica |
| D4. Higiene | 7,5/10 | Backup removido; ainda pendentes: test.tmp, scripts descontinuados, ELSEVIER_DOWNLOAD.html, pii_map.json |
| D5. Claude-readiness | 8,0/10 | CLAUDE.md com marcadores; FM em 15/16; banco Excel ainda requer Python para acesso |
| **Geral** | **8,0/10** | Melhorias aplicadas nesta sessão elevaram score de 7,5 → 8,0 |

*D3 não avaliado por incompatibilidade metodológica — este vault é documental/operacional, não Zettelkasten.

## Histórico de atualizações

| Data | Mudança |
|---|---|
| 2026-06-04 | Avaliação inicial — 13 propostas geradas; 4 resolvidas nesta execução (MOCs + CLAUDE.md) |
| 2026-06-04 (2ª passagem) | Auto-detectado: 4 propostas concluídas (d4.4-backup-pre-reml, d2.3-notas-sem-frontmatter, plano-2, plano-5) — total 8/13 |

## Notas metodológicas

- Avaliação calibrada para vault RSL/operacional — critérios Zettelkasten (conectividade, atomicidade) não aplicados.
- Áreas classificadas como catálogo (00_REFERENCIAS, 04_EXTERNAL SOURCES), temporal (01_BUSCAS NAS BASES) e arquivo (02_ARQUIVOS ANTERORES).
- Classificação confirmada pela Kiê em 2026-06-04.
- Sub-vaults aninhados: nenhum detectado.
- Cada proposta tem ID único determinístico.

<!-- AUTO:END -->

<!-- USER:BEGIN -->
<!--
Suas anotações pessoais sobre esta avaliação — nunca sobrescritas.
Exemplos:
- Justificativas para não-aplicar certas propostas
- Contexto que mudou desde a avaliação
- Prioridades para a próxima sessão
-->
<!-- USER:END -->

---

*Relatório gerado pela skill `avaliacao-critica-vault`.*
