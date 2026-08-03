---
name: rsl-marcacao-r-vs-p
description: "Na triagem da RSL, marcar R: quando título/resumo resolve e P: só quando precisou ler o PDF completo"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: fb2a5077-0c97-4017-a789-3068eea0b954
---

Na re-triagem da RSL (vault REVISÃO SISTEMÁTICA DE LITERATURA), a marcação nas células C1–C8 deve refletir **a profundidade da avaliação**:

- **Título/resumo resolveu a decisão** → usar **R:** Não acrescentar um segundo token `| P:`. Em vez disso, **corrigir o PRIMEIRO `R:` da célula com a decisão** (a re-triagem sobrescreve o valor do R: original). Ex.: célula era `R:Aceito` e pelo título vi que é asfalto → vira `R:Rejeitado`.
- **Quando a re-triagem MUDA o resultado original** → registrar nos `comments` que foi reavaliado: `[Reavaliado por título/resumo: <Cn> era R:<original>]` (preserva o histórico do valor anterior).
- **Precisei ler o texto completo do PDF** (corpo/métodos/busca de termos além do resumo) → usar **P:**, no formato `R:<original> | P:<decisão>` (aí sim mantém o R: original + o P:).

**Why:** a Kiê quer que P: signifique de fato "avaliado pelo PDF (texto completo)", não pelo título. Marcar tudo como P: quando só o título resolveu é impreciso e compromete a rastreabilidade metodológica da RSL.

**How to apply:** ao classificar cada artigo, decidir honestamente se o título/resumo bastou (→ corrige o R:) ou se foi preciso ler o corpo (→ acrescenta P:). Ler apenas a 1ª página/resumo do PDF conta como nível resumo (R:). Convenção da aba `Critérios`: R: = avaliado pelo resumo; P: = avaliado pelo PDF (texto completo). Indicador de progresso passa a ser `material_C2` preenchido (Aceito) ou `[Cn Rejeitado]` nos comments (Rejeitado), não mais "tem P:". Ver [[rsl-criterios-verbatim]] e [[rsl-validacao-pdf-rejeitados]].
