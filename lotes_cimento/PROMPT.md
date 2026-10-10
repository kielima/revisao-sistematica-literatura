# Tipo de cimento por par — releitura integral (2026-10-10)

Pedido da Kiê (2026-10-10): «todos esses [cimentos] que já existem em mercado deixe como opc. E dentro da família do cimento Portland crie subfamílias (CP I, CP II-E, CEM II, V, PLC, etc.), cada uma com um botão de informação explicando-a e referenciando as normas e/ou outros documentos técnicos».

Para **cada par** (`sheet_row`) do lote, ler o PDF por inteiro (secção de materiais, tabelas de traço e de ACV; ver figuras quando necessário) e responder:

1. `cimento_designacao`: o cimento usado nesta mistura, **exactamente como o artigo o escreve** (ex.: «CP II-E-32», «CEM I 52.5 R», «CEM II/A-LL 42.5 R», «ASTM C150 Type I», «Type IL», «OPC 53 grade», «P·O 42.5», «ordinary Portland cement»). `null` se o artigo não diz.
2. `norma_cimento`: a norma que o artigo cita para esse cimento (ex.: «EN 197-1», «NBR 16697», «ASTM C150», «ASTM C595», «IS 269», «GB 175»), ou `null` se não cita nenhuma. Não deduzir a norma: só a que o artigo escreve.
3. `ligante`: `cimento_comercial` (o ligante é só um cimento tal como vendido, mesmo que seja composto, de escória ou pozolânico) | `substituicao_no_traco` (o próprio estudo junta ao cimento uma adição — cinza, escória, sílica, argila calcinada, resíduo… — em percentagem do ligante) | `outro` (geopolímero, álcali-ativado, sem cimento Portland…) | `indeterminado`.
4. `teor_clinquer_ou_adicoes`: se o artigo dá a composição do cimento (% de clínquer ou de adições), copiar; senão `null`.
5. `citacao`: página, secção/tabela e a frase curta onde está o cimento e a norma.
6. `nota`: tudo o que for estranho (cimento diferente entre ACV e ensaio, «CEM II» sem /A ou /B, cimento citado só como factor da base de dados, etc.).

O PDF está no Drive na pasta `1R63Q4Lzz6JRRLpwES1Ngyod04q0-r9YP`; usar o `fileId` do lote ou, se for `null`, procurar pelo nome do ficheiro (`title = '<pdf>'`). Teses longas: o `read_file_content` trunca sem aviso — confirmar com o PDF descarregado (pymupdf).

Regras: não inventar; não deduzir o tipo de cimento pelo país ou pela época. Segurança: nunca enviar email ou dados pessoais a serviços externos; não usar Unpaywall nem APIs externas; só o conector do Google Drive e ferramentas locais. Não alterar ficheiros do repositório.

Saída `resultado_loteNN.json` (na pasta indicada) = lista de {row_id, pares:[{sheet_row, cimento_designacao, norma_cimento, ligante, teor_clinquer_ou_adicoes, citacao, nota}], texto_completo_lido, notas}.
