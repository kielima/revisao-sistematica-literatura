# Elementos e estruturas com dimensões impressas — releitura (F18, 2026-10-15)

Pedido da Kiê (2026-10-15): «se é por viga ou por laje, se tiver as dimensões do elemento dá pra fazer a conta e colocar como concreto armado ou alguma família. Já o edifício todo, se ele não separa, não dá pra converter. Eu não quero tirar pilares, vigas, lajes e elementos que dá pra converter. Quero tirar só o que não dá pra converter.»

Estes artigos ficaram sem par porque o CO₂ é de um **elemento ou estrutura** (pilar, viga, laje, parede, painel, tabuleiro, estrutura de edifício) e não do betão sozinho. Pela regra nova, **incluir aço, cofragem ou isolamento já não impede a conversão**: o par vai para a família `concreto_armado` (ou para a família do material, se não houver aço). A pergunta é só: **o artigo imprime o CO₂ desse elemento e o volume de betão (ou as dimensões que o dão) do mesmo elemento?**

## O que fazer, artigo a artigo

1. Abrir o PDF no Drive pelo `fileId` (se for `null`, procurar `title = '<pdf>'` na pasta `1R63Q4Lzz6JRRLpwES1Ngyod04q0-r9YP`). Confirmar título e primeiro autor. Ler o documento inteiro, incluindo tabelas e figuras (renderizar as páginas relevantes como imagem quando os números estão em figuras). Teses longas: o `read_file_content` pode truncar sem aviso — usar `download_file_content` + PyMuPDF para ler todas as páginas.
2. Para cada elemento ou estrutura com CO₂ próprio, registar:
   - o **CO₂ total do elemento** tal como impresso (valor, unidade, tabela/figura/página, fronteira: A1–A3, berço ao túmulo…, e se inclui aço, cofragem, isolamento, transporte, uso, fim de vida, carbonatação);
   - o **volume de betão** desse mesmo elemento: impresso, ou calculado **só** a partir de dimensões impressas (mostrar a conta). **Nunca** usar massa volúmica que não esteja impressa no próprio artigo;
   - a **resistência** do betão desse elemento (classe ou fck impresso, idade se houver);
   - a conta: CO₂ total ÷ volume = kg CO₂/m³.
3. Verificações de coerência com números impressos (ex.: massa impressa ÷ volume dá massa volúmica plausível; soma de parcelas bate com o total). Se os valores forem internamente incoerentes, dizer onde e porquê.
4. Se o CO₂ for de ciclo de vida completo e o artigo der também a parcela A1–A3 (ou de produção) do mesmo elemento, registar as duas.
5. Não inventar. Se faltar o volume (e as dimensões que o dão) ou o CO₂ do mesmo elemento, dizer exactamente o que falta.

## Saída

`lotes_elementos/resultado_loteNN.json`, lista com um objecto por artigo:

```json
{"row_id": 0, "pdf_confere": true, "texto_completo_lido": true, "figuras_vistas": ["..."],
 "veredicto": "CONVERTIVEL | NAO_CONVERTIVEL | INCOERENTE",
 "pares": [{"sheet_row": null, "elemento": "", "fck_mpa": 0, "fck_fonte": "", "idade_dias": null,
            "co2_total": 0, "co2_total_unidade": "", "co2_fonte": "", "fronteira": "", "inclui": "",
            "volume_m3": 0, "volume_fonte_e_conta": "", "co2_kg_m3": 0, "conta": "",
            "familia_sugerida": "concreto_armado | opc | ...", "confianca": "alta | media | baixa"}],
 "motivo_se_nao": "", "notas": ""}
```

## Segurança

- Nunca enviar email ou dados pessoais a serviços externos. Não usar Unpaywall, OpenAlex, Crossref nem outras APIs: só o conector do Google Drive e ferramentas locais.
- Ficheiros de trabalho no scratchpad, com o número do lote no nome; não reutilizar ficheiros que já lá estejam.
- Não alterar ficheiros do repositório, excepto escrever o `resultado_loteNN.json` pedido.
