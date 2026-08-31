# Relatório de limpeza do CSV mestre da conferência PDF × banco

**Data:** 2026-08-31
**Ficheiro afectado:** `VERIFICACAO_TITULO_AUTOR_DOI.csv`
**Backup pré-limpeza:** `02_ARQUIVOS ANTERORES/VERIFICACAO_TITULO_AUTOR_DOI_backup_pre-limpeza_20260831.csv`

## Porquê este relatório existe

O `VERIFICACAO_TITULO_AUTOR_DOI.csv` é o registo da conferência PDF × banco: cada linha diz "abri este ficheiro, com este nome, nesta data, e confirmei que era X (ou não)". Ao longo de várias sessões (16→31/08), quando um ficheiro errado era corrigido — trocado por outro nome, religado depois de solto, ou substituído por um par trocado — a entrada **antiga** (que descrevia o ficheiro errado) não era removida, só ficava ao lado da entrada nova. Isto significava que o CSV acumulava registos duplicados: um a descrever o erro histórico, outro a descrever o estado actual — e a contagem de `PDF_ERRADO` no total ficava congelada em 35, mesmo depois de a maioria dos casos já estar corrigida.

A Kiê pediu para o banco (CSV) ficar **corrigido por completo, sem entradas duplicadas — substituídas, não acumuladas** — e para o histórico de tudo o que foi encontrado e corrigido ficar preservado à parte, neste relatório.

## O que foi feito

1. Reconciliação linha a linha entre o CSV mestre e o estado actual da coluna `pdf` do `articles_final.xlsx`: para cada uma das 1.999 entradas do CSV, verificou-se se o nome do ficheiro que ela descreve ainda é o nome actualmente ligado a essa(s) linha(s) do banco.
2. **38 entradas obsoletas** identificadas e **removidas** do CSV vivo (documentadas na íntegra abaixo).
3. **12 entradas corrigidas/reconstruídas**, reaproveitando a identidade já verificada nos registos antigos (DOI/título/autor já confirmados por leitura do PDF em auditorias anteriores — não foi preciso reabrir nenhum ficheiro, porque a prova já existia, só estava associada à linha errada do banco).
4. **3 entradas estendidas** para cobrir uma linha `Duplicado` irmã que partilha legitimamente o mesmo PDF (não é erro, é convenção do banco — mas a entrada do CSV não cobria as duas linhas).

## Resultado

| | Antes da limpeza | Depois da limpeza |
|---|---|---|
| Total de entradas no CSV | 1.999 | **1.972** |
| CONFERE | 1.907 (+ os que eu já tinha corrigido nesta sessão) | **1.970** |
| PDF_ERRADO | 35 | **0** |
| NAO_ENCONTRADO | 4 | **0** |
| ILEGÍVEL | 1 | **1** (ARROYO, genuinamente por resolver) |
| INDETERMINADO | 1 | **1** (PACHECO-TORGAL, genuinamente por resolver) |

Confirmado por reconciliação programática: **0 linhas vivas do banco sem entrada correspondente no CSV, 0 linhas com mais de uma entrada válida, 0 entradas obsoletas remanescentes.**

---

## Entradas substituídas (ficheiro errado → ficheiro certo)

Estes 33 casos tinham um ficheiro errado documentado (por colisão de nome, troca de pares, ou obra derivada) que **já foi corrigido no banco** — o nome mudou e a entrada antiga descrevia um ficheiro que já não está ligado a nenhuma linha viva.

| Linha | Ficheiro antigo (errado) | Veredito antigo | Ficheiro novo (certo) | O que aconteceu |
|---|---|---|---|---|
| 4753 | `BACKES, 2023b.pdf` | PDF_ERRADO | `BACKES et al., 2023 - su151511548.pdf` | Colisão de nome; PDF certo descarregado por DOI em 30/08 |
| 4681 | `CHEN et al., 2022.pdf` | PDF_ERRADO | `CHEN et al., 2022 - su14010144.pdf` | Colisão de nome; PDF certo descarregado por DOI em 30/08 |
| 4127 | `DE MENDONCA et al., 2021.pdf` | PDF_ERRADO | `AGUIAR et al., 2021 - 1980-5160.2021.v16n2.1712.pdf` | Ficheiro era doutro artigo (Renewable Energy); certo descarregado 30/08 |
| 3433 | `FARAHZADI et al., 2022.pdf` | PDF_ERRADO | `FARAHZADI et al., 2022 - j.jclepro.2022.135504.pdf` | Colisão de nome; PDF certo descarregado por DOI em 30/08 |
| 3889 | `GOMES et al., 2019.pdf` | PDF_ERRADO | `GOMES et al., 2019 - 1755-1315_323_1_012055.pdf` | Colisão de nome; PDF certo descarregado por DOI em 30/08 |
| 3139 | `GUO et al., 2023.pdf` | PDF_ERRADO | `GUO et al., 2023 - j.conbuildmat.2023.130441.pdf` | Colisão de nome; PDF certo baixado manualmente pela Kie em 31/08 |
| 4459 | `HADIZADEH-BAZAZ et al., 2023.pdf` | PDF_ERRADO | `HADIZADEH-BAZAZ et al., 2023 - jmse11020433.pdf` | **Achado grave 31/08**: correcção de 17/08 nunca tinha sido aplicada ao banco — o artigo irmão (jmse11091656) ficou ligado durante 2 semanas, com decisões E1/E2 tomadas sobre o conteúdo errado (anuladas nesta sessão). Ficheiro certo estava órfão no Drive desde 23/08; renomeado e religado |
| 4460 | `HADIZADEH-BAZAZ et al., 2023b.pdf` | PDF_ERRADO | `HADIZADEH-BAZAZ et al., 2023 - jmse11091656.pdf` | Par do caso acima; PDF certo descarregado por DOI em 30/08 |
| 4705 | `JI et al., 2022.pdf` | PDF_ERRADO | `JI et al., 2022 - su14116907.pdf` | Ficheiro era cópia redundante doutra linha (3747); certo descarregado 30/08 |
| 2715 | `KUMAR et al., 2024b.pdf` | PDF_ERRADO | `KUMAR et al., 2024 - j.sdewes.d12.0488.pdf` | Ficheiro era da linha 4514; o artigo certo estava "obra perdida" até ser descarregado por DOI em 30/08 |
| 3483 | `LI et al., 2021.pdf` | PDF_ERRADO | `LI et al., 2021b.pdf` | **Troca de pares** com a linha 4081 (dois ficheiros "LI 2021" trocados entre si); fechada 23/08 |
| 4081 | `LI et al., 2021b.pdf` | PDF_ERRADO | `LI et al., 2021.pdf` | Par da troca acima |
| 4501 | `MOHAMMED et al., 2023.pdf` | PDF_ERRADO | `MOHAMMED et al., 2023 - ma16052020.pdf` | Ficheiro era da linha 4926 (colisão apelido+ano); certo descarregado 30/08 |
| 4173 | `ONYELOWE et al., 2022.pdf` | PDF_ERRADO | `ONYELOWE et al., 2022 - cej-2022-08-11-03.pdf` | **Achado grave 31/08**: mesma situação da 4459 — correcção de 17/08 nunca aplicada, artigo irmão (cej-08-12-018) ficou ligado 2 semanas com E1/E2 sobre conteúdo errado (anuladas). Artigo certo não existia em nenhum ficheiro do Drive; localizado como OA via Unpaywall/civilejournal.org e integrado |
| 4174 | `ONYELOWE et al., 2022b.pdf` | PDF_ERRADO | `ONYELOWE et al., 2022 - cej-2022-08-12-018.pdf` | Ficheiro era da linha 4200 (auto-citação entre artigos do mesmo grupo); certo descarregado 30/08 |
| 4991 | `OSORTO, 2023.pdf` | PDF_ERRADO | `OSORTO, 2023 - dissertacao-unb-49254.pdf` | Ficheiro era o artigo derivado (MDPI) da tese, não a tese; dissertação encontrada no repositório da UnB e integrada em 31/08 |
| 4609 | `PARK et al., 2020.pdf` | PDF_ERRADO | `PARK et al., 2020b.pdf` | **Troca de pares** com a linha 4613; fechada 23/08 |
| 4613 | `PARK et al., 2020b.pdf` | PDF_ERRADO | `PARK et al., 2020.pdf` | Par da troca acima |
| 3612 | `POLO-MENDOZA, 2023.pdf` | PDF_ERRADO | *(ainda sem substituto — ver secção "PDFs ainda sem ficheiro" abaixo)* | — |
| 4286 | `PUSHKAR et al., 2022.pdf` | PDF_ERRADO | `PUSHKAR et al., 2022 - buildings12020157.pdf` | Ficheiro era da linha 4297 (mesma autora, mesmo ano); certo descarregado 30/08 |
| 4583 | `PUSHKAR, 2019.pdf` | PDF_ERRADO | `PUSHKAR, 2019 - su11185037.pdf` | Ficheiro era da linha 4580 (mesma autora, tema quase igual); certo descarregado 30/08 |
| 3136 | `SAMPAIO et al., 2022.pdf` | PDF_ERRADO | `SAMPAIO et al., 2022 - j.conbuildmat.2022.129332.pdf` | Ficheiro era cópia redundante (linhas 4090/4091/4093); certo descarregado 30/08 |
| 2790 | `SANTOS et al., 2022.pdf` | PDF_ERRADO | `SANTOS, 2022 - ufba.34967.pdf` | Ficheiro era artigo amazónico de fibras (linha 3028, colisão de apelido "Santos"); dissertação certa baixada manualmente pela Kie em 31/08 |
| 4026 | `TEH et al., 2018.pdf` | PDF_ERRADO | `TEH et al., 2018 - s40008-018-0112-4.pdf` | Ficheiro era cópia redundante (linha 4027); certo descarregado 30/08 |
| 4690 | `WANG et al., 2022.pdf` | PDF_ERRADO | `WANG et al., 2022 - su14031448.pdf` | Ficheiro era da linha 4491 (colisão apelido+ano); certo descarregado 30/08 |
| 3508 | `YU et al., 2024.pdf` | PDF_ERRADO | `YU et al., 2024 - j.jobe.2024.110929.pdf` | Certo descarregado pela Kie em 21/08, retriado por PDF em 23/08 |
| 4376 | `ZHANG et al., 2020b.pdf` | PDF_ERRADO | `ZHANG et al., 2020c.pdf` | **Troca de pares** com a linha 4591 (dois ficheiros "ZHANG 2020" trocados); fechada 23/08 |
| 4591 | `ZHANG et al., 2020c.pdf` | PDF_ERRADO | `ZHANG et al., 2020b.pdf` | Par da troca acima |
| 3855 | `KANE, 2025 - 1748-9326-ad99e9.pdf` | PDF_ERRADO | `KANE, 2025 - 1748-9326-ad99e9-osti.pdf` | **Achado 31/08**: capa de metadados correcta, mas o corpo inteiro do documento era outro artigo (erro na fonte). Todas as decisões E1/E2 anuladas; PDF certo obtido via OSTI (repositório do DOE) |
| 4087 | `PASSUELLO, 2019b.pdf` | NAO_ENCONTRADO | `PASSUELLO et al., 2019.pdf` | Renomeação para corrigir nome com diacríticos; mesma obra |
| 4088 | `PASSUELLO, 2019b.pdf` | NAO_ENCONTRADO | `PASSUELLO et al., 2019.pdf` | Idem |
| 4563 | `ŠVAJLENKA et al., 2018.pdf` | NAO_ENCONTRADO | `SVAJLENKA, 2018.pdf` | Renomeação para corrigir nome com diacríticos; ficheiro partilhado legitimamente com a linha 4562 (Duplicado) |
| 4619 | `ŽENÍŠEK et al., 2020.pdf` | NAO_ENCONTRADO | `ZENISEK, 2020.pdf` | Idem, partilhado com a linha 4617 |
| 4635 | `ŽIBRET et al., 2021.pdf` | NAO_ENCONTRADO | `ZIBRET, 2021.pdf` | Idem, partilhado com a linha 4629 |

## Entradas removidas sem substituto ainda (ficheiro solto, PDF certo por obter)

Estes 5 casos tinham um ficheiro errado que foi **solto** (removido da célula `pdf`) e continuam **sem PDF associado** — a entrada antiga descrevia um ficheiro que já não está ligado a nenhuma linha viva, e não há ainda entrada nova porque não há ficheiro novo.

| Linha | Ficheiro antigo (errado) | O que se descobriu | Estado actual |
|---|---|---|---|
| 3692 | `CHEN et al., 2023.pdf` | Colisão de nome, dono do ficheiro errado nunca identificado | `Rejeitado`, sem PDF. Sem cópia em acesso aberto (Unpaywall `is_oa=false`) |
| 3233 | `GETTU, 2024i.pdf` | Colisão de nome | `Duplicado` da linha 3232, que já tem o ficheiro certo — não precisa de PDF próprio |
| 300 | `HAFEZ, 2020.pdf` | Cópia redundante | `Duplicado` da linha 3389, que já tem o ficheiro certo — não precisa de PDF próprio |
| 2880 | `MESHRAM et al., 2024.pdf` | Colisão de nome, dono do ficheiro errado nunca identificado | `Inconclusivo`, sem PDF. Sem cópia em acesso aberto (Unpaywall `is_oa=false`) |
| 678, 1273, 1900, 4131 | `ZHOU, 2024i.pdf` | O ficheiro pertencia a um proceedings de energia que nenhuma linha do banco reclama — erro de atribuição na integração original | 3× `Duplicado` + 1× `Rejeitado`, sem PDF. Artigo certo (Riofrio et al.) é Gold Open Access confirmado, mas o ScienceDirect bloqueia download automático (403) — link: `doi.org/10.1016/j.cscm.2022.e01150` |

`POLO-MENDOZA, 2023.pdf` (linha 3612) segue o mesmo padrão — está listado na tabela anterior por ordem alfabética do ficheiro antigo, mas também não tem substituto ainda. Artigo certo é Gold Open Access, mas igualmente bloqueado por 403 no ScienceDirect — link: `doi.org/10.1016/j.rineng.2023.100984` (cópia alternativa no DOAJ: `doaj.org/article/440793f8c39341cea74feefd4019bccd`).

## Correcção especial: linha 4999 (AGUIAR)

Este caso não aparecia na reconciliação automática porque o nome do ficheiro **não mudou** — o PDF errado foi substituído no mesmo nome (`AGUIAR, 2021.pdf`) em 22/08/2026, quando a Kie descarregou e eu integrei a tese certa (David Barreto de Aguiar, UERJ, 214 páginas) por cima do ficheiro antigo. Como o casamento automático compara por nome de ficheiro, não por conteúdo, a entrada antiga (PDF_ERRADO, 18/08, a descrever o ARTIGO errado que lá estava antes) continuava a "bater" com o nome actual sem realmente descrever o ficheiro actual. Corrigida manualmente para CONFERE, citando a integração de 22/08 e a retriagem por PDF de 23/08.

## Entradas novas reconstruídas (linha correcta que nunca tinha registo)

Estas 11 linhas ficaram, durante a limpeza, com um PDF actual **sem nenhuma entrada no CSV** — normalmente porque o ficheiro tinha sido identificado como pertencendo a esta linha só na *nota* de uma entrada PDF_ERRADO doutra linha (a auditoria já tinha aberto e lido o ficheiro, só estava associado ao número de linha errado). Reconstruídas sem reabrir o PDF, reaproveitando a prova já obtida — o DOI descrito na nota antiga bate exactamente com o `doi` que a própria linha já tinha no banco.

| Linha | Ficheiro | DOI confirmado | Proveniência da prova |
|---|---|---|---|
| 3028 | `SANTOS et al., 2022.pdf` | 10.1016/j.clcb.2022.100034 | Nota da entrada errada da linha 2790 (auditoria de colisão "Santos", 16/08) |
| 3483 | `LI et al., 2021b.pdf` | 10.1016/j.jhazmat.2021.126156 | Nota da entrada errada da linha 4081 (troca de pares LI, 16–23/08) |
| 4081 | `LI et al., 2021.pdf` | 10.1557/s43577-021-00118-z | Nota da entrada errada da linha 3483 |
| 4200 | `ONYELOWE et al., 2022b.pdf` | 10.3389/fbuil.2022.992552 | Nota da entrada errada da linha 4174 (colisão Onyelowe) |
| 4297 | `PUSHKAR et al., 2022.pdf` | 10.3390/buildings12111854 | Nota da entrada errada da linha 4286 (colisão Pushkar) |
| 4376 | `ZHANG et al., 2020c.pdf` | 10.3390/en13123109 | Nota da entrada errada da linha 4591 (troca de pares Zhang, 16–23/08) |
| 4591 | `ZHANG et al., 2020b.pdf` | 10.3390/su12031054 | Nota da entrada errada da linha 4376 |
| 4491 | `WANG et al., 2022.pdf` | 10.3390/ma15113767 | Nota da entrada errada da linha 4690 (colisão Wang) |
| 4580 | `PUSHKAR, 2019.pdf` | 10.3390/su11154083 | Nota da entrada errada da linha 4583 (colisão Pushkar) |
| 4609 | `PARK et al., 2020b.pdf` | 10.3390/su12176951 | Nota da entrada errada da linha 4613 (troca de pares Park, 16–23/08) |
| 4613 | `PARK et al., 2020.pdf` | 10.3390/su12198096 | Nota da entrada errada da linha 4609 |

## Casos genuinamente ainda abertos (não tocados nesta limpeza)

| Linha | Ficheiro | Veredito | Situação |
|---|---|---|---|
| 5022 | `ARROYO et al., 2025.pdf` | ILEGÍVEL | Ficheiro de 93MB (proceedings inteiro da Springer, não só o capítulo); compressão via Ghostscript ficou presa e foi cancelada em 31/08. Linha já é `Rejeitado`, fora do funil activo |
| 3002 | `PACHECO-TORGAL et al., 2013.pdf` | INDETERMINADO | Ficheiro é só a folha de rosto do livro (editores batem com o autor do banco), sem o capítulo nem DOI impresso — falta o PDF do capítulo em si |

## Metodologia de verificação de integridade

Depois de cada alteração, corri uma reconciliação programática que confirma:
1. **0 linhas vivas do banco** (com PDF ligado) **sem entrada correspondente** no CSV.
2. **0 linhas com mais de uma entrada válida** (sem duplicados).
3. **0 entradas no CSV a descrever um ficheiro que já não está ligado à linha que mencionam** (sem lixo obsoleto).

Este relatório, junto com o CSV limpo, é agora a fonte única de verdade: o CSV mostra o estado actual, este documento preserva o histórico completo de como se chegou lá.
