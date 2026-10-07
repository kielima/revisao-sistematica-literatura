# CO2 bruto vs CO2 com desconto (créditos) — releitura integral (2026-10-07)

Pedido da Kiê (2026-10-07): «quero ter uma opção para poder ver os dois cenários com o desconto e sem o desconto […] criar uma nova coluna para CO2 descontado e reabrir todos os PDFs para ver quais declaram CO2 descontado e quais só o CO2 bruto».

**Desconto / crédito** = qualquer parcela que o artigo SUBTRAI ao CO2 de produzir o betão/mistura:
- `carga_evitada` — produção evitada (cimento, agregado natural, clínquer, aço/gusa recuperado), aterro/deposição evitado, «avoided product», substituição de energia;
- `carbonatacao` — CO2 reabsorvido pelo betão ao longo da vida/fim de vida, ou captado por cura com CO2 / mineralização;
- `biogenico` — carbono biogénico armazenado (madeira, cânhamo, casca de arroz, biochar…) contado com sinal negativo;
- `modulo_D` — benefícios para lá da fronteira (EN 15804 módulo D), reciclagem no fim de vida;
- `outro` — dizer qual.

Para **cada par** (`sheet_row`) do lote, ler o PDF por inteiro (texto + tabelas + figuras da ACV) e responder sobre **o valor gravado em `co2_kg_m3`** (mesma mistura, mesma unidade funcional, mesma conversão de `co2_conversao`):

1. `artigo_declara_desconto`: `sim` (o artigo apresenta, para esta mistura, algum crédito/desconto como os acima — mesmo que o gravado seja o bruto) | `nao` (a ACV não tem nenhum crédito; só CO2 bruto) | `indeterminado` (explicar).
2. `tipos_desconto`: lista dos tipos acima presentes (vazia se `nao`).
3. `gravado_e`: `bruto` (o `co2_kg_m3` gravado não tem desconto) | `liquido` (o gravado já tem o desconto) | `misto` (tem parte dos descontos) | `indeterminado`.
4. `co2_bruto`: CO2 sem nenhum desconto, **na mesma base do gravado** (kg CO2-eq/m3, mesma fronteira e conversão). Número ou `null` se o artigo não o permite obter. Pode ser calculado a partir de números impressos no próprio artigo (ex.: líquido + crédito impresso) — dizer a conta.
5. `co2_com_desconto`: CO2 com todos os descontos que o próprio artigo aplica a esta mistura, na mesma base. Número ou `null` (se `artigo_declara_desconto` = `nao`, `null`).
6. `citacao`: onde está cada número (tabela/figura/página) + a conta, se houver. `derivado`: `sim` se algum dos dois números foi calculado por nós ou lido por píxel numa figura.
7. `nota`: qualquer coisa estranha (fronteira diferente, valor gravado que não bate com o artigo, etc.).

Regras: não inventar; se o artigo só dá percentagens sem valor absoluto do crédito, `null` e explicar. Teses longas: o `read_file_content` trunca sem aviso — confirmar com o PDF descarregado. Ver figuras quando a ACV está só em figura (descarregar e renderizar com pymupdf).

Segurança: nunca enviar email ou dados pessoais a serviços externos; não usar Unpaywall nem APIs externas; só o conector do Google Drive e ferramentas locais. Não alterar ficheiros do repositório.

Saída `resultado_loteNN.json` = lista de {row_id, pares:[{sheet_row, artigo_declara_desconto, tipos_desconto, gravado_e, co2_bruto, co2_com_desconto, citacao, derivado, nota}], texto_completo_lido, notas}.
