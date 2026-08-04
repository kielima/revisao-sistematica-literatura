---
titulo: RSL PROGRESSO
descricao: Estado atual do banco de dados da RSL — verificado programaticamente
tags: [academico-e-pesquisa, revisao-sistematica, UHPC]
status: em-andamento
ultima_atualizacao: 2026-06-21
---

# Progresso da RSL — Estado atual

> Verificado programaticamente em 22/05/2026 pelo Claude/Cowork via leitura direta do Excel.
> Atualizado após auditoria PRISMA (2 passagens) + decisão HABERT 2026-05-23 — ver `00_REFERENCIAS/PRISMA/FLUXOGRAMA_PRISMA_2020_DOC.md`.

---

## ♻️ REFAZENDO A RSL — Triagem por PDF (iniciado em 2026-06-05)

> A RSL está sendo refeita. A triagem anterior foi feita por resumo (prefixo `R:`). A nova etapa aplica os mesmos critérios C1–C8 usando as **primeiras 2 páginas do PDF** de cada artigo (prefixo `P:`), para Elegíveis e Inconclusivos.

### Snapshot pré-triagem-PDF (estado da triagem por resumo — 2026-06-05)

Registrado programaticamente antes de qualquer alteração pela triagem por PDF:

| Status | N |
|--------|---|
| Elegível | **480** |
| Inconclusivo | **1.347** |
| Rejeitado (por resumo) | **575** |
| Duplicado | **2.623** |
| Sem acesso | **68** |
| **Total** | **5.093** |

**Artigos no escopo da triagem por PDF:** 480 + 1.347 = **1.827**

### Disponibilidade de PDFs (atualizado em 2026-06-05)

| Grupo | Com arquivo físico | Sem arquivo físico |
|-------|-------------------|-------------------|
| Elegíveis | **480 / 480** ✅ | 0 |
| Inconclusivos | **1.347 / 1.347** ✅ | 0 |

**Integrados em 2026-06-05:** 12 Inconclusivos + 4 Elegíveis (JONES, CUNNINGHAM, SVAJLENKA et al., PASSUELLO). Fonte alternativa para PASSUELLO: repositório LUME/UFRGS (SciELO estava fora do ar).

### Plano de execução — triagem por PDF

**Escopo:** Elegíveis (480) + Inconclusivos (1.347) = 1.827 artigos. Rejeitados por resumo ficam fora.

**Formato das células C1–C8:** preservar o valor `R:` existente e **acrescentar** o `P:` na mesma célula, separado por ` | `. Células que estavam em branco recebem só o `P:`.
- Exemplo célula com R:: `R:Aceito | P:Aceito` ou `R:Aceito | P:Rejeitado`
- Exemplo célula vazia: `P:Aceito` ou `P:Rejeitado`
- **Sem PDF / colisão:** NÃO pular. Claude auxilia a localizar o PDF correto (busca por DOI, título, autor). Só após resolver registra `P:`.

**Lógica em cascata:** aplicar os critérios na ordem C1 → C2 → … → C8. Um artigo rejeitado em Cn não é avaliado em Cn+1.

**Fonte para avaliação:** primeiras **2 páginas** do PDF (título, abstract, keywords, início da introdução). Se as 2 primeiras páginas não forem suficientes para decidir o critério, ler páginas adicionais até ter informação suficiente.

**⚠️ REGRA CRÍTICA — parar entre critérios:** ao concluir um critério, **parar e aguardar confirmação da Kiê** antes de iniciar o próximo. Não avançar automaticamente.

**Resultado final:** atualizar `status_triagem` conforme decisão consolidada R: + P:.

**⚠️ VERIFICAÇÃO DE PDF (regra para todos os critérios — TODOS os artigos, em TODOS os lotes):** para cada artigo do lote, verificar se o PDF aberto corresponde à linha (conferir título e primeiro autor na primeira página). Esta verificação é obrigatória, artigo por artigo, sem exceção. Se houver divergência (colisão de nomes ou arquivo errado):
1. Registrar `[Colisão PDF]` nos `comments` da linha afetada com descrição do problema
2. Tentar localizar o PDF correto na pasta (busca por palavras-chave do título)
3. Se não encontrado: **parar e reportar à Kiê** com DOI/título/autor para baixar o PDF correto — **nunca pular ou avaliar sem o PDF correto**
4. Aguardar confirmação antes de continuar a linha com colisão

**Coluna `material_C2`:** durante a aplicação do C2, preencher a coluna `material_C2` (inserida após C2 na planilha) com o material estrutural principal identificado no PDF. Artigos aceitos recebem o nome do material (ex: `concreto + cinza volante`, `CLT`, `UHPC`, `geopolímero`). Artigos rejeitados em C2 não preenchem esta coluna (motivo vai para `comments`).

**Justificativa de rejeições:** ao rejeitar um artigo em qualquer critério, registrar na coluna `comments` da planilha uma justificativa breve no formato:
`[Cn Rejeitado] <motivo específico>`
Exemplos:
- `[C1 Rejeitado] Publicado em 2003 (< 2006)`
- `[C2 Rejeitado] Estudo sobre painel de fachada — material não estrutural`
- `[C5 Rejeitado] Sem menção a CO₂, GEE ou ACV — foco em resistência mecânica`
Se já houver conteúdo na coluna `comments`, acrescentar ao final separado por ` | `.

### Decisões operacionais (registradas em 2026-06-05)

| Decisão | Valor |
|---------|-------|
| Ordem de processamento | Conforme ordem da planilha (`Articles`), de cima para baixo |
| Tamanho do lote | **50 artigos por lote** — salvar e reportar ao final de cada lote |
| Casos ambíguos | Parar e tirar dúvida com a Kiê antes de classificar |
| Definições dos critérios | Usar a aba `Critérios` do `articles_final.xlsx` como fonte canônica (ver abaixo) |
| Coluna `material_C2` | Inserida após C2 na planilha; registrar o material estrutural identificado para artigos aceitos em C2 |

### Convenção de sufixos para PDFs com colisão de nome (adicionado em 2026-06-05)

Quando múltiplos artigos do mesmo autor/ano existem na planilha, o arquivo PDF precisa de sufixo diferenciador:

- Arquivo já existente na pasta (sem sufixo) → corresponde à linha registrada primeiro na planilha
- Segundo artigo: `SOBRENOME et al., ANOb.pdf`
- Terceiro: `SOBRENOME et al., ANOc.pdf` — e assim por diante

**Ao baixar um PDF para linha com colisão:** salvar com o sufixo designado e atualizar a coluna `pdf` da linha correspondente na planilha.

**PDF com conteúdo incorreto (arquivo existe mas tem artigo errado):**
- Baixar o artigo correto para `BAIXADOS MANUALMENTE` com o nome definitivo correto (ex: `MING et al., 2024.pdf`)
- Usar `os.replace()` via Python para sobrescrever o arquivo errado atomicamente (não usar `rm` — permissão negada no ambiente Linux)
- O arquivo errado geralmente é um duplicado de outro artigo que já tem seu próprio PDF — verificar se alguma linha ficou sem o arquivo e corrigir
- Atualizar a coluna `pdf` na planilha e limpar qualquer nota `[PDF incorreto]` nos `comments`

**Caso especial — PDF pertence a linha fora do escopo (Rejeitado/Duplicado):**
- Atualizar a coluna `pdf` da linha correta (mesmo que Rejeitada) para registrar onde o arquivo está
- Não mover nem renomear o arquivo — apenas corrigir o mapeamento na planilha

**Mapeamento de colisões (✅ todas resolvidas em 2026-06-05):**

Todas as 10 colisões identificadas foram resolvidas: PDFs com sufixo b/c/d estão na pasta e mapeados na planilha (verificado programaticamente). C2 já preenchido para todas essas linhas.

### Definições completas dos critérios C1–C8 — TEXTO LITERAL da aba `Critérios` (fonte canônica)

> ⚠️ **Claude: consultar e CITAR esta redação literal a cada decisão de triagem.** Cascata C1→C8: artigo rejeitado em Cn não é avaliado em Cn+1. Colunas da aba: C# | Título | Descrição | Exemplo | Justificativa | Refinamentos/Decisões.

**C1 — Antes de 2006**
- **Descrição (literal):** "Estudos publicados antes de 2006"
- **Exemplo:** "ANO<2006"
- **Justificativa:** "São estudos publicados antes da primeira publicação da ISO 14040/44 e consequentemente não seguem métodos padronizado de análise."

**C2 — Material não estrutural**
- **Descrição (literal):** "Materiais que não são estruturais"
- **Exemplo (literal):** "Paredes, materiais asfálticos, elementos arquitetônico, etc..."
- **Justificativa (literal):** "Não são aplicáveis a grandes obras de infraestrutura urbana, foco dessa dissertação."
- **Refinamentos:** Materiais estruturais moldáveis ACEITOS: concreto, cimento, UHPC, HPC, geopolímero, concreto reciclado, argamassa estrutural, alkali-activated em contexto estrutural. Se artigo mistura material estrutural moldável com outros → ACEITO. Madeira estrutural industrializada ACEITA (CLT, glulam, LVL e equivalentes — geometria customizável). REJEITA-SE apenas o que não é estrutural moldável: painéis de revestimento/fachada, isolamento, asfalto, alvenaria decorativa, tijolo cerâmico não-estrutural, etc. **Decisão 2026-06-06 (Kiê):** artigos que NÃO são material de construção (captura/sequestro de CO₂, processos energéticos, descomissionamento, restauração costeira/ecológica) → REJEITADOS direto no C2 ("materiais que não são estruturais" + não aplicáveis a infraestrutura urbana).

**C3 — Materiais não moldáveis**
- **Descrição (literal):** "Materiais que não podem ser moldados conforme especifidades, em fábrica ou in loco."
- **Exemplo (literal):** "Blocos e tijolos."
- **Justificativa (literal):** "Não são aplicáveis a grandes obras de infraestrutura urbana, foco dessa dissertação."
- **Refinamentos:** NÃO moldáveis = forma padronizada única, sem personalização por projeto (blocos, tijolos, unidades de alvenaria) → REJEITADO. MOLDÁVEIS = conformados sob demanda, geometria por projeto (concreto, UHPC pré-fabricado, painéis/elementos pré-moldados de geometria variável; blocos de concreto customizáveis) → ACEITO. Concreto celular/espumoso (AAC, CLC, Ytong) = A REVISAR. AAC=Alkali-Activated Concrete → ACEITO; AAC=Autoclaved Aerated Concrete → A REVISAR.
- **⭐ Regra "bloco/tijolo de material aceito" (decisão Kiê 2026-08-03):** quando o bloco/tijolo é feito de um material já aceito em C2 (terra, solo-cimento, geopolímero — não cerâmica/concreto convencional de catálogo), a rejeição automática de "blocos e tijolos" não se aplica cegamente. Distinguir pela origem do processo: **prensado/comprimido sob demanda, sem padronização industrial de catálogo** (bloco de terra comprimida, ICEB, tijolo solo-cimento — tipicamente produção artesanal/local, dimensões ajustáveis ao projeto) → **ACEITO**. **Produto manufaturado padronizado vendido como substituto drop-in de um item de catálogo** (paver/bloco de pavimentação, "bloco emergente" comercializado como substituto de CMU padrão com dimensões fixas de catálogo) → **REJEITADO**. Aplicado em 2026-08-03: 3871, 4133, 4717 (Aceito) vs. 2996, 5078 (Rejeitado).

**C4 — Materiais não relacionados a construção**
- **Descrição (literal):** "Materiais que não são relacionados a construção civil"
- **Justificativa (literal):** "Não aderem ao tema da pesquisa"
- **Refinamentos:** REJEITADO: setores sem relação com construção civil (medicina, farmácia, biologia, agricultura, alimentos, eletrônica, embalagens, automóvel, aeronáutica, naval não-infra, energia solar/eólica com foco no painel/turbina). Também REJEITADO: processos industriais de produção de precursores SEM ACV do elemento final (produção isolada de clínquer, emissões de fornos de cimento, mineração de agregados sem produto final). ACEITO: qualquer artigo sobre concreto, cimento, UHPC ou materiais cimentícios em contexto de construção civil. BRANCO: infraestrutura genérica sem material especificado; LCA de sistemas completos sem foco em material.

**C5 — Não menciona emissões de GEE**
- **Descrição (literal):** "Não menciona análise de ciclo de vida (ACV), emissão de CO2 ou gases do efeito estufa"
- **Justificativa (literal):** "Unidade essencial para analise de impacto nas metas de redução de emissão de GEE."
- **Refinamentos:** Determinístico — sem branco. ACEITO se menciona ≥1 de: CO2/CO₂/carbon dioxide, GEE/GHG/greenhouse gas, ACV/LCA/avaliação do ciclo de vida, emissões/emissions (contexto carbono), carbon footprint/pegada de carbono, embodied carbon/carbono incorporado, GWP/aquecimento global, CO2eq, low-carbon, ReCiPe, decarbonization, carbon impact, carbon sequestration, bajo carbono, ELCA, SimaPro, OpenLCA, GaBi, ISO 14040/14044, carbon capture, descarbonização. REJEITADO: nenhum (durabilidade, resistência mecânica, eficiência energética sem CO₂, ACV de outros impactos sem GEE). EXCLUÍDOS por amplitude: 'environmental impact', 'eco-efficiency' (ambíguo → rejeita).

**C6 — Estudos regionalizados (material geograficamente restrito)**
- **Descrição (literal):** "Materiais cujo material principal tem produção geograficamente restrita e baixa escalabilidade global, impossibilitando aplicação em contextos internacionais."
- **Exemplo (literal):** "Bamboo/bambu como material estrutural principal; fibras naturais de produção regional sem dados globais (sisal, juta, cânhamo, kenaf, linho, agave, fibra de coco)"
- **Justificativa (literal):** "Materiais de produção geograficamente restrita não são aplicáveis a grandes obras de infraestrutura urbana em escala global, foco desta dissertação."
- **Refinamentos:** REJEITADO: produção geograficamente restrita sem escalabilidade global (bambu como material principal). A REVISAR: fibras naturais como reforço (sisal, juta, cânhamo, kenaf, linho, agave, coco) — verificar escalabilidade. ACEITO: produção global/exportável (concreto, cimento, UHPC, geopolímero, cinza volante, escória, cinza de casca de arroz, cimentícios com resíduos amplamente disponíveis); LCA com inventários regionais (critério é sobre o MATERIAL, não a origem dos dados). BRANCO: não envolve claramente nenhum desses materiais.

**C7 — Foco em energia operacional (sem emissões de produção)**
- **Descrição (literal):** "LCA de edifícios cujo foco principal são emissões de energia na fase de uso (B6/B7), sem dados de emissões incorporadas na produção do material (A1-A3/cradle-to-gate)."
- **Exemplo (literal):** "Artigos de desempenho energético de edifícios (HVAC, thermal performance, U-value) sem embodied carbon ou cradle-to-gate."
- **Justificativa (literal):** "Emissões incorporadas na produção do material são a unidade essencial para comparação entre materiais estruturais."
- **Refinamentos:** ACEITO: embodied carbon, embodied energy, cradle-to-gate, A1-A3, manufacturing/production phase, upstream. REJEITADO: foco em operational energy, HVAC, thermal performance, heating & cooling, energy performance of buildings — sem nenhum padrão ACEITO. BRANCO: ambíguo.

**C8 — Artigos de opinião sem dados primários**
- **Descrição (literal):** "Editoriais, opinion papers, commentaries, perspectives, cartas ao editor — sem metodologia nem dados originais de ACV. Revisões sistemáticas e metanálises são ACEITAS."
- **Exemplo (literal):** "Editorial, Letter to Editor, Erratum, Retracted, Correction; viewpoint/commentary sem metodologia."
- **Justificativa (literal):** "Sem metodologia ou dados originais, não contribuem com dados primários para extração de CO₂/fck."
- **Refinamentos:** REJEITADO (document_type): Editorial, Editorial Material, Erratum, Retracted, Correction, Letter, Note, Short Communication. REJEITADO (title/abstract): "letter to the editor", "opinion paper", "viewpoint", "commentary", "editorial". NÃO rejeitar: Review, Systematic Review, Meta-analysis, Literature Review.

### Progresso da triagem por PDF

> ✅ Pré-requisito concluído: todos os 480 Elegíveis e 1.347 Inconclusivos têm arquivo físico.
> ⚠️ **Indicador de progresso (atualizado 2026-06-06):** "re-triados" = artigos com `material_C2` preenchido (Aceito) **ou** `[C2 Rejeitado]` nos comments (Rejeitado). NÃO se usa mais "tem P:" como indicador — pela nova convenção, decisões resolvidas por título/resumo ficam em `R:` (não `P:`). Ver memória `rsl-marcacao-R-vs-P`.

| Critério | Status | Rejeitados C2 | Re-triados | Pendentes |
|----------|--------|----------------|-------------------|-----------|
| C1 — Antes de 2006 | ✅ Concluído (2026-06-05) | 0 | 1.827 | 0 |
| C2 — Material não estrutural | ✅ Concluído (2026-06-12) | 146 | **1827** | **0** |

> **🏷️ Nova coluna `rastreio_potencial_futuro` (col. 33, criada 2026-06-12).** Marca tecnologias promissoras independentemente da decisão C2, em 5 categorias (tags separadas por `; `): **biocimento** (MICP/EICP/biocimentação — potencial estrutural futuro), **fator_clinquer** (redução/substituição do fator clínquer, LC3/argila calcinada), **aglomerante_alternativo** (geopolímero, álcali-ativado, MgO, CSA + SCM parcial: cinza volante, escória, sílica, metacaulim, etc. — abrangência AMPLA, decisão Kiê), **carbonatacao_captura** (carbonatação/sequestro de CO2 no próprio material, self-healing), **outra** (outras tecnologias promissoras com potencial estrutural futuro — aplicada caso a caso na leitura). Contagem retroativa (1.584 triados): biocimento 6, fator_clinquer 21, aglomerante_alternativo 359, carbonatacao_captura 93.
>
> **Regra biocimento (decisão Kiê 2026-06-12):** biocimentação standalone (MICP/EICP estabilizando solo/areia ou "growing bricks") continua **C2 Rejeitado** (não vira viga/pilar hoje) **+ marca** `biocimento`. Biocimento como aditivo em concreto estrutural (ex.: concreto autocicatrizante por bactérias, row 3242) → **C2 Aceito** + marca. Reclassificados nesta revisão: 3538 e 4647 (eram Aceito → C2 Rejeitado). Aplicar a coluna em todos os lotes daqui pra frente.
| C3 — Material não moldável | ✅ CONCLUÍDO (2026-06-13) | 41 | 1672 | **0** |
| C4 — Não relacionado a construção | ✅ CONCLUÍDO 2026-06-14 (leitura 3+ páginas) | 97 | 1631 | **0** |
| C5 — Não menciona GEE/ACV/CO₂ | ✅ CONCLUÍDO 2026-06-21 (regra: OPÇÃO A) | **43** | **1548** | **0** |
| C6 — Material geograficamente restrito | ✅ CONCLUÍDO (2026-06-21) | 8 | **1.488** | **0** |
| ~~C7 — Foco em energia operacional~~ | ❌ **REMOVIDO (2026-06-22)** | — | — | — |
| C8 — Opinião sem dados primários | ✅ **CONCLUÍDO (2026-06-22)** | **2** | **1.339** | **0** |

**✅ C2 CONCLUÍDO (2026-06-12):** todos os 1.827 in-scope (Elegível/Inconclusivo, C1 ok) triados em C2. 146 C2 Rejeitado; ~1.681 C2 Aceito (dos quais vários encaminhados a C3/C4/C7/C8 e marcados na coluna de rastreio). Coluna `rastreio_potencial_futuro` preenchida em todo o conjunto. **Próximo critério: C3 (materiais não moldáveis)** — começar do início da ordem.

### Progresso da triagem por PDF — Critério C3 (materiais não moldáveis)

> **Início 2026-06-12.** Definição literal (aba Critérios): *"Materiais que não podem ser moldados conforme especifidades, em fábrica ou in loco."* Ex.: *"Blocos e tijolos."* NÃO moldável (forma padronizada única, sem personalização — blocos, tijolos, unidades de alvenaria) = **Rejeitado**; MOLDÁVEL (conformado sob demanda, geometria por projeto — concreto, UHPC, pré-moldados/painéis de concreto de geometria variável, madeira CLT/glulam) = **Aceito**. Bloco de concreto customizável por projeto = Aceito. AAC=Alkali-Activated Concrete → Aceito; AAC=Autoclaved Aerated/celular/espumoso → decidir caso a caso lendo PDF (decisão Kiê).
>
> **📌 Nota histórica (Kiê, 2026-06-13):** na aplicação MANUAL de critérios feita anteriormente (triagem por título/resumo), **estudos que usaram blocos/tijolos de agregados foram descartados** — ou seja, estudos cujo produto é bloco/tijolo (mesmo feitos a partir de agregados reciclados/alternativos) foram rejeitados. Isso é coerente com as rejeições de C3 desta passada por PDF (blocos/tijolos = não moldáveis). **Distinção CONFIRMADA pela Kiê (2026-06-13):** quando o bloco/tijolo é apenas a FONTE de agregado triturado usado DENTRO de concreto moldável (produto final = concreto), **mantém C3 Aceito** (ex.: 4511, 4479, 4408). Apenas quando o bloco/tijolo é o PRODUTO → C3 Rejeitado. A nota histórica da triagem manual se refere ao bloco/tijolo como produto.
>
> **Universo C3 (decisão Kiê 2026-06-12):** TODO artigo aprovado em C2 é avaliado em C3, **independentemente** de já ter sido reprovado em C4/C7/C8 (essas reprovações foram adiantadas para facilitar trabalho posterior e NÃO excluem da avaliação de C3 — C3 vem antes na cascata). Pool = **1.669** (1.681 C2 Aceito − 12 já com veredito C3). **Método (decisão Kiê):** reabrir e verificar o PDF (título+1º autor) de cada artigo antes de decidir — mesmo rigor do C2. Lotes de 50.

**Lote C3-01 (2553–2674): ✅ 50/50** — todos **C3 Aceito** (materiais moldáveis). Concreto/argamassa/UHPC/geopolímero/CLT-mass timber/compósito madeira-concreto/light steel frame/terra apiloada-earthbag (conformada in loco)/painéis e pré-moldados de concreto/CTB/backfill cimentício. Sem blocos/tijolos, sem colisão, sem AAC/celular. 2673 (Felicioni) lido por OCR (PDF cid-encoded). Acumulado C3: 62 decididos (12 Rej + 50 Aceito), 1.619 pendentes.

**Lote C3-02 (2675–2791, 100): ✅ 100/100** — 97 C3 Aceito + **3 C3 Rejeitado** (2677 Galan-Marin: paredes de alvenaria de blocos de solo estabilizado/tijolo/bloco de concreto; 2767 Pesta 2020: blocos de alvenaria de concreto reutilizáveis; 2768 Pesta 2022: bloco de concreto leve). Falsos-positivos resolvidos (slab/panel/precast/prefab/earth em contexto de concreto moldável; 2783 jack arch = peça pré-fab de argamassa → Aceito; 2714 argamassa geopolimérica → Aceito; 2749 geopolímero de resíduos → Aceito; 2769 muros de contenção de concreto → Aceito). Método: verificação automática de autor + sinalização de termos; leitura aprofundada dos críticos. Acumulado C3: 162 decididos (15 Rej + 147 Aceito), 1.519 pendentes.

**Lote C3-03 (2792–2975, 100): ✅ 99/100 (1 pendente)** — 94 C3 Aceito + **5 C3 Rejeitado** (2815 Volk: AAC autoclavado pós-demolição — unidades aeradas padronizadas, decisão caso-a-caso; 2816 Wolfova: paredes de alvenaria de carga tijolo/bloco aerado; 2825 Zhang: tijolos de concreto geopolímero; 2830 Zhao: blocos de construção de agregado reciclado; 2880 Meshram: paving blocks/pavers de geopolímero red mud). Aceitos os comparativos que assessam concreto moldável junto (2801 painéis bloco-cerâmico×concreto-armado; 2844 abóbadas de alvenaria×estruturas de concreto), pórticos RC (2805 bahareque/RC), agregados leves como ingrediente (2926), 3D printing (2917), revisão de biochar cobrindo concreto (2933). **⏸️ 2897 PENDENTE (sem PDF):** di Summa et al., "A holistic life cycle design approach... concrete structures", DOI 10.1002/suco.202300645 (Wiley/Structural Concrete) — `pdf=Sem acesso`, marcado "[colisão PDF]". Material = concreto estrutural (moldável) mas não classificado sem leitura do PDF. Acumulado C3: 261 decididos (20 Rej + 241 Aceito), 1.420 pendentes (inclui 2897).

> **2897 RESOLVIDO (decisão Kiê 2026-06-12; status padronizado 2026-06-21):** sem acesso ao PDF é definitivo. `pdf=Sem acesso` mantido, removido do pool. **2026-06-21:** `status_triagem` migrado de `Recusado`→`Rejeitado` (padronização — não existe mais "Recusado") e P:Aceito indevido removido de C1.

**Lote C3-04 (2979–3136, 100): ✅ 100/100** — 97 C3 Aceito + **3 C3 Rejeitado** (2983 Patrisia: produtos de concreto = tijolos e telhas; 3085 Marcelino-Sadaba: blocos e tijolos de argila estabilizada; 3093 Miao: compósito solo-lignina como tijolo/unidades de alvenaria não estruturais). Aceitos: 3045 (sistemas de parede que incluem paredes de concreto armado moldável), 3121 (resíduo de pedra ornamental em SCC/argamassas/concreto além de blocos), 2989 (geopolímero — tijolos só como corpo de prova de ensaio), 3051 (CO2→metanol, não-construção → C4 trata). Acumulado C3: 361 decididos (23 Rej + 338 Aceito), 1.319 pendentes.

**Lote C3-05 (3138–3274, 100): ✅ 100/100** — 99 C3 Aceito + **1 C3 Rejeitado** (3174 Liu: blocos de concreto/paredes de alvenaria derivados de lodo — unidades padronizadas não moldáveis). Aceitos: 3159 (taipa/rammed earth conformada in situ), 3179 (concreto álcali-ativado caracterizado como concreto — blocos só na literatura), 3180 (compósito geopolimérico red mud+escória), 3240 (argamassas/rebocos de cal), 3273 (argamassa com caroço de azeitona moído). 3259 (Song, exergia indústria de cimento) lido por OCR (PDF cid-encoded). Acumulado C3: 461 decididos (24 Rej + 437 Aceito), 1.219 pendentes.

> **🔧 Correção C2 + auditoria (2026-06-12, a pedido da Kiê):** revendo 3240 e 3273, identifiquei que são materiais de **revestimento NÃO estruturais** (3240 = argamassas/rebocos/gessos de cal; 3273 = argamassa de fachada com caroço de azeitona) — erros de C2 de sessão anterior. Ambos **reclassificados para C2 Rejeitado** (saem do funil C3; C3 anterior anulado). Token canônico `[C2 Rejeitado]` aplicado. C2 Aceito: 1.680 → **1.678**.
> **Taipa/rammed earth (3159):** mantida **C3 Aceito** (estrutural + moldável, conformada in loco), mas **pré-marcada nos comments para rejeição no critério de aplicabilidade a grandes obras de infraestrutura** (decisão Kiê). Aplicar o mesmo a construção em terra crua daqui pra frente.
> **Varredura de revestimentos nos C2-Aceito vivos:** 9 candidatos sinalizados; 6 falsos positivos (concreto/cimento com gesso/gipsita como aditivo, segmentos de túnel pré-moldados, pontes); 3019 (bloco vazado) já estava C3 Rejeitado; **4455 RESOLVIDO (PDF lido 2026-06-12):** compósito ternário gesso-cimento-pozolana p/ impressão 3D, 37 MPa (comparável a concreto), durável em água — **ESTRUTURAL** → C2 Aceito confirmado + C3 Aceito (moldável por extrusão); rastreio aglomerante_alternativo. Acumulado C3: **460 decididos (24 Rej + 436 Aceito), 1.218 pendentes.**

**Lote C3-06 (3276–3407, 100): ✅ 100/100** — 97 C3 Aceito + **3 C3 Rejeitado** (3300 Di Maria: blocos isolantes OPC/AAC com goethita; 3324 Apithanyasai: tijolos de geopolímero/pavement bricks; 3332 Adu: tijolos de laterita + blocos de sancrete). Aceitos: 3276 (compara paredes incl. concreto armado moldável), 3307/3308 (painéis sanduíche UHPC), 3346 (concreto cast-in-place reaproveitado/cortado p/ passarela), 3348 (hempcrete p/ aplicação estrutural, moldável). Não-construção que passam C3 (→ C4): 3311 (S/S resíduo perigoso), 3316 (poço de petróleo), 3342 (fotocatalisador p/ tratamento de água). Sem revestimentos não estruturais detectados. Acumulado C3: 560 decididos (27 Rej + 533 Aceito), 1.118 pendentes.

**Lote C3-07 (3408–3523, 100): ✅ 100/100** — 97 C3 Aceito + **1 C3 Rejeitado** (3523 Jury: blocos de concreto portantes à base de miscanthus) + **1 reclassificado C2 Rejeitado** (3497 Momotaz: concreto de meio-fio/kerb — não estrutural, consistente com 4689) + **1 Duplicado** (3454 = duplicata do 3453, mesmo DOI). Aceitos: 3419 (copo de café como areia em concreto), 3511 (3D printing de concreto geopolímero), 3491 (blindagem radiológica incl. parede cast-in-place RC), 3449 (lajes de concreto cortadas reaproveitadas). 3498 (técnicas ancestrais adobe/cob/taipa) → Aceito + pré-marca de infraestrutura (terra crua). C2 Aceito: 1.678 → **1.676**. Acumulado C3: 658 decididos (28 Rej + 630 Aceito), 1.018 pendentes.

**Lote C3-08 (3524–3659, 100): ✅ 100/100** — 95 C3 Aceito + **4 C3 Rejeitado** (3585 paver blocks de concreto permeável; 3617 tijolos de adobe; 3619 tijolos estruturais/pavimento c/ aglomerante de amido; 3634 paredes de blocos/tijolos) + **1 reclassificado C2 Rejeitado** (3597 Zhou: revestimento geopolímero de resfriamento radiativo — não estrutural; material_C2 anterior não conferia com o PDF). 6 PDFs cid-encoded lidos por OCR (3535/3536 shotcrete/3546 pré-fab/3551/3555/3556 calçada-stamped concrete). 3556 incluía concreto estampado moldável → Aceito. ⚠️ **7 arquivos são apenas RESUMO GRÁFICO (imagem JPEG), sem texto completo** (3589 Adrianto, 3592 Georgiades, 3635 Millward-Hopkins, 3637 Quina, 3646 Soleimani, 3648 Toniolo, 3653 Tushar) — decididos em C3 pela imagem+metadados (todos moldáveis/cimentícios ou não-construção), mas **precisam ser re-baixados como full-text antes de C4/C5/C7/C8**. C2 Aceito: 1.676 → **1.675**. Acumulado C3: 757 decididos (32 Rej + 725 Aceito), 918 pendentes.

> **🔁 Full-text re-baixado e integrado (2026-06-13):** varredura da pasta inteira achou **18 arquivos que não eram PDF de texto** (10 imagens JPEG, 5 HTML, 3 multipart). **17 re-baixados e integrados** (13 Elsevier via CAPES + ACS Subraveti row 3719 OA-PMC + 3 teses BR: Iunes 5034, Invidiata 5049, Azevedo 5054). PDFs antigos (imagem/HTML) arquivados em `BAIXADOS MANUALMENTE/PARA VERIFICAR`. Resta apenas **GETTU 3233 (imagem)** — é **Duplicado**, não precisa. Todos os full-text agora disponíveis para C4/C5/C7/C8.

**Lote C3-09 (3660–3802, 100): ✅ 98/100 (2 colisões pendentes)** — 93 C3 Aceito + **4 C3 Rejeitado** (3675 CleanTechBlock sandwich-blocks; 3686 blocos miscanthus-cal; 3723 tijolos de argila cozida; 3770 alvenaria tijolo×AAC) + **1 C2 Rejeitado** (3669 painéis de gesso/cimento não estruturais). Aceitos: 3750 (praça — inclui concreto cast-in-place), 3782 (10 casas incl. madeira), 3791 (CO2 mineralization incl. ready-mix). **⏸️ 2 COLISÕES (PDF errado, não classificados):** 3707 (arquivo = pavimento semi-flexível; deveria ser Khan *repulping reject*, DOI 10.1016/j.wasman.2022.10.026) e 3712 (arquivo = revisão Wu; deveria ser Senevirathna *MgO de salmoura*, DOI 10.1016/j.wsee.2025.01.001) — re-baixar os corretos. C2 Aceito: 1.675 → **1.674**. Acumulado C3: 854 decididos (36 Rej + 818 Aceito), 820 pendentes.
> **Colisões 3707/3712 RESOLVIDAS (2026-06-13):** PDFs corretos baixados e integrados. 3707 = Khan *repulping reject* (Waste Management, DOI 10.1016/j.wasman.2022.10.026) → C3 Aceito (não-construção, C4 trata). 3712 = Senevirathna *MgO de salmoura* (DOI 10.1016/j.wsee.2025.01.001) → C3 Aceito (aglomerante moldável; nome do arquivo corrigido WU→SENEVIRATHNA; tag aglomerante_alternativo). Arquivos errados arquivados em PARA VERIFICAR. **Acumulado C3: 856 decididos (36 Rej + 820 Aceito), 818 pendentes.**

**Lote C3-10 (3803–3942, 100): ✅ 100/100** — **100 C3 Aceito, 0 Rejeitado.** Concreto/cimento/agregados reciclados/UHPC/madeira/metodologia/não-construção (MSW). 3805 (edifício c/ pórtico de concreto armado — CMU/AAC só vedação) → Aceito; 3896 (taipa/rammed earth álcali-ativada, Meek) → Aceito + pré-marca de infraestrutura (terra crua); 3883 (Pesta — agregados reciclados de RCD) → Aceito. Falsos-positivos "earth" = earthquake/Earth. Sem colisões. Acumulado C3: 956 decididos (36 Rej + 920 Aceito), 718 pendentes.

**Lote C3-11 (3943–4090, 100): ✅ 100/100** — 98 C3 Aceito + **1 C3 Rejeitado** (3980 Alegbe: comparação de materiais de parede HCB/mud brick/tijolo/bambu, sem opção moldável) + **1 C2 Rejeitado** (4085 Dossena: argamassa de selagem/assentamento, não estrutural). Aceitos: 4086 (ágata em argamassas/concretos), 4052 (concreto com entulho de alvenaria), 3983 (dataset LCI), RAP/agregados reciclados/cimentos. Sem colisões. C2 Aceito: 1.674 → **1.673**. Acumulado C3: 1055 decididos (37 Rej + 1018 Aceito), 618 pendentes.

**Lote C3-12 (4094–4240, 100): ✅ 100/100** — 97 C3 Aceito + **2 C3 Rejeitado** (4094 Caldas: blocos estruturais cerâmicos/concreto; 4195 Raihan: tijolos cimentícios/argila) + **1 C2 Rejeitado** (4239 Almeida: argamassa de revestimento/reboco/rejunte). Aceitos: 4135 (mecânica concreto+pedra, inclui concreto), 4209 (espuma geopolimérica fundível), 4143 (ferroviária — concreto/geopolímero); vários não-construção (4127 microalgas, 4129 truta, 4132 esgoto, 4237 óleo) passam C3→C4. Sem colisões. C2 Aceito: 1.673 → **1.672**. Acumulado C3: 1154 decididos (39 Rej + 1115 Aceito), 518 pendentes.

**Lote C3-13 (4241–4382, 100): ✅ 100/100** — 98 C3 Aceito + **2 C3 Rejeitado** (4241 Reyes-Quijije: blocos de concreto aerado/celular; 4368 Estokova: paredes portantes de concreto celular/aerado). Aceitos: 4249 (revisão smart construction — 3D printing/pré-fab), 4379 (concreto leve para casas), 4336 (LC3), 4284 (pré-fab RC/madeira/aço). Sem colisões, sem revestimentos. Acumulado C3: 1254 decididos (41 Rej + 1213 Aceito), 418 pendentes.

**Lote C3-14 (4389–4537, 100): ✅ 100/100** — **100 C3 Aceito, 0 Rejeitado.** Concreto/cimento/argamassa estrutural/agregados reciclados/geopolímero/eco-cimento/revisões. 4402 (revisão de alvenaria — inclui precast/XLAM), 4500 (argamassa p/ pré-fab estrutural), 4511 (resíduo de bloco como agregado em concreto), 4479 (blocos britados como agregado) — todos os "blocos/tijolos" eram fonte de agregado ou contexto de revisão. Sem colisões. Acumulado C3: 1354 decididos (41 Rej + 1313 Aceito), 318 pendentes.

**Lote C3-15 (4539–4686, 100): ✅ 100/100** — **100 C3 Aceito, 0 Rejeitado.** Concreto/cimento/geopolímero/casas de madeira (estrutura de madeira+concreto)/clínquer. "masonry/brick" eram comparadores em LCA de moradias (4562, 4607, 4626 — estruturas de madeira/concreto armado). Falsos-positivos: gesso (revisão/ponte), 'render' (mass timber). Sem colisões. Acumulado C3: 1454 decididos (41 Rej + 1413 Aceito), 218 pendentes.

**Lote C3-16 (4690–4854, 100): ✅ 100/100** — **100 C3 Aceito, 0 Rejeitado.** Concreto/cimento/SCM/agregados reciclados/concreto espumado/madeira-aço/biochar/revisões. 4837 ("block type" = tipologia de edifício flat/T-type c/ concreto armado, não bloco de alvenaria), 4738 (revisão cimentícios incl. concreto), 4814 (restauração incl. ready-mix). **🔁 4826 RESOLVIDO:** arquivo `WU et al., 2025.pdf` recuperado de PARA VERIFICAR — pertencia a este row (revisão de materiais reciclados na construção), não ao 3712; copiado de volta à pasta principal. Acumulado C3: 1554 decididos (41 Rej + 1513 Aceito), 118 pendentes.

**Lote C3-17 FINAL (4855–5093, 118): ✅ 116 C3 Aceito + 1 C2 Rejeitado (4907 Zhou: geopolímero de metacaulim p/ revestimento de resfriamento radiativo — não estrutural) + 1 colisão (4938).** 4993 (Wagner, paredes timber-concrete-composite/CLT) lido por OCR → Aceito. 5034 (dissertação taipa Iunes) → Aceito + pré-marca infraestrutura. 5042 (hidrelétrica, concreto) → Aceito.

> **🧩 Cluster de PDFs trocados resolvido (2026-06-13):** três rows tinham PDFs cruzados. **4907** (metakaolin geopolymer, energy-proceedings DOI 10.46855/energy-proceedings-11075) = PDF correto → C2 Rejeitado (revestimento radiativo). **3597** (título real: *LCA of recycling copper slags as cement replacement*, Zhou, DOI 10.1016/j.resconrec.2024.107591) estava com o PDF do geopolímero → minha rejeição C2 anterior foi **ANULADA**; vira colisão pendente (substituição de cimento = MOLDÁVEL). **4938** (De Toldi & Pestre, *cut-stone for low-carbon buildings*, DOI 10.5334/bc.278) estava com o PDF de concreto de escória de cobre do Filipovic → colisão. **Correção (2026-06-13):** o PDF do Filipovic (copper slag aggregate concrete) NÃO era órfão — pertence à linha **4948** (DOI 10.5937/GRMK2202057F, já C3 Aceito); foi **restaurado** à pasta principal. A 4938 apenas apontava por engano para o mesmo arquivo. Único arquivo que permanece em PARA VERIFICAR: a **duplicata** do geopolímero do Zhou (`ZHOU et al., 2024_dup...`), pois o row 4907 já tem a própria cópia — pode ser descartada mediante autorização.

### Progresso da triagem por PDF — Critério C4 (não relacionado a construção)

> **⚠️ RECOMEÇO DO C4 (decisão Kiê 2026-06-14):** a 1ª passada (lotes C4-01..04, 500 itens, método por resumo/metadados) foi **ANULADA** — encontrados erros (ex.: 3311, 3257 rejeitados indevidamente; resíduos usados em concreto). C4 zerado (marcas P: e notas C4 datadas removidas; R: original e rastreio do C2 preservados). **NOVO MÉTODO OBRIGATÓRIO:** ler as **3 PRIMEIRAS PÁGINAS de cada PDF**; se não der para classificar, **continuar lendo as páginas seguintes** até ter conteúdo suficiente; dúvida real → **PARAR e perguntar à Kiê**. NUNCA decidir por resumo/título isolado. Pool = 1.631 (todos C3-Aceito). Carimbo da nova passada = `2026-06-14`.
>
> **C4-REDO Lote 1 (2553–2794): ✅ 147 Aceito + 3 Rej** (2640 clínquer, 2662 eólica/H2, 2676 combustível/clínquer). **C4-REDO Lote 2 (2795–3072): ✅ 139 Aceito + 11 Rej** (2845 gestão de resíduos, 2888 fotovoltaica, 2965 agricultura, 2970 pesca, 2973 resíduo plástico, 2975 forragem, 2990 microalgas/combustível, 3004 microalga-aviação, 3006 Power-to-Gas, 3012 aquicultura, 3051 CO2→metanol). **Correções vs 1ª passada:** 3005 (carbonação de escória BOF como substituto de cimento) → Aceito (era Rej). Acumulado C4-REDO: 300 revisados (14 Rej + 286 Aceito), 1.331 pendentes.
>
> **C4-REDO Lote 3 (3073–3294): ✅ 146 Aceito + 4 Rej** (3077 ACV de produção de clínquer+cimento/Etiópia→precursor [tag fator_clinquer]; 3080 proteção contra geada na viticultura; 3113 predição de temperatura de esterco/laticínio; 3259 contabilidade exergética da indústria de cimento [OCR, tag outra]). **Aceito por adendo/decisão:** 3257 (carbonação mineral→agregado [tag carbonatacao_captura]); 3268 (geopolímero de RCD p/ ambiente construído, energia renovável só como vetor de otimização [tag aglomerante_alternativo]); **3252 (ACV de estação de tratamento de água — infraestrutura/obra civil, decisão Kiê 2026-06-14 → Aceito + "A revisar"; regra geral p/ ETAs/ETEs/instalações).** Acumulado C4-REDO: 450 revisados (18 Rej + 432 Aceito), 1.181 pendentes.
>
> **C4-REDO Lote 4 (3297–3488): ✅ 130 Aceito + 20 Rej.** Rejeitados off-topic: 3299 (eólica offshore), 3310 (biocombustível/cinza de carvão—política energética), 3316 (poço de petróleo), 3320 (fim de vida de turbinas eólicas), 3342 (fotocatalisador p/ tratamento de água), 3350 (frutas), 3376 (RSU São Paulo), 3382 (frutos do mar), 3415 (RSU Moscou), 3432 (planta P2X), 3441 (agricultura urbana), 3468 (CO2→metanol), 3476 (metanol defossilizado), 3482 (H2 de gás/biogás). Rejeitados precursor/cimento: 3297 (fuel switching no cimento→outra), 3369/3408/3412 (clínquer CSA/consequencial→fator_clinquer), 3452 (combustível alternativo no cimento→outra). **Decisões Kiê 2026-06-14:** 3400 (pá eólica co-processada substituindo matéria-prima do clínquer → **Aceito** pelo adendo); 3383 (cinza de incineração por S/S com cimento p/ imobilização/descarte → **Rejeitado**, gestão de resíduo, distinto do 3311). Aceitos notáveis: 3439 (torre eólica em concreto por AM), 3473 (ETE→infra), 3474 (pás eólicas em 2ª vida→adendo), 3478 (concreto de RCD), 3329 (geopolímero+nanofibras). Acumulado C4-REDO: 600 revisados (38 Rej + 562 Aceito), 1.031 pendentes.
>
> **C4-REDO Lote 5 (3491–3708): ✅ 134 Aceito + 16 Rej.** Rejeitados off-topic: 3562 (biochar/cimento como adsorvente em águas pluviais), 3569 (microalgas), 3573 (lodo de esgoto/OPTIMASS), 3578 (embalagem plástica), 3583 (inventário de turbinas eólicas), 3586 (estruvita/lodo), 3611 (minerais críticos PT), 3631 (eólica offshore), 3632 (biogás), 3637 (gestão de cinzas de incineração), 3639 (detritos espaciais), 3649 (alimentos), 3658 (H2/metanol), 3670 (fábrica fotovoltaica), 3677 (aviação). Precursor: 3596 (clínquer belita de AAC pós-demolição→fator_clinquer). **Decisão Kiê 2026-06-14:** 3699 (ACV de aterro sanitário de RSU) → **Aceito** porque o inventário documenta o concreto com fluxos de entrada/saída (3,10 kg/t resíduo, ecoinvent). **Nova regra:** instalação/sistema com concreto documentado no LCI (fluxos) qualifica para C4. Aceitos notáveis pelo adendo: 3579 (plantas invasoras→concreto), 3584 (cinza fora de spec→UHPC), 3648 (escória de aço→cimento/pavimento), 3704 (pá eólica→co-processamento em cimento, como 3400), 3660 (cimento de fosfato de magnésio com resíduo de aço). Acumulado C4-REDO: 750 revisados (54 Rej + 696 Aceito), 881 pendentes.
>
> **🔧 Re-revisão sob a REGRA DO INVENTÁRIO (Kiê 2026-06-14):** aba Critérios atualizada (linha C4) com todas as nuances (método de leitura 3+pág; precursor vs elemento final; adendo/co-processamento; ETA/ETE; e a regra do inventário do 3699). Re-checados os 54 rejeitados do C4: os de gestão de resíduos / energia-química (3006, 3432, 2845, 2973, 3376, 3415, 3637) têm concrete≈0 (cimento só como rota de processo/descarte) → permanecem rejeitados. **6 corrigidos para Aceito** por documentarem concreto com fluxos quantificados no inventário: 2888 (PV, kt/GW + EF), 3299 (fundações concreto vs aço, eólica offshore), 3583 (concreto em ton/MW), 3631 (fundação 7,04E+08 kg + estacas 5,04E+07 kg), 2662 (concreto de fundação com EF), 3320 (concreto de fundação em t + reciclagem como agregado). Carimbo da correção = `[C4 CORRIGIDO 2026-06-14 -> Aceito]`. **Rejeitados C4 agora: 48** (696→702 Aceito).
>
> **C4-REDO Lote 6 (3709–3914): ✅ 140 Aceito + 10 Rej.** Rejeitados: 3715 (gestão de amianto), 3771 (reciclagem de fósforo), 3784 (ensaio ética/materiais), 3866 (survey de relatórios ICV por setor), 3716 (Power-to-Hydrogen), 3717 (etanol+CCS), 3734 (cimento→CO2→metanol→outra), 3735 (CCU em cimento→carbonatacao_captura), 3762 (reúso de CO2), 3765 (palestra utilização de CO2). Aceitos pela regra do inventário/adendo/infra: 3709 (ETE), 3757 (cleanroom), 3846 (estacionamento — concreto no inventário), 3774 (pá eólica→cimento), 3884 (lodo→cimento/concreto), 3841 (fibra de vidro de pá→sílica no cimento). Acumulado C4-REDO: 900 revisados (58 Rej + 842 Aceito), 731 pendentes.
>
> **C4-REDO Lote 7 (3915–4145): ✅ 136 Aceito + 14 Rej.** Rejeitados: 3927 (RDF→combustível no cimento→outra), 3929 (bateria), 3949 (madeira/floresta), 3951 (inseticida em arena de concreto/entomologia), 3959 (biodiversidade), 3967 (ímãs de terras-raras), 4018 (cirurgia), 4032 (resíduo de perfuração), 4056 (compostagem), 4061 (lodo de celulose — cimento só descarte), 4083 (biossólidos — cimento só combustível), 4122 (pás eólicas), 4127 (microalgas), 4129 (aquicultura de truta). Aceitos notáveis: 3971 (cinza de madeira→SCM), 4052 (agregado reciclado), 4023 (fibra de carbono na construção), 4132 (tratamento de esgoto onsite), 3978 (edifícios/telhados). Acumulado C4-REDO: 1.050 revisados (72 Rej + 978 Aceito), 581 pendentes.
>
> **C4-REDO Lote 8 (4152–4364): ✅ 141 Aceito + 9 Rej.** Rejeitados: 4165 (resíduo de saúde), 4178 (produção de cimento c/ combustível alternativo→outra), 4179 (mineração de calcário→fator_clinquer), 4210 (CCU→químicos orgânicos), 4212 (emissões negativas geoquímicas→carbonatacao_captura), 4213 (gestão de RSU), 4222 (templates CCU), 4225 (combustível de aviação), 4228 (suplementação animal). Aceitos notáveis: 4156/4157 (ETE individual/fossas sépticas — infra saneamento), 4243 (materiais de construção p/ cobertura de aterro), e muitos de concreto verde/UHPC/RHA/fly ash/geopolímero. Acumulado C4-REDO: 1.200 revisados (81 Rej + 1.119 Aceito), 431 pendentes.
>
> **🔧 Correção 4165 (Kiê 2026-06-14):** 4165 (valorização de resíduo de saúde) → **CORRIGIDO para Aceito** — uma das rotas de valorização é o plástico tratado como insumo de *reinforced cement / reinforced asphalt* (resíduo como material em cimento → adendo). **Nuance reforçada:** resíduo off-topic usado como MATERIAL/INSUMO em cimento/concreto (mesmo sendo uma de várias rotas avaliadas) = Aceito; resíduo usado só como COMBUSTÍVEL no forno de cimento, ou cimento usado só para imobilização/descarte = Rejeitado. Lote 8 ajustado: 142 Aceito + 8 Rej. Aplicada a nova nuance retroativamente: **4061** (lodo de celulose — reciclagem da cinza na indústria de cimento) e **3637** (cinzas de incineração → agregados leves/glass-ceramics/cimento/concreto) → CORRIGIDOS para Aceito. Acumulado C4-REDO: 1.200 revisados (78 Rej + 1.122 Aceito), 431 pendentes.
>
> **Rastreio: nova categoria `combustivel` (Kiê 2026-06-14)** — resíduo/combustível alternativo queimado no forno de cimento (ACV) migrou de `outra` para `combustivel`: 2676, 2990, 3297, 3452, 3927, 4083, 4178. Categorias do rastreio agora: fator_clinquer, combustivel, carbonatacao_captura, aglomerante_alternativo, outra.
>
> **C4-REDO Lote 9 (4365–4584): ✅ 144 Aceito + 6 Rej.** Rejeitados: 4380 (SNG de CO2), 4399 (biogás agrícola), 4414 (fábrica fotovoltaica), 4528 (membranas de CO2), 4540 (metanol de CO2), 4541 (poço de petróleo). Aceitos notáveis pela regra do inventário/adendo: 4372/4373/4394 (parques eólicos com concreto de fundação documentado), 4401 (pás eólicas→co-processamento de cimento + arquitetura), 4543 (concha→agregado em concreto poroso), 4475 (CFRP em matriz cimentícia), 4542 (vidro→geopolímero). Acumulado C4-REDO: 1.350 revisados (84 Rej + 1.266 Aceito), 281 pendentes.
>
> **C4-REDO Lote 10 (4585–4835): ✅ 144 Aceito + 6 Rej.** Rejeitados: 4585 (embalagem/sacaria de cimento), 4592 (capitalização de terra), 4679 (eletricidade de incineração/gaseificação), 4684 (cadeia florestal), 4765+4778 (métodos de produção de cimento — processo →outra). Aceitos notáveis pelo adendo: 4760 (mármore→substituto de calcário no clínquer), 4771 (GRP/fibra de vidro→co-processamento em cimento), 4808 (cinza volante→agregado leve), 4674 (pó de concha em cimento), 4660 (biochar em cimentício), 4744 (agregado reciclado de concreto). 4401 pré-marcado p/ reavaliação em C8 (framework conceitual). Acumulado C4-REDO: 1.500 revisados (90 Rej + 1.410 Aceito), 131 pendentes.
>
> **C4-REDO Lote 11/FINAL (4836–5093): ✅ 124 Aceito + 7 Rej.** Rejeitados: 4850 (wetland p/ efluente), 4865 (ACV agricultura), 4903 (produção de cimento Portland→outra), 4917 (sistema alimentar), 4926 (energia eólica Líbia), 4999 (co-processamento de resíduo no forno→combustivel), 5028 (wetland p/ esgoto). Aceitos notáveis pelo adendo: 4867 (resíduo hospitalar→pozolana em cimento), 4904 (resíduos carbonatados→concreto), 4949 (carbonação mineral em materiais de construção), 4862 (RCD).
>
> ## ✅ C5 CONCLUÍDO (2026-06-21) — "Não menciona emissões de GEE/CO₂"
> Universo = 1.548 artigos C4-Aceito triados. **Método final (Opção A, decisão Kiê 2026-06-15):** ACEITO = qualquer menção a CO₂/GWP/GHG/LCA/climate change relacionada ao material — com qualquer resultado (mesmo relativo, mesmo de outro estudo). REJEITADO = PDF inteiro (texto + figuras renderizadas) sem NENHUMA menção. Exceção: CO₂ puramente analítico-químico sem contexto ambiental. Script: `scan_and_save_lote.py` (PAT regex pdftotext) + `audit_lote_s*.py` (verificação corpo dos médios/fracos/misses com pdftotext + fitz). Lotes de 200 a partir do lote 350. Resultado final verificado no xlsx: **P:Aceito = 1.505 | P:Rejeitado = 43**. Único falso-positivo revertido: row 4184 (Dosho 2014 — mixing design puro, zero CO₂). Miss notável: row 4978 (Akita 2008, texto japonês — confirmado LCA no abstract EN). **Próximo critério: C6 (material geograficamente restrito).**
> **C5 Lote 1 (2553–2797, 150): ✅ 147 Aceito + 3 Rej.** 103 aceite automático (termo+valor); 44 aceites por leitura dirigida (reportam CO₂/GWP). Rejeitados (confirmados por leitura do PDF INTEIRO): 2636 (revisão de resíduo plástico, 19 págs, 1 menção a "greenhouse gases" sem número), 2697 (LCA de confiabilidade/manutenção ferroviária, 10 págs, zero menção a carbono). **2791 CORRIGIDO para Aceito** após leitura completa (tese 208 págs — reporta Climate change kg CO₂ eq e valores de CO₂ no fim; estava além da pág. 25). C5 acumulado: 150 revisados (2 Rej / 148 Aceito), 1.384 pendentes.
> **⚠️ REGRA C5 (Kiê 2026-06-14): antes de marcar qualquer C5 Rejeitado, LER O PDF INTEIRO (todas as páginas)** — valores de CO₂/GWP costumam estar em tabelas de LCI/resultados no fim, sobretudo em teses longas.
>
> **⭐⭐ REGRA C5 FINAL (Kiê 2026-06-14, SUPERA as anteriores): ACEITO EXIGE VALOR NUMÉRICO de emissão de CO₂/GEE** declarado no corpo (kgCO₂eq, kgCO₂/m³, tCO₂, GWP=valor, % de redução de CO₂, carbon/embodied footprint com número). Menção só qualitativa = Rejeitado. Rejeitar também: metodologia/teoria, política/ETS, S-LCA social (cuidado: "carbon" pode ser fibra), poluentes locais (mg/Nm³) sem CO₂, contexto genérico sem quantificar. Verificar valor no PDF inteiro (pdftotext rápido; se GWP só em figura, abrir imagem). **Reauditados os 88 aceites-sem-valor-automático dos Lotes 1–2:** 80 mantidos Aceito (têm valor, vários em tabela/figura que o regex perdeu) e **8 corrigidos p/ Rejeitado** (2636, 2812, 2909, 2936, 2954, 2967, 2997, 3010 — mencionam CO₂ mas sem valor / metodologia / política / poluentes).
>
> **⭐⭐⭐ REGRA C5 REVISADA (Kiê 2026-06-15 — OPÇÃO A, SUPERA a anterior):** ACEITO = qualquer artigo que conduza LCA **ou** mencione GWP/CO₂/GHG com **qualquer resultado** (mesmo % relativo, mesmo valor de outro estudo, mesmo resultado em figura não extraível por texto). REJEITADO apenas se o PDF inteiro (texto + todas as páginas renderizadas visualmente) não tiver NENHUMA menção a CO₂/GWP/GHG/LCA/climate change relacionada ao material estudado. Exceção: CO₂ puramente analítico-químico (ex.: picos FTIR de carbonatos sem avaliação ambiental) sem qualquer menção a LCA ou impacto ambiental. **OBRIGATÓRIO: ler 100% das páginas + renderizar figuras/gráficos antes de qualquer REJEITADO.** LCA com resultados relativos (%) e valores citados de outros estudos = ACEITO (os outros estudos entram como fontes externas).
>
> **C5 Lote 2 (2798–3094, 150): ✅ 144 Aceito + 5 Rej + 1 problema.** Rejeitados (estruturais, zero menção a carbono no corpo): 2857 (corrosão de pontes), 2858 (durabilidade de UHPC), 2866 (tubulações enterradas), 2870 (métodos semi-probabilísticos), 2878 (gestão de estruturas). **Problema:** 3002 = só capa/front matter de livro Woodhead (3 págs, sem conteúdo) → NÃO classificado, precisa do PDF correto. C5 acumulado: 299 classificados (38 Rej / 261 Aceito), 1.235 pendentes (inclui 3002 livro, aguarda PDF correto).
>
> **✅ Verificação visual dos 38 artigos provisoriamente P:Aceito (2026-06-15):** concluída. Dos 38 revisados com pdftotext -layout + pdf2image dpi=150-170: **15 mantidos Aceito** (valor absoluto CO₂/GEE confirmado visualmente — GWP kg CO₂eq, embodied carbon kg CO₂e, ton CO₂e explícitos em tabela/figura/corpo) + **23 corrigidos para Rejeitado** (apenas menções qualitativas, só % de redução, indicadores análogos/kJ/DALY/SUI-yr·MPa⁻¹, ou CO₂ apenas em referências/contexto de fundo). Todos os 38 registrados no xlsx com carimbo e evidência/motivo na coluna comments (col 32).
>

---

## 🌍 C6 — Material geograficamente restrito (iniciado 2026-06-21)

> **Definição literal (aba Critérios):** *"Materiais cujo material principal tem produção geograficamente restrita e baixa escalabilidade global, impossibilitando aplicação em contextos internacionais."* Ver `PROMPT_RETOMADA_C6.md` e `CLAUDE.md` para refinamentos completos.

### ⚠️ Correções de base aplicadas ANTES de prosseguir o C6 (2026-06-21)

Detectaram-se inconsistências herdadas da cascata + um bug de coluna meu. **Tudo corrigido e verificado** (backups em `02_ARQUIVOS ANTERORES/`):

- **Lógica R:/P: confirmada (lida da aba Critérios):** `R:` = decisão por título/resumo; `P:` = decisão por PDF completo. `P:` é o **histórico de quem foi triado por PDF** — artigos rejeitados por PDF MANTÊM o histórico (P:Rejeitado + P:Aceito anteriores). Rows **fora-da-cascata** (Duplicado/Sem acesso/Rejeitado-por-resumo) **não recebem P: em nenhum critério**.
- **Grupo A** — 4 rows Duplicado/Sem acesso com P: indevido → P: removido (3258, 3261, 3262, 3454).
- **Grupo B** — 3 vazamentos de cascata (P:Rejeitado em Cn + P: em Cm>n) → P: posteriores removidos (3259, 3273, 3291).
- **Grupo C** — `status_triagem = Recusado` ELIMINADO (padronizado p/ Rejeitado): row 2897 migrado + P:C1 removido. 100 rows `Inconclusivo` com P:Rejeitado em C1–C5 → `status = Rejeitado`.
- **Grupo D** — 1.705 células C8 sem prefixo → prefixadas `R:` (só rows na cascata; C8 decidido por document_type).
- **Retro C6** — 8 rejeitados C6 dos Lotes 1–2 → `status = Rejeitado`.

**Snapshot status_triagem após correções (2026-06-21):** Duplicado 2.624 · Inconclusivo 1.246 · Rejeitado 676 · Elegível 479 · Sem acesso 68 · **Recusado 0**.

### Universo C6 LIMPO (redefinido)

**= 1.488** rows = na cascata (Elegível/Inconclusivo) **E** C5=P:Aceito **E** sem rejeição anterior por PDF **E** C6 sem P:. ⚠️ O antigo "1.505/1.534 P:Aceito no C5" incluía falsos-positivos sem PDF/fora-da-cascata. Pendentes ao iniciar Lote 3 = **1.103** (lista: `outputs/c6_pending_clean.json`).

### Nova regra operacional (Kiê 2026-06-21)
**Ao fim de cada lote:** salvar + **atualizar `status_triagem`→`Rejeitado`** nos rows com C6 P:Rejeitado + reportar. Fibra natural = parar e perguntar caso a caso.

### Lotes C6

- **Lote 1 (2553–2968, 200): ✅ 196 Aceito + 4 Rej.** Rejeitados: 2581 (rammed earth/taipa), 2805 (bahareque), 2790 (fibras vegetais Amazônia, foco — rastreio `outra`), 2753 (cortiça). Pré-screen por palavra-chave de material restrito + leitura individual dos 14 sinalizados.
- **Lote 2 (2971–3286, 200): ✅ 192 Aceito + 4 Rej + 4 fora-da-cascata revertidos.** Rejeitados: 3016 (construção em terra/3D-print), 3120 (stabilised earth), 3159 (rammed earth+fibras), 3254 (materiais costeiros naturais — rastreio `outra`). Revertidos (sem PDF/fora-da-cascata): 3258, 3261, 3266, 3278.
- **Decisões de princípio C6:** 3348 hemp-reforço=Aceito · 3284 adobe-vs-concreto=Aceito (metade concreto armado) · 4938 De Toldi cut-stone=Rejeitado.
- **Lote 3 (3287–3572, 200): ✅ 199 Aceito + 1 Rej.** Rejeitado: 3498 (técnicas ancestrais terra/palha — straw bale/adobe/rammed earth/cob). Decisões: 3349 bio-materiais (misto, inclui engineered wood escalável)=Aceito · 3397/3511 cob/earth-vs-concreto=Aceito (concreto é metade) · 3515 self-healing road=Aceito.

### ⚠️ Recuperação metodológica (2026-06-21) — re-leitura dos 583 aceitos dos Lotes 1–3
Detectou-se que os Lotes 1–3 usaram um ATALHO indevido: pre-screen por regex (3 primeiras págs) + leitura individual só dos sinalizados; os "limpos" foram marcados Aceito SEM leitura real. Isso violou a regra de **ler as 3 primeiras páginas de CADA artigo**. O caso 3275 (review de compósitos de MICÉLIO) escapou e estava Aceito indevido → corrigido para **C6 Rejeitado** (rastreio `outra`).
**Ação corretiva:** re-leitura das 3 primeiras páginas dos 583 aceitos C6, verificando o material principal de cada um. Resultado: além do 3275, **nenhuma outra reclassificação** — todos os demais são materiais globais (concreto, cimento, geopolímero, fly ash, escória, madeira engenheirada, resíduos amplamente disponíveis) ou LCA de sistemas/edifícios sem material restrito.
**Regra reforçada (memória `rsl-metodo-leitura-pdf-obrigatoria`):** pre-screen por regex é só auxiliar; NUNCA substitui a leitura das 3 primeiras páginas de cada artigo.

### ⭐ MUDANÇA DE REGRA — Terra = ACEITO (Kiê 2026-06-21)
Reverificação dos rejeitados por "terra": **terra/solo é material UNIVERSAL e escalável** (disponível em toda parte); a restrição da taipa/adobe/cob é de TÉCNICA/mão-de-obra, não de disponibilidade do material → materiais de terra passam a **C6 Aceito**. (C6 é só sobre restrição geográfica do material; ser estrutural já foi avaliado em C2/C3.)
**6 revertidos P:Rejeitado→P:Aceito + status restaurado:** 2581, 3016, 3120, 3159 (taipa/terra estabilizada, incl. com fibra-reforço), 3498 (terra+palha+adobe), 3896 (taipa álcali-ativada). **EXCEÇÃO mantida Rejeitado:** 2805 bahareque (estrutura de BAMBU+terra → rejeitado pelo bambu, que ≠ terra e é restrito).

### ✅ C6 CONCLUÍDO (2026-06-21): **1.488 P:Aceito + 8 P:Rejeitado** | universo limpo 1.488 | 0 pendentes
**8 Rejeitados C6** (todos com rastreio col 33): 2753 (cortiça), 2790 (fibras vegetais Amazônia foco), 2805 (bahareque/bambu), 3254 (fibras costeiras coir/juta), 3275 (micélio), 4707 (pedra natural estrutural), 4720 (cinza de açaí amazônico), 4938 (cut-stone De Toldi).
Lotes 1–8 (rows 2553–5093). Método: leitura das 3 primeiras páginas de cada artigo (sem atalho regex, após correção metodológica).
**Regra de resíduo agrícola/vegetal como SCM:** universal (bagaço, casca de arroz, aguapé invasor, lignina, palha) = Aceito; regional concentrado (açaí amazônico) = Rejeitado.

### ⚠️ Limpeza de vazamentos de cascata (2026-06-21, antes do C7)
Auditoria pelo **veredito final** (P: supera R:) revelou ~246 rows com veredito Rejeitado num critério anterior mas status_triagem errado — em maioria **C2 R:Rejeitado** (telhas, drenagem, isolamento = não-estruturais, rejeitados por resumo) que vazaram pela cascata. Causa: filtros de universo checavam só `P:Rejeitado`, ignorando `R:Rejeitado`.
**Corrigido:** 7 P:Aceito vazados removidos de C5/C6 (3253, 3267, 3272, 3275, 3277, 3278, 3296) + 244 status→Rejeitado. Verificado: 0 vazamentos, 0 vereditos-Rejeitado com status errado.
**status_triagem após limpeza:** Duplicado 2.621 · Rejeitado 928 · Inconclusivo 1.078 · Elegível 398 · Sem acesso 68.
**Regra consolidada (memória `rsl-cascata-status-P`):** o universo de qualquer critério Cn exclui quem tem **veredito final Rejeitado** (P: supera R:; inclui `R:Rejeitado` sem P:) em QUALQUER critério anterior. Usar função `verdict()`.

### ❌ C7 REMOVIDO da RSL (decisão Kiê, 2026-06-22)

**Motivo:** artigos com foco exclusivo em energia operacional são rejeitados via C2 (material não estrutural) ou C3 (material não moldável), tornando C7 redundante. O funil vai de C6 directo para C8.

**Estado no xlsx:** os 200 `P:Aceito` escritos no Lote 1 do C7 foram **removidos** da coluna C7 (preservando o `R:` original onde existia). Carimbos `[C7 ...]` nos `comments` também removidos. Backup em `02_ARQUIVOS ANTERORES/articles_final_backup_remove_C7_20260622_024454.xlsx`.

### ✅ C8 CONCLUÍDO (2026-06-22) — artigos de opinião sem dados primários

**Método:** `document_type` do banco + análise de título. Prefixo `R:` (não requer leitura de PDF). Universo real triado = **1.339** (artigos do universo C6-Aceito sem C8 pré-marcado).

**Resultado:** 1.337 R:Aceito + **2 R:Rejeitado**:
- Row 3180 — `document_type=retracted` (artigo retractado)
- Row 4050 — Jolliet et al. 2015, *Environmental Life Cycle Assessment* (livro de metodologia LCA pura — exemplos de copos/lâmpadas/embalagens, sem dados primários de materiais estruturais; conteúdo do PDF confirmado)

**Nota sobre universo:** 1.339 < 1.488 porque ~149 rows já tinham `R:Aceito` pré-marcado no C8 desde sessões anteriores (Grupo D das correções de base 2026-06-21). Status dos 2 rejeitados actualizado para `Rejeitado`. Backup: `02_ARQUIVOS ANTERORES/articles_final_backup_C8_20260622.xlsx`.

**Funil final após C8:** 1.337 artigos aceitos em todos os critérios C1–C8 → entram na fase de extração de dados (meta-análise).


> **C5 Lote 8 (3449–3511, 50): ✅ 50 Aceito + 0 Rej.** Todos com CO₂/LCA/GWP confirmado por pdftotext (Windows). C5 acumulado: 584 classificados (39 Rej / 545 Aceito), 950 pendentes.
> **C5 Lote 7 (3375–3447, 50): ✅ 50 Aceito + 0 Rej.** Todos com CO₂/LCA/GWP confirmado por pdftotext. C5 acumulado: 534 classificados (39 Rej / 495 Aceito), 1.000 pendentes.
> **C5 Lote 6 (3301–3374, 50): ✅ 50 Aceito + 0 Rej.** Todos com CO₂/LCA/GWP confirmado por pdftotext. Filtro corrigido: `P:Aceito in C4` (universo exato de 1534). C5 acumulado: 484 classificados (39 Rej / 445 Aceito), 1.050 pendentes.
>
> **C5 Lote 5 (3246–3299, 52 rows, 49 classificados): ✅ 49 Aceito + 0 Rej + 3 aguarda PDF.** 44 com CO₂/LCA/GWP confirmado por pdftotext. 3 ACEITO por título+resumo sem PDF local (3258 — CO₂ utilisation + LCA; 3261 — CO₂ emissions cement industry; 3266 — LCA green concrete). 3 aguarda PDF (3260 CFRP reciclagem — "carbon fibre" material, não CO₂; 3262 microalgas — sem CO₂/GWP no resumo; 3295 social maintenance — sem CO₂/GWP no resumo). C5 acumulado: 448 classificados (39 Rej / 409 Aceito), 1.086 pendentes (inclui 3002 livro + 3 aguarda PDF).
>
> **C5 Lote 4 (3182–3245, 50): ✅ 50 Aceito + 0 Rej.** Sob Opção A: 27 com kgCO₂/tCO₂ explícito no texto (regex) + 23 com LCA/GWP/carbon mentions confirmados por pdftotext full-scan (todos tinham LCA, carbon footprint, GWP, GHG ou carbon emissions). Zero rejeições neste lote. C5 acumulado: 399 classificados (39 Rej / 360 Aceito), 1.135 pendentes (inclui 3002 livro).
>
> **C5 Lote 3 (3095–3181, 50): ✅ 49 Aceito + 1 Rej.** Classificação inicial (regra anterior): 36 Aceito + 14 Rej. **CORRIGIDO 2026-06-15 sob Opção A:** 13 dos 14 rejeitados revertidos para Aceito (3098, 3102, 3104, 3107, 3123, 3139, 3142, 3149, 3151, 3154, 3163, 3176, 3180 — todos mencionam LCA/GWP/CO₂/GHG com resultados relativos, % ou de outros estudos). **Único mantido Rejeitado: 3119** (JULLIEN — "LCA of alternative granular materials: ecotoxicity and toxicity" — LCA presente mas focado 100% em ecotoxicidade/toxicidade com chumbo/cobre/zinco em água; zero menção a CO₂/GWP/GHG/climate change em todas as páginas + figuras verificadas). C5 acumulado: 349 classificados (39 Rej / 310 Aceito), 1.185 pendentes (inclui 3002 livro, aguarda PDF correto).
>
> ## ✅ C4 CONCLUÍDO (2026-06-14) — 1.631 revisados: **1.534 Aceito / 97 Rejeitado**, 0 pendentes
> Método: leitura de 3+ páginas de cada PDF (recomeço que anulou a 1ª passada por resumo). Regras consolidadas na aba Critérios: adendo (resíduo off-topic→material do concreto/cimento = Aceito), precursor/processo (clínquer, mineração de calcário, produção de cimento = Rejeitado), ETA/ETE e instalações com concreto no inventário (Aceito), resíduo como combustível no forno ou só imobilização/descarte (Rejeitado). Rastreio_potencial_futuro dos rejeitados/marcados: aglomerante_alternativo 402, carbonatacao_captura 107, fator_clinquer 32, combustivel 8, biocimento 6, outra 8. Pré-marca C8: 4401 (framework conceitual). **Próximo critério: C5 (menção a GEE/ACV/CO2).**
>
> **Início 2026-06-13.** Definição (aba Critérios): *"Materiais que não são relacionados a construção civil"* — "Não aderem ao tema da pesquisa". **REJEITADO:** setores off-topic (medicina, farmácia, biologia, agricultura, alimentos, eletrônica, embalagens, automóvel, aeronáutica, naval não-infra, energia solar/eólica com foco no painel/turbina). Também REJEITADO: **precursor sem ACV do elemento final** (clínquer isolado, fornos de cimento, mineração de agregado sem produto final). **ACEITO:** concreto/cimento/UHPC/cimentícios em contexto de construção. **BRANCO/A revisar:** infraestrutura genérica sem material; LCA de sistema completo sem foco em material.
> **Universo (decisão Kiê 2026-06-13): TODOS os 1.631 C3-Aceito**, **incluindo a RE-REVISÃO dos 228 pré-marcados C4 Rejeitado** nas passadas de C2/C3 (a Kiê quer revisá-los aqui com o adendo abaixo). **Método: reabrir e verificar o PDF de cada artigo** (mesmo rigor do C3). Lotes de 100. Indicador de "revisado nesta passada" = carimbo `2026-06-13` na nota C4 dos comments.
> **⭐ ADENDO DE ACEITAÇÃO (decisão Kiê 2026-06-13):** mesmo que o artigo seja de setor off-topic (medicina, agricultura, alimentos, eletrônica, energia, etc.), se ele **usa um material/resíduo desse setor com o propósito de melhorar ou substituir o concreto** (ex.: partes de turbina eólica como agregado no concreto; casca de arroz, lodo, etc. como SCM/agregado) → **C4 ACEITO**. O que decide é a aplicação como material para substituto/componente do concreto, não o setor de origem.
> **Dúvida → PARAR e perguntar à Kiê antes de classificar.**
> **Tratamento de nuances:** precursor-sem-elemento-final → Rejeitado após confirmar no PDF; BRANCO (infra genérica/sistema sem material) → C4 Aceito com nota "A revisar".

**Lote C4-01 (2553–2733, 100): ✅ 100/100** — 97 C4 Aceito + **3 C4 Rejeitado** (2640 Del Serrone: produção de clínquer/precursor; 2662 Du: eólica→hidrogênio, energia; 2676 Fozer: combustível de resíduo/marítimo em planta de cimento, processo/forno). Aceitos pelo adendo/construção: 2575 (bio-cimentício), 2709 (placas geopolímero/cimento), 2724 (cimentício com rejeito de molibdênio). 2673 (Felicioni) lido por OCR. Acumulado C4: 100 revisados (3 Rej + 97 Aceito), 1.531 pendentes.

> **🏷️ Regra rastreio em C4-rejeitados (Kiê 2026-06-13):** C4 Rejeitado com tecnologia ligada a concreto/cimento → tag em `rastreio_potencial_futuro` (clínquer→fator_clinquer; combustível/descarbonização cimento→outra; CO2→carbonatacao_captura; aglomerante→aglomerante_alternativo). Energia sem tecnologia de concreto (concreto só em inventário) → sem tag. Aplicado: 2640→fator_clinquer, 2676→outra.

**Lote C4-02 (2734–2888, 100): ✅ 100/100** — 99 C4 Aceito + **1 C4 Rejeitado** (2888 Kim: usina fotovoltaica 30 MW, energia solar — pré-marca confirmada, sem tag pois concreto só no inventário). Adendo aplicado: 2810 (tecidos naturais em placa cimentícia), 2847 (cinza sucroalcooleira como ligante), 2849 (painéis de cimento magnesiano), 2774 (LCA de cimento+aço+vidro+plástico) → Aceito. Acumulado C4: 200 revisados (4 Rej + 196 Aceito), 1.431 pendentes.

> **⚠️ Interrupção 2026-06-13:** a pasta conectada caiu no meio do C4 (mount do bash perdido); migrada de `02_PESQUISA`→`01_PESQUISA`; resolvido após reiniciar o Claude. Nada perdido. Script `c4_extract.py` recriado.

**Lote C4-03 (2889–3156, 150): ✅ 150/150** — 131 C4 Aceito + **19 C4 Rejeitado** + (2968 resolvido por consulta → Aceito). Rejeitados: off-topic sem ponte (2965 agric, 2970 pesca, 2973 resíduo plástico, 2975 forragem, 2979 indústria metalúrgica, 2990 microalgas, 3004 microalga-aviação, 3006 Power-to-Gas, 3012 aquicultura, 3051 CO2→metanol, 3080 viticultura, 3110 escândio de bauxita, 3113 esterco) + processos (2997 incineração em forno rotativo, 3007 calcium looping CCS, 3009 descarbonização macro, 3010 qualidade do ar de planta de cimento, 3005 carbonação de CO2 [+tag carbonatacao_captura], 3077 produção de clínquer+cimento Etiópia [+tag fator_clinquer]). Adendo/construção aceitos: 2902 (fundação de concreto impressa 3D p/ torre eólica), 2955 (construção de redes de esgoto), 2952/3001/3017 (resíduos como SCM/material), 2968 (UHPC em raft de aquicultura — decisão Kiê: Aceito por ser UHPC estrutural). Acumulado C4: 350 revisados (23 Rej + 327 Aceito), 1.281 pendentes.

**Lote C4-04 (3157–3364, 150): ✅ 150/150** — 131 Aceito + **19 Rejeitado** (3252 GEE de ETA água; 3256 florestal/bioenergia; 3257 carbonação mineral [+carbonatacao_captura]; 3259 exergia indústria cimento [+outra]; 3264 captura CO2 pós-combustão; 3274 descomissionamento nuclear; 3297 troca de combustível na produção de cimento [+outra]; 3299 eólica offshore; 3310 biocombustível/cinza carvão policy; 3311 S/S resíduo perigoso; 3315 materiais p/ eletricidade; 3316 poço de petróleo; 3317 GEE militar; 3333 calcium carbonate looping; 3342 fotocatalisador TiO2 água; 3343 negócios&biodiversidade; 3350 frutas; 3351 fotovoltaico; 3357 desempenho planta de cimento [+outra]). Adendo aceitos: 3254 (concreto/cimento de baixo carbono p/ estruturas costeiras), 3320 (reciclagem de concreto/pás de turbina como agregado), 3182 (e-waste em concreto), 3346 (reuso de concreto p/ passarela). 3259 lido por OCR. Acumulado C4: 500 revisados (42 Rej + 458 Aceito), 1.131 pendentes.

### ✅ C3 CONCLUÍDO (2026-06-13)
- **C2 Aceito in-scope: 1.672.** **C3 decididos: 1.670** — **41 C3 Rejeitado** (blocos/tijolos/alvenaria/AAC/paver/adobe não moldáveis) + **1.629 C3 Aceito**.
- **Colisões resolvidas (2026-06-13):** **3597** (Zhou, copper slag como substituto de cimento, DOI 10.1016/j.resconrec.2024.107591) → C3 **Aceito** (cimentício moldável; tag aglomerante_alternativo). **4938** (De Toldi, cut-stone, DOI 10.5334/bc.278) → C3 **Aceito + NOTA + PRÉ-MARCA p/ C6** (decisão Kiê: cut-stone = pedra de cantaria personalizável/estrutural, mas produção geograficamente restrita / baixa escalabilidade → rever em C6). PDFs integrados com nomes próprios (ZHOU et al., 2024.pdf / DE TOLDI et al., 2023.pdf).
- **C3 100% fechado: 0 pendentes.**
- Reclassificações C2 durante o C3 (revestimentos/não estruturais que escaparam): 3240, 3273, 3497 (kerb), 3597-anulado→colisão, 3669, 3597... 4085, 4239, 4907. Recusados/duplicados tratados: 2897 (Recusado), 3454 (Duplicado).
- **Próximo critério: C4 (materiais não relacionados a construção)** — muitos já pré-identificados nos comments (microalgas, esgoto, aquicultura, óleo, CO2→metanol, poço de petróleo, fotocatalisador de água, wetlands, etc.).

**Lote final 5012–5093: ✅ (43 in-scope)** — 29 C2 Aceito + 7 C2 Rejeitado (5022 cobblestones, 5024 vedação interna, 5025 asfalto, 5030 telha fibrocimento, 5033/5035 solo, 5082 pavimento invertido) + 2 C3 (5078/5092 blocos) + 5 C4 (5020 captura CO2, 5028 wetland, 5031 trabalho decente, 5042 hidrelétrica, 5076 carbonatação/uso CO2).

**Lote 4929–5011: ✅ 50/50** — 46 C2 Aceito (4 C4: 4941 metodologia hidrelétrica, 4944 processos industriais, 4965 proteção de encostas, 4968 peças de máquina em concreto polimérico) + 4 C2 Rejeitado (4967 louça sanitária, 4974 restauração de pavimento, 4977 grouting/solo, 4991 asfalto HMA). Coluna de rastreio aplicada (4938 cut-stone → tag 'outra').

**Lote 4842–4927: ✅ 50/50** — 35 C2 Aceito puros + 11 C4 (4849 plástico, 4850 wetland, 4854 e-waste, 4865 ABM, 4896 IA, 4904 CCUS, 4905 fixação carbono, 4917 comida, 4918 esgoto, 4926 eólica, 4927 CO2 uptake macro do cimento) + 1 C8 (4908 bibliometria 3D) + 2 C3 (4853 blocos concreto/cerâmico, 4877 tijolos) + 1 C2 Rejeitado (4852 pavimento permeável). Coluna de rastreio aplicada.

**Lote 4769–4841: ✅ 50/50** — 47 C2 Aceito (2 C4: 4771 GFRP pá eólica, 4791 orçamentos macro de carbono) + 3 C2 Rejeitado (4796 papelão reciclado, 4793 pavimento permeável). Coluna de rastreio aplicada. Colisão 4793 resolvida → `WANG, 2024c.pdf` (C2 Rejeitado, pavimento permeável).

**Lote 4685–4766: ✅ 50/50** (primeiro com coluna de rastreio) — 47 C2 Aceito (2 C4: 4714 lignina kraft, 4735 governança ambiental; 2 C3: 4717 tijolos solo-cimento, 4740 tijolos cerâmicos) + 3 C2 Rejeitado (4689 meio-fio/kerb, 4757 construção rodoviária, 4759 pavimento flexível). Tags do lote: aglomerante_alternativo 20, fator_clinquer 4, carbonatacao_captura 3, outra 1 (4702 mass timber).

**Lote 4605–4684: ✅ 50/50** — 49 C2 Aceito (5 C4: 4642 bioeconomia, 4646 metodologia resíduo mineral, 4649 transporte rodoviário, 4679 WtE/RSU, 4684 cadeia florestal) + 1 C2 Rejeitado (4676 biocimento/MICP).

**Lote 4539–4604: ✅ 50/50** — 50 C2 Aceito (5 C4: 4541 poço de petróleo, 4566 S-LCA social, 4567 iluminação/túnel, 4585 embalagem de cimento, 4592 política de terras). Sem C2 Rejeitado neste lote.

**Lote 4463–4537: ✅ 50/50** — 46 C2 Aceito (3 C4: 4528 captura de carbono, 4533 mineração, 4534 reciclagem CFRP/GFRP; 1 C8: 4523 bibliometria fibra vegetal) + 3 C2 Rejeitado (4483 green roof, 4491 revestimento geopolímero, 4506 asfalto poroso).

**Lote 4398–4462: ✅ 50/50** — 47 C2 Aceito (8 C4: 4399 biogás, 4401 pá eólica, 4411 CCS, 4414 fotovoltaica, 4427 cheesecake/comida, 4429 gestão de desastre, 4432 plástico, 4462 captura PCC; 1 C8: 4409 revisão crop-based) + 3 C2 Rejeitado (4423 geossintético, 4430/4451 asfalto).

**Lote 4327–4396: ✅ 50/50** — 48 C2 Aceito (5 C4: 4366 hidro financeiro, 4367 pneus, 4372/4373 eólica, 4380 gás sintético) + 2 C2 Rejeitado (4361 pavimento semi-flexível asfáltico, 4378 envoltória operacional). Notas: 4377 (roadmap setor construção) e 4382 (energia/carbono construção) e 4396 (ML dano) aceitos em C2 mas marcados p/ verificar C5/C7 depois.

**Lote 4263–4325: ✅ 50/50** — 45 C2 Aceito (2 C4: 4276 previsão demanda cimento, 4318 paisagismo rio urbano; 1 C8: 4308 bibliometria) + 5 C2 Rejeitado (4271 concreto não-estrutural, 4280 parede não-portante, 4298 fachada sanduíche, 4324 asfalto/RAP, 4325 partições leves). Colisões resolvidas:
- **4308** → `CHEN, 2023i_2.pdf`; C8 (bibliometria de descarbonização de edifícios).
- **4167** (lote anterior) → `CHEN, 2023i_3.pdf`; C2 Aceito confirmado (construção modular em madeira). [Os 3 — 3817, 4167, 4308 — compartilhavam `CHEN, 2023i_1.pdf`; agora cada um tem o seu.]

**Lote 4198–4261: ✅ 50/50** — 49 C2 Aceito (12 C4: 4209 espuma industrial, 4210 CCU químicos, 4212 NETs, 4213 RSU, 4215 hidro-reservatório, 4222 CCU, 4223 previsão, 4225 combustível aviação, 4228 pecuária, 4237 óleo lubrificante, 4245 bibliometria transporte, 4259 pneus; 1 C8: 4216 perspective ISRU) + 1 C2 Rejeitado (4261 estabilização de solo argiloso).

**Lote 4126–4197: ✅ 50/50** — 48 C2 Aceito (7 C4: 4127 microalgas, 4129 aquicultura, 4132 esgoto OWTS, 4157 fossa séptica, 4165 resíduo hospitalar, 4179 mineração calcário, 4181 circularidade macro suíça) + 2 C2 Rejeitado (4163 hempcrete envelope, 4188 subbase granular) + 2 C3 Rejeitado (4133 tijolos ICEB, 4150 bloco de concreto). 4196 lido por OCR.
- **4181** (MFA macro da economia suíça) → C4 confirmado pela Kiê (não é estudo de um material; cairia também na extração do fck).

**Lote 4055–4124: ✅ 50/50** — 48 C2 Aceito (5 C4: 4056 compostagem, 4061 lodo celulose, 4063 macro China, 4083 lodo esgoto, 4122 turbinas eólicas) + 2 C2 Rejeitado (4096 envoltória, 4118 MICP/biocimentação) + 1 C3 Rejeitado (4059 blocos de concreto vazados).
- **4106** — resolvido; PDF corrompido substituído pelo correto (SciELO OA, mesmo nome `BACELAR, 2022.pdf`); C2 Aceito (pilar de concreto armado).

**Lote 3987–4054: ✅ 50/50** — 47 C2 Aceito (4 C4: 4011 comércio cimento, 4018 cirúrgico, 4031 dieta/renal, 4032 perfuração) + 3 C2 Rejeitado (3987 asfalto, 3990 pavimento, 3996 base de estrada). 3 colisões resolvidas:
- **3990** → `HUANG et al., 2018b.pdf`; C2 Rejeitado (modelo LCA de pavimento).
- **3996** → `WANG, 2019c.pdf`; C2 Rejeitado (base estabilizada de estrada).
- **4013** → `HUANG et al., 2022b.pdf`; C2 Aceito (RCD de obras ferroviárias).
- Investigado: `HUANG et al., 2018.pdf` (dormitórios) pertence ao **row 3365** (já C2 Aceito) e `HUANG et al., 2022.pdf` (plastic waste review) ao **row 4432** (Inconclusivo, a triar) — ambos corretos, sem ação. Arquivo `64675-pt.pdf` (meteorologia, não pertence à RSL) movido para `BAIXADOS MANUALMENTE/PARA VERIFICAR/`.

**Lote 3914–3986: ✅ 50/50** — 46 C2 Aceito (12 C4 incl. ferrovia 3932 + 1 C8 perspective 3966) + 4 C2 Rejeitado (3921/3986/3954 asfalto/rodoviário, 3922 parede de alvenaria). Escopo (decisões Kiê): ferrovia 3932 → C4; dique costeiro 3943 → Aceito; pavimento de aeroporto 3982 → Aceito (tem PCC).
- **3954** — resolvido; PDF correto integrado como `ZHANG et al., 2022b.pdf`; **C2 Rejeitado** (biomassa→material rodoviário). ⚠️ Órfão `ZHANG et al., 2022.pdf` (pjoes/147185, concreto de agregado reciclado) pode pertencer a outra linha — verificar depois.

**Lote 3858–3913: ✅ 50/50** — 47 C2 Aceito (3 C4, 1 C7) + 3 C2 Rejeitado (3860 telha/tijolo, 3874 forro willow-clay, 3908 pavimento de calçada) + 2 C3 Rejeitado (3871 blocos de terra, 3913 blocos de concreto). Escopo: terra/taipa estrutural (3896 parede portante, 3903 estabilização de terra) → Aceito; blocos → C3.
- **3884** — resolvido; PDF correto integrado como `WANG, 2019b.pdf`; **C4** (tratamento de lodo de esgoto). O arquivo `WANG, 2019.pdf` (concreto ternário ma12152448) pertence corretamente ao **row 4465** (Inconclusivo, ainda não triado) — investigado e confirmado, sem ação necessária.

**Lote 3786–3857: ✅ 50/50** — 43 C2 Aceito (5 C4 Rej) + 7 C2 Rejeitado (3797/3798/3799/3800/3842/3854 asfalto-pavimento; 3809 fachada).
- **3839** — resolvido; PDF 012175 integrado como `HOXHA, 2021i_2.pdf`; **C2 Aceito**.
- **3800** — resolvido; PDF correto integrado como `DE PASCALE et al., 2023.pdf`; **C2 Rejeitado** (asfalto/RAP). (Campo `author` já estava correto — De Pascale et al.; o "De Bortoli" era só o nome do arquivo antigo, do PDF errado.)
- **3846 e 3847** — reavaliados a fundo: confirmados **C4** (3846 = sistema de transporte/estacionamento+automóvel, automobile/transport 35x vs material 7x; 3847 = LCA de elementos de rede de distribuição de água, water/pipe 53x vs material 2x). Não são estudos de material de construção.

**Revisar depois (classifiquei C4, borderline):** 3846 (infraestrutura de estacionamento + ciclo de vida automóvel) e 3847 (redes de distribuição de água) — sistemas de infraestrutura, não estudos de material; se preferir, reavaliar. Lotes 3628–3677, 3678–3727 e 3728–3785 concluídos.

**✅ Lote 3728–3785 fechado 100% (50/50).** Resultado: 47 C2 Aceito (dos quais 14 C4 Rejeitado e 1 C8 Rejeitado) + 3 C2 Rejeitado (3744 biocimentação/solo, 3753 micélio-tijolo, 3769 fachada não-estrutural).

Casos que exigiram download/resolução:
- **3751** — colisão resolvida; PDF correto integrado como `WANG et al., 2024b.pdf`; **C4** (sistema de energia a gás natural). ⚠️ Arquivo órfão `WANG et al., 2024.pdf` (BIM End-of-Life Buildings, su16072980) ficou no destino — verificar se pertence a outra linha.
- **3762** — corrompido (HTML) resolvido; PDF correto integrado (Zenodo CC-BY); **C4** (reuso de CO2 em indústrias de processo).
- **3784** — confirmado **C8** (ensaio de ética sem dados primários).

**🔧 Convenção R: vs P: corrigida (2026-06-06):** decisões resolvidas por título/resumo ficam em **R:** (corrige-se o primeiro `R:` da célula com a decisão; quando muda o resultado, nota `[Reavaliado por título/resumo: Cn era R:X]` nos comments). **P:** só para artigos lidos no texto completo. Conversão retroativa: **936 marcações `P:`→`R:`** (162 com nota de mudança); mantidas `P:` só 10 linhas lidas a fundo (C2: 3019/3291/3340/3341/3585/3603/3675; C3: 3019; C4: 3051/3299). Regra na memória `rsl-marcacao-R-vs-P`.

**✅ Lote 3578–3627 concluído (43 in-scope).** 3603 (borracha de pneu sismo-resistente): C2 Aceito (inclui RuC, concreto com borracha). 2 colisões resolvidas: 3590 → `KOMKOVA, 2023ib.pdf` (cadeia de suprimentos de AAM concrete — Aceito); 3621 → `WU et al., 2014b.pdf` (concreto, fases uso/fim de vida — Aceito). Lote 3528–3577 triado; pendências abaixo.

**⚠️ Pendências (lote 3528–3577):**
- **3561** (LCSA de pisos industriais): C2 Aceito — é concreto reforçado com fibra estrutural (verificado no PDF).
- **Colisão do lote anterior resolvida — 3360:** o arquivo `TEH et al., 2017.pdf` pertence ao **3558** (Replacement scenarios, proeng). O PDF correto do **3360** ("Hybrid LCA of GHG emissions de cimento/concreto/geopolímero, Austrália") foi rebaixado e integrado como `TEH et al., 2017b.pdf` → C2 Aceito.
- Duplicatas verdadeiras marcadas: 3543=3542, 3550=3549.

**✅ Lote 3478–3527 concluído (46 in-scope → 43 Aceito, 3 Rejeitado):** C2 Rejeitado: 3489 (casca de arroz p/ barreira acústica/isolamento), 3517 (revisão ACV de rodovias), 3527 (pavimento betuminoso). C4 pré-marcado: 3479 (pás eólicas), 3482 (hidrogênio), 3483 (hidrogênio/carbono em concreto). 2 colisões resolvidas: 3514 → `FAN et al., 2025.pdf` (ativadores de casca de amêndoa p/ concreto — Aceito), 3517 → `LIU et al., 2022b.pdf` (Rejeitado). Lote 3428–3477 quase completo; pendências abaixo.

**✅ Lote 3428–3477 concluído (46 in-scope → 43 Aceito, 3 Rejeitado):**
- **3467** (nano-CaCO₃ de cimento residual): decisão Kiê = C2 Aceito + C4 Rejeitado.
- **5 colisões/corrompidos resolvidos:** 3430 → `HATZFELD et al., 2022b.pdf` (Modeling circularity — C2 Rejeitado), 3436 → `TAUTORAT, 2023i.pdf` (decarbonização cimento/aço, topic modeling — C2 Rejeitado), 3446 → `HUANG et al., 2024b.pdf` (concreto de lodo — Aceito), 3451 → `HUANG et al., 2024c.pdf` (concreto permeável geopolimérico — Aceito), 3469 → `MEIJSSEN, 2023i.pdf` (carbonatação mineral — C4).
- **Nota:** 3454 = duplicata verdadeira do 3453 (mesmo DOI). O arquivo original `HUANG et al., 2024.pdf` é um 3º artigo (framework LC3 de Guangtong Huang) que não pertence a 3446 nem 3451 — **verificar a quem pertence** em lotes futuros. Lote 3378–3427 quase completo; pendências abaixo.

**✅ Lote 3378–3427 concluído (44 in-scope → 39 Aceito, 5 Rejeitado):**
- **3381** (micro-hidrelétricas): decisão Kiê = C2 Aceito (mantido na cascata, sem pré-marcar C4).
- **2 colisões resolvidas:** 3379 → `ZHANG et al., 2018b.pdf` (reciclagem de concreto urbano, Chongqing) Aceito; 3412 → `MAES et al., 2021b.pdf` (produção de clínquer) C2 Aceito + C4 Rejeitado.
- C4 pré-marcado no lote: 3382 (frutos do mar), 3391 (remoção de GEE), 3400 (pás de turbina eólica), 3383 (cinza WtE), 3408 (clínquer CSA), 3410 (reciclagem de carbono), 3415 (MSW), 3422 (CCUS), 3425 (eletricidade). C2 Rejeitado: 3387 (louça sanitária), 3394 (asfalto), 3414 (barreira acústica), 3421 (reciclagem de resíduo de construção), 3427 (carpete).

- rows 3328–3377 (2026-06-06): 43 in-scope → **38 Aceito, 5 Rejeitado**. C2 Rejeitado: 3340 (permeabilidade de pavimento permeável), 3341 (asfalto poroso), 3368 (gestão de resíduo de demolição), 3370 (gestão de resíduo de concreto), 3371 (asfalto borracha). C4 pré-marcado: 3333/3342/3343/3350/3351/3357/3369/3376 (captura CO₂, fotocatálise/água, biodiversidade, frutas, solar, planta de cimento, clínquer CSA, resíduo sólido municipal).

**✅ 6 PDFs corrompidos/colisão do lote 3328–3377 resolvidos (rebaixados ez128 + integrados):** 3330 (`KEHINDE, 2024i.pdf`), 3372 (`MADDALENA, 2018i.pdf`), 3376 (`LIIKANEN, 2018i.pdf`); os 3 WANG distintos → 3340 `WANG, 2018i.pdf`, 3368 `WANG, 2018ib.pdf`, 3371 `WANG, 2018ic.pdf` (coluna `pdf` atualizada).

**Validação de PDF + harmonização C2→C4 (2026-06-06):**
- **Validação explícita:** todos os **76 P:Rejeitado** (C2/C4/C8) receberam nota de validação no `comments` (método de extração pdfplumber p.1 + se corrompido). Regra agora vigente para todo novo rejeitado (ver regra abaixo). Falsos-negativos de match por caractere: 2965 (ø/Kløverpris) e 3051 (acento quebrado/Guzmán) — PDFs confirmados corretos.
- **Harmonização C2→C4:** 16 artigos não-construção que estavam em C2 Rejeitado migraram para **C2 Aceito + C4 Rejeitado** (agricultura/pesca/alimentos: 2965, 2970, 2975, 3012; energia/CO₂/processo: 2888, 3004, 3005, 3006, 3007, 3009; metalurgia/resíduos não-construção: 2979, 2990, 2997, 2973; planta de cimento: 3010; floresta/bioenergia: 3256). Mantidos em C2 Rejeitado: materiais de construção não-estruturais (asfalto, telhas, vedação, isolamento, fibrocimento, revestimento, BIPV, micélio, cool pavement, HVAC) e construção-correlatos sem material (gestão de RCD, metodologias de LCA).
- **Regra de validação (vigente):** ao marcar P:Rejeitado, acrescentar ao `comments` `[Validação PDF AAAA-MM-DD: pdfplumber p.1; extração OK|corrompida; sobrenome/título conferido]`.
- **3291** reclassificado C2 Aceito → **C2 Rejeitado** (sistema HVAC não-estrutural).

**✅ 7 PDFs pendentes resolvidos (2026-06-06, rebaixados via CAPES ez128 e integrados):**

| Row | Arquivo final | C2 |
|-----|---------------|-----|
| 3207 | `ZHANG et al., 2024b.pdf` | Aceito — UHPC c/ fibra de aço |
| 3252 | `ZHANG et al., 2024c.pdf` | Aceito — ACV estação de tratamento de água (infraestrutura; revisar C4/C7) |
| 3231 | `BROYLES, 2024i.pdf` (sobrescrito) | Aceito — dataset EPD de concreto |
| 3232 | `BASAVARAJ, 2024i.pdf` (sobrescrito) | Aceito — ICV produção de cimento |
| 3238 | `PYO, 2023i.pdf` (sobrescrito) | Aceito — ativação alcalina de lama de cal (AAM) |
| 3269 | `KHAN et al., 2022c.pdf` | Aceito — geopolímero de resíduo de C&D |
| 3275 | `JIN, 2025ib.pdf` | **Rejeitado** — compósitos de micélio (biomaterial não-estrutural) |

> **⚠️ Verificar em lotes futuros:** o arquivo `ZHANG et al., 2024.pdf` (conteúdo real: "Urban Renewal Design Method… Suzhou", MDPI Buildings) é o artigo correto do **row 3292** (confirmado 2026-06-06). Os rows **3808 e 4332** apontam para o mesmo arquivo → são colisões; baixar os PDFs corretos ao chegar neles.

- rows 3278–3327 (2026-06-06): 41 in-scope → **40 Aceito, 1 Rejeitado (C2)**. C2 Rejeitado: 3296 (fachada BIPV — painel não-estrutural + solar). **Pré-marcações C4 Rejeitado (não-construção/processo, C2 Aceito):** 3297 (troca de combustível no cimento), 3299 (eólica offshore), 3300 (goethita/recuperação de metais), 3310 (biocombustível+cinza de carvão), 3311 (S/S de resíduo perigoso), 3315 (materiais p/ eletricidade), 3316 (poços de petróleo), 3317 (emissões militares), 3320 (fim de vida de turbina eólica). **3308** = corrigendum do 3307 → **C8 Rejeitado** (sem download). 3291 (HVAC) Aceito = candidato C7; 3292 (renovação urbana) Aceito = candidato C4 BRANCO.

Lotes concluídos:
- rows 3028–3077 (2026-06-06): 34 in-scope → todos P:Aceito.
- rows 3078–3127 (2026-06-06): 39 in-scope → 32 Aceito, 7 Rejeitado. Rejeitados C2: 3100 (vedação não-estrutural), 3086 (fibrocimento), 3106 (revestimento), 3108/3109/3111/3126 (ACV de gestão/reciclagem de resíduos — não-material).
- rows 3128–3177 (2026-06-06): 34 in-scope → 29 Aceito, 5 Rejeitado. Rejeitados C2: 3129/3131/3160/3164 (asfalto), 3171 (gestão de RCD — não-material). 3135 KOMKOVA (PDF corrompido) rebaixado via CAPES ez128 e integrado → C2 P:Aceito (materiais álcali-ativados).
- rows 3178–3227 (2026-06-06): 45 in-scope → 41 Aceito, 4 Rejeitado. Rejeitados C2: 3199/3226 (asfalto — reciclagem a frio), 3195 (pavimento semi-flexível base asfáltica), 3209 (reaproveitamento de solo escavado — processo/não-material).

**✅ Colisão de PDF resolvida — row 3189 AMRAN:** NÃO era duplicata. 3184 e 3189 são artigos distintos do Amran que apontavam para o mesmo `AMRAN et al., 2022.pdf`. O arquivo físico era o do **3184** (e01439, correto). O PDF correto do **3189** (e01688 — "fly ash + glass cullet nano additive concrete") foi rebaixado via CAPES ez128 e integrado como `AMRAN et al., 2022b.pdf` (coluna `pdf` atualizada) → C2 `P:Aceito`.

- rows 3228–3277 (2026-06-06): 41 in-scope → **35 Aceito, 6 Rejeitado** (7 downloads já integrados). Rejeitados C2: 3253 (sistema águas pluviais), 3272 (indústria construção — macro), 3256 (produtos florestais/bioenergia), 3267 (CMU+isolamento — térmico), 3277 (cool pavement), 3275 (compósitos de micélio — biomaterial não-estrutural). **Decisão de harmonização (Kiê, 2026-06-06):** artigos não-construção (agricultura, metalurgia, química, captura de CO₂, nuclear, restauração costeira) seguem o caminho **C2 Aceito + C4 Rejeitado** (C4 é o critério literal "não relacionado a construção civil"). Reclassificados nesse padrão: 3051, 3080, 3110, 3113 (lotes anteriores) + 3254, 3257, 3264, 3274 (este lote).

**Pré-marcações C4 Rejeitado (não-construção, confirmadas por leitura do PDF):** 3051 GUZMAN (CO2→metanol), 3080 BAILLET (viticultura), 3110 HENGEVOSS (escândio/metalurgia), 3113 GENEDY (esterco/agropecuária). Todos com C2 `P:Aceito` + C4 `P:Rejeitado`.

**✅ 2 PDFs do lote 3028–3077 resolvidos (rebaixados via CAPES ez128 em 2026-06-06):**

| Row | Arquivo | Resolução | C2 |
|-----|---------|-----------|-----|
| 3030 | BALASBANEH et al., 2021.pdf | PDF correto (CLT vs GLT) integrado, sobrescreveu o Zhang 2018 | `R:Aceito \| P:Aceito` — CLT vs GLT (madeira engenheirada) |
| 3051 | GUZMAN, 2021i.pdf | PDF válido integrado (era JPEG) | `P:Aceito` (C2) + **C4 `P:Rejeitado`** — verificado 2026-06-06: CO2→metanol, energia/química, sem relação com construção (menções a "cement" só em referências) |

> ⚠️ Nota: ao sobrescrever o arquivo errado de 3030, o conteúdo deslocado era Zhang 2018 ("ontology-based structural design") — provável duplicata órfã; não rastreado. Verificar se alguma linha Zhang 2018 ficou sem PDF, se aplicável.

**✅ PDFs inválidos — resolvidos em 2026-06-05 (baixados via proxy CAPES ez128):**

| Row | Arquivo | Estado | C2 |
|-----|---------|--------|-----|
| 2989 | PEYS, 2018i.pdf | ✅ PDF válido integrado | `R:Aceito \| P:Aceito` — polímero inorgânico/geopolímero de escória |
| 2991 | GHEIBI, 2018i.pdf | ✅ PDF válido integrado | `R:Aceito \| P:Aceito` — concreto (produção; ACV poluentes do ar) |
| 3019 | HANANDEH, 2015d.pdf | ✅ PDF válido integrado | `R:Aceito \| P:Aceito` — bloco de concreto vazado + revestimento (decisão Kiê 2026-06-05: aceitar; C3/C7 filtram) |

---

## Contagens gerais (pós-auditoria 22/05/2026 + decisão HABERT 23/05/2026)

| Aba | Linhas de dados | Observação |
|-----|----------------|------------|
| ARTIGOS ACEITOS | 187 | 88 ACEITO + 99 RECUSADO; **75 estudos únicos ACEITO** (74 via bases + CELIK via FE; CELIK ocupa 13 linhas M1–M13) |
| ANÁLISE | 187 | espelha ARTIGOS ACEITOS |
| ANÁLISE DE QUALIDADE | **75** | estudos únicos elegíveis (E1–E7 aprovados); HABERT removido da elegibilidade em 2026-05-23 |
| METANÁLISE | 139 | observações; 37 estudos únicos (Fase 5 expandiu 117→139) |
| SUMÁRIO PRISMA | — | 5 seções; inclui canais "citação" e "comunicação pessoal" |
| FONTES_EXTERNAS | 2 | FE001 CELIK (JÁ INCORPORADO) + FE002 HABERT (**REJEITADO — UF incompatível**; manter como referência bibliográfica normal) |

### Aritmética PRISMA (estudos únicos)

```
5.093 identificados → 2.551 duplicatas → 2.542 triados
2.542 − 2.369 (excluídos triagem) = 173 publicações recuperadas
173 − 99 (E1–E7) = 74 elegíveis via bases
+ 1 fonte externa (CELIK) = 75 elegíveis totais
[HABERT 2012: identificado via comunicação pessoal → REJEITADO do PRISMA em 2026-05-23 — UF incompatível (sistema ponte; resultados em % relativa)]
75 − 6 (qualidade <4,0) = 69 incluídos (síntese quantitativa)
Síntese qualitativa: 0
METANÁLISE: 139 observações
```

---

## Análise de Qualidade ✅ COMPLETA

- **75/75 estudos únicos elegíveis avaliados** (Q1–Q6, escala 0/0,5/1,0)
- **Incluídos (escore ≥ 4,0):** 69
- **Excluídos (escore < 4,0):** 6
- **Pendentes:** 0

---

## Normalização ci / ci_t

### Aba METANÁLISE

| Coluna | Preenchido | Vazio | Observação |
|--------|-----------|-------|------------|
| ci (kg CO₂eq/m³/MPa) | **139/139** ✅ | 0 | COMPLETO |
| ci_t (kg CO₂eq/m³/MPa/ano) | ~21/139 | ~118 | Limitado por artigos que declararam vida útil — comportamento esperado |
| Vida útil técnica (anos) | ~21/139 | ~118 | Idem |

### Aba ANÁLISE

| Coluna | Preenchido | Vazio |
|--------|-----------|-------|
| CO₂eq normalizado (col R) | ~35/76 estudos elegíveis | ~41 |
| ci_t (col S) | parcial | — |

**Próxima ação:** completar normalização na aba ANÁLISE para os estudos elegíveis pendentes (Fase 5 em andamento).

---

## Verificação de números de página

> Estado registrado em 11/05/2026 — pode ter mudado desde então.

- **Verificados [x]:** 76 de 173 (estado de 11/05)
- **Pendentes [ ]:** 97 (estado de 11/05)

---

## Artigos Verificados (76 registrados em 11/05/2026)

- [x] ABOUHAMAD et al., 2020
- [x] ABUSHANAB et al., 2025
- [x] ADAMS et al., 2024
- [x] AL-GHEETHI et al., 2022
- [x] AL-OBAIDY et al., 2022
- [x] ALBRECHT et al., 2025
- [x] ANDERSEN et al., 2022
- [x] ANKUR et al., 2024
- [x] ARRIGONI et al., 2018
- [x] ASSUNCAO, 2020
- [x] BACKES et al., 2022
- [x] BALASBANEH et al., 2018
- [x] BARBHUIYA et al., 2024
- [x] BHAGAT et al., 2021
- [x] BILAR, 2016
- [x] CHO et al., 2025
- [x] CHOI et al., 2023
- [x] COELHO, 2016
- [x] CONG et al., 2024
- [x] CORDOBA et al., 2023
- [x] CORTI et al., 2023
- [x] CUNHA, 2022
- [x] D'ORAZIO et al., 2023
- [x] DA SILVA et al., 2021a
- [x] DA SILVA et al., 2021b
- [x] DE SOUZA et al., 2015
- [x] DEL SERRONE et al., 2023
- [x] DERVISHAJ et al., 2024
- [x] DI MARIA et al., 2020
- [x] DIGULLA et al., 2023
- [x] DING et al., 2023
- [x] DING et al., 2024
- [x] DOLCI et al., 2020
- [x] DONG et al., 2021
- [x] DU et al., 2024
- [x] DURAO et al., 2024
- [x] DYNAN et al., 2023
- [x] EK et al., 2020
- [x] FARAHZADI et al., 2025
- [x] FELICIONI et al., 2023
- [x] FERREIRA et al., 2023
- [x] FIRDOUS et al., 2022
- [x] GROSSI et al., 2023
- [x] GUAYGUA et al., 2024
- [x] HABIBI et al., 2024
- [x] HAFEZ et al., 2024a
- [x] HAFNER et al., 2020
- [x] HAJIESMAEILI et al., 2019
- [x] HAVERKAMP et al., 2025
- [x] HEMMATI et al., 2024
- [x] HERTWICH et al., 2019
- [x] INGRAO et al., 2018
- [x] INMAN et al., 2017
- [x] JANG et al., 2022
- [x] JAYASINGHE et al., 2021
- [x] JI et al., 2025
- [x] KASTIUKAS et al., 2019
- [x] KHORGADE et al., 2023
- [x] KIM et al., 2016
- [x] KIRUPAKARAN, 2024
- [x] KOH et al., 2025
- [x] KONG et al., 2022
- [x] KONO et al., 2018
- [x] KOUVARA et al., 2023
- [x] KUL et al., 2023
- [x] KUMAR et al., 2024a
- [x] KUMAR et al., 2024b
- [x] KURSULA et al., 2024
- [x] LASVAUX et al., 2015
- [x] LEI et al., 2023
- [x] LI et al., 2024
- [x] LI et al., 2025
- [x] LIU et al., 2023
- [x] LYRA et al., 2024
- [x] MA et al., 2021
- [x] MALABI EBERHARDT et al., 2020

---

## Artigos Pendentes de Verificação de Página (97 em 11/05/2026)

- [ ] AKBULUT et al., 2024
- [ ] BRESSI et al., 2022
- [ ] BUMANIS et al., 2022
- [ ] CARRETERO-AYUSO et al., 2018
- [ ] CARROBE et al., 2024
- [ ] CARUSO et al., 2018
- [ ] CHEN et al., 2020
- [ ] CHEN et al., 2024a
- [ ] CHEN et al., 2024b
- [ ] CHIPPAGIRI et al., 2023
- [ ] FOZER et al., 2025
- [ ] GALAN-MARIN et al., 2016
- [ ] GANAPATHI CHOTTEMADA et al., 2023
- [ ] GOMES, 2023
- [ ] HAFEZ et al., 2024b
- [ ] MALABI EBERHARDT et al., 2024
- [ ] MANAN et al., 2025
- [ ] MANJUNATHA et al., 2022
- [ ] MARTINEZ-MUNOZ et al., 2021
- [ ] MARTINEZ-MUNOZ et al., 2022
- [ ] MARTINEZ-MUNOZ et al., 2025
- [ ] MATIAS DE PAULA FILHO et al., 2024
- [ ] MENEGATTI et al., 2022
- [ ] MILANI et al., 2020
- [ ] MING et al., 2024
- [ ] MIR et al., 2022
- [ ] MISTRY et al., 2016
- [ ] MITTERPACH et al., 2023
- [ ] MOHAJERANI et al., 2019
- [ ] MOURA et al., 2025
- [ ] MUELLER et al., 2024
- [ ] NASSAR et al., 2025
- [ ] NAVARRO et al., 2022
- [ ] ONN et al., 2019
- [ ] PAIK et al., 2019
- [ ] PALACIOS-MUNOZ et al., 2018
- [ ] PAPADAKI et al., 2022
- [ ] PARATSCHA et al., 2019
- [ ] PASSUELLO et al., 2014
- [ ] PAVLU et al., 2019
- [ ] PEDROSO et al., 2024
- [ ] PESTA et al., 2020
- [ ] PESTA et al., 2022
- [ ] PONS et al., 2018
- [ ] PRISTERA et al., 2024
- [ ] PUJADAS-GISPERT et al., 2021
- [ ] PUSHKAR et al., 2020
- [ ] QAMHIA et al., 2023
- [ ] RANATUNGA et al., 2023
- [ ] RAZA et al., 2023
- [ ] RIHNER et al., 2025
- [ ] RINNE et al., 2022
- [ ] ROHDE et al., 2023
- [ ] ROSA et al., 2017
- [ ] ROSALES et al., 2020
- [ ] ROSSI, 2013
- [ ] RUIZ SANCHEZ et al., 2021
- [ ] SAMEER et al., 2020
- [ ] SANCHEZ-BURGOS et al., 2024
- [ ] SANCHEZ-PANTOJA et al., 2023
- [ ] SANDAGOMIKA et al., 2024
- [ ] SANGIORGIO et al., 2025
- [ ] SANTOS et al., 2022
- [ ] SANTOS, 2015
- [ ] SANTOS, 2022
- [ ] SBAHIEH et al., 2022
- [ ] SBAHIEH et al., 2023a
- [ ] SBAHIEH et al., 2023b
- [ ] SENSENEY et al., 2023
- [ ] SHANBHAG et al., 2024
- [ ] SIKORA et al., 2023
- [ ] SILVA et al., 2023
- [ ] SOLTANZADEH et al., 2022
- [ ] SOMBRIO, 2015
- [ ] SONG et al., 2020
- [ ] STARCZYK-KOLBYK, 2024
- [ ] TAIT et al., 2016
- [ ] TELLO-AYELA et al., 2023
- [ ] TEPLY et al., 2018
- [ ] UGURAL et al., 2024
- [ ] VACLAVIK et al., 2020
- [ ] VALENCIA-BARBA et al., 2020
- [ ] VAN LOON et al., 2019
- [ ] VENTURA et al., 2022
- [ ] VIDAL et al., 2019
- [ ] VILLALBA et al., 2025
- [ ] VITIELLO et al., 2016
- [ ] VLADIMIROV et al., 2019
- [ ] VOLK et al., 2023
- [ ] VOLK et al., 2024
- [ ] WOLFOVA et al., 2020
- [ ] XIAO et al., 2014
- [ ] YU et al., 2023
- [ ] ZHANG et al., 2023
- [ ] ZHAO et al., 2020
- [ ] ZHENG et al., 2025
- [ ] ZUCARATO, 2020


---

## Estado dos Downloads de PDFs ✅ COMPLETO (2026-06-05)

> Última auditoria: sessão 05/06/2026 — processo de download **concluído**.

### Situação final (05/06/2026) ✅

| Item | Valor |
|------|-------|
| Total de arquivos em `ARTIGOS ACEITOS APÓS REMOÇÃO DAS DUPLICATAS` | **1.798** |
| **Elegíveis com PDF** | **480 / 480** ✅ |
| **Inconclusivos com PDF** | **1.347** |
| Status `Sem acesso` na planilha | **68** artigos |
| Status `Duplicado` | **2.623** |
| `DOWNLOAD_MANUAL.html` | **Apagado** — download concluído, arquivo não é mais necessário |

### Mudanças estruturais — sessão 05/06/2026 (conclusão)

- **Download 100% concluído** — todos os 480 Elegíveis têm PDF; Inconclusivos com acesso público também integrados
- **36 duplicatas físicas removidas** da pasta destino (confirmadas por MD5/DOI)
- **Causa raiz do ciclo de re-download identificada:** arquivos Elsevier salvos com nome PII (`1-s2.0-S...-main.pdf`) em vez de ABNT; sessões anteriores actualizavam um Excel temporário (ex: `articles_final_new_YYYYMMDD.xlsx`) em vez do `articles_final.xlsx` principal, fazendo com que os itens voltassem como pendentes
- **`DOWNLOAD_MANUAL.html` apagado** — não é mais necessário
- **68 artigos marcados como `Sem acesso`** (embargados, bloqueio por servidor, acesso institucional insuficiente)

### Mudanças estruturais — sessão 03/06/2026

- **Scripts de download removidos** — download é agora 100% manual via `DOWNLOAD_MANUAL.html` + CAPES
- **`ELSEVIER_DOWNLOAD.html` eliminado** — tudo num único `DOWNLOAD_MANUAL.html`
- **HTML gerado directamente pelo Claude** (sem script standalone na raiz)
- **Novo status `Sem acesso`** na coluna `status_triagem` — artigos sem acesso no login institucional CAPES
- **Coluna `pdf` com prefixo `R:`/`P:`** adicionada às colunas C1–C7 para diferenciar triagem por resumo vs PDF
- **67 PDFs com nome não-ABNT renomeados** na pasta de destino
- **73 duplicatas novas** marcadas como `Duplicado` no banco

### ⚠️ Incidente 03/06/2026 — deleção acidental de PDFs

44 PDFs em `BAIXADOS MANUALMENTE` foram apagados permanentemente por erro de processo (o Claude aplicou deleção automática de não-matches sem autorização explícita). Os ficheiros não são recuperáveis. O protocolo foi corrigido no CLAUDE.md: ficheiros sem match devem ser movidos para `BAIXADOS MANUALMENTE\PARA VERIFICAR\`, nunca apagados.

### HTMLs de download (estado 03/06/2026 — primeira geração)

| Ficheiro HTML | Elegível | Inconclusivo | Total |
|---|---|---|---|
| `ELSEVIER_DOWNLOAD.html` | 0 | 161 | **161** |
| `DOWNLOAD_MANUAL.html` | 164 | 194 | **358** |

> **Todos os Elegível Elsevier** (16 que constavam como pendentes em 02/06) foram integrados nesta sessão.
>
> **Localização correta da pasta de entrada:** `00_REFERENCIAS\ARTIGOS ACEITOS APÓS REMOÇÃO DAS DUPLICATAS\BAIXADOS MANUALMENTE\` (documentação do CLAUDE.md corrigida em 03/06/2026).

---

### Situação após sessão 02/06/2026

| Ficheiro HTML de apoio | Pendentes Elegíveis | Pendentes Inconclusivos | Total pendente |
|------------------------|--------------------|-----------------------|----------------|
| `ELSEVIER_DOWNLOAD.html` | 9 | 169 | **178** |
| `DOWNLOAD_MANUAL.html` | 54 | 324 | **378** |

- **19 novos PDFs integrados** na sessão de 02/06/2026 (baixados manualmente via CAPES + ResearchGate).
- **12 linhas atualizadas** de URL → caminho de ficheiro na coluna `pdf` de `articles_final.xlsx`.
- **Total de ficheiros na pasta de destino** (`ARTIGOS ACEITOS APÓS REMOÇÃO DAS DUPLICATAS`): **1.247**.

### Histórico — situação em 2026-05-31

> Auditado programaticamente via Python/openpyxl em 2026-05-31.

| Categoria | Com PDF | Sem PDF | Total |
|-----------|---------|---------|-------|
| Elegível | 187 | 330 | 517 |
| Inconclusivo | 887 | 566 | 1453 |
| **Total relevante** | **1074** | **896** | **1970** |

**PDFs únicos na pasta `ARTIGOS ACEITOS APÓS REMOÇÃO DAS DUPLICATAS` (31/05):** 962

### Pendentes por publisher (referência — estado 31/05/2026)
| Publisher | Elegível | Inconclusivo | Total | Método recomendado |
|-----------|----------|--------------|-------|-------------------|
| Elsevier (10.1016) | 122 | 307 | 429 | HTML `ELSEVIER_DOWNLOAD.html` + CAPES proxy |
| MDPI (10.3390) | 100 | 15 | 115 | Download manual mdpi.com |
| Outros DOI | ~54 | ~94 | ~148 | Variável |
| Sem DOI | 32 | 78 | 110 | Manual (Scholar/ResearchGate) |
| URL/outro | 16 | 47 | 63 | Manual |
| Wiley (10.1002+10.1111) | 1 | 29 | 30 | CAPES proxy (manual) |
| T&F (10.1080) | 0 | 8 | 8 | CAPES proxy (testar) |
| ASCE (10.1061) | 2 | 2 | 4 | CAPES proxy (testar) |
| IOP (10.1088) | 1 | 0 | 1 | Falha conhecida (SRAVANI) |

**Arquivos de apoio para downloads:** `ELSEVIER_DOWNLOAD.html` e `DOWNLOAD_MANUAL.html` na raiz da pasta RSL.

---

## Notas sobre nomenclatura

O banco usa nomes simplificados (sem caracteres especiais: ç→c, ã→a, ł→l, š→s).

- ASSUNCAO, 2020 = Assunção, 2020
- DURAO et al., 2024 = Durão et al., 2024
- PESTA et al., 2020/2022 = Pešta et al.
- STARCZYK-KOLBYK, 2024 = Starczyk-Kołbyk, 2024
- SANCHEZ-PANTOJA et al., 2023 = Sánchez-Pantoja et al., 2023
- HAFEZ et al., 2024a/b = dois artigos distintos do mesmo autor/ano
- CHEN et al., 2024a/b = dois artigos distintos do mesmo autor/ano
