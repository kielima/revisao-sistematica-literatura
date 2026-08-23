# Retomada — estado em 2026-08-22, actualizado a 2026-08-23

> **Ler este ficheiro primeiro.** Substitui `PROMPT_RETOMADA_CONFIRMACAO_PDF_METANALISE.md` e
> `PROMPT_RETOMADA_AUDITORIA_COLISOES_PDF.md`, ambos anteriores à conferência e com pontos de
> retoma que já não são válidos.
> A seguir, ler o `CLAUDE.md` (método, armadilhas, convenções) e o `CRITERIOS_E_NUANCES_RSL.md`
> (texto literal dos critérios C1–C8 e refinamentos).

> ## 🔄 ACTUALIZAÇÃO DE 2026-08-23 — leia isto antes das secções 3 e 4
>
> A 23/08 **os registos foram aplicados ao banco**. As secções 3 e 4 abaixo descrevem o
> estado de 22/08, quando quase nada estava aplicado — continuam a valer como contexto,
> mas as tarefas 4.1, 4.2, 4.4 e boa parte da 4.3 **já foram feitas**.
> **O relato completo está em `APLICACAO_REGISTOS_2026-08-23.md`.** Em resumo:
>
> - ✅ 47 DOIs aplicados · 15 metadados corrigidos · 33 hyperlinks alinhados (defeito fechado)
> - ✅ **Três** pares de troca fechados — ZHANG, LI e **PARK (novo, 4609↔4613)**
> - ✅ 5 ficheiros devolvidos a linhas vivas que estavam sem PDF · 22 ficheiros soltos
> - ✅ 5 nomes com diacríticos corrigidos
>
> **🔢 O funil não é 1.397 — é 1.248.** O número publicado contava 12 linhas mortas *e*
> contava `R:` como decisão, contra a regra do projecto. Ver o `CLAUDE.md`, bullet
> «Estado real», para as três definições lado a lado.
>
> **➡️ O que falta é o C2:** das 1.248 linhas do funil, **1.161 têm o C2 só com `R:`**, e
> **nenhuma delas está sem ficheiro PDF**. É a tarefa #7 (secção 4.6), e agora não há
> nada a bloqueá-la.

---

## 1. O que foi feito, e está fechado

**A conferência PDF × banco terminou.** Os **1.422** ficheiros da pasta do Drive foram todos
abertos e conferidos em **título, primeiro autor e DOI** — decisão da Kiê a 2026-08-16, executada
em 99 lotes com um subagente de cada vez e auditoria entre lotes.

| Veredito | Nº |
|---|---:|
| CONFERE | 1.379 |
| PDF_ERRADO | 34 |
| ILEGIVEL | 4 |
| NAO_ENCONTRADO | 4 |
| INDETERMINADO | 1 |

Registo linha a linha em `VERIFICACAO_TITULO_AUTOR_DOI.csv`. Cada lote tem a sua atribuição e o
seu resultado em `lotes_verificacao/`.

**Os 4 `NAO_ENCONTRADO` são problemas de nome, não de obra.** Três são linhas duplicadas cuja
célula `pdf` foi escrita **com diacríticos** (`ŽIBRET`) a apontar para ficheiros guardados sem
acentos (`ZIBRET`); a obra está na pasta e já foi conferida para a linha vizinha. O quarto era o
PASSUELLO. **Nenhuma obra falta ao Drive.**

⚠️ **Armadilha registada:** não corrigir esses nomes por transliteração cega. `ŠVAJLENKA et al.,
2018.pdf` → `SVAJLENKA et al., 2018.pdf` apontaria a linha 4563 para o **artigo errado**, porque
esse nome existe e é outra obra. O alvo certo é `SVAJLENKA, 2018.pdf`, sem o «et al.».

---

## 2. O que foi aplicado ao banco

Até 2026-08-19 **nada** tinha sido aplicado — tudo ficava registado à espera de decisão. A partir
daí, com autorização da Kiê:

**Anulação das decisões tomadas sobre PDFs errados (2026-08-19).** 38 decisões `P:` em 9 linhas.
Backup em `02_ARQUIVOS ANTERORES/articles_final_backup_pre-anulacao-pdferrado_20260819.xlsx`.
Registo em `ANULACAO_PDF_ERRADO_2026-08-19.csv`.

Seguiu-se à letra a convenção da anulação de 2026-08-15 (134 linhas), verificada no banco antes de
agir: retirar o `| P:` deixando o `R:` (e o `M:`, que sobrevive) → limpar `material_C2` → limpar a
célula `pdf` e o hyperlink → `status_triagem` = `Rejeitado` se sobrevive um `R:Rejeitado`, senão
`Inconclusivo` → carimbo em `comments`.

| Linha | P: anuladas | Status |
|---|---:|---|
| 2715 | 5 | Elegível → **Inconclusivo** |
| 3483 | 5 | Inconclusivo → **Rejeitado** |
| 3508 | 5 | Inconclusivo |
| 4591 | 5 | Inconclusivo |
| 4501 | 5 | Rejeitado → Inconclusivo |
| 2790 | 5 | Rejeitado → Inconclusivo |
| 4127 | 3 | Rejeitado |
| 4999 | 3 | Rejeitado → Inconclusivo |
| 2880 | 2 | Rejeitado → Inconclusivo |

Dois movimentos merecem nota. A **2715** estava **Elegível** — já aceite no corpus — com as cinco
decisões tomadas sobre outro artigo. E a **3483** foi ao contrário, para `Rejeitado`: tinha
`C4 = R:Rejeitado | P:Aceito`, ou seja, a leitura do PDF tinha **revertido** uma rejeição por
resumo, e essa reversão foi feita sobre o artigo errado.

**Integração de 5 PDFs novos (2026-08-21 e 22).** A Kiê descarregou-os; foram conferidos por
abertura antes de entrar, renomeados na convenção nova e movidos para a pasta principal:

- linha **2715** → `KUMAR et al., 2024 - j.sdewes.d12.0488.pdf`
- linha **3508** → `YU et al., 2024 - j.jobe.2024.110929.pdf`
- linha **4501** → `MOHAMMED et al., 2023 - ma16052020.pdf`
- linha **4127** → `AGUIAR et al., 2021 - 1980-5160.2021.v16n2.1712.pdf`
- linha **4999** → `AGUIAR, 2021.pdf` *(a tese verdadeira, UERJ, 214f)*

⚠️ **Estas 5 linhas têm ficheiro certo mas as decisões `P:` anuladas — a triagem por PDF tem de
ser REFEITA sobre elas.** O carimbo em `comments` diz isso.

---

## 3. Estado actual do banco (medido, não estimado)

```
Duplicado     2.622
Inconclusivo  1.140
Rejeitado       901
Elegível        370
Sem acesso       60
TOTAL         5.093

1.397 linhas com Aceito em C1–C6 e C8 (cascata cheia)
1.604 linhas com alguma decisão P:
  144 linhas vivas sem ficheiro PDF (84 Inconclusivo + 60 Sem acesso)
```

⚠️ **Ao contar linhas sem PDF:** as 60 `Sem acesso` têm a célula `pdf` **preenchida com uma nota**
(«Sem acesso — Taylor & Francis») ou com o URL do DOI. Exigir que o valor termine em `.pdf` e não
comece por `http`, senão contam-se como tendo ficheiro.

---

## 4. Por onde continuar — por ordem de importância

### 4.1 Os dois pares de troca (rápido, sem descarregar nada)

Dois casos em que **os ficheiros estão trocados entre duas linhas**. Cada metade foi verificada
independentemente e as duas encaixam. Resolve-se por reatribuição.

**ZHANG — linhas 4376 ↔ 4591**
- 4376 quer `10.3390/en13123109` (Tao Zhang, *Energies*, Planalto de Loess) → está em `ZHANG et al., 2020c.pdf`
- 4591 quer `10.3390/su12031054` (Yurong Zhang, *Sustainability*, vigas com fibra de basalto) → está em `ZHANG et al., 2020b.pdf`
- As 5 decisões `P:` que foram anuladas na 4591 **foram tomadas sobre o artigo da 4376**, que não
  tem decisão nenhuma. Podem **migrar** em vez de se perderem. O mesmo vale para o `fonte_no_pdf`
  da metanálise da 4376, que veio do artigo da 4591.
- Passou despercebido porque a Yurong Zhang da 4591 é a **mesma pessoa** que assina o
  `ZHANG, 2017.pdf` — o apelido nunca levantou suspeita.

**LI — linhas 3483 ↔ 4081**
- 3483 quer `10.1016/j.jhazmat.2021.126156` (césio/sulfoaluminato) → está em `LI et al., 2021b.pdf`
- 4081 quer `10.1557/s43577-021-00118-z` (sequestro de carbono) → está em `LI et al., 2021.pdf`
- A 3483 tinha 5 decisões `P:` (anuladas); a 4081 não tem nenhuma.

### 4.2 O PDF que pertence a outra linha

O `SANTOS et al., 2022.pdf`, retirado da linha 2790, **pertence à linha 3028** — mesmo DOI
(`10.1016/j.clcb.2022.100034`), mesmo título — e a 3028 está **sem PDF**. Reapontar.

### 4.3 As 36 pendências por decidir

`PENDENTES_DECISAO_KIE_2026-08-17.csv`. As mais consequentes são as que ainda têm decisões `P:`
sobre ficheiro não verificável:
- **4416** (Elegível, 5 decisões) — `ASDRUBALI, 2025.pdf` é ILEGIVEL. Candidato a OCR.
- **3002** (Inconclusivo, 3 decisões) — `PACHECO-TORGAL et al., 2013.pdf` é INDETERMINADO (quimera).
- **5022** — `ARROYO et al., 2025.pdf`, 93 MB dos quais não se extrai uma letra; 93 MB para um
  capítulo de 9 páginas é candidato sério a conter o **volume inteiro** das actas. Precisa de ser
  aberto localmente. Drive id `1EjCng0AF5o3JxPUNb6WWdscLbmapE8Sc`.

### 4.4 Os 47 DOIs recuperados e os 35 defeitos de metadado

`DOIS_RECUPERADOS_2026-08-18.csv` e `CORRECOES_METADADOS_2026-08-16.csv`. **Nenhum foi aplicado.**
É escrituração: não afecta conclusões, mas o banco fica mais correcto.

Entre os defeitos, um é **causa raiz** e vale a pena corrigir primeiro: o campo `url` da linha
**4999** aponta para o ResearchGate do **artigo derivado**, não para a tese. Foi por aí que o
ficheiro errado entrou **duas vezes**.

### 4.5 Os ficheiros que faltam

`SEM_PDF_WORKLIST_2026-08-21.csv` (144 linhas) e `OA_DISPONIVEL_2026-08-22.csv`.

**Achado importante:** dos 57 DOIs das linhas `Sem acesso`, **46 têm cópia legal em acesso aberto**
— 29 no próprio editor e 16 em repositório institucional. Aquelas linhas não foram marcadas porque
a obra fosse inacessível, mas porque o download automático falhou em Junho.

⚠️ 15 dos 46 são **`submittedVersion`** (preprint). Podem diferir da versão publicada — assinalar
antes de extrair dados de metanálise.

Ainda em falta, sem OA conhecido: **2880** (`10.1002/ep.14503`, Wiley) e **2790** (tese UFBA,
`repositorio.ufba.br/bitstream/ri/34967/1/Tese_Tiago%20Assunc%CC%A7a%CC%83o_Final_pdf.pdf`).

### 4.6 A tarefa #7, replaneada

A confirmação C2 por PDF e a extração de metanálise ficaram paradas em «1.325 pendentes, próxima a
2688». **Não retomar desse ponto sem antes tratar 4.1 a 4.3** — parte das decisões anteriores foi
tomada sobre ficheiros errados, e as 5 linhas reintegradas precisam de triagem nova.

Não há contaminação numérica na metanálise: das 41 linhas afectadas, 20 têm linha própria em
`dados_fck` e **todas as 20 têm `fck_mpa` vazio**. Mas 11 têm `fonte_no_pdf` com texto citado do
PDF errado.

---

## 5. Limitações da ferramenta, verificadas

**Não é possível carregar PDFs para o Drive a partir da sessão.** Foi testado nos dois conectores:

- `mcp__Google_Drive__create_file` aceita `base64Content` — o conteúdo passa pelo contexto do
  modelo. O mais pequeno PDF do lote (669 KB) dá ~223 mil *tokens*; o maior, ~486 mil. Inviável.
- O Drive do **Toolkit** (mcp.ai): `googledrive_upload_file` pede um **`s3key`** (o ficheiro tem de
  já estar no armazenamento deles, e não há ferramenta para lá o pôr); `create_file_from_text` e
  `edit_file` aceitam só texto; `create_file` e `update_file_put` são só metadados. **Nenhuma faz
  upload por URL.**

Há uma assimetria: **ler** do Drive é barato (o conector extrai o texto para um ficheiro em disco e
devolve só o caminho); **escrever** não tem equivalente.

**A via que funciona:** descarregar na sessão e enviar à Kiê pela conversa (`SendUserFile`), que
não passa pelo contexto; ela guarda no Drive. Depois a sessão confere e integra.

**Download automático tem pouco rendimento.** Dos 46 links OA, `curl` obteve **6**. Os 40 restantes:
24 devolveram HTTP 200 mas são **páginas de destino** (os links `doi.org` e `hdl.handle.net` são
assim por natureza — o PDF está atrás de um clique), 12 devolveram **403** por bloqueio anti-bot
(ScienceDirect, Wiley, IOP — o mesmo problema do `como_contornamos_o_akamai.md`), e o resto foram
erros pontuais. Uma segunda passagem a extrair a meta tag `citation_pdf_url` recuperou 3 dos 24.
Detalhe em `DOWNLOAD_OA_TENTATIVA_2026-08-22.csv`.

---

## 6. Como trabalhar (o que a Kiê pediu, e o que funcionou)

- **Perguntas sempre em texto corrido no chat**, nunca em componente de escolha múltipla.
- **Português europeu** nas respostas; dados e carimbos nas planilhas **sem acentos**.
- **Um subagente de cada vez**, com auditoria minha entre lotes.
- **Lotes de 5 para teses**, não de 15. Três agentes morreram a meio de lotes de 15 sem notificar,
  por tentarem carregar teses de 100–300 páginas para o contexto. Com lotes de 5 e regras
  explícitas de leitura (`Read` com `limit` ≤120 linhas só na folha de rosto, `grep` para o resto),
  não voltou a acontecer.
- **Escrever o CSV de resultado linha a linha.** Foi só isso que salvou o trabalho dos agentes que
  morreram (12 de 15, 4 de 15, 1 de 4).
- **Nada se apaga** de `BAIXADOS MANUALMENTE` nem do Drive sem autorização explícita.
- **Conferir antes de integrar**, sempre, mesmo quando o nome do ficheiro parece óbvio.

---

## 7. Sobre acesso a artigos

A Kiê usa Sci-Hub e Sci-Net por conta própria e traz os ficheiros depois. **Não ajudar com isso** —
nem a usar, nem a obter links. A sessão confere e integra o que ela trouxer, como faz com qualquer
outro ficheiro.

Vias legítimas que funcionam e já deram resultado: **Unpaywall** (46 dos 57 têm OA), pedido directo
ao autor, ResearchGate «Request full-text», COMUT, e o proxy CAPES com o host reescrito
(`www-sciencedirect-com.ezNNN.periodicos.capes.gov.br`, com o `NNN` a mudar por sessão).

Nota metodológica que vale a pena lembrar à Kiê quando o assunto voltar: num RSL, um artigo que não
se consegue obter **é um resultado a documentar**, não um problema a resolver a qualquer custo. O
PRISMA prevê-o e o banco já tem a categoria `Sem acesso`.
