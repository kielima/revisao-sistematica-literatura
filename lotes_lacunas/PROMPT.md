# Lacunas de vida útil, dispersão (IC) e volume do corpo de prova — instruções por lote (2026-09-29)

Estás a ajudar a completar a base `dados_fck` de uma metanálise de betão (resistência à compressão × CO2).
Cada artigo do teu lote já tem pares fck×CO2 gravados; falta extrair um ou mais destes campos
(o campo `extrair` de cada artigo diz quais):

- `vida_util` — vida útil de projecto/serviço DECLARADA pelo próprio artigo para a estrutura ou material
  (ex.: "service life of 50 years", "período de análise de 100 anos"). Em anos. Só o que o artigo afirma
  como premissa própria; um valor citado de outro estudo só conta se o artigo o adoptar explicitamente.
  Se houver valores diferentes por mistura, dar por par.
- `ic` — dispersão medida PELO PRÓPRIO ARTIGO, por par (por mistura):
  `ic_fck_valor`, `ic_fck_tipo` ∈ {desvio_padrao, cv_percentual, intervalo_min_max, ic_declarado},
  `ic_fck_n` (nº de réplicas, se declarado), `ic_fck_citacao` (onde: tabela/figura/página + texto curto);
  e o mesmo para CO2 (`ic_co2_*`), que normalmente não existe (ACV determinística).
  Regras: (a) dispersão copiada de outro estudo NÃO conta; (b) um STDEV no rodapé de uma tabela com
  várias misturas (dispersão ENTRE misturas) NÃO conta; (c) barras de erro só em figura: se os números
  estiverem impressos ou forem legíveis com segurança na figura renderizada, dar o valor; se não, dar
  `ic_fck_tipo` e citação com `ic_fck_valor=null` e dizer porquê. Os ± de tabelas contam como desvio_padrao
  salvo se o artigo disser outra coisa.
- `volume` — volume do corpo de prova em que o fck foi medido, em m3, e a fonte:
  `vol_corpo_prova_fonte` ∈ {medido_ensaio (corpo de prova de laboratório com dimensão declarada),
  medido_elemento_real (elemento estrutural real com dimensão declarada), norma_referencia (dimensão
  inferida da norma de ensaio citada no artigo, ex. EN 12390-3 cubo 150 mm, ASTM C39 cilindro 100×200 —
  só se o artigo citar a norma), indisponivel (nenhuma das anteriores; ex. classe de projecto sem ensaio)}.
  Referências: cubo 100 mm = 0,001; cubo 150 mm = 0,003375; cubo 50 mm = 0,000125; cubo 70,7 mm = 0,000353;
  cilindro 100×200 = 0,0015708; cilindro 150×300 = 0,0053014; prisma 40×40×160 = 0,000256.
  Dar também `vol_corpo_prova_citacao` (texto curto + página).
- De caminho, se o par ainda não tiver: `tipo_corpo_prova` (cubo/cilindro/prisma + dimensões) e
  `idade_dias` do ensaio de fck. Só se estiver explícito.

## Como ler
- Use `mcp__Google_Drive__read_file_content` com o `fileId` (carregue a ferramenta com ToolSearch
  "select:mcp__Google_Drive__read_file_content,mcp__Google_Drive__download_file_content"). O resultado
  grande fica gravado num ficheiro: leia-o todo, em blocos sequenciais.
- Se o `fileId` for null, procure na pasta 1R63Q4Lzz6JRRLpwES1Ngyod04q0-r9YP com
  `mcp__Google_Drive__search_files` (query `parentId = '1R63Q4Lzz6JRRLpwES1Ngyod04q0-r9YP' and title contains 'APELIDO'`)
  e confirme título/DOI na primeira página.
- Para dispersão só visual (barras de erro), descarregue o PDF (`download_file_content`, base64; ficheiros
  acima de ~6 MB costumam falhar — nesse caso diga-o) e renderize as páginas relevantes com pymupdf
  (dpi 200) para ver. Não invente números.
- Teses longas: `read_file_content` pode truncar sem aviso a partir de ~135–180 mil caracteres. Se o texto
  acabar antes da secção de resultados, diga-o explicitamente em vez de concluir "não existe".
- Casar cada valor com o par certo pelo `material` (nome do traço) e pelo fck gravado. Se não conseguir
  casar com segurança, não preencha e explique.

## Proibições
- Não contacte nenhum serviço externo além do Google Drive; nunca envie nenhum endereço de email a lado nenhum.
- Não edite ficheiros do repositório nem planilhas. Escreva APENAS o ficheiro de resultado indicado.

## Saída
Grave `lotes_lacunas/resultado_loteNN.json` (NN = número do lote) com uma lista, um objecto por artigo:
{"row_id":..., "lido":"integral|parcial (porquê)", "notas":"...",
 "pares":[{"sheet_row":..., "vida_util_anos":num|null, "vida_util_citacao":"...",
   "ic_fck_valor":num|null, "ic_fck_tipo":..., "ic_fck_n":int|null, "ic_fck_citacao":"...",
   "ic_co2_valor":..., "ic_co2_tipo":..., "ic_co2_n":..., "ic_co2_citacao":"...",
   "vol_corpo_prova_m3":num|null, "vol_corpo_prova_fonte":"...", "vol_corpo_prova_citacao":"...",
   "tipo_corpo_prova":str|null, "idade_dias":num|null}]}
Inclua só os campos que o artigo tinha em `extrair` (mais tipo/idade se encontrados). Campos procurados
e não encontrados: null + explicação na citação correspondente (ex. "nao declarado no artigo inteiro").
No fim responda com um resumo curto: por artigo, o que encontrou e qualquer caso incomum.
