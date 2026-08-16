# Instruções para o Claude — Vault REVISÃO SISTEMÁTICA DE LITERATURA

Quando esta pasta for usada como Projeto Claude, leia este arquivo primeiro. Ele orienta a navegar com eficiência e economizar tokens.

## ⚠️ Este repositório NÃO contém os PDFs — acesso via Google Drive

Este repositório GitHub (`REVISÃO SISTEMÁTICA DE LITERATURA`) é um espelho desta pasta **sem os PDFs de artigos** (excluídos via `.gitignore` — `*.pdf`). Motivo: tamanho (7GB+, ~1.900 PDFs) e direitos autorais de artigos de editoras (Elsevier, Springer, MDPI etc.) — inviável e arriscado versionar no GitHub, mesmo em repo privado.

**Todo o resto está aqui normalmente:** notas `.md`, scripts `.py`, planilhas de controle (`articles_final.xlsx`, `meta_analysis_base.xlsx`, `GRÁFICOS DA RSL.xlsx`), logs de auditoria, PNGs de figuras extraídas.

**Quando a tarefa exigir ler o conteúdo de um PDF específico** (ex.: continuar triagem C1–C8, extrair dados de LCA/CO₂, verificar um artigo citado), use o **conector do Google Drive** (ferramentas `mcp__*` de Drive — `search_files`, `read_file_content`, `download_file_content`) em vez de procurar o arquivo neste repositório. Ele lê o texto completo do PDF (testado e confirmado em 2026-08-03).

**Atenção — existem duas pastas com o nome "REVISÃO SISTEMÁTICA DE LITERATURA" no Google Drive, com propósitos diferentes (não é duplicata acidental):**
- Uma fica na área de **PESQUISA** e contém a **fundamentação teórica** sobre RSL como método (aula, conceitos, PICO, PRISMA genérico) — não tem os PDFs nem o banco de dados desta dissertação.
- A pasta abaixo é a de **execução prática** desta RSL específica (dissertação UHPC) — é aqui que estão o banco de dados e os PDFs. **Use sempre esta para acessar os PDFs dos artigos.**

```
REVISÃO SISTEMÁTICA DE LITERATURA/          (folder id: 1xwwyHNp9VCX1fc4855Ll8IkOAogm-_w5)
└── 00_REFERENCIAS/
    └── ARTIGOS ACEITOS APÓS REMOÇÃO DAS DUPLICATAS/   (folder id: 1R63Q4Lzz6JRRLpwES1Ngyod04q0-r9YP)
        └── ~1.605 PDFs, padrão "SOBRENOME et al., ANO.pdf"
```

Query de busca útil (tool `search_files`):
```
parentId = '1R63Q4Lzz6JRRLpwES1Ngyod04q0-r9YP' and fullText contains 'termo'
```
ou para achar um artigo específico por título/autor:
```
parentId = '1R63Q4Lzz6JRRLpwES1Ngyod04q0-r9YP' and title contains 'SOBRENOME'
```

O Excel `articles_final.xlsx` (versionado neste repo) também é mantido sincronizado na mesma pasta do Drive — mudanças feitas aqui via Claude Code devem ser replicadas lá (upload manual ou `copy_file`/`create_file` do conector) para não perder o trabalho feito do celular, e vice-versa.

<!-- AUTO:BEGIN -->

## Sobre este vault

- **Nome:** REVISÃO SISTEMÁTICA DE LITERATURA
- **Tipo:** Projeto RSL (Revisão Sistemática de Literatura) + Projeto Claude híbrido
- **Total de notas .md:** 16 (11 com frontmatter, 5 sem)
- **PDFs de artigos:** 1.798 (em `00_REFERENCIAS/ARTIGOS ACEITOS APÓS REMOÇÃO DAS DUPLICATAS/`)
- **Banco principal:** `articles_final.xlsx` — 5.093 entradas, coluna `pdf` com caminhos/hyperlinks
- **Metodologia:** Zettelkasten + MOCs + frontmatter (aplicado às notas de metodologia estatística; notas operacionais não seguem o padrão)
- **Última varredura de organização:** 2026-06-04 pela skill `avaliacao-critica-vault` — desatualizada (não cobre a auditoria de dados abaixo); nenhuma rodada nova da skill desde então.
- **Downloads:** ✅ CONCLUÍDO (2026-06-05) — 480/480 Elegíveis com PDF; 60 Sem acesso (era 68 até 2026-08-03; 7 resolvidos na auditoria, 1 seguiu rejeitado por outro motivo).
- **Triagem PDF:** C1 ✅ C2 ✅ C3 ✅ C4 ✅ C5 ✅ C6 ✅ | ~~C7 REMOVIDO (2026-06-22)~~ | C8 ✅ — cascata fechada desde 2026-06-22. Os totais "Aceito/Rejeitado" registrados durante a execução original de cada critério (jun/2026) ficaram levemente desatualizados por correções pontuais linha-a-linha feitas em jul–ago/2026; não recalcular a partir deles sem checar a auditoria abaixo.
- **✅ Estado real (reverificado em 2026-08-16, depois da Opção A):** **1.383 artigos** com C1–C6 e C8 = Aceito em toda a cascata. `status_triagem`: Duplicado 2.622 | Inconclusivo 1.136 | Rejeitado 904 | Elegível 371 | Sem acesso 60. **79 linhas vivas estão sem PDF** e entram na lista de download. *(Medições anteriores: 2026-08-13, 1.401 artigos; 2026-08-03, 1.333. As diferenças vêm das anulações por colisão de PDF e da Opção A.)*
- **🔴 Tarefa #7 em curso — confirmação C2 por PDF:** **1.325 linhas pendentes**, próxima é a **2688**. Lotes 9 e 10 fechados (2673–2679 e 2681–2687). `meta_analysis_base.xlsx` tem **1.694 linhas** de dados na aba `dados_fck`, mais a aba `LEGENDA`.
- **🚨 PRIORIDADE ABERTA — colisões de PDF (descoberta 2026-08-13):** a convenção `SOBRENOME et al., ANO.pdf` **não é única**, e por isso **67 linhas estão associadas ao PDF de outro artigo — 49 delas já com decisão `P:` tomada sobre o artigo errado**. Inventário completo em `AUDITORIA_COLISOES_2026-08-13.csv`. **Anuladas em 2026-08-15** (69 linhas, incluindo 2 indeterminadas); lista de PDFs a rebaixar em `PDFS_A_REBAIXAR_COLISOES.html`.
- **🚨🚨 SEGUNDA FRENTE — as 80 linhas `A_VERIFICAR` (fechada em 2026-08-16):** eram as linhas em que o DOI do banco não aparecia no texto do PDF. Abertas **uma a uma** a pedido da Kiê. Resultado: **54 PDF_ERRADO, 23 CONFERE, 2 ilegíveis, 1 pendente** — ver `VERIFICACAO_80_A_VERIFICAR_2026-08-16.csv`. Das 54 erradas, **18 já tinham decisão `P:` tomada** sobre o artigo errado e **8 alimentaram 14 valores de `fck` na `meta_analysis_base.xlsx`** que vieram do artigo trocado. **✅ Anuladas em 2026-08-16** (a Kiê autorizou; 36 das 54 já tinham sido anuladas a 15/08 pela outra via, o que as confirmou por dois caminhos independentes). Nota metodológica: o grupo A_VERIFICAR tem taxa de erro de **68%**, contra **0%** nos 375 pares já confirmados; "DOI ausente do texto" é, portanto, um sinal forte de ficheiro trocado, não um artefacto de extração.
- **🔤 Convenção de nome nova (autorizada pela Kiê, 2026-08-16):** `SOBRENOME et al., ANO - sufixo-do-DOI.pdf`. Aplica-se aos PDFs novos e, retroactivamente, aos existentes. **Só é seguro renomear pares já confirmados** — renomear pelo DOI do banco um ficheiro que não foi conferido carimba o erro no nome. Estado: **✅ 307 de 307 renomeados (concluído 2026-08-16)** — Drive + `articles_final.xlsx` (valor da célula e alvo do hyperlink) em sincronia, verificado célula a célula; nenhum nome novo colide com outro. Registo completo em `RENOMEACAO_PDFS_2026-08-16.csv` e script `renomear_local.py` (lê esse CSV) para a Kiê aplicar o mesmo na pasta local, que o Drive não alcança. Os PDFs **fora** deste conjunto mantêm o nome antigo de propósito — são os pares por confirmar. **+7 renomeados em 2026-08-16** depois da Opção A (2616, 2689, 2912, 2951, 2986, 3208, 3213), que estavam retidos pela partilha de nome e deixaram de estar. Restam **1.338 ficheiros de dono único ainda com o nome antigo**: são os pares que ninguém conferiu, e renomeá-los pelo DOI do banco carimbaria o erro no nome — não fazer sem confirmar primeiro. **✅ +52 renomeados em 2026-08-16**, os nomes que a auditoria da Terceira Frente tornou seguros — Drive sem nenhum nome antigo do lote, banco sincronizado (60 células, contando as linhas `Duplicado` da mesma obra). Total na convenção nova: **366 ficheiros**. Ficam de fora, de propósito: `SILVA, 2013i.pdf` (dissertação sem DOI, nada para sufixar) e `WU et al., 2014.pdf` (não pertence a nenhuma linha — é cópia do artigo da 3621; não apagar sem a Kiê autorizar).

  ⚠️ **Armadilha nº3 — hyperlink codificado em URL (descoberta e corrigida em 2026-08-16):** o alvo do hyperlink guarda o caminho com os espaços em `%20` (`.../BATUECAS%20et%20al.,%202021a.pdf`), enquanto o valor da célula tem espaços normais. Um `target.replace(nome_antigo, nome_novo)` **falha em silêncio** — não levanta erro, apenas não substitui nada, e a célula fica com o nome novo a apontar para o ficheiro antigo. Foi o que aconteceu a **249 linhas** (189 da leva dos 307, 60 da dos 52); todas corrigidas. A verificação que deixou passar o problema comparava o valor da célula com o alvo **sem descodificar o URL** — comparar sempre com `urllib.parse.unquote(target)`. A correcção segura é substituir a última componente do caminho (depois do último `/`) e repor os espaços como `%20` se o segmento original os tinha assim.

  📌 **Defeito anterior, ainda por resolver — 30 linhas em `HYPERLINKS_DESALINHADOS_2026-08-16.csv`:** o valor da célula tem sufixo de desambiguação (`BARBHUIYA et al., 2024c.pdf`) mas o hyperlink aponta para o nome base (`BARBHUIYA et al., 2024.pdf`). Não vem das renomeações — é anterior. Não foi mexido porque resolver exige saber se o ficheiro com sufixo existe mesmo no Drive; fazer isso antes de renomear qualquer um destes.

  ⚠️ **Armadilha do conector Drive nº1 (descoberta 2026-08-16):** `search_files` devolve **no máximo 10 resultados por página**. Uma query com 12 títulos em `or` devolve 10 e cala-se sobre os outros 2 — parece que os ficheiros não existem. Manter os lotes em ≤8 títulos, ou conferir sempre o número de resultados contra o número de títulos pedidos.

  ⚠️⚠️ **Armadilha do conector Drive nº2 (descoberta 2026-08-16) — a mais perigosa das duas:** `fullText contains 'frase de várias palavras'` **NÃO faz correspondência exacta de frase**. Devolve acertos por tokens soltos, e portanto dá **falsos positivos**. Verificado: `PITTAU, 2019i.pdf` acertou na sonda `'Massive timber building'`, que não existe no texto (a leitura mostrou que o ficheiro é o artigo 296/012037); e `SILVA, 2013i.pdf` acertou em `'Influence of service life'`, que tem **zero** ocorrências no ficheiro. **Só usar sondas de token único e distintivo** — o sufixo do DOI (`su16020484`, `j.eti.2024.103857`) é o ideal. Para decidir de quem é um ficheiro, sonda de frase não serve; ou é DOI, ou é abrir e ler.

  💡 **Truque para ler PDF grande sem rebentar o contexto:** `read_file_content` num PDF de artigo devolve 80–260 mil caracteres e falha por excesso de tokens, mas **grava o resultado num ficheiro** e dá o caminho. Ler daí só os primeiros ~1.200 caracteres basta para identificar título e autores; e dá para contar ocorrências de um termo no texto todo com um script, que é como se apanham os falsos positivos da armadilha nº2.
- **✅ TERCEIRA FRENTE — nomes de ficheiro partilhados (fechada em 2026-08-16):** o banco tinha **255 nomes a servir mais do que uma linha**. Separando o joio: **196 são duplicados legítimos** (as várias linhas são a mesma obra, o ficheiro está certo para todas) e **54 eram atribuição ambígua** — obras diferentes a disputar o mesmo ficheiro. Todos os 54 resolvidos, por três vias: 31 pelo cruzamento com o `VERIFICACAO_DOI_PDF_WORKLIST.csv` (que já tinha testado a presença do DOI no texto), 17 por sonda de DOI nova no Drive, e 6 abrindo o ficheiro. Resultado: **73 linhas ficaram sem PDF** pela Opção A (56 Inconclusivo, 9 Duplicado, 8 Rejeitado) — registo em `SOLTURA_PDF_OPCAOA_2026-08-16.csv`. **Hoje há zero nomes ambíguos no banco.**

  Achados que vale a pena reter: **em 7 casos o dono era o oposto do que a ordem do banco sugeria** (LIU 2024→4541, PUSHKAR 2022b→4483, XU 2024→3777, ZHOU 2023→4863, KARLSSON→4377, MOSTAFAEI→4263, SILVA→2850) — nos dois últimos a presença do DOI do outro candidato era **auto-citação entre artigos do mesmo grupo**, que só a leitura desfaz. E **um ficheiro não era de nenhuma das linhas que o reclamavam**: `WU et al., 2014.pdf` é o artigo 10.1016/j.rser.2014.04.070 da linha 3621, que já tem PDF próprio — é uma cópia redundante, e as duas linhas que apontavam para ele (3314, 4882) ficaram sem PDF.

  Nota que continua válida: em vários dos casos errados o PDF «errado» é afinal o PDF *certo de outra linha do banco* (2951/4128, 2986/4028, 2912/3499, 2689/4790) — os ficheiros não se perderam, foram mal atribuídos.
- **Auditoria de qualidade dos dados (12/07/2026 → 03/08/2026):** ✅ CONCLUÍDA — ver `PENDENCIAS_AUDITORIA_2026-07-12.md`. 10 achados (cascata quebrada, C8 sem prefixo `R:`/`P:`, 596 resíduos de C7, linhas "Sem acesso" com PDF já disponível, status_triagem dessincronizado de decisões já tomadas por PDF etc.) — todos resolvidos, exceto **1 pendência em aberto**: linha 2897 (di Summa et al., 2023, *Structural Concrete*, DOI `10.1002/suco.202300645`) aguardando acesso ao PDF via biblioteca institucional da Kiê.

## Preferências de interação da Kiê

- **⭐ Perguntas: sempre no texto do chat, nunca em componente de escolha múltipla** (pedido explícito, 2026-08-12). Não usar a ferramenta de perguntas com opções — escrever a pergunta diretamente na resposta, em texto corrido, e aguardar. Vale para dúvidas de triagem, decisões de critério e qualquer outra escolha.
- **Idioma:** português europeu nas respostas; os dados e carimbos nas planilhas ficam sem acentos (ver regra de `clean_str`).

## Como navegar economizando tokens

Hierarquia recomendada:

1. **MOC mestre primeiro.** Leia `_MOC.md` na raiz para visão geral de todas as áreas.
2. **MOC da área.** Antes de ler arquivos individuais, consulte `<AREA>/_MOC.md`.
3. **RSL_PROGRESSO.md.** Para estado atual do projeto (contagens PRISMA, downloads pendentes, tarefas abertas).
4. **Frontmatter das notas.** Antes do corpo, leia o frontmatter (campos `titulo`, `descricao`, `tags`, `status`).
5. **articles_final.xlsx.** Não é diretamente legível pelo Claude; use scripts Python + openpyxl para extrair dados quando necessário.

## Áreas raiz

- **`00_REFERENCIAS/`** (catálogo) — 7 notas .md + ~1.630 PDFs. Contém notas de metodologia estatística e documentação PRISMA. MOC: [[00_REFERENCIAS/_MOC]]
- **`01_BUSCAS NAS BASES/`** (temporal) — 4 buscas sequenciais (BUSCA 01–04). Arquivos .bib/.ris/.csv das buscas originais. MOC: [[01_BUSCAS NAS BASES/_MOC]]
- **`02_ARQUIVOS ANTERORES/`** (arquivo) — Backups e versões obsoletas. Não avaliar como área ativa.
- **`04_EXTERNAL SOURCES/`** (catálogo) — 8 PDFs de fontes externas (Celik, Costa, Mohammadi…). MOC: [[04_EXTERNAL SOURCES/_MOC]]

## Notas operacionais na raiz

| Nota | Propósito |
|---|---|
| `CRITERIOS_E_NUANCES_RSL.md` | **⭐ Ler antes de qualquer triagem C1–C8.** Consolida num único arquivo o texto literal dos critérios + todos os refinamentos/decisões acumulados (RSL_PROGRESSO.md + CLAUDE.md + `claude/memoria/rsl-*.md`), o protocolo vigente de confirmação por PDF e o processo de extração para `meta_analysis_base.xlsx` (tarefa #7). Criado 2026-08-14. |
| `PROMPT_RETOMADA_AUDITORIA_COLISOES_PDF.md` | **⭐ PRIORITÁRIO (criado 2026-08-13).** Prompt para retomar a auditoria de colisões de PDF (67 linhas com ficheiro errado, 49 já com decisão tomada), as 7 linhas revistas à espera de confirmação, e só depois a triagem C2. Contém as regras novas da sessão de 2026-08-13. |
| `AUDITORIA_COLISOES_2026-08-13.csv` | Veredito linha a linha das 131 afetadas por colisão: DOI do banco vs DOI realmente no PDF. Lista de trabalho da correção. |
| `SOLTURA_PDF_OPCAOA_2026-08-16.csv` | **Registo da Opção A (2026-08-16).** As 73 linhas que ficaram sem PDF porque o ficheiro que reclamavam é de outra linha: número da linha, nome do ficheiro retirado, linha a que pertence, status. Cada uma tem também o motivo por extenso no carimbo (`comments`) do `articles_final.xlsx`. |
| `COLISOES_PDF_2026-08-13.csv` | Inventário bruto das linhas que partilham nome de ficheiro com DOIs diferentes; mantido por rastreabilidade. |
| `PROMPT_RETOMADA_CONFIRMACAO_PDF_METANALISE.md` | Prompt para retomar a tarefa #7 (confirmação C2–C8 por PDF + extração de metanálise) numa sessão nova — cita o `CRITERIOS_E_NUANCES_RSL.md` e o ponto exato onde parou. Criado 2026-08-14. |
| `RSL_PROGRESSO.md` | Estado atual: contagens PRISMA, downloads, TODOs (⚠️ última entrada datada é 2026-06-22 — para o estado real da triagem por PDF, ver bullet "Estado real pós-auditoria" acima) |
| `PENDENCIAS_AUDITORIA_2026-07-12.md` | Auditoria de qualidade de dados do funil C1-C8 — concluída 2026-08-03, 1 pendência aberta (linha 2897) |
| `DOWNLOAD_MANUAL.html` | ~~Apagado~~ — download concluído (2026-06-05) |
| `DOWNLOAD_LESSONS_LEARNED.md` | Documentação de lições aprendidas no processo de download |
| `RELATORIO_VERIFICACAO_BD_RSL.md` | Relatório de verificação do banco de dados |
| `EXTERNAL_SOURCES_DOIs.md` | Lista de DOIs de fontes externas |
| `FASE5_LOG_PROBLEMAS.md` | Log de problemas da Fase 5 (meta-análise) |
| `RSL_COL_R_LOG.md` | Log de coleta R (análise estatística) |
| `PROMPT_RETOMADA_VERIFICACAO_RSL.md` | Prompt de retomada para verificação RSL |
| `PROMPT_RETOMADA_C5.md` | ~~ARQUIVADO~~ — C5 concluído 2026-06-21 |
| ~~`PROMPT_RETOMADA_C6.md`~~ | ⚠️ **Referenciado aqui mas o ficheiro não existe mais no repo nem em `02_ARQUIVOS ANTERORES`** (constatado 2026-08-03) — as regras C6 sobrevivem em `RSL_PROGRESSO.md` (seção C6) e neste ficheiro (seção "Regra C6 — refinamentos consolidados"), então nada foi perdido, mas a linha da tabela ficou órfã. Remover esta entrada quando alguém confirmar que o ficheiro nunca vai voltar. |
| `PROMPT_RETOMADA_C7.md` | ~~ARQUIVADO~~ — C7 REMOVIDO da RSL (2026-06-22); ver nota no ficheiro |
| `como_contornamos_o_akamai.md` | Documentação técnica de contorno anti-bot |

## Convenções deste vault

### Frontmatter padrão (notas de metodologia)

```yaml
titulo: ...
descricao: ...
tags: [academico-e-pesquisa, meta-analise, metodologia]
status: revisado | em-andamento | rascunho | arquivado
ultima_atualizacao: YYYY-MM-DD
```

**Cobertura:** 11/16 notas (68,75%) — as notas operacionais na raiz não têm frontmatter.

### Tags mais frequentes

- `academico-e-pesquisa` (11 notas)
- `revisao-sistematica` (5)
- `UHPC` (4)
- `meta-analise` (4)
- `metodologia` (4)
- `engenharia-e-construcao` (2)
- `tecnologia-da-informacao` (2)
- `PRISMA` (1)

### Nomenclatura de PDFs

Padrão: `SOBRENOME et al., ANO.pdf` (sem caracteres especiais: ç→c, ã→a, ł→l, š→s).

### Banco de triagem (articles_final.xlsx)

- Coluna `pdf`: nome do ficheiro + hyperlink `file:///` para o caminho completo
- Fundo amarelo na célula `pdf` = PDF pendente de download
- Coluna `status_triagem`: Elegível | Inconclusivo | Duplicado | Sem acesso | Rejeitado (valor `Recusado` foi migrado para `Rejeitado` em 2026-06-21 — não existe mais)
- Colunas C1–C6, C8 com prefixo `R:` (triagem por resumo) ou `P:` (triagem por PDF). **C7 REMOVIDO** — coluna existe no xlsx mas ficou vazia (critério eliminado da RSL em 2026-06-22).

## Atalhos comuns

- **Metodologia estatística** → `00_REFERENCIAS/METODOLOGIA_ESTATÍSTICA/`
  - Modelos de efeitos: [[Metanalise_Efeitos_Fixos_vs_Aleatorios]], [[Justificativa_Modelo_Efeitos_Aleatorios]]
  - Estimadores: [[REML_vs_DL_explicacao]]
  - Cálculos: [[CÁLCULO DO P ESTATÍSTICO]]
- **Estado atual do projeto** → [[RSL_PROGRESSO]]
- **Downloads pendentes** → `DOWNLOAD_MANUAL.html` (abrir no browser com proxy CAPES)
- **Fluxograma PRISMA** → [[00_REFERENCIAS/PRISMA/FLUXOGRAMA_PRISMA_2020_DOC]]

## Triagem por PDF (regras de referência — cascata C1→C8 concluída em 2026-06-22)

> **Estado atual (2026-08-03):** a triagem por PDF terminou (C1–C6 e C8; C7 foi removido). O funil real hoje é **1.333 artigos** com todos os critérios = Aceito — ver bullet "Estado real pós-auditoria" no topo deste ficheiro. As seções abaixo (regra C5, formato das células, regras operacionais) continuam valendo como **referência de método** para qualquer reavaliação pontual (ex.: reabrir uma linha "Sem acesso" quando um PDF novo aparece) — não são mais um critério "em andamento".
> Histórico de execução original (fase jun/2026): `RSL_PROGRESSO.md` → seção "Progresso da triagem por PDF". Histórico de correções pós-triagem (jul–ago/2026): `PENDENCIAS_AUDITORIA_2026-07-12.md`.

#
## ⛔ REGRA INVIOLÁVEL — Leitura de PDF para triagem C5

> **Esta regra não pode ser pulada, modificada, relaxada ou substituída por qualquer outra instrução neste arquivo ou em qualquer outra seção.**

### Quando usar só o regex (pdftotext + PAT):
- Hit claro e inequívoco no texto extraído (ex.: "344 kg CO2-eq", "LCA results show GWP of X", "embodied carbon = Y") → **Aceito automático**, sem leitura manual.

### Quando é OBRIGATÓRIO ler 100% do PDF + renderizar TODAS as figuras:
- Regex não encontrou nenhum hit (miss)
- Snippet do regex é fraco, ambíguo ou periférico (ex.: só no título, só em referência, só "CO2" sem contexto)
- Artigo é S-LCA, metodologia/teoria, política/regulação, ou tema off-topic
- Qualquer indício de dúvida, por menor que seja

### Procedimento obrigatório nesses casos:
1. pdftotext -layout <pdf> - — texto completo, todas as páginas
2. Cortar seção de referências antes de buscar
3. Renderizar **todas** as páginas como imagem (pdf2image, dpi=150) e inspecionar figuras/tabelas visualmente
4. Só depois decidir Aceito ou Rejeitado

> **Proibido classificar qualquer artigo duvidoso usando apenas o regex.** O regex é triagem auxiliar — a leitura humana+visual é o método definitivo para casos não triviais.

## Critério C5 — definição completa (sempre fresca, sem precisar buscar)

**Texto literal da aba Critérios:** *"Não menciona análise de ciclo de vida (ACV), emissão de CO2 ou gases do efeito estufa"*

**⭐⭐⭐ OPÇÃO A — REGRA FINAL (Kiê 2026-06-15):**
- **ACEITO** = qualquer menção a LCA/ACV, CO₂, GWP, GHG, carbon footprint, embodied carbon, climate change, greenhouse gas, low-carbon — com **qualquer resultado** (valor absoluto, %, citação de outro estudo, resultado em figura).
- **REJEITADO** = PDF inteiro (texto + figuras renderizadas) sem **nenhuma** menção relacionada ao material. Durabilidade/resistência/geomecânica puras sem CO₂ = Rejeitado.
- **Exceção Rejeitado:** CO₂ puramente analítico-químico (picos FTIR de carbonatos) sem LCA/impacto ambiental.
- **Obrigatório antes de rejeitar:** ler 100% das páginas + renderizar figuras/gráficos.
- **S-LCA:** verificar se o corpo menciona CO₂/GHG no contexto/motivação — se sim, Aceito. Se LCA é 100% social sem nenhuma menção ambiental = Rejeitado.

**PAT regex (pdftotext):** lca|life.cycle.assess|carbon.footprint|embodied.carbon|gwp|global.warming.potential|co2.eq|co2eq|kgco2|greenhouse.gas|ghg|carbon.emission|climate.change|co2|embodied.emission|carbon.intensi|low.carbon
## Regras operacionais (sempre vigentes)

- **⭐ Indicador correto (reconfirmado 2026-08-03, corrige nota conflitante de 2026-06-06):** progresso medido por presença de `P:` nas células (P:Aceito / P:Rejeitado), NÃO por ter qualquer conteúdo. **Células com apenas `R:` são consideradas NÃO triadas, mesmo que título/resumo pareçam suficientes para decidir.** Toda linha `R:Aceito` precisa ser confirmada com `P:` antes de ser considerada definitiva — não é permitido aceitar um critério só com base em título/resumo. Uma nota anterior (`claude/memoria/rsl-marcacao-R-vs-P.md`, sessão 2026-06-06) permitia manter `R:` quando "título/resumo resolvia" — **essa permissão foi revogada pela Kiê em 2026-08-03**; a nota de memória foi corrigida.
- **Verificação PDF × artigo:** para **cada artigo** do lote, conferir título e primeiro autor na primeira página do PDF antes de avaliar. Obrigatório, sem exceção.
- **⭐ Páginas a ler (reconfirmado 2026-08-03):** desconsiderar resumo/título — ler as **primeiras 5 páginas do corpo do artigo**. Se essas 5 páginas não forem suficientes para decidir `P:Aceito` ou `P:Rejeitado`, continuar lendo até conseguir decidir. (Substitui a orientação anterior de "primeiras 2 páginas".)
- **Colisões de PDF:** nunca pular. Claude para, reporta DOI/título/autor e aguarda a Kiê baixar o PDF correto antes de continuar essa linha.
- **Parar entre critérios:** ao concluir um critério, parar e aguardar confirmação da Kiê antes de iniciar o próximo.
- **Lotes de 50 artigos:** salvar e reportar ao final de cada lote.
- **Casos ambíguos:** parar e tirar dúvida com a Kiê antes de classificar.

### Formato das células C1–C8

Preservar `R:` existente e acrescentar `P:` separado por ` | `.
- Com R:: `R:Aceito | P:Aceito`
- Sem R:: `P:Aceito` ou `P:Rejeitado`
- Colisão sem PDF correto: aguardar resolução — não registrar `P:` até ter o PDF certo.

### Coluna material_C2

Preencher para todos os artigos com `P:Aceito` em C2. Formato descritivo: material principal + contexto (ex: `"geopolímero para impressão 3D (revisão de materiais precursores)"`). Artigos rejeitados em C2 não preenchem esta coluna.

## Último relatório de avaliação

Nenhum — o relatório de 2026-06-04 foi removido em 2026-08-03 (todas as suas 5 pendências em aberto já haviam se resolvido organicamente; ver histórico de commits). Rodar a skill `avaliacao-vault` quando quiser um novo diagnóstico.

<!-- AUTO:END -->

<!-- USER:BEGIN -->
<!-- conteúdo original preservado — CLAUDE.md manual encontrado sem marcadores em 2026-06-04; backup em _AVALIACOES/_backups/CLAUDE_backup_2026-06-04.md -->

# Convenções da pasta REVISÃO SISTEMÁTICA DE LITERATURA

## Regra de arquivamento — backups e versões obsoletas

**Manter na raiz APENAS os arquivos ativos e mais atualizados.**

Sempre que surgir um arquivo obsoleto, backup, ou versão anterior, mover imediatamente para:

```
07_ANÁLISES DE DADOS/REVISÃO SISTEMÁTICA DE LITERATURA/02_ARQUIVOS ANTERORES/
```

### O que vai para 02_ARQUIVOS ANTERORES

- Backups automáticos gerados por scripts (`*_backup_*.xlsx`, `*_backup_*.csv`)
- Versões anteriores de planilhas (`articles_final_new.xlsx` → `articles_final_old.xlsx`)
- Arquivos corrompidos ou descartados
- Qualquer arquivo com sufixo `_old`, `_bak`, `_backup`, `_pre-*`, `_v[0-9]*` que não seja a versão corrente

### O que fica na raiz

| Arquivo | Descrição |
|---|---|
| `articles_final.xlsx` | Banco de triagem ativo (todas as 5.093 entradas, PDFs linkados) |
| `GRÁFICOS DA RSL.xlsx` | Gráficos da meta-análise |
| `BANCO DE DADOS DA RSL.xlsx` | Banco principal da RSL (já na pasta 02_ARQUIVOS ANTERORES — versão de trabalho migrou para o Excel do vault) |
| Scripts `.py` | Scripts de análise ativos |

### Convenção de nomenclatura ao arquivar

Ao mover, renomear descritivamente se necessário:
- `articles_final_new.xlsx` → `articles_final_old.xlsx` (arquivado em 2026-05-28)
- `*_backup_YYYYMMDD_HHMMSS.xlsx` → manter nome original

---

*Nota criada em 2026-05-28 para evitar confusão entre versões de arquivos.*

---

## Processo de download de PDFs — arquitetura em 4 camadas

> Documentado em 2026-06-02 após sessão de integração de PDFs manuais.

A pasta de destino de todos os PDFs é:
```
00_REFERENCIAS\ARTIGOS ACEITOS APÓS REMOÇÃO DAS DUPLICATAS\
```
O banco de triagem que regista os caminhos é `articles_final.xlsx`, coluna `pdf`.

---

### Camada 1 — Unpaywall automático (`download_pdfs_win.py`)

**Quando usar:** primeira execução; roda sem supervisão, processa todos os registros com `is_oa=true` no scan Unpaywall.

**Inputs:**
- `unpaywall_scan_results.json` — resultado do scan OA (gerado previamente)
- `articles_final_backup_*.xlsx` — versão de entrada do banco

**Checkpoint:** `download_checkpoint.json` — guarda `done`, `ok`, `fail`, `ok_rows`

**O que faz:** tenta descarregar o `pdf_url` de cada registo OA. Domínios bloqueados (Elsevier, Wiley, T&F, MDPI, ACS, ASCE…) são ignorados de imediato sem fazer pedido HTTP. Se o download tiver sucesso, grava o caminho completo na coluna `pdf` do Excel de saída e remove o fundo amarelo da célula.

**Outputs gerados:** `articles_final_new_YYYYMMDD_HHMMSS.xlsx` + `articles_final_backup_YYYYMMDD_HHMMSS.xlsx` (mover ambos para `02_ARQUIVOS ANTERORES/` após integrar).

---

### Camada 2 — MDPI via Chrome CDP (`mdpi_batch_dl.py` / `mdpi_resume.py`)

**Quando usar:** após Camada 1; para os artigos MDPI que ficaram pendentes (MDPI bloqueia automação simples com 403).

**Inputs:** `mdpi_todo.json` — lista de registos MDPI com campos `row`, `pdf_url`, `filename`

**Checkpoint:** `chrome_dl_checkpoint.json` — campos `processed`, `downloaded`, `failed`

**O que faz:** lança Chrome em modo depuração remota (CDP porta 9224 para `mdpi_batch_dl.py`, 9222 para `mdpi_resume.py`), injeta script anti-detecção, visita a página do artigo como warm-up, depois navega para o URL do PDF e aguarda o ficheiro em `C:\Temp\mdpi_dl\`. Após validar assinatura `%PDF`, move para a pasta de destino com o nome `filename` do `todo.json`.

**Diferença entre os dois scripts:** `mdpi_resume.py` é idêntico em lógica mas usa perfil Chrome diferente (`chrome_resume_profile`) — usar se o perfil principal ficar corrompido ou travar.

---

### Camada 3 — IOP Publishing + repositórios Handle (`iop_hdl_dl.py`)

**Quando usar:** para artigos IOP (10.1088) e artigos em repositórios institucionais com URL `hdl.handle.net/…`.

**Inputs:** `iop_todo.json` + `hdl_todo.json` — combinados internamente; campos `row`, `pdf_url`, `filename`, `_type` (`iop` ou `hdl`)

**Checkpoint:** `iop_hdl_checkpoint.json`

**Estratégias:**
- `dl_iop`: mesma lógica do MDPI — warm-up na página do artigo, depois navega para URL direto do PDF (CDP porta 9223).
- `dl_hdl`: navega ao handle (redireciona para repositório), executa JS para encontrar links com `.pdf` ou texto "PDF/Download/Full text", navega ao link encontrado e aguarda download.

---

### Camada 4 — Downloads manuais via CAPES / listas HTML

**Quando usar:** para Elsevier e quaisquer artigos que as camadas 1–3 não conseguiram.

**Ficheiros de apoio (na raiz da pasta RSL):**
- `ELSEVIER_DOWNLOAD.html` — lista clicável dos artigos Elsevier pendentes
- `DOWNLOAD_MANUAL.html` — lista de todos os outros artigos pendentes de download manual

Abrir no browser conectado ao proxy CAPES (VPN ou rede da instituição). Clicar nos DOIs e guardar os PDFs para a pasta `00_REFERENCIAS\ARTIGOS ACEITOS APÓS REMOÇÃO DAS DUPLICATAS\BAIXADOS MANUALMENTE\` (ver abaixo).

#### ⚠️ Formato CORRETO do link proxy CAPES (validado em 2026-06-05)

O acesso só é liberado com o **host reescrito** (pontos→hífens) + sufixo `.ezNNN.periodicos.capes.gov.br`, usando a **página do artigo** (não o caminho `content/pdf`):

```
https://link-springer-com.ez128.periodicos.capes.gov.br/article/10.1007/{DOI-suffix}
https://www-sciencedirect-com.ez128.periodicos.capes.gov.br/science/article/pii/{PII}
```

Regras aprendidas:
- **NÃO usar** `ezl` (ex.: `doi-org.ezl.periodicos.capes.gov.br`) — host inexistente, dá `ERR_CONNECTION_TIMED_OUT`. O número do proxy é `ezNNN` (ex.: `ez128`), **atribuído por sessão pelo CAPES** — pode mudar; confirmar com a Kiê a sessão ativa.
- Usar a **página do artigo** (`/article/...`), não `content/pdf` — a página é que renderiza o botão "Download PDF" com "Access provided by CAPES".
- Unpaywall pode marcar `is_oa=true` incorretamente para artigos Springer/Elsevier que na prática estão atrás de paywall — não confiar; ir direto pelo proxy CAPES.

---

### Integração de PDFs baixados manualmente

**Pasta de entrada:** `00_REFERENCIAS\ARTIGOS ACEITOS APÓS REMOÇÃO DAS DUPLICATAS\BAIXADOS MANUALMENTE\`

**Regra:** após integração, a pasta deve ficar vazia — os ficheiros são **movidos** para o destino (não copiados). A pasta serve apenas como área de entrada temporária.

### ⚠️ REGRA CRÍTICA — NUNCA APAGAR FICHEIROS DE BAIXADOS MANUALMENTE

> Adicionado em 2026-06-03 após incidente de deleção acidental de 44 PDFs.

**PROIBIDO:** apagar qualquer ficheiro de `BAIXADOS MANUALMENTE` automaticamente, sem autorização explícita da Kiê, mesmo que não haja match no banco.

**O que fazer com ficheiros sem match:**
1. Tentar matching por DOI (extraído do PDF)
2. Se falhar: tentar matching por título, autor e ano (metadados do PDF via pypdf / crossref)
3. Se ainda sem match: **MOVER** para `BAIXADOS MANUALMENTE\PARA VERIFICAR\` e **reportar** à Kiê quais foram movidos, com os dados encontrados (DOI extraído, título, autor)
4. **Nunca apagar** sem confirmação explícita

**Protocolo de matching correto (em ordem de prioridade):**
1. DOI exato no banco (`doi` column)
2. DOI limpo (remover sufixos de journal, corrigir ligaduras tipográficas)
3. DOI por prefixo (ex: `10.1016/j.jclepro.2019.1` → buscar `startswith`)
4. Título normalizado (lowercase, sem pontuação) — comparar com `title` column
5. Autor + ano + journal (combinação)
6. Se todos falharem → PARA VERIFICAR, nunca deletar

**Fluxo de integração:**

1. Renomear os PDFs para o padrão `SOBRENOME et al., ANO.pdf` (sem caracteres especiais: ç→c, ã→a, ł→l, š→s) — ver convenção em "Notas sobre nomenclatura" no `RSL_PROGRESSO.md`.
2. **Mover** para `00_REFERENCIAS\ARTIGOS ACEITOS APÓS REMOÇÃO DAS DUPLICATAS\`.
3. Abrir `articles_final.xlsx` e localizar a linha correspondente ao artigo (por DOI, título ou autor).
4. Na coluna `pdf`: **valor da célula = nome do ficheiro** (`SOBRENOME et al., ANO.pdf`) + **hyperlink = URI `file:///` apontando para o caminho completo**. NÃO preencher o caminho completo como texto — usar `cell.hyperlink` via openpyxl ou inserir hiperlink manual no Excel (Ctrl+K).
5. Remover o fundo amarelo da célula `pdf` se estiver marcada.
6. Re-gerar `DOWNLOAD_MANUAL.html` directamente (Claude faz isso, não há script standalone).

**Nota (2026-06-03):** os scripts de download automático (Camadas 1–3) foram removidos. O download é agora exclusivamente manual via `DOWNLOAD_MANUAL.html` + CAPES. O HTML é gerado directamente pelo Claude quando solicitado.

---

### Ficheiros de estado / checkpoint — referência rápida

| Ficheiro | Pertence a | Descrição |
|----------|-----------|-----------|
| `unpaywall_scan_results.json` | Camada 1 | Resultados do scan OA (input) |
| `download_checkpoint.json` | Camada 1 | Estado do download Unpaywall |
| `mdpi_todo.json` | Camada 2 | Lista de artigos MDPI pendentes |
| `chrome_dl_checkpoint.json` | Camada 2 | Estado do Chrome CDP (MDPI) |
| `iop_todo.json` | Camada 3 | Lista de artigos IOP pendentes |
| `hdl_todo.json` | Camada 3 | Lista de artigos Handle/repositório |
| `iop_hdl_checkpoint.json` | Camada 3 | Estado do Chrome CDP (IOP/hdl) |
| `ELSEVIER_DOWNLOAD.html` | Camada 4 | Lista clicável Elsevier pendentes |
| `DOWNLOAD_MANUAL.html` | Camada 4 | Lista clicável outros pendentes |

---

*Secção adicionada em 2026-06-02.*
## articles_final.xlsx — Índices de colunas verificados ⚠️

> Adicionado 2026-06-15 após bugs causados por índices errados em C4/C5.

Usar **sempre** estes índices ao escrever scripts openpyxl (`ws.cell(row, column)`, 1-based). **MAPA COMPLETO RE-VERIFICADO pelo cabeçalho em 2026-06-21:**

| Campo | col openpyxl | Excel | Nota |
|-------|-------------|-------|------|
| `pdf` | **11** | K | Caminho/nome do PDF |
| `url` | **12** | L | URL do artigo |
| `status_triagem` | **20** | T | Elegível/Inconclusivo/Rejeitado/Duplicado/Sem acesso |
| `C1` | **21** | U | Triagem C1 |
| `C2` | **22** | V | Triagem C2 |
| `material_C2` | **23** | W | Material identificado (⚠️ FICA ENTRE C2 e C3!) |
| `C3` | **24** | X | Triagem C3 |
| `C4` | **25** | Y | Triagem C4 |
| `C5` | **26** | Z | Triagem C5 |
| `C6` | **27** | AA | Triagem C6 |
| ~~`C7`~~ | **28** | AB | ~~Triagem C7~~ — **REMOVIDO (2026-06-22), coluna vazia** |
| `C8` | **29** | AC | Triagem C8 |
| `comments` | **32** | AF | Carimbo / justificativa |
| `rastreio_potencial_futuro` | **33** | AG | Tags de rastreio |

> ⚠️⚠️ **ARMADILHA FATAL (causou bug em 2026-06-21):** a coluna `material_C2` (23) fica ENTRE C2 e C3. NÃO usar `zip(range(21,29), ["C1".."C8"])` — isso pula material_C2 e desloca C3–C8 em 1 coluna! Sempre usar o dict explícito: `COL={"C1":21,"C2":22,"C3":24,"C4":25,"C5":26,"C6":27,"C7":28,"C8":29}`.

### ❌ Armadilha — filtro errado para universo C5

```python
# ERRADO: captura R:Aceito-only e C4-Rejeitados (719 linhas a mais)
'Aceito' in str(c4_val)

# CORRETO: apenas linhas com P:Aceito explícito no C4
'P:Aceito' in str(c4_val)   # col 25
```

### ❌ Armadilha — IllegalCharacterError no openpyxl

PDFs podem conter caracteres de controle nos snippets extraídos por pdftotext. Antes de qualquer escrita no xlsx:

```python
import re
def clean_str(s):
    return re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', str(s))
# Aplicar em TODA string antes de ws.cell(...).value = ...
```

### PDF cid-encoded / garbled

Quando pdftotext retorna texto cifrado (fonte não-padrão, padrão ROT), usar OCR via pdf2image + tesseract. Nunca classificar REJEITADO sem ter lido o conteúdo real.

## ⭐ Lógica R: vs P: e regras de cascata (fonte: aba Critérios, lida 2026-06-21)

**Prefixos (aba Critérios, linhas 14–15):**
- **`R:`** = decisão tomada pela triagem de **título/resumo** (sem PDF). Valores: `R:Aceito | R:Rejeitado | R:A revisar`.
- **`P:`** = decisão pela leitura do **PDF completo**. Valores: `P:Aceito | P:Rejeitado | P:A revisar`.
- O C8 é decidido por **metadado (`document_type`)** → usa prefixo `R:` (disponível sem PDF).

**Regras de cascata (confirmadas com a Kiê 2026-06-21):**
1. **`P:` é o histórico de quem foi triado por PDF.** Um artigo rejeitado por PDF num critério (ex.: `P:Rejeitado` em C4) MANTÉM o histórico P: (o `P:Rejeitado` + os `P:Aceito` dos critérios anteriores). NÃO apagar esse histórico.
2. **Rows FORA-DA-CASCATA não recebem P: em critério nenhum.** Fora-da-cascata = `status_triagem` ∈ {`Duplicado`, `Sem acesso`, `Rejeitado`-por-resumo}. Esses já foram decididos por R:/metadado e nunca entram na triagem-PDF.
3. **Não existe mais `status_triagem = Recusado`.** Padronizado: usar só `Rejeitado`. (Era 1 row — 2897 — migrado em 2026-06-21.)
4. **Ao fim de cada lote, atualizar `status_triagem` → `Rejeitado`** para todo row que recebeu `P:Rejeitado` no critério do lote (regra Kiê 2026-06-21).
5. **Vazamento de cascata** = artigo com `P:Rejeitado` em Cn que recebeu `P:` em Cm>n. É erro; remover os P: posteriores ao P:Rejeitado.

**Universo correto da triagem-PDF de um critério Cn:**
rows na cascata (`status` ∈ {Elegível, Inconclusivo}) **E** `P:Aceito` em C(n-1) **E** sem `P:Rejeitado` em nenhum critério anterior **E** Cn ainda sem `P:`.
- ⚠️ Filtrar só por `"P:Aceito" in C(n-1)` NÃO basta — pega falsos-positivos sem PDF/fora-da-cascata. Cruzar SEMPRE com `status_triagem`.

## Correções de base 2026-06-21 (antes de retomar o C6)

Durante o C6 detectaram-se inconsistências herdadas + um bug de coluna. Tudo corrigido (backups em `02_ARQUIVOS ANTERORES/`):
- **Grupo A** — 4 rows `Duplicado`/`Sem acesso` com `P:` indevido → P: removido (3258, 3261, 3262, 3454).
- **Grupo B** — 3 vazamentos de cascata → P: posteriores ao `P:Rejeitado` removidos (3259, 3273, 3291).
- **Grupo C** — `Recusado`→`Rejeitado` (2897, +remoção P:C1); 100 `Inconclusivo` com `P:Rejeitado` em C1–C5 → `status=Rejeitado`.
- **Grupo D** — 1.705 células C8 sem prefixo → prefixadas `R:` (só rows na cascata).
- **Retro C6** — 8 rejeitados C6 dos Lotes 1–2 → `status=Rejeitado` (2581, 2753, 2790, 2805, 3016, 3120, 3159, 3254).

**status_triagem após correções:** Duplicado 2.624 · Inconclusivo 1.246 · Rejeitado 676 · Elegível 479 · Sem acesso 68.

## Regra C6 — refinamentos consolidados (Kiê 2026-06-21)

- **C6 NÃO avalia função estrutural** — isso já foi filtrado em C2 (não-estrutural) e C3 (não-moldável). C6 trata só de restrição geográfica/escalabilidade do MATERIAL.
- **Glossário:** *taipa* (rammed earth) = terra úmida socada/compactada em fôrmas, formando paredes monolíticas portantes — é material ESTRUTURAL; *adobe* = tijolo de terra crua; *cob* = mistura de terra+palha modelada à mão; *bahareque* = estrutura de bambu/madeira preenchida com terra (pau-a-pique).
- **Fibra natural** (sisal, juta, cânhamo/hemp, kenaf, linho, agave, coco): NÃO há regra automática — **parar e perguntar caso a caso**. Princípio emergente já aplicado: *fibra natural como REFORÇO incidental num material global (concreto) = Aceito; fibra natural REGIONAL como material-foco do estudo = Rejeitado.*
- **⭐ Material de terra** (rammed earth/taipa, adobe, cob, earthen, terra estabilizada/álcali-ativada) = **ACEITO** (REGRA REVISADA Kiê 2026-06-21: terra/solo é material UNIVERSAL e escalável, disponível em toda parte; a restrição da taipa/adobe é de TÉCNICA/mão-de-obra, NÃO de disponibilidade do material). Palha (straw bale) idem = resíduo universal. **Revertidos para Aceito em 2026-06-21:** 2581, 3016, 3120, 3159, 3498, 3896. ⚠️ EXCEÇÃO: **bahareque** (2805) = estrutura de BAMBU preenchida com terra → Rejeitado pelo BAMBU (bambu ≠ terra; é geograficamente restrito).
- **Cut-stone** (pedra de cantaria) = **Rejeitado** (row 4938 De Toldi); **pedra natural estrutural** como foco = Rejeitado (4707).
- **Resíduo agrícola/vegetal como SCM/agregado em concreto:** UNIVERSAL = Aceito (bagaço de cana, casca de arroz, aguapé/water hyacinth invasor, lignina kraft, palha de cereais, plantas invasoras); REGIONAL CONCENTRADO = Rejeitado (cinza de açaí amazônico, row 4720). O divisor é a disponibilidade global do resíduo.
- **Cortiça** como material relevante do estudo = **Rejeitado** (produção concentrada).
- **Materiais costeiros naturais** (coir/juta/concha de ostra para living shorelines) fora do escopo de concreto urbano = **Rejeitado** + rastreio `outra`.
- **Decisões registradas:** 3348 hemp-reforço=Aceito; 2790/3254 fibras regionais foco=Rejeitado; 3284 adobe-vs-concreto=Aceito (metade concreto armado).
- **Lotes de 200**; ao fim do lote: salvar + atualizar status dos rejeitados + reportar.

## Regra C5 — OPÇÃO A (vigente 2026-06-15, SUPERA todas as anteriores)

**ACEITO** = qualquer artigo que conduza LCA *ou* mencione GWP/CO₂/GHG com *qualquer* resultado — mesmo % relativo, mesmo valor citado de outro estudo, mesmo em figura não extraível por texto.

**REJEITADO** = PDF inteiro (texto + todas as páginas renderizadas) sem **nenhuma** menção a CO₂/GWP/GHG/LCA/climate change relacionada ao material. Exceção: CO₂ puramente analítico-químico (picos FTIR de carbonatos) sem ACV ou impacto ambiental.

**OBRIGATÓRIO antes de qualquer REJEITADO:** ler 100% das páginas + renderizar figuras visualmente (pdf2image).

**PAT regex (pdftotext -layout):**
`lca|life.cycle.assess|carbon.footprint|embodied.carbon|gwp|global.warming.potential|co2.eq|co2eq|kgco2|greenhouse.gas|ghg|carbon.emission|climate.change|co2|embodied.emission|carbon.intensi|low.carbon`

**Carimbo C5:** `[C5 Aceito 2026-06-15: <evidência>]` ou `[C5 Rejeitado 2026-06-15: <motivo>]`

**Pending list:** `c5_pending_correto.json` em outputs — 1.100 rows gerados com filtro correto (`P:Aceito in C4`). Após Lote 6 restam 1.050. Ao retomar, pular row 3002 (aguarda PDF de capítulo de livro).

<!-- USER:END -->
