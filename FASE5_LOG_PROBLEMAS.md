---
titulo: Log de Problemas — Fase 5 (Extração de dados para Metanálise)
descricao: Registro em tempo real dos problemas identificados durante a extração de GWP/m³ e fck dos estudos incluídos na RSL (escore ≥ 4)
tags: [academico-e-pesquisa, meta-analise, revisao-sistematica, UHPC]
status: em-andamento
ultima_atualizacao: 2026-05-19
---

# LOG DE PROBLEMAS — FASE 5: Extração de dados dos PDFs para METANÁLISE

> Registro dos problemas identificados durante a extração de GWP/m³ e fck dos estudos incluídos na RSL (escore ≥ 4) ausentes da METANÁLISE.
> Atualizado em tempo real conforme análise avança.

---

## Categorias de problema

| Código | Descrição |
|--------|-----------|
| `UF-SISTEMA` | UF = sistema multi-componente (edifício, parede com isolamento, etc.) — GWP não isolável ao concreto |
| `UF-KG` | UF = kg de material — fora do escopo m³ |
| `UF-ELEMENTO` | UF = peça/elemento específico sem dimensões declaradas |
| `SEM-FCK` | fck não declarado ou não atribuível por traço |
| `GWP-FIGURA` | GWP reportado apenas em figuras, sem tabela de valores absolutos |
| `GWP-DATABASE` | GWP vem de banco de dados genérico (GaBI, One Click LCA), não de medição original |
| `GWP-ESCALA` | GWP reportado numa escala impossível para 1 m³ (erro de unidade, créditos de reciclagem) |
| `GWP-INVERTIDO` | Rankings de GWP inconsistentes com composição dos traços (indicativo de créditos/alocação especial) |

---

## Estudos INVIÁVEIS

### SESSÃO ANTERIOR (2026-05-18, primeira parte)

---

#### CUNHA, 2022
- **Linha ANÁLISE:** 83
- **Códigos:** `GWP-ESCALA` `GWP-INVERTIDO`
- **UF declarada:** 1 m³ de concreto (p. 63)
- **Dados extraídos:**
  - Tabela 4.6 (p. 69): quantidades por m³ — CONREF00: cimento=283 kg, brita=1075 kg, areia=929 kg, água=181 kg
  - Tabela 5.2 (p. 94): GWP unitário — cimento=0,927; brita=0,0163; areia=0,0129; RCA=0,0115 kg CO₂eq/kg
  - Figura 5.11 (p. 90): CONREF00 = 43.700 kg CO₂eq — reportado como referência ao estudo
- **Problema:** GWP reportado ~150× maior que o calculável pela composição declarada (CONREF00 reconstruído ≈ 292 kg CO₂eq/m³ vs. Figura 5.11 = 43.700 kg CO₂eq). Fator de escala inconsistente entre traços (80–150×). Rankings invertidos: Figura 5.11 mostra CONARM25 < CONREF00, mas cálculo pela composição dá CONARM25 > CONREF00 (mais cimento). Provável causa: créditos de sistema de expansão no SimaPro por reciclagem de agregado, mas não explicitados.
- **Decisão:** INVIÁVEL — GWP não utilizável; ci não calculável com confiança.

---

#### GANAPATHI CHOTTEMADA et al., 2023
- **Linha ANÁLISE:** 13
- **Códigos:** `SEM-FCK` `GWP-FIGURA`
- **UF declarada:** 1 m³ (p. 7, cradle-to-gate)
- **Dados extraídos:**
  - Tabela 2 (p. 6): composições em kg/m³ — S100 (GGBS=450), FS70 (GGBS=315+FA=135), FS50 (GGBS=225+FA=225), PCC (CP=450); agregados iguais para todos
  - Tabela 5 (pp. 10–11): GWP unitário por constituinte (FA=0; GGBS=0,101; CP=0,885; silicato sódio=0,828; hidróxido sódio=1,315 kg CO₂eq/kg)
  - Resultados de GWP: apenas figuras normalizadas em % — sem valor absoluto por traço em tabela
- **Problema:** fck declarado apenas como range "35 a 55 MPa" para todos os traços conjuntamente, sem valor individual por traço. GWP absoluto (kg CO₂eq/m³) não tabelas — apenas gráficos normalizados em %.
- **Decisão:** INVIÁVEL — ci não calculável sem fck por traço.

---

#### KIM et al., 2016
- **Linha ANÁLISE:** 105
- **Códigos:** `GWP-FIGURA` `SEM-FCK`
- **UF declarada:** 1 m³ (p. 2)
- **Dados extraídos:**
  - ~1000 traços de concreto coreano, resistência 18–80 MPa
  - Tabela 2 (p. 4): GWP unitário — cimento=9,48E-01; areia fina=1,49E-03; cinza volante=1,50E-02; água=1,14E-01 kg CO₂eq/kg
  - Resultados: Figuras 4–6 apenas (dispersão GWP vs. fck) — conclusão comparativa ("13% menor ci para 60 MPa vs. 24 MPa")
- **Problema:** Nenhuma tabela com GWP absoluto por traço ou por classe de resistência. Estudo de tendência de banco de dados; não fornece pares (GWP; fck) extraíveis por formulação.
- **Decisão:** INVIÁVEL — GWP por traço não disponível em formato tabular.

---

#### ONN et al.
- **Linha ANÁLISE:** 131
- **Códigos:** `UF-SISTEMA`
- **Problema:** Material não estrutural — fora do escopo do estudo.
- **Decisão:** INVIÁVEL.

---

#### BILAR et al.
- **Linha ANÁLISE:** 6
- **Códigos:** `SEM-FCK` `UF-SISTEMA`
- **Problema:** fck máximo 6 MPa — material não estrutural.
- **Decisão:** INVIÁVEL.

---

#### VENTURA et al.
- **Linha ANÁLISE:** 164
- **Códigos:** `SEM-FCK`
- **Problema:** fck não declarado.
- **Decisão:** INVIÁVEL.

---

#### VIDAL et al.
- **Linha ANÁLISE:** 165
- **Códigos:** `SEM-FCK`
- **Problema:** fck não declarado.
- **Decisão:** INVIÁVEL.

---

#### VOLK, 2023
- **Linha ANÁLISE:** 168
- **Códigos:** `UF-KG`
- **Problema:** UF = kg de material — fora do escopo m³.
- **Decisão:** INVIÁVEL.

---

#### INMAN et al.
- **Linha ANÁLISE:** 48
- **Códigos:** `UF-KG`
- **Problema:** UF = kg de material — fora do escopo m³.
- **Decisão:** INVIÁVEL.

---

#### KASTIUKAS et al., 2019
- **Linha ANÁLISE:** 17
- **Códigos:** `UF-KG`
- **Problema:** UF = kg de material — fora do escopo m³.
- **Decisão:** INVIÁVEL.

---

#### EK et al.
- **Linha ANÁLISE:** 11
- **Códigos:** `UF-ELEMENTO`
- **Problema:** UF = ponte/edifício completo como elemento — sem dimensões por componente ou m³ isolável.
- **Decisão:** INVIÁVEL.

---

### SESSÃO ATUAL (2026-05-18, segunda parte)

---

#### PESTA et al., 2020
- **Linha ANÁLISE:** 29
- **Códigos:** `UF-SISTEMA`
- **UF declarada:** 1 m² de parede construída com U=0,29 W/m²K
- **Dados extraídos:**
  - Tabela 1 (p. 4): traços por m³ — RMAC: cimento=320 kg/m³, ρ=1900 kg/m³, fck_medido=33,3 MPa (alvo C25/30); RCAC: cimento=320, ρ=2100, fck=35,4 MPa; NAC: cimento=300, ρ=2300, fck=31,2 MPa
  - Tabela 4 (p. 7): materiais por m² de parede — Plano 4 (parede convencional): cimento=84 kg, agregado=551 kg, lã mineral=5,2 kg, reboco=30 kg, água=42 kg → espessura ≈ 677/2300 ≈ 295 mm
  - Tabela 7 (p. 9, CML2001): GWP por m² — Plano 1 (RMAC)=106; Plano 2 (RCAC)=48,5; Plano 3 (NAC)=108; Plano 4=113 kg CO₂eq/m²
- **Problema:** GWP de 106–113 kg CO₂eq/m² inclui o sistema de parede completo: 130 mm de lã mineral de isolamento + caixilho de madeira + reboco + adesivo. Impossível isolar GWP exclusivo do concreto. fck IS declarado (33–35 MPa), mas sem GWP separado do concreto, ci não é calculável.
- **Decisão:** INVIÁVEL — sistema de parede multi-componente; GWP não isolável ao concreto.

---

#### FERREIRA et al., 2023
- **Linha ANÁLISE:** 12
- **Códigos:** `UF-SISTEMA` `SEM-FCK`
- **UF declarada:** 1 m² de área de vendas de edifício de varejo (ECI normalizado)
- **Dados extraídos:**
  - GWP total do shell = 1689 kg CO₂eq/m² (inclui concreto armado 72% em peso + aço + EPS + betume + lã de rocha)
  - GWP do concreto = 290 kg CO₂eq/m² (por m² de área de vendas) — mas inclui agregados e cimento sem separação de traço específico
  - Dois pisos de parque subterrâneo + laje do piso de vendas + estrutura de aço = múltiplos elementos de concreto agregados
  - Nenhum fck declarado para o concreto estrutural
- **Problema:** Estudo de caso de edifício de varejo completo (Portugal). UF = m² de área de vendas. GWP do concreto não é separável por elemento estrutural ou classe de resistência. Sem fck declarado por elemento.
- **Decisão:** INVIÁVEL — estudo edilício; sem fck; GWP do concreto não isolável por traço.

---

#### MATIAS DE PAULA FILHO et al., 2024
- **Linha ANÁLISE:** 123
- **Códigos:** `GWP-DATABASE` `UF-SISTEMA`
- **UF declarada:** m² de área bruta de piso (GFA) de edifício de escritórios 9 pavimentos, Luxemburgo
- **Dados extraídos:**
  - Tabela 7: GWP do concreto via One Click LCA — C30/37=270,88; C40/50=355,83; C50/60=429,00 kg CO₂eq/m³
  - Resultados por m² GFA: sistema estrutural aço-concreto vs. RC pré-fabricado vs. madeira
  - fck declarado: C30/37, C40/50, C50/60 (classes Eurocode)
- **Problema:** GWP do concreto provém de banco de dados comercial (One Click LCA, "internamente verificado") — não é inventário original do estudo. Os valores de 270–429 kg CO₂eq/m³ representam dados genéricos da plataforma, não uma ACV conduzida pelos autores para traços específicos. Estudo de comparação de sistemas estruturais de edifício, não de traços de concreto.
- **Nota:** Os valores absolutos (C30/37 = 270,88 kg CO₂eq/m³ etc.) são plausíveis e internamente consistentes, mas incluí-los seria equivalente a incluir dados do banco One Click LCA diretamente, não este artigo.
- **Decisão:** INVIÁVEL — dados de banco de dados genérico; sem inventário original; UF = m² GFA de edifício.

---

#### SOMBRIO, 2015
- **Linha ANÁLISE:** 40
- **Códigos:** `GWP-DATABASE`
- **UF declarada:** 1,312 m² de painel pré-fabricado (fração 1/5 do painel real)
- **Dados extraídos:**
  - Tabela 11 (p. 79): UF contém 9 blocos cerâmicos, 0,094 m³ de concreto C20, vergalhões de aço
  - Espessura do painel = 11 cm
  - Tabela 15 (p. 88): GWP total = 31,9 kg CO₂eq/UF; concreto = 22,5 kg CO₂eq (70,09%)
  - → GWP/m³ de concreto = 22,5/0,094 = **239 kg CO₂eq/m³** (fck=20 MPa, traço 1:3:3)
  - Tabela 33 (p. 109): análise de sensibilidade com dados de obra → GWP total = 40,03 kg CO₂eq (+20%) sem breakdown por material
- **Problema:** GWP do concreto (22,5 kg CO₂eq/m³) provém do banco de dados GaBI 6 alemão ("dado alemão"), não de medição original brasileira. A análise de sensibilidade com dados reais do canteiro de obras (traço 1:3:3 coletado in loco) fornece valor 20% maior mas sem separação por material — impossível isolar GWP real do concreto. ci calculável pelo GaBI, mas representaria banco de dados europeu genérico, não o concreto brasileiro real.
- **Nota:** É o único estudo nacional (BR) encontrado com dados completos de painel com concreto, porém a fragilidade do dado de GWP compromete a inclusão.
- **Decisão:** INVIÁVEL — GWP do concreto = dado GaBI alemão genérico; sensibilidade com dado real não isola concreto.

---

#### ZHANG et al., 2023
- **Linha ANÁLISE:** 172
- **Códigos:** `UF-SISTEMA`
- **UF declarada:** 1 kg de tijolo de alvenaria geopolimérico
- **Problema:** Produto = tijolo de alvenaria (não concreto estrutural). Escopo cradle-to-grave. O estudo reporta diretamente o índice de Damineli (ci), mas para um material não estrutural fora do escopo da RSL.
- **Decisão:** INVIÁVEL — material não estrutural; escopo cradle-to-grave.

---

#### MALABI EBERHARDT et al., 2020
- **Linha ANÁLISE:** 117
- **Códigos:** `UF-SISTEMA` `SEM-FCK`
- **Problema:** Estudo de metodologia de alocação em ACV de edifícios. UF = edifício completo; sem fck declarado por traço de concreto; GWP não isolável ao concreto.
- **Decisão:** INVIÁVEL — estudo edilício de nível de sistema; sem fck; GWP não isolável.

---

#### KUMAR et al., 2024b
- **Linha ANÁLISE:** 111
- **Códigos:** `UF-SISTEMA` `SEM-FCK`
- **Problema:** Estudo de caso de edifício residencial no Nepal. UF = edifício completo; GWP agregado de todos os materiais estruturais sem separação por traço de concreto; sem fck declarado.
- **Decisão:** INVIÁVEL — estudo edilício; GWP não isolável; sem fck.

---

### SESSÃO ATUAL (2026-05-18, terceira parte)

---

#### VILLALBA et al., 2025
- **Linha ANÁLISE:** 42
- **Códigos:** `UF-ELEMENTO` `UF-SISTEMA`
- **UF declarada:** Retrofit sísmico de uma viga RC específica com deficiência de cisalhamento, garantindo 50 anos de vida útil (cradle-to-grave)
- **Dados extraídos:**
  - 5 alternativas de reforço: jacketing de concreto (CJ), jacketing por shotcrete (SCJ), jacketing de aço (STE), placa de aço com adesivo (STA), fibra de carbono (CFRP)
  - Tabela 2 (p. 14): inventário por UF — CJ usa 0,27 m³ de concreto 24–30 MPa + 32,83 kg de aço + adesivos + tinta anti-carbonatação + energia de demolição
  - GWP reportado por alternativa de retrofit; inclui concreto + aço + FRP + adesivos + manutenção + fim de vida
- **Problema:** UF = retrofit sísmico de viga específica (elemento multi-componente). Escopo cradle-to-grave. Concreto utilizado é material de reforço sobre estrutura existente, não traço de concreto estrutural primário. GWP do concreto não isolável dos demais componentes de retrofit.
- **Decisão:** INVIÁVEL — UF = elemento de retrofit multi-componente; cradle-to-grave; GWP não isolável ao concreto.

---

#### MARTINEZ-MUNOZ et al., 2025
- **Linha ANÁLISE:** 121
- **Códigos:** `UF-SISTEMA`
- **UF declarada:** Ponte mista aço-concreto de três vãos (60 m + 100 m + 60 m), otimização multi-objetivo via teoria dos jogos
- **Dados extraídos:**
  - Estudo de otimização multi-objetivo (custo + ELCA + SLCA + construtividade) de ponte com tabuleiro de concreto e perfis de aço
  - GWP reportado como função objetivo a minimizar (CO₂/ponte completa); sem breakdown por m³ de concreto
  - fck não declarado para o concreto do tabuleiro
- **Problema:** UF = ponte completa (sistema aço-concreto). Estudo de otimização estrutural, não de caracterização de traços de concreto. GWP do concreto não isolável do aço e demais componentes. Sem fck declarado.
- **Decisão:** INVIÁVEL — UF = sistema ponte multi-componente; GWP não isolável; sem fck.

---

#### MILANI et al., 2020
- **Linha ANÁLISE:** 24
- **Códigos:** `UF-SISTEMA`
- **UF declarada:** Superestrutura de ponte de pequeno vão (6 a 20 m), cradle-to-grave; 405 configurações analisadas (aço-concreto composto, CA moldado in loco, pré-moldado, protendido)
- **Dados extraídos:**
  - 27 configurações de ponte × 15 variações de vão = 405 estruturas
  - GWP por tipo de ponte por vão (em kg CO₂eq/m² de tabuleiro, variando por configuração)
  - Concreto com 25 MPa mencionado para paredes de contenção similares, mas sem fck declarado sistematicamente por configuração de ponte
- **Problema:** UF = superestrutura de ponte completa (multi-material: concreto + aço + outros). Escopo cradle-to-grave. GWP por ponte não isolável ao concreto. Sem fck por traço de concreto.
- **Decisão:** INVIÁVEL — UF = sistema ponte; multi-material; cradle-to-grave; GWP não isolável.

---

#### PONS et al., 2018
- **Linha ANÁLISE:** 138
- **Códigos:** `UF-ELEMENTO`
- **UF declarada:** Metro linear de muro de contenção para altura determinada (1 a 6 m); 4 tipos: cantilever, gravidade, alvenaria, gabião
- **Dados extraídos:**
  - Tabela 1: materiais por metro linear — muro cantilever usa concreto 25 MPa (208 kg/m³ cimento, 164 L/m³ água, 1110 kg/m³ brita, 919 kg/m³ areia) + aço B500S
  - Tabela 2 (p. 23): GWP para muros de 4 m — cantilever=907,43; gravidade=1025,58; alvenaria=915,08; gabião=629,23 kg CO₂eq/m linear
  - Escopo: cradle-to-grave (produção + construção + uso 50 anos + fim de vida)
- **Problema:** UF = metro linear de muro de contenção (estrutura multi-componente). GWP inclui concreto + aço + aterro + transporte + construção + demolição + reciclagem. Impossível isolar GWP exclusivo do concreto. Adicionalmente, escopo é cradle-to-grave.
- **Decisão:** INVIÁVEL — UF = metro linear de sistema multi-componente; GWP não isolável ao concreto; cradle-to-grave.

---

#### SBAHIEH et al., 2023a
- **Linha ANÁLISE:** 160
- **Códigos:** `UF-ELEMENTO` `GWP-DATABASE`
- **UF declarada:** Viga RC específica de 5×0,3×0,5 m (0,75 m³ de concreto) com diferentes armações: aço / GFRP (c/ água do mar) / CFRP (c/ água do mar)
- **Dados extraídos:**
  - Tabela 2 (p. 5): f'c = 25 MPa para todas as vigas; dimensões 5000×300×500 mm
  - Tabela 4 (p. 8): GWP por componente — viga de aço: cimento=286; brita=2,51; areia=0,983; água dessalinizada=3,98; aço=124 kg CO₂eq → total=417 kg CO₂eq/viga
  - Tabela 5: viga GFRP: cimento=286; água do mar=0,0104; GFRP=32,8 → total=322 kg CO₂eq/viga
  - GWP concreto (sem armação) back-calculável: viga aço = 293,5/0,75 = **391 kg CO₂eq/m³**; viga FRP = 289,5/0,75 = **386 kg CO₂eq/m³**
- **Problema:** (1) Estudo compara TIPOS DE ARMAÇÃO (FRP vs aço), não traços de concreto — o concreto é elemento ancilário, não objeto da pesquisa. (2) GWP do concreto provém do banco de dados GaBI (nenhum inventário original de traço específico). (3) Uso de água dessalinizada/do mar como variável experimental introduz contexto muito específico do Qatar não representativo. (4) Valor back-calculado (391 kg CO₂eq/m³ para C25) é elevado para a classe, refletindo o contexto geográfico e a base GaBI, não um mix design primário.
- **Nota:** Back-cálculo tecnicamente possível, mas o dado não representa caracterização original de traço de concreto.
- **Decisão:** INVIÁVEL — estudo de comparação de armações; concreto ancilário; GWP de banco de dados genérico (GaBI); contexto Qatar com água dessalinizada.

---

## Estudos VIÁVEIS — adicionados à METANÁLISE

### SESSÃO ANTERIOR (2026-05-18, segunda parte)

---

#### HAFEZ et al., 2024b ✓
- **Linha ANÁLISE:** 104
- **Linhas METANÁLISE:** 132–135
- **UF declarada:** m² de laje unidirecional (4 cenários: d=175mm/325mm; L/d=20/25)
- **Método de conversão:** GWP/m³ back-calculado de Tabela 5:
  `GWP_concreto/m³ = (GWP_total/m² − armadura_kg/m² × 1,08 kg CO₂eq/kg) ÷ volume_concreto_m³/m²`
  Validação: valores consistentes em todos os 4 cenários de laje (σ < 1,5 kg CO₂eq/m³).
- **fck:** 40 MPa — C40/50 (classificação do paper); LC3 medido = 49,1 ± 1,8 MPa (cilindro 28d)
- **Vida útil:** 50 anos (declarado para dimensionamento contra carbonatação)
- **Traços e resultados:**

| ID | Formulação | GWP (kg CO₂eq/m³) | ci | ci_t |
|----|-----------|------------------|----|------|
| HAFEZ_2024b_OPC | CEM I 300 kg/m³, sem fibras | 272,0 | 6,80000 | 0,13600 |
| HAFEZ_2024b_OPC-SF | CEM I 300 kg/m³ + fibras aço 60 kg/m³ | 345,9 | 8,64750 | 0,17295 |
| HAFEZ_2024b_LC3 | LC3 (CEM I 159+argila 90+calc. 45+gipso 6 kg/m³) | 170,2 | 4,25500 | 0,08510 |
| HAFEZ_2024b_LC3-SF | LC3 + fibras aço 60 kg/m³ | 241,5 | 6,03750 | 0,12075 |

- **Observação:** Estudo de alta relevância — LC3 tem ci 37% menor que OPC com mesma classe de resistência C40/50. Único estudo com LC3 na METANÁLISE até agora.

---

---

# SESSÃO 2026-05-19

## Estudos INVIÁVEIS — sessão 2026-05-19

### HAJIESMAEILI et al., 2019
- **Código:** HAJIESMAEILI
- **Status:** INVIÁVEL — UF-SISTEMA
- **Motivo:** FU = Guillermaux Footbridge completa (estrutura completa de ponte). LCA por metro linear de ponte. GWP declarado em kg CO₂eq/m de ponte, não por m³ de concreto. Back-calculation inviável: seção transversal variável, múltiplos elementos estruturais (deck UHPFRC + vigas transversais + apoios), sem itemização de volumes por componente.
- **ANÁLISE tab:** Row 15 → ci = 'INVIÁVEL'

---

### KOUVARA et al., 2023
- **Código:** KOUVARA
- **Status:** INVIÁVEL — GWP-FIGURA
- **Motivo:** GWP reportado exclusivamente em gráficos de barras (figuras). Nenhum valor numérico em tabelas. Valores estimados visualmente das figuras não têm precisão suficiente para meta-análise (escala da figura não permite leitura confiável de kg CO₂eq/m³).
- **ANÁLISE tab:** Row 18 → ci = 'INVIÁVEL'

---

### KUMAR et al., 2024a
- **Código:** KUMAR 2024a
- **Status:** INVIÁVEL — GWP-FIGURA
- **Motivo:** Estudo do tipo dataset de bills of materials; resultados de GWP apresentados somente em gráficos comparativos. Sem tabelas com valores numéricos de kg CO₂eq/m³ por traço. Dados de resistência declarados mas GWP ilegível com precisão suficiente.
- **ANÁLISE tab:** Row 110 → ci = 'INVIÁVEL'

---

### MARTINEZ-MUNOZ et al., 2025
- **Código:** MARTINEZ-MUNOZ 2025
- **Status:** INVIÁVEL — GWP-ESCALA
- **Motivo:** Método LCA = ReCiPe Endpoint (damage categories). Resultados em "Points" (espécies·ano/m², USD/m², DALY/m²), não em kg CO₂eq. Zero valores de GWP em kg CO₂eq/m³ em qualquer tabela. Confirmado nesta sessão.
- **ANÁLISE tab:** Row 121 → ci = 'INVIÁVEL'

---

### MILANI et al., 2020
- **Código:** MILANI 2020
- **Status:** INVIÁVEL — GWP-ESCALA
- **Motivo:** Método LCA = ReCiPe Endpoint. Resultados reportados em Pontos normalizados (damage categories). Ausência total de valores em kg CO₂eq/m³. Tabelas de resultados com unidade "Pt" (Pontos) confirma ReCiPe Endpoint — impossível converter para GWP em kg CO₂eq.
- **ANÁLISE tab:** Row 24 → ci = 'INVIÁVEL'

---

### PONS et al., 2018
- **Código:** PONS 2018
- **Status:** INVIÁVEL — UF-SISTEMA
- **Motivo:** FU = muro de contenção gravidade (massa de concreto) por metro de altura variável (1–6 m). Back-calculation tentada: Tabela 1 fornece Vconcrete/m² para alturas 1–6 m e contribuição do concreto (83–114%). Problemas: (a) altura exata para o caso de 4 m não declarada; (b) crédito EoL por carbonatação cria anomalia >100% em algumas alturas; (c) resultados inconsistentes para mesmo traço (~211 vs ~251 kg CO₂eq/m³ dependendo da altura assumida). Critério de consistência falhou → INVIÁVEL UF-SISTEMA.
- **ANÁLISE tab:** Row 138 → ci = 'INVIÁVEL'

---

### ROSSI, 2013
- **Código:** ROSSI 2013
- **Status:** INVIÁVEL — SEM-FCK
- **Motivo:** Dissertação de mestrado sobre LCA de agregados/brita para concreto. Escopo A1-A3 de materiais granulares, não de concreto como produto final. Sem fck declarado (não é estudo de mistura de concreto). GWP em kg CO₂eq/t de agregado. Fora do escopo da RSL — concreto como produto não está no estudo.
- **ANÁLISE tab:** Row 32 → ci = 'INVIÁVEL'

---

### VILLALBA et al., 2025
- **Código:** VILLALBA 2025
- **Status:** INVIÁVEL — GWP-ESCALA
- **Motivo:** Método LCA = ReCiPe Endpoint. Resultados em Pontos normalizados (damage categories). Ausência de valores em kg CO₂eq/m³. Log anterior (2026-05-18) havia classificado como UF-ELEMENTO; reclassificado nesta sessão para GWP-ESCALA — causa raiz é a escala de impacto (ReCiPe Pts), não o tipo de UF.
- **ANÁLISE tab:** Row 42 → ci = 'INVIÁVEL'

---

## Estudos VIÁVEIS — sessão 2026-05-19

### MENEGATTI et al., 2022
- **Código:** MENEGATTI 2022
- **Status:** VIÁVEL — 2 traços adicionados à METANÁLISE
- **FU declarado:** 1 m³ de concreto (UF por volume ✓)
- **Escopo:** A1-A3 (cradle-to-gate)
- **fck:** 60 MPa (C60 nominal, resistência cilindro medida ≥ 60 MPa)
- **Vida útil:** 50 anos (declarado)
- **Traços:**

| ID | Formulação | GWP (kg CO₂eq/m³) | ci | ci_t |
|----|-----------|------------------|----|------|
| MENEGATTI_2022_ORB | Ordinary Reinforced Beam mix | 351,76 | 5,862667 | 0,117253 |
| MENEGATTI_2022_DRB | Ductile Reinforced Beam mix | 352,43 | 5,873833 | 0,117477 |

- **Escore qualidade:** 6
- **METANÁLISE:** Rows 136–137 inseridos
- **ANÁLISE tab:** Row 23 → ci = 5,8683, ci_t = 0,11737

---

### SBAHIEH et al., 2023a
- **Código:** SBAHIEH 2023a
- **Status:** VIÁVEL — 2 traços adicionados à METANÁLISE
- **⚠️ DECISÃO REVISADA:** Log anterior (2026-05-18) havia classificado como INVIÁVEL por dois motivos: (1) GWP-DATABASE (valores de CO₂eq de banco genérico Ecoinvent sem dados primários) e (2) UF-ELEMENTO (viga estrutural). Revisado para VIÁVEL nesta sessão após leitura mais aprofundada do PDF: Tables 4/5/6 fornecem itemização completa do GWP por componente do elemento (concreto, armadura de aço, GFRP, CFRP); dimensões da viga declaradas (5 × 0,5 × 0,3 m → V = 0,75 m³); back-calculation tecnicamente válido e consistente com o critério aceito para HAFEZ 2024b. A origem Ecoinvent dos dados materiais não invalida o resultado — é prática padrão em LCA de concreto.
- **FU declarado:** Viga estrutural 5,0 × 0,5 × 0,3 m (A1-A3, cradle-to-gate)
- **Back-calculation:** GWP_concreto/m³ = GWP_beam_concrete_only ÷ V_concreto (0,75 m³)
- **fck:** 25 MPa (C25 nominal, mix de concreto de desempenho normal declarado)
- **Vida útil:** não declarada (ci_t = None)
- **Traços:**

| ID | Formulação | GWP (kg CO₂eq/m³) | ci | ci_t |
|----|-----------|------------------|----|------|
| SBAHIEH_2023a_steel_fw | Freshwater desalinated + steel rebars | 391,29 | 15,651733 | — |
| SBAHIEH_2023a_FRP_sw | Seawater + FRP rebars (GFRP/CFRP) | 386,00 | 15,440000 | — |

- **Nota:** Os dois traços diferem pela água de amassamento (água doce dessalinizada vs água do mar); o mix de concreto base é idêntico, mas o GWP varia por diferença no processo de dessalinização.
- **Escore qualidade:** 5
- **METANÁLISE:** Rows 138–139 inseridos
- **ANÁLISE tab:** Row 160 → ci = 15,545 (média), ci_t = None

---

### HAVERKAMP et al., 2025
- **Código:** HAVERKAMP 2025
- **Status:** VIÁVEL — 1 traço adicionado à METANÁLISE
- **FU declarado:** Painel de fachada CRC (Compact Reinforced Composite) — 4000 × 3600 × 40 mm
- **Escopo:** A1-A3 (cradle-to-gate, baseado em PEF — Product Environmental Footprint, método EU)
- **Back-calculation:** Tabela 12 do paper fornece contribuição percentual por processo; "concrete production" = 34% do GWP total. GWP_total = 456 kg CO₂eq (Ecoinvent). GWP_concreto = 0,34 × 456 = 155,04 kg CO₂eq. Volume painel = 4,0 × 3,6 × 0,04 = 0,576 m³. GWP/m³ = 155,04 / 0,576 = **269,17 kg CO₂eq/m³**.
- **fck:** 50 MPa (C50/60, declarado no paper como CRC de alta resistência)
- **Vida útil:** 100 anos (declarado explicitamente para fachadas de edifícios)
- **Traços:**

| ID | Formulação | GWP (kg CO₂eq/m³) | ci | ci_t |
|----|-----------|------------------|----|------|
| HAVERKAMP_2025_CRC | CRC (Compact Reinforced Composite) façade panel | 269,17 | 5,383333 | 0,053833 |

- **Escore qualidade:** 5,5
- **METANÁLISE:** Row 140 inserido
- **ANÁLISE tab:** Row 16 → ci = 5,38, ci_t = 0,0538

---

## Resumo acumulado

| Status | N estudos | Observações |
|--------|-----------|-------------|
| INVIÁVEL — UF sistema (ponte / edifício / sistema multi-componente) | 10 | PESTA, FERREIRA, MATIAS, ZHANG, MALABI, KUMAR (2023), MARTINEZ-MUNOZ 2025, MILANI 2020, PONS 2018, HAJIESMAEILI 2019 |
| INVIÁVEL — UF /kg | 3 | VOLK, INMAN, KASTIUKAS |
| INVIÁVEL — UF /elemento (back-calc inviável) | 1 | EK |
| INVIÁVEL — sem fck por traço | 5 | GANAPATHI, VENTURA, VIDAL, BILAR, ROSSI 2013 |
| INVIÁVEL — GWP em figuras apenas | 4 | KIM, GANAPATHI (parcial), KOUVARA 2023, KUMAR 2024a |
| INVIÁVEL — GWP de banco de dados genérico | 2 | MATIAS DE PAULA FILHO, SOMBRIO |
| INVIÁVEL — GWP com escala impossível (ReCiPe Endpoint Pts) | 2 | CUNHA, VILLALBA 2025 |
| **VIÁVEL — adicionado à METANÁLISE** | **4** | HAFEZ 2024b (4 traços), MENEGATTI 2022 (2 traços), SBAHIEH 2023a (2 traços, REVISADO), HAVERKAMP 2025 (1 traço) |
| **n (observações) METANÁLISE** | **140** | Anterior: 135 (+5 esta sessão) |
| **Total analisados Fase 5** | **~35** | Sessões 2026-05-18 + 2026-05-19 |

---

*Última atualização: 2026-05-19 (sessão 4)*
