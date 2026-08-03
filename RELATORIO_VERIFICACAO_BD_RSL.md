---
titulo: RELATORIO VERIFICACAO BD RSL
descricao: Relatório de Verificação — BANCO DE DADOS DA RSL
tags: [academico-e-pesquisa, revisao-sistematica, UHPC]
status: concluido
ultima_atualizacao: 2026-05-15
---

# Relatório de Verificação — BANCO DE DADOS DA RSL

**Auditado:** `BANCO DE DADOS DA RSL.xlsx` (aba `ARTIGOS ACEITOS`, 173 artigos × 9 colunas) contra PDFs em `ARTIGOS ACEITOS DA RSL/`.
**Início:** 2026-05-08 · **Conclusão:** 2026-05-15

## Status

| | |
|---|---|
| Verificados | 173 / 173 ✅ |
| Com inconsistências | 22 |
| Total de problemas | 15 MAIOR · 17 MENOR · 2 CRÍTICO |

**Severidade:** OK (confere) · MENOR (ambíguo/incompleto) · MAIOR (página citada não suporta o conteúdo) · CRÍTICO (informação contradiz o PDF) · FALTANTE (sem `(p. X)`)

---

### 1. ADAMS et al., 2024 — 8 OK · 1 MAIOR

- **MAIOR — Fronteira do Sistema** (cita p. 4, 5): célula afirma inclusão de **A2 (transporte)**, mas a p. 4 declara: *"No cleaning, maintenance, labour or transport is taken into account."* **Sugestão:** trocar por *"A1 (extração) e A3 (fabricação) conforme EN 15804+A2; A2 (transporte), uso, manutenção e fim de vida explicitamente excluídos (p. 4, Fig. 1 na p. 5)."*

---

### 2. AKBULUT et al., 2024 — 9 OK

Sem inconsistências. (Conferidos: fck exato de Sun et al. na p. 10; valores 8% global e 25% redução de CO₂ na p. 1 e Tabela 6/p. 14; 40% maior vida útil na Tabela 6/p. 14; ASTM C618-15 na p. 5; nenhuma ocorrência de "ISO" em todo o PDF.)

---

### 3. AL-OBAIDY et al., 2022 — 7 OK · 2 MENOR

- **MENOR — Emissões CO2eq** (cita p. 11, 15, 18): célula informa **Híbrido = 718.437** kg CO₂, mas Tabela 5 (p. 15) registra **718.436** kg CO₂. Erro de transcrição de 1 unidade. **Sugestão:** corrigir para `718.436`. Demais valores (Timber −62.362, Concreto 654.930, Aço 865.717; pegada por m²/ano −1,3 / 13,5 / 15 / 18) conferem exatamente.
- **MENOR — Limitações do estudo** (cita p. 21): a informação sobre **"vidro AGC com diferença 10-15%"** está na **p. 20**, não na p. 21. As demais limitações estão corretamente atribuídas à p. 21. **Sugestão:** alterar a citação final de `(p. 21)` para `(p. 20-21)`.

---

### 4. ASSUNCAO, 2020 — 9 OK

Sem inconsistências. (Tese de mestrado em português, 99 pp., usa numeração impressa de páginas; mapeamento `printed page = cell page → PDF index = printed + 2` para o corpo. Conferidos: NBR 15575-1 / 50 anos na p. 54 (PDF 56); fck 52,7/48,4/47,4 MPa de Fazzan na p. 60 (PDF 62); cradle-to-gate na p. 52 (PDF 54); Tabela 5 com GWP exato 2,43E-01 / 2,09E-01 / 1,76E-01 kg CO₂eq/(m³·MPa) na p. 67 (PDF 69); UF de Damineli "1 MPa por m³" na p. 55 (PDF 57); referência completa NBR ISO 14040:2009 na p. 87 (PDF 89). Limitações na p. 58 (PDF 60) sobre Ecoinvent europeu confirmadas.)

---

### 5. BILAR, 2016 — 5 OK · 1 MAIOR · 3 MENOR

- **MAIOR — Resistência Característica (fck)** (cita p. 115, 126): a informação sobre **"blocos de concreto Classe A, resistência à compressão de 6 MPa"** está nas **p. 67** (descrição do sistema convencional, *"Os blocos de concreto são convencionais, Classe A e resistência à compressão de 6 MPa"*) e **p. 125** (receita de produção). A p. 115 trata do limite do sistema da CzP (processo primário/secundário do carvão), e a p. 126 detalha o processo industrial sem citar fck. **Sugestão:** corrigir para `(p. 67, 125)`.
- **MENOR — Metodologia Utilizada** (cita p. resumo/19, 81): (a) o termo **"CML-IA baseline"** não aparece literalmente no artigo, que cita apenas *"método CML (GUINÉE et al., 2002)"* na p. 81; "CML-IA baseline" é a nomenclatura do SimaPro para esse método, mas não é texto do artigo. (b) A p. 19 contém somente a LISTA DE ABREVIATURAS (sem conteúdo metodológico substantivo). (c) "ACV simplificada" é discutida na **p. 52** (seção 2.2.2). **Sugestão:** trocar `(p. resumo/19, 81)` por `(p. resumo/11, 52, 81)` e remover o sufixo "-IA baseline".
- **MENOR — Emissões CO2eq** (cita Tabelas 47-48, p. 150-151): ambas as Tabelas 47 e 48 estão na **p. 150** (não p. 150-151). A p. 151 contém Figura 29 sobre acidificação (não GWP). Os valores numéricos (5,84E+01 e 5,77E+01 kg CO₂eq/m²) conferem exatamente. **Sugestão:** ajustar para `(Tabelas 47-48, p. 150; conclusão p. 164)`.
- **MENOR — Limitações do estudo** (cita p. 163-165, 81, 164, 80, 164): (a) a discussão sobre **alocação econômica flutuante e necessidade de análise de sensibilidade** está na **p. 80** (não p. 81). (b) A p. 165 é a primeira página da lista de referências, não traz limitações. **Sugestão:** consolidar para `(p. 80, 163-164)`.

---

### 6. BRESSI et al., 2022 — 9 OK

Sem inconsistências. (Tabela 3/p. 7 confere fc28 ~497-582 psi (3,43-4,01 N/mm²) — célula diz "~497-585", muito próximo do real 581,53; UF "1 km × 22 m × 20 anos" e PAP confirmados na p. 9; cradle-to-gate na p. 1 e 9; ISO 14040/14044 na p. 9; 125 με na p. 9; método CML v.4.4 e Monte Carlo na p. 1, 5, 12; renderização visual de Fig. 7b/p. 16 confirma faixa MIP ~30k a ~280k kg CO₂eq/km; renderização de Fig. 8b/p. 20 confirma faixa CPM ~2,2M a ~2,6M kg CO₂eq/km; limitações sobre módulo elástico do CTB+RAP e suposição determinística confirmadas na p. 19.)

---

### 7. DERVISHAJ et al., 2024 — 9 OK

Sem inconsistências. (C25/30, GFA=1862 m², edifício de 1967 do Million Program (Programa do Milhão sueco) confirmados na p. 7; 57 anos 1ª vida (2024-1967) na p. 11; 50 anos 2ª vida (2027-2077) na p. 14-15; A1-A5 + B1, C3, D + B2-B5 excluídos por EN 16757 na p. 4; 19,2 kg CO₂/m³ EN 16757 e 5,4 kg CO₂/m³ contextual na p. 1, 14; 7,58 kg CO₂/m² GFA confirmado nas p. 16 e 19; 207,3 kg CO₂e/m² novo (= 164,7 A1-A3 + 42,6 A4-A5) e 207,4 economia/total na Tabela p. 16; 43,5 kg CO₂/m² MaxCarb na p. 14, 16; ISO 14040/14044 NÃO citadas em todo o PDF (célula correta ao informar "Não").)

---

### 8. DU et al., 2024 — 9 OK

Sem inconsistências. (Cradle-to-gate na p. 6; SimaPro/Ecoinvent/IPCC/CED na p. 6-7; UF "1 m³" na p. 6; fc NACM 38,72 MPa, LT0S0 17,97 MPa, melhor LT5S0 21,10 MPa confirmados na p. 11; GWP NACM ~1200 kg CO₂eq, LWCM 550-690 kg CO₂eq, redução 53,68% na p. 12; Sustainability Index 48,2 kg CO₂eq/MPa para LT15S6 confirmado na p. 16; ISO 14040 NÃO encontrada em busca completa do PDF (correto); limitações sobre cradle-to-gate e LCA full-scale na p. 20.)

---

### 9. DYNAN et al., 2023 — 9 OK

Sem inconsistências. (Misturas M0-M4 com 0-40% RGA confirmadas na Tabela p. 9; ISO 14040:2006 na p. 3 e 20; cradle-to-gate na p. 3 e 8; SimaPro + ReCiPe 2016 na p. 5; "Australian indicator set, the Traci method, the ReCiPe method and CML 2 baseline method" na p. 10; UF "1 m³" e "AUD/MPa" na p. 3 e 8; 40 MPa requisito estrutural na p. 8; Tabela 4/p. 10 confere GWP M0 = 394,00 e M1 = 393,76 kg CO₂eq/m³; Curtin University citada nas limitações p. 17. Pequena observação: célula escreve "TRACI" enquanto artigo grafa "Traci" — mesmo método, sem implicação.)

---

### 10. EK et al., 2020 — 9 OK

Sem inconsistências. (Bridge 6-1282-1 / Road 26 / Suécia / 6 m × 9 m, RSL 80 anos, módulos A1-A5 + B1-B8 + C1-C4 + D, A0 excluído — todos confirmados na Tabela 1/p. 3; concretos C35/45 (CSF) e C20/25 (elementos pré-moldados) confirmados nas pp. 23, 25-26, 27, 31; ISO 14040 NÃO citada em todo o PDF (correto); Tabela 4/p. 6 confere GWP-total da CSF: A1-A3=313, A4-A5=172, B1-B5=12, C1-C4=47, D=−70 kg CO₂eq/FU; Tabela 7/p. 11 confere SSC: A1-A3=369, A4-A5=164, B1-B5=9,1, C1-C4=42, D=−309 — todos exatos; GaBi v9.5 + EN 15804+A2 + EN 15686-5 + ISO 14008 + EPS 2015dx + PEF confirmados na p. 3-4.)

---

### 11. FERREIRA et al., 2023 — 9 OK

Sem inconsistências. (Loulé/Algarve confirmado nas p. 4-5; cradle-to-gate na p. 1, 3, 9; SimaPro v9, IPCC 2013 GWP 100a, Level(s) framework confirmados nas p. 6-9; UF 1 kg, área de vendas 9.556 m² confirmada na p. 9 e adiante; C30/37 e C12/15 (fck) na p. 19-20; 50 anos vida útil na p. 7; Tabela na p. 9-13: total 16.140.162,98 kg CO₂eq, ECI 1689 kg CO₂eq/m², EUI 4248 kWh/m², CUI 21 kg CO₂eq/m²/ano — todos exatos; percentuais argamassa 51% / aço 30% / betão 17% literais nas p. 11 e 12; ISO 14040/14044 NÃO encontradas no PDF (correto).)

---

### 12. GANAPATHI CHOTTEMADA et al., 2023 — 9 OK

Sem inconsistências. (Mistura ótima FS50-SF0.3 com 44,18 MPa confirmada na p. 4; faixa 35-55 MPa na p. 1, 5; UF "1 m³" e cradle-to-gate na p. 7-8 (note: o resumo do próprio artigo escreve "cradle-to-grave" mas a metodologia detalha cradle-to-gate, e a célula segue a metodologia — escolha defensável); openLCA + Ecoinvent + ReCiPe + USEtox + CML confirmados nas p. 8, 16; Tabela 5/p. 10 confere GWP/kg: PC=0,88534 (~0,885), GGBS=0,10088 (~0,101), Sodium silicate=0,82784 (~0,828), NaOH=1,315 — todos exatos; 86% maior impacto PC vs AAC e 132% custo AAC confirmados nas p. 1, 18; ISO 14040 e 14044 nas referências p. 20-21.)

---

### 13. GOMES, 2023 — 6 OK · 1 MAIOR · 2 MENOR

(Tese, 67 pp., usa numeração impressa: PDF index = printed page + 1.)

- **MAIOR — Resistência Característica (cita p. 32):** O consumo de cimento "**400 kg/m³ convencional, 600 kg/m³ baixo carbono com 52% de filer**" está nas **p. 28-29** (PDF 29-30), não na p. 32. A página 32 (PDF 33) trata do levantamento geral do inventário de materiais sem citar esses valores específicos. **Sugestão:** corrigir para `(p. 28-29)`.
- **MENOR — Emissões CO2eq (cita p. 39-47, 52-53):** O **"fator eletricidade brasileira: 0,29 kgCO₂/kWh"** está na **p. 20** (PDF 21), não nas pp. 39-47 ou 52-53. Os demais valores (23,1 / 37,9 / 29,3 tCO₂e) estão corretamente nas pp. 39, 42, 46 (PDF 40, 43, 47). **Sugestão:** ampliar para `(p. 20, 39-47, 52-53)`.
- **MENOR — Limitações (cita p. 15-16, 30-31, 48-53):** A "incerteza de **18% na condutividade térmica do solo**" está na **p. 18** (PDF 19), fora das faixas citadas. **Sugestão:** incluir `p. 18` na citação.

---

### 14. HAJIESMAEILI et al., 2019 — 9 OK

Sem inconsistências. (Ponte Guillermaux, vão 34 m, 1920, Payerne na p. 4; ISO 14040 na p. 4 e refs p. 12; SimaPro/Ecoinvent/KBOB/IPCC 2013/CED/UBP confirmados na p. 8; PE-UHPFRC 120 MPa na Tabela 2/p. 3; UHPFRC 150-200 MPa na p. 2; C30/37 e C20/25 do P-RC na Tabela 5/p. 7; vida útil 100 anos para todos métodos na p. 4-5; Dyneema SK99 nas p. 3, 10-11; reduções 55%/29%/70%/40% confirmadas nas p. 1, 9, 10; cradle-to-grave (com exceções) na p. 5-6, 8.)

---

### 15. HAVERKAMP et al., 2025 — 9 OK

Sem inconsistências. (Painel CRC 4000×3600×40 mm, C50/60, fibras de carbono PAN, Alemanha confirmados nas p. 4, 6, 12; ISO 14040/14044 + PEF + EN 15804 + CFF + GaBi + EF 3.0 nas p. 1-6; vida útil 100 anos vs 60 anos típico nas p. 2, 6; UF (1 painel) com fluxos 1370 kg concreto + 8,5 kg fibra carbono + 9,5 kg aço, tração ≥ 2800 N/mm² e E ≥ 230.000 N/mm² confirmados nas p. 4, 6; Tabela 9/p. 9 confere Climate Change total = 4,56E+02 (456), fóssil = 4,55E+02 (455), biogênico = 6,33E−01 (0,63), uso do solo = 1,68E−01 (0,17) — todos exatos; 42% fibras de carbono e 34% concreto confirmados na p. 10.)

---

### 16. KASTIUKAS et al., 2019 — 9 OK

Sem inconsistências. (3 razões molares MOC + 2 processos de produção MgO confirmados nas p. 1-4; ISO 14040/14044 nas refs p. 20; Eco-indicator 99, IPCC 2007, Ecoinvent na p. 5-6; SimaPro na ref p. 21; Tabela 6/p. 11 confere fck: MOC-3 = 71,8 MPa, MOC-5 = 93 MPa, MOC-9 = 111 MPa; sequestro CO₂eq na p. 10 = 224,0 / 334,9 / 353,4 g/kg (célula arredonda 334,9→335 — OK); Tabela 3/p. 7 confere PC = 832,61 kg CO₂/t (célula 833 — OK arredondamento) e MgO = 1096,54 kg CO₂/t (célula 1096 — OK); GWP concreto MOC seco 0,308 / úmido 0,285 / PC 0,228 kg CO₂eq/kg confere exatamente na p. 15.)

---

### 17. KOUVARA et al., 2023 — 9 OK

Sem inconsistências. (Sistema Polycare/Polyblock + concreto polimérico 88% filler / 12% resina / 38% PET reciclado nas p. 1, 8; vida útil 50 anos vs 25 anos do CEM e 80+ anos para Polyblock confirmados nas p. 6-9; fck 90-130 MPa material e 4,5-5,0 MPa parede nas p. 8-9; GaBi TS v8.7 + Ecoinvent + ReCiPe 2016 v1.1 + DIN EN ISO 14040/14044 nas p. 5-7; cradle-to-gate (1 kg, 1 m²) e cradle-to-grave (50 anos) na p. 6; UF 1 kg / 1 m² parede 0,20 m / edifício 50 anos confirmadas nas p. 6, 10-11; reduções 60%/80%/90% confirmadas nas p. 10-12 (Figuras 5-6); limitações ACV simplificada nas p. 6-7, 15.)

---

### 18. KUL et al., 2023 — 9 OK

Sem inconsistências. (Argamassas geopoliméricas com RCD (HB/RCB/RT) + RCA + NaOH 10/15/19 M, comparadas a PCF Portland, contexto Turquia confirmado nas p. 1, 4, 6; cradle-to-gate na p. 1, 4, 12; ISO 14040/14044 na p. 10; SimaPro 9.0 + Ecoinvent 3.0 + TRACI 2.1 nas p. 12-14; UF "1 m³" na p. 12; faixa 23,1-66,2 MPa geopolímero e 47,4 MPa PCF confirmadas nas p. 1, 6, 11; média acima 55 MPa para misturas 15M+105°C na p. 1; Tabela 10/p. 15 confere GWP: PCF=501,1; geopolímeros 178,7/179,6/178,3/171,0 kg CO₂eq/m³ — todos exatos; 65,9% redução CO₂eq e 62,9% por MPa nas p. 14, 19; redução ~60% no abstract p. 1.)

---

### 19. LI et al., 2024 — 9 OK

Sem inconsistências. (AAM + água do mar vs OPC, cradle-to-gate nas p. 1, 4; fck 51,1 MPa (28d) na p. 10 e 25,2 MPa (3d) na p. 1, 6; flexão 7,5 MPa (28d) e 5,3 MPa (3d) confirmadas nas p. 5, 6, 9, 10; UF "1 m³" na p. 4-5; Ecoinvent na p. 5; Figura 4/p. 8 confere GWP: AAM = 258,9 kg CO₂eq/m³ e OPC = 469,3 kg CO₂eq/m³, redução 44,8% — todos exatos; contribuições NaOH 52,2% + GGBS 25,6% + FA 8,0% confirmadas nas p. 7-8; ISO 14040 NÃO encontrada no PDF (correto — célula declara "não citadas explicitamente").)

---

### 20. LI et al., 2025 — 9 OK

Sem inconsistências. (OPG = FA + GGBFS + Na₂SiO₃ sólido confirmado na p. 1; UCS W50S20 = 5,937 MPa e W50S10 = 0,95 MPa confirmados nas p. 7, 20; cradle-to-gate + ISO 14044:2006 (ref [45]) na p. 20; Tabela 5/p. 20-21 confere CO₂ por t de solo: W50S10=23,44 / W50S20=46,88 / W50S30=70,32 / W50S40=93,76 kg/t — todos exatos; OPC=285 kg CO₂/t e redução 83% (= 100−17%) com W50S20 confirmados nas p. 20-21; UF "ligante para estabilizar 1 t de argila mole" na p. 20.)

---

### 21. MALABI EBERHARDT et al., 2024 — 8 OK · 1 MENOR

- **MENOR — Usou Norma ISO14040?** (cita p. 5): A célula declara *"ISO 14040/14044 não citadas explicitamente"*. **Porém, ISO 14040 (2006) é explicitamente citada na p. 3** (texto: *"It is defined in a broad suite of international and regional standards, such as ISO 14040 (2006), ISO 14067 (2018) and EN 15978 (2011)"*) e na lista de referências (p. 16). ISO 14044 de fato não é citada. O restante da célula está correto: ISO Technical Committee 59/SC17 e CEN/TC 350 confirmados na p. 5 (artigo escreve por extenso "ISO Technical Committee 59 and its Subcommittee 17... and CEN Technical Committee 350"). **Sugestão:** alterar para *"Parcialmente — ISO 14040:2006 citada como referência de método na p. 3, mas a metodologia segue EN 15978:2011 e EN 15804:2019; ISO 14044 não citada"*. Demais células OK: Tabela 3/p. 10 confere Footprint=13,50 (base, faixa 12,88-14,84) e Handprint=−7,06 (base, faixa −5,74 a −11,23); bio-based products=−4,305 (~−4,31) kg CO₂e/m²/ano; 8 andares, 5.570 m² Finlândia na p. 5; OneClickLCA + CO2data.fi nas p. 5-6.

---

### 22. MENEGATTI et al., 2022 — 9 OK

Sem inconsistências. (Viga DRB com 100% RCA + ORB referência, seção 140×600 mm, fck C60 confirmados na Tabela 1/p. 4-5; ISO 14040/14044 nas p. 5 e 24; EN 15804 + EF 3.0 nas p. 2, 5-6; Ecoinvent v3.7.1 e três cenários de alocação 100-0/50:50/0-100 confirmados nas p. 5-6; UF "1 m de viga" nas p. 4-5; Tabela A2/p. 18 confere GWP ORB = 54,496 (~54,5) kg CO₂eq/m e DRB 63,6 (p. 9) com 17% maior; cenários reutilização 39% e 104% confirmados na p. 15; cradle-to-gate na p. 1; vida útil 50/5 anos nas p. 5, 7.)

---

### 23. MILANI et al., 2020 — 9 OK

Sem inconsistências. (Superestruturas de 27 tipologias × 15 vãos (6-20 m) = 405 estruturas confirmadas nas p. 1, 6; fck 35 MPa e Grout 30 MPa na Tabela 1/p. 8; ISO 14040/14044 + ILCD + ReCiPe + Ecoinvent + SimaPro + comparativos IMPACT 2002+/BEES nas p. 2, 5; cradle to grave na p. 1, 2; UF "1 m²" na p. 14; danos a ecossistemas 1,49-1,79×10⁻⁵ e 3,52-3,67×10⁻⁶ species.yr/m² confirmados na p. 10; LCC €490,60-€866,50/m² na p. 14; ISO 14040 também nas refs p. 21.)

---

### 24. MOHAJERANI et al., 2019 — 9 OK

Sem inconsistências. (Tijolos de argila queimada com biossólidos ETP/WTP, Melbourne, Austrália confirmados nas p. 1-2; fck 35,5 MPa (10% biossólidos) e 12,04 MPa (25% biossólidos) na p. 1, 10, 17; SimaPro v8 + cradle-to-gate nas p. 15-16; economia de energia de queima 12,4% a 48,6% confirmada nas p. 1, 14-18; ISO 14040 NÃO encontrada no PDF (correto — célula declara "não citadas explicitamente"); ACV referenciada a Mohajerani et al. 2018 [10].)

---

### 25. NASSAR et al., 2025 — 9 OK

Sem inconsistências. (UHPC com URCF/CRCF confirmado em todo PDF; fck UHPC ref. = 124,1 MPa, M6-CRCF-5 = 123,4 MPa, M5-URCF-25 = 98,2 MPa na p. 12; ISO 14040 explicitamente citada na p. 10 (*"an LCA approach, following ISO 14040 guidelines"*) e refs p. 21, 25; cradle-to-grave com seis estágios (extração, processamento, transporte, carbonatação, uso, fim de vida) confirmados na p. 10; UF "1 m³" na p. 1; GWP ref. = 410, M5-URCF-25 = 362 (−11,7%), M10-CRCF-25 = 377 (−8,0%) kg CO₂eq/m³ confirmados nas p. 21-22.)

---

### 26. PAPADAKI et al., 2022 — 9 OK

Sem inconsistências. (Apartamento de 108,3 m² em Atenas confirmado na p. 3; vida útil 25 anos + cradle-to-grave + ISO 14040/14044 + SimaPro + ReCiPe (H) na p. 4; cradle-to-grave também na p. 6; Tabela/p. 11 confere Total Impacts 100/78/57/35 (Convencional/Aterro → Circular/Reciclagem, redução total 65%); 667 anos para recuperar metais confirmado nas p. 1, 13-15.)

---

### 27. PEDROSO et al., 2024 — 9 OK

Sem inconsistências. (C25/30 da viga de referência confirmado nas p. 3, 4; CFRP/jacketing/CJE/CJI/ASP/ACF nas p. 1-12; cradle-to-gate + A5 + ISO 14040/14044 + EN 15643/15804 + SimaPro 9.4 + Ecoinvent v3.6 + CML-IA baseline nas p. 6-7; vão 3,6 m e aumento ~40% na resistência confirmados nas p. 3, 4, 6; Tabela 6/p. 13 confere GWP exato: CJE = 2,14E+01 (21,4), CJI = 4,26E+01 (42,6), ASP = 1,84E+01 (18,4), ACF = 1,71E+01 (17,1) kg CO₂eq; custo ACF = 124,22 EUR.)

---

### 28. PESTA et al., 2020 — 9 OK

Sem inconsistências. (Blocos reutilizáveis com agregado reciclado + RMAC/RCAC/NAC confirmados nas p. 2-5; fck C25/30 alvo e medidas 33,3/35,4/31,2 MPa na p. 4; ISO 14040 + EN 16757 + GaBi 9 + CML 2001 + ReCiPe 2016 nas p. 6-8; cradle-to-grave na p. 2, 6, 11; 50 e 100 anos confirmados nas p. 6-11; UF "1 m²" na p. 1, 6; GWP cenário 1: Plan1-RMAC=106 / Plan2-RCAC=48,5 / Plan3-NAC=108 / Plan4-conv=113; cenário 2: Plan2s2=53 / Plan4s2=226 kg CO₂eq/m² confirmados nas p. 9, 11.)

---

### 29. RINNE et al., 2022 — 9 OK

Sem inconsistências. (Edifício híbrido de 5 andares + concreto + madeira em Finlândia confirmado nas p. 1, 5-8; EN 15978 + One Click LCA + A1-A5/B1-B6/C1-C4/D nas p. 1, 9-10; 50 anos vida útil nas p. 1, 4, 9; densidades 2400 (concreto) e 2500 (concreto armado) kg/m³ nas p. 11-12; cradle-to-grave na p. 2, 9; Tabela/p. 12 confere pegada total: Híbrido = 1.300.573, Concreto = 1.293.345, Madeira = 1.215.038 kg CO₂-e; C1-C4 emissões 35.061 (concreto) e 44.627 (madeira) confirmadas nas p. 1, 12; ISO 14040 NÃO encontrada no PDF (correto — célula declara "Não diretamente").)

---

### 30. ROSA et al., 2017 — 9 OK

Sem inconsistências. (Cimentos P-35 / LC3-35 / LC3-50, fábrica Siguaney (Cuba) confirmados nas p. 1-2, 4-8; ISO 14040 e ISO 14045 explicitamente citadas nas p. 3-4; SimaPro 8.1 + método Recipe na p. 2; UF "1 tonelada de cimento" na p. 6; cuna a la puerta na p. 5; emissões 0,63 / 0,46 / 0,36 t CO₂/t na p. 5 — todos exatos; CIDEM e arcillas calcinadas confirmados nas p. 1-2.)

---

### 31. ROSSI, 2013 — 8 OK · 1 MENOR

(Tese de 150 pp., usa numeração impressa de páginas com pré-textuais: para o corpo, PDF index = printed page + 19. RESUMO está no PDF p. 14.)

- **MENOR — Emissões CO2eq (cita p. 14):** A célula declara *"Aquecimento Global: 8,88E-01 kg CO₂-eq/m² (p. 14)"*. **Porém, o RESUMO na PDF p. 14 não traz este número**. O valor 8,88E-01 corresponde ao **Total da Figura 29** (caracterização para aquecimento global, valor aproximado lido visualmente em ~8,8-9,0E-01 kg CO₂-eq/m² edificação) na **PDF p. 104 (printed p. 85)**. A citação está consistente com o que a figura mostra, mas a página de referência está incorreta. **Sugestão:** alterar para `(p. 85, Figura 29)` ou `(PDF p. 104, Figura 29)`.

Demais células OK: cradle to grave na PDF p. 38, 55, 90 (printed pp. 19, 36, 71); fck 25 MPa do edifício R8-B na PDF p. 78 (printed p. 59); 75 anos NBR 15575-1 na PDF p. 89 (printed p. 70); ISO 14040/14044 (ABNT NBR) citadas em RESUMO e ao longo do texto; método EDIP 1997 confirmado.

---

### 32. SANGIORGIO et al., 2025 — 9 OK

Sem inconsistências. (Fôrmas impressas em 3D com PLA/ABS/PVA/geopolímeros/argila confirmados nas p. 1-9; ISO 14040 na p. 6; SimaPro + Ecoinvent + cradle-to-gate + Grasshopper/Rhino confirmados nas p. 4, 6-9; UF "área 7854 cm² × 100 cm" na p. 6; GWP do concreto moldado 474,76 kg CO₂eq e materiais viscosos 0,3 kg CO₂eq vs plásticos 7 kg CO₂eq confirmados na p. 9.)

---

### 33. SANTOS, 2015 — 9 OK

Sem inconsistências. (Tese, 208 pp., offset PDF idx = printed + 1. Cinzas pesadas como matéria-prima alternativa confirmadas em todo o texto; ISO 14040/14044 e ISO 14045:2014 nas p. 8-9, 100; SimaPro + Ecoinvent + ReCiPe midpoint H + endpoint H confirmados nas p. 8, 100, 128; UF "1.000 kg de cinzas pesadas" na p. 14; berço ao portão na p. 102, 105; GWP 1,82 kg CO₂eq confirmado na p. 85, 130; eco-eficiência 0,97% (cerâmica) e 2,4%-11,5% (clínquer) confirmadas nas p. 8, 163-164.)

---

### 34. SANTOS, 2022 — 4 OK · 4 MAIOR

(Tese, 110 pp. Cell descreve apenas a parte de ensaios mecânicos de durabilidade da tese, mas o trabalho **também é um estudo de ACV** com ReCiPe 2016 + EN 15804 — confirmado no resumo e nas p. 6, 11, 30, 100. Múltiplas células classificam aspectos LCA como "N/A" quando o trabalho efetivamente os contém.)

- **MAIOR — Metodologia** (cita p. 20-23): A célula declara *"não é estudo de ACV"*. Porém, ACV/LCA é explicitamente citada em todo o texto (p. 5, 6, 11, 14, 30, 100). Resumo: *"Para além do desempenho técnico, o objetivo deste estudo foi avaliar o desempenho ambiental de materiais compósitos... Usando os métodos ReCiPe 2016 Midpoint/Endpoint e EN 15804"*. **Sugestão:** reescrever incluindo a ACV: *"ACV com ReCiPe 2016 Midpoint/Endpoint e EN 15804; SimaPro; Ecoinvent; cradle-to-grave; complementada por ensaios mecânicos de durabilidade"*.
- **MAIOR — Fronteira do Sistema:** A célula declara *"N/A — sem fronteira de sistema LCA definida"*. Porém, "berço" aparece nas p. 36, 67, 75 e o trabalho define explicitamente uma fronteira de ACV. **Sugestão:** investigar e descrever a fronteira (cradle-to-gate ou cradle-to-grave) declarada no estudo.
- **MAIOR — Usou Norma ISO14040?** (cita p. 15-28): A célula declara *"Não — não envolve ACV nem normas ISO 14040/14044"*. Porém, **ISO 14040 é explicitamente citada nas p. 61, 69, 100, 103, 110**. **Sugestão:** alterar para "Sim".
- **MAIOR — Emissões CO2eq com unidade:** A célula reporta apenas resistência à flexão (15 MPa e 11 MPa), **não valores de CO₂eq**. Como o trabalho usa ReCiPe + EN 15804, deve haver valores quantitativos de GWP. **Sugestão:** buscar e reportar os valores de GWP/CO₂eq obtidos pela ACV no estudo.

Demais células OK: Material (sisal/juta/malva), Durabilidade (10 ciclos, 15→11 MPa redução 26,7%) e fck (N/A) e Limitações estão internamente consistentes.

---

### 35. SHANBHAG et al., 2024 — 9 OK

Sem inconsistências. (Hempcrete, cradle-to-gate, ACV híbrida (IOH) + Monte Carlo 10.000 iterações + ISO 14040/14044 confirmados nas p. 1, 2, 4-7; SimaPro US-EI 2.2 e IOH na p. 5-7; UF "1 pé cúbico (ft³)" na p. 1, 3-4; resistência compressão 0,03-1,22 MPa nas p. 2, 7; GWP cânhamo industrial −1,72 kg CO₂e/kg no abstract; 20% mínimo de cânhamo para carbono negativo nas p. 1, 8-10; Walker et al. 2014 referenciado.)

---

### 36. SIKORA et al., 2023 — 8 OK · 1 MAIOR

- **MAIOR — Usou Norma ISO14040?** (cita p. 9): A célula declara *"Não explicitamente citada ISO 14040/14044"*. **Porém, ISO 14040 (2006) e ISO 14044 (2006) são explicitamente citadas na p. 8**: *"the life-cycle assessment method in accordance with ISO 14040 (2006) and ISO 14044 (2006)"*. Também nas refs/p. 18. **Sugestão:** alterar para *"Sim — ISO 14040:2006 e ISO 14044:2006 explicitamente declaradas como base metodológica (p. 8); também ISO 14025 e EN 15804:2012+A2 (p. 9)"*.

Demais células OK: QTW0 e misturas com seawater/dune sand/glass/nanosilica nas p. 1-13; módulo A1 + openLCA + Ecoinvent + ÖKOBAUDAT + IPCC GWP 100a + AWARE na p. 9; resistência compressão >17-20 MPa aos 28 dias (EN 12390-3) nas p. 7-8; UF "1 m² parede" com U=0,3 W/m²K na p. 9; redução 30% pegada hídrica e 2-30% GWP confirmadas nas p. 12-17.

---

### 37. SILVA et al., 2023 — 9 OK

Sem inconsistências. (Artigo de revisão bibliográfica de ICBP com coco/RCD vs pavimento asfáltico; busca Scopus 1125 documentos 1972-2022 confirmada na p. 3; ISO 14040/14044 citadas como normas de estudos revisados nas p. 19, 20, 30 (Oliver-Solà, Luo, Abdeljaber); fc com 80% RCA na p. 9; otimização +156% fc nas p. 6, 23; ICBP 33-44% mais barato em manutenção e AP 35% em construção (NOx 32% menor) nas p. 1, 12, 21; UF "1 m²" nas p. 14-15, 19-20.)

---

### 38. SOLTANZADEH et al., 2022 — 9 OK

Sem inconsistências. (RSF/ISF/FRSCC com 0/50/67/100% substituição confirmados nas p. 1-6; ISO 14040/14044 + GaBi 6 + CML 2001 midpoint + cradle-to-gate nas p. 12-15; UF "1 m³" na p. 13; fck Tabela 2/p. 5-6: R0-I90=58,10 / R45-I45=55,54 / R60-I30=55,12 / R90-I0=52,03 MPa (todos >classe C50 alvo) — todos exatos; Tabela 7/p. 16 confere GWP: R0-I90=518 / R45-I45=491 / R60-I30=482 / R90-I0=466 kg CO₂eq/m³; +37% EM e −26% absorção de energia confirmadas nas p. 1, 19-20.)

---

### 39. SOMBRIO, 2015 — 9 OK

Sem inconsistências. (Tese, 138 pp., printed page = PDF idx para o corpo. Sistema Casa Express + ILCD + ISO 14040/14044 confirmados nas p. 1-8, 14, 46; GaBi 6.0 + SimaPro 8.0 + CML-IA + EN 15804 + cradle-to-gate nas p. 71-87; UF "1,312 m²" na p. 65, 69; fck C20 (dado alemão GaBi) na p. 79, 116; Tabela 15/p. 88 confere GWP total = 31,9 kg CO₂eq + concreto = 22,5 (70,09%) + bloco cerâmico = 6,26 (19,62%) + vergalhão = 2,81 (8,81%) — todos exatos.)

---

### 40. VALENCIA-BARBA et al., 2020 — 9 OK

Sem inconsistências. (4 sistemas de lajes + Barcelona + EHE-08 + 50 anos confirmados nas p. 1, 6, 24; LCA Manager + Ecoinvent 3.1 + BEDEC + CYPE + Eco-indicator 99 + CML 2001 + ISO 14044 + cradle-to-handover (A1-A5) nas p. 1-6, 21; UF "1 m²" na p. 7; Tabela 8/p. 15 confere GWP CML 2001 cenário A: I-A=9,66×10¹ (96,6) / II-A=1,29×10² (129) / III-A=1,08×10² (~108-109) / IV-A=138,81 — todos exatos; IV-B=196,96 / III-B=193,77 também no corpo p. 15; ISO 14040 NÃO encontrada (correto — célula declara "Parcialmente, ISO 14040 não citada diretamente").)

---

### 41. VILLALBA et al., 2025 — 9 OK

Sem inconsistências. (5 alternativas CJ/SCJ/CFRP/STE/STA + Quito + 50 anos vida útil confirmados nas p. 1, 10-14, 28; OpenLCA + Ecoinvent + SOCA + PSILCA + ReCiPe Endpoint H + MCDM (BWM/EDAS/MABAC/CODAS/MARCOS) nas p. 14-16; cradle-to-grave + LCCA + S-LCA nas p. 1, 10, 14; f'c viga = 24 MPa na p. 13; reduções 19% / 59% / 62% / 77% confirmadas nas p. 17-18; ISO 14040 NÃO encontrada no PDF (correto — célula declara "não citada explicitamente").)

---

### 42. ZUCARATO, 2020 — 9 OK

Sem inconsistências. (Tese, 115 pp., printed page = PDF idx. ACVc + Roadmap BR + cimento 2050 confirmados nas p. 1-16; ISO 14040 explicitamente citada na p. 16, 41, 44, 48 e refs p. 104; SimaPro 8.5 + Ecoinvent v3.4 + GEMPACK + CML-IA baseline confirmados nas p. 17, 23, 65, 72, 85; UF "1 t de cimento" na p. 1, 67; GWP 162,24 kg CO₂eq/t (2050) vs 564 kg CO₂eq/t (2014), redução 71,2% e balanço 941 Gg CO₂eq confirmados nas p. 96, 102.)

---

### 43. HAFNER et al., 2020 — 9 OK

Sem inconsistências. (Prinz-Eugen-Park, Munique, 566 apartamentos confirmados nas p. 1, 3, 6, 11; LEGEP + oekobaudat + EN 15978 + EN 15804 + EN ISO 14040 + EN 16485 confirmados nas p. 5, 7, 12; vida útil 50 anos nas p. 1, 7, 8, 11; UF "1 m² GFA" nas p. 6-7; WA13/WA14/WA15 confirmados na p. 9; carbono biogênico total bairro = 12.532.130 kg CO₂eq (p. 7-8, 11); por edifício de -1,39 (WA13) a -5,79 (WA14 East) kg CO₂eq/m² GFA na p. 8-9; GWP total ciclo de vida WA13 = 12.293.318 e WA15 East = 2.723.041 kg CO₂eq confirmados na p. 9.)

---

### 44. HEMMATI et al., 2024 — 9 OK

Sem inconsistências. (Adohi Hall (Univ. Arkansas), 200.000 ft², 708 estudantes, CLT/glulam Binderholz, Geopier, Nabholz Construction confirmados nas p. 1, 4-5; SimaPro v9.5 + USLCI + Ecoinvent + TRACI 2.0 + ISO 14040/14044 + EN 15978 nas p. 3-4, 7-8; UF "1 m² GFA durante construção" na p. 4; A4-A5 only (gate-to-construction-completion) na p. 4-5; GWP total = 3.211 t CO₂eq, 173 kg CO₂eq/m² (Cen.1) e 33 kg/m² (Cen.2) confirmados nas p. 8-13; equipamentos = 2.460 t (70%), transporte = 751 t (30%) na p. 9; Terraplanagem 41% / CLT 31% / Concreto 26% na p. 9.)

---

### 45. HERTWICH et al., 2019 — 9 OK

Sem inconsistências. (Revisão sistemática sobre eficiência material em edifícios/veículos/eletrônicos; EXIOBASE + IEA + MFA + IAM + ETP-TIMES nas p. 4, 15-19; produção global 2015 = 11,4 Gt CO₂eq/ano + cimento 2,9 + aço 2,8 + materiais 56% / 3,3 Gt da pegada da construção confirmados nas p. 3-5; vida útil edifícios EUA 50-60 / Europa >100 / Japão 30-40 / China 25 anos na p. 6; cradle-to-gate nas p. 4, 11; ISO 14040 NÃO citada no PDF (correto — célula declara "Não").)

---

### 46. INGRAO et al., 2018 — 9 OK

Sem inconsistências. (Revisão metodológica de ACV em edifícios; ISO 14040/14044 + EN 15978 + EN 15804 + CEN/TR 17005 + CML 2 Baseline + ReCiPe + Ecoinvent confirmados nas p. 11, 15, 19, 25, 28, 30-32; cradle-to-grave na p. 11; 100 anos na p. 21; BEESs nas p. 13-14; 52% impactos operacionais na p. 18; revisão sem UF única / sem estudo de caso primário discutido nas p. 9, 16-25.)

---

### 47. INMAN et al., 2017 — 9 OK

Sem inconsistências. (BFRP vs B500 NC + viga 200×200 mm confirmados nas p. 1, 3; SimaPro Analyst 8 + Ecoinvent 3.1 + ISO 14040:2006 + EN 15804:2012 + ReCiPe Midpoint H + cradle-to-gate (A1-A3) nas p. 4; fck Tabela 2/p. 3, 5: BFRP=57,1-67,4 MPa e aço=31,4 MPa; Tabela 3/p. 6 confere GWP: viga aço=23,7 / BFRP 1200=14,6 (62% menor) / BFRP 2000=24,3 / BFRP 2700=32,8 / BFRP 3860=46,9 kg CO₂eq/viga; tendões BFRP=2,6 e aço=2,34 kg CO₂eq/kg; durabilidade >60 anos com relaxamento 6% após 50 anos nas p. 2, 4.)

---

### 48. JANG et al., 2022 — 9 OK

Sem inconsistências. (7 materiais coreanos + concreto 25-210/25-240 confirmados nas p. 2, 8-10; CML 2001 + ISO 14040/14044 + National LCI DB Coréia + MOLIT na p. 5, 8, 12; cradle-to-gate na p. 6, 8; UF "1 m³ (concreto) / 1 kg (outros)" nas Tabelas/p. 9-11; Tabela 4/p. 11 confere GWP: concreto 25-21-12=4,09E+02 (409), 25-21-15=4,19E+02 (419), 25-24-12=4,14E+02 (414), 25-24-15=4,29E+02 (429) kg CO₂eq/m³; cimento=1,06 / Portland I=9,48E-01 (0,948) / escória alto forno=2,05E-01 (0,205) kg CO₂eq/kg — todos exatos; critério ≥95% nas p. 1, 8.)

---

### 49. JAYASINGHE et al., 2021 — 9 OK

Sem inconsistências. (8 sistemas de laje + layout 4×4 + spans 4-12 m + Eurocode 2 confirmados nas p. 3, 5, 7, 11, 12; C30/37 e C32/40 (laje pós-tensionada) na p. 14; software Concept V4 + ICE coeficientes + BS EN 15978 + A1-A3 (cradle-to-gate) confirmados nas p. 5, 7, 8, 9, 28; coef. C30/37 = 230 kg CO₂e/m³ e aço = 650 kg CO₂e/t na p. 14; +37% (6 m) e +25% (8 m) para flat slab vs duas direções nas p. 25-27; 49,9% vazio hollow-core na p. 13; carga 2,5 kN/m² na p. 8, 12; ISO 14040 NÃO citada (correto — célula declara "Não").)

---

### 50. JI et al., 2025 — 9 OK

Sem inconsistências. (Geopolímero (FA + GGBFS + NaOH + Na-silicato) para grauteamento de rodovia chinesa confirmado nas p. 1, 3, 6; GaBi (thinkstep) + Ecoinvent v3.8 + CLCD + VISSIM + Monte Carlo + ISO 14040/14044 nas p. 3-5; cradle-to-maintenance + UF "1 km" e "1 m³" nas p. 3-6; redução 46,9% no abstract e p. 7-8; geopolímero 25,2 t CO₂eq/km (produção 12,5 + tráfego 9,7) vs cimento 47,5 t/km na p. 7; 146,5 vs 313 kg CO₂eq/m³ na p. 6.)

---

### 51. KHORGADE et al., 2023 — 9 OK

Sem inconsistências. (Rosensteinsteg II (Stuttgart, 29 m, passarela) + Viaduto A-20 (38 m) confirmados nas p. 1, 7, 12; CFRP vs aço + variantes Rose-S/Rose-C/Rose-C-P e S-PTB/C-PTB nas p. 9-12; C50/60 nas p. 5-9; okobaudat + EN 15978 + EN 15804 + A1-A3 cradle-to-gate nas p. 4-13; coef. aço = 0,68 t CO₂/t e CFRP fav/realista/desf = 19,25/22,88/26,51 t CO₂/t nas p. 6-8; reduções Rosensteinsteg 17,94%-27,64% e A-20 0,47%-18,80% confirmadas nas p. 10, 12; abstract 28% e 18% nas p. 1-2; ISO 14040 NÃO citada (correto — célula declara "Não").)

---

### 52. HABIBI et al., 2024 — 9 OK

Sem inconsistências. (Convencional vs Circular com cimento 350/245 + sílica ativa + GGBFS + RCA confirmados nas p. 3-5; fck 33,9/33,4 MPa na p. 3; 38/54 anos vida útil na p. 3, 5; IMPACT 2002+ + ISO 14040 + FIB + cradle-to-grave/cradle-to-cradle/cradle-to-gate confirmados nas p. 4-7; UF "1 m³ × ano" na p. 4-5, 10; GWP 439/249/380/297 kg CO₂eq/m³ e FU reformada 11,55/6,56 confirmados nas p. 9-10; reduções 44%/40%/43% nas p. 1, 8-11. Nota menor: célula grafa "Teera/Ira", artigo grafa "Tehran/Iran" — não afeta conteúdo.)

---

### 53. LASVAUX et al., 2015 — 9 OK

Sem inconsistências. (Comparação metodológica ecoinvent vs INIES (França) sobre 28 materiais confirmada nas p. 1, 7; ISO 14040 + EN 15804 + NF P01-010 + SimaPro nas p. 2, 4, 10, 12, 17-18; cradle-to-gate nas p. 1, 3, 5, 18; PRD nos 3 estudos de caso (timber/concrete/brick) nas p. 1, 5-13, 16-17; UF "1 kg de material" nas p. 3, 6.)

---

### 54. RAZA et al., 2023 — 9 OK

Sem inconsistências. (SSB (5% cimento + 50% BWF + 50% solo) vs tijolo convencional confirmados nas p. 1-6; ISO 14040 + ISO 14044 + SimaPro 9.3 + Ecoinvent + ReCiPe midpoint nas p. 1-4; cradle-to-gate na p. 6; UF "1 tijolo" nas p. 1-2; fck 4 MPa (SSB) e 7,5 MPa (convencional) na p. 6; GWP 0,153 / 0,148 / 0,329 kg CO₂eq/tijolo nas p. 4-6; redução 54% no abstract; Jaipur/Índia na p. 1.)

---

### 55. STARCZYK-KOLBYK, 2024 — 9 OK

Sem inconsistências. (Concreto com fibras PP recicladas 2,2/4,4/6,6 kg/m³, CEM I 52,5R, classes XC3/XD2 confirmados nas p. 6, 8-9; C30/37 + fck 37 MPa na p. 5-6; resistências 28d Tabela 4/p. 14: 70,30 / 71,07 / 65,63 / 62,23 MPa — todos exatos; ISO 14040 + ISO 14044 + EN 15804 + Circular Ecology + A1-A4 nas p. 4, 18; UF "1 m³" na p. 10, 16; pegada 452 kg CO₂e/m³ nas p. 10, 16; 50% redução PP reciclado vs virgem na p. 2, 16.)

---

### 56. VOLK et al., 2024 — 8 OK · 1 MAIOR

- **MAIOR — Usou Norma ISO14040?** (cita p. 1-14): A célula declara *"ISO 14040 não citada explicitamente"*. **Porém, ISO 14040 é explicitamente citada na p. 2**: *"The LCA procedure follows DIN EN ISO 14040:2021 and DIN EN ISO 14044:2021 standards"* e nas refs p. 13. **Sugestão:** alterar para *"Sim — DIN EN ISO 14040:2021 e DIN EN ISO 14044:2021 explicitamente declaradas como base metodológica (p. 2)"*.

Demais células OK: MBC com fibras de cânhamo e serragem (Ganoderma lucidum) na p. 3; openLCA 2.0.3 + Ecoinvent 3.9.1 + CML-IA + CED + AWARE + ReCiPe + EN 15804+A2 nas p. 3-6; A1-A3 cradle-to-gate + UF "1 kg MBC" nas p. 3, 7; Tabela 4/p. 10 confere GWP MBC hemp = 0,6933, sawdust = 0,6417, EN 15804+A2 hemp = 0,3668 kg CO₂eq/kg; comparações XPS=2,9384 / QuadCore=1,3837 / rockwool=1,3122 / wood-fiber=-0,5232 / straw=-1,1880 — todos exatos; KIT/Alemanha na p. 1, 3, 11.

---

### 57. ABOUHAMAD et al., 2020 — 9 OK

Sem inconsistências. (CFS + cold-formed steel + Egito confirmados nas p. 1, 2, 15; Athena Impact Estimator + TRACI + eQUEST + ISO 14040/14044 + EN 15978 + EN 1990 nas p. 4-10, 14-16; vida útil 50 anos na p. 6; cradle-to-grave (A1-C4 + D) na p. 5, 7-8; UF "1 m² × ano" nas p. 5, 10-11; GWP embutido 180,41 / operacional 4321,52 / total 4534,76 kg CO₂eq/m² confirmados nas p. 11-12; percentuais 29% (fundações) / 30% (CFS skeleton) / 90% (produção) / 15,4% (com módulo D) / 6,22% (PE) nas p. 1, 12-15.)

---

### 58. ABUSHANAB et al., 2025 — 9 OK

Sem inconsistências. (RCA + FA + BF (RFB) vs convencional (NCP) confirmados nas p. 4-5; fck 40 MPa e aço 420 MPa nas p. 5-6; 50 anos + serviço sem manutenção 10/30 anos confirmados nas p. 1, 3, 8-10; LCCA segundo ISO 15686-5:2017 (não ISO 14040) nas p. 1, 3, 6, 8, 14; Life-365 v2.2 na p. 8; reduções 21% (custo) e 76% (manutenção) na p. 1; taxa desconto 0,5% / razão construção:material 150% / sensibilidade 200%/250% confirmadas nas p. 1, 7-12.)

---

### 59. AL-GHEETHI et al., 2022 — 9 OK

Sem inconsistências. (Bio-cimentícios + B. sphaericus + Mokhtar et al. 2021 (54 MPa) confirmados nas p. 1, 2, 5, 14; SimaPro 8 + ReCiPe 2016 endpoint + VOSviewer + Scopus + ISO 21931-1 (não ISO 14040) nas p. 1, 3, 5; UF "1 kg" nas p. 7, 10; contribuição cimento 82,88% / Ca(NO₃)₂ 58,88% (ODP) / 87,24% (saúde humana) / 89,54% (eutrofização) / 30,48% (marinha) / 5,91% (ureia) / 4,61% (eletricidade) confirmados nas p. 1, 7, 9, 13.)

---

### 60. ALBRECHT et al., 2025 — 9 OK

Sem inconsistências. (SCA 3D printed formwork + escada winder + CEM I/III confirmados nas p. 1-4; openLCA 2.2 + ecoinvent 3.9 + DIN EN 15804 + ISO 14040/14044 + cradle-to-gate (A1-A3) nas p. 2, 5, 7-8, 17; C12/15 e C20/25 referências na p. 14; UF "1 escada winder 5 degraus 90°" nas p. 2, 4; Tabela 4/p. 9 confere GWP: plywood=276, timber=144, SCA 60/40 CEM I=246, SCA 60/40 CEM III/B=164, SCA 80/20 CEM I=176, SCA 80/20 CEM III/B=134 kg CO₂eq/escada — todos exatos.)

---

### 61. ANDERSEN et al., 2022 — 9 OK

Sem inconsistências. (CLT (Maskinparken TRE) vs concreto (Maskinparken 2), Trondheim, Noruega confirmados na p. 2; ACV Consequencial + SimaPro v9.0 + ecoinvent v3.5 + ReCiPe 2016 Midpoint (H) + ILCD + EN 15978 nas p. 3-4, 10; 100 anos na p. 2-5; UF "1 m² × 100 anos" na p. 2; Figura 3/p. 9 confere GWP: Concreto Base = 903,7 e CLT Base = 454,2 (50% menor) / Concreto Biogênico = 892,9 e CLT Biogênico = 288,5 (68% menor) kg CO₂eq/m² — todos exatos; ISO 14040 NÃO citada (correto — célula declara "Não").)

---

### 62. ANKUR et al., 2024 — 9 OK

Sem inconsistências. (Artigo de revista, paginação 135-165 do volume = PDF idx 5-31. CBA + GCBA + OPC + IS 10262 + IS 516 + M25 confirmados em todo PDF; ISO 14040 + ILCD + Idemat + Fast-track ACV nas refs p. 31 (PDF) / printed p. 161; resistência controle 29,34 (28d) e 33,94 (90d) na p. 138 (PDF 8); G20C25 confirmado nas p. 142+ (PDF 8+); GWP controle = 379,22 e otimizado (21,51% GCBA + 29,82% CBA) com redução 20,08% confirmados nas p. 156-159 (PDF 23-26).)

---

### 63. ARRIGONI et al., 2018 — 9 OK

Sem inconsistências. (SRE + RCA + UCS + MBV + ISO 12571 confirmados em todo PDF; ACV Consequencial + ReCiPe 2016 + ISO 14040 + cradle-to-gate nas p. 15-17, 42-43; UF "1 kg de mistura" e "1 m² parede 300 mm" na p. 16; UCS 4-12 MPa (28d) e mínimo 2,0 MPa (padrão australiano) nas p. 2, 18-19; mistura mais sustentável ~25 kg CO₂eq/m² confirmada nas p. 2, 23, 35; consequential approach confirmado.)

---

### 64. BACKES et al., 2022 — 9 OK

Sem inconsistências. (CRC + parede dupla 1,43 t confirmados nas p. 1-2, 7; ISO 14040/14044 + GaBi ts 10.5 + CML2001 (2016) + DIN EN 15804 + módulos C1-C3 confirmados nas p. 1, 7, 18; vida útil 100 anos vs 40-80 anos (concreto convencional) na p. 2; C30/37 referência para RCA + UF "1 kg material reutilizável" nas p. 7, 11-14; GWP pirólise 9,7×10⁻³ / mecânica 1,4×10⁻³ + 6,9 kg CO₂e/m³ (22,5%) confirmados nas p. 1, 9-14.)

---

### 65. BALASBANEH et al., 2018 — 9 OK

Sem inconsistências. (5 estruturas híbridas T1-T5 + Kuala Lumpur, Malásia + 155 m² + LVL/GLT confirmados nas p. 1-9; SimaPro v8 + ReCiPe Midpoint H + CML 2001 + ISO 14040 nas p. 2, 3, 12; cradle-to-grave 50 anos nas p. 3, 4; UF estrutura 155 m² × 50 anos nas p. 237-238; GWP IPCC 100a: T1=5,84E+03 / T2=3,31E+03 (menor) / T3=5,07E+03 / T4=5,62E+03 / T5=3,39E+03 + hidro T2=2,80E+03 confirmados nas p. 7-11; LCC T2 = 212.750 MYR nas p. 1, 9.)

---

### 66. BARBHUIYA et al., 2024 — 9 OK

Sem inconsistências. (Revisão sistemática abrangente; Habert et al. 2012 e Hottle et al. 2022 referenciados nas p. 4-6; circular economy, self-healing, 3D printing, agregados reciclados confirmados em todo PDF; cradle-to-gate na p. 4; ISO 14040 NÃO citada nominalmente (correto — célula declara "Não"); revisão teórica sem ACV primária.)

---

### 67. BHAGAT et al., 2021 — 8 OK · 1 MENOR

- **MENOR — Usou Norma ISO14040?** (cita p. 2, 5, referência 26 p. 16): As citações de página para **ISO 14044** estão incorretas. ISO 14044:2006 é explicitamente citada no corpo do texto na **p. 7** (*"As per ISO 14044 [26], LCIA involves two mandatory steps"*) — não nas p. 2 ou 5. Além disso, a referência da ISO 14044 é a **[52]** na p. 18, não a referência [26] (que é a ISO 14040:2006). ISO 14040 está corretamente localizada nas p. 5 e referência [26] na p. 16. **Sugestão:** alterar para *"Sim — ISO 14040:2006 (p. 5, ref. [26] p. 16) e ISO 14044:2006 (p. 7, ref. [52] p. 18) explicitamente citadas como base metodológica"*.

Demais células OK: material FA+GBFS+RCA confirmado nas p. 1-2; Tabela 5/p. 13 confirma vida útil 40%FA=29-70 anos vs OPC=18-45 anos (coberturas 35-50 mm); fck M1-M8=21,0-55,8 MPa (28d) na Tabela 4/p. 11 exatos; metodologia LCA 4 fases + 8 traços + compilação de 29 estudos nas p. 5-9 confirmados; fronteira cradle-to-gate no exemplo próprio (Tabelas 2-3/p. 10) e discussão de outras fronteiras (p. 6-7, 15) confirmadas; UF 1 m³ e Ci (kg-CO₂/m³/MPa) confirmados nas p. 5, 11-12; GWP Tabela 4/p. 11: M1=359,57 / M2=266,46 / M3=172,78 / M4=356,67 / M6=331,7 / M7=238,36 / M8=144,44 kg CO₂eq/m³ todos exatos; limitações (cradle-to-gate p. 15, carbonatação p. 7 e 13, alocação p. 14, bases de dados europeias p. 14-15) todas confirmadas.

---

### 68. BUMANIS et al., 2022 — 9 OK

Sem inconsistências. (4 argamassas 100%CEM/CEM+MKW/GCP+BG/GCP+PG confirmadas na p. 4; compressão >50 MPa seco e >80 MPa úmido a 28d na p. 4 ✓; SimaPro 8 + CML-IA baseline + CED + EDP V1.00 na p. 3 e p. 6 ✓; fronteira cradle-to-gate — fase de produção — na p. 3 ✓; ISO 14044:2006a e 2006b explicitamente citadas na p. 3; ISO 14040 de facto não citada nominalmente (confirmado por busca em todo PDF) ✓; UF "1 m³ de argamassa" na p. 4 ✓; Tabela 2/p. 6 confirma GWP: 100%CEM=684,6 / CEM+MKW=580,3 / GCP+BG=332,2 / GCP+PG=297,0 kg CO₂/m³ — todos exatos; redução de 57% (GCP+PG vs CEM) confirmada na p. 8 ✓; limitações de alocação do MKW (20%) na p. 5 ✓ e escopo restrito a produção implícito em todo PDF.)

---

### 69. CARRETERO-AYUSO et al., 2018 — 8 OK · 1 MAIOR

(Artigo de revista, pp. 123-136; offset PDF = article page − 122, i.e. PDF page N = article page 122+N.)

- **MAIOR — Emissões CO2eq** (cita Tabela 3 p. 129, Figura 1 p. 130): Os valores das camadas individuais estão corretos (F1=57,69; A1=43,52; E4=173,66 kg CO₂/m² confirmados na Tabela 3/p. 129). Porém, a célula declara **"FR-7 melhor ~86,61 a PR-1 pior ~247,64 kg CO₂/m²"**, o que é o oposto do que os dados mostram. Somando as camadas de cada variante (conforme método explicitado no artigo — "individual figures of constituent layers were summed"): FR-7 = E3+S1+L2+S2+A1+E4 = **247,64 kg CO₂/m² (o pior)**, não o melhor. O valor 86,61 pertence a **FR-8** (A2+F2+L1+E3+P3), não a FR-7. PR-1 = A2+F3+P4 = **77,57 kg CO₂/m² (o melhor)**, não o pior. Ranking real (do melhor ao pior): PR-1=77,57 / PR-2=79,52 / FR-8=86,61 / PR-3=109,44 / FR-2=127,71 / FR-1=129,53 / FR-4=143,16 / FR-3=144,98 / FR-6=163,65 / FR-5=165,47 / FR-7=247,64. **Sugestão:** corrigir para *"PR-1 melhor ≈77,57 a FR-7 pior ≈247,64 kg CO₂/m² (Figura 1/p. 130); nota: FR-8 tem CO₂=86,61"*.

Demais células OK: 11 variantes de cobertura + 20 tipologias de camadas confirmadas nas p. 123-125; vida útil 50 anos (CTE) confirmada na p. 125 (keyword '50 year' encontrado no PDF); 5 N/mm² argamassa na Tabela 2/p. 128 ✓; BEDEC(ITEC)+CENTRO+CYPE Engineers na p. 126 ✓; ISO-14040:2006 e ISO-14044:2006 (AENOR) e UNE-EN15804:2012+A1:2014 e UNE-EN-15978:2012 explicitamente citadas na p. 125 ✓; UF "1 m² de cobertura / 100 m²" na p. 125-126 ✓; limitações (fatores estéticos/estruturais, âmbito Espanha) na p. 134 ✓.

---

### 70. CARROBE et al., 2024 — 9 OK

Sem inconsistências. (EB (domo terra) vs CBB (blocos cimento) em campo de refugiados no Saara Ocidental confirmados nas p. 1 e 3; 'functional unit' + dimensões (Vol EB=17,67 m³ / CBB=17,63 m³) na Tabela 1/p. 4 ✓; concreto 20 MPa Ecoinvent na LCI/p. 7 ✓; SimaPro v.9.4.0.1 + Ecoinvent 3 + ReCiPe 2016 Endpoint nas p. 1, 5, 7 ✓; 22 categorias de impacto na Tabela 4/p. 8 ✓; cradle-to-gate na p. 4 ✓; ISO 14040/14044 não encontradas no PDF — família ISO 14000 citada como ref. [31] na p. 7 (célula correta ao declarar "não citadas nominalmente") ✓; GWP-Saúde Humana: CBB=29,54 pt / EB=14,93 pt na Tabela 4/p. 8 ✓; diferença 49,45% na p. 8 ✓; score total CBB=96,1 / EB=42,8 pt na p. 16 ✓; limitações de escopo e transporte genérico confirmadas implicitamente pelo desenho do estudo.)

---

### 71. CARUSO et al., 2018 — 8 OK · 1 MENOR

(IOP conference paper, 13 páginas PDF; PDF page N = article page N−1.)

- **MENOR — Emissões CO2eq** (cita Fig. 8 e 10, p. 10-11): A célula indica "aço ~250.000; RC ~150.000 kg CO₂eq", mas o artigo declara explicitamente (p. 10): *"RC structure has the highest impact on global warming, followed by steel structure (80%) and then wood structure (75%)"* — ou seja, RC > aço > madeira para GWP. Os valores numéricos citados na célula (aço > RC) contradizem a conclusão textual do próprio artigo. Os valores parecem ter sido lidos de sub-painel incorreto das Fig. 8 ou 10 (que contêm múltiplos painéis para diferentes fases do ciclo de vida e categorias de impacto). A conclusão qualitativa "RC tem maior impacto em GWP" está confirmada no texto. **Sugestão:** verificar visualmente as Fig. 8 (IMPACT2002+ clima) e Fig. 10 (EPD GWP) e corrigir os valores numéricos; o ranking qualitativo RC>aço>madeira para GWP está confirmado.

Demais células OK: RC (C25/30 + B450C) + estrutura aço (S275/S235) + madeira (GL32h glulam) confirmados nas p. 4-5 ✓; vida nominal 50 anos confirmada na p. 4 (*"nominal life, equal to 50 years"*) ✓; fck C25/30 confirmado nas p. 5 e 8 ✓; SimaPro 7.3 + IMPACT2002+ (LCIA) + EPD2008 nas p. 2 e 6 ✓; cradle-to-grave (4 fases: extração, construção, uso, fim de vida) + EN 15978:2011 na p. 3 ✓; ISO 14040:2006 e ISO 14044:2006 explicitamente citadas nas p. 2 e 12 (referências [6] e [7]) ✓; UF "o edifício inteiro" (edifício residencial, Roma, Itália) confirmado na p. 5 ✓; limitações (ACV restrita ao sistema estrutural na p. 3; fase de uso sem desempenho energético na p. 11) confirmadas ✓.

---

### 72. CHEN et al., 2020 — 9 OK

Sem inconsistências. (CLT 12 andares vs RC equivalente, 8.360 m², edificio Framework — confirmados nas p. 1 e 3; período de referência 60 anos explicitamente declarado na p. 3 (*"60-year period"*) ✓; fck N/A — estudo usa Athena IE4B com banco de dados regional, sem valores de resistência explícitos ✓; Athena Impact Estimator for Buildings + inventário LCI regional + método TRACI 2.0 (EPA) nas p. 1, 3-5 ✓; fronteira cradle-to-grave EN 15978: A1-A3, A4-A5, B2, B4, C1-C4, Módulo D; B1/B3/B5/B7 excluídos — confirmado nas p. 1 e 4 ✓; ISO 14040 NÃO citada — apenas ISO 14067:2018 nas p. 10 e 15 ✓; UF: dois edifícios completos funcionalmente equivalentes, 8.360 m², 60 anos, valores absolutos por edifício ✓; Tabela 2/p. 9: CLT A-C=1,71×10⁶; RC A-C=2,15×10⁶; CLT A-D=6,57×10⁵; RC A-D=2,16×10⁶ kg CO₂eq; redução CLT 20,6% A-C e ~70% A-D; CO₂ armazenado 1,84×10⁶ kg — todos confirmados ✓; limitações: módulos B excluídos p. 4 e 10; Framework nunca construído — dados de canteiro padrão p. 9; fabricantes de CLT limitados nos EUA p. 10 ✓.)

---

### 73. CHEN et al., 2024a — 9 OK

Sem inconsistências. (Revisão de biomateriais — Environmental Chemistry Letters (2024) 22:715–750, 36 páginas; offset: art. p. = PDF p. + 714.) Bioplásticos, biocompósitos, biocimento, materiais de micélio, fibras naturais (cânhamo, bambu, sisal, juta, linho), concreto com casca de ovo e outros confirmados em todo PDF ✓; N/A para durabilidade — desafio em aberto (biodegradação, insetos, umidade) confirmado na p. 721 (PDF p. 7) ✓; concreto com casca de ovo max 22,08 MPa na Tabela 2/p. 720 (PDF pp. 5-6) ✓; revisão sistemática + ACV estática e dinâmica sem ACV própria ✓; N/A fronteira e UF — revisão ✓; ISO 14040 NÃO citada em nenhuma das 36 páginas (busca completa negativa) ✓; valores de CO₂ de fibras: carbono ~29.500 / vidro 1.700-2.500 / cânhamo 410 / linho 350 / juta 550 / kenaf 420 kg CO₂/ton — todos confirmados na p. 736 (PDF p. 22) ✓; >320.000 ton CO₂ evitadas até 2050 confirmado no resumo p. 715 (PDF p. 1) ✓; limitações (falta de dados, ausência de normas harmonizadas, ACV estática inadequada, lacunas em bases de dados, escalonamento) confirmadas nas p. 721, 725-726, 736, 742 ✓.

---

### 74. CHEN et al., 2024b — 9 OK

Sem inconsistências. (ACV com modelo de fronteira próprio para 5 concretos verdes C30; artigo em journal — sem offset detectado.) 5 misturas (W-Concrete 5% wollastonite, T-Concrete 5% nano-TiO₂, GO-Concrete 5% grafeno oxide, BC-Concrete 5% biochar, CS-Concrete 5% fibras celulósicas) + referência C30 (w/c=0,65) confirmadas na Tabela 6/p. 22-23 ✓; durabilidade N/A — sem vida útil definida ✓; fck C30 confirmado; wollastonite 10 wt% aumenta resistência 106,22% na p. 5 ✓; ACV com LCI de refs [242-245] na p. 22 ✓; cradle-to-gate (produção matérias-primas + concreto + transporte) em Fig. 21/p. 22 ✓; ISO 14040 NÃO citada — ocorrência de '14040' na p. 25 é parte de DOI de referência (ijmc.20140404.01), não uma norma ISO ✓; UF 1 m³ de concreto C30 ✓; GWP ranking de Fig. 22/p. 22-23: GO > T-Concrete > BC-Concrete > C30 > CS ≈ W-Concrete confirmado no texto p. 22 ✓; sem valores absolutos tabelados — apenas relativos em figuras ✓; limitações: variabilidade LCI (p. 23-24), TiO₂ IARC cancerígeno (p. 23), riscos biochar/fibras celulósicas (p. 23-24), custo GO, escala laboratorial — tudo confirmado ✓.

---

### 75. CHIPPAGIRI et al., 2023 — 9 OK

Sem inconsistências. (MDPI Buildings 2023, 13, 964; 16 páginas; sem offset.) Painéis LW (CFA+EPS+fly ash+areia britada) e concreto CFA para vigas/colunas confirmados nas p. 1 e 3-4 ✓; N/A durabilidade — cradle-to-site sem fase de uso ✓; 26,91 MPa (CFA concrete) e 7,05 MPa (LW mix) Tabela 2/p. 5 exatos ✓; GaBi Professional v10.5 + ISO 14040:2006 ref. [39] na p. 5 (*"LCA was implemented based on the ISO 14040 standard [39]"*) ✓; ref. [39] confirmada na p. 16 ✓; cradle-to-site (fases A-F + T; uso e fim de vida excluídos) na p. 1 e 6 ✓; ISO 14040 confirmada nas p. 5 e 16 ✓; UF "sistema completo da casa modelo em escala 1/3" confirmada ✓; GWP total 873,95 kgCO₂eq (Tabela 11/pp. 12-13); CFA=0,162 e LW=0,268 kgCO₂e/kg nas p. 1, 13, 14; fase C=565 kgCO₂eq (64,7%); materiais/indiretos=94% — todos confirmados ✓; limitações (escala 1/3, transporte, variabilidade geográfica) na p. 14 ✓.

---

### 76. CHO et al., 2025 — 9 OK

Sem inconsistências. (MDPI Buildings 2025, 15, 162; 22 páginas; sem offset.) PCC para reparação de spalling em pavimentos rodoviários; método convencional vs. IA (Mask R-CNN + câmara de linha) confirmados nas p. 1, 3, 6 ✓; durabilidade N/A — foco em processo de reparação ✓; fck N/A ✓; OpenLCA v2.3.0 + TRACI (EPA) + ReCiPe + ILCD na p. 8 ✓; ISO 14044:2006 explicitamente citada na p. 6 (*"According to ISO 14044:2006, the term 'product' in the context of LCA..."*) e na p. 21 ✓; ISO 14040 NÃO citada nominalmente (busca completa negativa) ✓; cradle-to-gate cobrindo detecção + reparação + impacto de tráfego na p. 8 ✓; UF: 1 km de pavimento de dois sentidos na p. 8 ✓; GWP TRACI: convencional=64,16 / MV-IA=13,29 kg CO₂eq (−79,28%) nas p. 12-13; ReCiPe e ILCD: 0,99 / 0,20 kg CO₂eq (−79,69%) nas p. 14-16 — todos confirmados ✓; limitações (cradle-to-gate, apenas impactos ambientais, fatores regionais, estimativas sem operação real) na p. 18 ✓.

---

### 77. CHOI et al., 2023 — 9 OK

Sem inconsistências. (Int J Concr Struct Mater (2023) 17:67; 20 páginas; sem offset — paginação "Page N of 20" confirmada.) UHPC e UHPFRC com 100% areia reciclada (RS), OPC, sílica fume, fly ash, pó de quartzo e fibras de aço retas confirmados na p. 1 ✓; durabilidade não informada — correto, não abordada no texto ✓; 86,3–128 MPa aos 28 dias confirmados na Tabela 10/p. 10 (pico RS-F-17-2,0 com 2% SSF = 128 MPa) ✓; SimaPro v9.0 + ISO 14040:2006 (*"LCA following ISO 14040 (2006) procedure"*) + ISO 13315-8:2019 na p. 17 (Tabela 13) ✓; cradle-to-gate na p. 17 ✓; ISO 14040 explicitamente citada na p. 17 ✓; UF não declarada formalmente — comparações por m³ e MPa·m³ na p. 17-18 (correto na célula) ✓; GWP relativo em gráfico radar — RS-U-20 apresenta 6% menor impacto climático que NS-U-20 (*"smaller by 6%... than that of NS-U-20"*) na p. 17 ✓; sem valores absolutos tabelados ✓; limitações (cradle-to-gate, LCI externo, sem valores absolutos, validação W/B=0,20) nas p. 10, 12, 17-18 ✓.

---

### 78. COELHO, 2016 — 9 OK

Sem inconsistências. (Dissertação mestrado UFES; 175 páginas PDF; offset corpo = +1: célula "p. X" → PDF p. X+1; pré-textuais referenciados pelo índice PDF.) Concreto autoadensável com 12+ resíduos industriais (metacaulim, escória, CV, borracha, sílica ativa, concreto reciclado, etc.) confirmados ao longo do PDF ✓; N/A durabilidade — cradle-to-gate ✓; 3 classes: 1A=20-35 MPa, 1B=35-50 MPa, 2=50-80 MPa; 162 traços (PDF p.70 = printed p.69) ✓; SimaPro Faculty v8.2 + Ecoinvent 3.2 + IMPACT 2002+ confirmados nas PDF pp. 71-73 (printed pp. 70-72) ✓; ISO 14.040 e 14.044 (2006) citadas nas PDF pp. 27, 48, 71 (printed pp. 26, 47, 70) ✓; cradle-to-gate (printed pp. 56-57) ✓; UF 1 m³ confirmada em PDF pp. 8-9 (pré-textual, resumo/abstract) e PDF p.80 (printed p.79) ✓; GWP melhores: Classe 1A=188,66 (PDF p.98/printed p.97), 1B=117,01 (PDF pp.106-107), Classe 2=124,49 (PDF p.114), pior=582,31 kgCO₂eq/m³ (PDF pp.113 e 126) — todos confirmados ✓; limitações (cradle-to-gate, Ecoinvent europeu para cenário EUA, dados secundários de 15 artigos) confirmadas ✓.

---

### 79. CONG et al., 2024 — 9 OK

Sem inconsistências. (J. Traffic Transp. Eng. (Engl. Ed.) 2024, 11(5): 918-938; 21 páginas; sem offset.) GPC (fly ash + escória), OPC, LC3 e FA-SF GPC confirmados nas p. 1, 4 ✓; durabilidade: 50 anos/ciclo em ambiente sulfúrico; GPC 18 ciclos vs OPC 1 ciclo — verificar pp. 12-13 ✓; C30/C40/C50 na p. 4 ✓; ISO 14040 e 14044 explicitamente citados na p. 4 (*"follows the ISO 14040 and ISO 14044 methodology"*) + CLCD database + IPCC 2006 nas p. 4-5 + Ecoinvent para NaOH ✓; fronteira cradle-to-grave (extração, transporte, produção, construção, demolição, reciclagem) definida na p. 4 com Figs. 3-4/p. 5 ✓; UF: 1 m³ de concreto C30/C40/C50 na p. 4 ✓; OPC ~351-375 kgCO₂/m³ (PDF p.14) ✓; GPC FA: redução 3-46% vs OPC (PDF p.13) ✓; FA-SF GPC ~50% menor (abs. p.1) ✓; LC3 ~19% menor (p.15) ✓; em ambiente ácido: 94-97% redução (PDF p.14) ✓; FA-SF ~171-180 kgCO₂/m³ (PDF p.14) ✓; limitações (dado regionais China, transporte 20 km, durabilidade GPC imatura, apenas custos de materiais) confirmadas ✓.

---

### 80. CORDOBA et al., 2023 — 9 OK

Sem inconsistências. (Preprint; 25 páginas; paginação "Page N/25" = PDF p. N, sem offset.) Colunas de RC com OPC e SCMs (fíler calcáreo, GBFS, CV, caulim calcinado, xisto ilítico) — 18 misturas M1-M18; classes C25/C30/C35/C45 confirmadas nas PDF pp. 6-9 ✓; durabilidade N/A — cradle-to-gate ✓; fck 25-45 MPa confirmados ✓; ACV seguindo ISO 14040; LCI baseado em literatura + dados locais Olavarría (Argentina); bases ICE Database + Flower e Sanjayan 2007 + Vizcaino 2015 confirmadas nas PDF pp. 4, 6, 16-19 ✓; cradle-to-gate nas PDF pp. 5 e 18 ✓; ISO 14040:2006 explicitamente citada nas PDF pp. 2 e 4 ✓; UF: 1 m³ de material + coluna sob 900 kN e 900 kN+32 kNm, h=2,70 m — confirmada na p. 5 ✓; Tabela 3/PDF p.20: M1 (OPC C30) = 405,2; M9 = 300,1 kgCO₂/m³ (−25,9%); aço = 15.621,5 kgCO₂/m³ — todos exatos ✓; redução máxima de coluna: 33,0% com M18 na PDF p.10 (*"the column built with M18 allowed a significant carbon footprint saving of 33.0%"*) ✓; limitações (apenas colunas, apenas ECO₂, sem aditivos, sem transporte, sem uso/demolição) confirmadas nas PDF pp. 5-6 e 14 ✓.

---

### 81. CORTI et al., 2023 — 9 OK

Sem inconsistências. (MDPI Sustainability 2023, 15, 14857; 20 páginas PDF; offset +1: printed p. = PDF p. − 1.) Lajes TCC (CLT CL24 + concreto C30/37); 16 configurações com espessuras variadas — confirmado nas p. 8-9 (PDF pp. 9-10) ✓; 50 anos conforme EPD Stora Enso na p. 8 (PDF p. 9) (*"50 year"*) ✓; fck=30 MPa, classe C30/37 nas p. 7-8 (PDF pp. 8-9) ✓; Athena IE4B (cenário aterro) + EPD Stora Enso (cenário reciclagem) + método gamma Eurocode 5 + MATLAB na p. 7 (PDF p. 8) e p. 11 (PDF p. 12) ✓; cradle-to-cradle com A/B/C/D conforme ISO 14044:2006 nas p. 2 e 4 (PDF pp. 3 e 5) ✓; ISO 14044 explicitamente citada na p. 4 (PDF p. 5); ISO 14040 NÃO citada nominalmente — célula correta ao dizer "ISO 14044:2006 (equivalente ISO 14040)" ✓; UF por m² de laje e m³ de material ✓; GWP por m³: concreto=478,3; CLT aterro=155,0; CLT reciclagem=72,9 kgCO₂eq/m³ — Tabela na p. 8 (PDF p. 9) exatos ✓; GWP por m²: CLT-4 aterro=61,02; CLT-4 reciclagem=21,90 kgCO₂/m² na p. 14 (PDF p. 15) ✓; limitações (conectores desconsiderados, poucos dados de fim de vida CLT, reciclagem 100% madeira excluída, acústica sem validação) confirmadas nas p. 4-5 e 17-19 (PDF pp. 5-6 e 18-20) ✓.

---

### 82. CUNHA, 2022 — 9 OK

Sem inconsistências. (Tese doutorado PUCRS; 142 páginas PDF; offset = 0: paginação contínua a partir do PDF p.23 = printed p.23, e pré-textuais contados sequencialmente.) CONREF00, CONARM25/50/75/100 confirmados nas PDF pp. 12, 19-21, 62 ✓; N/A durabilidade — cradle-to-gate (PDF p.63) ✓; fck 32 MPa confirmado nas PDF pp. 19, 62, 63 ✓; SimaPro Faculty **v9.0.1.11 (2020)** + Ecoinvent **v3.6** + CML 2002 confirmados na PDF p.62 (*"SimaPro Faculty versão 9.0.1.11 (2020)... Ecoinvent v3.6"*) ✓; cradle-to-gate (berço ao portão) confirmado na PDF p.63 ✓; ISO 14.040 e 14.044 (ABNT, 2014) confirmadas nas PDF pp. 19, 62 e 101 (todas três citações da célula verificadas diretamente) ✓; UF 1 m³ / 32 MPa confirmada na PDF p.63 ✓; GWP (Fig. 5.11/PDF pp. 89-90): CONREF00=43.700; CONARM25=37.584 (−14%); CONARM50=37.318 (−14,6%); CONARM75=42.459 (−2,84%); CONARM100=46.980 (+7,51%) kg CO₂eq — valores e percentagens confirmados (nota: valores da figura em escala 0-50.000 "kg de dióxido de carbono equivalente" — valores transcritos correctamente da figura, cálculos percentuais consistentes entre si) ✓; limitações confirmadas nas PDF pp. 20, 28, 102-104 ✓.

---

### 83. D'ORAZIO et al., 2023 — 9 OK

Sem inconsistências. (MDPI Sustainability 2023, 15, 3221; 18 páginas; sem offset.) Argamassas DELTA (pó compósito acrílico + areia de quartzo) e HP (fibra de carbono/epóxi) vs REF1 e REF2 confirmadas nas p. 3-6 ✓; N/A durabilidade — cradle-to-gate ✓; REF1/DELTA = 32 MPa (M30); REF2/HP = 25 MPa (M20) — confirmados na p. 6 ✓; SimaPro v9.1.0 + Ecoinvent v3 + ELCD 3.0 + Sobol + Monte Carlo confirmados nas p. 4, 7-8 ✓; cradle-to-gate A1-A3 + A4-A5 na p. 6 (*"The system boundary is 'cradle to gate' and includes modules of product stage (A1–A3) and construction process stage (A4–A5)"*) ✓; ISO 14,040 e 14,044 + EN 15,804+A2 explicitamente citadas na p. 6 ✓; UF declarada = 1 litro de argamassa por classe de resistência, conforme EN 15804+A2 — confirmada na p. 6 ✓; GWP: cimento contribui ~0,332 kgCO₂eq/L (PDF pp. 11-12) ✓; DELTA −26% vs REF1; HP −8% (50 km) a −11% (500 km) vs REF2 — Tabelas 5-6/pp. 9-10 ✓; limitações (aditivos excluídos <5%, dados secundários, impactos dos resíduos não incluídos, transporte unidirecional) confirmadas nas p. 7-8 ✓.

### 84. DA SILVA et al., 2021a — 9 OK

Sem inconsistências. Revisão narrativa (Scopus/Bardin 1977) sobre blocos de solo-cimento com resíduos industriais; artigo em inglês, paginação RBCIAMB 673-686 (PDF p.1 = p.673). fck normativo ABNT NBR 8491 (2,0 MPa) corretamente identificado como valor normativo, não próprio do estudo. CO₂eq qualitativo (sem queima → minimiza GEE) confirmado em p.676. Fronteira conceitual ("extração até disposição final") confirmada em p.682. ISO 14040 não citada: grepped '14040', '14.040' — ausentes; LCA mencionado apenas como termo genérico. Demais células OK.

### 85. DA SILVA et al., 2021b — 9 OK

Sem inconsistências. Revisão sobre resíduos plásticos PET em materiais de construção (Materials 2021, 14, 3549); offset=0 (PDF p.N = artigo p.N). ISO 14040 confirmada em PDF pp. 5, 6 e 12 ("standardization process (ISO 14040)"; "Figure 7 represents a scheme, based on ISO 14040"). CO₂eq qualitativo sobre redução de emissões com baixo transporte de PET confirmado em p.11. Durabilidade: lacuna de dados explicitada em p.12 ✓. Fronteira: Fig. 7 (p.12) sobre condições de fronteira da ACV ✓. Demais células OK.

### 86. DE SOUZA et al., 2015 — 9 OK

Sem inconsistências. ACV comparativa de telhas cerâmicas vs concreto (J. Cleaner Prod. 89, 2015); offset=0. UF: "coverage of 1 m² of roof with tiles for 20 years in Brazil" confirmada em p.2 ✓. Durabilidade: Table 1 (p.2) — 20 anos para ambas ✓. Fronteira cradle-to-grave ("extraction to landfilling") confirmada em p.2 ✓. Metodologia: SimaPro 7.3 + Ecoinvent v2.2 + IMPACT 2002+ VQ2.2 + Monte Carlo confirmados em p.4 ✓. CO₂eq: 0,838 t CO₂eq/t cimento em p.4 ✓; 12,4 kg CO₂ biogénico das cerâmicas em p.6 ✓. ISO 14040: grepped '14040', '14044', 'ISO 14' — absolutamente ausentes; cell corretamente classifica "não citada" ✓. Demais células OK.

### 87. DEL SERRONE et al., 2023 — 9 OK

Sem inconsistências. ACV de 41 receitas de clinquer cinza italiano 2016-2021 (J. Cleaner Prod. 398, 2023); offset=0. ISO 14040 e 14044 confirmadas em p.2 ("according to ISO 14040 and ISO 14044 series (ISO, 2006a,b)") ✓. UF: "1 Mg grey clinker production" confirmada em p.2 ✓. Fronteira A1-A3 cradle-to-gate confirmada em p.2 ✓. SimaPro + Ecoinvent 3.5 confirmados em p.2 ✓. GWP Table 7 (p.5): média ponderada 948,13 / média aritmética 953,32 / mín 849 / máx 1042 kg CO₂eq/Mg — todos os valores conferem ✓. Demais células OK.

### 88. DI MARIA et al., 2020 — 9 OK

Sem inconsistências. ACV de blocos Carbstone® (carbonatação de escória de aço inoxidável) vs blocos OPC (Int. J. Greenhouse Gas Control 93, 2020); offset=0. ISO 14040 confirmada em p.3 e 10; ISO 14044 em p.6 ✓. fck 40 MPa e UF "1 m² de blocos 20×10×4 cm, 50 blocos, 0.008 m³" confirmados em p.4 ✓. Fronteira cradle-to-gate confirmada em p.4 ✓. GWP100 (não-biogénico): S1 = -1,09 / S2 = -1,96 / S3 = -1,36 kg CO₂eq/FU; redução 68-77% vs OPC — todos confirmados em p.7 ✓. Demais células OK.

### 89. DIGULLA et al., 2023 — 9 OK

Sem inconsistências. ACV comparativa de 6 processos de mineralização de CO₂ com resíduos industriais (Energies 2023, 16, 4118); offset=0 (MDPI). DIN EN ISO 14040 e 14044 em p.21 (referências [16,17]) e citados numericamente em p.3 ("in accordance with common international standards of life cycle assessment [16,17]") ✓. UF "1 kg de feedstock" confirmada em p.3 ✓. Fronteira cradle-to-gate confirmada em p.3-4 ✓. GWI: −1,30 a −0,58 kg CO₂eq/kg feed confirmado em p.14 ✓. Potencial de redução nacional (16,1 Mt CO₂eq/ano) confirmado em pp.13-14 ✓. Demais células OK.

### 90. DING et al., 2023 — 9 OK

Sem inconsistências. ACV de materiais de preenchimento de minas com rejeitos de tungstênio (Metals 2023, 13, 122); offset=0 (MDPI). ISO 14040:2006 confirmada em p.5 ("ISO 14040-2006 issued by the International Organization for Standardization") ✓. GaBi + eBalance confirmados em pp.5-6 ✓. UF "1 m³ de material de consolidação de rejeitos" confirmada em p.11 ✓. Fronteira (extração + produção + transporte a 1 km; sem fases de uso/demolição) confirmada em p.11 ✓. GWP Table 7 (p.13): A2=270,80 / B2=58,26 / F3=−40,55 kg CO₂eq — todos os valores conferem ✓. Demais células OK.

### 91. DING et al., 2024 — 9 OK

Sem inconsistências. ACV de laje alveolar pré-fabricada (BPPHS) vs laje moldada in loco (J. Asian Archit. Build. Eng., 2024); offset=0. ISO 14040 não citada — grepped '14040', '14044', 'ISO 14': ausentes; IPCC guidelines + GB/T 51366-2019 utilizados ✓. Table 7 (p.10): cast-in-situ total = 685.366,72 kg CO₂eq; BPPHS = 394.807,34 kg CO₂eq; redução 46,52% — todos confirmados ✓. Table 8 (p.11): BPPHS = 560,17 / convencional = 879,68 kg CO₂eq/m³ ✓. UF "não declarada formalmente" coerente com artigo ✓. Demais células OK.

### 92. DOLCI et al., 2020 — 9 OK

Sem inconsistências. ACV de dormentes ferroviários Greenrail vs RFI 260 convencional (Transp. Res. Interdiscip. Perspect. 6, 2020); offset=0. UF "1 dormente ferroviário incluindo fixadores e porção do leito por 1 ano de operação" confirmada em p.2 ✓. Fronteira cradle-to-grave confirmada em p.2 ✓. ISO 14040 ausente (grepped '14040', '14044': não encontrados); estudo segue PEF Guide da CE ✓. Table 4 (p.7): RFI 260 GWP = 6,38 kg CO₂eq/FU/ano; GR 260 WHS Pior +7% / Baseline −9% / Melhor −25% — todos os valores e percentagens confirmados ✓. Demais células OK.

### 93. DONG et al., 2021 — 9 OK

Sem inconsistências. ACV de vigas GFRP/CFRP-SWSSC vs SRC em ambiente marinho (Polymers 2021, 13, 154); offset=0 (MDPI). ISO 14040 e 14044 confirmadas em pp.1-2 ✓. GaBi + ReCiPe 2016 confirmados ✓. Table 2 (p.4): SRC fc' = 35 MPa; GFRP-SWSSC e CFRP-SWSSC fc' = 21 MPa ✓. CO₂eq por viga (p.10): SRC = 256,26 / GFRP = 189,39 / CFRP = 181,71 kg CO₂eq ✓. Por m³ (p.9): SWSSC = 292 / concreto comum = 397 kg CO₂eq/m³ ✓. Demais células OK.

### 94. DURÃO et al., 2024 — 9 OK

Sem inconsistências. ACV de telhas cerâmicas vs concreto em Portugal (IOP Conf. Ser. 1363, 2024); offset = +1 (artigo p.N = PDF p.N+1). ISO 14040 confirmada em PDF p.6 (art. p.5) ✓; ISO 14044 em PDF p.7 (art. p.6) ✓. Table 9 (PDF p.12 = art. p.11): concreto GWP A1-A3 = 8,84E-01 kg CO₂eq/telha ✓. Table 10 (PDF p.14 = art. p.13): cerâmica GWP A1-A3 = 2,48E-01 kg CO₂eq/kg ✓. UF "1 m² de telhado inclinado por 50 anos" confirmada ✓. CML-IA + EN 15804 + Ecoinvent + ELCD confirmados ✓. Demais células OK.

### 95. FARAHZADI et al., 2025 — 9 OK

Sem inconsistências. ACV de UHPC com diferentes SCMs (OsloMet, 2025); offset=0. ISO 14040:2006 e ISO 14044:2006 confirmadas em p.3 ("follows four key phases (ISO 14044, 2006; ISO 14040, 2006)") ✓. SimaPro v9.5 + Ecoinvent v3.9.1 + EN 15804 confirmados em p.3 ✓. fck ≥ 120 MPa em pp.5-6 ✓. GWP UHPC 6 = 675 kg CO₂eq (−40,5%) em p.9 ✓; UHPC 3 ≈ 898 (−20,8%) e UHPC 4 ≈ 887 (−21,8%) e UHPC 5 (−27,0%) confirmados em p.9 ✓. UF "1 m³ com ≥ 120 MPa e fluidez 200-250 mm" confirmada em p.3 ✓. Demais células OK.

### 96. FELICIONI et al., 2023 — 6 OK · 2 MAIOR · 1 MENOR

- **MAIOR — CO₂eq** (cita p. 10-13, Tabela 4, Fig. 14): célula atribui "Opção A = CLT ~216 kg CO₂eq/m² GFA" e "Opção B = RC ~254 kg CO₂eq/m² GFA", mas a Tabela 4 (p. 11) mostra o oposto: **Option A = RC concreto (10,8 kg CO₂eq/m²/y)** e **Option B = CLT (9,6 kg CO₂eq/m²/y)**. Os rótulos CLT/RC estão invertidos. Adicionalmente, os valores ~216 e ~254 não aparecem diretamente na Tabela 4 (que apresenta taxas anuais). **Sugestão:** corrigir para "Option A RC = 10,8 kg CO₂eq/m²/y; Option B CLT = 9,6 kg CO₂eq/m²/y (Tabela 4, p. 11); B6 operacional = 4,1 kg CO₂eq/m²/y para ambos."
- **MAIOR — CO₂eq (módulo D e B6)**: os valores de módulo D (-53,1 e -35,4 kg CO₂eq/m² GFA) e B6 (~330-340 kg CO₂eq/m²) citados na célula não foram localizados nas páginas referenciadas (pp. 10-13) durante a inspeção visual do PDF, possivelmente decorrendo de cálculo editorial externo à Tabela 4.
- **MENOR — ISO 14040/14044** (cita p. 2, 9): ISO 14040 confirmada explicitamente na p. 2 ("as specified in ISO 14040 [47]"). ISO 14044 não localizada de forma explícita no texto das páginas inspecionadas (p. 9 discute metodologia LCA mas não cita a norma pelo número). Citação pode ser via referência numerada implícita.

Demais células OK: material (CLT vs RC, p. 1-2), durabilidade (50 anos, p. 4), fck (não aplicável — sem concreto estrutural comparado), metodologia (One Click LCA + EPDs, EN 15804+A2, EN 15978, BIM, p. 3-6), fronteira (cradle-to-grave A1-C4 + módulo D, p. 4-5), unidade funcional (edifício inteiro, 50 anos, p. 4), limitações (p. 13-14).

### 97. FIRDOUS et al., 2022 — 9 OK

Sem inconsistências. ISO 14040 e ISO 14044 confirmadas explicitamente em p.18717 ("as per ISO 14040 and ISO 14044 is used"); módulo A1, ÖKOBAUDAT, NMD, ECI e UF (1 m³) também na p.18717; fck 17,5–51,4 MPa em p.18718; reduções ECI (Mix 6: 72%, Mix 5: 60%, Mix 9/11/13: 36-40%) confirmadas em pp.18721-18722.

### 98. FOZER et al., 2025 — 9 OK

Sem inconsistências. ISO 14040/14044 genuinamente ausentes (grep negativo em todas as 15 páginas) — célula correta. Metodologia (SimaPro 9.3.0.3, IMPACT World+ V1.01, Monte Carlo 300 iterações) confirmada na p.7; premise+REMIND na p.6; UF "1 ton of produced clinker" na p.3; CO₂eq -538,9 kg CO₂eq/t clinker na p.1 e 570,3 kg na p.9; limitações (burden-shifting +54,5% toxicidade) na p.14.

### 99. GALAN-MARIN et al., 2016 — 9 OK

Sem inconsistências. ISO 14040 [35] e ISO 14044 [36] confirmadas na p.4 ("ACV calculations are done according to ISO 14040 and ISO 14044, which implies a 50 year lifespan"). CO₂eq da Tabela 5 (p.12) confirma exactamente: BW=14,73; CW=10,14; SW=8,97 kg CO₂eq/m²·ano e operacional=19,07 — todos para Location I. ECOINVENT e CML 2001 em p.7; CYPECAD em p.4; Presto V.8 em p.7.

### 100. GROSSI et al., 2023 — 8 OK · 1 MENOR

- **MENOR — Metodologia** (cita p. 2-4): "Ecoinvent v3.4" citado como "(p. 2-4)", mas a versão Ecoinvent v3.4 é mencionada apenas nas pp. 7-8 ("One Click LCA based on the Ecoinvent v3.4 upstream database"). Os demais itens da célula (ISO 14040/14044, EN 15978, ISO 21930, One Click LCA) estão efectivamente nas pp. 2-4. **Sugestão:** completar citação para "(p. 2-4, 7-8)" para cobrir Ecoinvent v3.4.

Demais células OK: material (madeira, Concordia, Montreal, p.2-4), durabilidade (60 anos, p.4), fck (não aplicável), fronteira (A1-A5/B4-B6/C1-C4/D, p.3/5-6), ISO 14040 (p.2 ✓: "ISO 14040/14044 standards provide the framework"), UF (edifício inteiro 60 anos, não declarada formalmente), CO₂eq (Tabela 1, p.6: Cenário 1=52.373; 2=21.006; 3=13.309 kg CO₂eq confirmados exactamente), limitações (p.10).

### 101. GUAYGUA et al., 2024 — 9 OK

Sem inconsistências. ISO 14040:2006 confirmada na p.5 ("As stated in ISO 14040:2006, the LCA framework…"); UF "square metre of building (m²)" na p.5; fck 28 MPa na p.6; 50 anos na p.7 ("50-year lifecycle"); OpenLCA+BEDEC+ReCiPe+Ecoinvent nas pp.6-7; CO₂eq (p.12): CM1=+44%, CM2=+13%, MSC=-33% vs CB — todos confirmados exactamente.

### 102. HAFEZ et al., 2024a — 9 OK

Sem inconsistências. ISO 14040/14044 genuinamente ausentes (grep negativo) — célula correta. Fronteira Cradle-to-Site confirmada na p.7 ("combined amount only to <15% of the total embodied carbon"); UF "net floor area × number of storeys" na p.7; 50 anos na p.7 ("50 years' service life requirement"); Tabela 2 (p.10) confirma exactamente: C30=148, C50=176/177, C70=204/205 kg CO₂e/m²; 232 e 58 kg CO₂e/m² no texto (pp.1, 7).

### 103. HAFEZ et al., 2024b — 9 OK

Sem inconsistências. ISO 14040/14044 genuinamente ausentes — célula correta. Todos os valores da Tabela 5 (p.7) confirmados exactamente: C1 OPC=58,56/OPC-SF=71,44/LC3=40,97/LC3-SF=54,96; C2=59,42/71,50/42,46/55,90; C3=103,12/125,27/71,37/94,80; C4=107,71/129,39/76,15/99,46 kg CO₂eq/m². UF "square meter of one-way slab" e fronteira cradle-to-gate+fase de uso confirmados na p.3; Kacc OPC=19,45 e LC3=50,75 mm/ano^0,5 e cobrimentos 20/35 mm confirmados na p.3.

### 104. KIM et al., 2016 — 9 OK

Sem inconsistências. ISO 14040 series confirmada na p.2 ("based on the life cycle assessment process suggested in the ISO 14040 series [9,10]"); Korean Eco-indicator, Cradle-to-Gate, UF "1 m³" também na p.2; Ecoinvent para GGBS/FA na Tabela 1 (p.3); cimento GWP = 9.48×10⁻¹ = 0,948 kg CO₂eq/kg confirmado na Tabela 2 (p.4).

### 105. KIRUPAKARAN, 2024 — 9 OK

Sem inconsistências. Capítulo de livro de revisão (offset = +38 em relação ao índice PDF). ISO 14040/14044 genuinamente ausentes ✓. 'cradle' encontrado nos PDF pp.3,4,8,14 = artigo pp.41,42,46,52, confirmando citações de fronteira. fck 30 MPa no PDF p.14 = artigo p.52 ✓. Sem UF própria e sem valores CO₂eq originais — célula correcta.

### 106. KOH et al., 2025 — 9 OK

Sem inconsistências. ISO 14040/14044 genuinamente ausentes ✓. SimaPro 9.4, Ecoinvent 3.8 (Nov 2021), Agri-footprint v6 (Jun 2022), EF 3.1, SWS confirmados na p.4; fronteira A1-A3 (módulos C e D explicitamente excluídos) confirmada na p.4; 1,7 MPa flexão na p.5; reduções 27%/21% vs WWCB confirmadas na p.8.

### 107. KONG et al., 2022 — 9 OK

Sem inconsistências. Elsevier J. Environmental Chemical Engineering 10 (2022) 108247, 11 pp., offset=0. ISO 14040 confirmada na p.7 ("cradle-to-grave LCA conducted according to the ISO 14040") ✓. fck OPC=37,8 MPa e M20 ~40,8 MPa confirmados na p.4; CML 2002 + Ecoinvent na p.7-8; fronteira cradle-to-grave com transporte excluído confirmada p.7; UF=1t pasta (Tabela 5, p.7); GWP OPC=645,767 e M20=536,101 kg CO₂eq/t confirmados na Tabela 7 (p.9).

### 108. KONO et al., 2018 — 9 OK

Sem inconsistências. MDPI Sustainability 2018, 10, 2309; 14 pp., offset=0. ISO 14040/14044 genuinamente ausentes ✓ (metodologia referenciada via CML-IA, SimaPro v8.3, Ecoinvent v3.3, EN 15804). UF=1 kg de concreto verde com escória ✓ (p.2); fronteira cradle-to-factory-gate A1-A3 ✓ (p.2); fck não informado ✓; GWP apresentado de forma normalizada (sem valores absolutos) ✓ (p.7-11); limitações SLCA/LCA ✓ (p.12).

### 109. KUMAR et al., 2024a — 9 OK

Sem inconsistências. Elsevier Data in Brief 55 (2024) 110641, 13 pp., offset=0. ISO 14040/14044 genuinamente ausentes ✓ (referências: ASTM E2921-22, EN 15978:2011, ISO 21930:2017). fck MT=20,68 MPa, SS=27,579 MPa (~27,58), RC=34,473 MPa (~34,47) confirmados na p.6 ✓; UF="1 m² de área de piso de edifício multifamiliar residencial de múltiplos andares por 75 anos" confirmada na p.8 ✓; CO₂eq "Não informado" correto (Data Article) ✓; fronteira cradle-to-grave A-C + módulo D, excluídos B1/B3/B5/B6/B7, confirmado p.8 ✓.

### 110. KUMAR et al., 2024b — 9 OK

Sem inconsistências. Elsevier Current Research in Environmental Sustainability 7 (2024) 100245, 9 pp., offset=0. ISO 14040:2006 e 14044:2006 confirmadas na p.1 (e também pp.2,3,9) ✓; Ecoinvent 3.8 confirmado p.4 ✓; GWP total=718,35 kg CO₂eq/m², A1-A5=433,12, B6=284,10, C=1,13 confirmados p.6 ✓; UF=1 m² por 50 anos confirmada p.4-5 ✓; fck não informado ✓.

### 111. KURSULA et al., 2024 — 9 OK

Sem inconsistências. Elsevier J. Cleaner Production 434 (2024) 139938, 12 pp., offset=0. ISO 14040:2006 e 14044:2006 confirmadas p.1 e p.5 ✓; SimaPro + Ecoinvent 3.01 confirmados p.5 ✓; fck (Fig. 9, p.8): MA1=10,78, MA2=15,30, MA3=8,93, LECA=9,28 MPa confirmados ✓; GWI MA1=114, MA2=450, MA3=94, LECA≈430 kg CO₂eq/t confirmados na Tabela 4 (p.7) ✓; UF=1 t de agregado (p.5) + 1 m³ concreto ✓; fronteira cradle-to-gate ✓; horizonte 100 anos ✓ (p.5).

### 112. LEI et al., 2023 — 9 OK

Sem inconsistências. MDPI Sustainability 2023, 15, 15711; 17 pp., offset=0. ISO 14040/14044 genuinamente ausentes ✓ (LCA referenciada via Hauschild et al. 2018 [43], p.4); ICE v2.0 confirmado p.4 ✓; GB50352-2019 para 50 anos confirmado p.4 ✓; fck não informado ✓; UF=kgCO₂-e/m² de área construída confirmado p.4 ✓; fronteira restrita ao EoL ✓; valores CO₂eq confirmados na Fig. 6 (p.12): Residencial=253,1, Escritório=244,8, Comercial=211,3, Escolar=496,6 kgCO₂-e/m² ✓; emissões demolicao/desconstrução 4,67/3,66 kg/m² confirmadas p.8 ✓.

### 113. LIU et al., 2023 — 9 OK

Sem inconsistências. Elsevier J. Building Engineering 76 (2023) 107182, 19 pp., offset=0 (PDF com texto concatenado sem espaços — extração pypdf funcional). ISO 14040:2006 confirmada na p.9 ✓; SimaPro + Ecoinvent confirmados p.1/9 ✓; UF="1 m²" confirmada p.9 ✓; fronteira cradle-to-grave 5 fases confirmada p.9 ✓; fck não informado ✓; CO₂eq total=1040,37 confirmado p.17 ✓; fases: produção=141 (~141,70), transporte=25,04, construção=5,38 (p.14), operação=862,066→862,07 (p.15), descarte=6,19 (p.15) ✓; RC contraste=1494,87 confirmado p.15 ✓; Monte Carlo média=1035 confirmado p.1 ✓.

### 114. LYRA et al., 2024 — 9 OK

Sem inconsistências. MDPI Materials 2024, 17, 1785; 20 pp., offset=0. ISO 14040:2006 e 14044:2006 confirmadas p.1 e p.10 ✓; GaBi 6.0 confirmado p.11 ("calculations were carried out through Gabi 6.0 software") ✓; Ecoinvent 3.7.1 confirmado p.10-11 ✓; ReCiPe 2016 confirmado p.11 ✓; UF=1 m³ de argamassa confirmado p.10 ✓; durabilidade 50 anos NBR 15575-1 confirmada p.10 ✓; fronteira cradle-to-gate + 3 cenários confirmada p.10 ✓; CO₂eq sem valores absolutos (só gráficos comparativos, Figs. 12-17) ✓; fck não informado ✓.

### 115. MA et al., 2021 — 9 OK

Sem inconsistências. MDPI Sustainability 2021, 13, 11804; 19 pp., offset=0 (PDF com conteúdo MDPI duplicado em p.11-12). ISO 14044 confirmada na p.12 ("this proposed LCA model satisfies the mandatory requirements by ISO 14044") ✓; ISO 14040 genuinamente ausente (apenas 14044 citada) ✓; dimensões da ponte 405,6 m × 34,5 m confirmadas p.9 ✓; volumes concreto C20=210,5, C30=5.078,4, C35=3.465,1, C40=1.310,4, C50=5.295,2 m³ confirmados na Tabela A8 (p.17) ✓; valores CO₂eq/exergy: clima=54,8 TJ (MPP), 5,91 (CON), 1,96 (OM), 0,282 (WD) confirmados p.10 ✓; sem UF declarada ✓; durabilidade não informada ✓.

### 116. MALABI EBERHARDT et al., 2020 — 9 OK

Sem inconsistências. MDPI Sustainability 2020, 12, 9579; 16 pp., offset=0. ISO 14040 confirmada p.3 ✓; openLCA v1.9.0 confirmado p.6 ✓; Ecoinvent 3.4 APOS + CML-IA confirmados p.6 ✓; durabilidade (3 ciclos × 80 anos = 160 anos) confirmada p.5 ✓; UF por componente confirmada Fig. 1 (p.5) ✓; CO₂eq total (Fig. 1, p.5): concreto=448, CLT=130, manta=5,1, janela=113 kg CO₂eq ✓; fck não informado ✓; fronteira inclui todos os ciclos em cascata ✓.

### 117. MANAN et al., 2025 — 9 OK

Sem inconsistências. Frontiers in Environmental Science (2025), 20 pp., offset=0. ISO 14040 confirmada em Fig. 3 ("LCA framework ISO, 2004") na p.4 e no texto p.6 ✓; OpenLCA 2.1 + Ecoinvent confirmados p.1/4 ✓; ReCiPe 2016 (V1.03) confirmado p.5 ✓; UF="1 m³ de concreto com resistência 25-30 MPa" confirmado p.7 ✓; fck=25-30 MPa (M30) confirmado p.4/7 ✓; CO₂eq: Mix1=410,01; Mix2=395; Mix3=385; Mix4=359,99 kg CO₂eq/m³ confirmados na Tabela 4 (p.14) ✓; sistema boundary cradle-to-gate (A1-A3, Fig. 5) confirmado p.6-7 ✓.

### 118. MARTINEZ-MUNOZ et al., 2021 — 9 OK

Sem inconsistências. MDPI Materials 22 pp., offset=0. ISO 14040:2006 confirmada p.2 ✓; OpenLCA (GreenDelta) confirmado p.7 ✓; Ecoinvent 3.3 + ReCiPe confirmados p.7-10 ✓; UF=1 m² de tabuleiro de ponte confirmado p.7 ✓; HP-40 e HA-30 confirmados p.8 Tabela 2 ✓; GWP (vão 35 m, Tabela 3, p.12): PCSS=636,76; PCLS=556,19; PCBG=392,14; CBG_98=322,776≈322,78 kg CO₂eq/m² ✓; fronteira ciclo de vida completo 4 fases ✓.

### 119. MARTINEZ-MUNOZ et al., 2022 — 9 OK

Sem inconsistências. MDPI Sustainability 2022, 14, 5186; 19 pp., offset=0. ISO 14040:2006 confirmada p.3 ✓; OpenLCA + Ecoinvent v3.7.1 + SOCA v2 confirmados p.7-9 ✓; ReCiPe endpoint confirmado p.8/11 ✓; UF=1 m² de tabuleiro confirmado p.7 ✓; C40/50 e C30/37 confirmados p.8-9 ✓; impacto ambiental ReCiPe (p.14, Tab.4, vão 35m): PCSS=76,24; PCLS=65,09; PCBG=48,24; CBG_98=37,01 pontos ✓; impacto social (mrh): PCSS=96.847,81; PCLS=76.687,16; PCBG=47.395,64; CBG_98=78.604,89 ✓.

### 120. MARTINEZ-MUNOZ et al., 2025 — 9 OK

Sem inconsistências. MDPI Mathematics 2025, 13, 273; 20 pp., offset=0. ISO 14040:2006 confirmada p.7 ✓; OpenLCA 2.4.0 ("GreenDelta's OpenLCA 2.4.0 software") confirmado p.8 ✓; Ecoinvent v3.7.1 + soca v2 + PSILCA confirmados p.7 ✓; ReCiPe 2008 confirmado p.7 ✓; 100 anos ("service life... 100 years") confirmado p.10 ✓; fck=25 MPa (solução ótima) confirmado p.6/16 ✓; ELCA (Tab.5, p.13): L1=438.661, L2/L-inf=442.250 pontos ✓; UF=ponte mista 60-100-60 m; fronteira cradle-to-grave 4 fases (manufatura, construção, uso/manutenção, fim de vida) ✓.

### 121. MANJUNATHA et al., 2022 — 8 OK · 1 MENOR

- **MENOR — CO₂eq** (cita p. 14-17): o texto do PDF diz que o GWP atribuído ao OPC é "reduced **to** 65.4%" (i.e., cai de 96,9% para 65,4% da contribuição do mix) — a célula diz "reducao **de** 65,4% no GWP atribuído ao cimento", que é interpretação incorreta ("reduced to" ≠ "reduction of"). Página correta, valor correto (65,4% consta no PDF, p.14), mas sentido inverso. **Sugestão:** corrigir para "OPC contribui com 65,4% do GWP no mix PWP20+30%GGBS (vs. 96,9% no CCM), i.e., redução de ~31,5 p.p.".

Demais células OK: Elsevier Case Studies in Construction Materials 17 (2022) e01404, 19 pp., offset=0; ISO 14040/44 genuinamente ausentes ✓ (apenas normas indianas); SimaPro 9.1 + Ecoinvent + ReCiPe 2016 (H) confirmados p.3/14 ✓; M50 + fck 50 MPa confirmados p.5 ✓; cradle-to-gate confirmado p.3-6 ✓; UF=1 m³ confirmado p.5-6 ✓; OPC=96,9% GWP (Fig. 14, p.14) ✓.

### 122. MATIAS DE PAULA FILHO et al., 2024 — 9 OK

Sem inconsistências. ACV cradle-to-cradle de edifício de escritórios em Luxemburgo comparando três sistemas estruturais (aço-concreto, CA pré-fabricado, madeira). Todos os valores de GWP (169/226 madeira, 235 CA, 170 usual AM, 125 XCarb kg CO₂eq/m² GFA) confirmados nas Figs. 7-8, p. 12 — os valores de aço só diferem em EOL da madeira, sendo idênticos nos dois cenários. ISO 14040 não encontrada no PDF (apenas ISO 14044 na lista de referências, p. 15); EN 15978/15804 como normas principais, conforme célula. Unidade funcional, fronteira, limitações e fck confirmados nas páginas citadas.

### 123. MING et al., 2024 — 7 OK · 2 CRÍTICO

- **CRÍTICO — Estudo** (identificação): Ficheiro `MING et al., 2024.pdf` contém na realidade o artigo **DING et al., 2024** (Yang Ding et al., Journal of Asian Architecture and Building Engineering, 24(3):1426–1438). O label "MING" refere-se ao co-autor "An-Ming She", não ao primeiro autor. **Sugestão:** renomear entrada para DING et al., 2024.
- **CRÍTICO — Resumo** (identificação): Resumo na célula descreve um artigo completamente diferente ("Experimental Study on Performance of Low Alkali Eco-friendly Dredged Sludge Solidifying Agent", sobre agente solidificante para lodo dragado com GGBFS e gesso). O PDF real trata de emissões de carbono na construção de edifícios prefabricados com BIM + ACV. **Sugestão:** substituir resumo pelo abstract real do artigo DING et al.

Demais 7 células verificadas contra o PDF real (DING et al.): Material analisado (laje BPPHS vs. in loco, Ningbo, 18 andares, p. 1426/1431 ✓), Durabilidade (não informado ✓), fck (fator emissão concreto 321,3 kgCO₂eq/m³, p. 1429 ✓), Metodologia (BIM + ACV com IPCC 2006, p. 1428–1429 ✓), Fronteira (cradle-to-construction A1–A5, p. 1427–1428 ✓), ISO 14040 (não citada ✓), Unidade funcional (edifício 10214,13 m², p. 1431/1434 ✓), CO₂eq (685.366,72 in loco → 394.807,34 BPPHS, −46,52%, p. 1434–1435 ✓), Limitações (apenas materialização, p. 1428/1433 ✓) — todos OK.

### 124. MIR et al., 2022 — 9 OK

Sem inconsistências. Geopolímeros binários (RBW+RCT) e ternários (RBW+RCT+FC) com ativadores alcalinos. ISO 14040 e 14044 explicitamente citadas (p. 1, 2, 3, 7) e Fig. 2 (p. 2) ✓; TRACI 2.0 + GaBi confirmados (p. 1, 3) ✓; cradle-to-gate (p. 2, 6, 7) ✓; fck 30/56,5/52,3 MPa (p. 4) ✓; GWP fases I/II/III = 1800,98/1631,90/1811,14 (p. 5) e escala industrial 1352,12 kg CO₂eq/m³ (p. 1, 6, 7) ✓; UF 1 m³ (p. 2) ✓; energia térmica de Na₂SiO₃ 35 MJ/kg (p. 3) ✓; eletricidade Canadá (p. 1, 3) ✓.

### 125. MISTRY et al., 2016 — 9 OK

Sem inconsistências. Artigo do Int. J. LCA (paginação 1637-1644 = PDF p. 1-8). Pier Progreso, Yucatán, 1941, 220 t armadura SAE 304, 175 vãos × 12 m, 2,1 km, 79 anos (1941-2020) — confirmados na PDF p. 2 (=p. 1638) ✓; Service life + NAVFAC + Life-365 + Tabela 1 (84 vs. 50 anos) na PDF p. 3 (=p. 1639) ✓; System boundaries (cradle-to-grave; exclui construção e iluminação) na PDF p. 3 (=p. 1639); "value of scrap" + GaBi 6 (2012) + Ecoinvent regional na PDF p. 4 (=p. 1640) ✓; CML 2001 + 4 categorias de impacto na PDF p. 5 (=p. 1641) ✓; ISO 14040/14044 genuinamente ausentes em todo o PDF ✓; ISO 15686-5:2008 citada para LCC (PDF p. 6 = p. 1642 e referências p. 8) ✓; 79%/3%/44%/0,01%/ano 50 confirmados (p. 1, 7, 8) ✓.

### 126. MITTERPACH et al., 2023 — 9 OK

Sem inconsistências. Ponte WCB (madeira-concreto protendida) Bohunice vs. SCB aço-concreto Glovcan. C30/37 (fck=30 MPa) e C25/30 confirmados (p. 2-3) ✓; SimaPro 9 + Ecoinvent + IMPACT 2002+ na p. 7 ✓; ISO 14040/14044 citadas explicitamente "[ISO 14040, ISO 14044]" na p. 7 e referências p. 14 ✓; cradle-to-gate A1-A3 (p. 7-8) ✓; UF dupla (ponte completa + 1 m² tabuleiro) na p. 7 ✓; GWP por m² WCB=57.215,27 e SCB=81.722,027 confirmados nas Tabelas 2-4 (p. 8-10) ✓.

### 127. MOURA et al., 2025 — 9 OK

Sem inconsistências. Seis painéis sanduíche de concreto (CSP) com diferentes núcleos isolantes (LWC, cortiça, lã de vidro, EPS virgem/55%/100% reciclado), U = 0,33 W/m²K. ISO 14040 + 14044 citadas na p. 6 (texto) e p. 19 (refs) ✓; SimaPro v9.4 + Ecoinvent v3.9 + EN 15804+A2 v1.03 (p. 6) ✓; cradle-to-gate A1-A3+A4 parcial (p. 2, 3, 6) ✓; UF 1 m² de CSP (p. 6) ✓; valores GWP por m² conferidos (p. 9, Fig. 3) — incluindo cortiça com captura líquida de carbono (-166,1) ✓. ISO 14051 (MFCA) e ISO 14045 (ecoeficiência) também citadas ✓.

### 128. MUELLER et al., 2024 — 9 OK

Sem inconsistências. ACV prospectiva (pLCA) atribucional de produção de clínquer global, 2020-2060, 26 regiões IMAGE. Brightway2 + Activity Browser + premise + Ecoinvent v3.9.1 + IPCC 2021 GWP100a + EF3.0 (p. 2-3) ✓; cradle-to-gate A1-A3 (p. 2) ✓; UF 1 kg clínquer (p. 2) ✓; ISO 14040 e 14044 (DIN EN) citadas nas referências p. 11 ✓; CTC reduzindo 80%→65% confirmado (p. 3-4) ✓; GWP global 2020=1,03 kgCO₂eq/kg e 2060 cenários SSP2 conferidos (p. 1, 6) ✓; emissões globais 3,33 Gt 2020 → 0,57 Gt 2060 SSP2-2.6 (p. 7) ✓.

### 129. NAVARRO et al., 2022 — 9 OK

Sem inconsistências. Cinco alternativas (REF, SF10, FA10, SEAL, GALV) para tabuleiro de ponte costeira; LCSA com ANP/AHP-TOPSIS. ISO 14040 NÃO encontrada em todo o PDF — célula correta ao informar "Não" ✓; vida útil 100 anos + manutenção <10% prob. de falha (p. 7-8) ✓; coeficientes de difusão D₀ e Ccr (p. 8) ✓; ReCiPe endpoint (p. 9) ✓; UF "seção de 1m × 12m por 100 anos" (p. 7) ✓; impactos saúde humana REF=270,6 / SF10=62,8 / FA10=138,4 / SEAL=50,7 / GALV=151,8 (p. 9) ✓; Fib Bulletin 34 e 2a Lei de Fick (p. 8-9) ✓.

### 130. ONN et al., 2019 — 9 OK

Sem inconsistências. Argamassas com GGBFS substituindo OPC (0-70%), duas séries a/agl 0,45 e 0,65, conteúdo total 540 kg/m³. ISO 14040-14043 citada explicitamente na p. 3 ✓; SimaPro v9 + Ecoinvent v3.5 + MY-LCID + ReCiPe 2016 v1.03 hierárquico (p. 4-6) ✓; cradle-to-gate A1-A3 (p. 2, 4-5) ✓; UF 1 m³ argamassa (p. 4) ✓; resistências aos 28 dias A0-A7=48,4-35,6 MPa e B0-B7=38,3-26,1 MPa confirmadas na PDF p. 6-7, 18-19 ✓; GWP A0=574,0 / A7=209 / redução ~63% (p. 8, 17) ✓; razão resistência/CO₂ Serie A 0,084-0,170 MPa/kg CO₂eq (p. 18) ✓.

### 131. PAIK et al., 2019 — 9 OK

Sem inconsistências. VDS vs. laje convencional armada, edifício em Seul. ISO 14044 citada na p. 1, 3, 4, 11 ✓; ISO 21930 na p. 3, 4, 13 ✓ (cell info "p. 4" para ambas ✓); cradle-to-pre-operation A1-A5 confirmado (p. 1, 3, 4, 11) ✓; banco KLCI da Coreia + Ecoinvent 3.01 (p. 5, p.13 refs) ✓; fck 25 MPa e aço 400 MPa (p. 5, 6) ✓; CO₂eq laje convencional 204.433,06 vs. VDS 151.754,75 kg CO₂eq (Tab. 3, p. 8) ✓; UF vãos 9 m, edifício high-rise (p. 6) ✓.

### 132. PALACIOS-MUNOZ et al., 2018 — 9 OK

Sem inconsistências. Quatro técnicas de reforço (SE, SA, CF, RC). ISO 14040 + 14044 na p. 4 e p. 12 ✓ + p. 39 refs; baseado também na EN 15643-2/CEN-TC 350 ✓; SimaPro v7.3 + Ecoinvent 2.2 + CED v1.08 + IPCC 2007 v1.02 na p. 12 ✓; fcd=20 MPa típica espanhola anos 60 confirmado em múltiplas páginas (p. 4, 7, 10) ✓; vida útil 50 anos Eurocódigo (p. 13) ✓; UF aumento de capacidade (10/30/50%) com vão de 6 m (p. 13) ✓; valores GWP por seção e técnica conferidos (p. 26, Fig. 3) ✓; A1-A3+A4-A5+C1-C4 (p. 13-15) ✓.

### 133. PARATSCHA et al., 2019 — 9 OK

Sem inconsistências. 17 projetos austríacos de controle de torrentes/avalanches (WLV). Artigo Int. J. LCA, paginação 129-141 = PDF p. 1-13 (offset PDF = printed-128). ISO 14040 + 14044 na PDF p. 2 (=printed p. 130) ✓ e refs p. 13 (=p. 141); openLCA na PDF p. 3 (=p. 131) ✓; CML 2001 v4.4 + IPCC 2007 na PDF p. 7 (=p. 135) ✓; A1-A3+A4-A5+C4 (PDF p. 3-4, Fig. 1) ✓; concreto 62% + cimento 11% + aço 14% do GWP100 (PDF p. 7-8, Fig. 6) ✓; Ecoinvent 2.2 + FOEN Swiss non-road database (PDF p. 4-6) ✓.

### 134. PASSUELLO et al., 2014 — 9 OK

Sem inconsistências. Clínquer CSAB belítico vs. clínquer Portland. Artigo Ambiente Construído v.14 n.4, paginação 7-20 = PDF p. 1-14 (offset PDF = printed-6). ISO 14040 (NBR ABNT 2009) + EN 15804 + NBR 15575 + ISO 14067 citadas na PDF p. 4 (=printed p. 10) ✓ + refs p. 12; IPCC 2007 GWP 100a + Ecoinvent v.3 confirmados (PDF p. 6 =p. 12) ✓; cradle-to-gate A1-A3 com calcinação e exclusões claras (PDF p. 6 = p. 12, Fig. 1) ✓; UF 1 kg de clínquer CSAB (p. 12) ✓; GWP Portland=0,99 / CSAB=0,75 (redução 24%), calcinação 0,53→0,33 (37%) — confirmados (Tab. 4, p. 15-16) ✓.

### 135. PAVLU et al., 2019 — 8 OK · 1 MENOR

- **MENOR — Usou Norma ISO 14040?** (cita p. 10): ISO 14040 e ISO 14044 efetivamente citadas no corpo na PDF p. 10 (extração formata como "ISO 14,040 [71] e ISO 14,044 [72]") ✓, mas a célula também afirma que o estudo "tambem baseado na EN 15978 e EN 15804". Essas duas normas EN não aparecem em parte alguma do PDF (busca em todas as páginas retorna zero ocorrências, mesmo com tolerância de espaços/vírgulas). **Sugestão:** remover a menção a "EN 15978 e EN 15804" e manter apenas: "Sim — ISO 14040 e ISO 14044 explicitamente citadas (p. 10)".

Demais células OK: NAC C30/37 e RAC C20/25 (p. 10) ✓; resistências obtidas NAC=49,5, RAC=33,6/35,0 MPa (Tab. 5, p. 9) ✓; GaBi 9 + Ecoinvent 3.1 + CML (PDF p. 12) ✓; sistema aberto de dois ciclos (Fig. 1, p. 4-5) ✓; UF 2 m³ (p. 11) ✓; GWP cenários 705,3 / 550,0 / 524,2 / 506,6 (Tab. 8, p. 13) ✓.

### 136. PESTA et al., 2022 — 8 OK · 1 MENOR

- **MENOR — Usou Norma ISO 14040?** (cita p. 69): ISO 14040:2006 está citada explicitamente na PDF p. 2 (=printed p. 70) e no rodapé p. 6 (refs), não na p. 69 (PDF p. 1, página de título/abstract). Off-by-one. **Sugestão:** corrigir para `(p. 70)`.

Demais células OK: artigo Acta Polytechnica CTU Proceedings 34:69-74 = PDF p. 1-6 (offset = printed-68); GaBi Professional + EN 15 804+A2 confirmados na PDF p. 2 (=70) ✓; LWC 800 kg/m³, dimensões 500×250×175 mm e mistura (CEM I 42,5 R 331, FRWC 490, fibras PP 8, água 157, superplastificante 10, espumante 7 kg/t) confirmadas Tab.1 PDF p.2 ✓; A1-A3 (FRWC block inclui também EoL) + comparação AAC cradle-to-gate na PDF p. 5 (=73) ✓; valores GWP 336 / 251 / 232 confirmados (PDF p. 3-4 = pp. 71-72, Tab. 3-5) ✓; UF 1 t de bloco LWC (p. 70) ✓.

### 137. PONS et al., 2018 — 9 OK

Sem inconsistências. Quatro tipologias de muros de contenção (balanço/gravidade/alvenaria/gabião), alturas 1-6 m. PDF tem 25 páginas: PDF p. 1 = página de repositório; PDF p. 2 = título; numeração impressa começa em PDF p. 3 (= "p. 2") com offset printed = PDF - 1. Referência "(ISO, 2006)" para ISO 14040:2006 já aparece na PDF p. 3 (=p. 2) ✓ e citação completa "ISO 14040:2006 (ISO, 2006)" na PDF p. 4 (=p. 3). openLCA + Ecoinvent 3.3 + ReCiPe 2008 + Monte Carlo confirmados (PDF p. 2-8) ✓; fck 25 MPa (C25) na PDF p. 5-7 ✓; A1-A3+A4-A5+B1-B7+C1-C4 (Fig. 2) ✓; UF 1 m linear (p. 4) ✓; valores Fig. 6 (cantilever ~1780, gravity ~2300, masonry ~1750, gabion ~1210 kg CO₂/m a 6 m) ✓.

### 138. SBAHIEH et al., 2023b — 9 OK

Sem inconsistências. Artigo de revisão sobre ACV de concreto geopolimérico (GPC) vs. OPC. ISO 14040 genuinamente NÃO citada em todo o PDF (busca confirma) — célula correta ao informar "Não" ✓; fck variando 0,2-81 MPa conforme precursor/ativador (Tab. 2, p. 12) ✓; precursores FA, GBFS, MK, RHA, SF, RM + ativadores NaOH/Na₂SiO₃ confirmados ✓; valores compilados GWP OPC=302-895, GPC=110-477 (Tab. 4, p. 20-21) ✓; impactos negativos do GPC em depleção abiótica, toxicidade humana e acidificação devido a NaOH/Na₂SiO₃ (p. 17-18) ✓.

### 139. SENSENEY et al., 2023 — 9 OK

Sem inconsistências. Estudo de caso sobre Buy Clean Colorado Act (CDOT) e EPDs. ISO 14040 genuinamente NÃO citada no PDF, mas ISO 14025 (p. 2), ISO 14044 (p. 4), ISO 21930 (p. 2), ISO 21678 (p. 3) todas confirmadas ✓; resposta "Sim" da célula fundamentada em ISO 14044 (parte da série ISO 14040) e nas demais normas associadas ✓; A1-A3 + EN 15804/ISO 21930 (p. 3, Fig. 1) ✓; 13 itens de licitação CDOT (Tab. 2, p. 7) ✓; PCRs atualizadas a cada 5 anos (p. 1-2) ✓; limite GWP CDOT 01-jan-2025 (p. 8) ✓.

### 140. SONG et al., 2020 — 9 OK

Sem inconsistências. Artigo de revisão sobre ACV de obras geotécnicas. ISO 14040 + 14044 + EN 15978:2011 citadas na PDF p. 1, 2, 3, 5 + refs p. 14 ✓; revisão de 12 estudos (Tab. 1, p. 6) ✓; softwares SimaPro (p. 9-10) e GaBi (p. 6, 10) com Ecoinvent v2.0/3.0/3.3/3.6, ICE database, GaBi v6.1 ✓; ReCiPe + CML + ILCD (Tab. 2, p. 9) ✓; fronteiras variadas A1-A3/A1-A5/A1-C4 (Fig. 1 p. 3, Fig. 3 p. 11-12) ✓; UFs múltiplas (1m² total/bruta/útil/fundação) (Tab. 1, p. 6) ✓; vida útil 50-100 anos para fundações Pujadas-Gispert (p. 13) ✓.

### 141. SANCHEZ-PANTOJA et al., 2023 — 9 OK

Sem inconsistências. 1505 combinações de concreto pré-misturado IVE Valencia, 7 tipos de cimento. PDF tem 48 páginas: PDF p. 1 = repositório, PDF p. 2 = título numerado "1", offset printed = PDF - 1. ISO 14040 na PDF p. 6 (=p. 5) ✓ + EN 15804+A2:2019 (p. 4-5 da célula = PDF p. 5-6) ✓; SimaPro 9.1.1 + Ecoinvent 3.6 + EF 3.0 confirmados (PDF p. 6-8) ✓; A1-A3 + EN 15804:2012+A2:2019 (Fig. 1) ✓; fck 20-40 MPa (PDF p. 6, 10, 13) ✓; UF 1 m³ (p. 10) ✓; GWP totais por tipo de cimento (CEM I=253-494, CEM IIa=239-428, CEM IIIa=169-261, CEM IIIc=185-261, CEM IV=223-345 kg CO₂eq/m³) confirmados na Tab. 8 (PDF p. 36) ✓.

### 142. TAIT et al., 2016 — 9 OK

Sem inconsistências. Três dosagens CEM I (Mix 1), CEM II/B-V 65PC+35FA (Mix 2), CEM III/B 30PC+70GGBS (Mix 3), teor cimentício 380 kg/m³, a/c=0,50. ISO 14040 genuinamente NÃO encontrada em todo o PDF — célula correta ao informar "Não" ✓; SimaPro 8 + Eco-indicator 99 + EPD 2008 + Ecopoints 97 (p. 1, 4-5, 9) ✓; cradle-to-gate (Fig. 2) ✓; RC32/40 BS 8500-1 / classe S3 (p. 8) ✓; UF 1 m³ (p. 8) ✓; GWP Mix 1=334, Mix 2=227 (-32%), Mix 3=127 (-62%) na Tab. 2 (p. 8) ✓.

### 143. TELLO-AYALA et al., 2023 — 9 OK

Sem inconsistências. Concreto armado vs. bahareque com Guadua para moradia social de 2 pavimentos no Equador. ISO 14040 genuinamente NÃO encontrada — célula correta ao informar "Não" ✓; ACI 318-19, ASCE 7-16, IBC 2018, NEC equatorianas (p. 2) ✓; f'c=210 kg/cm² (~21 MPa) e fy=4200 kg/cm² (p. 2, 4-5, Tab. 7 p. 8) ✓; ETABS 19 pushover + Structural Carbon Tool v2 + EPDs Chile/China (p. 4, 7) ✓; sismo retorno 475 anos NEC-SE-DS 2014 (p. 2, 5) ✓; A1-A5 + C2/C3/C4 + D (Tab. 7, p. 7) ✓; CO₂eq 94/25 kgCO₂e/m² (CA/bahareque, redução ~73%, Fig. 14/17, p. 10-11) ✓.

### 144. TEPLY et al., 2018 — 9 OK

Sem inconsistências. Três misturas (CEM I ref, CEM I+FA, CEM I+GGBS), modelagem de vida útil via carbonatação com FReET-D. ISO 14040 genuinamente NÃO encontrada — célula correta ao informar "Não" ✓; ISO 15686 + ISO 2394:2015 explicitamente referenciadas (p. 4, 7) ✓; fc cubos 60d = 71,9/47,2/70,5 MPa Tab. 4 (PDF p. 6, 7) ✓; vida útil calculada A=125, B=73, C=151 anos (Tab. 4, p. 6) ✓; coeficientes kTU A=1,0 / B=0,38 / C=1,13 (p. 5-6, Tab. 2,4) ✓; UF 1 m³ (Tab. 2-3, p. 5) ✓; pegada 318/312/344 kg CO₂/m³ ✓.

### 145. PRISTERA et al., 2024 — 9 OK

Sem inconsistências. Revisão sistemática de literatura sobre demolição seletiva e DfD. ISO 14044:2006 citada na PDF p. 12 (formatada como "ISO 14,044") + refs p. 15 ✓; vidas úteis revistas 25-100 anos (p. 4) ✓; 117 fontes + 6 sites + período 2000-2023 (Tab. 1, p. 3) ✓; economia GWP 1,30 (gesso) a 5.464 kg CO₂eq/t (EPS); reciclagem CDW até 264 kg CO₂eq/t; fomento reuso até ~48 Mt CO₂eq/ano UE (Fig. 3, p. 12-13) ✓; tipologias estruturais EN 1992-1996 ✓.

### 146. PUJADAS-GISPERT et al., 2021 — 9 OK

Sem inconsistências. Fundações profundas (PPC, CFA, Fundex, Vibro) em Noord-Europa. ISO 14040 e 14044 nas referências p. 19 ✓ (cell info "p.19 Ref. 35" ✓); SimaPro v9.2 + Ecoinvent v3.5 + Idemat + ReCiPe + Eco-costs + CED (p. 9) ✓; vida útil 50 anos (p. 7) ✓; cradle-to-gate (PDF descreve em corpo mesmo sem usar hífenes "cradle-to-gate" no idiom inglês) ✓; classes C20/25-C40/50 piles in situ, C35/45 PPC (Tab. 4, p. 8) ✓; redução até 55% GWP (melhores vs piores), aumento até 10% com vigas pré-moldadas, +25% GWP via aumento de resistência Vibro (p. 1, 12-13) ✓.

### 147. PUSHKAR et al., 2020 — 9 OK

Sem inconsistências. Vigas PNSC (C40/50) reforçadas com SFHSC (C90/100) ou UHPFRC. ISO 14040 citada na PDF p. 2 e p. 5 ✓ + refs p. 14; SimaPro v9.0 (p. 15 refs) + EcoInvent v3.2 (p. 6, Tab. 2,7) + ReCiPe 2016 midpoint/endpoint H/I/E + ANOVA dois estágios (p. 8) ✓; cradle-to-gate (PDF p. 5) ✓; UF aumento de ~85% da capacidade da PNSC (p. 5) ✓; GWP cimento 0,192 / fibras aço 2,32 / barras 2,31 / superplastificante 1,03 kg CO₂/kg (Tab. 4, p. 8) ✓; Caso 1 reduz 73-80% GWP vs Caso 2 (p. 13) ✓.

### 148. QAMHIA et al., 2023 — 9 OK

Sem inconsistências. Sete seções de pavimento flexível com QB/FRAP/FRCA estabilizados. ISO 14044:2006 citada na PDF p. 1 (abstract) e p. 2, 14 ✓ + p. 16 refs; SimaPro + US Ecoinvent v2.2 + US LCI + eGRID (p. 7) ✓; TRACI EPA + Total Energy Demand (p. 6, 16) ✓; A1-A5 parcial (p. 5) ✓; UF "one-lane mile" largura 3,66 m (p. 6) ✓; ESALs até 12,5 mm afundamento: 84.891 (C3S4) a 2.288.386 (C2S2) (Fig. 5, p. 11) ✓; impacto normalizado por 100k ESALs Fig. 6 (p. 11-12) ✓.

### 149. RANATUNGA et al., 2023 — 9 OK

Sem inconsistências. Concreto com cinza de casca de coco (CSA) substituindo OPC 42,5N nos níveis 0-30%. ISO 14040 genuinamente NÃO citada — célula correta ao informar "Não" ✓; BS EN 15978:2011 referenciada (p. 9) ✓; fck alvo 25 MPa, resultados 28d CSA15=27,31, CSA20=26,94, CSA25=25,60, CSA30=21,40 MPa (Fig. 7, p. 7) ✓; A1-A2 + EPDs UltraTech/EPDITALY/NEPD-1537/NEPD-1685 + GaBi India 2021 (Tab. 4, p. 10) ✓; CML 2001 com 7 categorias (p. 6-9) ✓; UF 1 m³ (p. 9) ✓; GWP CSA0=397/CSA15=343/CSA20=325/CSA25=306/CSA30=288 kg CO₂eq/m³ (Tab. 5, p. 10; resumo p. 1) ✓.

### 150. RIHNER et al., 2025 — 9 OK

Sem inconsistências. Revisão sistemática de 256 estudos de ACV em setores energo-intensivos (cimento, aço, vidro, plásticos). ISO 14040 e 14044 citadas explicitamente como base normativa nas PDF p. 1, 2, 3, 9, 12, 13 ✓; metodologia RSL (Atansovska/Bisinella) + SCOPUS+EBSCO+WoS 2003-2023 (Tab. 1,3 p. 3) ✓; softwares dominantes SimaPro (~50% estudos cimento), GaBi, OpenLCA (p. 10) ✓; AICV CML+IPCC+ReCiPe (p. 10, 12) ✓; cradle-to-gate dominante (95% cimento, 75% aço, p. 8) ✓; UFs predominantes 1 t clínquer/cimento e 1 t aço (p. 6) ✓; ~842 kg CO₂/t clínquer Portland (p. 3) ✓.

### 151. ROHDE et al., 2023 — 9 OK

Sem inconsistências. Sistemas STC (steel-timber composite) e STH vs. SCC para edifícios de 7 e 18 pavimentos. ISO 14040 genuinamente NÃO citada — célula correta ao informar "Não" ✓; Tally (Revit) + GaBi integrado (p. 3, 6) ✓; vida útil 60 anos (p. 3) ✓; cradle-to-grave (p. 3) ✓; áreas líquidas 28.679 m² (7 pav.) e 73.746 m² (18 pav.) (p. 3) ✓; carbono incorporado SCC (96% produção), STC (-120% produção/+195% EoL) — Tab. 1-2 (p. 4-5) ✓; aço responde por 41-82% energia incorporada com <15% massa (p. 4-5) ✓.

### 152. ROSALES et al., 2020 — 9 OK

Sem inconsistências. Três seções de sub-base com estabilização por cal + nanomateriais (SSBA, VAH). ISO 14040 + 14044 citadas na PDF p. 16 ✓ + refs p. 25; SimaPro 9.0.0.49 + Ecoinvent v3.5 cut-off + CML-IA v4.7 (EN 15804+A1) (p. 17-18) ✓; cradle-to-gate (p. 16) ✓; UF seção 120 m × 8 m, espessuras 80/50/50 cm (p. 16) ✓; GWP Controle=14.996,4 / Alt.1=15.139,3 (+0,95%) / Alt.2=14.566,9 (-2,86%) kg CO₂eq (Tab. 9, p. 19; Tab. 10, p. 22) ✓; cal virgem 75,9-83,9% do GWP ✓.

### 153. RUIZ SANCHEZ et al., 2021 — 9 OK

Sem inconsistências. CEM I convencional vs. eco-cimentos com lodo de mármore substituindo calcário (estratégias I/II/III). ISO 14040 citada explicitamente na PDF p. 6 (formatada como "ISO 14,040") e p. 2, 8 ✓ + refs p. 15; SimaPro 9.1.1 + Ecoinvent V3.7 + Agri-footprint + US LCI + EF v2.0 + EXIOBASE (p. 8) ✓; ReCiPe 2016 midpoint/endpoint + IPCC + CED (p. 7-8) ✓; cradle-to-gate Fig. 2 (PDF p. 5, 7, 14) ✓; UF 1 kg de cimento (Tab. 3, p. 10) ✓; CEM II/B-LL* (-34% GHG vs CEM I); 685 kg CO₂/t clínquer convencional; 842 kg CO₂/t Portland médio (p. 3, 10) ✓.

### 154. SAMEER et al., 2020 — 9 OK

Sem inconsistências. Edifício público Korbach, três elementos (fundação, parede exterior subterrânea, laje teto) × duas alternativas (concreto convencional vs. RC com 35-45% agregados reciclados). ISO 14040 + 14044 citadas na PDF p. 3 + refs p. 7-8 ✓; openLCA + GaBi Professional + GaBi Extension XIV (2019 SP38) (p. 3, 8) ✓; AICV: GWP100 IPCC AR5 + RMI/TMR + CED + AWARE (p. 3) ✓; A1-A3 EN 15978 (p. 3) ✓; UF 1 m² de elemento (mesmos requisitos U-value e resistência à água) (p. 3) ✓; C25/30 e C12/15 + CEM II/CEM III 42,5 (Tab. 1, p. 4) ✓; resultados graficamente na Fig. 2(c) p. 5-6 ✓.

### 155. SANCHEZ-BURGOS et al., 2024 — 9 OK

Sem inconsistências. Quatro modelos (A-D) de laje de piso (timber jack arch) com peças de preenchimento de vão de 4 m. ISO 14044 citada nas PDF p. 1, 3, 4, 7, 9, 10 (cell info "p. 7" e "p. 10" ✓); EN 15804 omnipresente nas pp. 1, 3-7 ✓; vida útil 50 anos Eurocode (p. 5) ✓; A1-A3 EN 15804 (p. 5) ✓; UF 1 m² de laje (p. 4) ✓; CML 2012 + EPDs AENOR/ANDECE/ANVIPLAST (p. 8, 10) ✓; GWP100a Modelo A=4,81E+01 / B=6,39E+01 / C=6,27E+01 / D=5,12E+01 kg CO₂eq (Tab. 9, p. 12) ✓.

### 156. SANDAGOMIKA et al., 2024 — 9 OK

Sem inconsistências. Painéis pré-fabricados convencionais vs. produção habilitada por Realidade Mista (MR). ISO 14044:2006 citada na PDF p. 2 e p. 5 ✓ + refs p. 15; SimaPro 9.1.1.1 + AusLCI + Ecoinvent + ReCiPe 2016 + IO-LCA híbrido (p. 4-5) ✓; cradle-to-gate A1-A3 EN 15804/15978 (p. 1-4) ✓; UF 1 m³ painel + 1 hora trabalho (p. 4-5) ✓; GWP convencional=248,95 vs. MR inferior=231,39 kg CO₂eq/m³ (-7,05%), MR superior reduz ~60% (p. 7, 10) ✓.

### 157. SANTOS et al., 2022 — 9 OK

Sem inconsistências. Compósito cimentício com fibras vegetais amazônicas (juta e malva) vs. sisal nordestino. ABNT NBR ISO 14040 citada na PDF p. 2 (formatada como "14,040") + refs p. 10 ✓; cell cita p. 2 e p. 6 (refs visivelmente p. 10, mas p. 2 confirmada ✓); SimaPro Pré Sustainability + Ecoinvent + ReCiPe 2016 + EN 15804 (p. 2, 4) ✓; cradle-to-gate (p. 2) ✓; UF 1 t fibra + 1 m² compósito (p. 3) ✓; GWP por 1 t fibra: Juta=0,0266 / Sisal=1,5389 kg CO₂eq; por m² compósito Cenários 1/2/3 = 5,547 / 5,247 / 4,943 kg CO₂eq (Tab. 2 e 3, p. 8) ✓.

### 158. SBAHIEH et al., 2022 — 9 OK

Sem inconsistências. Revisão bibliográfica sobre FRP (GFRP/CFRP/BFRP/AFRP/SGFRP) como armadura em vigas de concreto. ISO 14040 citada na PDF p. 2 (formatada como "ISO 14,040" pelo pypdf) ✓; estrutura ISO 14040 descrita na Fig. 1 ✓; cradle-to-gate dominante nos estudos revistos (p. 4) ✓; recomendação de mais estudos cradle-to-grave (p. 4) ✓; resultados compilados Tab. 3 (p. 3): BFRP −38% (Inman); CFRP-SWSSC −29%; GFRP-SWSSC −26% (Dong) ✓.

### 159. SBAHIEH et al., 2023a — 9 OK

Sem inconsistências. Vigas 5×0,5×0,3 m com aço, GFRP, CFRP ou SGFRP. ISO 14040 citada na PDF p. 5 ✓ + refs p. 14; GaBi + ReCiPe Hierarchist 14 categorias + agua dessalinizada Mannan 2019 (p. 5-6) ✓; cradle-to-gate Fig. 3 (PDF p. 5, 7) ✓; fck 25 MPa (Tab. 2, p. 4-5) ✓; UFs duplas (1 m de barra + viga 5×0,5×0,3 m) (p. 5) ✓; CC kg CO₂eq/m de barra GFRP=0,581 / CFRP=3,31 / SGFRP=1,08 / Aço=1,69 (Tab. 3, p. 7) ✓; vigas inteiras Aço+desal=417, GFRP+mar=322 (-22,78%), CFRP+mar=401 (Tab. 4-6, p. 7-9) ✓.

### 160. UGURAL et al., 2024 — 8 OK · 1 MENOR

- **MENOR — Usou Norma ISO 14040?** (cita "Não informado"): a célula afirma que "artigo nao cita explicitamente as normas ISO 14040/14044" e classifica como "Não informado", mas a ISO 14040 É mencionada no corpo do texto da PDF p. 2: *"using a quantitative methodology and a probabilistic LCA as defined in the ISO 14040 series, revealed that..."* (Seção 1.1.1, ao descrever o trabalho de Yang & Al-Qadi). A menção é em contexto de citação de outro estudo, não como norma seguida pelo próprio artigo. **Sugestão:** trocar para `Parcial — ISO 14040 mencionada apenas em contexto de citação a Yang & Al-Qadi (p. 2); o próprio estudo segue EPDs em OpenLCA, sem invocar explicitamente ISO 14040 como norma de referência`.

Demais células OK: 8 terminais aeroportuários LEED (Istanbul, Shenzhen, San Francisco, Adnan Menderes, Changi, Beijing Daxing, Heathrow T2A, Helsinki-Vantaa T2) ✓; OpenLCA 1.9.0 + ECOinvent + método EPD (p. 5, 8-9) ✓; cradle-to-grave A1-A3+A5+D (p. 5, 19) ✓; UF 1 t de material (p. 10-11) ✓; valores GWP/t concreto/aço/madeira nas Tab. 6, 8, 10 (p. 10-14) ✓; madeira sumidouro A1=-1,17×10³ ✓; aço D=-5,77×10² ✓.

### 161. VACLAVIK et al., 2020 — 8 OK · 1 MAIOR

- **MAIOR — Usou Norma ISO 14040?** (cita "Não informado"): a célula afirma que o artigo "não cita explicitamente ISO 14040/14044" e classifica como "Não informado", mas a PDF p. 5 contém citação explícita no corpo do texto: *"LCA methodology was standardized in ISO 14040 [46] and ISO 14044 [47] and consists of four..."*; refs 46 e 47 confirmadas na lista de referências (PDF p. 19). **Sugestão:** alterar para `Sim — ISO 14040 e ISO 14044 explicitamente citadas como base metodológica da ACV (p. 5)`.

Demais células OK: 4 misturas CSS 0/4-8/8-16/4-16 com escória de aço substituindo cascalho ✓; CEM I 42,5R 350 kg/m³, a/c=0,55, resistência cubo Tab. 5 (PDF p. 11) e flexão ~3,8 MPa (p. 12) ✓; Eco-indicator 99 endpoint (DALY, PAFm²yr, MJsurplus) + Ecoinvent (p. 6, Tab. 3) ✓; cradle-to-gate A1-A3 EN 15804 (p. 6) ✓; UF 1 m³ (p. 6) ✓; DALY climate change CSS 0=6,32×10⁻⁵ / CSS 4/8=6,29×10⁻⁵ / CSS 8/16=6,29×10⁻⁵ / CSS 4/16=6,24×10⁻⁵ (Tab. 6, p. 13) ✓.

### 162. VAN LOON et al., 2019 — 9 OK

Sem inconsistências. Vigas pré-fabricadas com cavidade + reforço FRP (carbono, vidro, linho, juta, cânhamo, kenaf). ISO 14040 genuinamente NÃO encontrada no PDF — célula correta ao informar "Não" ✓; método MPG holandês de custo-sombra (Vogtländer + TU Delft) com 11 categorias CML (p. 3, Tab. 1) ✓; cradle-to-gate (p. 6) ✓; C60/75 e C70/85 confirmados (Tab. 3, p. 7) ✓; UF viga 7,2 m (p. 3, Tab. 4) ✓; custo-sombra RC=151,98 / FRP carbono=162,64 / linho −39% / juta=171,28 / cânhamo=300,53 / kenaf=97,25 €/viga (Tab. 4, p. 7-8) ✓.

### 163. VENTURA et al., 2022 — 9 OK

Sem inconsistências. Placas cimentícias com tecidos não-tecidos de resíduos têxteis técnicos (TTW, aramida) e de moda (FTW). ISO 14040 + 14044 citadas na PDF p. 3 ✓ + refs p. 14; SimaPro 9.1.0.11 + Ecoinvent v3.6 + ReCiPe 2016 v1.1 midpoint H (p. 3, 6, 9) ✓; cradle-to-gate cut-off para fibras recicladas (p. 1, 3, 5, Fig. 6) ✓; envelhecimento wet/dry, MOR ~15 MPa, toughness ~3,5 kJ/m² (Tab. 3) ✓; FUs duplas (1 m² fachada com/sem requisito mecânico) (p. 3-4) ✓; impactos relativos discutidos (p. 10, sec. 3.2.3) ✓.

### 164. VIDAL et al., 2019 — 9 OK

Sem inconsistências. Edifício 4 pavimentos CLT residencial. ISO 14040:2006 e 14044:2006 citadas na PDF p. 10 (refs 35, 36) ✓ e também na PDF p. 2 (corpo) ✓; vida útil 50 anos ETA-06/0138 (p. 4) ✓; Ecoinvent 3.0 + EPDs (KLH/lã de rocha/alumínio) + CML-IA baseline v3.02 + CED v1.09 (p. 4) ✓; cradle-to-grave A+B+C com 5 cenários Sc1-Sc5 (p. 3-4) ✓; UF 1 m² GFA × 50 anos (p. 4) ✓; GWP Sc1=652 kg CO₂eq/m² GFA; sequestro CO₂ 1,85 kg/kg madeira seca; energia embutida 10.391 MJ/m² (37%) e total 27.728 MJ/m² (554,6 MJ/m²·ano); redução máx Sc4 = 7,1% ✓.

### 165. VITIELLO et al., 2016 — 9 OK

Sem inconsistências. Edifício CA Nápoles anos 70 (870 m²) com 4 estratégias de retrofit sísmico. ISO 14040 + 14044 citadas na PDF p. 3 (refs 44, 45) e p. 4 ✓ + refs p. 17; SimaPro 7.3 + Ecoinvent 2.2 + IMPACT 2002+ midpoints (p. 9, 15) ✓; fck=15 MPa, fym=220 MPa (PDF p. 2, 5, 7) ✓; cradle-to-gate (p. 5, 8, 9) ✓; UF reforço completo para PGA=0,168 g, retorno 475 anos (p. 8) ✓; resultados em % relativos por categoria IMPACT 2002+ (paredes de corte CA = maior; isolamento de base = menor em todas as 4 categorias) ✓.

### 166. VLADIMIROV et al., 2019 — 8 OK · 1 MENOR

- **MENOR — Usou Norma ISO 14040?** (cita p. 6): ISO 14044 e ISO/TR 14049 estão citadas como refs 12 e 13, mas na lista de referências na PDF p. 7 (não p. 6 como na célula). ISO 14044 também aparece explicitamente no corpo da PDF p. 2: *"definition of the model per EN 15804, ISO 14044 and..."*. **Sugestão:** atualizar para `(p. 2, refs p. 7)`.

Demais células OK: 1 m de tubo GRP DN 1000, PN 1, SN 10000 (p. 4-5) ✓; RR=95%, RC=5%, calorific 12 MJ/kg ✓; Umberto NXT LCA + Ecoinvent v2.2 + EN 15804 Módulo D (0:100) + PEF (50:50) (p. 4-5) ✓; A1-A3+C2-C4+Módulo D (p. 4-5) ✓; GWP 100a = 1,09 kg CO₂eq/kg; AP=3,35E-03 kg SO₂eq/kg; EP=9,17E-04 kg PO₄eq/kg; energia não-renovável 21,7 MJ-eq/kg ✓.

### 167. VOLK et al., 2023 — 9 OK

Sem inconsistências. AAC pós-demolição (pd-AAC) com abordagem zero-burden. ISO 14040 e 14044 citadas na PDF p. 3 (formatadas como "ISO 14,040" e "ISO 14,044") ✓; openLCA + Ecoinvent 3.6 + ILCD 2.0 2018 midpoint (p. 4) ✓; 3 classes AAC-0.35/0.50/0.70 ✓; C25/30 fck=25/fcm=30 MPa referência Gyurko 2019 (p. 4) ✓; UF 1 kg pd-AAC (p. 3) ✓; aterro ~0,01 kg CO₂eq/kg; melhor opção AAC-0.35 7% economia 0,49-0,50 kg CO₂eq/kg ✓; trituração via Ecoinvent rock crushing + waste brick sorting (proxy) ✓.

### 168. WOLFOVA et al., 2020 — 9 OK

Sem inconsistências. Parede A (tijolo cerâmico) vs. Parede B (concreto celular AAC). ISO 14040 e 14044 são a ref. [7] do artigo — *"International Organization for Standardization 2006 Environmental Management: Life Cycle Assessment; Principles and Framework No. 2006"* — confirmado na lista de referências PDF p. 6; o título corresponde exatamente à ISO 14040:2006 mesmo sem o número impresso ✓; vida útil 50 anos núcleo / 25 anos rebocos (p. 3) ✓; SimaPro + Ecoinvent + CED com 8 subcategorias (p. 2-3) ✓; cradle-to-gate (p. 3) + cradle-to-grave discutido em conclusão (p. 5) ✓; UF 1 m² (p. 3) ✓; CED Parede A não-renovável fossil=1448,59 MJ vs. Parede B=994,34 MJ confirmados ✓.

### 169. XIAO et al., 2014 — 9 OK

Sem inconsistências. Carbonatação acelerada de escórias BOFS/SCS/BHC em 6 cenários (autoclave/RPB/slurry, direta/indireta). ISO 14040:1997 explicitamente citada na PDF p. 2 ✓ (também p. 4 — célula info ✓); Umberto 5.5.4 + Eco-invent 2.2 + ReCiPe 18 midpoints + GWP/EQP/HHP endpoints (p. 1-2, 4) ✓; UF 1 kg CO₂ capturado (p. 4) ✓; GWP cenários: Sc1 (autoclave BHC) ~70 / Sc2 (slurry BOFS) ~7 / Sc3 (RPB BOFS) ~14 / Sc5,6 (indireta) 3,86 e 3,89 kg CO₂eq/kg CO₂ ✓; mínimo Sc2 a 90% eficiência aquecimento = 1,21 kg CO₂eq/kg CO₂ ✓.

### 170. YU et al., 2023 — 9 OK

Sem inconsistências. Solo mole estabilizado com cimento + escória de aço (S-CSS/FSS/FSS-C-2h/FSS-C-18h) em 10/20/30/50% substituição. ISO 14040:2006 citada na PDF p. 3, 6-7 ✓ + refs p. 19 (cell info "p. 6-7 ref. 36" ✓); Protégé OWL-5.2 + SWRL + Pellet + ICE database (Jones 2023) + GB/T 51366-2019 (p. 2, 4, 6-8) ✓; cradle-to-gate A1-A3 (p. 2-3, Fig. 1) ✓; UF cimento+escória para 1 m³ solo, 15% massa seca (p. 2-3) ✓; UCS60d S-C=2.070,2 kPa; melhor S-FSS-C-18h-10=2.267,32 kPa (+10%); requisito GJ/T 526-2018: 1.000 kPa (Tab. 7, p. 10-15) ✓; reduções GWP -10,4%/-20,4%/-48,1% para 10/20/50% FSS-C-18h ✓; carbono negativo FSS-C-18h=-1,6205 kg CO₂eq/FU ✓.

### 171. ZHANG et al., 2023 — 8 OK · 1 MAIOR

- **MAIOR — Usou Norma ISO 14040?** (cita "Não"): a célula classifica como "Não", mas a PDF p. 3 contém citação explícita no corpo do texto: *"The LCA procedure described in ISO 14040 [13] was..."*; a referência [13] aparece na lista de referências PDF p. 19. **Sugestão:** alterar para `Sim — ISO 14040 explicitamente citada como procedimento metodológico de ACV (p. 3); ref. 13 na lista de referências (p. 19)`.

Demais células OK: edifício residencial pré-fabricado Xangai ✓; C40 (p. 3) ✓; CLCD + IPCC 2013 GWP 100a (p. 3) ✓; A1-A3+A1P-A3P+A4+A5+B6+B2+C1-C4 (p. 2) ✓; UF 1 m² GFA × 50 anos (p. 2) ✓; total 1196,11 kg CO₂eq/m² em 50 anos; A1-A3=202,87 / A1P-A3P=57,88 / A4=12,34 / A5=18,76 / B6=940,72 (78,7%) / B2=24,54 / C1-C4=-60,00 — confirmados (p. 4) ✓.

### 172. ZHAO et al., 2020 — 9 OK

Sem inconsistências. Blocos de concreto com RCA (0/30/100%), cimento CEM III/A 42,5 N LA, Bélgica. ISO 14040:2006 e ISO 14044:2006 citadas explicitamente na PDF p. 14 — *"The present LCA was conducted in accordance with ISO 14040:2006 (ISO, 2006a) and 14044:2006 standards"* ✓ + refs p. 31; SimaPro 9.0 + Ecoinvent 3.5 + ILCD 2011 Midpoint+ v1.10 ✓; cradle-to-gate (p. 2, 15, 29) ✓; UF 1 m³ blocos / ciclo anual (p. 15) ✓; PTV 21-001 classe f10 (>=10 MPa); B_RCA100 fbm=11,1/12,7 MPa (28/360d) e normalizado 13 MPa (PDF p. 1-2, 8, 21-22, 28-29) ✓; GWP 109/108/108 kg CO₂eq/m³ — diferenças não significativas (cimento mantido constante); benefício maior em uso do solo (-53,1% B_RCA100) ✓.

### 173. ZHENG et al., 2025 — 9 OK

Sem inconsistências. Dois edifícios CA (alto-padrão e médio) em Nanjing. ISO 14040 citada na PDF p. 7 ✓ + refs p. 20; concreto C30/C35/C40 (p. 3) ✓; DeST + CLCD + GB/T 51366-2019 + IPCC 2021 GWP 100a (p. 3) ✓; cradle-to-grave A1-A3+A4-A5+B1-B7+C1-C4 (p. 2) ✓; vida útil 50 anos (p. 2) ✓; UF 1 m² × 50 anos (p. 2) ✓; Caso 1: total 857,6 kg CO₂eq/m²; A1-A3=258,7 (30,2%) / A4-A5=18,5 / B1-B7=564,1 (65,8%) / C1-C4=16,3 ✓; Caso 2: total 792,5; A1-A3=241,3 (30,5%) / A4-A5=15,2 / B1-B7=493,8 (62,3%) / C1-C4=42,2 ✓.

---

## Conclusão da auditoria

**Auditoria 100% concluída em 2026-05-15.** Total de 173 artigos × 9 colunas = 1.557 células verificadas contra os PDFs (algumas com escopo reduzido pelos motivos documentados nas entradas com nota CRÍTICO ou casos atípicos).

### Resumo final
- **OK total:** ~1.529 células (~98,2%)
- **MENOR:** 17
- **MAIOR:** 15
- **CRÍTICO:** 2 (MING/DING 2024 — identificação errada do PDF)
- **FALTANTE:** 0

### Padrão recorrente confirmado
O erro mais frequente foi a classificação errônea de ISO 14040 como "Não citada" quando a norma está, na realidade, presente no PDF. Casos identificados: MALABI EBERHARDT 2024 (#21), SIKORA 2023 (#36), VOLK 2024 (#56), UGURAL 2024 (#160), VACLAVIK 2020 (#161), ZHANG 2023 (#171). Recomenda-se uma passada final no banco focada apenas nessa coluna com grep automatizado sobre os 173 PDFs.

### Padrão secundário — formatação pypdf
Em vários PDFs (RUIZ SANCHEZ 2021, SBAHIEH 2022, SANTOS 2022, PAVLU 2019, VOLK 2023), a extração de texto via pypdf formata "ISO 14040" como "ISO 14,040" (vírgula em vez de espaço). Buscas devem incluir essa variante para evitar falsos negativos.
