# Achados pendentes da extração ci_mpa — para resolver com a Kiê depois de todos os lotes

> Criado 2026-09-24. A Kiê pediu para correr todos os ~30 lotes da extração de
> `vol_corpo_prova_m3` primeiro, e só depois voltar a estes achados, um a um.
> Este ficheiro acumula tudo o que precisa da decisão dela — não resolver
> sozinho, só registar aqui à medida que aparece.

## Da Onda 1 (lotes 01-05)

1. **DI MARIA et al. 2020 (dados_fck linhas 116-118, row_id 2653).** O próprio
   artigo é internamente inconsistente sobre o volume da unidade funcional —
   imprime "0,008 m³" duas vezes, mas também imprime peso=92kg e
   densidade=2300kg/m³ para a mesma FU, o que dá 0,04 m³ (5× maior). Há ainda
   um possível descasamento de escala entre `fck` (1 bloco, 0,0008 m³) e o
   `co2_valor` (FU inteira, 50 blocos). Pergunta: qual volume usar, ou deixar
   `indisponivel`?

   ✅ **RESOLVIDO 2026-09-25 (decisão da Kiê, após leitura completa do PDF por mim).**
   O artigo imprime três volumes diferentes para a FU (0,008 m³ no texto, 0,08 m³ na
   Tabela 3), mas duas vias independentes convergem em **0,04 m³**: 92 kg ÷ 2300 kg/m³,
   e 50 blocos × 20×10×4 cm (a frase "800 cm³" é o volume de *um* bloco). O
   `co2_valor` já registado tinha sido derivado com o divisor errado (0,008) numa
   sessão anterior — corrigido para divisor 0,04: S1 −136,25→−27,25; S2 −245→−49;
   S3 −170→−34 kg CO2-eq/m³. `vol_corpo_prova_m3` = 0,04 (medido_ensaio).

2. **GALANO 2023i (dados_fck linha 773, row_id 2864).** `fck`=30 é do concreto
   M30 da laje (referência externa) mas `co2_valor`=134,43 é do *mortar
   filler* usado para selar fissuras — dois materiais distintos. Par
   fisicamente incoerente. Pergunta: rever ou remover esta linha de
   `dados_fck`?

   ✅ **RESOLVIDO 2026-09-25 (decisão da Kiê, após leitura completa do PDF + figuras).**
   A premissa do achado estava errada: a Fig. 2 mostra que o Caso 1 é o sistema
   inteiro (19,1 m³ de concreto = 99,1% + argamassa 0,86%), não só a argamassa. O
   problema real era outro: a Sec. 3.2 diz que a Tabela 2 contém só CO2 de
   "land transformation and biogenic sources" — não o GWP total (~7 kg/m³, sem o CO2
   fóssil do cimento). `co2_valor` removido das 3 linhas (773-775); sem CO2 válido
   no artigo, row_id 2864 → `E2_co2`=Rejeitado, `status_triagem`=Rejeitado (regra
   E2 de 2026-09-21). `fck`=30 (classe M30 citada) estava correto — classe de
   projeto/citada vale na metanálise.

3. **JONES 2024d (dados_fck linhas 790-791, row_id 2902).** Linha 791
   (fck=35, co2=405) vem de uma frase hipotética/contrafactual do artigo, não
   de material real. Linha 790 (fck=78, co2=983, material real) tem dois
   volumes candidatos igualmente válidos na Tabela 2 (161 m³ ou 203 m³, dois
   designs distintos). Pergunta: descartar a 791? Como decidir entre os dois
   volumes da 790?

   ✅ **RESOLVIDO 2026-09-25 (decisão da Kiê, após leitura completa + Figs. 7-10 e
   Tabela A4 via recorte `shrink-drive-pdf.yml`).** A 791 **não** é hipotética: o
   texto cita a mistura real de 35 MPa impressa do estudo companheiro [23] — mantida,
   volume `indisponivel`. A 790 fica com **161 m³** (Short Flat Ribbed Beam, projeto
   final). **Achado novo:** o concreto convencional de 35 MPa (material principal das
   4 fundações) faltava no banco — adicionado como linha 1863 (fck 35, CO2 364 =
   983/2,7 pela razão impressa, confiança média, volume 1015 m³ da fundação Tapered).
   QF 1,0 → 0,5, total 5,0 → 4,5, continua `principal`.

## Da Onda 2 (lotes 06-10)

4. **SANDANAYAKE et al. 2022 (dados_fck linha 814, row_id 3035).** O
   `co2_valor`=109,95 registado no banco não é o CO2 absoluto do geopolímero —
   o texto diz explicitamente "the alkali activated soil filter cake achieved
   a total GHG emission reduction of 109.95 kgCO2-eq/m³ compared with CEM-I,
   which equates to approximately 31%" (Secção 5.1): 109,95 é uma
   redução/delta frente ao CEM-I, não o valor absoluto próprio do
   geopolímero. O valor absoluto não está impresso em texto (só na Fig.3,
   gráfico não renderizado). Pergunta: manter o delta, ou tentar reconstituir
   o absoluto (precisaria também do valor absoluto do CEM-I, que também não
   está impresso directamente)?

   ✅ **RESOLVIDO 2026-09-25 (decisão da Kiê, após leitura completa + Figs. 3-6 a 300dpi).**
   A Fig. 4 dá o CEM-I em 465 kg/m³ (eixo com grelha de 20); 465 − 109,95 = **355**,
   confirmado pela barra da Fig. 3 (~351-355) e pelos 31% (109,95/355 — os autores
   calcularam sobre o geopolímero). `co2_valor` 109,95 → 355, confiança média. Por
   ser reconstrução nossa, **QF 0,5 → 0**, total 4,0 → 3,5, estrato principal →
   sensibilidade. Volume continua `indisponivel`.

5. **ZHANG et al. 2025, UHPC com resíduos de molibdénio (dados_fck linha 933,
   row_id 3222).** O campo `fck_mpa` é composto (5 misturas na mesma célula:
   "MT0(controlo):104.98; MT25:105.27; MT50:107.15; MT75:108.27;
   MT100:109.32"). O texto diz explicitamente que o controlo MT0 atingiu
   107,15 MPa — mas esse valor já está na célula, só que atribuído a MT50,
   não a MT0. As percentagens de aumento que o artigo lista para as outras 4
   misturas não reconciliam de forma monótona com os valores impressos
   (parece haver uma troca de rótulos ou erro do próprio artigo). Pergunta:
   como reatribuir os 5 valores às 5 misturas correctas — ou fica assim?

   ✅ **RESOLVIDO 2026-09-26** (leitura completa do PDF + renderização Fig.10/18,
   decisão Kiê). Os parênteses da sec.5.3 são gralha do artigo; a Fig.10a
   (altura das barras pela geometria vetorial) dá 107,16/108,27/108,93/109,33/109,53,
   igual a 107,15×(1+%) do texto. `fck_mpa` corrigido para MT0 107,15 → MT100 109,53.
   CO2 trocado da leitura do radar pelo cálculo exacto Tab.5×Tab.7
   (443,61/443,33/443,05/442,78/442,50; MT0−MT100 = 1,11 kg, como no texto).
   QF mantém 1, artigo continua 3,5 (sensibilidade).

6. **MENG et al. 2023, ponte (dados_fck linha 939, row_id 3241).** A linha é
   composta e mistura dois elementos estruturais reais distintos, cada um
   com o seu próprio volume: laje do tabuleiro C30 (secção única 5×3×0,5m =
   7,5 m³/secção, 24 secções) e encontro/abutment C40 (63,47 m³ totais, sem
   dimensão de elemento único). `fck_mpa` já é um texto composto
   ("C30:30; C40:40; ..."). Pergunta: dividir esta linha em duas (uma por
   classe/elemento, cada uma com o seu volume), ou manter `indisponivel`
   para a linha toda?

   ✅ **RESOLVIDO 2026-09-26** (leitura completa do PDF, Tab.1-9; decisão Kiê).
   Linha dividida: 939 = C30 (fck 30, 295 kgCO2e/m³, 178,51 m³, laje do
   tabuleiro, Tab.3-5); nova linha 1864 = C40 (fck 40, 340 kgCO2e/m³,
   257,61 m³, Tab.4 — encontro 63,47 + estrutura especial inferior 194,14;
   o subagente só tinha visto os 63,47). Volumes = quantitativo total do
   projecto, `medido_elemento_real`. CO2 do betão impresso 3D e do de cinza
   volante saíram de `co2_valor` (sem classe → sem par), ficam só na nota.
   E4 inalterado (3,0, sensibilidade).

## Da Onda 3 (lotes 11-15)

7. **DI SARNO et al. 2024 (dados_fck linhas 364-365, row_id 3348).** O artigo é
   internamente inconsistente sobre a forma do corpo de prova: descreve os
   ensaios de resistência à compressão como feitos em "cubes
   (100×100×500mm)" — a mesma dimensão impressa para os PRISMAS de flexão
   ("prisms (100×100×500mm)"), fisicamente impossível para um cubo (lados
   desiguais). fck/co2 continuam corretos e confirmados; só o volume do
   corpo de prova ficou por resolver (mantido `indisponivel`, sem assumir
   qual dimensão está certa). Pergunta: a Kiê tem acesso a outra versão do
   artigo (errata, versão publicada final) que possa esclarecer a dimensão
   real do cubo?

   ✅ **RESOLVIDO 2026-09-26** (leitura completa do PDF + renderização
   pp.9-13; decisão Kiê). "×500" é erro tipográfico copiado da linha dos
   prismas; forma cúbica confirmada pelo texto ("cubes" em 6.2 e 6.2.3) e
   pelas fotos (Fig.14/16). Linhas 364-365: `vol_corpo_prova_m3` = 0,001
   (cubo 100 mm), `medido_ensaio`. fck (Fig.10) e CO2 (Tab.5) reconfirmados.

8. **BAYAT et al. 2024 (dados_fck linhas 441/443, row_id 3504).** A unidade
   funcional (FU) do artigo não é 1 m³ fixo — varia entre 1,4554 e 1,4799 m³
   por mistura, conforme a durabilidade/cobrimento de armadura de uma viga
   de 6 m (Tabela 4). Os valores de CO2 (352/356 kg CO2-eq, confirmados
   exatos no texto) aparecem só na Fig.12, rotulados apenas "kg of CO2eq"
   — sem dizer se é por m³ de material ou total da FU-viga inteira. Sem
   saber a unidade real, aplicar a fórmula `CO2_total = co2_valor × volume`
   pode ficar fisicamente inválida. Corpo de prova físico real está
   confirmado e disponível (cubo 100mm, ASTM C39) para o dia em que a Kiê
   decidir a unidade. Pergunta: o valor da Fig.12 é por m³ ou é o total da
   viga-FU?

   ✅ **RESOLVIDO 2026-09-26** (leitura completa do PDF + medição da Fig.12
   por pixel; decisão Kiê). A Fig.12 está em m³-equivalentes da viga de
   referência (segmento PC = cimento × 906,23 kg/t × volume relativo da FU,
   Tab.4) — ou seja, por m³, não o total da viga. Descoberta extra: os valores
   do texto (ZS30 352, S40 356) contradizem a figura e as percentagens nela
   impressas (−30%/−29% face a R≈475). CO2 das 10 misturas (linhas 435-444)
   passa a vir da figura ÷ volume relativo (R 475 … ZS40 300 kg/m³); volume do
   corpo de prova = cubo 100 mm (0,001 m³, `medido_ensaio`). QF 1→0, total
   6→5, continua principal.

9. **AYGUN 2025 (dados_fck linha 450, row_id 3525).** O artigo reporta o
   CO2 do geopolímero de forma internamente inconsistente entre secções:
   ~100 kg/m³ (Secção LCIA), ~200 kg/m³ (Secção TOPSIS), ~400 kg/m³
   (Conclusões, igual ao valor isolado do estágio "matéria-prima"), e 475
   kg/m³ (soma dos 4 estágios do ciclo de vida, já registado em
   `dados_fck` como `[DERIVADO]`). Não há evidência textual de qual dos
   quatro é "o" valor correto do artigo. Sem dimensão de corpo de prova
   declarada em lado nenhum do texto de qualquer forma (então mesmo que a
   unidade se resolvesse, o volume continuaria `indisponivel`). Pergunta:
   manter o valor `[DERIVADO]` de 475 que já está na célula, ou é melhor
   marcar como incerto?

   ✅ **RESOLVIDO 2026-09-26** (leitura completa do PDF + figuras; decisão
   Kiê). CO2 **rejeitado**: são cinco valores contraditórios (~100, 200, 400,
   475 derivado e ~295 pela Fig.8, onde a matéria-prima está a ~0 contra 400
   no texto) para um geopolímero genérico, nunca atribuído a nenhuma das 5
   misturas ensaiadas. O fck de 50 MPa era da série PEF após 270 d em Mg₂SO₄
   (a Fig.5 mostra ~55). `co2_valor` da linha 450 removido; row_id 3525 →
   E2_co2 Rejeitado, status Rejeitado, etapa 2 (mesmo tratamento do GALANO).

## Da Onda 4 (lotes 16-20)

10. **CUNNINGHAM 2021 (dados_fck linha 1084, row_id 3732).** `co2_valor`=469,8
    kg CO2-eq/m³ vem de uma equação hiperbólica (y=469,8/x) que o próprio
    artigo diz explicitamente só ser válida para "bioash-cement mortars"
    (misturas com cinza) — mas esta linha representa o CONTROLE 100% PC
    (fck=42,1 MPa, Tabela 3), não uma mistura com cinza. O mesmo parágrafo
    do artigo trata "the control PC mortar" como referência separada. O
    valor real do controle só aparece na Fig.2c/d (gráfico, não extraível
    por texto) — não verificado. `fck` está confirmado correto; só o
    `co2_valor` pode estar a usar a fórmula errada. Corpo de prova físico
    real existe e tem dimensão declarada (cilindro 50mm×100mm) — o volume
    seria 0,0001963 m³ se o par ficar confirmado. Pergunta: o
    `co2_valor`=469,8 é mesmo do controle, ou pertence a outra mistura?

    ✅ **RESOLVIDO 2026-09-26** (leitura completa do PDF + medição vetorial das
    Figs.2c/3; decisão Kiê). O 469,8 é das argamassas **com cinza**. Controlo
    (linha 1084): CO2 → 543 kg/m³ (Fig.3: 14,20 × 38,2; Fig.2c ≈540) e fck
    42,1 → 38,2 (42,1 era aos 56 dias, a linha dizia 28). Acrescentadas as 16
    misturas com cinza (linhas 1865-1880, fck 28 d da Tab.3, CO2 469,8).
    Volume cilindro 50×100 mm (0,0001963 m³, `medido_ensaio`) em todas. QF
    1→0,5, total 4,5, continua principal.

11. **LI/ZHU, monorail (dados_fck linha 1162, row_id 4012).** O `co2_valor`
    registado (54.255,77 t CO2/km) é o CO2 total do ciclo de vida de 50
    anos da linha inteira, normalizado por km — uma métrica de
    escopo/unidade completamente diferente do formato habitual "kg
    CO2/m³". O mesmo artigo tem, na Tabela 2, um fator de produção
    específico por classe que bate exatamente com `fck`=50 (a maior
    classe fisicamente usada, 13,59 m³): 510,94 kg CO2/m³ — na unidade
    certa e específico da classe já registada. Há também C20=201,38,
    C25=250,54, C30=306,78, C40=391,03 kg/m³, cada um com quantidade real
    do projeto. Pergunta: trocar o `co2_valor` desta linha pelo 510,94
    kg/m³ da Tabela 2 (aí sim calculável com o volume 13,59 m³), ou manter
    o valor actual (que fica fora do escopo do `ci_mpa`)?

    ✅ **RESOLVIDO 2026-09-26** (leitura completa do PDF; decisão Kiê). O
    valor antigo era pior do que parecia: 54.255,77 t/km é a emissão da
    **eletricidade de operação** dos comboios da linha inteira em 50 anos,
    não CO2 de betão. Linha 1162 → C50, 510,94 kg/m³, 13,59 m³; acrescentadas
    C20/C25/C30/C40 (linhas 1881-1884) com fator e quantidade da Tabela 2.
    Volumes `medido_elemento_real` (quantitativo do projeto). E4 inalterado.

**Nota metodológica sobre 5 linhas RESOLVIDO da Onda 4 (row_ids 3930, 3944,
4255 — GAO, edifícios inteiros):** nestas linhas, o "elemento real" usado
como `medido_elemento_real` é a quantidade agregada de uma classe de
concreto usada num edifício real inteiro (soma de tabela de quantitativos
do próprio artigo), não um único membro estrutural isolado (viga/pilar)
como o exemplo literal do protocolo sugere. Os números vêm de tabelas de
quantitativo (BOQ/takeoff) reais do artigo e o `ci_mpa` resultante é
coerente, mas é uma extensão da categoria 2 do protocolo — mesmo padrão já
usado antes (STOIBER, MONCASTER nas ondas 1-3) e agora confirmado de novo
em maior escala. Não é uma dúvida bloqueante, só um ponto para a Kiê
confirmar se quer manter esta leitura mais ampla da categoria daqui em
diante (parece que sim, dado o uso já repetido).

## Da Onda 6 (lotes 26-30, última onda — todos os 437 artigos cobertos)

12. **JI et al. 2022 (dados_fck linha 1695, row_id 4705).** O `vol_corpo_prova_m3`
    desta linha já estava preenchido (0,75) por trabalho de uma sessão
    anterior a esta extração — mas ao reconferir contra a Tabela 1 do
    artigo, o par `fck`=35,3 corresponde à linha "On-site TC, 60°C"
    (Width=487,8mm, 28-Day Strength=35,3MPa, Concrete Volume=**0,714**
    m³), não 0,75 (esse é o volume de outra linha da tabela, "20°C",
    fck=33,6MPa). Não foi corrigido por estar fora do escopo desta
    extração (só se preenchem células vazias). Pergunta: corrigir
    0,75→0,714?

    ✅ **RESOLVIDO 2026-09-26** (leitura completa do PDF; decisão Kiê). Volume
    0,75 → 0,714 m³ (Tabela 1, TC 60 °C; 0,75 era a coluna de referência da
    FU). O erro contaminava também o CO2/m³: 295,5 kg/coluna ÷ 0,714 = 413,9
    kg/m³ (antes 394, dividido por 0,75). Linha 1694 (UHPC 50 °C) conferida,
    sem alteração.

13. **ASCIONE et al. 2024 (dados_fck linha 598, row_id 4820).** O
    `fck_mpa`=30 registado nesta linha corresponde, pela leitura do
    artigo, à resistência à compressão paralela às fibras (fc,0,k) da
    classe de madeira lamelada colada GL30h (Tabela 2), não à
    resistência de concreto — já visível no próprio campo
    `material`/`classe_resistencia` da linha ("classe GL30h (fc,0,k)").
    Não é erro de leitura (o valor bate com o texto), parece inclusão
    deliberada de uma sessão anterior comparando sistemas estruturais
    aço/concreto/madeira híbrida (edifício Mjøstårnet). Mesma família do
    caso AL OMAR/vergalhão já tratado retroativamente no protocolo.
    Pergunta: aplicar o mesmo tratamento (retirar do funil de `ci_mpa`,
    já que não é concreto)?

    **✅ RESOLVIDO 2026-09-26 (decisão Kiê, opção A).** A premissa não se
    aplica: fc,0,k é compressão paralela às fibras e glulam é material
    aceite — a linha fica, como **família madeira**, não sai do funil (ao
    contrário do AL OMAR, cuja grandeza era tração). O problema real era o
    CO2: 132 "tCO2e/m²" (Tab.11) é o edifício inteiro por m² de área, com
    lajes de betão (68%, Fig.28b), CLT e LVL — não pareável ao GL30h, e com
    a unidade errada no próprio artigo (1193 t / 132 ⇒ ~9000 m², logo
    kg/m²). Substituído por **138,24 kgCO2e/m³** = fator A1–A5 do timber
    frame (Tab.8: 0,28+0,005+0,003 kg/kg) × densidade GL30h (Tab.3: 480
    kg/m³), com `[ALERTA ETAPA4: valor derivado]`, confiança baixa. QF já
    era 0; total E4 inalterado (3, sensibilidade). Volume continua
    `indisponivel` (valor característico normativo, sem provete).

14. **MEDEIROS 2016 (dados_fck linha 50, row_id 5040, tese UFMT).** O
    `co2_valor` já é um total absoluto (soma Fundação+Superestrutura =
    812.132,42 kg CO2eq), não uma taxa kg/m³. O artigo tem, nas mesmas
    duas etapas, as quantidades reais de concreto 25MPa (Fundação=630,00
    + Superestrutura=989,21 = 1.619,21 m³) que batem exatamente com essa
    agregação — mas como o `co2_valor` já não é kg/m³, multiplicar por
    esse volume duplicaria a escala (daria um `ci_mpa` inválido). Só faria
    sentido calcular `ci_mpa = co2_valor / fck` diretamente, sem volume —
    fora do escopo desta extração (que só preenche `vol_corpo_prova_m3`).
    Pergunta: este padrão ("CO2 já agregado em total absoluto + volume
    real do próprio artigo") merece uma via de cálculo própria no
    protocolo (`ci_mpa` sem passar por `vol_corpo_prova_m3`), para não
    perder estes casos?

    **✅ RESOLVIDO 2026-09-26 (decisão Kiê, opção A).** Não é precisa via
    nova: gravar a linha como taxa por m³ de betão (812.132,42 ÷ 1.619,21
    = **501,56 kg CO2eq/m³**) com `vol_corpo_prova_m3`=1.619,21
    (`medido_elemento_real`, Tab.3/4) faz `co2 × vol` devolver exactamente
    o total publicado, e o `ci_mpa` sai pela fórmula normal (≈32.485 kg
    CO2eq/MPa). Achado extra: o total inclui 92.722,77 kg de aço CA-50,
    181,96 m³ de formas e transporte (Tab.3/4), e a Fig.23 só decompõe por
    processo — impossível isolar o betão. Linha na **família betão
    armado** (precedente KONTRA 4931), `[ALERTA ETAPA4: valor derivado;
    inclui aço, formas e transporte]`, confiança média. QF já era 0;
    total E4 inalterado (5, principal).

## BLOQUEADOS (precisam de reabrir por outra via, não é dúvida de critério)

- **LYRA 2023i (dados_fck linhas 763-770, row_id 2847).** Armadilhas nº7+nº8
  combinadas (`read_file_content` truncado, `download_file_content` "session
  expired" 3×). Já resolvido antes para `vida_util_anos` via
  `shrink-drive-pdf.yml` com `first_page`/`last_page` — repetir a mesma
  técnica para o volume.

  **✅ RESOLVIDO 2026-09-26 (decisão Kiê, opção A).** PDF inteiro comprimido
  (`/screen`, 2,4 MB) e lido. CP cilíndrico 5×10 cm (p.77-78 impressas) →
  `vol_corpo_prova_m3`=1,9635e-4 (`medido_ensaio`). Achado: os fluxos de
  referência da Tab.7 (UF "1 MPa") são o material de UM cilindro dividido
  pelo fck — Tab.7 × fck / volume dá massa específica 2.270–2.272 kg/m³
  constante nas 8 argamassas. CO2 convertido de kg/MPa para kg/m³
  (co2 × fck / vol): 556,6 / 554,6 / 528,3 / 482,9 / 423,5 / 518,8 /
  469,6 / 395,5, `[DERIVADO]`, confiança média.
