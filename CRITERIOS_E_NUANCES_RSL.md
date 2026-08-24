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
- **⭐ Revestimento vence a família do material (2026-08-23, caso 4491 Wang et al., geopolímero):** a lista de materiais aceites nomeia «geopolímero» sem qualificador, o que parece aceitar qualquer geopolímero. **Não aceita.** O C2 decide pela **aplicação**, não pela família — a própria lista qualifica «alkali-activated *em contexto estrutural*», e a regra da argamassa abaixo mostra o mesmo padrão. Um revestimento protector de geopolímero aplicado sobre estrutura existente é **Rejeitado**. Sinais que o denunciam: unidade funcional em volume de *coating*, ensaios de dureza e **aderência ao substrato** em vez de compressão, e zero ocorrências de `compressive`/`flexural` no documento.
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
- **⭐ C2 ou C4? O discriminador é a FRONTEIRA DO SISTEMA (2026-08-23, casos 4127 e 4999, mesmo autor e mesmo tema).** Quando um estudo de processo industrial é rejeitado, é fácil hesitar entre o C2 («não é material de construção») e o C4 («produção isolada de precursor sem ACV do elemento final»). A regra:
  - **Não há material cimentício dentro da fronteira → C2.** Caso 4127: ACV da blendagem de resíduos perigosos, com o artigo a excluir expressamente «o consumo do blend nos fornos de clínquer». Não há cimento nenhum no sistema.
  - **Há material cimentício dentro da fronteira, mas falta o elemento final → C4.** Caso 4999: unidade funcional «1 tonelada de clínquer produzida», excluindo a produção de cimento e os seus usos. O clínquer está lá dentro, logo o C2 passa; o que falta é a jusante.
  O veredito final é o mesmo (fora da RSL), mas o critério registado muda a contagem do PRISMA por critério — por isso não é indiferente.
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

---

# ⚠️ REESTRUTURAÇÃO EM 4 ETAPAS — em desenho desde 2026-08-24

> **Estado: em definição.** A Kiê decidiu reorganizar a aplicação dos critérios por etapas,
> ordenadas por custo de evidência, e transformar os dois critérios mais subjectivos
> (material estrutural e menção a GEE) em **testes quantitativos**. Isto substitui a
> estrutura C1–C8 descrita acima, que fica como histórico.
>
> **Nada disto está aplicado ao banco ainda.** As secções acima continuam a descrever o
> que está lá dentro. Não misturar.

## Porquê

Praticamente todas as decisões difíceis do projecto foram juízos de C2 — «este laminado é
estrutural?», «este revestimento é estrutural?», «o concreto é incidental nesta ACV?». Todo
o aparato do «material incidental», da «obra de infraestrutura urbana» e do «material
simétrico comparado» existe porque o C2 era um critério de *escopo temático*. Substituí-lo
por um teste numérico — o artigo declara resistência ≥ 20 MPa? — torna a triagem objectiva
e reprodutível.

Além disso, alinha a inclusão com o que a metanálise precisa. Na estrutura antiga entravam
no funil artigos que não contribuíam com nada (só MJ, ou só dados de terceiros, ou `fck` sem
CO₂) e caíam depois, na extracção — uma **exclusão escondida** que o PRISMA não contava.

## As quatro etapas

### Etapa 1 — Metadados (título, resumo, tipo de documento). Não abre PDF.

⭐⭐ **REGRA DA DÚVIDA: nesta etapa, na dúvida ACEITA-SE.** É a convenção do PRISMA para
triagem por título e resumo — desenhada para ser **sensível**, não específica. Só se rejeita
quando os metadados deixam claro que o artigo cai no critério. **O erro não é simétrico:**
rejeitar por dúvida perde um artigo bom para sempre e ninguém dá conta; aceitar por dúvida
custa uma leitura de PDF a mais na etapa seguinte.

Ordem de aplicação, que importa porque cada artigo é contado no **primeiro** critério que o
exclui:

1. **Ano** — antes de 2006 (o antigo C1, inalterado).
2. **Tipo de documento** — editoriais, erratas, cartas (o antigo C8). Decidido por
   `document_type`. ⚠️ **Revisitável:** se mais tarde o PDF revelar que é artigo de opinião,
   rejeita-se retroactivamente por este critério.
3. **Moldável** — o antigo C3. ➕ **Telha entra na família «blocos e tijolos»** (calibrado
   pela Kiê, 2026-08-24): é produto de catálogo, forma única, sem personalização por
   projecto — a justificativa do critério aplica-se-lhe palavra por palavra. Vale também
   para **paver** e **telha-canal**. ⚠️ *Excepção que se mantém:* telha ou tijolo usados como
   **fonte de matéria-prima** (triturados para dentro de outro material) continuam a
   **aceitar** — o que conta é o produto final. E quando o objecto do estudo é o **ligante**,
   com os blocos ou pavers apenas como aplicação pretendida, também aceita.
4. **Relacionado a construção** — o antigo C4. Duas calibrações da Kiê (2026-08-24):
   - ⭐ **Processo que torna materiais estruturais menos emissores = ACEITA.** A regra antiga
     («rejeitar produção isolada de precursores sem ACV do elemento final») estava a apanhar o
     próprio tema da dissertação — rejeitaria uma tese sobre desenvolvimento de cimento
     sustentável. **O que decide não é se o objecto é um processo ou um material, é se o
     processo resulta em menor emissão de CO₂ para materiais estruturais.** Casos: 2597
     (clinquerização com coprocessamento de resíduos) e 2569 (classificação a ar de areia
     manufaturada, que é agregado de betão) — **os dois aceitam**.
   - ⭐ **A aplicação decide, não a família do material.** Material de construção usado num fim
     off-topic **rejeita**. Caso 2642: betão e tijolo triturados como **substrato de plantas**
     em paredes vivas. É a mesma regra que já vale para o revestimento de geopolímero no C2
     antigo, agora aplicada no sentido inverso da seta.
   - 📌 **O aço entra** (confirmado pela Kiê, 2026-08-24). O critério de resistência da Etapa 2
     aceita qualquer material com força por área, e o aço passa com folga. Estruturas
     metálicas com CO₂ declarado entram na metanálise **como família própria**.
5. **Acesso ao PDF** — em **último**, de propósito: só faz sentido perguntar «conseguimos
   obter?» depois de o artigo ter sobrevivido à triagem temática.

⚠️ **O critério de acesso só se aplica depois de esgotadas as vias de obtenção.** Tudo o que
for possível descarregar, descarrega-se e avalia-se em todos os critérios. Só o que não vier
por via nenhuma — incluindo as que a Kiê tenta pessoalmente — é que se marca como sem acesso
e se rejeita.

### As regras que a triagem por metadados obrigou a escrever (24/08/2026)

Todas saíram de casos concretos que os subagentes levantaram e a Kiê arbitrou.

**⭐ Aplica-se em dois passos, nesta ordem.** *Passo 1:* a peça é um produto de catálogo de
forma fixa? Se **não** é — geometria por projecto, prensada sob demanda, dimensões
ajustáveis — **aceita e pára aqui**. *Passo 2:* só se for de catálogo, pergunta-se o que o
estudo mede. ⚠️ **O passo 2 é uma porta de entrada, não de saída:** só pode transformar
Rejeitado em Aceito, nunca o contrário.

**⭐ O discriminador do passo 2 — o que é que o estudo mede?** **Aceita** se caracteriza o
material, o que exige **as duas condições**: (i) varia um constituinte da mistura *e*
(ii) mede propriedades. **Rejeita** se trata a peça como produto acabado. ⚠️ Ter só (ii) sem
(i) — uma ACV que compara quatro tipos de tijolo prontos e de passagem tabela a compressão de
cada um — é comparação de produtos, não caracterização de material.

**⭐ Manda a lógica, não a lista.** O critério não é «está na lista de blocos e tijolos», é
«é um produto de catálogo de forma fixa». Rejeitam também telha, paver, telha-canal, louça
sanitária, tubo, painel modular de série e molde.

**⭐ Elemento construtivo (parede, painel, partição, fachada, cobertura).** Tem duas leituras:
como **conjunto** é feito à medida do projecto, mas as **peças** que o compõem são de
catálogo. A regra fixa o nível: **aceita por omissão** (olha-se para o conjunto), **excepto**
quando o próprio artigo desce ao nível da peça, comparando materiais **por unidade de área**
(1 m² de partição). Aí foi o autor que escolheu o nível, não nós. **O nível de análise do
artigo manda.**

**⭐ Energia: a estrutura aceita, o dispositivo rejeita.** Torre, fundação e barreira acústica
aceitam; pá, nacelle, gerador, painel fotovoltaico e casco flutuante rejeitam.

**⭐ Sem material *e* sem obra rejeita** — mas só no `E1_construcao`. A regra «artigo sem
material aceita» vale para o `E1_moldavel`. Se há obra sem material nomeado, aceita.

**⭐ Combustível em forno de cimento aceita se mostrar redução na emissão da produção do
cimento.** Resolve o choque entre «resíduo só como combustível rejeita» e «processo que baixa
a emissão de materiais estruturais aceita». O teste é decidível pelo resumo: há resultado de
emissão atribuído ao cimento ou ao clínquer?

**⭐ A aplicação decide, não a família do material** — nos dois sentidos. Betão triturado que
vira substrato de plantas rejeita (2642); betão moldado in loco que *é* a envolvente do
edifício e por acaso hospeda plantas aceita (4306).

📌 **O `E1_moldavel` corta pouco, e é esperado** (medido no lote 1: 58 em 60 passaram). A
razão é estrutural: muitos artigos do corpus são bibliometrias, revisões de gestão, estudos
de BIM — **não têm material nenhum**, e não se pode dizer que um material inexistente não é
moldável. Eles morrem depois na Etapa 2, por falta de resistência. Consequência a assumir no
PRISMA: **a Etapa 2 faz o grosso do trabalho de exclusão**, e isso é por desenho.

### Etapa 2 — Análise **quantitativa** do PDF (desconsiderando título e resumo)

6. **Resistência** — o artigo declara resistência **convertível para MPa** (força por área)?
   Se não declara, ou se não atinge **20 MPa**, rejeita.
   - ⚠️ **Não é restrito a concreto.** Qualquer material com força por área serve — bambu,
     madeira, solo estabilizado. O que conta é a grandeza, não a família do material.
   - **Classe declarada conta.** Os que só têm valor medido são classificados por classe, e
     a comparação faz-se por classe em todos.
   - **Sem limite de cubo ou cilindro** — a conversão entre corpos de prova é feita e
     justificada cientificamente na metanálise.
   - **Artigo com várias misturas:** entra se **alguma** atingir 20 MPa. As misturas abaixo
     de 20 MPa **não entram na metanálise**, mas **são registadas** para se poder documentar
     quantas saíram por não atingir o mínimo.
7. **CO₂** — o artigo declara valor de emissão? Se não, rejeita.
   - **Todas as unidades reportadas são aceites**, com uma excepção: **CO₂ por edifício**,
     que não há como normalizar.

#### O que o piloto de 12 artigos mediu (2026-08-24)

Antes de correr os 1.591, leu-se um piloto de 12 artigos escolhidos ao acaso. Resultado:
**7 aceites e 4 rejeitados na resistência, 1 em dúvida; 6 dos 12 passaram os dois
critérios.** Taxa de aprovação de 50%, e a cascata poupou a leitura do CO₂ em 4 deles.

**As tabelas sobrevivem à extracção — a hipótese contrária estava errada.** 10 dos 12
ficheiros entregaram as tabelas achatadas numa linha, mas com valores e cabeçalhos pela
ordem certa; nos melhores casos o GWP e os MPa aparecem lado a lado. Não é preciso
renderizar página para ler tabelas.

**⚠️ Mas 2 em 12 (17%) têm o valor decisivo só em figura.** O caso puro é o **RO 2024**
(linha 3752): os autores ensaiaram compressão aos 28 dias pela ASTM C39, com 5 provetes por
mistura, e **não imprimem um único valor em MPa no artigo todo** — a string «MPa» tem zero
ocorrências, e tudo está num gráfico de barras. Do lado do CO₂, o **SUMMA 2023** (2858) faz
LCA CML com 10 indicadores e só reporta percentagens de redução. Estimativa: **240 a 320
artigos** dos 1.591 vão exigir renderizar figura. Tratá-los num lote próprio com `pdf2image`,
não misturados no fluxo normal.

##### 🚨 A consequência que isto tem para o pré-filtro

É tentador contar as ocorrências de `MPa|N/mm2|C\d\d/\d\d` e rejeitar quem der zero — o
piloto chegou a propor isso, e teria despachado 3 dos 4 rejeitados sem leitura nenhuma.
**Não se pode fazer assim**, e é o próprio piloto que dá o contra-exemplo: o RO 2024 dá
**zero** ocorrências de «MPa» e tem ensaios de compressão a sério. Zero ocorrências manda o
artigo para a fila das figuras, **nunca directamente para Rejeitado**.

E o erro simétrico também está medido: no **ZAJAC 2022** (4393) a única ocorrência de «MPa»
em 131 mil caracteres é a **pressão de transporte do CO₂ supercrítico (10 MPa)**. Um filtro
«tem MPa → aceita» classificava-o mal.

📌 É a mesma lição da sonda por DOI na conferência de ficheiros, outra vez: **o regex acha
candidatos, não decide.** Serve para ordenar a fila, não para carimbar o veredito.

##### Armadilhas de extracção que o piloto apanhou

- **`grep -o` não serve neste corpus.** O texto vem com quebras de linha a meio das frases e
  o contexto do valor cai sempre na linha seguinte. Normalizar `\s+` para espaço, em Python,
  antes de procurar. Salva um turno por artigo.
- **`Mpa` com «m» minúsculo** existe (2 das 3 ocorrências no DAI 2024). Procurar sem
  distinguir maiúsculas.
- **O corte da secção de referências quase nunca funciona** — acertou em 1 de 10 ficheiros,
  porque o cabeçalho «References» raramente aparece isolado numa linha. Consequência real:
  títulos de referências com «Strength» poluem a contagem.
- **`title = '<nome exacto>'` falha em nomes acentuados** no conector do Drive
  (`GALÁN-MARÍN et al., 2015.pdf` não foi encontrado). Resolvido de raiz pelo mapa
  `nome → fileId` (ver `DRIVE_FILEID_MAP.csv`), que dispensa procurar por título.

##### O quarto estado que a especificação não previa

A cascata cria um estado que não é Aceito, Rejeitado nem DUVIDA: **«não avaliado»**, para o
CO₂ de um artigo já rejeitado na resistência. Fixá-lo por escrito antes de correr a sério —
o piloto teve de o inventar em 4 das 12 linhas.

#### ✅ DECIDIDO pela Kiê a 2026-08-24 — as duas regras que faltavam

**1. Valor só em figura: extrair da figura, não rejeitar.** A Kiê mandou verificar se era
sequer possível ler MPa de um gráfico. **É** — testado e demonstrado no caso que levantou a
questão.

- **RO 2024 (linha 3752)** — o artigo tem **zero** ocorrências de «MPa» em todo o texto e os
  resultados vivem na Fig. 1a. Renderizada a p. 3 a 200 dpi, o gráfico de barras tem eixo
  rotulado «Compressive Strength (MPa)» de 0 a 50 com marcas de 10 em 10, e lê-se sem esforço:
  **≈ 44,5 MPa** para o betão só com cimento Portland e **≈ 37,8 MPa** para o de 15% RHA.
  Ambos acima de 20 → **E2_resistencia = Aceito**. A precisão da leitura é de cerca de ±1 MPa,
  mais do que suficiente para um limiar em 20 e utilizável na metanálise com nota de incerteza.

⚠️ **Armadilha nova, apanhada neste mesmo teste — `MPa` procurado sem distinguir maiúsculas
dá falsos positivos.** Uma primeira contagem com `re.I` deu 3 ocorrências na p. 1 deste
artigo; eram todas **`compa`** de *comparison* e *compared*. Procurar **sempre com
maiúsculas respeitadas**. Isto contradiz a nota do piloto sobre o `Mpa` de «m» minúsculo no
DAI 2024: a solução não é ignorar maiúsculas, é procurar as variantes explicitamente
(`MPa|Mpa|mPa`), nunca `re.I` sobre uma sigla de três letras que é substring de palavras
comuns.

**2. CO₂: se tem o total da obra *e* um valor normalizado, aceita.** Palavras da Kiê: «se tem
os dois pode aceitar, vamos rejeitar somente se o CO₂ só vier por edifício e não tiver mais
nada além disso». A razão da exclusão era não haver como normalizar; havendo valor
normalizado, a razão cai. Ficam aceites os três casos de fronteira do piloto — ABDALLA 4664
(casa inteira mas kg CO₂/m²), WU 3212 (túnel inteiro mas kt/m de túnel) e GALÁN-MARÍN 3276
(total por modelo e kg eq-CO₂/m²).

📌 **Mas «percentagem de redução» não é valor de emissão, e a figura confirma-o.** O
**SUMMA 2023 (linha 2858)** estava em dúvida por se suspeitar que a Fig. 5 escondesse um GWP
absoluto. Renderizada: é um **gráfico radar de percentagens**, com eixo de 0% a 80%, e o
painel direito são custos em euros. O artigo faz LCA CML com dez indicadores e **não imprime
um único valor absoluto de CO₂** — «Global warming (GWP100a)» é só um vértice do radar, em
percentagem. → **E2_co2 = Rejeitado.**

🧾 **Os dois testes correram em sentidos opostos, e é isso que os valida:** renderizar a
figura salvou o RO e condenou o SUMMA. A leitura de figura não é uma via de aceitação
automática — é uma medição, e mede nos dois sentidos.

### Etapa 3 — Análise **qualitativa** do PDF

8. **Regionalização** — o antigo C6, escopo inalterado.
   ⚠️ Nota: como a Etapa 2 aceita qualquer material com força por área, os materiais
   regionais (bambu, fibras) **continuam a chegar aqui**. O C6 permanece operante.

### Etapa 4 — Controlo de qualidade ✅ REDESENHADA (2026-08-24)

**Seis itens, escala 0 / 0,5 / 1,0, máximo 6,0.** Ver a secção «O checklist de qualidade
redesenhado» mais abaixo para as rubricas de cada item.

⭐⭐ **ESTRATIFICAÇÃO POR TERÇOS.** Decisão da Kiê, 2026-08-24: o resultado principal usa
os **dois terços de cima**; o terço mais fraco **não é apagado** — fica guardado e entra na
**análise de sensibilidade**, que repete a conta com todos e reporta a diferença.

## 🚨 Porque o checklist de qualidade tem de ser refeito

O checklist antigo, na aba `ANÁLISE DE QUALIDADE` do `BANCO DE DADOS DA RSL.xlsx`:

| Item | Média nos 75 avaliados |
|---|---|
| Q1 — Unidade funcional | 0,85 |
| Q2 — Método de análise | 0,90 |
| **Q3 — Unidade de medida CO₂** | 0,81 |
| Q4 — Fonte dos dados | 0,89 |
| Q5 — Vida útil | 0,53 |
| **Q6 — fck** | 0,85 |

**O problema: Q3 e Q6 passam a ser critérios de exclusão na Etapa 2.** Tudo o que chegar à
Etapa 4 terá obrigatoriamente CO₂ declarado e `fck` — logo pontua 1,0 nos dois
automaticamente. Isso **infla todos os escores em 2 pontos** e destrói o corte: com 2 pontos
garantidos, bastariam 2 dos 4 restantes para passar o corte de 4,0.

**✅ RESOLVIDO em 2026-08-24:** removem-se o Q3 e o Q6, e entram dois itens novos que a
Etapa 2 não captura. Ver a secção seguinte.

📌 O **Q5 (vida útil)** mantém-se e passa a pesar mais (1/6 → um dos quatro herdados de
quatro itens). Isso é deliberado, não acidente: **a vida útil entra na unidade funcional
necessária para normalizar o `ci_t`**, portanto declará-la é uma propriedade de qualidade
que a análise usa directamente.

---

# ✅ O checklist de qualidade redesenhado (2026-08-24)

**Seis itens, escala 0 / 0,5 / 1,0, máximo 6,0.**

⚠️ **Identificadores por LETRA, de propósito.** Não reutilizar «Q1–Q6»: o checklist antigo
usava esses números com significados diferentes, e os 75 estudos já pontuados estão
registados com eles. Letras tornam impossível confundir os dois.

| Item | Vem de | O que mede |
|---|---|---|
| **QA — Unidade funcional** | antigo Q1 | A UF está declarada e é inequívoca |
| **QB — Método de análise** | antigo Q2 | O método de avaliação de impacto (LCIA) está nomeado |
| **QC — Fonte dos dados** | antigo Q4 | A base de inventário está nomeada |
| **QD — Vida útil** | antigo Q5 | A vida útil está declarada (entra na UF do `ci_t`) |
| **QE — Fronteira do sistema** | **novo** | O que está dentro e fora do sistema |
| **QF — Emparelhamento CO₂↔resistência** | **novo** | Os dois números do quociente pertencem à mesma mistura |

~~Q3 — Unidade de medida CO₂~~ e ~~Q6 — fck~~ **saem**: passaram a ser critérios de
exclusão na Etapa 2, e mantê-los pontuaria 1,0 automaticamente em tudo o que chegasse aqui.

## QE — Fronteira do sistema

É o item da ISO 14044 que mais afecta a **magnitude** do valor, e nenhum dos herdados o
cobre. Comparar 300 kg CO₂/m³ *cradle-to-gate* com 450 *cradle-to-grave* não é comparar
nada. Casos reais que motivaram o item: linha 4999 (fronteira em «1 t de clínquer»), 4297
(*cradle-to-gate* com 50 km de transporte incluídos), 4613 (contabiliza só a fracção
perdida).

| Pontos | Critério |
|---|---|
| **1,0** | Fronteira nomeada explicitamente (*cradle-to-gate*, A1–A3, *cradle-to-grave*…) **e** com as etapas incluídas e excluídas discriminadas |
| **0,5** | Fronteira nomeada mas sem discriminar etapas, ou deduzível do texto sem ser declarada |
| **0** | Não é possível determinar o que está dentro do sistema |

## QF — Rastreabilidade do par CO₂ ↔ resistência

**É o item que nenhum checklist genérico de ACV apanha e que esta análise precisa
absolutamente.** O `ci` é um **quociente entre dois números**. Se o artigo dá CO₂ agregado
e resistências por mistura — ou CO₂ de uma mistura e resistência de outra — o quociente
passa a ser fabricado por quem extrai, não medido por quem publicou.

Caso puro: **linha 4613**, em que o GWP tabelado é o da *fracção perdida* de resíduo, não o
do concreto aplicado. Quem não reparar calcula um `ci` que não existe em lado nenhum.

| Pontos | Critério |
|---|---|
| **1,0** | Cada valor de CO₂ está inequivocamente associado a **uma** mistura identificada, que tem o seu próprio valor de resistência |
| **0,5** | A associação existe mas exige inferência (ex.: CO₂ por mistura numa tabela, resistência noutra, ligadas só pelo nome do traço) |
| **0** | CO₂ agregado, médio, ou de recorte diferente do da resistência — o par tem de ser construído por quem extrai |

## ⭐⭐ Estratificação por terços — o terço fraco sai do resultado principal, mas fica guardado

**Decisão da Kiê, 2026-08-24.** Os estudos são ordenados pelo escore e divididos em
**terços**.

| | O que entra |
|---|---|
| **Resultado principal** | Os **dois terços de cima** |
| **Análise de sensibilidade** | **Os três terços**, para comparar |

O terço mais fraco **não é apagado**: continua pontuado, extraído e no ficheiro. Só não
entra no número que vai para o resumo e para a conclusão.

### Porquê assim, e não de outra forma

**Porque não excluir de vez.** Se o terço fraco fosse apagado, **deixaria de ser possível
fazer a análise de sensibilidade** — a análise *é* a comparação entre estratos, e apagar um
estrato apaga o termo de comparação.

**Porque não manter tudo no resultado principal.** A Kiê quer que o número principal não
venha contaminado por estudos fracos, o que é legítimo e é como as revisões sérias fazem.

**O que se ganha com o desenho híbrido:** se as duas contas derem quase o mesmo, isso mostra
que a exclusão foi rigor e não conveniência, e que o resultado **não depende** dela. Se
derem diferente, é um achado sobre a literatura — documentado em vez de escondido. Custa uma
linha numa tabela e um parágrafo no texto, e não custa dados nenhuns.

### ⚠️ Regras que têm de ser fixadas ANTES de pontuar

1. **A regra «terço de baixo fora do principal» é pré-especificada** — está aqui, escrita
   antes de existir um único escore. Os *pontos de corte* só se calculam depois de pontuar
   tudo (é a natureza dos terços), mas **a regra não muda**. É isso que a torna honesta.
2. **Empates na fronteira sobem.** Se o corte calhar num escore repetido — por exemplo, se o
   percentil 33 der 4,0 e houver seis estudos com 4,0 — **todos os empatados vão para o
   estrato de cima**. Sem esta regra, dois estudos idênticos podiam ter destinos diferentes
   só pela ordem em que aparecem na lista, o que seria arbitrário.
3. **Nunca redefinir os terços depois de ver os resultados.** Se os cortes forem ajustados
   depois de olhar para os valores de `ci`, a análise de sensibilidade perde todo o valor.

### Consequências que decorrem desta escolha

1. **O fluxograma PRISMA volta a ter uma caixa de exclusão por qualidade** — o terço de
   baixo sai do resultado principal. Mas com uma diferença face ao desenho antigo: o número
   não é «os que ficaram abaixo de 4,0», é «o terço mais fraco», e os estudos continuam
   descritos no texto.
2. **O escore por estudo tem de ir para a `meta_analysis_base.xlsx`**, numa coluna própria —
   senão não se consegue nem estratificar nem refazer a conta com todos.
3. **A análise de sensibilidade tem de ser feita por família de material também**, porque a
   estratificação por qualidade e a estratificação por material são independentes e podem
   interagir (ex.: se todos os estudos de bambu caírem no terço fraco, excluí-lo elimina uma
   família inteira). ⚠️ **Verificar isso explicitamente antes de fechar os números.**

## ✅ Tipo de corpo de prova — NÃO é item de qualidade (decidido 2026-08-24)

**1.171 das 1.694 linhas já extraídas não declaram o tipo de corpo de prova.** Como a
conversão cubo→cilindro vai ser feita e justificada, isso significa aplicá-la a corpos de
prova maioritariamente desconhecidos.

**Decisão da Kiê: não entra no checklist.** Fica como **regra de extracção obrigatória** —
registar sempre o tipo, e marcar «não declarado» **explicitamente** quando o artigo não o
disser. Nunca deixar a célula vazia, porque vazio confunde-se com «ainda não extraído».

⚠️ Quando o tipo não for declarado, a conversão cubo→cilindro **não se aplica por omissão**;
o valor entra como está, marcado como corpo de prova indeterminado, e a análise de
sensibilidade tem de conseguir isolar esse grupo.

## ✅ Estratificação da metanálise por FAMÍLIA DE MATERIAL (decidido 2026-08-24)

O critério de resistência da Etapa 2 aceita qualquer material com força por área — concreto,
bambu, madeira, solo estabilizado. São todos MPa, mas **não são a mesma grandeza física nem
o mesmo ensaio**: converter cubo→cilindro é padrão e defensável; converter bambu→concreto
não é, são materiais diferentes.

**A análise é estratificada por família de material.** O indicador `ci`
(kg CO₂eq/m³/MPa) já normaliza parte disso, mas a comparação directa entre famílias sem
estratificar não seria legítima.

## Convenções de dados

- **Não reutilizar os nomes C1–C8.** Se o antigo C3 passasse a chamar-se C2, o histórico
  `R:`/`P:` de 1.618 linhas ficaria ambíguo para sempre. Colunas novas, nomes novos; as
  antigas ficam intactas como histórico.
- **`status_triagem` é substituída** por dois campos: `etapa_saida` (1, 2, 3, 4 ou
  «incluído») e `criterio_saida`. O fluxograma PRISMA sai daí por contagem.
- **Duplicados ficam FORA das etapas.** No PRISMA a remoção de duplicados acontece antes da
  triagem — não é critério de exclusão. Os 2.622 já marcados mantêm-se fora da contagem.
- **A metanálise é refeita do zero**, conferindo linha a linha: parte dela foi extraída sobre
  PDFs que se veio a descobrir estarem trocados. Fica mais barato do que parece, porque a
  identidade ficheiro↔linha já está provada para os 1.422 PDFs conferidos.

## O que se aproveita da estrutura antiga

| Aproveita | Porquê |
|---|---|
| A conferência dos 1.422 PDFs | É sobre identidade de ficheiro, não sobre critérios |
| Os 47 DOIs, metadados e hyperlinks | Idem |
| O critério de ano | Não muda; recalcula-se dos metadados |
| As decisões dos antigos C3 e C4 | ~1.360 linhas decididas **por leitura de PDF** — evidência mais forte do que a Etapa 1 exige. Reaproveitar onde existem. |
