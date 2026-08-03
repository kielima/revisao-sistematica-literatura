---
name: rsl-estado-triagem
description: "Estado da triagem por PDF da RSL: C1–C5 concluídos (C5 em 2026-06-21, P:Aceito=1.505/P:Rejeitado=43); C6 é o critério ATIVO. Fonte canônica de progresso = RSL_PROGRESSO.md"
metadata:
  node_type: memory
  type: project
  originSessionId: dreaming-2026-06-21
---

Estado da **triagem por PDF** da RSL (vault REVISÃO SISTEMÁTICA DE LITERATURA), consolidado no dreaming de 2026-06-21 a partir do `RSL_PROGRESSO.md` e do `CLAUDE.md`.

**Critérios concluídos:**
- **C1** (antes de 2006) — concluído 2026-06-05.
- **C2** (material não estrutural) — concluído 2026-06-12. 146 Rejeitado.
- **C3** (material não moldável) — concluído 2026-06-13. 41 Rejeitado.
- **C4** (não relacionado a construção) — concluído 2026-06-14, leitura 3+ páginas. 1.534 Aceito / 97 Rejeitado.
- **C5** (não menciona GEE/ACV/CO₂) — **concluído 2026-06-21** sob a Opção A. Universo = 1.548 C4-Aceito. **Resultado final verificado no xlsx: P:Aceito = 1.505 | P:Rejeitado = 43.**

**Critério ATIVO agora:** **C6** (material geograficamente restrito / estudos regionalizados). Prompt de retomada ativo = `PROMPT_RETOMADA_C6.md`. Universo C6 = os 1.505 C5-Aceito. Já há **pré-marcas de C6 nos comments** de artigos de taipa/rammed earth e cut-stone/pedra de cantaria (ver [[rsl-argamassa-revestimento-e-taipa]]) — esses entram na avaliação do C6 agora.

**Pendência rastreada:** row **3002** (só capa/front matter de livro Woodhead, 3 págs) segue sem PDF correto — aguarda a Kiê. Ao retomar a triagem, pular 3002 até ter o PDF.

**Why:** as memórias de critério (C5 etc.) descreviam regras de triagem como se a triagem ainda estivesse em curso; o índice ainda carregava a regra C5 obsoleta. Este fato fixa o estado atual real para não reabrir critérios já fechados nem aplicar a regra C5 antiga.

**How to apply:** ao iniciar uma sessão de triagem, ler primeiro a seção "Progresso da triagem por PDF" do `RSL_PROGRESSO.md` (fonte canônica) — este memo é um ponteiro de estado, não substitui a contagem oficial. A regra C5 vigente é a Opção A: ver [[rsl-c5-criterio]]. Parar entre critérios e aguardar confirmação da Kiê (ver [[rsl-criterios-verbatim]]).
