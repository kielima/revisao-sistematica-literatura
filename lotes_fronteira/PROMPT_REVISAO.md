# Revisao dos estudos de fronteira/transporte (F37, 2026-10-18)

Pedido da Kie: rever os 19 estudos nao lidos e os 29 com resposta duvidosa do rastreio da fronteira. Regras do
`lotes_fronteira/PROMPT.md` (leia-o primeiro) com estas diferencas:

1. **PDF:** cada estudo tem `pdf_reduzido` quando o original e grande: ficheiro «TMP2 <row_id> reduzido.pdf» na pasta
   `1R63Q4Lzz6JRRLpwES1Ngyod04q0-r9YP` (procurar com `search_files`: `parentId = '1R63Q4Lzz6JRRLpwES1Ngyod04q0-r9YP' and title contains 'TMP2 <row_id>'`),
   comprimido a /screen (todas as paginas, texto e figuras legiveis). Se `pdf_reduzido` for nulo, usar o `fileId` original.
   `download_file_content` **um de cada vez**; se falhar, repetir uma vez. So em ultimo caso `read_file_content` (texto), e dizer-no.
2. **Ver as figuras de fronteira** (renderizar paginas a >=150 dpi com pymupdf e olhar) e as tabelas do inventario.
3. `resposta_anterior` e `nota_anterior` mostram o que se tinha dito e a duvida. Resolver a duvida: dizer **qual valor de CO2
   esta gravado nos pares** (`pares`, com `sheet_row`/material/fck) e se esse valor inclui o transporte das materias-primas e o A4
   (comparando o valor gravado com as tabelas/figuras do artigo). Se nao for possivel, `incerto` e porque.
4. **Novos campos de localizacao** (a Kie pediu para rastrear o local da informacao): `local_fronteira`, `local_transporte_materiais`,
   `local_transporte_a4`, `local_valor_gravado` — cada um no formato «p.N, Tab.X / Fig.Y / Sec.Z» (so o local; a frase fica em `citacao`).
5. Saida `lotes_fronteira/resultado_revNN.json`: lista, uma entrada por estudo, com os mesmos campos do PROMPT.md mais
   `valor_gravado_inclui` (`so_A1-A3` | `A1-A3+A4` | `ciclo_completo` | `incerto`), `a4_somavel` (`sim` | `nao` | `incerto`: pode-se somar o A4 do nosso grafico a este par sem contar duas vezes?),
   `local_*` acima e `mudou` (true/false: a resposta anterior muda?) com `mudanca` (o que muda).
Seguranca: nunca enviar email nem dados pessoais a servicos externos; sem APIs externas; so Drive e ferramentas locais. Nao alterar mais ficheiros do repositorio. Nao apagar nada no Drive.
