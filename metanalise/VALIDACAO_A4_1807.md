# Validação do motor do A4 contra os pares com A4 publicado (F49, tarefa #1807, 2026-11-16)

Fase 4 do plano da F40. Compara o A4 que o motor (F48, `metanalise/motor_a4.py`) atribuiria a cada par com o A4 que o
próprio artigo publica (`dados_fck` col 80 `co2_a4`, extraído na F39). Script: `metanalise/validar_a4.py` →
`metanalise/transporte_a4_validacao.csv` (um registo por par). Nada em `dados_fck`, no painel ou no modelo muda.

## 1. Universo

| | pares | estudos |
|---|---|---|
| com `co2_a4` publicado | 140 | 46 |
| **A4 > 0** (comparáveis) | **65** | **26** |
| A4 = 0 | 75 | 20 |

Os 75 pares com A4 = 0 não são medições: são **exclusões explícitas** do transporte do betão pelo artigo
(«A4 neglected», «transportation is not considered», fronteira A1–A3 com A4 declarado fora — ver `etapas_nota`
da F39: WAGNER 4993, BORGES 4997, ALSALMAN 3071, RADOVIC 4092, GOH 3182, SABAU 3321, …). Ficam fora da comparação;
para o motor são o caso normal do grupo `sim` (A4 não está no valor e soma-se da grelha).

Dos 65 pares comparáveis, 43 estão no grupo `nao` (A4 já incluído no `co2_kg_m3` — o motor não lhes soma nada),
13 no grupo `sim` e 9 no `provavel`. Em **todos** os 26 estudos a massa volúmica é a premissa F43 (2.400 kg/m³):
nenhum deles estava nas 14 listas da fase 2 (são quase todos `nao`, por isso nunca foram lidos para massa) — a
#1860 cobre os de `sim`/`provavel`.

## 2. Factor implícito (16 estudos que imprimem a distância central→obra)

factor implícito = A4 publicado ÷ (2,4 t/m³ × distância declarada em `transporte_dados`)

| estudo | distância (km) | factor implícito kg CO₂/(t·km) | o que o artigo diz usar (`transporte_dados`, F37) |
|---|---|---|---|
| 5041 BENTO 2016 | 60 | 0,051 | processo «US: Truck» do software |
| 5050 BRAGA 2018 | 20,5 | 0,056 | 0,0136 L diesel/(t·km), truck articulado 27 t |
| 4349 ZAHABI 2025 | 40 | 0,068 | Tally defaults |
| 3221 LIN 2025 | 40 | 0,078 | 0,000129 kg CO₂e/(kg·km) |
| 4753 BACKES 2023 | 250 | 0,084 | processo GaBi, truck euro4 28–32 t |
| 2803 STARCZYK-KOLBYK 2024 | 50 | 0,104 | calculadora Circular Ecology (ICE) |
| 4255 GAO 2024 | 40 | 0,108 | 0,104 kg CO₂e/(t·km), gasolina |
| 4724 LEI 2022 | 20 | 0,108 | 0,111 |
| 4869 MEL 2015 | 30 | 0,110 | auto-hormigonera, ~30 km |
| 4786 ZHAO 2024 | 40 | 0,148 | 0,162 kg CO₂/(t·km) |
| 3225 JIANG 2025 | 40 | 0,151 | — |
| 4756 HUBER 2024 | 20 | 0,171 | 85,1 g/(t·km) truck (+ comboio/navio) |
| 3615 ALKHAWALDEH 2024 | 30 | 0,250 | NREL 0,2542 kg CO₂/(t·km) short-haul |
| 3003 ZHANG 2018 | 30 | 0,278 | 0,674 kg CO₂/(m³·km) |
| 4841 ABD RASHID 2017 | 50 | 0,361 | 0,848 kg CO₂/tkm (16 t); 0,939 (betoneira 24 t) |
| 4297 PUSHKAR 2022 | 50 | 0,392 | 0,376 kg CO₂/tkm (Tab.6, ecoinvent lorry 22 t) |

- **Mediana 0,109 kg CO₂/(t·km)** (mín. 0,051; máx. 0,392). O factor SIDAC da **betoneira (0,10) fica na mediana da
  literatura**; os 3 factores de camião/carreta (0,07/0,07/0,06) ficam no terço inferior (5 dos 16 estudos abaixo
  da betoneira; 2–3 abaixo das carretas).
- Razão mediana «motor ÷ publicado» na distância declarada: **0,67 (betoneira)**, 0,47 (truck e carreta 4 eixos),
  0,40 (carreta 5 eixos). Ou seja, com o SIDAC o A4 sai, em mediana, ~1/3 abaixo do que os artigos calculam para
  a mesma distância em betoneira, e ~metade nos outros modos.
- Onde o factor implícito bate com o declarado (GAO 0,108 vs 0,104; LEI 0,108 vs 0,111; HUBER 0,171 vs 0,085 — o
  dobro, porque o artigo soma comboio e navio; ZHAO 0,148 vs 0,162) a reconstrução confirma que a leitura de
  `co2_a4` e a premissa de 2.400 kg/m³ são coerentes com os artigos (massa real ~2.300–2.400).
- Os 4 estudos acima de 0,25 explicam-se pelo factor que usam, não pela distância: ZHANG 3003 aplica 0,674 kg
  CO₂/(m³·km) (≈0,28/t·km) a 30 km «assumidos»; ALKHAWALDEH usa o NREL short-haul (0,254); ABD RASHID imprime
  0,85–0,94 kg CO₂/tkm, 8–9× o SIDAC (provável factor por veículo·km ou com retorno em vazio, a confirmar no PDF
  se for preciso); PUSHKAR usa 0,376 kg CO₂/tkm do ecoinvent «Euro 0-4 mix, 22 t». São factores de inventário
  diferentes, legítimos nos seus contextos — não são erro de extracção.

## 3. Distância implícita (26 estudos)

distância implícita = A4 publicado ÷ coeficiente SIDAC (factor × 2,4 t/m³), por estudo (mediana dos pares)

| modo | mediana | p10 | p90 | dentro da grelha 0–300 km |
|---|---|---|---|---|
| betoneira (0,24 kg/(m³·km)) | 55 km | 22 | 210 | **24 de 26** |
| carreta 5 eixos (0,144) | 92 km | 36 | 349 | 20 de 26 |

Fora da grelha com a betoneira só **DERVISHAJ 2641/2650** (108 kg CO₂/m³ → 450 km): o A4 é do Boverket por **kg de
elemento pré-fabricado** (0,045 kg CO₂e/kg, Tab.2), aplicado a um elemento inteiro — não é transporte de betão
fresco e o estudo está no grupo `nao` (A4 já no valor; o motor não lhe soma nada). A grelha 0–300 km × 4 modos
cobre, portanto, todos os A4 publicados de betão.

## 4. Peso do A4 no CO₂ do par

A4 publicado = **3,5 % do CO₂ do par** em mediana (p10 1,3 %; p90 15,4 %), por estudo. O motor dá, no grupo `sim`
em betoneira, +3,5 % a 50 km e +7,0 % a 100 km (F48): a ordem de grandeza coincide com a literatura para
distâncias de 30–60 km, que é o que os 16 estudos com distância declaram (mediana 40 km).

## 5. Conclusão

O motor é **plausível**: (i) os A4 publicados reconstroem-se com a fórmula factor × massa × distância e a premissa
de 2.400 kg/m³ (coerência a ±10 % nos estudos que declaram factor e distância); (ii) a grelha 0–300 km cobre todos
os A4 publicados de betão; (iii) o peso relativo bate (3–7 %). O **viés conhecido** é o factor: o SIDAC betoneira
(0,10) é a mediana da literatura, os camiões/carretas do SIDAC (0,06–0,07) estão no terço inferior, e os estudos
que usam ecoinvent/NREL/factores por veículo chegam a 0,25–0,39 kg CO₂/(t·km). Com o SIDAC, o A4 somado sai, em
mediana, 1/3 abaixo (betoneira) a metade (carretas) do que esses artigos calculariam para a mesma distância.

**Recomendação (por confirmar pela Kiê, #1808/#1809):** manter os factores SIDAC como base (decisão F40: factores
nacionais, 4 modos) e dar ao painel/modelo uma **sensibilidade de factor** (ex.: ×1,5 e ×2,5 sobre a betoneira, que
é a faixa 0,15–0,25 observada) em vez de trocar de fonte; a distância da grelha já cobre a dispersão. A dúvida do
regresso em vazio (F40/F48) continua aberta e explicaria parte da diferença (um factor com retorno vazio ≈ 1,5–2×).
