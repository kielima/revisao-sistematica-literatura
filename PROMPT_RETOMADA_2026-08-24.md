---
titulo: Retomada — estado em 2026-08-24
descricao: O estado real da RSL depois da reestruturação em 4 etapas, com a Etapa 1 concluída e a Etapa 2 por arrancar
tags: [academico-e-pesquisa, revisao-sistematica, retomada]
status: revisado
ultima_atualizacao: 2026-08-24
---

# Retomada — estado em 2026-08-24

> **⭐⭐ Ler este ficheiro primeiro numa sessão nova.** Substitui o
> `PROMPT_RETOMADA_2026-08-22.md`, que descreve o desenho antigo da triagem (critérios C1–C8
> aplicados em cascata) e cujo ponto de retoma deixou de existir. O de 22/08 continua a valer
> como **história** do que foi a conferência PDF × banco.
>
> A seguir, ler o `CRITERIOS_E_NUANCES_RSL.md` (os critérios novos, etapa a etapa) e o
> `CLAUDE.md` (método, armadilhas do conector, convenções de escrita no banco).

---

## 1. O que mudou: a triagem foi reorganizada em quatro etapas

Decisão da Kiê a 2026-08-24. Os critérios são os mesmos na substância, mas passam a ser
aplicados por **tipo de prova**, e não todos de uma vez sobre o PDF:

| Etapa | O que é | Critérios |
|---|---|---|
| **1** | Metadados exportados do Parsifal (título e resumo incluídos) | ano · tipo de documento · moldável · construção · acesso ao PDF |
| **2** | Análise **quantitativa** do PDF (desconsiderando título e resumo) | resistência ≥ 20 MPa · CO₂ declarado |
| **3** | Análise **qualitativa** do PDF | regionalização (o antigo C6) |
| **4** | Controlo de qualidade | seis itens, 0 / 0,5 / 1,0 |

**Porquê:** a ordem em que um artigo é excluído decide em que caixa do PRISMA ele é contado,
e o desenho antigo misturava provas de natureza diferente no mesmo passo.

⚠️ **A Etapa 2 é que faz o grosso da exclusão, e isso é por desenho.** A Etapa 1 corta pouco
porque muitos artigos do corpus (bibliometrias, revisões de gestão, estudos de BIM) **não têm
material nenhum** — não se pode dizer que um material inexistente não é moldável. Morrem
depois, por falta de resistência.

⭐ **Estratificação por terços na Etapa 4:** o resultado principal usa os **dois terços de
cima**; o terço mais fraco **não é apagado** — fica guardado para a análise de sensibilidade,
que repete a conta com todos e reporta a diferença.

### Colunas novas do banco (34–44)

`E1_ano`=34 · `E1_tipo_doc`=35 · `E1_moldavel`=36 · `E1_construcao`=37 · `E1_acesso`=38 ·
`E2_resistencia`=39 · `E2_co2`=40 · `E3_regional`=41 · `E4_qualidade`=42 · `etapa_saida`=43 ·
`criterio_saida`=44.

As colunas antigas C1–C8 **ficam intactas** como registo histórico. `etapa_saida` e
`criterio_saida` são o que o PRISMA lê: cada artigo é contado no **primeiro** critério que o
exclui.

---

## 2. ✅ Etapa 1 — CONCLUÍDA

Aplicada às 5.093 linhas, em lotes por subagente, com auditoria de integridade de cascata
entre lotes. **Zero erros de integridade em todo o banco.**

```
sobreviventes da Etapa 1 : 2.206
  com ficheiro PDF       : 1.591     <- universo da Etapa 2
  sem ficheiro           :   615
exclusoes: ano 1 | tipo_doc 9 | moldavel 66 | construcao 189
```

Lista de trabalho da Etapa 2 já escrita: **`lotes_etapa2/UNIVERSO_E2.csv`** (1.591 linhas, com
`linha`, `pdf`, `doi`, `title`, `year`).

---

## 3. 🔴 Etapa 2 — É O QUE FALTA FAZER

### O piloto de 12 artigos já foi lido (2026-08-24)

Resultado em `lotes_etapa2/PILOTO_RESULTADO.csv`. **Só 6 dos 12 passaram os dois critérios** —
taxa de aprovação de 50%. Custo medido: **~15k tokens por artigo**, o que dá ~24M para os
1.591; não cabe numa sessão, tem de ser em lotes com subagente.

**O que o piloto provou, e que muda o plano:**

- ✅ **As tabelas sobrevivem à extracção** em 10 dos 12 ficheiros. A hipótese contrária estava
  errada — não é preciso renderizar página para ler uma tabela.
- ⚠️ **17% têm o valor decisivo apenas em figura.** Estimados **240 a 320 artigos** dos 1.591.
- 🚨 **O pré-filtro por regex ordena a fila, não carimba o veredito.** Zero ocorrências de
  «MPa» manda o artigo para a fila das figuras, **nunca directamente para Rejeitado** — o caso
  RO 2024 tem ensaios ASTM C39 a sério e zero ocorrências. E ter «MPa» também não chega: no
  ZAJAC 2022 a única ocorrência em 131 mil caracteres é a pressão de transporte do CO₂
  supercrítico.

Os detalhes todos, incluindo as armadilhas de extracção medidas, estão no
`CRITERIOS_E_NUANCES_RSL.md`, secção «O que o piloto de 12 artigos mediu».

### ⛔ Duas decisões da Kiê estão a bloquear o arranque

**1. O artigo que ensaiou a resistência mas só publicou o gráfico.** O RO 2024 (linha 3752)
mediu compressão aos 28 dias pela ASTM C39, com 5 provetes por mistura, e não imprimiu um
único valor em MPa. Conta como «declara resistência convertível para MPa»? Três saídas:
rejeitar por não declarar valor; aceitar e ir ler a figura (~300 artigos a mais, mas a
metanálise fica com o dado); ou aceitar no critério e deixar a Etapa 4 penalizar na qualidade.

**2. O CO₂ do edifício inteiro que também vem normalizado por m².** A regra exclui CO₂ por
edifício por não haver como normalizar, mas **três dos seis aceites do piloto caíram nessa
zona**: o ABDALLA (4664) fala de uma casa mas normaliza por m²; o WU 2024 (3212) dá o CO₂ de
um túnel completo e também a intensidade por metro linear; o GALÁN-MARÍN (3276) dá o total por
modelo de edifício **e** por m². Basta existir *algum* valor normalizado para salvar o artigo?

---

## 4. 🛠️ Ferramenta nova: `DRIVE_FILEID_MAP.csv`

**1.900 ficheiros mapeados** `nome → fileId`, cobrindo **os 1.591 nomes da Etapa 2 com
correspondência exacta**, acentuados incluídos. Cobertura provada por dupla travessia
independente. Zero nomes repetidos na pasta do Drive.

⭐ **Usar sempre este mapa em vez de `search_files` por título.** Poupa uma chamada por artigo
e **elimina de raiz a falha das buscas com diacríticos** — `title = 'GALÁN-MARÍN et al.,
2015.pdf'` não encontra nada.

⚠️ **Armadilha nº6 do conector, medida ao construir o mapa:** `pageSize: 100` **não pagina** —
as páginas sobrepõem-se e o avanço colapsa (100 novos, 69, 59, 3). A receita certa é
**`pageSize: 1000`**, que varre a pasta em 2 chamadas e ainda grava o resultado num ficheiro
em vez de o despejar no contexto.

---

## 5. As 615 sobreviventes sem ficheiro

Muito mais do que as 91 conhecidas antes, porque **472 delas tinham sido rejeitadas pelo C2
antigo** e nunca foram descarregadas. Destas, 571 têm DOI.

**Varrimento Unpaywall (`OA_ETAPA1_2026-08-24.csv`): 546 das 571 têm cópia legal em acesso
aberto (95,6%)**, 493 na versão publicada.

🚨 **Mas «acesso aberto» não é «dá para automatizar».** Medido editora a editora em
`DESCARGA_POR_EDITORA_2026-08-24.txt`:

| Alojamento | N | Obtidos |
|---|---:|---|
| MDPI | 209 | **0 de 3** — `403` até na página do artigo |
| ScienceDirect | 48 | **0 de 3** — `403` |
| Wiley · Hindawi · SciELO · Cell | 19 | **0** — `403` |
| Springer · els-cdn · HAL · handles | 48 | 0 de 12 (páginas de aterragem, não o ficheiro) |
| WITpress · Frontiers · Civil Eng. Journal | 7 | **7 de 7** ✅ |

O padrão é limpo: **as editoras comerciais bloqueiam este contentor; as revistas pequenas e os
repositórios universitários entregam o ficheiro.** A automação recupera talvez 30 a 60 dos 546.

⚠️ **Só 404 dos 546 têm ligação directa ao ficheiro**; os outros 142 trazem apenas o DOI,
porque o Unpaywall não devolveu `url_for_pdf`. Uma leitura descuidada do CSV conta-os como se
fossem ligações ao PDF.

**A lista clicável para descarga manual está em `DOWNLOAD_OA_2026-08-24.html`**, separada em
quatro grupos por esforço: A) 117 que abrem directamente · B) 283 que precisam do proxy CAPES
· C) 146 só com DOI · D) 25 sem acesso aberto.

📌 Sci-Hub e Sci-Net: a Kiê trata disso sozinha e traz os ficheiros; a sessão verifica e
integra, não ajuda a obter.

---

## 6. O que continua em aberto, de antes

| O quê | N | Estado |
|---|---|---|
| Linhas `ILEGIVEL` | 4 | 1029, 3951, 4416, 5022 — precisam de novo download |
| Linha `INDETERMINADO` | 1 | 3002 — capítulo de livro, por resolver desde Junho |
| Anuladas à espera do PDF certo | 7 | 2715, 2790, 2880, 3508, 4127, 4501, 4999 |
| Decisões de metadado que precisam da Kiê | 2 | 4951 (Pena Compas vs Corpa) · 4999 (`url` aponta para obra errada) |
| Renomeações que exigem mexer no Drive | 18 | 13 com sufixo de DOI truncado + 5 baptizados com o nome errado |
| **3028** — o C2 | 1 | Rejeita em C2, ou aceita e deixa a regionalização rejeitar? Muda a contagem do PRISMA |
| **3483** — qual regra manda | 1 | Valorização multirota (Aceito) ou imobilização (Rejeitado)? As duas aplicam-se |

---

## 7. Por onde continuar

1. **Obter as duas decisões da secção 3.** Sem elas a redacção do critério da Etapa 2 fica
   indefinida e os lotes teriam de ser refeitos.
2. **Correr a Etapa 2 em lotes por subagente** sobre `lotes_etapa2/UNIVERSO_E2.csv`, usando o
   `DRIVE_FILEID_MAP.csv` para chegar ao ficheiro sem procurar, com auditoria entre lotes e
   verificação por amostragem — o mesmo método que correu bem na Etapa 1 e na conferência.
3. **Tratar os artigos de figura num lote próprio**, com `pdf2image`, e não misturados no
   fluxo normal.
4. **Etapa 3, depois Etapa 4**, e só então a metanálise.

⚠️ **A metanálise tem de ser refeita do zero.** Decisão da Kiê: pode ter sido construída sobre
os PDFs errados que a conferência descobriu, e cada linha tem de ser reconferida.
