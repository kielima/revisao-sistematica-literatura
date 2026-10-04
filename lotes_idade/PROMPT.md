# Lotes de idade do ensaio de resistência (2026-10-04)

Objectivo: preencher `idade_dias` (col 10 de `dados_fck`) nos pares fck×CO2 de artigos Elegíveis em que está vazia, lendo o PDF.

Regras:
- Para cada par (`sheet_row`), encontrar a idade (dias) do ensaio de compressão a que corresponde **o valor de fck gravado** (`fck_mpa`). Confirmar que o número gravado aparece no artigo para essa idade (tabela/figura/texto).
- Se o fck gravado é uma **classe de resistência / resistência de projecto** (ex.: C30/37, "30 MPa concrete", EPD) sem ensaio próprio: `idade_dias` = 28 **só se** o artigo ou a norma citada no artigo o disser (ex.: "28-day characteristic strength", EN 206/EN 1992); senão `null` com tipo `classe_sem_idade`.
- Se o artigo não diz a idade do valor gravado: `null` (nunca inventar; não presumir 28 d).
- Se o fck gravado não corresponde ao valor de 28 d mas existe valor aos 28 d para a mesma mistura, reportar em `notas` (não alterar fck).
- Ler o PDF completo (texto; renderizar figuras/tabelas quando a idade só estiver numa figura). Atenção à armadilha de truncagem em teses longas.
- Segurança: nunca enviar email ou dados pessoais a serviços externos; não usar Unpaywall nem APIs externas; só o conector do Google Drive e ferramentas locais. Não alterar ficheiros do repositório.

Saída: `resultado_loteNN.json` = lista de {row_id, pares:[{sheet_row, idade_dias (int|null), tipo ('ensaio'|'classe_28d_declarada'|'classe_sem_idade'|'nao_declarada'), citacao (local + texto curto), nota}], texto_completo_lido, notas}.

## Regra acrescentada depois dos lotes (decisão da Kiê, 2026-10-04)
- Classe escrita no artigo na notação de uma norma que a define aos 28 d (Cxx/yy da EN 206, HA-xx da EHE-08) conta como 28 d mesmo sem a norma citada (`aplicar_notacao.py`). Valores soltos em MPa sem norma continuam `null`.
