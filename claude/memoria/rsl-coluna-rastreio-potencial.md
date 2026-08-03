---
name: rsl-coluna-rastreio-potencial
description: "Na triagem da RSL, preencher a coluna rastreio_potencial_futuro (col 33) marcando tecnologias promissoras; biocimento standalone = C2 Rejeitado + marca"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 765c97a3-90ca-4417-87d0-42553152c8a7
---

Na triagem da RSL (vault REVISÃO SISTEMÁTICA DE LITERATURA), além de classificar C1–C8, preencher a coluna **`rastreio_potencial_futuro`** (coluna 33 do `articles_final.xlsx`, criada 2026-06-12 a pedido da Kiê) em **todos os lotes**. Ela marca tecnologias promissoras com potencial estrutural futuro, **independentemente da decisão C2**. Tags separadas por `; `:

- **biocimento** — MICP/EICP/biocimentação, precipitação microbiana de calcita, concreto autocicatrizante por bactérias.
- **fator_clinquer** — estudos sobre redução/substituição do fator clínquer (LC3, argila calcinada, etc.).
- **aglomerante_alternativo** — geopolímero, álcali-ativado, MgO, sulfoaluminato de cálcio (CSA), LC3 **E** SCM parcial (cinza volante, escória, sílica, metacaulim, pozolana, cinza de casca de arroz/bagaço, pó de vidro, biochar, etc.). Abrangência **AMPLA** (decisão Kiê: inclui substituição parcial).
- **carbonatacao_captura** — carbonatação/sequestro de CO2 no próprio material (carbonatação de concreto, mineralização, self-healing).
- **outra** — qualquer outra tecnologia promissora que possa vir a ser estrutural em substituição ao concreto no futuro, mesmo sem esse foco hoje (aplicada caso a caso na leitura).

**Regra de decisão para biocimento (decisão Kiê 2026-06-12):** biocimentação **standalone** (MICP/EICP estabilizando solo/areia, ou "growing bricks" de biocimento) → continua **C2 Rejeitado** (não é viga/pilar hoje) **+ marca** `biocimento`. Biocimento como **aditivo em concreto estrutural** (ex.: concreto autocicatrizante por bactérias) → **C2 Aceito** + marca. Isso substitui o tratamento antigo de simplesmente rejeitar-e-esquecer.

**Why:** a Kiê quer rastrear tecnologias emergentes (bioengenharia, aglomerantes alternativos, fator clínquer, captura de carbono) que hoje não entram como material estrutural mas têm potencial futuro — sem perdê-las de vista nem poluir a extração de fck/CO2.

**How to apply:** ao classificar cada artigo do lote, além de C2, setar a coluna 33 com as tags aplicáveis (por palavra-chave + leitura). Ver [[rsl-criterios-verbatim]]. Reclassificados na revisão retroativa: 3538, 4647 (biocimento → C2 Rejeitado); 3242 permaneceu Aceito (autocicatrizante).
