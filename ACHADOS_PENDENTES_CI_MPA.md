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

## BLOQUEADOS (precisam de reabrir por outra via, não é dúvida de critério)

- **LYRA 2023i (dados_fck linhas 763-770, row_id 2847).** Armadilhas nº7+nº8
  combinadas (`read_file_content` truncado, `download_file_content` "session
  expired" 3×). Já resolvido antes para `vida_util_anos` via
  `shrink-drive-pdf.yml` com `first_page`/`last_page` — repetir a mesma
  técnica para o volume.
