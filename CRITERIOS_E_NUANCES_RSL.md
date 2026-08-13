---
titulo: Critérios e Nuances da RSL — Referência Consolidada
descricao: Documento único com o texto literal dos critérios C1–C8, todos os refinamentos/decisões acumulados e o protocolo vigente de confirmação por PDF + extração de metanálise. Consolida RSL_PROGRESSO.md + CLAUDE.md + toda a pasta claude/memoria/rsl-*.
tags: [academico-e-pesquisa, revisao-sistematica, UHPC, metodologia]
status: revisado
ultima_atualizacao: 2026-08-14
---

# Critérios e Nuances da RSL — Referência Consolidada

> **Propósito deste arquivo:** reunir num único lugar tudo que hoje está espalhado entre `RSL_PROGRESSO.md`, `CLAUDE.md` e a pasta `claude/memoria/rsl-*.md`, para consulta rápida sem precisar abrir vários arquivos. **Não substitui as fontes originais** — quando houver dúvida sobre um número (contagens, datas de conclusão), a fonte canônica continua sendo `RSL_PROGRESSO.md` (histórico de lotes) e `PENDENCIAS_AUDITORIA_2026-07-12.md` (estado pós-auditoria). Este arquivo é sobre **regras e nuances de decisão**, não sobre progresso numérico.
>
> Sempre que uma nova nuance for decidida com a Kiê, registrar aqui **e** no arquivo de memória atômico correspondente em `claude/memoria/` (ou criar um novo), mantendo os dois sincronizados.

---

## 1. Como a RSL está estruturada

- **Cascata C1 → C8:** os critérios são aplicados em ordem. Um artigo rejeitado em `Cn` não é avaliado em `Cn+1` (a célula de `Cn+1` fica em branco).
- **`C7` foi REMOVIDO da RSL em 2026-06-22** (decisão Kiê). A coluna ainda existe no Excel mas fica vazia — não citar nem aplicar C7 em trabalho novo.
- **Duas fases de triagem:**
  1. **Triagem por resumo** (título + abstract) → prefixo `R:` nas células C1–C8. **Nunca é decisão final**, mesmo quando parece óbvia (ver seção 3).
  2. **Triagem por PDF** (leitura do corpo do artigo) → prefixo `P:` nas mesmas células. É a única marcação que conta como critério definitivamente avaliado.
- **Fonte canônica dos critérios:** aba `Critérios` do `articles_final.xlsx` (colunas: C# | Título | Descrição | Exemplo | Justificativa | Refinamentos/Decisões). O texto literal está espelhado abaixo (seção 4) e em `RSL_PROGRESSO.md`.

---

## 2. Estado atual (referência rápida — não é a fonte de verdade numérica)

- Cascata C1–C6 + C8 concluída "por resumo" em 2026-06-22.
- **Funil real pós-auditoria (verificado 2026-08-03):** 1.333 artigos com C1–C6 e C8 = Aceito.
- `status_triagem`: Duplicado 2.621 | Inconclusivo 1.066 | Rejeitado 963 | Elegível 383 | Sem acesso 60.
- **Fase ativa desde 2026-08-04:** confirmação por PDF (`P:`) dos ~1.428 artigos Elegível/Inconclusivo + extração simultânea de dados para `meta_analysis_base.xlsx` (tarefa #7 — ver seção 7). Nenhum critério "novo" está em aberto; qualquer trabalho de triagem hoje é confirmação por PDF do que já foi decidido por resumo, ou correção pontual de linha.
- Para números atualizados, consultar `RSL_PROGRESSO.md` e `PENDENCIAS_AUDITORIA_2026-07-12.md` diretamente — eles mudam a cada lote e este arquivo não tenta replicá-los.

---

## 3. Lógica `R:` vs `P:` (regra vigente desde 2026-08-03)

- **`R:`** = decisão preliminar, só com título/resumo. **Nunca é considerada triagem concluída**, mesmo que a decisão pareça óbvia.
- **`P:`** = única marcação que conta como critério definitivamente avaliado. Para registrar `P:Aceito` ou `P:Rejeitado` é obrigatório **ler as primeiras 5 páginas do corpo do artigo** (desconsiderando resumo/título) e, se não bastar, **continuar lendo até conseguir decidir**.
- Formato da célula: `R:<decisão original> | P:<decisão confirmada por PDF>`. O `R:` original nunca é apagado, só complementado. Célula sem `R:` prévio recebe só `P:`.
- **⚠️ Revogado:** uma nota de memória de 2026-06-06 permitia manter só `R:` quando "óbvio". Essa permissão foi revogada pela Kiê em 2026-08-03 — não usar.
- **Verificação de PDF obrigatória:** para cada artigo, conferir título e primeiro autor na primeira página do PDF antes de avaliar qualquer critério. Colisão de PDF → nunca pular; parar, reportar DOI/título/autor e aguardar o PDF correto.
- **Todo `P:Rejeitado`** deve ter nota de validação no `comments`: `[Validação PDF AAAA-MM-DD: <método de extração>; extração OK/corrompida; sobrenome conferido no texto]`. Caracteres quebrados (ø, acentos) causam falso-negativo no match de sobrenome — nesses casos confirmar pelo título e registrar o motivo.
- **PDF ilegível nunca é motivo para decidir por metadados.** Se a extração vier vazia/corrompida/cid-encoded: (1) tentar OCR (`pdf2image`/`pdftoppm` + `pytesseract`/`tesseract`); (2) se falhar, rebaixar versão limpa via CAPES; (3) registrar `[Validação PDF: lido por OCR]` nos comments.

---

## 4. Critérios C1–C8 — texto literal + todos os refinamentos acumulados

### C1 — Antes de 2006
- **Descrição:** "Estudos publicados antes de 2006"
- **Exemplo:** "ANO<2006"
- **Justificativa:** "São estudos publicados antes da primeira publicação da ISO 14040/44 e consequentemente não seguem métodos padronizado de análise."
- Sem refinamentos adicionais — critério puramente factual.

### C2 — Material não estrutural
- **Descrição:** "Materiais que não são estruturais"
- **Exemplo:** "Paredes, materiais asfálticos, elementos arquitetônico, etc..."
- **Justificativa:** "Não são aplicáveis a grandes obras de infraestrutura urbana, foco dessa dissertação."
- **Materiais estruturais moldáveis ACEITOS:** concreto, cimento, UHPC, HPC, geopolímero, concreto reciclado, argamassa **estrutural**, alkali-activated em contexto estrutural. Se o artigo mistura material estrutural moldável com outros → ACEITO. Madeira estrutural industrializada ACEITA (CLT, glulam, LVL e equivalentes — geometria customizável).
- **REJEITA-SE** apenas o que não é estrutural moldável: painéis de revestimento/fachada, isolamento, asfalto, alvenaria decorativa, tijolo cerâmico não-estrutural.
- **Decisão 2026-06-06:** artigos que NÃO são material de construção (captura/sequestro de CO₂ como tema central sem material, processos energéticos — parques eólicos, solar, H₂ —, descomissionamento, restauração costeira/ecológica) → **REJEITADOS direto no C2**.
- **Argamassa de revestimento ≠ argamassa estrutural.** Só "argamassa estrutural" é aceita. Argamassas/materiais de revestimento, reboco, gesso, cal, fachada, assentamento, acabamento → **C2 Rejeitado** (caem no exemplo "Paredes, elementos arquitetônico"). Atenção: gesso/gipsita **como aditivo no concreto/cimento** (regulador de pega) não rejeita — aí o produto é concreto moldável (Aceito).
- **⭐ Regra do "material incidental" (2026-08-04 — exige discussão caso a caso, não auto-aplicar):** quando o material estrutural aparece só como componente secundário/pano de fundo do estudo (sem traço próprio, sem propriedades próprias, só citado como baseline de comparação ou item genérico de bill-of-materials) — **parar e apresentar o caso específico à Kiê antes de decidir C2**, mesmo que pareça igual a um caso já decidido antes (não generalizar o precedente automaticamente). C2 é um critério de **escopo temático** (o material estrutural moldável é o que está sendo estudado?), não de disponibilidade de dado — um número de CO2 existir para o material incidental não muda a decisão, porque geralmente esse número não é comparável (sem traço, sem classe de resistência, unidade por m² de edifício em vez de por m³ de material). Exemplos já discutidos e **rejeitados** por esse padrão: Abouhamad (concreto = fundação genérica em edifício de aço-leve), Adams (telha de concreto = só baseline para filme de resfriamento radiativo), Du et al. 2024d (concreto = só um dos "materiais poluentes" da infraestrutura de parque eólico + eletrolisador, sem fck).
- **⭐⭐ ACV de OBRA DE INFRAESTRUTURA URBANA — ACEITA (decisão Kiê, 2026-08-12; casos 2685 Hafner et al. 2020 e 2662 Du et al. 2024d).** Quando o estudo é a ACV de uma **obra de infraestrutura urbana** em que o concreto é um dos materiais presentes, **C2 = Aceito mesmo sem traço, sem fck e sem CO₂ atribuído ao material**.
  - **⚠️ "Obra de infraestrutura urbana" é MAIS AMPLO do que "edifício".** Esta é a correção expressa da Kiê (2026-08-12) a uma leitura estreita minha: a justificativa literal do C2 é *"Não são aplicáveis a grandes obras de infraestrutura urbana, foco dessa dissertação"* — logo o escopo abrange edificação, bairros, **e também obras de energia, transporte e redes** (parques eólicos, subestações, pontes, vias, saneamento). Não restringir a edifícios.
  - **A pergunta de escopo é: o estudo avalia uma OBRA, ou avalia um PRODUTO/MATERIAL?** Obra com concreto → Aceito. Produto ou material cujo objeto não é obra nenhuma, com o concreto a aparecer só como referência de comparação → continua Rejeitado. Caso que se manteve rejeitado por esta fronteira: **2557** (Adams et al. 2024) — os dez materiais avaliados são filmes finos de arrefecimento radiativo e a telha de concreto é apenas o *baseline*; não há obra.
  - **Ao aceitar, extrair o que existir e registar explicitamente o que não existe.** Nestes artigos o valor costuma vir por m² de área bruta, por edifício ou por unidade de obra; `fck_mpa` e `co2_valor` ficam em branco quando não há atribuição ao material, com a justificação em `observacoes`. **Nunca imputar ao concreto uma parcela do GWP da obra por inferência.**
  - **Ao reverter um `P:Rejeitado` de C2, verificar a cascata:** os `P:` de C3–C8 podem ter sido removidos na limpeza de vazamento, restando só o histórico `R:`. Nesse caso a linha volta a precisar de confirmação por PDF nesses critérios — foi o que aconteceu com a 2662.
  - Alcance estimado à data: ~207 dos 1.326 pendentes têm título de escala edifício/urbana/infraestrutural sem material cimentício no título.
- **Padrão já consolidado — NÃO precisa mais de discussão caso a caso:** "material simétrico comparado" — quando o concreto é uma de várias alternativas de sistema estrutural comparadas com **seu próprio traço completo e seu próprio resultado de GWP/CO2** (não apenas citado como referência) → **C2 Aceito** direto. Exemplos que confirmaram o padrão: Andersen (CLT×concreto), Al-Obaidy (4 sistemas), Chen 2020 (CLT×RC via Athena), Balasbaneh T1 (concreto em estudo de estrutura híbrida de madeira), Corti (laje TCC madeira-concreto, GWP próprio de ambos), Dong (viga SWSSC×concreto comum, 292×397 kg CO2eq/m³), Ek (ponte de concreto×ponte solo-aço, estudo de caso real), Di Maria (bloco carbonatado×concreto PC).
- **⭐ Revisão de literatura sem dados próprios** (Review/Systematic Review — lembrar que C8 NÃO rejeita revisões): não tentar extrair dado da própria revisão. Registrar em `comments`: `[Revisão sem dados próprios — candidatos p/ busca externa: <lista de referências relevantes citadas, autor/ano/tema>]`. Fica como pendência para busca individual posterior (podem já estar no banco sob outro registro, ou virarem "fonte externa"). Não bloqueia o fluxo da RSL. **Atenção:** um artigo pode ser rotulado "review" pelo próprio periódico/resumo e ainda assim ter **dados/modelagem próprios** (ex.: Dynan et al. — resumo diz "this paper reviews" mas são 5 amostras de concreto produzidas e medidas pelos próprios autores; Cong et al. — "Review Article" mas é cálculo de CO2-E com equações autorais). Ler o corpo antes de assumir que é Regra 2.

### C3 — Materiais não moldáveis
- **Descrição:** "Materiais que não podem ser moldados conforme especifidades, em fábrica ou in loco."
- **Exemplo:** "Blocos e tijolos."
- **Justificativa:** "Não são aplicáveis a grandes obras de infraestrutura urbana, foco dessa dissertação."
- **NÃO moldáveis** (forma padronizada única, sem personalização por projeto — blocos, tijolos, unidades de alvenaria) → REJEITADO. **MOLDÁVEIS** (conformados sob demanda, geometria por projeto — concreto, UHPC pré-fabricado, painéis/elementos pré-moldados de geometria variável, madeira CLT/glulam) → ACEITO.
- Concreto celular/espumoso: **AAC = Alkali-Activated Concrete → ACEITO**; **AAC = Autoclaved Aerated Concrete → decidir caso a caso lendo o PDF**.
- **⭐ Regra "bloco/tijolo de material aceito" (2026-08-03):** o exemplo literal "blocos e tijolos = rejeitado" foi pensado para unidades de alvenaria industriais de catálogo (tijolo cerâmico, bloco de concreto padrão). Quando o bloco/tijolo é feito de um material que já tem exceção documentada em C2 (**terra, solo-cimento, geopolímero** — não cerâmica/concreto convencional de catálogo), a rejeição automática não se aplica cegamente:
  - **ACEITO** — prensado/comprimido **sob demanda**, sem padronização industrial de catálogo, produção tipicamente artesanal/local com dimensões ajustáveis ao projeto. Ex.: bloco de terra comprimida (3871), ICEB (4133), tijolo solo-cimento (4717).
  - **REJEITADO** — produto manufaturado **padronizado**, vendido como substituto drop-in de item de catálogo com dimensões fixas. Ex.: paver de geopolímero (2996), "bloco de alvenaria emergente" substituto de CMU padrão (5078).
- **Bloco/tijolo como FONTE de agregado** (triturado e usado dentro de concreto moldável, onde o produto final é o concreto) → **C3 Aceito** (ex.: 4511, 4479, 4408). Só quando o bloco/tijolo é o **produto final** → C3 Rejeitado. (Nota histórica: na triagem manual antiga por resumo, estudos cujo produto final era bloco/tijolo — mesmo de agregados reciclados — já eram descartados; é coerente com esta regra.)
- **Taipa / rammed earth** = terra úmida compactada em fôrmas in loco → parede monolítica portante → **estrutural e moldável → C3 Aceito**. (Ver também regra C6 de terra, que reverteu a rejeição por regionalização.)
- **Cut-stone / pedra de cantaria (dimension stone):** pedra extraída de pedreira e cortada sob medida, usada como parede portante → **C3 Aceito** (tratada como personalizável), mas **pré-marcar nos comments para avaliação em C6** (produção geograficamente restrita). Caso: 4938 (De Toldi & Pestre) — mantido **Rejeitado** em C6.

### C4 — Materiais não relacionados a construção
- **Descrição:** "Materiais que não são relacionados a construção civil"
- **Justificativa:** "Não aderem ao tema da pesquisa"
- **REJEITADO:** setores sem relação com construção civil (medicina, farmácia, biologia, agricultura, alimentos, eletrônica, embalagens, automóvel, aeronáutica, naval não-infra, energia solar/eólica com foco no painel/turbina/processo). Também REJEITADO: processos industriais de produção de precursores SEM ACV do elemento final (produção isolada de clínquer, emissões de fornos de cimento, mineração de agregados sem produto final).
- **ACEITO:** qualquer artigo sobre concreto, cimento, UHPC ou materiais cimentícios em contexto de construção civil.
- **BRANCO** (aceito, marcar "A revisar"): infraestrutura genérica sem material especificado; LCA de sistemas completos sem foco em material.
- **⭐ ADENDO — resíduo/material de setor off-topic usado no concreto (2026-06-13):** mesmo que o artigo seja de setor off-topic, se ele **usa um material/resíduo desse setor com o propósito de melhorar ou substituir o concreto** → **C4 ACEITO**. Ex.: pá de turbina eólica triturada como agregado; casca de arroz/bagaço/lodo/cinza como SCM ou agregado. O que decide é a aplicação como material para o concreto, **não** o setor de origem. Só rejeitar quando o setor off-topic não faz essa ponte (microalgas para biocombustível, poço de petróleo, pesca, tratamento de água sem uso do material em concreto).
- **♻️ Resíduo em estudo de valorização multirota (2026-06-14):** se o estudo avalia várias rotas e UMA delas usa o resíduo como **MATERIAL/INSUMO em cimento/concreto/asfalto** → **C4 ACEITO** (dado da rota cimentícia é extraível). **MAS** resíduo usado só como **COMBUSTÍVEL** no forno (RDF, biossólido como fuel) ou cimento usado só para **imobilizar/descartar** o resíduo (solidificação/estabilização para aterro) → **REJEITADO**. Divisor: resíduo vira MATERIAL do concreto (Aceito) vs vira ENERGIA/é só imobilizado para descarte (Rejeitado).
- **🏗️ ACV de instalação de saneamento (2026-06-14):** ACV de ETA/ETE ou instalação semelhante, cobrindo construção + operação, com concreto/armadura como item de inventário → **C4 ACEITO** como infraestrutura urbana (marcar "A revisar").
- **📋 Critério do inventário para instalações/sistemas ambíguos (2026-06-14):** quando a ACV é de uma instalação/sistema que normalmente seria rejeitado (ex.: gestão de resíduos), verificar se o LCI documenta o concreto com **fluxos de entrada/saída quantificados** (kg, processo ecoinvent, etc.). Se sim → **C4 ACEITO**. Sem fluxos documentados → volta a ser gestão de resíduo (Rejeitado).
- **📖 Método de leitura obrigatório:** NUNCA classificar por resumo/título/metadados. Ler as **3 primeiras páginas** do PDF; se não bastar, continuar lendo. Dúvida real → parar e perguntar.
- **🏷️ Rastreio em rejeitados de C4:** quando o artigo for rejeitado mas trouxer tecnologia relacionada a concreto/cimento, marcar a tag correspondente na coluna `rastreio_potencial_futuro` mesmo assim (ver seção 5) — clínquer→`fator_clinquer`; combustível alternativo/descarbonização do cimento→`outra`; captura/mineralização CO2→`carbonatacao_captura`; aglomerante→`aglomerante_alternativo`.

### C5 — Não menciona emissões de GEE
- **Descrição:** "Não menciona análise de ciclo de vida (ACV), emissão de CO2 ou gases do efeito estufa"
- **Justificativa:** "Unidade essencial para analise de impacto nas metas de redução de emissão de GEE."
- **⭐⭐⭐ REGRA FINAL — OPÇÃO A (2026-06-15, supera todas as anteriores):**
  - **ACEITO** = qualquer artigo que conduza LCA **ou** mencione GWP/CO₂/GHG com **qualquer resultado** — mesmo % relativo, mesmo valor citado de outro estudo, mesmo resultado só em figura não extraível por texto.
  - **REJEITADO** apenas se o PDF inteiro (texto + todas as páginas renderizadas visualmente) não tiver **nenhuma** menção a CO₂/GWP/GHG/LCA/climate change relacionada ao material.
  - **Exceção:** CO₂ puramente analítico-químico (ex.: picos FTIR de carbonatos, sem avaliação ambiental) = Rejeitado.
  - **Obrigatório antes de qualquer Rejeitado:** ler 100% das páginas + renderizar figuras/gráficos visualmente.
  - Regra anterior (14→15/06, DESCARTADA): exigia valor numérico no corpo do texto — não usar mais.
- **PAT regex de triagem auxiliar (nunca decisivo sozinho):**
  `lca|life.cycle.assess|carbon.footprint|embodied.carbon|gwp|global.warming.potential|co2.eq|co2eq|kgco2|greenhouse.gas|ghg|carbon.emission|climate.change|co2|embodied.emission|carbon.intensi|low.carbon`
  Busca robusta: achatar espaços (`re.sub(r'\s+','',texto)`) antes de descartar, porque `pdftotext` pode concatenar palavras.
- **Carbonatação/captura de CO₂** (Journal of CO2 Utilization etc.) = C5 Aceito pela Opção A. Marcar `carbonatacao_captura` no rastreio.

### C6 — Estudos regionalizados (material geograficamente restrito)
- **Descrição:** "Materiais cujo material principal tem produção geograficamente restrita e baixa escalabilidade global, impossibilitando aplicação em contextos internacionais."
- **Exemplo:** "Bamboo/bambu como material estrutural principal; fibras naturais de produção regional sem dados globais (sisal, juta, cânhamo, kenaf, linho, agave, fibra de coco)"
- **Justificativa:** "Materiais de produção geograficamente restrita não são aplicáveis a grandes obras de infraestrutura urbana em escala global."
- **REJEITADO:** produção geograficamente restrita sem escalabilidade global (bambu como material principal). **ACEITO:** produção global/exportável (concreto, cimento, UHPC, geopolímero, cinza volante, escória, cinza de casca de arroz, cimentícios com resíduos amplamente disponíveis); LCA com inventários regionais não conta contra o material (o critério é sobre o MATERIAL, não a origem dos dados do inventário). **BRANCO:** não envolve claramente nenhum desses materiais.
- **C6 NÃO avalia função estrutural** (já filtrada em C2/C3) — trata só de restrição geográfica/escalabilidade do material.
- **⭐ Material de terra (regra revisada 2026-06-21):** rammed earth/taipa, adobe, cob, earthen, terra estabilizada/álcali-ativada = **ACEITO** — terra/solo é material universal e escalável, disponível em toda parte; a restrição da taipa é de **técnica/mão-de-obra**, não de disponibilidade do material. Palha (straw bale) idem = resíduo universal. **Exceção: bahareque** (estrutura de bambu preenchida com terra) = Rejeitado pelo bambu (bambu ≠ terra, geograficamente restrito).
- **Fibra natural** (sisal, juta, cânhamo, kenaf, linho, agave, coco): **sem regra automática — decidir caso a caso.** Princípio emergente: fibra natural como REFORÇO incidental num material global (concreto) = Aceito; fibra natural REGIONAL como material-foco do estudo = Rejeitado.
- **Cut-stone** (pedra de cantaria) = **Rejeitado** (produção concentrada).
- **Resíduo agrícola/vegetal como SCM/agregado em concreto:** UNIVERSAL = Aceito (bagaço de cana, casca de arroz, aguapé invasor, lignina kraft, palha de cereais, plantas invasoras); REGIONAL CONCENTRADO = Rejeitado (ex.: cinza de açaí amazônico).
- **Cortiça** como material relevante do estudo = **Rejeitado** (produção concentrada).
- **Materiais costeiros naturais** (coir/juta/concha de ostra) fora do escopo de concreto urbano = **Rejeitado**.
- **Glossário:** *taipa* (rammed earth) = terra úmida socada em fôrmas, parede monolítica portante; *adobe* = tijolo de terra crua; *cob* = terra+palha modelada à mão; *bahareque* = estrutura de bambu/madeira preenchida com terra.

### C7 — REMOVIDO (2026-06-22)
- Existia como "foco em energia operacional sem emissões de produção" (B6/B7 sem A1-A3/cradle-to-gate). Removido da RSL por decisão da Kiê. Coluna existe no Excel mas vazia — não aplicar, não citar em trabalho novo.

### C8 — Artigos de opinião sem dados primários
- **Descrição:** "Editoriais, opinion papers, commentaries, perspectives, cartas ao editor — sem metodologia nem dados originais de ACV. Revisões sistemáticas e metanálises são ACEITAS."
- **Exemplo:** "Editorial, Letter to Editor, Erratum, Retracted, Correction; viewpoint/commentary sem metodologia."
- **Justificativa:** "Sem metodologia ou dados originais, não contribuem com dados primários para extração de CO₂/fck."
- **REJEITADO** (por `document_type`): Editorial, Editorial Material, Erratum, Retracted, Correction, Letter, Note, Short Communication.
- **REJEITADO** (por título/resumo): "letter to the editor", "opinion paper", "viewpoint", "commentary", "editorial".
- **NÃO rejeitar:** Review, Systematic Review, Meta-analysis, Literature Review (mas ver Regra 2 do C2 sobre revisões sem dados próprios).
- Decidido por metadado (`document_type`), disponível sem PDF → usa prefixo `R:`.

---

## 5. Coluna `rastreio_potencial_futuro` (coluna 33)

Marca tecnologias promissoras com potencial estrutural futuro, **independentemente** da decisão C2. Tags separadas por `; `:

| Tag | Cobertura |
|---|---|
| `biocimento` | MICP/EICP, precipitação microbiana de calcita, concreto autocicatrizante por bactérias |
| `fator_clinquer` | Redução/substituição do fator clínquer (LC3, argila calcinada) |
| `aglomerante_alternativo` | Geopolímero, álcali-ativado, MgO, CSA, LC3 **e** SCM parcial (cinza volante, escória, sílica, metacaulim, cinza de casca de arroz/bagaço, pó de vidro, biochar) — abrangência ampla |
| `carbonatacao_captura` | Carbonatação/sequestro de CO2 no próprio material, self-healing |
| `combustivel` | Resíduo/combustível alternativo queimado no forno de cimento |
| `outra` | Qualquer outra tecnologia promissora aplicada caso a caso |

**Regra biocimento:** biocimentação **standalone** (MICP/EICP em solo/areia, "growing bricks") → **C2 Rejeitado + marca** `biocimento`. Biocimento **como aditivo em concreto estrutural** (ex.: concreto autocicatrizante) → **C2 Aceito + marca**.

---

## 6. Mapa de colunas do `articles_final.xlsx` (índices openpyxl, 1-based)

| Campo | col | Excel |
|---|---|---|
| `pdf` | 11 | K |
| `url` | 12 | L |
| `status_triagem` | 20 | T |
| `C1` | 21 | U |
| `C2` | 22 | V |
| `material_C2` | 23 | W — ⚠️ fica ENTRE C2 e C3 |
| `C3` | 24 | X |
| `C4` | 25 | Y |
| `C5` | 26 | Z |
| `C6` | 27 | AA |
| ~~`C7`~~ | 28 | AB — vazio |
| `C8` | 29 | AC |
| `comments` | 32 | AF |
| `rastreio_potencial_futuro` | 33 | AG |

**Armadilha fatal:** não usar `zip(range(21,29), [...])` — pula `material_C2` e desloca C3–C8. Usar sempre o dict explícito.

**IllegalCharacterError:** limpar toda string antes de escrever: `re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', str(s))`.

**Formato das células C1–C8:** preservar `R:` existente e acrescentar `P:` separado por ` | ` (`R:Aceito | P:Aceito`); célula vazia recebe só `P:Aceito`/`P:Rejeitado`. Colisão sem PDF correto: aguardar resolução, não registrar `P:`.

**`material_C2`:** preencher para artigos `P:Aceito` em C2, com material principal + contexto (ex.: `"geopolímero para impressão 3D (revisão de materiais precursores)"`). Rejeitados em C2 não preenchem.

**Lógica de cascata / vazamento:** `P:` é o histórico de quem foi triado por PDF — nunca apagar um `P:Rejeitado` anterior. Rows fora-da-cascata (`status_triagem` ∈ Duplicado/Sem acesso/Rejeitado-por-resumo) nunca recebem `P:`. Se um artigo é rejeitado por PDF num critério Cn que **já tinha** `P:` em critérios posteriores Cm>n (herdados de uma passada anterior), isso é "vazamento de cascata" — remover os `P:` de Cm>n ao rejeitar retroativamente em Cn (ex.: linha 2662 rejeitada em C2 após já ter C3-C8 com `P:Aceito` de uma passada antiga — os `P:` de C3-C8 foram removidos, mantendo só `R:`).

---

## 7. Fase atual — confirmação por PDF + extração de metanálise (tarefa #7)

Escopo: ~1.428 artigos Elegível/Inconclusivo com C1 `P:Aceito` mas ainda sem `P:` em C2 (ou critério posterior). Para cada um: ler ≥5 páginas do corpo (protocolo da seção 3), confirmar/reverter C2–C6 e C8, e — se aceito e com dados quantificáveis — extrair para `meta_analysis_base.xlsx` (aba `dados_fck`).

### 7.1 Protocolo de leitura
1. Buscar o PDF no Google Drive (`search_files` na pasta de PDFs aceitos).
2. Ler o corpo completo (não só abstract) — arquivos grandes: salvar o `fileContent` em scratch e ler em blocos, ou usar `Grep` para localizar tabelas/seções de resultados (`Table`, `kg CO2`, `GWP`, `MPa`).
3. **Se a extração de texto do Google Drive truncar antes do capítulo de resultados** (documentos muito longos, ex. teses/dissertações de 100+ páginas): baixar o PDF bruto via `download_file_content` (base64), decodificar e salvar localmente, e reprocessar com `pdftotext -layout` (poppler-utils; instalar via `apt-get install poppler-utils` se preciso). Caso confirmado: Coelho (2609/2632), onde a extração do Drive parava no início do capítulo 4 mas o `pdftotext` local recuperou os Quadros de resultados completos.
4. Confirmar C2 (aplicando a seção 4 acima, incluindo Regra 1/Regra 2 quando cabível) e, se aceito, seguir a cascata C3–C6/C8 (normalmente já vêm com `P:` de passadas anteriores — só reconfirmar se algo não bater).
5. Escrever `C2 = "R:Aceito | P:Aceito"` (ou `P:Rejeitado`) + comentário datado explicando a decisão + `status_triagem` atualizado (`Elegível` quando toda a cascata fecha em Aceito; `Rejeitado` quando cai em algum critério — nesse caso limpar `P:` de critérios posteriores, ver seção 6).
6. Extrair dados para `meta_analysis_base.xlsx` quando aplicável (seção 7.2).
7. Processar em lotes de 5, commitar e enviar (push) ao final de cada lote com mensagem descritiva.

### 7.2 Extração para `meta_analysis_base.xlsx` (aba `dados_fck`)

**Colunas (18):** `row_id, doi, titulo, autores, ano, journal, material, fck_mpa, classe_resistencia, idade_dias, tipo_corpo_prova, fonte_no_pdf, observacoes, co2_valor, co2_unidade, co2_fonte_no_pdf, durabilidade_resumo, durabilidade_fonte_no_pdf`.

**Quando criar uma linha:**
- O artigo tem dado próprio (experimento, ACV própria, ou ACV própria aplicada a traços compilados da literatura — ver padrão abaixo) — não uma revisão pura (ver Regra 2 do C2).
- Sempre citar `fonte_no_pdf`/`co2_fonte_no_pdf` com a tabela/seção exata de onde veio o número — nunca preencher `fck_mpa`/`co2_valor` sem o PDF aberto e conferido.
- **Valor só disponível em gráfico/figura, não em texto:** ainda assim criar a linha, com `fck_mpa`/`co2_valor` em branco e uma nota explícita em `observacoes` (`"valor apresentado apenas graficamente (Fig. X), não extraível em texto"`). Não inventar o número lendo a régua do gráfico.
- **Comparação simétrica (material_C2 "simétrico"):** quando o artigo compara concreto com uma alternativa (madeira, aço, solo-aço, etc.), extrair os dados de **ambos os materiais** quando o comparador também tiver traço/GWP próprios — útil para contextualizar a metanálise mesmo que o foco seja o concreto.
- **⭐ Concreto armado: a armadura FAZ PARTE do material (regra Kiê, 2026-08-12).** Quando o estudo reporta o aço de armadura como linha separada do concreto (típico de ACV de edifício, onde o inventário usa processos EcoInvent distintos — `Concrete` e `Reinforcing steel`), **somar as duas parcelas** para obter o CO₂ do produto. O raciocínio: sendo concreto *armado*, o aço integra o produto, do mesmo modo que as fibras integram um UHPC. Registrar em `observacoes` as parcelas somadas e a evidência de que não há dupla contagem.
  - **Como verificar se as linhas são complementares ou sobrepostas** (obrigatório antes de somar): (a) checar se a massa volumica por elemento = densidade do concreto base + taxa de armadura em kg/m³ — se sim, a massa do elemento já inclui o aço e a tabela de materiais foi desagregada por processo; (b) calcular os fatores de emissão implícitos e conferir se caem na faixa esperada de cada processo (aço de armadura ≈ 2,0–2,3 kg CO₂/kg; concreto estrutural ≈ 0,09–0,12 kg CO₂/kg, ou 220–300 kg CO₂/m³); (c) conferir se o grupo "Metals" da tabela de impactos contém apenas a armadura ou também outros metais (perfis, deck, telha) — se contiver outros, somar só a parcela da armadura. Caso resolvido: linha 2674 (Ferreira et al. 2023), onde os três testes confirmaram complementaridade e o CO₂ do produto passou de 2.774.402 para **7.668.185 kg CO₂-eq** (17% → 47% do edifício).
  - **Efeito na intensidade:** com taxas de armadura altas o aço pode dominar. Em 2674, a 191 kg/m³, o aço contribui ~403 kg CO₂/m³ contra ~228 do concreto — a intensidade quase triplica em relação a contar só o ligante. Preferir sempre a intensidade **por tonelada** quando o volume não for confirmável por soma direta do bill of quantities (elementos medidos em m² com espessura não são somáveis sem reconstruir a geometria).
- **ACV própria sobre traços compilados de outros artigos** (padrão confirmado nesta sessão, ex. Coelho/Assunção/Cong): quando o estudo não fez experimento mecânico próprio mas **computou seu próprio GWP/impacto ambiental** (SimaPro/Ecoinvent/modelo próprio) sobre traços de fck citados de fontes externas — **não é Regra 2** (não é revisão sem dados próprios), porque a análise ambiental é contribuição original do estudo. Documentar em `observacoes` que o fck vem do artigo-fonte e o CO2 é calculado pelo estudo em avaliação.

**⭐ Valor derivado tem de ser marcado e documentado (regra Kiê, 2026-08-12).** Todo número que **não está publicado na fonte** e resultou de cálculo feito durante a extração recebe **três marcações redundantes**, para que nenhuma via de leitura perca a informação:

1. **Cor da célula** — fundo âmbar `FFE699` (derivado) ou `FFF2CC` (parcialmente derivado) na própria célula do valor.
2. **Comentário na célula** — memória de cálculo completa: de que números publicados partiu, que operação foi feita, que ressalvas existem.
3. **Prefixo textual** — `[DERIVADO]` ou `[PARC. DERIVADO]` no início de `co2_unidade`. **É o único marcador que sobrevive à exportação para CSV/pandas/R** — cor e comentário perdem-se; por isso o prefixo não é opcional.

A aba **`LEGENDA`** do `meta_analysis_base.xlsx` documenta o código de cor e mantém o inventário das linhas derivadas.

⚠️ **Não confundir com "calculado pelos autores".** Se a ACV própria do artigo, ou o modelo próprio dos autores, produziu o número, isso é **dado publicado** — transcreve-se sem marca. "Derivado" é só quando a conta foi feita **aqui, na extração**. Verificação de 2026-08-12: das 18 linhas com indício de cálculo, apenas 7 eram derivadas (10, 11 parcial, 1556, 1557, 1562, 1678, 1679); as de `row_id` 2609, 2611 e 3087 são valores publicados pelas fontes.

⛔ **Nunca derivar valor a partir de comparação percentual verbal sem antes esgotar a busca pelo valor publicado (lição de 2026-08-12, linha 1562 / row_id 2588).** Frases do tipo *"o sistema X emite 25–40% menos que Y"* **não são bandas de incerteza** — são resumos verbais aproximados, frequentemente imprecisos face aos próprios números do artigo, e podem abranger mais de uma comparação em simultâneo. Antes de inverter uma frase dessas:
1. Procurar a tabela de valores associada às figuras (muitos PDFs trazem os números da figura como texto, fora da secção de resultados — inclusive depois das referências, na extração).
2. Cruzar os valores encontrados com as âncoras citadas no corpo do texto para confirmar o mapeamento de rótulos.
3. Só derivar se o valor realmente não existir em lado nenhum — e, mesmo aí, marcar como derivado e assinalar a linha.

No caso 2588 a derivação produziu `~4.100–4.600` quando o valor publicado era **5.840** — a faixa nem continha o valor real, porque a frase do próprio artigo subestimava a diferença (43,3% e 41,1% reais contra os "25–40%" declarados).

**Preferir sempre a grandeza que não depende de estimativa.** Quando a derivação exige um intermediário incerto (ex.: volume estimado por massa ÷ densidade), extrair também a forma que só usa valores publicados e assinalar qual é a robusta — caso 2674, onde a intensidade por tonelada é publicada-derivada direta e a intensidade por m³ depende de um volume estimado.

**⛔ Verificação obrigatória do PDF por DOI, antes de qualquer leitura (regra reforçada pela Kiê, 2026-08-13).** Conferir título e primeiro autor na primeira página **não basta** — apanha colisões grosseiras, mas não as subtis (mesmo primeiro autor, mesmo ano, artigo diferente). Antes de avaliar qualquer critério ou extrair qualquer dado:

1. Extrair o DOI do texto do PDF (`10\.\d{4,9}/[-._;()/:A-Za-z0-9]+`) e compará-lo com a coluna `doi` do banco.
2. Divergiu → **é colisão de PDF**. Parar, reportar linha, DOI do banco e DOI do PDF, e aguardar o ficheiro correto. Não decidir, não extrair.
3. Documento sem DOI (dissertações, teses, relatórios) → conferir título **e** primeiro autor **e** instituição/ano, e registar essa via nos `comments`.

**Causa estrutural, medida em 2026-08-13:** a convenção `SOBRENOME et al., ANO.pdf` **não é única** — dois artigos diferentes do mesmo primeiro autor no mesmo ano colapsam no mesmo ficheiro. Diagnóstico do banco nessa data: 250 nomes de ficheiro servem mais de uma linha (536 linhas); destes, **56 ficheiros têm linhas com DOIs diferentes entre si — 131 linhas, das quais 100 já tinham decisão `P:` tomada**. Caso confirmado: linha 4295, cujo `ALOTAIBI et al., 2022.pdf` tem DOI `10.1038/s41598-022-09723-7` (Scientific Reports, areias biocimentadas por EICP) quando o banco regista `10.3390/buildings12081203` (Buildings, edifício residencial em altura) — a rejeição de 2026-07-12 foi decidida sobre o artigo errado.

**Verificação obrigatória de DOI antes de confiar num valor numérico já existente na planilha:**
```
curl -s -w '\n__HTTPSTATUS__%{http_code}' https://api.crossref.org/works/<DOI>
```
- Status 404 → DOI não existe → fabricado.
- Status 200 mas título retornado sem relação com `material`/`titulo` da linha → fabricado.
- `doi="pending"` ou vazio → candidato legítimo aguardando resolução, não é fabricação — não apagar sem investigar.
- **Histórico (2026-08-14):** 233 das 1.794 linhas então existentes (13%) tinham DOI inexistente ou de artigo sem relação (71 com fck/CO2/durabilidade inventados) — removidas após verificação e aprovação da Kiê. Regra permanente: nunca confiar num dado numérico dessa planilha sem essa verificação, especialmente linhas com título abreviado tipo "SOBRENOME AAAA — assunto".

### 7.3 Erros já cometidos nesta fase (para não repetir)
- **Esquecer de escrever o `C2` em `articles_final.xlsx` depois de já ter lido o PDF completo** — aconteceu com as linhas 2606/2607 no lote 4 (leitura feita, decisão tomada, mas a escrita no Excel ficou pendente até o lote seguinte reacusar as linhas como não-confirmadas). Sempre confirmar que a escrita foi persistida antes de passar para o próximo artigo do lote.
- **Deixar `status_triagem` desatualizado** mesmo com toda a cascata `P:Aceito` — checar consistência com linhas irmãs do mesmo lote antes de fechar.

---

## 8. Links de download (proxy CAPES)

Sempre fornecer links de PDF no **formato proxy CAPES**, nunca link direto do editor (Unpaywall pode marcar `is_oa=true` incorretamente para artigos na prática pagos).

- Formato: reescrever o host (pontos→hífens) + sufixo `.ezNNN.periodicos.capes.gov.br`, usando a **página do artigo** (não `content/pdf`) — é ela que renderiza "Download PDF / Access provided by CAPES". `ezNNN` é atribuído por sessão (confirmar número atual com a Kiê se mudar; último registrado: `ez128`).
  - Springer/Nature: `https://link-springer-com.ez128.periodicos.capes.gov.br/article/{DOI}`
  - ScienceDirect: `https://www-sciencedirect-com.ez128.periodicos.capes.gov.br/science/article/pii/{PII}`
  - ACS: `https://pubs-acs-org.ez128.periodicos.capes.gov.br/doi/{DOI}` (pode dar 404 → buscar pelo DOI no Portal CAPES)
  - RSC: `https://pubs-rsc-org.ez128.periodicos.capes.gov.br/en/content/articlelanding/{ano}/{cc}/{doi-suffix}`
- Sempre oferecer também cópia OA de repositório (PMC, Zenodo, handle institucional) quando existir — abrem sem proxy.

---

## 9. Índice de arquivos-fonte (o que cada um ainda guarda de melhor)

| Arquivo | O que tem de único |
|---|---|
| `RSL_PROGRESSO.md` | Histórico completo de lotes de cada critério (contagens, casos individuais resolvidos, colisões de PDF) — fonte canônica de progresso numérico |
| `PENDENCIAS_AUDITORIA_2026-07-12.md` | Auditoria de qualidade de dados do funil C1-C8 (10 achados, 1 pendência aberta: linha 2897) |
| `CLAUDE.md` | Ponto de entrada do vault, convenções de arquivamento, processo de download de PDFs (4 camadas), lições de nomenclatura |
| `claude/memoria/rsl-*.md` | Memória atômica por nuance — continuam existindo e são a fonte "viva" onde novas decisões devem ser registradas primeiro; este arquivo consolida o que já existia até 2026-08-14 |
| `claude/memoria/MEMORY.md` | Índice de todos os arquivos de memória do vault (não só RSL) |

**Manutenção deste arquivo:** ao decidir uma nuance nova durante a triagem, registrar em `claude/memoria/` (arquivo novo ou existente) **e** atualizar a seção correspondente aqui. Rodar a skill `dreaming` periodicamente para garantir que os dois fiquem sincronizados.
