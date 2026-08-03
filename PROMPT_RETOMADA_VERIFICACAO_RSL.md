---
titulo: PROMPT RETOMADA VERIFICACAO RSL
descricao: Prompt para Retomada — Auditoria do BANCO DE DADOS DA RSL
tags: [academico-e-pesquisa, revisao-sistematica, UHPC]
status: em-andamento
ultima_atualizacao: 2026-05-14
---

# Prompt para Retomada — Auditoria do BANCO DE DADOS DA RSL

Cole este prompt no início de uma nova conversa para retomar a verificação exatamente de onde parou.

---

## CONTEXTO

Estou auditando a planilha `BANCO DE DADOS DA RSL.xlsx` (aba `ARTIGOS ACEITOS`) contra os 173 PDFs em `ARTIGOS ACEITOS DA RSL/`, todos dentro de:

`C:\Users\ttibu\Documents\03_PROFISSIONAL\02_PESQUISA\DISSERTAÇÃO\07_ANÁLISES DE DADOS\REVISÃO SISTEMÁTICA DE LITERATURA\`

**Objetivo:** verificar se cada uma das 9 colunas de informação extraída (Material analisado, Durabilidade, fck, Metodologia, Fronteira, ISO 14040, Unidade funcional, CO₂eq, Limitações) de cada artigo corresponde ao que está no PDF na página citada. Total: **173 artigos × 9 colunas = 1.539 células a verificar**.

**Relatório acumulado (em andamento):**
`C:\Users\ttibu\Documents\03_PROFISSIONAL\02_PESQUISA\DISSERTAÇÃO\07_ANÁLISES DE DADOS\REVISÃO SISTEMÁTICA DE LITERATURA\RELATORIO_VERIFICACAO_BD_RSL.md`

---

## ESTADO ATUAL

**66 / 173 artigos verificados** (38,2%) · **9 com inconsistências** · **18 problemas** registados (9 MAIOR + 9 MENOR).

### Artigos verificados (em ordem da planilha)

1. ADAMS et al., 2024 — **8 OK · 1 MAIOR** (Fronteira: A2 transporte incluído erroneamente)
2. AKBULUT et al., 2024 — 9 OK
3. AL-OBAIDY et al., 2022 — **7 OK · 2 MENOR** (CO₂eq: 718.437 → 718.436; Limitação AGC vidro p. 20 não 21)
4. ASSUNCAO, 2020 — 9 OK
5. BILAR, 2016 — **5 OK · 1 MAIOR · 3 MENOR** (fck cita p. 115,126 — correto: p. 67,125)
6. BRESSI et al., 2022 — 9 OK
7. DERVISHAJ et al., 2024 — 9 OK
8. DU et al., 2024 — 9 OK
9. DYNAN et al., 2023 — 9 OK
10. EK et al., 2020 — 9 OK
11. FERREIRA et al., 2023 — 9 OK
12. GANAPATHI CHOTTEMADA et al., 2023 — 9 OK
13. GOMES, 2023 — **6 OK · 1 MAIOR · 2 MENOR** (fck cita p. 32 — correto: p. 28-29)
14. HAJIESMAEILI et al., 2019 — 9 OK
15. HAVERKAMP et al., 2025 — 9 OK
16. KASTIUKAS et al., 2019 — 9 OK
17. KOUVARA et al., 2023 — 9 OK
18. KUL et al., 2023 — 9 OK
19. LI et al., 2024 — 9 OK
20. LI et al., 2025 — 9 OK
21. MALABI EBERHARDT et al., 2024 — **8 OK · 1 MENOR** (ISO 14040 está citada na p. 3, célula diz "não citada")
22. MENEGATTI et al., 2022 — 9 OK
23. MILANI et al., 2020 — 9 OK
24. MOHAJERANI et al., 2019 — 9 OK
25. NASSAR et al., 2025 — 9 OK
26. PAPADAKI et al., 2022 — 9 OK
27. PEDROSO et al., 2024 — 9 OK
28. PESTA et al., 2020 — 9 OK
29. RINNE et al., 2022 — 9 OK
30. ROSA et al., 2017 — 9 OK
31. ROSSI, 2013 — **8 OK · 1 MENOR** (CO₂eq 8,88E-01 está na Fig. 29/PDF p. 104, não na p. 14 do resumo)
32. SANGIORGIO et al., 2025 — 9 OK
33. SANTOS, 2015 — 9 OK
34. SANTOS, 2022 — **4 OK · 4 MAIOR** (caso atípico: célula descreve só durabilidade mecânica e ignora a ACV completa que o trabalho tem com ReCiPe + EN 15804 + ISO 14040)
35. SHANBHAG et al., 2024 — 9 OK
36. SIKORA et al., 2023 — **8 OK · 1 MAIOR** (ISO 14040/14044 ESTÃO citadas na p. 8, célula diz "não")
37. SILVA et al., 2023 — 9 OK
38. SOLTANZADEH et al., 2022 — 9 OK
39. SOMBRIO, 2015 — 9 OK
40. VALENCIA-BARBA et al., 2020 — 9 OK
41. VILLALBA et al., 2025 — 9 OK
42. ZUCARATO, 2020 — 9 OK
43. HAFNER et al., 2020 — 9 OK
44. HEMMATI et al., 2024 — 9 OK
45. HERTWICH et al., 2019 — 9 OK
46. INGRAO et al., 2018 — 9 OK
47. INMAN et al., 2017 — 9 OK
48. JANG et al., 2022 — 9 OK
49. JAYASINGHE et al., 2021 — 9 OK
50. JI et al., 2025 — 9 OK
51. KHORGADE et al., 2023 — 9 OK
52. HABIBI et al., 2024 — 9 OK
53. LASVAUX et al., 2015 — 9 OK
54. RAZA et al., 2023 — 9 OK
55. STARCZYK-KOLBYK, 2024 — 9 OK
56. VOLK et al., 2024 — **8 OK · 1 MAIOR** (ISO 14040 ESTÁ citada na p. 2, célula diz "não")
57. ABOUHAMAD et al., 2020 — 9 OK
58. ABUSHANAB et al., 2025 — 9 OK
59. AL-GHEETHI et al., 2022 — 9 OK
60. ALBRECHT et al., 2025 — 9 OK
61. ANDERSEN et al., 2022 — 9 OK
62. ANKUR et al., 2024 — 9 OK
63. ARRIGONI et al., 2018 — 9 OK
64. BACKES et al., 2022 — 9 OK
65. BALASBANEH et al., 2018 — 9 OK
66. BARBHUIYA et al., 2024 — 9 OK

### Próximo artigo a verificar: linha 68 — **BHAGAT et al., 2021**

(Os dados de BHAGAT, 2021 e o PDF já foram inspecionados na conversa anterior — mas a entrada no relatório ainda não foi escrita. Comece por escrever o resultado dele e seguir a partir daí.)

---

## PROTOCOLO DE VERIFICAÇÃO

### Decisões fechadas com a Kiê

- **Escopo:** todos os 173 artigos, ordem alfabética da planilha
- **Profundidade:** validação rigorosa de conteúdo (a página citada deve efetivamente conter a informação extraída)
- **Formato:** Markdown único, atualizado incrementalmente em `RELATORIO_VERIFICACAO_BD_RSL.md`
- **Ritmo:** 1 artigo por vez, atualizando o relatório acumulado a cada iteração
- **Formato compacto:** o que está OK marcar apenas como "9 OK" + linha curta com confirmações pontuais. Detalhar SÓ as inconsistências (MAIOR/MENOR/CRÍTICO/FALTANTE).
- **Cooperação:** quando aparecer caso atípico, perguntar à Kiê antes de avançar.

### Severidade

- **OK** — informação confere
- **MENOR** — citação correta mas redação ambígua/incompleta, ou número levemente arredondado
- **MAIOR** — página citada não suporta o conteúdo; informação está noutra página
- **CRÍTICO** — informação não consta no PDF ou contradiz o PDF
- **FALTANTE** — célula sem `(p. X)`

### Protocolo técnico escalonado

1. **Extração de texto** com `pypdf` das páginas citadas (sempre primeiro)
2. **Renderização visual** com `pymupdf` → PNG 200 dpi → leitura multimodal (para figuras, gráficos, tabelas embutidas como imagem)
3. **Extração de tabelas** com `camelot`/`tabula` (tabelas estruturadas em texto)
4. **Material suplementar externo** (DOI/site da revista) — apenas se citado explicitamente

### Numeração de páginas — regra crítica

As citações `(p. X)` nas células referem-se à **página impressa visível ao leitor**, NÃO ao índice do PDF. Em teses/dissertações brasileiras com pré-textuais, há offset. **Antes de classificar inconsistência:**
1. Detectar offset (verificar header da página)
2. Mapear `printed page = cell page → PDF index = printed + offset`
3. Localizar via Python
4. Só classificar como MAIOR/MENOR se a informação não estiver na página impressa correspondente

Casos confirmados de offset:
- ASSUNCAO, 2020: offset +2 (corpo)
- ROSSI, 2013: offset +19 (corpo, com pré-textuais longos)
- GOMES, 2023: offset +1 (corpo)
- SOMBRIO, 2015: sem offset (1:1)
- SANTOS, 2015: offset +1 (corpo)
- ZUCARATO, 2020: sem offset (1:1)

### Formato de cada entrada no relatório

```markdown
### N. AUTOR et al., ANO — 9 OK

Sem inconsistências. (Resumo curto de 1-2 frases com confirmações-chave.)
```

OU, se há problemas:

```markdown
### N. AUTOR et al., ANO — X OK · Y MAIOR · Z MENOR

- **MAIOR/MENOR — Coluna** (cita p. X): descrição do problema em 1-2 linhas. **Sugestão:** correção sugerida.

Demais células OK: ...
```

---

## PADRÃO DE ERROS RECORRENTE

Vários erros são do tipo "ISO 14040 não citada" quando ISO 14040 **está** citada no PDF (encontrado em VOLK 2024, SIKORA 2023, MALABI EBERHARDT 2024). Verificar sempre com `grep` no PDF inteiro.

---

## COMO INSPECIONAR CADA ARTIGO

Script Python padrão (executar via Bash no sandbox):

```python
import openpyxl
from pypdf import PdfReader

wb = openpyxl.load_workbook("BANCO DE DADOS DA RSL.xlsx", data_only=True)
ws = wb["ARTIGOS ACEITOS"]
header = [ws.cell(1, c).value for c in range(1, 13)]
row_data = [ws.cell(N, c).value for c in range(1, 13)]  # N = linha do artigo
for h, v in zip(header, row_data):
    print(f"--- {h} ---\n{v}\n")

pdf = PdfReader("ARTIGOS ACEITOS DA RSL/AUTOR et al., ANO.pdf")
print(f"PDF: {len(pdf.pages)} páginas")
```

Depois, busca de palavras-chave (valores numéricos, normas, softwares):

```python
all_texts = [pdf.pages[i].extract_text() for i in range(len(pdf.pages))]
for kw in ['14040', 'ISO 14040', 'SimaPro', 'Ecoinvent', ...]:
    found = [i+1 for i, t in enumerate(all_texts) if kw in t][:5]
    if found: print(f"  '{kw}': {found}")
```

---

## INSTRUÇÃO INICIAL PARA A NOVA CONVERSA

Cole exatamente isto no início:

> Estou retomando a auditoria do BANCO DE DADOS DA RSL. O estado atual está em `RELATORIO_VERIFICACAO_BD_RSL.md` (66/173 verificados). Por favor:
>
> 1. Leia o arquivo `PROMPT_RETOMADA_VERIFICACAO_RSL.md` na pasta `07_ANÁLISES DE DADOS/REVISÃO SISTEMÁTICA DE LITERATURA/` para obter contexto completo.
> 2. Leia também `RELATORIO_VERIFICACAO_BD_RSL.md` na mesma pasta para ver o formato do relatório e o que já foi feito.
> 3. Confirme que entendeu o protocolo (em particular: formato compacto, severidade, mapeamento de páginas impressas vs PDF index).
> 4. Retome a partir do artigo 67 da planilha — **BHAGAT et al., 2021** (linha 68 da aba `ARTIGOS ACEITOS`).
> 5. Continue sequencialmente sem confirmação para cada artigo. Apenas pergunte se aparecer caso atípico (como SANTOS, 2022 — onde a célula descreve só parte do trabalho).

---

---

## BLOCO DE RETOMADA — Integração de PDFs Manuais

> Usar este bloco quando a tarefa for continuar o download/integração de PDFs, não a auditoria de verificação.

### Contexto

Os PDFs da RSL são obtidos em 4 camadas (documentado em `CLAUDE.md`, secção "Processo de download de PDFs"):
1. Unpaywall automático (`download_pdfs_win.py`)
2. MDPI via Chrome CDP (`mdpi_batch_dl.py` / `mdpi_resume.py`)
3. IOP + Handle (`iop_hdl_dl.py`)
4. Manual via CAPES + listas HTML (`ELSEVIER_DOWNLOAD.html`, `DOWNLOAD_MANUAL.html`)

Pasta de destino: `00_REFERENCIAS\ARTIGOS ACEITOS APÓS REMOÇÃO DAS DUPLICATAS\`
Banco de triagem: `articles_final.xlsx`, coluna `pdf`

### Estado em 02/06/2026

- **Total de ficheiros na pasta de destino:** 1.247
- **`ELSEVIER_DOWNLOAD.html`:** 178 pendentes (9 Eleg. + 169 Inc.)
- **`DOWNLOAD_MANUAL.html`:** 378 pendentes (54 Eleg. + 324 Inc.)
- 19 PDFs integrados + 12 células `pdf` atualizadas (URL → caminho) na sessão de 02/06/2026

### Instrução inicial para nova sessão de integração

Cole exatamente isto no início:

> Estou retomando a integração de PDFs baixados manualmente na RSL. O estado atual está em `RSL_PROGRESSO.md` (secção "Estado dos Downloads de PDFs"). Por favor:
>
> 1. Lê `CLAUDE.md` na pasta RSL para obter o protocolo completo de download (secção "Processo de download de PDFs — arquitetura em 4 camadas").
> 2. Lê `RSL_PROGRESSO.md` para ver o estado atual (contagens, pendentes por publisher).
> 3. Confirma o conteúdo atual da pasta `NOVOS BAIXADOS MANUALMENTE\` (listar ficheiros).
> 4. Para cada PDF novo encontrado: (a) verificar se o nome segue a convenção; (b) **mover** para `00_REFERENCIAS\ARTIGOS ACEITOS APÓS REMOÇÃO DAS DUPLICATAS\`; (c) localizar a linha correspondente em `articles_final.xlsx`; (d) preencher coluna `pdf` com o nome do ficheiro + hyperlink `file:///`.
> 5. Após integrar: `NOVOS BAIXADOS MANUALMENTE\` deve ficar **vazia**. Atualizar `RSL_PROGRESSO.md` com novo total de ficheiros e novas contagens de pendentes.
> 6. Re-gerar `ELSEVIER_DOWNLOAD.html` e `DOWNLOAD_MANUAL.html` com o script `gerar_htmls.py`.

### Comandos Python úteis para integração

Listar PDFs em `NOVOS BAIXADOS MANUALMENTE\`:
```python
import os
base = r"C:\Users\ttibu\Documents\03_PROFISSIONAL\02_PESQUISA\04_DISSERTAÇÃO\07_ANÁLISES DE DADOS\REVISÃO SISTEMÁTICA DE LITERATURA"
pasta = os.path.join(base, "NOVOS BAIXADOS MANUALMENTE")
pdfs = sorted(f for f in os.listdir(pasta) if f.lower().endswith(".pdf"))
print(f"{len(pdfs)} PDFs:"); [print(f"  {p}") for p in pdfs]
```

Contar ficheiros na pasta de destino:
```python
dest = os.path.join(base, r"00_REFERENCIAS\ARTIGOS ACEITOS APÓS REMOÇÃO DAS DUPLICATAS")
print(len([f for f in os.listdir(dest) if f.lower().endswith(".pdf")]))
```

Atualizar coluna `pdf` em lote (após matching manual):
```python
import openpyxl, shutil
wb = openpyxl.load_workbook(os.path.join(base, "articles_final.xlsx"))
ws = wb.active
hdrs = [ws.cell(1, c).value for c in range(1, ws.max_column + 1)]
C_PDF = hdrs.index("pdf") + 1
# Para cada (linha, caminho) identificado:
# ws.cell(row, C_PDF).value = caminho_completo
# wb.save(os.path.join(base, "articles_final.xlsx"))
```

---

## MEMÓRIAS RELEVANTES PARA O CLAUDE

Arquivos em `C:\Users\ttibu\AppData\Roaming\Claude\local-agent-mode-sessions\d7a862c2-66c0-4b4a-b024-bead4a4217bb\4dbe1778-d479-494b-9463-8ebed463f431\spaces\930a2f8a-634b-42d1-bf7d-c6a9edb4a009\memory\`:

- `project_rsl_verification.md` — protocolo completo de auditoria
- `MEMORY.md` — índice de memórias

---

**Última atualização:** verificação do artigo 66 (BARBHUIYA et al., 2024) concluída. Próximo: BHAGAT et al., 2021.
