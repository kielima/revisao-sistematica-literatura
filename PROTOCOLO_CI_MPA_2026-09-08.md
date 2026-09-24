# Protocolo — indicadores ci_m3 / ci_mpa / ci_t (painel kielima.com/metanalise)

> Criado 2026-09-08, na conversa com a Kiê sobre dividir o indicador `ci` do
> painel em três. Este é o ponto central da dissertação da Kiê: entender como
> o CO₂ já emitido na produção do material é aproveitado pela resistência
> que ele entrega. Ficheiro-mestre de definições — atualizar aqui sempre que
> uma decisão nova for tomada, do mesmo espírito que `lotes_etapa2/PROMPT_E2.md`.

## As três grandezas

- **ci_m3 = kg CO₂-eq / m³** — já existe, é o campo `co2_valor` de `dados_fck`
  sozinho, sem dividir por resistência. Intensidade de carbono por volume de
  material, sem nenhum ajuste por desempenho.
- **ci_mpa = kg CO₂-eq / MPa** — **grandeza nova**, ainda não calculável a
  partir do que já está no banco. Não é o `ci` actual (que é
  `co2_valor/fck`, ou seja `kg/(m³·MPa)` — a "carbon intensity" do Damineli
  et al. 2010, que o painel já usa). `ci_mpa` responde a uma pergunta
  diferente: "para o **lote físico real** que foi de facto ensaiado (o
  corpo de prova ou o elemento estrutural), quanto CO₂ esse lote específico
  carregava e quanta resistência ele entregou por esse CO₂" — não uma
  intensidade normalizada por 1 m³ hipotético.
- **ci_t = kg CO₂-eq / (MPa·ano)** — dilui `ci_mpa` pela vida útil de
  projecto (`vida_util_anos`), quando declarada. Continua a não ter volume
  nenhum embutido.

## Por que `ci_mpa` não sai só de reescalar `ci_m3`

MPa é uma grandeza intensiva (força/área) — não carrega volume. `co2_valor`
é sempre uma intensidade volumétrica (kg/m³). Multiplicar `co2_valor` por
MPa nunca faz o "por m³" desaparecer, só o esconde dentro do numerador.
Para chegar a `kg CO₂-eq / MPa` de verdade, o numerador tem de ser um
**total absoluto de CO₂**, não mais uma intensidade — e a única forma
correta é multiplicar `co2_valor` pelo **volume real do material que foi
ensaiado** para produzir aquele MPa.

```
vol_corpo_prova_m3 = volume do corpo de prova / elemento (m³)
CO2_total_kg        = co2_valor (kg/m3) × vol_corpo_prova_m3
ci_mpa               = CO2_total_kg / fck_mpa
ci_t                 = ci_mpa / vida_util_anos
```

Confirmado com a Kiê (2026-09-08): o volume tem de ser o **volume real que
cada estudo de facto usou**, nunca um valor fixo convencionado por nós — é
justamente essa variação real entre estudos que a Kiê quer capturar (não
anular). Um volume-padrão fixo para todos os pares só reescalaria `ci_m3`
por uma constante, sem trazer informação nova.

## Fonte do volume — ordem de prioridade

1. **Corpo de prova de ensaio, com dimensão declarada no artigo** (cilindro,
   cubo, prisma — a maioria dos casos).
2. **Elemento estrutural real analisado pela ACV** (pilar, viga, laje,
   parede, bloco pré-moldado etc.), quando o artigo dá as dimensões desse
   elemento e a resistência reportada é a desse elemento — autorizado pela
   Kiê 2026-09-08 ("podem ter ACVs que analisam 1 elemento como um pilar ou
   uma viga real, e se tiver as dimensões também da pra converter").
3. **Norma de ensaio citada, quando ela fixa uma única dimensão possível**
   (ex.: ASTM C109 → cubo 50mm; EN 196-1 / UNE-EN 196-1 / NBR 7215 /
   EN 1015-11 → prisma 40×40×160mm). Autorizado pela Kiê 2026-09-08, mas só
   para "modelos computacionais" (sem corpo de prova físico) que **citem**
   uma norma de ensaio com dimensão-padrão — normas de **fator de emissão**
   (EN1992 GWP/kg, EN206/EPD, GB51366-2019) não contam, só normas de
   **dimensão de corpo de prova** (EN 12390, ASTM C39, IS 516 etc. — e só
   quando a norma citada não permitir mais de um tamanho válido).
4. Nada disso disponível → a linha fica **sem `ci_mpa`/`ci_t`**, mas mantém
   `ci_m3` normalmente (mesmo padrão já usado para `vida_util_anos` em falta).

## Armadilhas já encontradas (2026-09-08, na análise do universo)

- **"FU=1m³" pode ser a unidade funcional da ACV, não o corpo de prova.**
  O campo `tipo_corpo_prova` às vezes traz "FU=1m³" ou "1m³ (demonstrador)".
  Como `co2_valor` já é sempre por 1 m³ (é a própria unidade funcional
  padrão de ACV de concreto), aceitar "1m³" como se fosse o volume do
  corpo de prova ensaiado devolveria `ci_mpa` numericamente igual ao `ci`
  actual — nenhuma informação nova, e um erro conceptual silencioso.
  Volumes "não-1m³" vindos do texto (ex.: "0,008 m³, demonstrador
  industrial") não têm este problema — só o valor exacto "1m³" é suspeito.

  ✅ **As 2 linhas confirmadas por leitura completa (2026-09-24), a armadilha aplica-se às duas.**
  `dados_fck` linha 842 (`row_id` 3099, GARCES et al. 2021, geopolymer self-healing): o
  próprio texto diz "*The functional unit was taken to be 1 m3 of concrete blocks with
  50 MPa compressive strength*" — é a FU da ACV, não um bloco físico ensaiado (o `fck`
  desta linha já vinha marcado "FU de projecto, sem ensaio próprio"). `dados_fck` linha
  1201 (`row_id` 4110, ARCE et al. 2023, argamassa alcali-ativada): "*The functional
  unit applied in this analysis is 1 m3 of mortar*" — mesmo padrão. Ambas com
  `vol_corpo_prova_fonte=indisponivel`; ficam com `ci_m3` normal, sem `ci_mpa`/`ci_t`.

- **✅ Achado de contaminação de dados — vergalhão não tem `fck` — RESOLVIDO (2026-09-24).**
  `fck` é a notação de resistência característica **à compressão do concreto**; vergalhão
  (aço de reforço) é caracterizado por resistência **à tração** (fy/fu), ensaio e
  propriedade física diferentes. As 2 linhas de `dados_fck` (`row_id` 3821 — Al Omar &
  Abdelhadi 2024, *"Comparative Life-Cycle Assessment of Steel and GFRP Rebars"*) com
  `fck_mpa` = 690 e 1207 foram **removidas de `dados_fck`**, confirmado por PDF reaberto
  integralmente: a Tabela 1 do artigo rotula-os explicitamente "**Tensile strength**:
  Steel Rebars 483-690 MPa" / "GFRP Rebars 517-1207 MPa" — e nem sequer é dado primário do
  próprio estudo (nota 1 da tabela: "*Data from [17] Barker, C. (2016)... McGill
  University*"). O artigo inteiro é uma ACV comparativa pura de vergalhão (aço vs GFRP)
  para um "screed pre-cast hollow core topping" — não há nenhum `fck` nem CO2 de concreto
  em lado nenhum do texto, só do vergalhão. **Achado adicional, mais grave que a limpeza
  de `dados_fck`:** sem par fck+CO2 de concreto pareável, este artigo (`row_id` 3821)
  falha o critério E2 mais restritivo (Kiê, 2026-09-21) — foi rejeitado retroactivamente
  em `articles_final.xlsx` (`status_triagem`/`E2_resistencia`/`E2_co2`→Rejeitado), o mesmo
  tratamento dos 58 artigos já purgados nessa ronda; a nota "o aço entra" de
  `CRITERIOS_E_NUANCES_RSL.md` autoriza estruturas metálicas como família própria quando o
  estudo é sobre a estrutura em si, não autoriza tratar resistência de vergalhão de reforço
  como `fck` de concreto (mesma leitura já aplicada ao caso STOIBER/LOTE_36 e à regra 11
  MADDALENA da Etapa 2).

## Fora de escopo (confirmado com a Kiê, 2026-09-08)

- **Unidade funcional por massa** ("tonelada de cimento", "1 kg de cimento
  produzido") — normalização por massa, não por volume; precisaria de mais
  uma suposição (densidade) para virar volume. Fica fora de `ci_m3`/
  `ci_mpa`/`ci_t` como definidos agora — poderia ser um 4º indicador à
  parte no futuro, não implementado.
- Casos "outra grandeza" que não são resistência à compressão do concreto
  (vergalhão — ver acima) saem do `dados_fck`, não só do `ci_mpa`.

## Campos novos em `dados_fck`

- **`vol_corpo_prova_m3`** — o volume calculado, numérico, auditável (não
  só o `ci_mpa` já pronto — permite conferir a conta e reaproveitar para
  outro indicador derivado no futuro).
- **`vol_corpo_prova_fonte`** — categórica, uma de:
  `medido_ensaio` (corpo de prova de laboratório com dimensão declarada) |
  `medido_elemento_real` (elemento estrutural real com dimensão declarada) |
  `norma_referencia` (dimensão inferida de norma citada, sem corpo físico) |
  `indisponivel` (nenhuma das anteriores). Serve para o filtro que a Kiê
  pediu no site: mostrar só estudos com corpo de prova medido vs. só os
  modelos computacionais (Kiê, 2026-09-08, resposta 2).

## Panorama medido em 2026-09-08 (1.953 linhas de `dados_fck`)

| Balde | N | Situação |
|---|---:|---|
| RESOLVIDO (sem reabrir PDF) | 219 | dimensão numérica já no texto extraído |
| VAZIO | 820 | `tipo_corpo_prova` nunca preenchido |
| GENÉRICO_PRECISA_LER | 541 | tem nota mas sem dimensão |
| FORMA_SEM_DIMENSÃO | 104 | forma conhecida (cubo/cilindro), tamanho não |
| ELEMENTO_REAL_SEM_DIM | 58 | pilar/viga/laje/parede mencionados, sem dimensão |
| SEM_CORPO_FÍSICO | 197 | modelo computacional/classe de projeto/EPD |
| OUTRA_GRANDEZA | 14 | não é fck de concreto (vergalhão, UCS, FU por massa) |

Dos 197 "sem corpo físico": só 11 já citam alguma norma no texto extraído,
e as 11 são normas de **fator de emissão**, não de **dimensão de corpo de
prova** — ou seja, nenhuma das 197 tem hoje um atalho pronto; todas vão
precisar de reabertura de PDF para aplicar a regra da norma referenciada
(prioridade 3 acima).

Script de classificação (não escreve nada, só lê e categoriza):
`/tmp/.../scratchpad/classify_corpo_prova.py` desta sessão — reproduzir se
for preciso reclassificar após mudanças no banco.

## ⚠️ Achado colateral urgente, ainda por resolver com a Kiê (2026-09-08)

Durante o piloto (ver abaixo), ao ler o MENEGATTI et al. 2022 (`dados_fck`
linha 185), descobriu-se que `co2_unidade` (col 15) **nem sempre é kg/m³**,
apesar de `metanalise-export.py` e o site tratarem `co2_valor` sempre como
se fosse. Medição: **369 dos 1.447 pares (25,5%) têm uma unidade que não é
claramente "por m³"** — por m², por tonelada, por kg, por elemento inteiro
(viga/coluna/torre/casa), por metro linear, por espécime, e (o mais grave)
pelo menos 3 linhas em que o próprio artigo já publica `kg CO2-eq/(m³·MPa)`
— ou seja, o `ci` já pronto, sendo dividido de novo por MPa no export.
Dois exemplos confirmados como já visíveis, incorretos, no gráfico ao vivo:
linha 3 (Assunção 2020, `co2_valor=0,176 kg/(m³·MPa)` tratado como kg/m³) e
linha 1484 (Vitale et al. 2021, `co2_valor=0,394 kg/espécime 40x40x160mm`
tratado como kg/m³) — ambos aparecem como pontos de CO₂ quase-zero no
scatter. **Isto afeta o `ci_m3`/`ci` já publicados, não só o `ci_mpa`
novo** — provavelmente é a causa dos pontos com CO₂ perto de zero ou
negativo no painel. Decisão de prioridade (resolver isto primeiro vs.
junto com o `ci_mpa`, já que ambos precisam de reabrir os mesmos artigos)
ainda pendente de resposta da Kiê nesta conversa.

## Plano de execução (Kiê, 2026-09-08, resposta 4)

1. **Piloto de 12 linhas** — cobrindo os vários baldes (VAZIO, GENÉRICO,
   FORMA_SEM_DIMENSÃO, ELEMENTO_REAL, SEM_CORPO_FÍSICO), lidas por completo
   por mim, para validar o protocolo antes de escalar.
2. **Lotes seguintes**, com confirmação da Kiê a cada lote — mesmo padrão
   da Etapa 2.
3. **No final, integrar esta extração às ondas anteriores da reauditoria
   da metanálise** que ficaram por completar (a série de "ondas" já
   documentada em `meta_analysis_base.xlsx` → aba `LEGENDA`).
