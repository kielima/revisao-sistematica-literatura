# Prompt de retomada — auditoria de colisões de PDF + correções pendentes

> Criado em 2026-08-13, ao fim da sessão que descobriu o problema. Copia o bloco "PROMPT" abaixo para uma sessão nova.

---

## PROMPT (copiar daqui para baixo)

Retomar o trabalho de correção e auditoria da RSL no vault `REVISÃO SISTEMÁTICA DE LITERATURA`.

**Antes de qualquer coisa, ler nesta ordem:**
1. `CLAUDE.md` — em especial a secção "Preferências de interação da Kiê" e os bullets de estado no topo.
2. `CRITERIOS_E_NUANCES_RSL.md` — critérios C1–C8, regras acumuladas e o protocolo de extração (secção 7).
3. Este ficheiro, `PROMPT_RETOMADA_AUDITORIA_COLISOES_PDF.md`.

**⭐ Regra de interação, sem exceção:** perguntas sempre no texto do chat, em texto corrido. **Nunca** usar a ferramenta de perguntas com opções múltiplas.

### Tarefa 1 (prioritária) — anular as decisões tomadas sobre PDF errado

O ficheiro `AUDITORIA_COLISOES_2026-08-13.csv` lista 131 linhas, com as colunas `veredito, pdf, linha, doi_banco, doi_no_pdf, tem_P, status, titulo`. O veredito foi apurado comparando o DOI registado no banco com o DOI realmente presente no conteúdo do PDF.

- **67 linhas com `veredito = PDF_ERRADO`**, das quais **49 com `tem_P = sim`** — decisões de triagem tomadas sobre outro artigo.
- **62 linhas com `veredito = OK`** — validadas, não mexer.
- **2 linhas com `veredito = INDETERMINADO`** (`WU et al., 2014.pdf`): o ficheiro não contém nenhum dos dois DOIs, ou seja é um terceiro artigo. Precisa de inspeção manual.

**A Kiê ainda não autorizou a anulação.** Perguntar primeiro, em texto no chat. Se autorizar, para cada linha `PDF_ERRADO`:
1. Remover os `P:` de todos os critérios (C1 col 21, C2 col 22, C3 col 24, C4 col 25, C5 col 26, C6 col 27, C8 col 29), **preservando o histórico `R:`**.
2. Repor `status_triagem` em `Inconclusivo` (as que estavam `Rejeitado` ou `Elegível` por causa da decisão contaminada).
3. Carimbar em `comments` (col 32): `[COLISÃO DE PDF 2026-08-13: decisão anulada. O ficheiro <pdf> contém o DOI <doi_no_pdf>, não o <doi_banco> desta linha. Aguarda o PDF correto.]`
4. Limpar/assinalar as linhas correspondentes em `meta_analysis_base.xlsx` que tenham sido extraídas dessas linhas — cruzar por `row_id`.

### Tarefa 2 — rebaixar os PDFs corretos

Cada linha `PDF_ERRADO` tem o DOI certo na coluna `doi_banco`. Gerar uma lista de download (HTML clicável, como o antigo `DOWNLOAD_MANUAL.html`) com esses DOIs, para a Kiê baixar via proxy CAPES. Ver as regras de proxy e de integração na secção "Processo de download de PDFs" do `CLAUDE.md`.

**⚠️ Ao renomear os novos ficheiros, NÃO repetir a convenção que causou o problema.** Sugerir à Kiê uma convenção única, por exemplo `SOBRENOME, ANO — sufixo-do-DOI.pdf`, e confirmar antes de aplicar.

### Tarefa 3 — decidir as 7 linhas revistas em 2026-08-13

Foram lidas por completo e têm recomendação registada. A Kiê ainda não confirmou:

| Linha | Artigo | Recomendação | Base |
|---|---|---|---|
| 3729 | Chaudhary & Akhtar 2023 | **Aceitar** | Traço explícito 1:2:4 e 0,32 t de cimento/m³; RCC = 20–30% dos impactos |
| 3291 | Shindo et al. 2023 | **Aceitar** | 261 m³ de concreto com EPD, armadura 450/350/135 kg/m³, 2,7 kgCO₂-eq/m²/ano do pórtico |
| 2553 | Abouhamad et al. 2020 | **Aceitar** | Quantidades por elemento; fundações = 52 kg CO₂-eq/m², 29% do GWP incorporado |
| 3267 | Raouf & Al-Ghamdi 2020 | **Manter rejeitado** | Objeto são 7 materiais de isolamento; bloco CMU é substrato constante |
| 3340 | Wang et al. 2018 | **Manter rejeitado** | Pavimento é obra, mas o material avaliado é asfalto — exemplo literal de rejeição no C2 |
| 3341 | Lu et al. 2019 | **Manter rejeitado** | Os três materiais avaliados são asfalto, asfalto poroso e poliuretano; nenhum é concreto |
| 4295 | Alotaibi 2022 | **Não decidir** | Colisão de PDF confirmada — precisa do ficheiro certo (`10.3390/buildings12081203`) |

### Tarefa 4 — retomar a confirmação C2 por PDF

Só depois das anteriores. **1.325 linhas pendentes, próxima é a 2688.** Filtro do universo:

```python
COL={"C1":21,"C2":22,"C3":24,"C4":25,"C5":26,"C6":27,"C8":29}   # material_C2 = 23, NÃO usar range()
pend=[r for r in range(2,ws.max_row+1)
      if ws.cell(r,20).value in ('Elegível','Inconclusivo')
      and 'P:Aceito' in str(ws.cell(r,21).value or '')
      and 'P:' not in str(ws.cell(r,22).value or '')]
```

Lotes de 5 linhas; ao fim de cada lote gravar, fazer backup em `02_ARQUIVOS ANTERORES/` e reportar.

---

## Regras novas desta sessão — já escritas no `CRITERIOS_E_NUANCES_RSL.md`

Estão lá em detalhe; este resumo serve só para não se perderem de vista.

1. **⛔ Verificar o PDF por DOI antes de ler seja o que for.** Título e primeiro autor não bastam — apanham colisões grosseiras, não as subtis. Extrair o DOI do texto do PDF e comparar com a coluna `doi`. Divergiu → parar e reportar, não decidir nem extrair. Documentos sem DOI (dissertações) vão por título, autor e instituição, com a via registada.
2. **Valor derivado tem de ser marcado e documentado**, com três marcações redundantes: cor âmbar na célula, comentário com a memória de cálculo, e prefixo `[DERIVADO]` em `co2_unidade` — este último é o único que sobrevive a exportação para CSV, pandas ou R. Ver a aba `LEGENDA` do `meta_analysis_base.xlsx`. Não confundir com "calculado pelos autores", que é dado publicado e não leva marca.
3. **⛔ Não derivar valor a partir de comparação percentual verbal** sem esgotar a busca pelo valor publicado, incluindo as tabelas de valores das figuras, que na extração podem aparecer fora da secção de resultados. Caso que originou a regra: linha 1562, onde a derivação deu ~4.100–4.600 e o valor publicado era 5.840.
4. **Concreto armado: a armadura integra o material.** Quando o estudo reporta o aço em linha separada, somar as parcelas — depois de verificar que não há dupla contagem (massa volúmica = concreto base + taxa de armadura; fatores de emissão implícitos na faixa esperada; grupo de metais só com armadura).
5. **C2 aceita ACV de obra de infraestrutura urbana**, que é mais amplo do que "edifício" — abrange obras de energia, transporte e redes. A pergunta de escopo é: o estudo avalia uma **obra** ou um **produto**? Obra com concreto → aceita; produto onde o concreto é só referência de comparação → rejeita.

## Estado do banco em 2026-08-13

- `status_triagem`: Duplicado 2.621 · Inconclusivo 1.093 · Rejeitado 922 · Elegível 397 · Sem acesso 60
- Cascata completa (C1–C6 e C8 = Aceito): **1.401** artigos
- `meta_analysis_base.xlsx`, aba `dados_fck`: **1.694** linhas de dados; aba `LEGENDA` com o código de cor
- Linhas marcadas como derivadas: 11 (parcial), 1678, 1679, 1680
- Branch de trabalho: `claude/retomada-confirmacao-pdf-6tsyhg`, PR #3 aberto

## Ficheiros que interessam

| Ficheiro | Para quê |
|---|---|
| `AUDITORIA_COLISOES_2026-08-13.csv` | Veredito por linha das 131 afetadas — a lista de trabalho da Tarefa 1 |
| `COLISOES_PDF_2026-08-13.csv` | Inventário bruto anterior, sem veredito; mantido por rastreabilidade |
| `CRITERIOS_E_NUANCES_RSL.md` | Critérios e todas as regras acumuladas |
| `articles_final.xlsx` | Banco de triagem — índices de coluna no `CLAUDE.md` |
| `meta_analysis_base.xlsx` | Base da metanálise, abas `dados_fck` e `LEGENDA` |
