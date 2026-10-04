# Revarredura das famílias e do betão armado (2026-10-04)

Pedido da Kiê (2026-10-04): «corrija todas as inconsistências» das famílias e «faça a revarredura completa do concreto armado». Cada lote cobre ~10 estudos Elegíveis com pares no painel. Para **cada par** (`sheet_row`), ler o PDF e responder a quatro perguntas sobre **o par concreto** (a mistura/sistema daquela linha, com o CO2 gravado em `co2_kg_m3`).

1. **`co2_inclui_aco`** — o CO2 gravado inclui o aço de armadura, pré-esforço, cabos ou outro reforço metálico/estrutural (vergalhão, malha, BFRP/GFRP/carbono como armadura)?
   - `sim` = o valor do artigo (ou o total que dividimos) inclui esse reforço e não dá para separar com dados do próprio artigo;
   - `separavel` = o artigo dá o CO2 do betão sozinho (e o gravado é esse, ou podia ser) — dizer qual é o valor só do betão e onde;
   - `nao` = não há reforço no sistema avaliado, ou a fronteira da ACV é só o betão/argamassa (o caso de quase todas as misturas de laboratório por m3).
   Fibras dispersas (aço, PE, PVA, vidro, sisal) **não** são armadura: responder `nao` e descrever em `papel_material`.
2. **`tipo_ligante`** do par: `portland` (inclui cimentos compostos, SCM em substituição parcial, LC3, UHPC Portland) | `alcali_ativado` (geopolímero, AAM, AAS, inclui híbridos com OPC minoritário) | `csa` | `magnesiano` | `gesso` | `polimero` | `madeira` (estrutura de madeira/bio) | `outro` (dizer qual).
3. **`papel_material`** — o que distingue ESTE par da mistura de referência do artigo:
   `controlo` (é a própria referência, sem o material novo) | `substituicao_ligante` (resíduo/subproduto/adição a substituir cimento ou como ligante suplementar: cinzas, escórias, pó de vidro, pó cerâmico, filer, metacaulino…) | `agregado` (substitui areia/brita) | `fibra` (fibras dispersas) | `aditivo` (químico/bio-aditivo em pequena dose) | `ligante_alternativo` (o ligante principal não é Portland) | `sistema` (elemento/edifício sem mistura distintiva) | `outro`.
4. **`material_residuo`** — o material que distingue o par é resíduo/reciclado/subproduto? `sim` | `nao` | `na` (controlo/sistema). E **`uhpc`**: o próprio artigo chama a este betão UHPC/UHPFRC/ultra-alto desempenho? `sim` | `nao`.

Regras de leitura: ler o PDF completo (texto, tabelas e — se a fronteira/inventário só estiver numa figura ou tabela — descarregar e renderizar com pymupdf). Teses longas: o `read_file_content` trunca sem aviso; confirmar com o PDF descarregado. A fronteira do sistema e o inventário (lista de materiais com CO2) são o sítio onde se vê se o aço entra. Não inventar: se o artigo não deixa decidir, dizer `indeterminado` e explicar.

Segurança: nunca enviar email ou dados pessoais a serviços externos; não usar Unpaywall nem APIs externas; só o conector do Google Drive e ferramentas locais. Não alterar ficheiros do repositório.

Saída `resultado_loteNN.json` = lista de {row_id, pares:[{sheet_row, co2_inclui_aco, aco_citacao, co2_so_betao (número ou null), tipo_ligante, papel_material, material_residuo, uhpc, citacao, nota}], texto_completo_lido, notas}.
