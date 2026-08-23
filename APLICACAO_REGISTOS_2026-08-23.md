---
titulo: Aplicação dos registos ao banco — 2026-08-23
descricao: O que foi escrito no articles_final.xlsx a 23/08/2026, com a prova de cada operação e o que ficou por aplicar
tags: [academico-e-pesquisa, revisao-sistematica, auditoria]
status: revisado
ultima_atualizacao: 2026-08-23
---

# Aplicação dos registos ao banco — 2026-08-23

Até esta data, a conferência PDF × banco tinha produzido nove ficheiros de registo com
achados verificados, mas **só um deles tinha sido aplicado** ao `articles_final.xlsx`
(a anulação das decisões tomadas sobre PDF errado, a 19/08). Os restantes estavam a
ser guardados à espera de decisão da Kiê — indevidamente, porque a maioria são
correcções mecânicas que não dependem de nenhuma decisão de triagem.

Esta sessão aplicou tudo o que é mecânico e verificável. **Backup:**
`02_ARQUIVOS ANTERORES/articles_final_backup_pre-aplicacao-registos_20260823.xlsx`.

## O que foi aplicado

| # | Operação | Linhas | Registo |
|---|---|---|---|
| 1 | DOIs recuperados escritos na coluna `doi` | 47 | `APLICACAO_DOIS_2026-08-23.csv` |
| 2 | Metadados corrigidos (`author`, `year`, `journal`, `pages`, `affiliation`) | 15 correcções em 14 linhas | `APLICACAO_METADADOS_2026-08-23.csv` |
| 3 | Pares de troca e reatribuições de PDF | 10 | `REATRIBUICAO_PDF_2026-08-23.csv` |
| 4 | Terceiro par de troca, reatribuições e solturas | 28 | `SOLTURA_E_REATRIBUICAO_2026-08-23.csv` |
| 5 | Hyperlinks realinhados e normalizados | 33 | `HYPERLINKS_REALINHADOS_2026-08-23.csv` |

Cada linha tocada levou um carimbo na coluna `comments` a dizer o que mudou e porquê.

### 1. Os 47 DOIs recuperados

Todas as 47 células `doi` estavam **vazias** — nenhum conflito, nenhuma sobrescrita.
O banco passou de 4.250 para **4.297 linhas com DOI**.

### 2. Metadados

Aplicadas as 15 correcções cujo valor certo estava determinado. Destaque para a
**linha 3973, o único registo quimera do banco**: título e DOI eram do artigo do Hart,
mas `author`, `affiliation` e `pages` tinham vindo do artigo vizinho na mesma revista
(paginação consecutiva, 403–418 e 419–434 — é assim que a exportação do Web of Science
os colou). Confirmado no Crossref: `10.1111/jiec.13139` devolve Hart, D'Amico e Pomponi,
pp. 403–418. Corrigidos os três campos.

**Não aplicadas, de propósito** (três casos, todos por falta de valor certo determinado):
- **4951** — segundo autor «Pena Compas» vs «Pena Corpa»; o Crossref não desempata.
- ~~**5016**~~ — **RESOLVIDO em 2026-08-23, nada a corrigir.** A Kiê levantou a questão
  certa: seria retificação de nome? O campo `author` do banco diz «Schmidt, **Raquel
  Petry Brondani**» — contém os próprios nomes da folha de rosto, logo é a mesma pessoa
  com mais um apelido. E o mecanismo (casamento? retificação? correcção de registo?)
  **não foi verificado e não se deve afirmar** — a versão anterior desta nota afirmava-o
  indevidamente. Seja qual for, a forma do repositório é a actual e é a que fica; repor
  a forma impressa seria o erro.
- **4999** — o `url` aponta para o ResearchGate, que serve a obra errada; o registo certo
  na BDTD/UERJ está por localizar. É a causa raiz de o ficheiro errado ter entrado duas
  vezes nesta linha.

### 3 e 4. Atribuição de PDF — **três pares de troca fechados**

Cada ficheiro foi confirmado **directamente no Drive**, pelo DOI impresso na frente,
antes de ser reapontado. Não se confiou na nota da conferência.

| Par | Antes | Depois |
|---|---|---|
| ZHANG | 4376 tinha `2020b` (que é su12031054); 4591 sem PDF | 4376 ← `2020c` (en13123109) · 4591 ← `2020b` (su12031054) |
| LI | 4081 tinha `2021b` (que é o césio); 3483 sem PDF | 3483 ← `2021b` (jhazmat) · 4081 ← `2021` (s43577) |
| **PARK (novo)** | 4609 tinha `2020` (que é su12198096); 4613 tinha `2020b` (que é su12176951) | 4609 ← `2020b` · 4613 ← `2020` |

O par PARK foi descoberto nesta sessão, ao procurar o verdadeiro dono de cada ficheiro
errado em vez de simplesmente o soltar.

**Ficheiros devolvidos a linhas vivas que estavam sem PDF** (cinco recuperações):

| Ficheiro | Saiu da | Foi para | DOI impresso |
|---|---|---|---|
| `SANTOS et al., 2022.pdf` | 2790 | **3028** | 10.1016/j.clcb.2022.100034 |
| `ONYELOWE et al., 2022b.pdf` | 4174 | **4200** | 10.3389/fbuil.2022.992552 |
| `PUSHKAR et al., 2022.pdf` | 4286 | **4297** | 10.3390/buildings12111854 |
| `PUSHKAR, 2019.pdf` | 4583 | **4580** | 10.3390/su11154083 |
| `WANG et al., 2022.pdf` | 4690 | **4491** | 10.3390/ma15113767 |

**Nomes com diacríticos corrigidos** (5 linhas). A célula tinha sido escrita com os
diacríticos e o ficheiro está guardado sem eles. ⚠️ **Não é uma transliteração cega:**
no caso da 4563, o equivalente ASCII exacto (`SVAJLENKA et al., 2018.pdf`) é **outro
artigo** (su10124394); o desta linha é o `SVAJLENKA, 2018.pdf`, sem «et al.». Confirmado
ficheiro a ficheiro no Drive.

**22 ficheiros soltos** das linhas que os reclamavam sem lhes pertencerem — cópias
redundantes, obras derivadas, ou ficheiros cujo dono não se identificou.

### 5. Hyperlinks — defeito fechado

Os 30 hyperlinks desalinhados estavam em aberto desde 16/08 por se pensar que resolver
exigia ir ao Drive verificar cada nome. Não exigia: **os 28 valores de célula estavam
todos na lista mestra da conferência, todos `CONFERE`, e todos atribuídos exactamente
à linha em questão** — ou seja, o ficheiro existe e é o certo; era o hyperlink que
estava preso ao nome antigo. Em metade dos casos o nome antigo pertence a **outra
linha do banco**, pelo que seguir o link abria o artigo errado.

Mais 5 casos apanhados numa varredura ao banco inteiro (dois com caminho absoluto do
Windows, três sem hyperlink nenhum). **Auditoria final: das 2.042 células com ficheiro,
zero estão desalinhadas.**

## Estado medido depois de tudo aplicado

> ⏱️ **Instantâneo do momento desta passagem, já superado.** Ainda no mesmo dia fez-se a
> **retriagem por PDF de 16 artigos** (ver `RETRIAGEM_PDF_2026-08-23.md`), que moveu estes
> números: o funil passou de 1.248 para **1.259**, o C2 confirmado por PDF de 87 para **98**,
> e o `status_triagem` para Inconclusivo 1.138 / Rejeitado 903. Os valores abaixo ficam como
> registo do que esta passagem produziu; **para o estado actual, ver o `CLAUDE.md`.**

```
status_triagem : Duplicado 2622 | Inconclusivo 1140 | Rejeitado 901 | Elegível 370 | Sem acesso 60   (total 5093)
linhas com DOI : 4297   (eram 4250)
celulas com ficheiro PDF : 2042, todas com hyperlink coerente
linhas vivas sem ficheiro: 91  (+60 Sem acesso = 151)
linhas com alguma decisao P: : 1604
```

### ⚠️ A contagem do funil publicada estava inflacionada por duas vias

O número **1.397** que circulava no `CLAUDE.md` está errado de duas maneiras:

1. **Contava linhas mortas.** A definição usada não filtrava `status_triagem`, pelo que
   incluía 12 linhas `Duplicado`/`Rejeitado`/`Sem acesso`. Restringindo a linhas vivas
   dá **1.385**.
2. **Contava `R:` como decisão.** A regra do projecto diz que *«células com apenas `R:`
   são consideradas NÃO triadas»*. Exigindo `P:Aceito` em C1 e C3–C6, o funil real é
   **1.248**.

| Definição | N |
|---|---|
| Como estava publicado (sem filtrar status, `R:` conta) | 1.397 |
| Só linhas vivas, `R:` conta | 1.385 |
| **Só linhas vivas, C1 e C3–C6 confirmados por PDF** | **1.248** |

O backup de antes das alterações de hoje dá **exactamente 1.385** pela segunda
definição, o que confirma que **nada do que foi aplicado hoje mexeu no funil** — como
tinha de ser, já que só se tocou em linhas sem decisões `P:`.

### O C2 é o que falta

Dentro do funil de 1.248, **só 87 têm o C2 confirmado por PDF**; faltam **1.161**.
*(Depois da retriagem do mesmo dia: 1.259 no funil, 98 com C2 confirmado, os mesmos 1.161 por confirmar.)*
É exactamente o trabalho da tarefa #7, que parou em Agosto. Nenhuma dessas 1.248 linhas
está sem ficheiro PDF — o material para continuar está todo lá.

## O que ficou por aplicar, e porquê

| O quê | N | Porquê |
|---|---|---|
| Renomear ficheiros com sufixo de DOI truncado a 8 caracteres | 13 | Exige **renomear no Drive**, não só escrever no banco. Lista em `CORRECOES_METADADOS_2026-08-16.csv`. |
| Renomear ficheiros baptizados com o nome errado (`XIAOYU`→`SHENG`, `MENDES`→`SAADE`, `LUKAEVI`→`LUKACEVIC`, `WȨGLARZ`→`WĘGLARZ`, `HUU QUOC HUNG NGUYEN AND MAEKAWA`→`NGUYEN e MAEKAWA`) | 5 | O mesmo. O conteúdo está certo em todos — é só o rótulo. |
| Linhas `ILEGIVEL` | 4 | 1029, 3951, 4416, 5022 — o ficheiro não se deixa ler. Precisa de novo download. |
| Linha `INDETERMINADO` | 1 | 3002 — capítulo de livro, por resolver desde Junho. |
| Linhas anuladas à espera do PDF certo | 7 | 2715, 2790, 2880, 3508, 4127, 4501, 4999. |
| Decisões de metadado que precisam da Kiê | 3 | 4951, 5016, 4999 (ver secção 2). |

### Por decidir — pergunta para a Kiê

**As decisões `P:` anuladas podem migrar em vez de se perderem?** Quando uma decisão foi
tomada a ler o ficheiro X, e o ficheiro X pertence afinal à linha Y, a decisão é um facto
sobre o *artigo*, não sobre a linha — logo aplica-se à linha Y.

**Não migrei nenhuma**, e a razão é concreta: ao comparar os dois casos, encontrei uma
incoerência. Na **3483**, o `material_C2` anulado dizia «sequestro de carbono sólido em
concreto» — que descreve o artigo do *ficheiro* (o da 4081), o que confirma que a decisão
saiu mesmo da leitura do PDF. Mas na **4591**, o `material_C2` anulado dizia
«sustentabilidade de vigas de concreto armado» — que é o título da **própria 4591**, não
o do ficheiro que lá estava. Ou seja, nesse caso a decisão pode ter saído do resumo do
banco e não do PDF, e migrá-la para a 4376 carimbaria um erro.

Reler um artigo é barato; contaminar uma decisão não é. Ficam as duas por migrar, à
espera de que a Kiê diga se prefere migrar as que são claramente do PDF, ou reler todas.
