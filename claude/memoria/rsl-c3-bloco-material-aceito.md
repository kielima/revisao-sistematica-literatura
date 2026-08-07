---
name: rsl-c3-bloco-material-aceito
description: "Critério C3 (material não moldável): bloco/tijolo feito de material já aceito em C2 (terra, solo-cimento, geopolímero) não é rejeitado automaticamente -- distinguir prensado sob demanda (Aceito) de produto de catálogo padronizado (Rejeitado)"
metadata:
  node_type: memory
  type: project
  originSessionId: retriagem-166-linhas-2026-08-03
---

**Regra (decisão Kiê 2026-08-03):** o exemplo literal do critério C3 ("blocos e tijolos" → REJEITADO por forma padronizada sem personalização) foi escrito pensando em unidades de alvenaria industriais compradas de catálogo (tijolo cerâmico, bloco de concreto padrão). Quando o bloco/tijolo é feito de um material que já passou em C2 por uma exceção documentada (terra, solo-cimento, geopolímero — ver regra de terra em C6), essa rejeição automática não se aplica cegamente.

**Como decidir:**
- **ACEITO** — prensado/comprimido **sob demanda**, sem padronização industrial de catálogo, tipicamente produção artesanal/local com dimensões ajustáveis ao projeto. Exemplos aplicados: bloco de terra comprimida/moldado (row 3871), tijolo de terra comprimida intertravado ICEB (row 4133), tijolo solo-cimento (row 4717).
- **REJEITADO** — produto manufaturado **padronizado**, vendido explicitamente como substituto drop-in de um item de catálogo com dimensões fixas. Exemplos aplicados: bloco de pavimentação (paver) em geopolímero (row 2996), "bloco de alvenaria emergente" comercializado como substituto de CMU padrão com núcleo oco (row 5078).

**Why:** sem essa distinção, toda a categoria de material de terra (já aceita em C2 desde 2026-06-21 por ser universal/escalável) seria automaticamente eliminada em C3 só por ter formato de bloco — o que contradiria a lógica da própria exceção de terra. A distinção usa o CRITÉRIO REAL por trás da regra C3 (personalização por projeto vs. padronização industrial), não a forma do produto isoladamente.

**How to apply:** ao avaliar C3 de um bloco/tijolo, primeiro checar se o material já tem uma exceção documentada em C2 (terra, solo-cimento, geopolímero). Se sim, perguntar: é prensado localmente sob demanda, ou é um produto industrial padronizado de catálogo (mesmo que feito do material aceito)? Casos de concreto celular/espumoso (AAC/CLC/Ytong) continuam usando a regra "A REVISAR" separada já documentada em `RSL_PROGRESSO.md`.
