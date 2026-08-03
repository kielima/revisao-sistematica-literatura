---
titulo: RSL — Log de Coleta R (ci) e Coleta S (ci_t)
descricao: Registro da coleta das colunas ci (kg CO₂eq/m³/MPa) e ci_t (normalizado por vida útil) na aba ANÁLISE do banco de dados da RSL
tags: [academico-e-pesquisa, meta-analise, revisao-sistematica, UHPC, engenharia-e-construcao]
status: em-andamento
ultima_atualizacao: 2026-05-18
---

# RSL — Log de Col R (ci) e Col S (ci_t)

**Gerado em:** 2026-05-18  
**Arquivo:** `BANCO DE DADOS DA RSL.xlsx` — aba `ANÁLISE`  
**Responsável:** Claude (Cowork) + Kiê  

---

## 1. Definição dos índices (Equações 1 e 2 — Dissertação v15)

| Índice | Fórmula | Unidade | Coluna | Observação |
|---|---|---|---|---|
| **ci** | Emissão / fck | kg CO₂eq / (m³·MPa) | **Col R** | Proposto por Damineli et al. (2010). Calculável para qualquer artigo com GWP em kg/m³ e fck declarado. |
| **ci_t** | ci / vida_útil | kg CO₂eq / (m³·MPa·ano) | **Col S** | Desfecho primário da meta-análise. Calculável apenas para artigos com vida útil declarada. |

> **Nota histórica (2026-05-18):** A decisão de 2026-05-13 registrava "col R = ci_t". Ao verificar o banco e as equações da dissertação v15, constatou-se que col R já estava corretamente implementada como ci (Equação 1) e col S como ci_t (Equação 2). O nome "CO₂eq normalizado" foi renomeado para "ci — kg CO₂eq/(m³·MPa)" para eliminar ambiguidade.

---

## 2. Resumo do preenchimento

| Status | Artigos |
|---|---|
| ✅ PREENCHIDO | 41 |
| ⏳ PENDENTE (extração manual do PDF) | 43 |
| ❌ N/A — fck ausente ou não declarado | 70 |
| ❌ N/A — UF incompatível com m³ | 20 |
| ➖ Excluído por qualidade (score <4) | 12 |
| **Total** | **186** |

---

## 3. Correções aplicadas em 2026-05-18

### 3.1 HABIBI et al., 2024 — METANÁLISE (2 linhas)

**Problema detectado:** ambas as linhas tinham ID `HABIBI_et_al_principal`, `emissão=439` e `vida_útil=54`, gerando ci_t=0,32519 idêntico. Na verdade, o artigo descreve dois designs distintos.

| Linha | Cenário | Correção |
|---|---|---|
| 15 | Convencional (fcm=33,9) | ID → `HABIBI_et_al_convencional`; vida_útil 54→**38**; ci_t 0,32519→**0,46211** |
| 16 | Circular (fcm=33,4) | ID → `HABIBI_et_al_circular`; emissão 439→**354**; ci 17,56→**14,16**; ci_t 0,32519→**0,26222** |

> Fonte do GWP circular: Tabela 4 do artigo — Ω=5,10 = fc×SL/GWP → GWP = 33,4×54/5,10 = **353,6 ≈ 354** kg CO₂eq/m³. Confirmado pela Tabela 5: 6,56 kg/m³·ano × 54 = 354.  
> Backup criado: `BANCO DE DADOS DA RSL_backup_pre-HABIBI-fix_20260518.xlsx`

### 3.2 HABIBI et al., 2024 — aba ANÁLISE (col S)

| Campo | Antes | Depois |
|---|---|---|
| col S (ci_t) | 0,32519 (SL=54 indevido no convencional) | **0,46211** (ci_conv=17,56 / SL=38) |
| Cenário circular | — | ci_t=0,26222 registrado em Comentários e METANÁLISE |

### 3.3 Col R renomeada

`CO₂eq normalizado` → **`ci — kg CO₂eq/(m³·MPa)`**

### 3.4 Novos preenchimentos — col R (ci) via METANÁLISE

| Estudo | ci calculado | n obs. | Valores individuais |
|---|---|---|---|
| NASSAR et al., 2025 | 3,77835 | 2 | [3,5345; 4,0222] |
| STARCZYK-KOLBYK, 2024 | 15,06667 | 1 | [15,0667] |
| MANAN et al., 2025 | 12,91667 | 4 | [13,667; 13,1667; 12,8333; 11,9997] |
| PAVLU et al., 2019 | 11,75500 | 1 | [11,755] |
| TAIT et al., 2016 | 7,16667 | 3 | [10,4375; 7,0938; 3,9688] |
| RANATUNGA et al., 2023 | 13,27200 | 5 | [15,88; 13,72; 13,0; 12,24; 11,52] |

> **Metodologia:** ci médio calculado como média aritmética simples das observações na METANÁLISE para o mesmo estudo. Para estudos com múltiplos traços, o ci médio representa o desempenho central do estudo; valores individuais estão na METANÁLISE para análise detalhada.

---

## 4. Tabela completa — estado de cada artigo

### 4.1 Artigos com col R (ci) PREENCHIDO (41)

| Estudo | ci | ci_t | Score AQ | Fonte | Em METANÁLISE |
|---|---|---|---|---|---|
| ASSUNCAO, 2020 | 0.24868 | 0.00497 | 5.5 | Primário | ✅ |
| BACKES et al., 2022 | 0.23000 | 0.00230 | 4.5 | Primário | ✅ |
| BHAGAT et al., 2021 | 9.30797 | 0.13297 | 4.5 | Primário | ✅ |
| BUMANIS et al., 2022 | 9.47050 | — | 5 | Primário | ✅ |
| CELIK et al., 2015 | 12.54720 | — | 4.5 | Primário | ✅ |
| CELIK et al., 2015 | 12.54720 | — | 4.5 | Primário | ✅ |
| CELIK et al., 2015 | 12.54720 | — | 4.5 | Primário | ✅ |
| CELIK et al., 2015 | 12.54720 | — | 4.5 | Primário | ✅ |
| CELIK et al., 2015 | 12.54720 | — | 4.5 | Primário | ✅ |
| CELIK et al., 2015 | 12.54720 | — | 4.5 | Primário | ✅ |
| CELIK et al., 2015 | 12.54720 | — | 4.5 | Primário | ✅ |
| CELIK et al., 2015 | 12.54720 | — | 4.5 | Primário | ✅ |
| CELIK et al., 2015 | 12.54720 | — | 4.5 | Primário | ✅ |
| CELIK et al., 2015 | 12.54720 | — | 4.5 | Primário | ✅ |
| CELIK et al., 2015 | 12.54720 | — | 4.5 | Primário | ✅ |
| CELIK et al., 2015 | 12.54720 | — | 4.5 | Primário | ✅ |
| CELIK et al., 2015 | 12.54720 | — | 4.5 | Primário | ✅ |
| CHOI et al., 2023 | 16.66667 | — | 3 | Primário | ✅ |
| COELHO, 2016 | 13.29930 | — | 5 | Primário | ✅ |
| CONG et al., 2024 | 2.11500 | 0.04230 | 6 | Primário | ✅ |
| CORDOBA et al., 2023 | 11.61006 | — | 4 | Primário | ✅ |
| CORTI et al., 2023 | 3.79833 | 0.07597 | 5.5 | Primário | ✅ |
| DERVISHAJ et al., 2024 | 16.71300 | 0.33426 | 6 | Primário | ✅ |
| DONG et al., 2021 | 7.32171 | — | 5 | Primário | ✅ |
| DU et al., 2024 | 436.59330 | — | 4.5 | Primário | ✅ |
| DYNAN et al., 2023 | 9.83815 | — | 4.5 | Primário | ✅ |
| FARAHZADI et al., 2025 | 9.45000 | — | 4.5 | Primário | ✅ |
| HABIBI et al., 2024 | 17.56000 | 0.46211 | 5.5 | Primário | ✅ |
| JAYASINGHE et al., 2021 | 7.58350 | — | 4.5 | Primário | ✅ |
| KHORGADE et al., 2023 | 6 | — | 4.5 | Primário | ✅ |
| LI et al., 2024 | 8.09112 | — | 4 | Primário | ✅ |
| MANAN et al., 2025 | 12.91667 | — | 5 | Primário | ✅ |
| MIR et al., 2022 | 44.30608 | — | 5 | Primário | ✅ |
| NASSAR et al., 2025 | 3.77835 | — | 4 | Primário | ✅ |
| PAVLU et al., 2019 | 11.75500 | — | 6 | Primário | ✅ |
| RANATUNGA et al., 2023 | 13.27200 | — | 5 | Primário | ✅ |
| SANCHEZ-PANTOJA et al., 2023 | 5.34500 | — | 5.5 | Primário | ✅ |
| SOLTANZADEH et al., 2022 | 0.02000 | — | 5 | Primário | ✅ |
| STARCZYK-KOLBYK, 2024 | 15.06667 | — | 4.5 | Primário | ✅ |
| TAIT et al., 2016 | 7.16667 | — | 5 | Primário | ✅ |
| TEPLY et al., 2018 | 7.88000 | 0.05218 | 5 | Primário | ✅ |

### 4.2 Artigos PENDENTES — extração manual do PDF necessária (43)

| Estudo | Score AQ | Status AQ | UF (trecho) | fck (trecho) | Ação necessária |
|---|---|---|---|---|---|
| BILAR, 2016 | 5 | Incluído | 1 m2 do sistema vertical de vedacao (p. 77) | Blocos de concreto Classe A: resistencia a compressao de 6 MPa (p. 115, 126) | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| BRESSI et al., 2022 | 4.5 | Incluído | 1 km de pavimento rodoviário de 22 m de largura (2 pistas, 4 faixas) suportando  | Resistencia a compressao 28 dias (fc28): ~497-585 psi (~3,4-4,0 N/mm2) para espé | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| CARUSO et al., 2018 | 4.5 | Incluído | O edificio inteiro (sistema estrutural completo) (p. 5) | Concreto C25/30: fck = 25 MPa (cilindrico); aco de reforco B450C; aco estrutural | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| CHIPPAGIRI et al., 2023 | 4.5 | Incluído | Sistema completo da casa modelo em escala reduzida 1/3; resultados tambem expres | Concreto CFA: 26,91 MPa; LW mix: 7,05 MPa (ensaios IS 516:1959, Tabela 2 p. 5);  | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| CUNHA, 2022 | 5 | Incluído | 1 m3 de concreto com resistencia de 32 MPa (p. 19, 63) | 32 MPa (p. 19, 60, 62) | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| D'ORAZIO et al., 2023 | 4.5 | Incluído | 1 litro de mistura de argamassa: 32 MPa para REF1/DELTA; 25 MPa para REF2/HP (un | REF1 e DELTA: fck = 32 MPa (classe M30); REF2 e HP: fck = 25 MPa (classe M20) (p | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| DI MARIA et al., 2020 | 4.5 | Incluído | 1 m2 de blocos com 40 MPa de resistencia (0,008 m3; 50 blocos de 20x10x4 cm; 92  | 40 MPa (unidade funcional de referencia); blocos carbonatados atingiram 43 MPa n | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| DING et al., 2023 | 5.5 | Incluído | 1 m3 de material de consolidacao de rejeitos (p. 11) | Criterio minimo de desempenho: 3 MPa aos 28 dias; maximo obtido: 7,76 MPa (sulfo | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| FIRDOUS et al., 2022 | 4 | Incluído | 1 m3 de mistura de concreto (p. 18717) | 17,5 a 51,4 MPa aos 28 dias (faixa dos 14 tracos geopolimericos) (p. 18718) | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| GANAPATHI CHOTTEMADA et al., 2023 | 5 | Incluído | 1 m3 de concreto (p. 7) | 35 a 55 MPa aos 28 dias; mix otimo FS50-SF0.3: 44,18 MPa (p. 1, 4-5) | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| GUAYGUA et al., 2024 | 5 | Incluído | 1 mÂ² de area de edificio (p. 5) | 28 MPa para todos os elementos de concreto (p. 6) | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| HAFEZ et al., 2024a | 4 | Incluído | 1 m2 de area construida (area liquida x numero de andares) (p. 7) | C30/37 (fck=30 MPa), C50/60 (fck=50 MPa) e C70/85 (fck=70 MPa); combinacoes entr | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| HAJIESMAEILI et al., 2019 | 5.5 | Incluído | Intervencao na Ponte Guillermaux (restauracao ou substituicao) - escala da estru | PE-UHPFRC (Metodo 3): 120 MPa (p. 3, Tabela 2); UHPFRC convencional: 150-200 MPa | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| HAVERKAMP et al., 2025 | 5.5 | Incluído | Painel de fachada CRC: 4000mm x 3600mm x 40mm, forca compressiva C50/60, resiste | C50/60 (fck = 50 MPa, fcm = 58 N/mm2) conforme EN 206-1 (p. 4, Tabela 1; p. 6, T | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| INMAN et al., 2017 | 5.5 | Incluído | Por viga de concreto armado (por unidade funcional = 1 viga); dimensoes detalhad | Vigas BFRP: f circuloc = 57,1 a 67,4 MPa; vigas de aco: f circuloc = 31,4 MPa (m | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| KASTIUKAS et al., 2019 | 6 | Incluído | 1,0 kg de pasta MOC (razoes 3, 5 ou 9); 1,0 kg de concreto MOC (razao 9, w/s=0,3 | Pasta MOC-3: 71,8 MPa; MOC-5: 93 MPa; MOC-9: 111 MPa (resistencia a compressao a | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| KIM et al., 2016 | 5 | Incluído | 1 m3 de concreto; analises comparativas tambem por unidade de resistencia (GWP/1 | 18 a 80 MPa (normal: 18-40 MPa, 800 tracas; alta resistencia: 40-80 MPa, 200 tra | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| KONG et al., 2022 | 5 | Incluído | 1 tonelada (1t) de pasta: M20 (80% OPC + 20% HCP calcinada carbonatada, W/CM=0,4 | OPC puro (referencia): 37,8 MPa aos 28 dias; M20 (20% substituicao): aumento ~8% | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| KOUVARA et al., 2023 | 5.5 | Incluído | 1 kg de concreto (cradle-to-gate, comparacao de massa); 1 m2 de superficie de pa | Concreto polimerico: resistencia a compressao 90-130 MPa (material), 4,5-5,0 MPa | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| KUL et al., 2023 | 5 | Incluído | 1 m3 de argamassa geopolimerica a base de RCD (p. 12) | Argamassas geopolimericas: 23,1 a 66,2 MPa (media ~40 MPa); referencia PCF: 47,4 | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| KUMAR et al., 2024a | 5.5 | Incluído | 1 m2 de area de piso de edificio multifamiliar residencial de multiplos andares  | MT: 20,68 MPa (3000 psi) fundacao/cobertura; SS: 27,58 MPa (4000 psi) laje compo | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| MANJUNATHA et al., 2022 | 5 | Incluído | 1 m3 de concreto preparado conforme IS:10262-2019 (p. 6, 13) | M50 - resistencia caracteristica 50 MPa; compressivas obtidas variaram de 47,62  | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| MARTINEZ-MUNOZ et al., 2021 | 4.5 | Incluído | 1 m2 de tabuleiro de ponte (p. 7) | HP-40 (40 MPa) para PCSS, PCLS e PCBG; HA-30 (30 MPa) para laje do CBG (p. 8, Ta | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| MARTINEZ-MUNOZ et al., 2022 | 4 | Incluído | 1 m2 de tabuleiro de ponte (p. 7) | C40/50 (40 MPa) para PCSS, PCLS e PCBG; C30/37 (30 MPa) para laje do CBG (p. 9,  | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| MARTINEZ-MUNOZ et al., 2025 | 5.5 | Incluído | Ponte mista de tres vaos de 60-100-60 m com 16 m de largura (tabuleiro completo) | Variavel de otimizacao entre 25, 30, 35 e 40 MPa; solucao otima obteve fck = 25  | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| MATIAS DE PAULA FILHO et al., 2024 | 5.5 | Incluído | Edificio de escritorios de 9 pavimentos em formato L, 13,60 m x 78,15 m, com 50  | Concreto pronto C30/37, C40/50 e C50/60 MPa (p. 10, Tab. 7) | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| MENEGATTI et al., 2022 | 6 | Incluído | 1 m de viga com seção 140 x 600 mm e resistência à compressão de 60 MPa (p. 5) | fck = 60 MPa (classe C60) — concreto de alta resistência com 100% de agregados g | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| MITTERPACH et al., 2023 | 5 | Incluído | WCB completa para calculo de desempenho ambiental total; 1 m2 de area de tabulei | C30/37 (fck = 30 MPa cilindro / 37 MPa cubo) para concreto estrutural; C25/30 pa | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| PAIK et al., 2019 | 4.5 | Incluído | Sistemas de laje (convencional vs. VDS) de um edificio comercial-residencial de  | 25 MPa (concreto usinado); barras de aco com resistencia a tracao de 400 MPa (p. | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| PALACIOS-MUNOZ et al., 2018 | 4.5 | Incluído | Aumento especifico da capacidade de flexao (10%, 30% e 50%) de uma viga de concr | fcd = 20 MPa (tipico de construcoes espanholas de 1960); estudos de caso com C16 | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| PONS et al., 2018 | 5 | Incluído | Um metro linear de muro para uma determinada altura (1 a 6 m) (p. 4) | 25 MPa (C25) para ambos os muros de concreto (armado e gravidade); dosagem: 208  | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| PUJADAS-GISPERT et al., 2021 | 4 | Incluído | Fundacao convencional composta por vigas de fundacao de concreto e estacas, cons | C20/25, C25/30, C30/37, C40/50 para estacas moldadas in situ; C35/45 para estaca | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| RAZA et al., 2023 | 4.5 | Incluído | 1 tijolo produzido (SSB com resíduo de tijolo, SSB sem resíduo de tijolo e tijol | SSB com resíduo de tijolo (BWF): 4 MPa; tijolo convencional cozido: 7,5 MPa (res | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| ROSSI, 2013 | 5.5 | Incluído | Edifício padrão multifamiliar R8-B (baixo padrão) com resistência de concreto de | 25 MPa — resistência do concreto da unidade funcional (edifício padrão R8-B, bai | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| SBAHIEH et al., 2023a | 5 | Incluído | Dois FUs: (1) barra de 1 m de comprimento e 12 mm de diametro (para comparacao d | 25 MPa (fck declarado nas Tab.2 para vigas GFRP e CFRP, f'c = 25 MPa) (p. 5, Tab | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| SBAHIEH et al., 2023b | 4.5 | Incluído | Nao informado de forma unificada - varia entre os estudos revisados, geralmente  | Resistencia a compressao variando de 0,2 a 81 MPa conforme tipo de precursor, at | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| VACLAVIK et al., 2020 | 5 | Incluído | 1 m3 de concreto (p. 6, sec. 2.4) | Resistencia a compressao cubica apos 28 dias: CSS 0 = referencia; CSS 4/8 = lige | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| VILLALBA et al., 2025 | 5.5 | Incluído | Reforço sísmico de uma viga de concreto armado para vida útil de 50 anos (p. 1) | Viga original: f'c = 24 MPa (Tabela 1, p. 12); Reforço CJ e SCJ: concreto com re | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| VITIELLO et al., 2016 | 4.5 | Incluído | Reforco sismico completo do edificio de forma que a capacidade PGA seja igual a  | fck = 15 MPa (resistencia a compressao do concreto existente); fym = 220 MPa (re | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| VOLK et al., 2023 | 5 | Incluído | 1 kg de pd-AAC (po ou granulado pos-demolicao) - abordagem zero-burden com unida | C25/30 (fck = 25 MPa / fcm = 30 MPa) utilizado como referencia para a opcao de r | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| ZHANG et al., 2023 | 5 | Incluído | 1 m2 de area bruta de piso do edificio ao longo de 50 anos de vida util (p. 2) | C40 (40 MPa) para componentes pre-fabricados (p. 3) | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| ZHAO et al., 2020 | 5.5 | Incluído | 1 m3 de blocos de concreto, com base em um ciclo de producao anual [1 m3 of conc | B_RCA0 (0% RCA): classe f10 (fbm >= 10 MPa); B_RCA30 (30% RCA): resistencia redu | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |
| ZHENG et al., 2025 | 4.5 | Incluído | 1 m2 de area de edificio residencial ao longo de 50 anos de vida util (p. 2) | C30, C35 e C40 (30, 35 e 40 MPa) para estrutura de CA (p. 3) | Ler PDF — extrair GWP (kg/m³) e fck (MPa) |

### 4.3 Artigos N/A — fck não declarado (70)

| Estudo | Score AQ | Status AQ | Motivo |
|---|---|---|---|
| AL-GHEETHI et al., 2022 | 4 | Incluído | fck não declarado: N/A - ACV focada na produção; referência contextual: argamas |
| AL-OBAIDY et al., 2022 | 5 | Incluído | fck não declarado: N/A - estudo de ACV de sistemas construtivos; fck/resistênci |
| ALBRECHT et al., 2025 | 3.5 | Excluído | fck não declarado: N/A - fck não declarado diretamente; menção indireta a categ |
| BALASBANEH et al., 2018 | 4.5 | Incluído | fck não declarado: N/A - concreto T1 tipo grade 30 (~210 RM/m3) sem fck definid |
| BARBHUIYA et al., 2024 | 1 | Excluído | fck não declarado: N/A - revisão de literatura; sem ensaios próprios nem fck de |
| CARRETERO-AYUSO et al., 2018 | 4 | Incluído | fck não declarado: N/A - foco em sistemas de cobertura; sem fck estrutural; men |
| CARROBE et al., 2024 | 5 | Incluído | fck não declarado: N/A - fck nao definido; fundacao CBB usa concreto 20 MPa com |
| CHEN et al., 2020 | 5 | Incluído | fck não declarado: N/A - foco exclusivo em impactos ambientais (ACV); sem valor |
| CHO et al., 2025 | 3.5 | Excluído | fck não declarado: N/A (nao especificada para o PCC de reparo) (p. 1-22) |
| DA SILVA et al., 2021a | 3 | Excluído | fck não declarado: Resistencia minima normativa ABNT NBR 8491: 2,0 MPa; nao e f |
| DA SILVA et al., 2021b | 3 | Excluído | fck não declarado: Nao informado - revisao; cita estudos com variacao ampla de  |
| DE SOUZA et al., 2015 | 5 | Incluído | fck não declarado: Nao informado - estudo trata de telhas, nao elementos estrut |
| DEL SERRONE et al., 2023 | 3 | Excluído | fck não declarado: Nao informado - estudo trata de clinquer, nao concreto (veri |
| DIGULLA et al., 2023 | 3.5 | Excluído | fck não declarado: Nao informado - estudo trata de substitutos do cimento, nao  |
| DING et al., 2024 | 3 | Excluído | fck não declarado: Nao informado; fator de emissao do concreto utilizado: 321,3 |
| DOLCI et al., 2020 | 4 | Incluído | fck não declarado: Nao informado explicitamente; composicao: 420 kg/m3 de cimen |
| DURAO et al., 2024 | 5 | Incluído | fck não declarado: Nao informado; resistencia a flexao transversal das telhas d |
| EK et al., 2020 | 5.5 | Incluído | fck não declarado: C35/45 (fck = 35 MPa) para ponte CSF; elementos pre-moldados |
| FELICIONI et al., 2023 | 4.5 | Incluído | fck não declarado: Nao informado - classe de resistencia do concreto nao especi |
| FOZER et al., 2025 | 4 | Incluído | fck não declarado: Nao informado - estudo trata de clinquer, nao concreto (veri |
| GOMES, 2023 | 4 | Incluído | fck não declarado: Nao informado - concreto caracterizado pelo consumo de cimen |
| GROSSI et al., 2023 | 4 | Incluído | fck não declarado: Nao informado (verificado em todo o texto, pp. 1-13) |
| HAFNER et al., 2020 | 3.5 | Excluído | fck não declarado: Nao informado (verificado em todo o texto, pp. 1-12) |
| HEMMATI et al., 2024 | 3.5 | Excluído | fck não declarado: Nao informado (verificado em todo o texto, pp. 1-16) |
| INGRAO et al., 2018 | 4.5 | Incluído | fck não declarado: Nao informado (verificado em todo o texto, pp. 1-36) |
| JI et al., 2025 | 4 | Incluído | fck não declarado: Nao informado - material analisado e geopolimero de grauteam |
| KIRUPAKARAN, 2024 | 3.5 | Excluído | fck não declarado: Nao informado - revisao bibliografica; incidentalmente menci |
| KONO et al., 2018 | 4 | Incluído | fck não declarado: Nao informado (verificado em todo o texto, pp. 1-14) |
| KUMAR et al., 2024b | 5 | Incluído | fck não declarado: Nao informado - estudo nao declara fck de projeto; foco em i |
| KURSULA et al., 2024 | 5 | Incluído | fck não declarado: MA1: 10,78 MPa; MA2: 15,30 MPa; MA3: 8,93 MPa; LECA: 9,28 MP |
| LASVAUX et al., 2015 | 3 | Excluído | fck não declarado: N/A — estudo comparativo metodológico; não avalia resistênci |
| LIU et al., 2023 | 4 | Incluído | fck não declarado: Nao informado - concreto mencionado apenas em lajes e fundac |
| LYRA et al., 2024 | 6 | Incluído | fck não declarado: Nao informado - argamassa (nao concreto estrutural); traco b |
| MALABI EBERHARDT et al., 2020 | 5 | Incluído | fck não declarado: Nao informado - foco em metodologia de alocacao ACV; coluna  |
| MING et al., 2024 | 3 | Excluído | fck não declarado: N/A - estudo foca em emissoes de carbono da laje; utiliza fa |
| MISTRY et al., 2016 | 4.5 | Incluído | fck não declarado: Nao informado (verificado em todo o texto, pp. 1-8) |
| MOURA et al., 2025 | 4 | Incluído | fck não declarado: N/A - utiliza HPC (concreto de alto desempenho) reforcado co |
| MUELLER et al., 2024 | 4.5 | Incluído | fck não declarado: N/A - estudo de ACV prospectiva da producao de clinquer, nao |
| NAVARRO et al., 2022 | 3 | Excluído | fck não declarado: N/A - artigo nao especifica fck em MPa; foca em parametros d |
| ONN et al., 2019 | 5.5 | Incluído | fck não declarado: N/A - artigo reporta resistencia a compressao aos 28 dias de |
| PARATSCHA et al., 2019 | 3.5 | Excluído | fck não declarado: N/A - estudo nao especifica classe de resistencia do concret |
| PASSUELLO et al., 2014 | 4 | Incluído | fck não declarado: N/A - estudo avalia clinqueres (nao concreto estrutural); pr |
| PESTA et al., 2022 | 4.5 | Incluído | fck não declarado: N/A - classificacao como bloco leve para alvenaria sem funca |
| PRISTERA et al., 2024 | 3.5 | Excluído | fck não declarado: N/A - artigo de revisao sistematica sobre demolição seletiva |
| PUSHKAR et al., 2020 | 3.5 | Excluído | fck não declarado: Viga base (PNSC): C40/50 segundo EN-206-1; SFHSC (Caso 1): C |
| QAMHIA et al., 2023 | 3.5 | Excluído | fck não declarado: N/A (pavimentos; sem concreto estrutural convencional) (veri |
| RIHNER et al., 2025 | 3 | Excluído | fck não declarado: N/A - revisao sistematica (verificado em todo o texto, pp. 1 |
| RINNE et al., 2022 | 4.5 | Incluído | fck não declarado: N/A — estudo de edifício; densidades adotadas: concreto = 24 |
| ROHDE et al., 2023 | 4 | Incluído | fck não declarado: N/A - foco em sistemas estruturais de aco e madeira; concret |
| ROSA et al., 2017 | 2.5 | Excluído | fck não declarado: N/A — estudo de produção de cimento, não analisa resistência |
| ROSALES et al., 2020 | 3.5 | Excluído | fck não declarado: N/A (pavimento/sub-base; sem concreto estrutural) (verificad |
| RUIZ SANCHEZ et al., 2021 | 4 | Incluído | fck não declarado: N/A (cimento como material; sem concreto estrutural especifi |
| SANCHEZ-BURGOS et al., 2024 | 5 | Incluído | fck não declarado: N/A (artigo nao especifica fck do concreto da laje; concreto |
| SANDAGOMIKA et al., 2024 | 4.5 | Incluído | fck não declarado: Nao informado (artigo nao especifica classe de resistencia d |
| SANGIORGIO et al., 2025 | 3.5 | Excluído | fck não declarado: N/A — estudo analisa fôrmas impressas em 3D para concretagem |
| SANTOS et al., 2022 | 4.5 | Incluído | fck não declarado: N/A (material nao e concreto estrutural; e composto cimentic |
| SANTOS, 2015 | 4 | Incluído | fck não declarado: N/A — estudo analisa cinzas pesadas como resíduo industrial  |
| SANTOS, 2022 | 3 | Excluído | fck não declarado: N/A — compósito geopolimérico; sem fck estrutural definido;  |
| SBAHIEH et al., 2022 | 2.5 | Excluído | fck não declarado: Nao informado (artigo e revisao bibliografica; cita estudos  |
| SENSENEY et al., 2023 | 2.5 | Excluído | fck não declarado: N/A - estudo sobre politica de procurement e declaracoes amb |
| SHANBHAG et al., 2024 | 3 | Excluído | fck não declarado: N/A — hempcrete não é material estrutural portante; destinad |
| SONG et al., 2020 | 4.5 | Incluído | fck não declarado: N/A - artigo de revisao sobre metodologia de ACV aplicada a  |
| UGURAL et al., 2024 | 3.5 | Excluído | fck não declarado: Nao informado (artigo nao especifica classe de resistencia d |
| VENTURA et al., 2022 | 5 | Incluído | fck não declarado: N/A (material nao e concreto estrutural; e composto cimentic |
| VIDAL et al., 2019 | 5 | Incluído | fck não declarado: N/A - estrutura principal em madeira CLT; concreto apenas na |
| VLADIMIROV et al., 2019 | 4.5 | Incluído | fck não declarado: N/A - material composto (GRP), sem resistencia caracteristic |
| VOLK et al., 2024 | 4 | Incluído | fck não declarado: N/A — material de isolamento (não concreto estrutural); dens |
| WOLFOVA et al., 2020 | 3.5 | Excluído | fck não declarado: N/A - estudo nao reporta resistencia caracteristica dos mate |
| XIAO et al., 2014 | 3.5 | Excluído | fck não declarado: N/A — estudo de carbonatacao mineral de escoras siderurgicas |
| ZUCARATO, 2020 | 3.5 | Excluído | fck não declarado: N/A — não aplicável; o estudo avalia a produção de cimento P |

### 4.4 Artigos N/A — UF incompatível com m³ (20)

| Estudo | Score AQ | UF declarada |
|---|---|---|
| ABOUHAMAD et al., 2020 | 4.5 | 1 m² de área de piso por ano (p. 5, 10-11) |
| ABUSHANAB et al., 2025 | 3.5 | USD/m² de área construída ao longo de 50 anos; custos normalizados por m² de piso para comparar edifícios de 20 a 70 and |
| ADAMS et al., 2024 | 3.5 | 1 dm² de área de material produzido (correspondente à área típica das técnicas de deposição de filmes finos) (p. 4) |
| ANDERSEN et al., 2022 | 4.5 | 1 m² médio de edifício de apartamentos de 5-8 andares por 100 anos em países escandinavos (p. 2) |
| ARRIGONI et al., 2018 | 4 | (i) 1 kg de mistura SRE e (ii) 1 m² de parede portante acabada com espessura 300 mm (p. 16) |
| FERREIRA et al., 2023 | 6 | 1 kg de material (unidade declarada); resultados normalizados por m2 de area de vendas (9556 m2) (p. 9, 11) |
| GALAN-MARIN et al., 2016 | 5 | Superficie total das paredes em cada caso; resultados normalizados por m2 por ano de vida util (p. 6, 12) |
| HAFEZ et al., 2024b | 5 | 1 m² de laje de concreto armado de uma via (one-way slab), calculada como volume de concreto por m² × espessura total, i |
| HERTWICH et al., 2019 | 3.5 | Sem UF unica - revisao cita diferentes: kg CO2eq/m3 de madeira, kg CO2/kg aco, por m2 de area de piso, por veiculo (p. 6 |
| KOH et al., 2025 | 4 | Sem UF explicitamente declarada; resultados expressos por m2 de painel (espessura 15mm, dimensoes 300x200mm) (p. 2, 9, F |
| LEI et al., 2023 | 3.5 | kgCO2-e por m2 de area construida ('carbon dioxide equivalent generated per unit building area') (p. 4) |
| MALABI EBERHARDT et al., 2024 | 3.5 | m² de área útil por ano (p. 5) |
| MILANI et al., 2020 | 5 | 1 m² de superestrutura de ponte. (p. 14) |
| PAPADAKI et al., 2022 | 4.5 | Apartamento residencial de 108,3 m² localizado em Atenas, Grécia, com vida útil de 25 anos (p. 3-4) |
| PESTA et al., 2020 | 6 | 1 m² de sistema de parede. (p. 1) |
| SIKORA et al., 2023 | 4.5 | 1 m² de parede interna não estrutural com o mesmo perfil térmico (U=0,3 W/m²K) (p. 1) |
| SILVA et al., 2023 | 2 | 1 m² de calçada/pavimento (em estudos citados na revisão) (p. 19) |
| SOMBRIO, 2015 | 5 | 1,312 m² de painel (p. 8) |
| TELLO-AYALA et al., 2023 | 5 | Uma casa de interesse social unifamiliar de dois pavimentos; resultados expressos por m2 de construcao (p. 11) |
| VALENCIA-BARBA et al., 2020 | 5 | 1 m² de sistema de laje (p. 7) |

### 4.5 Artigos excluídos por qualidade (score < 4) sem col R (12)

| Estudo | Score AQ | Nota |
|---|---|---|
| AKBULUT et al., 2024 | 1.5 | Excluído da síntese — ci pode ser calculado para análise descritiva futura |
| ANKUR et al., 2024 | 3 | Excluído da síntese — ci pode ser calculado para análise descritiva futura |
| CHEN et al., 2024a | 3 | Excluído da síntese — ci pode ser calculado para análise descritiva futura |
| CHEN et al., 2024b | 3 | Excluído da síntese — ci pode ser calculado para análise descritiva futura |
| JANG et al., 2022 | 3.5 | Excluído da síntese — ci pode ser calculado para análise descritiva futura |
| LI et al., 2025 | 3.5 | Excluído da síntese — ci pode ser calculado para análise descritiva futura |
| MA et al., 2021 | 2 | Excluído da síntese — ci pode ser calculado para análise descritiva futura |
| MOHAJERANI et al., 2019 | 3 | Excluído da síntese — ci pode ser calculado para análise descritiva futura |
| PEDROSO et al., 2024 | 3.5 | Excluído da síntese — ci pode ser calculado para análise descritiva futura |
| SAMEER et al., 2020 | 3.5 | Excluído da síntese — ci pode ser calculado para análise descritiva futura |
| VAN LOON et al., 2019 | 3.5 | Excluído da síntese — ci pode ser calculado para análise descritiva futura |
| YU et al., 2023 | 3.5 | Excluído da síntese — ci pode ser calculado para análise descritiva futura |

---

## 5. Orientações para preenchimento futuro dos 43 pendentes

Para cada artigo na seção 4.2, abrir o PDF em `ARTIGOS ACEITOS DA RSL/` e localizar:
1. **GWP (kg CO₂eq/m³):** normalmente em tabela de resultados ou figura de barras
2. **fck ou fc (MPa):** classe de resistência do traço principal (usar fck nominal se fcm disponível: fck = fcm − 8 MPa, EN 206)
3. **ci = GWP ÷ fck** → registrar em col R da aba ANÁLISE
4. Se vida útil for declarada: **ci_t = ci ÷ vida_útil** → registrar em col S

**Prioridade:** artigos com score AQ ≥ 5 e Status = Incluído.

---

## 6. Próximos passos

- [ ] Extrair ci dos 43 artigos pendentes (prioridade: score ≥ 5)
- [ ] Decidir sobre 103 estudos incluídos ausentes da METANÁLISE (UF incompatível)
- [ ] Declarar na dissertação: "X artigos sem ci calculável por fck não declarado" e "Y por UF incompatível com m³"
- [ ] Verificar se col S precisa ser populada para mais estudos (localizar vida útil nos PDFs dos pendentes)

---
*Log gerado automaticamente por Claude (Cowork) em 2026-05-18. Verificado por Kiê.*
