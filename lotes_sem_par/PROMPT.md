# Tarefa: leitura integral de artigos Elegíveis sem par fck×CO2 em kg/m3

Metanálise de betão de baixo carbono (dissertação). Estes artigos passaram as 4 etapas de triagem (status Elegível), mas NENHUMA das suas linhas no banco `dados_fck` tem um par utilizável (fck em MPa + CO2 em kg CO2-eq por m3 de material). Preciso de saber PORQUÊ, artigo a artigo, lendo o PDF por inteiro. TAREFA SÓ DE LEITURA E RELATÓRIO: não alteres nenhum ficheiro do repositório, não faças commits.

## Para cada artigo do teu lote
1. **Abrir o PDF** pelo `fileId` (ToolSearch → `mcp__Google_Drive__read_file_content` e `mcp__Google_Drive__download_file_content`). Se o `fileId` vier vazio, procura com `mcp__Google_Drive__search_files` query `parentId = '1R63Q4Lzz6JRRLpwES1Ngyod04q0-r9YP' and title = '<nome exacto do pdf>'`. Resultados grandes são gravados num ficheiro: lê-os com Python aos pedaços, nunca despejes tudo no contexto.
   - ⚠️ `read_file_content` TRUNCA documentos longos (teses, >~135.000 caracteres) SEM AVISO. Em teses/dissertações ou sempre que o texto pareça acabar antes das conclusões/referências, descarrega o PDF (`download_file_content`, base64 → ficheiro) e extrai TODAS as páginas com PyMuPDF (`pip install pymupdf` se faltar).
   - Tabelas e figuras: renderiza as páginas relevantes (resultados, ACV/LCA, traços, resistências) a 150–200 dpi com PyMuPDF e vê-as com a ferramenta Read. Não concluas "não há valor" sem ver as figuras.
   - Se o download falhar com "session expired", regista-o e segue com o texto (diz que não viste figuras).
2. **Conferir a identidade do PDF**: título, primeiro autor e DOI impressos batem com o dossiê? Se for outro artigo → veredicto `PDF_ERRADO` e passa ao seguinte.
3. **Procurar o par**: resistência à compressão (fck/fcm, MPa; indicar se cubo ou cilindro; NÃO serve módulo de resiliência, flexão, tracção) e CO2/GWP do mesmo material/mistura/sistema. Anotar TODOS os valores que existam, com página/tabela/figura e texto literal.
4. **Converter para kg CO2-eq/m3** só com números impressos no próprio artigo:
   - já em kg CO2-eq/m3 → nativo;
   - total absoluto (elemento, edifício, UF) + volume de betão impresso → total ÷ volume (se o total inclui armadura, dizer "familia concreto_armado");
   - por kg/tonelada de betão + massa volúmica impressa no artigo → multiplicar; por m2 + espessura impressa → dividir pela espessura;
   - soma traço (kg/m3, impresso) × factores de emissão impressos → permitido (diz a conta);
   - percentagens/índices só se houver âncora absoluta impressa (ex.: "100% = 151,3 t");
   - leitura de gráfico só se o eixo tiver escala numérica (confiança média/baixa);
   - créditos de carga evitada (reciclagem, aterro evitado): reportar líquido publicado E bruto reconstruído se possível;
   - NUNCA assumir massas volúmicas, espessuras ou factores que o artigo não imprime. Nesse caso → não convertível, dizendo exactamente o que falta.
5. Vida útil (anos), se impressa, com local.

## Veredicto por artigo (um de)
- `PAR_CONVERTIVEL` — há pelo menos um par fck + CO2 em kg/m3 obtido pelas regras acima (dá as linhas);
- `PAR_NAO_CONVERTIVEL` — há fck e CO2 do mesmo material, mas o CO2 não pode ser levado a kg/m3 sem dados não impressos (diz qual falta);
- `SEM_FCK` — não há resistência à compressão própria do material estudado;
- `SEM_CO2` — não há CO2/GWP próprio pareável (só citação de terceiros, percentagem sem âncora, etc.);
- `PDF_ERRADO` / `ILEGIVEL`.

## Saída
Escreve `resultado_lote_XX.json` (XX = número do lote) na pasta do dossiê: lista de objectos
`{row_id, pdf_confere (sim/nao + nota), texto_completo (sim/nao, n_paginas), figuras_vistas (sim/nao/quais), veredicto, motivo, linhas:[{sheet_row_existente_ou_null, material, fck_mpa, fck_tipo(cubo/cilindro/nao_dito), fck_local, co2_original, co2_original_local, co2_conversao, co2_kg_m3, vol_m3, vol_fonte, vida_util_anos, vida_util_local, familia_sugerida, confianca}], citacoes_literais:[...]}`.
Usa as linhas existentes do dossiê (`sheet_row`) quando a tua linha corresponder a uma delas. Na resposta final: um resumo curto (uma linha por artigo com o veredicto).

## Proibições adicionais
- NUNCA envies o email da utilizadora (nem nenhum dado pessoal) a serviços externos (Unpaywall, Crossref, etc.). Se precisares de um parâmetro `email` numa API pública, usa `rsl-bot@example.com`. Prefere não consultar serviços externos: o PDF está no Drive.
- Se o PDF passar de 10 MB ou o download falhar, NÃO tentes sites de editoras; regista o bloqueio e as páginas que precisarias de ver (para eu isolar com o workflow shrink-drive-pdf).
