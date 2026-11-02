# F40 fase 2 — dados do transporte à obra (A4) por estudo

Contexto: vamos calcular o A4 (transporte do betão da central à obra) com 4 modos do SIDAC (betoneira 0,10; truck 3 eixos 0,07; carreta 4 eixos 0,07; carreta 5 eixos 0,06 kg CO2/t·km). Para isso precisamos, por estudo e por par, do que cada artigo imprime. NÃO assumas nada; nada de factores externos; nada de valores de normas ou de «típico». Se o artigo não diz, deixa vazio.

Para cada estudo de `loteNN.json` (campos já extraídos: `fronteira`, `transporte_betao_a4`, `transporte_dados`, e os `pares` com `sheet_row`):
1. Lê o PDF na ÍNTEGRA (texto completo, todas as secções; se o download falhar ou truncar, usa `shrink-drive-pdf.yml` com `first_page`/`last_page`, pasta 1R63Q4Lzz6JRRLpwES1Ngyod04q0-r9YP, e move os recortes para o lixo do Drive depois). Renderiza como imagem as figuras e tabelas em que apareçam distâncias, modos ou massas. Só `texto_completo_lido`/`figuras_vistas` true se for verdade.
2. Por ESTUDO regista: `o_que_e_transportado` (`betao_fresco` | `elemento_prefabricado` | `premistura_seca` | `materiais_separados` | `nao_declarado`), `modo_declarado` (texto do artigo: betoneira, camião basculante, camião de 16–32 t, carreta, barcaça…), `distancia_km_declarada` (valor(es) impressos, por viagem; indica se é ida ou ida-e-volta; se há vários cenários lista-os), `regresso_em_vazio` (`incluido`|`excluido`|`nao_declarado`), `a4_dentro_do_valor_gravado` (confirma ou contradiz o campo `a4_somavel=sim` já gravado, com citação), `citacao` (tabela/figura/página).
3. Por PAR (`sheet_row`) regista `densidade_betao_kg_m3` — SÓ se o artigo a imprime para essa mistura (massa volúmica do betão fresco/endurecido) OU se o traço impresso dá a soma dos componentes por m3 (então `densidade_origem` = `soma_do_traco` e mostra a soma); caso contrário null. Para elementos pré-fabricados regista a massa do elemento e o volume de betão do elemento, se impressos (`massa_elemento_kg`, `volume_betao_elemento_m3`). Inclui `local` e `citacao`.
4. Dúvidas ou contradições vão em `nota`. Não uses aqui o valor de A4 do artigo (já temos `co2_a4`); só os parâmetros.

Saída: `lotes_a4/resultado_loteNN.json`:
`[{"row_id":0,"o_que_e_transportado":"","modo_declarado":"","distancia_km_declarada":"","regresso_em_vazio":"","a4_dentro_do_valor_gravado":"","citacao":"","texto_completo_lido":true,"figuras_vistas":true,"nota_estudo":"","pares":[{"sheet_row":0,"densidade_betao_kg_m3":null,"densidade_origem":"","massa_elemento_kg":null,"volume_betao_elemento_m3":null,"local":"","citacao":"","nota":""}]}]`

Segurança: não envies dados pessoais da Kiê (email incluído) a serviços externos; não alteres outros ficheiros. Resposta final em máx. 6 linhas.
