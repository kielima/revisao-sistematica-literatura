# Lotes do transporte A4, fase 2 (F42, 2026-11-08)

Aprovação (Kiê, 2026-11-08, #0619, «Pode começar»): fase 2 do plano da F40 em lotes de releitura dos PDFs, começando pelos estudos com pares `indeterminado` da fase 1 (F41). Nada de dedução: só o que o artigo escreve.

Para cada estudo de `lotes_transporte/loteNN.json` (com `fileId`, `pares`, `classes`):
1. Ler o PDF **completo** (`mcp__Google_Drive__read_file_content`; se truncar ou falhar, `download_file_content` + `pdftotext -layout`; se «session expired»/>10 MB marcar `nao_lido`). Confirmar título e primeiro autor. Ver as figuras/tabelas relevantes (fronteira do sistema, inventário, transporte).
2. Responder:
   - `o_que_se_transporta`: `betao_fresco_betoneira` | `elemento_prefabricado` | `pre_mistura_seca` | `nao_transportado_in_situ` | `indeterminado` (só se o artigo disser o que é entregue/como; ex.: «ready-mix», «precast», «bagged»).
   - `massa_volumica_kg_m3`: massa volúmica do betão (fresco/endurecido) **impressa**, ou a soma do traço impresso (kg/m³) — indicar qual em `massa_volumica_origem` (`impressa` | `soma_do_traco` | `nao_disponivel`). Por par se diferir (`por_par`: lista `{row_dados_fck? usar sheet_row, ...}`).
   - `distancia_betao_km`: distância central/fábrica → obra impressa (número ou faixa).
   - `modo_transporte`: texto do artigo (caminhão betoneira, truck, carreta, barco...) e `capacidade_t_ou_m3` se impressa.
   - `regresso_vazio`: `contado` | `nao_contado` | `nao_declarado`.
   - `a4_publicado`: valor de A4 publicado por m³ (kg CO₂-eq/m³) e onde, se existir.
   - `citacao`: página/tabela/figura + frase curta para cada resposta.
3. Não declarado = `nao_declarado`/`nao_disponivel`, nunca deduzir. Sem email nem APIs externas (Unpaywall, Crossref, OpenAlex…): só o conector do Drive e ferramentas locais. Ficheiros de trabalho com o número do lote no nome.

Escrever `lotes_transporte/resultado_loteNN.json` = lista de
`{"row_id":0,"o_que_se_transporta":"","massa_volumica_kg_m3":null,"massa_volumica_origem":"","distancia_betao_km":null,"modo_transporte":"","capacidade":"","regresso_vazio":"","a4_publicado":null,"por_par":[],"citacao":"","texto_completo_lido":true,"figuras_vistas":false,"nota":""}`.
Não alterar mais nenhum ficheiro do repositório.
