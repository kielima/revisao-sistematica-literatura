---
name: rsl-marcacao-r-vs-p
description: "Na triagem da RSL, R: é só decisão preliminar por resumo; toda linha precisa ser confirmada com P: (leitura de PDF, 5+ páginas) antes de ser considerada definitiva. Correção de 2026-08-03 revoga permissão anterior de manter R: quando título/resumo 'parecia' suficiente."
metadata:
  node_type: memory
  type: feedback
  originSessionId: fb2a5077-0c97-4017-a789-3068eea0b954
---

**⚠️ CORREÇÃO (Kiê, 2026-08-03):** a versão anterior desta nota (sessão 2026-06-06) permitia manter uma célula em `R:` quando o título/resumo já "resolvia" a decisão, sem exigir leitura do PDF. **Isso está errado e foi revogado.** A regra vigente agora:

- **`R:`** é sempre uma decisão **preliminar/provisória**, feita só com título e resumo. Nunca é considerada uma triagem concluída, mesmo que a decisão pareça óbvia.
- **`P:`** é a única marcação que conta como critério definitivamente avaliado. Para chegar a `P:Aceito` ou `P:Rejeitado`, é obrigatório **ler as primeiras 5 páginas do corpo do artigo** (desconsiderando resumo/título) e, se essas 5 páginas não bastarem para decidir, **continuar lendo até conseguir decidir**.
- **Toda linha que hoje só tem `R:Aceito` (sem `P:` correspondente) em algum critério não está triada de fato** — precisa ser confirmada por leitura de PDF antes de ser tratada como parte do funil final da RSL.
- Formato da célula continua o mesmo: `R:<decisão original> | P:<decisão confirmada por PDF>`. O `R:` original nunca é apagado, só complementado.

**Why:** a Kiê esclareceu (2026-08-03) que a regra nunca foi "abrir o PDF e conferir só a 1ª página/título" — é ler pelo menos as 5 primeiras páginas do conteúdo real do artigo antes de aceitar ou rejeitar um critério. Decidir só pelo resumo é uma etapa preliminar (R:), não a decisão final. A convenção de 2026-06-06 que tratava `R:` como suficiente quando "óbvio" media progresso de forma imprecisa e permitia que artigos nunca tivessem seu conteúdo real verificado.

**Impacto conhecido (medido em 2026-08-03):** dos 1.109 artigos com `status_triagem=Inconclusivo`, apenas 39 têm C1-C6 100% confirmados por `P:` — os outros 957 têm pelo menos um critério ainda só em `R:` e precisam de confirmação por PDF antes de entrar no funil final da RSL.

**How to apply:** ao retomar qualquer trabalho de triagem, tratar toda célula `R:`-only como pendente de leitura de PDF, não como decidida. Ler no mínimo 5 páginas de corpo de texto (não resumo) antes de registrar `P:`. Ver [[rsl-criterios-verbatim]] e [[rsl-validacao-pdf-rejeitados]].
