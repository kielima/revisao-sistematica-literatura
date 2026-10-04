# Lotes de volume do provete pela norma citada (2026-10-04)

Objectivo: para cada par fck×CO2 de artigos Elegíveis sem `vol_corpo_prova_m3`, identificar no PDF a **norma citada pelo próprio artigo** que define o provete do valor de fck gravado. A Kiê decidiu (2026-10-04) assumir o provete-padrão dessa norma quando o artigo não dá as dimensões.

Para cada `sheet_row`:
1. **Dimensões declaradas:** se o artigo der as dimensões do provete do ensaio de compressão (ex.: "cubes of 100 mm", "cylinders 100 × 200 mm"), registar em `dimensoes_declaradas` com a citação. Nesse caso o volume vem das dimensões reais, não da norma.
2. **Norma do ensaio:** a norma de ensaio de compressão ou de moldagem citada pelo artigo para esse fck (ex.: ASTM C39, ASTM C31, ASTM C109, EN 12390-3, EN 12390-1, BS 1881, GB/T 50081, IS 516, NBR 5739, NBR 5738, AS 1012.9, KS F 2405, JIS A 1108, EN 196-1).
3. **Norma da classe:** se o fck gravado é uma classe ou resistência de projecto sem ensaio, a norma citada que define a classe (ex.: EN 206, EN 1992-1-1, ACI 318, NBR 6118, NBR 8953, GB 50010, AS 1379, EHE-08, IS 456, fib MC2010). A notação Cxx/yy (EN 206) e HA-xx (EHE-08) contam como norma mesmo sem citação explícita (regra da Kiê de 2026-10-04); registar `EN 206 (notacao)` ou `EHE-08 (notacao)`.
4. **Tipo de valor:** dizer se o valor gravado é de cubo, de cilindro ou de prisma, quando o artigo o diz ou a notação o implica (em Cxx/yy o primeiro número é de cilindro).
5. **Sem norma:** se não houver norma citada nem dimensões (ex.: «25 MPa concrete» de uma base de inventário sem norma), `norma` = null e tipo `sem_norma`. Nunca inventar nem deduzir uma norma pelo país.

Ler o PDF completo (texto e, se preciso, figuras e tabelas). Atenção à armadilha de truncagem em teses longas: confirmar com o PDF descarregado.

Segurança: nunca enviar email ou dados pessoais a serviços externos; não usar Unpaywall nem APIs externas; só o conector do Google Drive e ferramentas locais. Não alterar ficheiros do repositório.

Saída: `resultado_loteNN.json` = lista de {row_id, pares:[{sheet_row, tipo ('dimensoes'|'norma_ensaio'|'norma_classe'|'sem_norma'), norma (string|null), dimensoes_declaradas (string|null), provete ('cubo'|'cilindro'|'prisma'|'outro'|null), valor_de ('cubo'|'cilindro'|'prisma'|null), citacao, nota}], texto_completo_lido, notas}.
