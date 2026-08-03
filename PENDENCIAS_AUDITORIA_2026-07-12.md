---
titulo: Pendências da auditoria de 12/07/2026
descricao: Lista de itens a resolver, um a um, encontrados na auditoria profunda do funil C1-C8 do articles_final.xlsx
tags: [academico-e-pesquisa, revisao-sistematica, auditoria]
status: em-andamento
ultima_atualizacao: 2026-07-12
---

# Pendências da auditoria de 12/07/2026

> Gerado a partir de auditoria programática do `articles_final.xlsx` (5.093 linhas), pedida pela Kiê após lembrar de um alerta de PDFs faltando/análises incorretas em um dispatch anterior. Nada foi corrigido ainda — resolver **um item por vez**, marcando `[x]` conforme for fechado. Ver conversa de 12/07/2026 para o relatório completo de cada achado.

## Achado-chave: há atividade não documentada

`articles_final.xlsx` foi modificado em 23/06/2026 às 21:33, um dia depois da última atualização do `RSL_PROGRESSO.md`/`CLAUDE.md` (22/06 00:16). Alguém (provavelmente o dispatch que a Kiê lembra) reabriu casos e baixou PDFs nesse intervalo sem documentar nada. Os itens 3, 4 e 6 abaixo são consequência direta disso.

## Itens a resolver (ordem sugerida)

- [x] **1. Fechar C2 nas 51 linhas pendentes.** RESOLVIDO 2026-07-23 (lote original de 51 + reabertura pavimento/kerb + os 6 rows sem material-alvo próprio, decididos por potencial de fonte externa). 51 linhas com status Inconclusivo nunca receberam decisão em C2, mas várias já têm C4/C5/C6/C8 preenchidos (violação da ordem de cascata). Lista completa de rows disponível no histórico da auditoria (ex.: 3742, 3772, 3780, 3796, 3849, 3888, 3918, 3974, 3994, 4134, 4153, 4158, 4230, 4236, 4242, 4245, 4248, 4295, 4320, 4322, 4331, 4382, 4404, 4413, 4431, 4437, 4544, 4609, 4646, 4652, 4694, 4725, 4726, 4735, entre outras — a maioria parece claramente sobre LCA de edifícios/pontes/concreto pelo título).

- [x] **2. Padronizar as 36 células C8 sem prefixo `R:`/`P:`.** RESOLVIDO 2026-07-23: 31 células corrigidas para `R:Aceito`/`R:Rejeitado` (decisão por metadado/resumo, conforme regra do C8). 3907 já tinha sido resolvida no item 1 (C3 Rejeitado, C8 limpo). Restam 3941/4004/4436 — tratadas no item 3 (cascata completa). Formato inválido (ex.: `Aceito` puro em vez de `R:Aceito`/`P:Aceito`). Rows incluem: 2722, 2839, 2897, 2930, 2976, 3076, 3145, 3228, 3266, 3290, 3323, 3428, 3490, 3553, 3640, 3746, 3907, 3941, 3944, 3945, 3969, 3988, 4001, 4004, 4008, 4203, 4205, 4264, 4313, 4343, 4436, 4514, 4761, 5004, 5005 (+1). Decidir se cada uma foi de fato avaliada por resumo (`R:`) ou por PDF (`P:`) e reescrever.

- [x] **3. Resolver o cluster 3941 / 4004 / 4436 (cascata quebrada + referência cruzada errada).** RESOLVIDO 2026-07-23: confirmado que não são duplicatas de L4005/L4437. 3941 (McGrath) e 4436 (Kushima) — cascata completa refeita por leitura integral do PDF, ambos Elegível. 4004 (Muazu) — órfãos de cascata (C5/C8) limpos, mantido Rejeitado (C2). McGrath 2013 (retrofit), Muazu 2022 (briquetagem de biomassa) e Kushima 2019 (bibliometria) têm C2/C3/C4 em branco mas já "C8 Aceito" malformado. Os comentários pedem verificar se são duplicatas de L4005/L4437 — **já confirmei que não são** (essas linhas hoje são artigos completamente diferentes: Steel-Concrete Composite Bridges e Carbon Emission Factors Railway). Precisam da cascata completa refeita do zero (C2→C8).

- [x] **4. Vincular/mover os 6 PDFs soltos na raiz do vault.** RESOLVIDO 2026-07-23: verificado que todos os 6 já estão na pasta correta e vinculados (nenhum solto na raiz). Pretot (item da linha 3640, hemp concrete wall) confirmado como a linha "viva" reaberta. Baixados em 22-23/06, violam a convenção (deveriam estar em `00_REFERENCIAS/ARTIGOS ACEITOS APÓS REMOÇÃO DAS DUPLICATAS/`) e não estão linkados na coluna `pdf`:
  - `AREHART et al., 2020.pdf` → linha 4515 (Elegível, hempcrete — já tem decisões P:Aceito em C3-C6-C8, só falta o arquivo)
  - `KUSHIMA et al., 2019.pdf` → linha 4436 (ver item 3)
  - `MUAZU et al., 2022.pdf` → linha 4004 (ver item 3)
  - `McGRATH et al., 2013.pdf` → linha 3941 (ver item 3)
  - `ROMANOV et al., 2015.pdf` → linha 2876 (ver item 5)
  - `PRETOT et al., 2014.pdf` → hemp concrete wall — as 3 linhas desse artigo (121, 2209, 3640) estão todas marcadas Duplicado; nenhuma ficou "viva" para receber o PDF. Precisa decidir qual linha reabrir.

- [x] **5. Reavaliar linha 2876 (Romanov, "Mineralization of CO2").** RESOLVIDO 2026-07-23: confirmado C2 Rejeitado (revisão genérica de CCS/mineralização geológica; menções a concreto/cimento só na lista de referências). Órfão C5 limpo. Mantido Rejeitado. Status = Sem acesso, mas o PDF já foi baixado (item 4). Reabrir e retomar a triagem.

- [ ] **6. Reavaliar linha 2897 (di Summa, LCA/LCC de UHPC).** Documentado como resolvido/Rejeitado em 21/06, mas hoje está com status Inconclusivo e um comentário não-documentado dizendo "ARTIGO ALTAMENTE RELEVANTE... PDF necessário urgente". Decidir se busca o PDF (DOI 10.1002/suco.202300645, Wiley) ou mantém rejeitado.

- [ ] **7. Investigar linha 3729 (comentário trocado).** Título real = "Template for Evaluating Cradle-to-Site Environmental LCA of Buildings in India". C2 = `P:Rejeitado` com justificativa de OUTRO artigo (zeólitos/hidrocracking de plástico), enquanto C3-C6 têm justificativas corretas e "Aceito". Status ainda "Elegível". Provável erro de copiar/colar entre linhas — decidir o C2 correto e limpar o comentário.

- [ ] **8. Decidir o destino das 109 linhas com C1-C6 Aceito mas C8 nunca avaliado** (106 Inconclusivo + 3 Elegível). O funil documentado como "1.337 aprovados" na prática só tem 1.293 com tudo Aceito — essas 109 explicam boa parte da diferença e precisam passar pelo C8.

- [ ] **9. Verificar as 6 linhas "Sem acesso" que já têm um PDF na coluna `pdf`** (arquivo existe fisicamente): 3137 (YORIS-NOBILE, 2023), 3262 (COLLOTTA, 2016), 3481 (SALARIPOOR, 2025), 3977 (KLOTZ, 2023), 4058 (EMMANUEL, 2020), 4919 (ELGINOZ, 2019). Status provavelmente desatualizado — conferir e reabrir se o PDF for válido.

- [ ] **10. Limpar os 596 valores residuais em C7** (maioria `R:Aceito`) que sobraram da remoção do critério em 22/06 — só os 200 `P:Aceito` do Lote 1 foram apagados. Não afeta o funil, mas deixa a planilha inconsistente com a documentação.

---

## Lista de artigos "Sem acesso" para baixar via Sci-Hub (68 no total)

> 6 destes já têm um PDF na pasta (marcados abaixo com ✅ — ver item 9 antes de baixar de novo, pode já estar resolvido). Os demais 62 seguem sem PDF algum.

| Row | Título | Autor(es) | Ano | DOI | Link/nota |
|---|---|---|---|---|---|
| 2852 | An integrated life cycle assessment and life cycle analysis model for pavement overlay systems | Zhang, Keoleian, Lepech | 2008 | — | Taylor & Francis |
| 2873 | Environmental impacts of natural and conventional building materials: earth vs. concrete | Melia, Ruggieri, Sabbadini et al. | 2014 | — | dx.doi.org/10.1016/j.jclepro.2014.05.073 |
| 2875 | LCA of concrete made of 100% recycled aggregate compared to normal concrete | Stengel, Kustermann | 2024 | 10.1002/best.202400043 | doi.org/10.1002/best.202400043 |
| 2876 | Mineralization of Carbon Dioxide: A Literature Review | Romanov, Soong, Carney et al. | 2015 | 10.1002/cben.201500002 | ✅ já tem PDF (ver item 5) |
| 2882 | Seismic damage accumulation in multiple mainshock–aftershock sequences | Iervolino, Chioccarelli, Suzuki | 2020 | — | dx.doi.org/10.1002/eqe.3275 |
| 2898 | Valuing the manufacturing externalities of wind energy | Sovacool, Perea Mata et al. | 2016 | 10.1002/we.1941 | doi.org/10.1002/we.1941 |
| 3031 | Comparative life cycle assessment of four buildings in Greenland | Ryberg, Ohms, Møller et al. | 2021 | 10.1016/j.buildenv.2021.108130 | sciencedirect.com/science/article/pii/S036013232100531X |
| 3049 | Integrated calcium looping technologies for enhanced CO2 valorisation — a critical review | Kumari, Al Amoodi, Dumée | 2025 | 10.1016/j.ccst.2025.100371 | scopus eid 2-s2.0-85215441135 |
| 3056 | A plant based LCA of high-strength prestressed concrete elements | Dossche, Boel, De Corte et al. | 2016 | — | dx.doi.org/10.1016/j.cemconcomp.2016.07.011 |
| 3070 | Co-calcination to produce a synergistic blend of bauxite residue and low-grade kaolinitic clay | Peys, Preveniou, Konlechner et al. | 2024 | 10.1016/j.cement.2024.100122 | sciencedirect.com/science/article/pii/S2666549224000318 |
| 3082 | Life cycle assessment of a point absorber wave energy converter | Engelfried, Cucurachi, Lavidas | 2025 | — | dx.doi.org/10.1016/j.cesys.2025.100265 |
| 3133 | Circular economy in wood construction — additive manufacturing of fully recyclable walls | Kromoser, Reichenbach, Hellmayr, Myna | 2022 | 10.1016/j.conbuildmat.2022.128219 | — |
| 3137 | Artificial reefs built by 3D printing: systematisation in design, material selection | Yoris-Nobile, Slebi-Acevedo, Lizasoain et al. | 2023 | 10.1016/j.conbuildmat.2022.129766 | ✅ já tem PDF (ver item 9) |
| 3258 | Evaluation of Carbon Dioxide Utilisation Concepts: a quick and complete methodology | Engebø, Ahmed, Bureau-Cauchois | 2014 | — | sciencedirect.com/science/article/pii/S1876610214026526 |
| 3262 | Environmental assessment of co-location alternatives for a microalgae cultivation plant | Collotta, Champagne, Mabee et al. | 2016 | — | dx.doi.org/10.1016/j.egypro.2016.09.007 — ✅ já tem PDF (ver item 9) |
| 3398 | Stabilisation for peat improvement: extent of carbonation and environmental implications | Duggan, McCabe, Goggins et al. | 2020 | — | dx.doi.org/10.1016/j.jclepro.2020.122540 |
| 3458 | Advancing railway sustainability: strategic integration of circular economy principles | Koohmishi, Kaewunruen, He, Guo | 2025 | 10.1016/j.jclepro.2025.144713 | — |
| 3480 | LCA and the influence of alkaline activator content on mechanical properties | Gopalakrishna, Dinakar | 2024 | 10.1016/j.jer.2024.01.010 | sciencedirect.com/science/article/pii/S2307187724000105 |
| 3481 | Life cycle environmental assessment of Refuse-Derived Fuel (RDF) as alternative to fossil fuel | Salaripoor, Yousefi, Abdoos | 2025 | 10.1016/j.jfueco.2025.100135 | ✅ já tem PDF (ver item 9) |
| 3529 | Comprehensive assessment of mechanical and environmental properties of waste basalt powder | Çelikten, Baran | 2024 | 10.1016/j.nxmate.2024.100273 | sciencedirect.com/science/article/pii/S2949822824001709 |
| 3554 | Life Cycle Assessment of Reusing Fly Ash from Municipal Solid Waste Incineration | Huang, Chuieh | 2015 | 10.1016/j.proeng.2015.08.539 | sciencedirect.com/science/article/pii/S1877705815021943 |
| 3567 | Revealing the impact of a projected emission trading scheme on production technology | Ju, Fujikawa | 2019 | — | dx.doi.org/10.1016/j.rcrx.2019.100019 |
| 3618 | Integrating circular economy principles into concrete technology | Oyejobi, Firoozi, Blanco Fernández et al. | 2024 | 10.1016/j.rineng.2024.102846 | sciencedirect.com/science/article/pii/S2590123024011010 |
| 3684 | LCA study of UK decarbonised ammonia, cement, methanol and steel | Cooper, Hawkes | 2025 | 10.1016/j.spc.2025.04.005 | sciencedirect.com/science/article/pii/S235255092500079X |
| 3697 | Life cycle analysis of innovative building materials based on circular coffee ground | Adelfio, La Scalia, La Scalia | 2022 | 10.1016/j.trpro.2022.12.040 | sciencedirect.com/science/article/pii/S2352146522007670 |
| 3698 | Evaluation of greenhouse gas emissions in subway tunnel construction | Guo, Dong, Chen, Zhao et al. | 2025 | 10.1016/j.undsp.2024.12.001 | sciencedirect.com/science/article/pii/S2467967425000121 |
| 3728 | Pore-structure engineering of hierarchical β zeolites for enhanced hydrocracking | Azam, Fernandes, Ferreira et al. | 2024 | — | dx.doi.org/10.1021/acscatal.4c05354 (⚠️ este é o artigo que aparece incorretamente citado na linha 3729 — ver item 7) |
| 3759 | Environmental impacts and decarbonization strategies in the cement and concrete industries | Habert, Miller, John, Provis et al. | 2020 | 10.1038/s43017-020-0093-3 | doi.org/10.1038/s43017-020-0093-3 |
| 3788 | A stochastic formulation to assess environmental impact of life-cycle of engineering structures | Lanza, Gardoni, Giresini, Sassu | 2022 | 10.1061/(ASCE)ST.1943-541X.0003201 | doi.org/10.1061/(ASCE)ST.1943-541X.0003201 |
| 3793 | Conceptual model-based design and environmental evaluation of waste solvent technologies | Amelio, Figueroa Paredes, D. et al. | 2018 | 10.1080/01496395.2018.1442858 | — |
| 3811 | The use of a credibility index in the life-cycle assessment of structures | Garavaglia, Sgambi | 2015 | 10.1080/15732479.2014.896022 | doi.org/10.1080/15732479.2014.896022 |
| 3812 | Climate impacts from road bridges: concrete carbonation and biogenic carbon | Penaloza, Erlandsson, Pousette | 2018 | 10.1080/15732479.2017.1327545 | doi.org/10.1080/15732479.2017.1327545 |
| 3813 | On the robustness to corrosion in the LCA of an existing reinforced concrete structure | Cavaco, Neves, Casas | 2018 | 10.1080/15732479.2017.1333128 | — |
| 3815 | Cost and environmental analyses of reinforcement alternatives for a concrete bridge | Cadenazzi, Dotelli, Rossini et al. | 2020 | 10.1080/15732479.2019.1662066 | — |
| 3820 | An assessment of GHG emissions from CLT and glulam in two residential nZEB buildings | Lolli, Fufa, Kjendseth Wiik | 2019 | — | doi.org/10.1080/17480272.2019.1655792 |
| 3826 | Sources of uncertainties for total chloride profile measurements in concrete | Bonnet, Schoefs, Salta | 2020 | 10.1080/19648189.2017.1375997 | — |
| 3832 | LCA and MCDM analysis for artificial reef material selection | Yoris-Nobile, Lizasoain-Arteaga, Slebi-Acevedo et al. | 2023 | 10.1080/21650373.2022.2099479 | doi.org/10.1080/21650373.2022.2099479 |
| 3912 | Carbon footprint of construction using industrialised building system | Lim, Yahya, Aminudin, Zakaria | 2017 | — | dx.doi.org/10.1088/1757-899X/271/1/012107 |
| 3920 | Assessment of the time-dependent behaviour of a reinforced concrete water tank | Filip, Covatariu | 2019 | — | dx.doi.org/10.1088/1757-899X/586/1/012021 |
| 3934 | Comparative analysis of cement-based bricks in India: cradle-to-gate LCA | Sravani, Ramani, Anbu et al. | 2024 | 10.1088/2631-8695/ad3401 | doi.org/10.1088/2631-8695/ad3401 |
| 3955 | Multi-objective building envelope optimization through an LCA approach | Cellura, Longo, Montana et al. | 2019 | — | dx.doi.org/10.1109/EEEIC.2019.8783807 |
| 3957 | Probabilistic design of sustainable reinforced concrete infrastructure repairs using SIPMath | Zirps, Lepech, Savage | 2019 | — | doi.org/10.1109/wsc40007.2019.9004951 |
| 3961 | Net climate impacts of forest biomass production and utilization in managed boreal forests | Kilpelainen, Torssonen, Strandman et al. | 2016 | 10.1111/gcbb.12243 | doi.org/10.1111/gcbb.12243 |
| 3963 | Dynamic modeling of in-use cement stocks in the United States | Kapur, Keoleian, Kendall et al. | 2008 | 10.1111/j.1530-9290.2008.00055.x | doi.org/10.1111/j.1530-9290.2008.00055.x |
| 3972 | Design of concrete: setting a new basis for improving durability and environmental performance | Ventura, Ta, Kiesse Senga et al. | 2021 | 10.1111/jiec.13059 | doi.org/10.1111/jiec.13059 |
| 3977 | Potentials and limits of mechanical plastic recycling | Klotz, Haupt, Hellweg | 2023 | 10.1111/jiec.13393 | ✅ já tem PDF (ver item 9) |
| 4016 | Environmental assessment of waste-solvent treatment options. Part I: ecosolvent tool | Capello, Hellweg, Badertscher | 2007 | 10.1162/jiec.2007.1231 | scopus eid 2-s2.0-36849079780 |
| 4024 | The estimated carbon cost of concrete building demolitions after Canterbury earthquake | Gonzalez, Stephens, Toma et al. | 2022 | — | dx.doi.org/10.1177/87552930221082684 |
| 4034 | Re:Crete — reuse of concrete elements in new structures: a footbridge prototype | Brutting, Devenes, Kupfer, Bastien-Masse | 2022 | 10.1201/9781003023555-77 | — |
| 4049 | Climate change risks and climate adaptation engineering for built infrastructure | Stewart | 2015 | 10.1201/b17618-10 | scopus eid 2-s2.0-84941218835 |
| 4051 | Alternatives assessment frameworks: research needs for informed substitution of hazardous chemicals | Jacobs, Malloy, Tickner | 2016 | 10.1289/ehp.1409581 | doi.org/10.1289/ehp.1409581 |
| 4058 | Life cycle energy assessment (LCEA) approach for sustainable architecture | Emmanuel, Chukwuemeka, Kalu | 2020 | 10.13189/cea.2020.080505 | ✅ já tem PDF (ver item 9) |
| 4079 | Life-cycle cost and LCA at the design stage of a fiber-reinforced polymer bridge | Cadenazzi, Dotelli, Rossini et al. | 2019 | 10.1520/ACEM20180113 | — |
| 4116 | Future use of life-cycle assessment in civil engineering | Glass, Dyer, Georgopoulos et al. | 2013 | — | dx.doi.org/10.1680/coma.12.00037 |
| 4119 | A life cycle assessment of building demolition waste: a comparison study | Blay-Armah, Bahadori-Jahromi, Mylona | 2023 | — | dx.doi.org/10.1680/jwarm.22.00012 |
| 4120 | An LCA of building demolition waste: a comparison of end-of-life carbon emission | Blay-Armah, Bahadori-Jahromi, Mylona | 2023 | 10.1680/jwarm.22.00012 | — (⚠️ possível duplicata do 4119) |
| 4130 | LCA of wastewater treatment options for small and decentralized communities | Machado, Urbano, Brito, Janknecht | 2007 | 10.2166/wst.2007.497 | — |
| 4170 | A life-cycle analysis of a new Romanian automotive manufacturing battery | Ghenadi, Bibire, Topliceanu | 2011 | — | dx.doi.org/10.2507/22nd.daaam.proceedings.658 |
| 4183 | Comparative life cycle assessment of different recycled concrete aggregates | Doostdar, zum Brock, Ceraso et al. | 2023 | 10.31025/2611-4135/2023.18324 | — |
| 4888 | A review of the application of LCA for sustainable buildings in Asia | Abd Rashid, Yusoff, Mahat | 2013 | — | dx.doi.org/10.4028/www.scientific.net/AMR.724-725.1597 |
| 4919 | Construction of a large water treatment plant: appraisal of environmental hotspots | Elginoz, Alzaboot, Germirli Bahar | 2019 | 10.5004/dwt.2019.25107 | ✅ já tem PDF (ver item 9) |
| 4942 | LCA and mechanical strength of cement composites with conventional and alternative binders | Islam, Majumder, Mutsuddy | 2024 | 10.54113/j.sust.2024.000052 | scopus eid 2-s2.0-85204115207 |
| 4945 | LCA of timber Arch-Truss bridge using domestic Pinus rigida glued-laminated timber | Son, Park, Kim | 2014 | 10.5658/WOOD.2014.42.1.1 | koreascience.or.kr — servidor coreano inacessível |
| 5017 | Impactos ambientais da construção civil habitacional no Brasil à luz do ciclo de vida | Farias, E.E.V. de | 2022 | — | repositorio.uepb.edu.br/handle/123456789/72131 |
| 5029 | Metodologia para avaliação do ciclo de vida de ciclovias de pavimento rígido | Hora, K.M. da | 2021 | — | repositorio.unb.br/handle/10482/43688 |
| 5058 | Scenarios to valorize treated spent pot lining in cement and concrete | Camara, Ouellet-Plamondon | 2023 | — | dx.doi.org/10.1007/978-981-19-0507-0_23 |
| 5066 | Comparative assessment of insulated concrete wall technologies and wood-frame walls | Amiri Fard, Jafarpour, Nasiri | 2021 | — | dx.doi.org/10.1080/17512549.2019.1600583 |
| 5085 | Structural and environmental impact of new-generation wide-base tires in New Brunswick | Said, Hernandez, Kang et al. | 2020 | — | dx.doi.org/10.1080/14680629.2019.1590219 |

**Faltam na tabela acima** (não tinham DOI nem título claro suficiente para confirmar, conferir na planilha diretamente): nenhuma — todas as 68 linhas "Sem acesso" estão listadas.

---

*Nota criada em 2026-07-12 a partir de auditoria solicitada pela Kiê. Resolver item por item; atualizar esta nota e o RSL_PROGRESSO.md conforme cada pendência for fechada.*
