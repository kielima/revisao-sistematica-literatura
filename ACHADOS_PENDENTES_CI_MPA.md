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

2. **GALANO 2023i (dados_fck linha 773, row_id 2864).** `fck`=30 é do concreto
   M30 da laje (referência externa) mas `co2_valor`=134,43 é do *mortar
   filler* usado para selar fissuras — dois materiais distintos. Par
   fisicamente incoerente. Pergunta: rever ou remover esta linha de
   `dados_fck`?

3. **JONES 2024d (dados_fck linhas 790-791, row_id 2902).** Linha 791
   (fck=35, co2=405) vem de uma frase hipotética/contrafactual do artigo, não
   de material real. Linha 790 (fck=78, co2=983, material real) tem dois
   volumes candidatos igualmente válidos na Tabela 2 (161 m³ ou 203 m³, dois
   designs distintos). Pergunta: descartar a 791? Como decidir entre os dois
   volumes da 790?

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

5. **ZHANG et al. 2025, UHPC com resíduos de molibdénio (dados_fck linha 933,
   row_id 3222).** O campo `fck_mpa` é composto (5 misturas na mesma célula:
   "MT0(controlo):104.98; MT25:105.27; MT50:107.15; MT75:108.27;
   MT100:109.32"). O texto diz explicitamente que o controlo MT0 atingiu
   107,15 MPa — mas esse valor já está na célula, só que atribuído a MT50,
   não a MT0. As percentagens de aumento que o artigo lista para as outras 4
   misturas não reconciliam de forma monótona com os valores impressos
   (parece haver uma troca de rótulos ou erro do próprio artigo). Pergunta:
   como reatribuir os 5 valores às 5 misturas correctas — ou fica assim?

6. **MENG et al. 2023, ponte (dados_fck linha 939, row_id 3241).** A linha é
   composta e mistura dois elementos estruturais reais distintos, cada um
   com o seu próprio volume: laje do tabuleiro C30 (secção única 5×3×0,5m =
   7,5 m³/secção, 24 secções) e encontro/abutment C40 (63,47 m³ totais, sem
   dimensão de elemento único). `fck_mpa` já é um texto composto
   ("C30:30; C40:40; ..."). Pergunta: dividir esta linha em duas (uma por
   classe/elemento, cada uma com o seu volume), ou manter `indisponivel`
   para a linha toda?

## BLOQUEADOS (precisam de reabrir por outra via, não é dúvida de critério)

- **LYRA 2023i (dados_fck linhas 763-770, row_id 2847).** Armadilhas nº7+nº8
  combinadas (`read_file_content` truncado, `download_file_content` "session
  expired" 3×). Já resolvido antes para `vida_util_anos` via
  `shrink-drive-pdf.yml` com `first_page`/`last_page` — repetir a mesma
  técnica para o volume.
