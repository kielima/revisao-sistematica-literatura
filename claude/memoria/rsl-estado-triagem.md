---
name: rsl-estado-triagem
description: "Estado da triagem por PDF da RSL: cascata C1-C8 CONCLUÍDA (2026-06-22, C7 removido). Funil real pós-auditoria (2026-08-03) = 1.333 artigos Aceito. Fonte canônica de progresso = RSL_PROGRESSO.md + PENDENCIAS_AUDITORIA_2026-07-12.md"
metadata:
  node_type: memory
  type: project
  originSessionId: dreaming-2026-06-21
---

Estado da **triagem por PDF** da RSL (vault REVISÃO SISTEMÁTICA DE LITERATURA). Consolidado originalmente no dreaming de 2026-06-21; atualizado em 2026-08-03 após a auditoria de qualidade de dados de 12/07/2026 ter sido concluída.

**Todos os critérios concluídos:**
- **C1** (antes de 2006) — concluído 2026-06-05.
- **C2** (material não estrutural) — concluído 2026-06-12. 146 Rejeitado (na execução original; número subiu para ~319 após correções pontuais de jul-ago/2026 que reabriram linhas mal-classificadas).
- **C3** (material não moldável) — concluído 2026-06-13. 41 Rejeitado.
- **C4** (não relacionado a construção) — concluído 2026-06-14, leitura 3+ páginas. 1.534 Aceito / 97 Rejeitado.
- **C5** (não menciona GEE/ACV/CO₂) — concluído 2026-06-21 sob a Opção A. P:Aceito = 1.505 | P:Rejeitado = 43 (na execução original).
- **C6** (material geograficamente restrito) — concluído 2026-06-21. 1.488 Aceito + 8 Rejeitado.
- ~~**C7**~~ — **REMOVIDO da RSL em 2026-06-22** (decisão Kiê). Coluna existe no xlsx mas ficou vazia (596 resíduos limpos em 2026-08-03).
- **C8** (opinião sem dados primários) — concluído 2026-06-22. 1.337 Aceito + 2 Rejeitado (execução original).

**Nenhum critério está ativo.** Não há mais "próximo critério" a retomar — `PROMPT_RETOMADA_C6.md` (citado no CLAUDE.md) foi removido do repo em algum momento e a referência ficou órfã.

**Estado real hoje (verificado programaticamente em 2026-08-03):** os totais acima, registrados durante a execução original de cada critério (maio-jun/2026), ficaram levemente desatualizados por correções linha-a-linha feitas em jul-ago/2026 (ver auditoria abaixo). O número que importa agora é o funil agregado: **1.333 artigos com C1-C6 e C8 todos = Aceito**. `status_triagem`: Duplicado 2.621 | Inconclusivo 1.066 | Rejeitado 963 | Elegível 383 | Sem acesso 60.

**Auditoria de qualidade de dados (12/07/2026 → 03/08/2026):** rodada após a Kiê lembrar de um alerta de PDFs faltando/análises incorretas. Achou 10 inconsistências (cascata quebrada em algumas linhas, células C8 sem prefixo `R:`/`P:`, 596 resíduos da coluna C7 removida, 6 linhas "Sem acesso" que já tinham PDF físico vinculado mas nunca foram retriadas, `status_triagem` dessincronizado de decisões já tomadas por PDF, etc.). **9 de 10 resolvidas.** Pendência aberta: linha 2897 (di Summa et al., 2023, *Structural Concrete*, DOI `10.1002/suco.202300645`) — PDF não localizado no Google Drive nem via Sci-Hub; Kiê vai tentar via biblioteca institucional. Detalhe completo em `PENDENCIAS_AUDITORIA_2026-07-12.md`.

**Pendência antiga resolvida:** row 3002 (antes só tinha capa/front matter de livro Woodhead) já está com toda a cascata C1-C8 preenchida — não é mais bloqueio.

**Why este memo existe:** evitar que uma sessão futura reabra critérios já fechados ou tente "continuar o C6" a partir de instruções desatualizadas (o `PROMPT_RETOMADA_C6.md` que orientava isso não existe mais). A partir de agora, qualquer trabalho na triagem é correção pontual de linha (reabrir "Sem acesso" quando surge PDF novo, corrigir inconsistência de cascata), não avanço de critério.

**How to apply:** ao iniciar uma sessão de triagem/auditoria, ler primeiro `PENDENCIAS_AUDITORIA_2026-07-12.md` (estado da auditoria) e a seção "Estado real pós-auditoria" do `CLAUDE.md`/`RSL_PROGRESSO.md` — não assumir que há um critério em andamento. As regras de critério (C5 Opção A etc.) continuam válidas como referência de método para qualquer reavaliação pontual: ver [[rsl-c5-criterio]] e `RSL_PROGRESSO.md` seção "Definições completas dos critérios C1–C8".
