---
titulo: MOC — REVISÃO SISTEMÁTICA DE LITERATURA
descricao: Mapa navegacional do vault RSL. Auto-gerado pela skill avaliacao-critica-vault no bloco AUTO; suas anotações pessoais ficam preservadas no bloco USER.
ultima_atualizacao: 2026-06-04
status: ativo
tags: [moc, indice, rsl]
---

# 🗺️ MOC — REVISÃO SISTEMÁTICA DE LITERATURA

> MOC raiz do vault. Aponta para MOCs por área e oferece mapeamento temático geral. Auto-gerada — para preservar suas adições, edite somente dentro do bloco `<!-- USER:BEGIN -->`.

<!-- AUTO:BEGIN -->

## Visão geral

- **Total de notas .md:** 16
- **PDFs de artigos:** ~1.630 (contagem direta de pastas)
- **Total de anexos:** 1.713 arquivos (PDFs, xlsx, py, html, bib, ris, csv…)
- **Áreas raiz:** 4 (00_REFERENCIAS, 01_BUSCAS NAS BASES, 02_ARQUIVOS ANTERORES, 04_EXTERNAL SOURCES)
- **Sub-vaults aninhados:** 0
- **Links internos entre notas:** 0
- **TODOs pendentes:** 104 | concluídos: 82
- **Última varredura:** 2026-06-04

## Áreas

### 00_REFERENCIAS (catálogo)

- **Notas .md:** 7 (6 em METODOLOGIA_ESTATÍSTICA + 1 em PRISMA)
- **PDFs:** ~1.630 (em subpastas de artigos)
- **MOC da área:** [[00_REFERENCIAS/_MOC]]

**Notas principais:**
- [[Metanalise_Efeitos_Fixos_vs_Aleatorios]] — Base teórica da meta-análise
- [[Justificativa_Modelo_Efeitos_Aleatorios]] — Justificativa modelo REML
- [[REML_vs_DL_explicacao]] — Comparação estimadores
- [[CÁLCULO DO P ESTATÍSTICO]] — Cálculo estatístico
- [[FLUXOGRAMA_PRISMA_2020_DOC]] — Documentação PRISMA 2020

### 01_BUSCAS NAS BASES (temporal)

- **Notas .md:** 0
- **Arquivos de dados:** .bib, .ris, .csv das buscas originais
- **Buscas:** BUSCA 01 (VOS Viewer), BUSCA 02 (LCA + concreto/UHPC), BUSCA 03 (11-04-25), BUSCA 04 (15-04-25)
- **MOC da área:** [[01_BUSCAS NAS BASES/_MOC]]

### 02_ARQUIVOS ANTERORES (arquivo)

- Pasta de arquivamento de versões obsoletas — não avaliada como área ativa.
- Convenção: ver [[CLAUDE]] seção "Regra de arquivamento".

### 04_EXTERNAL SOURCES (catálogo)

- **Notas .md:** 0
- **PDFs:** 8 (Celik 2015, Costa 2020, Mohammadi 2023, Onyelowe 2022, Sakir 2020, Shen 2015, Wang 2019, Zahid 2023)
- **MOC da área:** [[04_EXTERNAL SOURCES/_MOC]]

## Notas operacionais na raiz

| Nota | Propósito | Status |
|---|---|---|
| [[RSL_PROGRESSO]] | Estado atual: contagens PRISMA, downloads | em-andamento |
| [[RELATORIO_VERIFICACAO_BD_RSL]] | Relatório de verificação do banco | operacional |
| [[DOWNLOAD_LESSONS_LEARNED]] | Lições aprendidas no processo | operacional |
| [[EXTERNAL_SOURCES_DOIs]] | Lista de DOIs de fontes externas | operacional |
| [[FASE5_LOG_PROBLEMAS]] | Log de problemas Fase 5 | operacional |
| [[RSL_COL_R_LOG]] | Log de coleta R | operacional |
| [[PROMPT_RETOMADA_VERIFICACAO_RSL]] | Prompt de retomada | operacional |
| [[como_contornamos_o_akamai]] | Documentação técnica anti-bot | operacional |

## Mapeamento temático

- **meta-analise** (4 notas): [[Metanalise_Efeitos_Fixos_vs_Aleatorios]], [[Justificativa_Modelo_Efeitos_Aleatorios]], [[REML_vs_DL_explicacao]], [[Justificativa_Modelo_Efeitos_Aleatorios_backup_pre-REML]]
- **metodologia** (4 notas): [[Metanalise_Efeitos_Fixos_vs_Aleatorios]], [[Justificativa_Modelo_Efeitos_Aleatorios]], [[REML_vs_DL_explicacao]], [[CÁLCULO DO P ESTATÍSTICO]]
- **revisao-sistematica** (5 notas): [[RSL_PROGRESSO]], [[FLUXOGRAMA_PRISMA_2020_DOC]], e notas de metodologia
- **UHPC** (4 notas): notas focadas em concreto de ultra-alto desempenho
- **PRISMA** (1 nota): [[FLUXOGRAMA_PRISMA_2020_DOC]]

## Relatórios de avaliação

- Nenhum relatório ativo — o de 2026-06-04 foi removido em 2026-08-03 (pendências já resolvidas organicamente). Rodar a skill `avaliacao-vault` para gerar um novo.

<!-- AUTO:END -->

<!-- USER:BEGIN -->
<!--
Adicione suas anotações pessoais aqui — este bloco NUNCA é sobrescrito pela skill.
Exemplos:
- Atalhos mentais ou lembretes de navegação
- Notas sobre prioridades atuais
- Conexões entre áreas que o mapa automático não captura
-->

## 🧠 Memória local do projeto (`claude/memoria/`)

> Migrada da auto-memória do espaço para dentro do vault em 2026-06-21 (skill `dreaming`). Fonte canônica e portátil da memória de método da RSL. Índice: `claude/memoria/MEMORY.md`. Relatórios de consolidação: `claude/memoria/_dreams/`.

- **Estado da triagem (C1–C8):** [[claude/memoria/rsl-estado-triagem]] — ✅ **cascata C1–C8 concluída (2026-06-22)**, sem critério ativo. Fase atual é auditoria/correção pontual de dados, não continuação de critério.
- **Auditoria de dados (2026-08-03):** funil real = 1.333 artigos Aceito em toda a cascata. Ver `PENDENCIAS_AUDITORIA_2026-07-12.md` (10 achados, 9 resolvidos, 1 pendente: linha 2897, PDF sem acesso).
- Regras de critério: C5 ([[claude/memoria/rsl-c5-criterio]]), C4 ([[claude/memoria/rsl-c4-adendo-residuo-em-concreto]]), C2/C3 ([[claude/memoria/rsl-argamassa-revestimento-e-taipa]]).
- Método: links CAPES, PDF ilegível, validação de rejeitados, marcação R:/P:, rastreio col 33.

## ⚠️ Notas de organização pendentes (2026-08-03)

- `PROMPT_RETOMADA_C6.md` é citado no `CLAUDE.md` mas o ficheiro não existe mais (nem na raiz, nem em `02_ARQUIVOS ANTERORES`) — referência órfã, ver nota na tabela de "Notas operacionais na raiz" do CLAUDE.md.
- ~13 PNGs soltos na raiz (`tmp_fig_p*.png`, `arredondo_p*.png`, `chen2024d_fig4_*.png`, ~7 MB) — sobras de verificação visual de PDF, ainda não arquivados/removidos.

<!-- USER:END -->
