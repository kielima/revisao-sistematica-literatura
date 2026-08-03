---
name: rsl-argamassa-revestimento-e-taipa
description: "Na RSL: argamassa de revestimento/reboco/gesso/fachada = NÃO estrutural = C2 Rejeitado (só argamassa estrutural passa); taipa/rammed earth = C3 Aceito mas pré-marcar p/ rejeição em grandes obras de infraestrutura"
metadata:
  node_type: memory
  type: feedback
  originSessionId: c3-triagem
---

Duas regras de triagem da RSL confirmadas pela Kiê em 2026-06-12 (durante o C3):

**1. Argamassa de revestimento ≠ argamassa estrutural (questão de C2, não C3).** O C2 só aceita *"argamassa estrutural"* (ver [[rsl-criterios-verbatim]]). Argamassas/materiais de **revestimento, reboco, gesso, cal, fachada, assentamento, acabamento** são **NÃO estruturais** → **C2 Rejeitado** (caem no exemplo do C2: "Paredes, elementos arquitetônico"). Não devem chegar ao C3. Casos corrigidos retroativamente: **3240** (lime-based mortars/renders/plasters) e **3273** (argamassa de fachada com caroço de azeitona, melhoria térmica) — eram C2 Aceito errado → reclassificados C2 Rejeitado. Atenção: gesso/gipsita **como aditivo no concreto/cimento** (set regulator) NÃO rejeita — aí o produto é concreto moldável (Aceito). Vigiar **4455** (compósito gesso-cimento-pozolana p/ impressão 3D — checar se é estrutural).

**2. Taipa / rammed earth = C3 Aceito + pré-marca de infraestrutura.** Taipa de pilão (rammed earth) = terra úmida compactada em fôrmas in loco → parede monolítica portante. É **estrutural e moldável** → **C3 Aceito**. MAS construção em terra crua não serve a grandes obras de infraestrutura urbana → **pré-marcar nos comments para rejeição no critério específico de aplicabilidade a grandes obras de infraestrutura** (decisão Kiê). Aplicar o mesmo a toda construção em terra crua (adobe estrutural in loco, etc.) daqui pra frente.

**3. Blocos/tijolos de agregados (nota histórica Kiê 2026-06-13).** Na aplicação MANUAL anterior (título/resumo), estudos cujo produto é **bloco/tijolo feito de agregados** (reciclados/alternativos) foram **descartados**. Coerente com rejeitar blocos/tijolos no C3 (não moldáveis). Distinção CONFIRMADA pela Kiê (2026-06-13): bloco/tijolo apenas como **fonte de agregado triturado em concreto** (produto final = concreto) → **Aceito** (ex. 4511, 4479, 4408); bloco/tijolo como **produto** → **Rejeitado**.

**4. Cut-stone / pedra de cantaria (dimension stone) — decisão Kiê 2026-06-13.** Pedra natural extraída de pedreira e cortada sob medida, usada como parede portante/elemento estrutural → **C3 Aceito** (tratada como personalizável/estrutural, não unidade padronizada), MAS **pré-marcar nos comments para rejeição no critério de especificidade/regionalização (C6)** — produção geograficamente restrita, baixa escalabilidade global ("não se extrai qualquer pedra de qualquer lugar"). Aplicar o mesmo a outros artigos de pedra dimensional/cantaria. Caso: row 4938 (De Toldi & Pestre, DOI 10.5334/bc.278).

**Why:** evitar propagar erro de C2 (revestimentos não estruturais entrando no funil) e manter rastreabilidade da decisão sobre terra crua.

**How to apply:** ao classificar C3, se o material for revestimento/reboco/gesso/cal/fachada → voltar e marcar C2 Rejeitado (token exato `[C2 Rejeitado]` nos comments, senão o filtro de pool não detecta). Para taipa/terra → C3 Aceito + nota de pré-marca. Ver [[rsl-coluna-rastreio-potencial]] e [[rsl-marcacao-R-vs-P]].
