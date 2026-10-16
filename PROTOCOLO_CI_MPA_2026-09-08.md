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
- **ci_t = kg CO₂-eq / (m³·MPa·ano)** — ⭐ **redefinido pela Kiê a 2026-10-16 (F22):** «Eu quero
  um ci_t mas não a partir do ci_mpa e sim um ci_t a partir do ci de Damineli. kg CO2/(m³ MPa).»
  `ci_t = ci ÷ vida_util_anos = (co2_kg_m3 ÷ fck) ÷ vida_util_anos`, quando a vida útil é
  declarada pelo próprio artigo. Não depende do volume. *(A definição antiga, até 2026-10-15,
  diluía o `ci_mpa` pela vida útil, em kg CO₂-eq/(MPa·ano); ficou abandonada.)* Coluna
  `dados_fck` 39 renomeada para `cit_kgco2_m3_mpa_ano`, escrita por `recalcular_ci.py`.

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

## 🆕 ONDA 1 — Lotes 01-05, 75 dos 437 artigos pendentes (2026-09-24)

**Decisão da Kiê (2026-09-24): "vamos misturar, na ordem do banco. Mas vamos abrir e reabrir todos os pdfs, pra confirmar tudo."** Sem pré-ordenar por dificuldade (balde) — os 437 artigos com par `fck_mpa`+`co2_valor` completo mas sem `vol_corpo_prova_m3` são processados na ordem do banco, em lotes de 15 artigos por subagente, cada um a reabrir o PDF por completo (não confiar no `fonte_no_pdf`/`observacoes` já escritos) e a reconferir também o par `fck_mpa`/`co2_valor` já registado, não só extrair o volume. Worklist completa em `lotes_ci_mpa/CI_MPA_WORKLIST_2026-09-24.csv` (437 artigos, 1.366 linhas de `dados_fck`); resultado de cada lote em `lotes_ci_mpa/LOTE0N_CI_MPA_2026-09-24.csv`.

**Resultado dos lotes 01-05 (75 artigos, 250 linhas de `dados_fck`):**

| Status | N | |
|---|---:|---|
| RESOLVIDO | 87 | `vol_corpo_prova_m3` preenchido |
| INDISPONIVEL | 147 | sem corpo físico/elemento com dimensão, ou co2_valor em unidade incompatível com m³ |
| BLOQUEADO | 8 | LYRA (row_id 2847) — ver achado abaixo |
| ACHADO_DIVERGENCIA | 8 | 5 corrigidos directamente (evidência textual inequívoca), 3 ficam para a Kiê decidir |

**✅ 5 correcções aplicadas directamente** (evidência textual clara, mesmo padrão já usado nas rondas anteriores de conferência):
- **Linha 654 (row_id 2694, JANG ma15145047):** `co2_valor` 420→429 — o próprio artigo (Sec.5.1) diz que 420 (4.20×10²) é só a parcela de CO₂ puro antes de somar CFC-11/114/12; o GWP/CO₂-eq final por m³ é 429 (4.29×10²), também impresso na Tabela 4.
- **Linhas 152/153 (row_id 2703, KIM et al. 2016e):** `co2_valor` estava trocado entre os dois tipos — Type2 (OPC+BFS-geral 30%) devia ter 259,14 (Case5 da Tabela 11), não 263,24 (Case4, que é do W-BFS); Type3/"4" (OPC+W-BFS 30%) devia ter 263,24, não 259,14. Trocados.
- **Linhas 144/145 (row_id 2672, SPOSITO 2024i):** campo `material` corrigido de "Painéis" para "Pastas" (Secção 4.1.3 do artigo, "AAMs pastes" — os painéis de fachada são um estudo diferente, Cap.5); `co2_valor` da linha 145 (NH-SS1.5) corrigido de 112 para 108 — o 112 pertencia à mistura NH-SS2.0, não à NH-SS1.5.

**⚠️ 3 achados que ficam para a Kiê decidir, não corrigidos:**
- **Linhas 116-118 (row_id 2653, DI MARIA et al. 2020):** o próprio artigo é internamente inconsistente sobre o volume da unidade funcional — imprime "0,008 m³" duas vezes, mas também imprime peso=92kg e densidade=2300kg/m³ para a mesma FU, o que dá 0,04 m³ (5× maior). Há ainda um possível descasamento de escala entre `fck` (1 bloco, 0,0008 m³) e o `co2_valor` (FU inteira, 50 blocos). Nenhum volume atribuído.
- **Linha 773 (row_id 2864, GALANO 2023i):** `fck`=30 é do concreto M30 da laje (referência externa) mas `co2_valor`=134,43 é do *mortar filler* usado para selar fissuras — dois materiais distintos dentro do mesmo "sistema de reparo". Par fisicamente incoerente; fica para a Kiê decidir se a linha deve ser revista ou removida de `dados_fck`.
- **Linhas 790-791 (row_id 2902, JONES 2024d):** a linha 791 (fck=35, co2=405) vem de uma frase hipotética/contrafactual do artigo, não de material realmente usado. A linha 790 (fck=78, co2=983, material real) tem dois volumes candidatos igualmente válidos na Tabela 2 (161 m³ ou 203 m³, dois designs distintos) — sem forma de saber qual corresponde a este par.

**🔴 BLOQUEADO — LYRA 2023i (row_id 2847, 8 linhas):** mesma combinação de armadilhas nº7+nº8 já documentada noutros casos — `read_file_content` parou aos ~176 mil caracteres (numa lista de notas de rodapé, sem alcançar o corpo), `download_file_content` falhou "session expired" 3× seguidas. Este mesmo artigo já foi lido com sucesso antes (para `vida_util_anos`) via `shrink-drive-pdf.yml` com `first_page`/`last_page` — é o caminho recomendado para desbloquear.

**Nota sobre unidade incompatível com m³:** confirmando o achado colateral já documentado acima (25,5% dos pares com unidade não claramente "por m³"), duas linhas desta ronda (REGÚLEZ 779/780 — kg CO₂/kg; ALONSO-CANON 792 — kg CO₂/tonelada) tinham volume real encontrado no artigo, mas foram mantidas `indisponivel` por prudência — registar `vol_corpo_prova_m3` ao lado de um `co2_valor` que não é kg/m³ habilitaria um `ci_mpa` fisicamente inválido se um script futuro não verificar `co2_unidade` primeiro. Mesmo padrão já aplicado a MA 2021, MARTINEZ-MUNOZ e SIKORA nos lotes 02-04.

**Progresso:** `vol_corpo_prova_m3` em `dados_fck` foi de 79 para 136 células preenchidas. Faltam **362 dos 437 artigos** (lotes 06-30, aprox.).

## 🆕 ONDA 2 — Lotes 06-10, mais 75 dos 437 artigos (2026-09-24)

A Kiê pediu para continuar todos os lotes sem pausa, acumulando achados em `ACHADOS_PENDENTES_CI_MPA.md` para resolver depois. Resultado dos lotes 06-10 (75 artigos, 197 linhas de `dados_fck`):

| Status | N | |
|---|---:|---|
| RESOLVIDO | 100 | `vol_corpo_prova_m3` preenchido |
| INDISPONIVEL | 94 | sem corpo físico/elemento com dimensão, ou co2_valor em unidade incompatível com m³ |
| BLOQUEADO | 0 | — |
| ACHADO_DIVERGENCIA | 3 | todos ficam para a Kiê decidir (ver `ACHADOS_PENDENTES_CI_MPA.md`) — SANDANAYAKE (delta vs absoluto), ZHANG (troca de rótulo numa célula composta), MENG (linha mistura dois elementos com volumes diferentes) |

**Confirmação de um caso-limite do protocolo:** quando o artigo reporta `co2_valor` "por 1 m³" (prática padrão de ACV) mas **também** tem um corpo de prova físico real menor (ex.: cubo 100mm) do mesmo traço, usar o volume real do corpo de prova é **válido** — não é a armadilha "FU=1m³". A armadilha só se aplica quando "1 m³" é o **único** volume mencionado no artigo inteiro, sem nenhum corpo físico menor testado. Já era o padrão seguido desde a Onda 1 (ex.: KUL, LI 2024 seawater), reconfirmado explicitamente nos lotes 06-10 (MEKKY, DACIC, SUN, MANAN, KANAGARAJ, JIANG, KANG).

**Progresso acumulado:** `vol_corpo_prova_m3` em `dados_fck` foi de 79 para **237** células preenchidas. Faltam **287 dos 437 artigos** (lotes 11-30, aprox.).

## 🆕 ONDA 3 — Lotes 11-15, mais 75 dos 437 artigos (2026-09-24)

Resultado dos lotes 11-15 (75 artigos, 211 linhas de `dados_fck`):

| Status | N | |
|---|---:|---|
| RESOLVIDO | 62 | `vol_corpo_prova_m3` preenchido |
| INDISPONIVEL | 146 | sem corpo físico/elemento com dimensão, ou co2_valor em unidade incompatível com m³ |
| BLOQUEADO | 0 | — |
| ACHADO_DIVERGENCIA | 3 | todos ficam para a Kiê decidir (ver `ACHADOS_PENDENTES_CI_MPA.md`, achados 7-9) — DI SARNO (forma do corpo de prova inconsistente no artigo), BAYAT (unidade da Fig.12 ambígua: por m³ ou total da FU-viga), AYGUN (4 valores de CO2 inconsistentes entre secções do próprio artigo) |

**⚠️ Armadilha de processo descoberta e corrigida nesta onda — numeração de linhas do worklist original ficou desatualizada para o Lote 11.** O subagente do Lote 11 já tinha avisado que os números de `dados_fck_row` do worklist (`CI_MPA_WORKLIST_2026-09-24.csv`) não correspondiam mais à posição real das linhas na planilha (provavelmente por inserções de linhas feitas por tarefas anteriores à criação do worklist) e afirmou ter corrigido isso reconsultando `row_id` diretamente — mas o CSV que devolveu continuava, na prática, com todos os 44 números de linha desviados em exactamente **+1** em relação à posição real (confirmado por comparação de `co2_valor`/`fck_mpa` idênticos, em ordem, nas posições corrigidas). Antes de aplicar, todo o CSV do Lote 11 foi corrigido (`dados_fck_row += 1` em todas as 44 linhas) e revalidado por `row_id` linha a linha — sem esse ajuste, o script de aplicação (que aborta com `assert` antes de qualquer escrita se algum `row_id` não bater) teria simplesmente recusado gravar, sem risco de corromper dados, mas ficaria bloqueado. Os lotes 12-15 não tiveram este problema (`row_id` bateu de primeira em 100% das 167 linhas restantes).

**Achado colateral de processo:** os subagentes dos Lotes 11 e 15 escreveram o seu relatório directamente como ficheiro dentro do repositório (`lotes_ci_mpa/LOTE11_CI_MPA_2026-09-24.csv` e `LOTE15_...csv`), apesar da instrução de só reportar em texto no chat. O conteúdo desses ficheiros foi conferido contra o relatório em chat (idêntico) antes de reaproveitado; os ficheiros soltos foram removidos do working tree (o CSV definitivo de cada lote só entra no repositório através do commit desta onda, em `lotes_ci_mpa/`).

**Progresso acumulado:** `vol_corpo_prova_m3` em `dados_fck` foi de 237 para **305** células preenchidas. Faltam **212 dos 437 artigos** (lotes 16-30, aprox.).

## 🆕 ONDA 4 — Lotes 16-20, mais 75 dos 437 artigos (2026-09-24)

Resultado dos lotes 16-20 (75 artigos, 187 linhas de `dados_fck`):

| Status | N | |
|---|---:|---|
| RESOLVIDO | 39 | `vol_corpo_prova_m3` preenchido |
| INDISPONIVEL | 146 | sem corpo físico/elemento com dimensão, ou co2_valor em unidade incompatível com m³ |
| BLOQUEADO | 0 | — |
| ACHADO_DIVERGENCIA | 2 | ambos ficam para a Kiê decidir (ver `ACHADOS_PENDENTES_CI_MPA.md`, achados 10-11) — CUNNINGHAM (fórmula hiperbólica do artigo só vale para misturas com cinza, aplicada por engano ao controle), LI/ZHU monorail (co2_valor registado é total do ciclo de vida por km, quando o próprio artigo tem um fator por classe/m³ mais adequado) |

**Achado de processo (não bloqueante) — auto-correção de um falso `INDISPONIVEL` de onda anterior.** O lote 19 encontrou que a linha 1199 (row_id 4110, ARCE et al. 2023) tinha sido marcada `indisponivel` por concluir (erradamente) que só existia o FU=1m³; a releitura completa achou o corpo de prova físico real (prisma de argamassa 40×40×160mm, EN 1015-11) do mesmo traço — corrigido para RESOLVIDO nesta mesma onda. Fica como lembrete de que "FU=1m³" só deve ser confirmado depois de varrer o artigo inteiro por termos de molde/prisma/cubo/cilindro, não só pela frase da unidade funcional.

**Extensão confirmada da categoria `medido_elemento_real` para quantitativos de edifícios inteiros** (ver nota em `ACHADOS_PENDENTES_CI_MPA.md`, após achado 11) — usada em mais 3 artigos nesta onda (GAO 4255, mais os já vistos em ondas anteriores), sempre com volume e CO2 vindos de tabelas de quantitativo reais do próprio artigo.

**Progresso acumulado:** `vol_corpo_prova_m3` em `dados_fck` foi de 305 para **344** células preenchidas. Faltam **137 dos 437 artigos** (lotes 21-30, aprox.).

## 🆕 ONDA 5 — Lotes 21-25, mais 75 dos 437 artigos (2026-09-24)

Resultado dos lotes 21-25 (75 artigos, 373 linhas de `dados_fck`):

| Status | N | |
|---|---:|---|
| RESOLVIDO | 130 | `vol_corpo_prova_m3` preenchido |
| INDISPONIVEL | 243 | sem corpo físico/elemento com dimensão, ou co2_valor em unidade incompatível com m³ |
| BLOQUEADO | 0 | — |
| ACHADO_DIVERGENCIA | 0 | nenhuma divergência de fck/co2 encontrada nesta onda |

**Onda com o maior rendimento até agora** — 130 RESOLVIDO em 373 linhas (35%), acima da média das ondas anteriores. Três padrões novos/reforçados:

- **Segunda tabela de quantitativos** (lote 21): dois artigos (MOSTAFAEI 4304, ALMULHIM 4321) tinham uma tabela de fatores GWP/m³ E uma segunda tabela de quantitativos reais de material («bill of quantities») por classe — só a segunda dá o volume real. Regra a levar para lotes futuros: nunca concluir `indisponivel` num artigo com quantitativos de edifício real sem procurar por essa segunda tabela.
- **Regra do FU normalizado por resistência** (lote 24, artigo 4580, 20 linhas): quando o próprio artigo declara que o `co2_valor` já vem "normalizado pela resistência aos 28 dias" (kg CO2/MPa, não kg CO2/m³ bruto), multiplicar por um volume duplicaria a normalização — mantido `indisponivel` mesmo com unidade nominalmente "kg CO2-eq/m³" na coluna do banco. Nova variante da regra de incompatibilidade de unidade, mais sutil que as anteriores (a etiqueta da unidade não denuncia o problema, só a leitura do texto).
- **Norma de ensaio com mais de um tamanho válido** (lotes 23-24): quando a norma citada (ex.: ASTM C39, que permite cilindro 4×8in OU 6×12in) não fixa uma dimensão única e o artigo não diz qual usou, a via `norma_referencia` não se aplica — mantido `indisponivel`. Confirma e formaliza a exceção já usada informalmente antes.

Um achado de rótulo (não é `ACHADO_DIVERGENCIA` de fck/co2): linha 1381→row_id 4463 (SAMEER, lote 22) tinha `tipo_corpo_prova` registado como "cubo 150mm" mas o artigo atribui o `fck` ao corpo **cilíndrico** (150×300mm) da classe C50/60, não ao cubo — sinalizado para a Kiê corrigir esse campo separadamente, não bloqueante para `ci_mpa`.

**Progresso acumulado:** `vol_corpo_prova_m3` em `dados_fck` foi de 344 para **474** células preenchidas. Faltam **62 dos 437 artigos** (lotes 26-30, aprox.).

## 🆕🏁 ONDA 6 — Lotes 26-30, últimos 62 dos 437 artigos (2026-09-24)

**Última onda — cobre a totalidade dos 437 artigos do worklist `CI_MPA_WORKLIST_2026-09-24.csv`.** Resultado dos lotes 26-30 (62 artigos, 187 linhas de `dados_fck`):

| Status | N | |
|---|---:|---|
| RESOLVIDO | 52 | `vol_corpo_prova_m3` preenchido |
| INDISPONIVEL | 135 | sem corpo físico/elemento com dimensão, ou co2_valor em unidade incompatível com m³ |
| BLOQUEADO | 0 | — |
| ACHADO_DIVERGENCIA | 1 | JI et al. 2022 — ver `ACHADOS_PENDENTES_CI_MPA.md`, achado 12 |

**Três achados novos** registados em `ACHADOS_PENDENTES_CI_MPA.md` (achados 12-14): um volume já preenchido por sessão anterior que parece errado (JI et al., 0,75 vs 0,714 m³), uma linha cujo `fck_mpa` é na verdade resistência de madeira laminada, não de concreto (ASCIONE et al., mesma família do caso AL OMAR/vergalhão), e um padrão metodológico novo (MEDEIROS 2016) em que `co2_valor` já é total absoluto e bate exatamente com um volume real do próprio artigo, mas a regra de incompatibilidade de unidade impede aplicar — candidato a uma via de cálculo alternativa do `ci_mpa`.

**Padrões novos confirmados nesta onda:**
- **Soma de elementos reais com a mesma taxa** (MAURY-RAMIREZ, lote 26): uma linha de `dados_fck` que agrega dois elementos estruturais reais distintos (vigas aéreas + vigas de fundação) com a mesma taxa de CO2/m³ — resolvido somando os volumes reais dos dois, reproduzindo exatamente o total publicado.
- **Ambiguidade "duas configurações do mesmo edifício"** (BAEK et al., lote 28): fator de emissão idêntico usado em dois cenários estruturais comparados (Referência vs Alternativo) do mesmo edifício, mas a linha do banco não distingue a qual cenário pertence e as quantidades reais diferem entre os dois — mantido `indisponível` por ambiguidade de pareamento, não catalogado antes.
- **Truncamento (armadilha nº7) atingiu 5 dos 15 artigos do lote 29** (teses/dissertações longas: SCHMIDT, FARIAS, REZENDE, SANTOS, ISAIA) — em todos esses casos a conclusão final já era `indisponível` por incompatibilidade de unidade (independente de fck/co2), então o truncamento não mudou nenhum resultado desta vez, mas fica registado para auditoria futura se necessário.

**Progresso final:** `vol_corpo_prova_m3` em `dados_fck` foi de 474 para **526** células preenchidas. **Os 437 artigos do worklist estão cobertos — não há mais lotes pendentes desta extração.** Restam só os achados acumulados nas Ondas 1-6 (14 no total) para a Kiê resolver, um a um, conforme pedido.
