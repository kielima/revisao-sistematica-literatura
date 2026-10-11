# Releitura dos Elegíveis sem par convertível (2026-10-11)

Pedido da Kiê (2026-10-11): «Quero revisar esses 129 artigos. Reler com mais detalhamento mais uma vez para realmente ter certeza de que não dá para converter em CO2/m³ e/ou CO2/MPa.»

Cada artigo do lote é `Elegível`: passou a Etapa 2 porque reporta resistência à compressão e CO2. Mas nenhuma linha dele chega hoje ao painel, porque o CO2 gravado não está em kg CO2-eq/m³ ou não há fck para a mesma mistura. A coluna `co2_conversao` de cada linha diz porque é que a leitura anterior (2026-09-27 ou antes) concluiu «NAO CONVERTIDO». **O teu trabalho é pôr essa conclusão à prova**, com uma leitura mais detalhada.

## O que fazer, artigo a artigo

1. Abrir o PDF no Drive (pasta `1R63Q4Lzz6JRRLpwES1Ngyod04q0-r9YP`) pelo `fileId` do lote ou, se for `null`, procurar `title = '<pdf>'` com `parentId` dessa pasta.
   - Confirmar título e primeiro autor na p.1.
   - Usar `read_file_content`. Para teses ou documentos longos, o texto pode vir **truncado sem aviso**: confirmar sempre com `download_file_content` e pymupdf (texto de todas as páginas).
2. Ler o artigo **inteiro**: métodos, traço, inventário da ACV, resultados, discussão, anexos e material suplementar impresso no PDF.
   - Renderizar como imagem (pymupdf, `get_pixmap(dpi=150-200)`) e **ver** as páginas com tabelas e figuras de CO2, de traço e de resistência.
   - Valores que só existem numa figura contam, se a figura tiver escala legível. Nesse caso, ler por píxel e dizer que foi lido da figura.
3. Procurar **qualquer** caminho para um destes, **só com números impressos no próprio artigo**:
   - **(a) kg CO2-eq por m³** da mistura cuja resistência à compressão é conhecida. Exemplos de caminhos válidos:
     - CO2 por kg ou tonelada de betão/argamassa/pasta × massa volúmica **impressa** no artigo.
     - CO2 por kg de ligante (ou de cada constituinte) × quantidades por m³ do traço impresso, somando todos os constituintes.
     - Total de um elemento ou edifício ÷ volume de betão **impresso**.
     - CO2 por m² ÷ espessura impressa, quando a unidade funcional é **só** o betão (não um sistema com outros materiais).
     - Soma de contribuições por constituinte dada em tabela.
   - **(b) kg CO2-eq/(m³·MPa)**, ou outro índice de intensidade que o artigo publique explicitamente por mistura, com a resistência dessa mistura também publicada. Nesse caso indicar o índice, a resistência e o CO2/m³ que daí resulta (índice × fck).
4. **Regra estrita da Kiê: «não vamos assumir nada».** Não usar massas volúmicas típicas, factores de emissão de outras fontes, densidades de cimento ou agregado que o artigo não imprima, nem valores de outro artigo. A única excepção já decidida é a massa específica do cimento (3,15 t/m³), e só quando o artigo deixa claro esse mecanismo (regra 5b do `lotes_etapa2/PROMPT_E2.md`); na dúvida, não usar.
   - Se a conversão exigir um número que o artigo não imprime, o veredito é `NAO_CONVERTIVEL` e deves nomear **exactamente o número que falta**.
5. O CO2 tem de ser **do betão/argamassa da mistura** (berço-ao-portão, A1-A3 no mínimo):
   - Não serve só a brita, só o transporte, só a energia de máquinas, nem um total que exclua o cimento ou os activadores.
   - Se o total inclui aço de armadura inseparável, dizer `inclui_aco: true` (vai para a família betão armado).
   - Se o artigo der CO2 bruto e líquido (créditos, carbonatação, carga evitada), registar os dois.
6. A resistência tem de ser à **compressão** da **mesma mistura** do CO2 (medida, ou classe de projecto quando é isso que o artigo usa para a ACV), com idade e provete se impressos.

## Saída

Ficheiro `resultado_loteNN.json` na pasta indicada pelo pedido: uma lista com um objecto por artigo:

```json
{"row_id": 0, "pdf_confere": true, "texto_completo_lido": true, "figuras_vistas": ["Fig.3 p.7", "..."],
 "veredicto": "CONVERTIVEL | NAO_CONVERTIVEL | PARCIAL",
 "pares": [{"sheet_row": 0, "mistura": "", "fck_mpa": 0, "fck_fonte": "pagina/tabela/figura e frase",
            "idade_dias": null, "co2_kg_m3": 0, "co2_bruto_ou_liquido": "bruto|liquido|unico",
            "co2_com_desconto_kg_m3": null, "conta": "exactamente como chegaste ao numero, com cada factor e onde esta impresso",
            "inclui_aco": false, "confianca": "alta|media|baixa"}],
 "nao_convertivel_motivo": "se nao converte: o numero exacto que falta e onde o artigo devia te-lo",
 "concorda_com_leitura_anterior": true, "notas": ""}
```

`sheet_row` deve ser o da linha existente que corresponde à mistura. Para uma mistura nova, sem linha, usar `null`. Não inventar valores: cada número citado com a página e a tabela, figura ou frase.

## Segurança

- Nunca enviar email ou dados pessoais a serviços externos.
- Não usar Unpaywall nem APIs externas: só o conector do Google Drive e ferramentas locais.
- Ficheiros de trabalho no scratchpad, com o número do lote no nome. Não reutilizar ficheiros que já lá estejam.
- Não alterar ficheiros do repositório, excepto escrever o `resultado_loteNN.json` pedido.
