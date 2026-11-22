---
titulo: FLUXOGRAMA PRISMA 2020 DOC
descricao: Fluxograma PRISMA 2020 da RSL no desenho de 4 etapas (E1 metadados, E2 texto completo, E3 restrição geográfica do material, E4 qualidade) — cada número com o filtro que o produz, contado por script a partir de articles_final.xlsx
tags: [academico-e-pesquisa, revisao-sistematica, PRISMA]
status: revisado
ultima_atualizacao: 2026-11-22
---

# Fluxograma PRISMA 2020 — desenho de 4 etapas

**Referência:** Page et al. (2021), PRISMA 2020. **Banco:** `articles_final.xlsx`, aba `Articles` (5.093 linhas).
**Script:** `00_REFERENCIAS/PRISMA/contar_funil_prisma.py` → `FUNIL_PRISMA.csv` (caixa, n, filtro) e `EXCLUSOES_POR_CRITERIO.svg` (barras por critério, tarefa #0594).
**Página pública:** `kielima.com/metanalise/prisma` (repositório `kielima-site`, `public/assets/metanalise-prisma.js`, fotografia de 10/11/2026 — os mesmos 14 números desta versão; actualizar à mão quando o funil mudar).
**Tarefa:** #1336 (refazer o fluxograma para o desenho de 4 etapas). Versão de 2026-11-22 (agente RSL, F56).

> **Esta versão substitui por inteiro a documentação do desenho antigo** (cascata C1–C8, 173 textos completos → 75 elegíveis → 69 na síntese, auditoria de 22–24/05/2026, decisão HABERT, `FLUXOGRAMA_PRISMA_2020.html`). Esse texto fica no histórico do git (`git show fb2c7f4:00_REFERENCIAS/PRISMA/FLUXOGRAMA_PRISMA_2020_DOC.md`) e não vale mais: a triagem foi reestruturada em 4 etapas a 2026-08-24 (`PROMPT_RETOMADA_2026-08-24.md`) e o funil é hoje outro.

---

## 1. O desenho e a regra de contagem

| Etapa | O que decide | Campos do banco | Unidade |
|---|---|---|---|
| Identificação | registos das 7 bases; duplicados removidos **antes** da triagem (não é critério de exclusão) | `source`, `status_triagem = Duplicado` | registo (linha) |
| **E1 — triagem por metadados** (sem abrir o PDF) | ano ≥ 2006 (ISO 14040/44); tipo de documento; material moldável; aplicação em construção | `E1_ano`, `E1_tipo_doc`, `E1_moldavel`, `E1_construcao` | registo |
| **E2 — texto completo** (leitura integral, texto e figuras) | dado extraível **no próprio artigo**: fck ≥ 20 MPa e CO₂ absoluto, pareáveis à mesma mistura/sistema | `E2_resistencia`, `E2_co2` | relatório |
| **E3 — restrição geográfica do material** | material enquadrado pelo estudo como categoria global vs. fonte local sem escala/comércio (`CRITERIOS_E_NUANCES_RSL.md`, Etapa 3) | `E3_regional` | artigo |
| **E4 — qualidade** (QA–QG, 0–7) | estrato do **resultado principal** vs. **sensibilidade**; não exclui do corpus | `E4_qualidade_total`, `E4_estrato` | estudo |

**Cada registo é contado no primeiro critério que o exclui** — é isso que define as caixas de exclusão. Em E1 a ordem é ano → tipo de documento → moldável → construção; em E2, resistência → CO₂. As caixas saem por **contagem simples dos campos**, sem contas à mão (`contar_funil_prisma.py`). As 5.093 linhas são a unidade da coluna da esquerda; os estudos secundários das revisões (coluna da direita) vivem na aba `estudos_secundarios`.

## 2. Números (contados em 2026-11-22; iguais à fotografia de 10/11 do site)

### 2.1 Coluna da esquerda — identificação via bases de dados

| Fase | Caixa | n | Filtro (em `articles_final.xlsx`) |
|---|---|---:|---|
| Identificação | Registos identificados nas bases | **5.093** | todas as linhas. Web of Science 1.917 · Scopus 1.427 · Engineering Village 763 · MDPI 475 · Science Direct 411 · BDTD 72 · SciELO 28 |
| Identificação | Duplicados removidos antes da triagem | 2.630 | `status_triagem = 'Duplicado'` |
| Triagem (E1) | Registos triados por metadados | **2.463** | `status_triagem <> 'Duplicado'` |
| Triagem (E1) | Excluídos na Etapa 1 | 272 | primeiro critério E1 `<> 'Aceito'`: construção 190 · material não moldável 72 · tipo de documento 9 · ano 1 (inclui a linha 3002, sem decisão — §5) |
| Elegibilidade (E2) | Textos completos procurados | **2.191** | os quatro critérios E1 `= 'Aceito'` |
| Elegibilidade (E2) | Texto completo não obtido | 6 | E1 completo e `E2_resistencia` vazia — `status_triagem = 'Sem acesso'` (2682, 2852, 2875, 2880, 4049, 5058) |
| Elegibilidade (E2) | Textos completos avaliados | **2.185** | E1 completo e `E2_resistencia` preenchida |
| Elegibilidade (E2) | **Excluídos na Etapa 2 — falta de dado extraível** | 1.643 | `E2_resistencia <> 'Aceito'` **1.303** (sem fck próprio pareável a um CO₂ próprio, ou fck < 20 MPa) · com fck mas `E2_co2 <> 'Aceito'` **340** (sem CO₂ absoluto do betão). Categoria própria: sustenta a discussão do viés de relato (#1331) |
| Elegibilidade (E3) | Artigos aceites na Etapa 2 | **542** | `E2_resistencia = 'Aceito'` e `E2_co2 = 'Aceito'` |
| Elegibilidade (E3) | Excluídos na Etapa 3 — material geograficamente restrito | 18 | `E3_regional <> 'Aceito'`: 14 com `E3_regional = 'Rejeitado'` + 4 com a célula vazia e `status_triagem = 'Rejeitado'` (rejeitados pelo mesmo motivo na triagem antiga C6: 2805, 4707, 4720, 4938 — §5) |
| Inclusão (E4) | Artigos que passam a Etapa 3 | **524** | `E3_regional = 'Aceito'` = 466 `Elegível` + 58 `Revisao` |
| Inclusão (E4) | Revisões sem ACV própria — ramo de citação | 58 | `status_triagem = 'Revisao'`: não pontuam; as fontes primárias que citam entram pela coluna da direita |
| Inclusão (E4) | **Artigos incluídos na revisão (corpus)** | **466** | `status_triagem = 'Elegível'` |
| Inclusão (E4) | Estrato de sensibilidade — fora do **resultado principal**, dentro do corpus | 104 | `E4_estrato = 'sensibilidade'` (`E4_qualidade_total` < 4,0 de 7: notas 0 ×1, 1 ×2, 1,5 ×3, 2 ×7, 2,5 ×12, 3 ×40, 3,5 ×39) |
| Inclusão (E4) | **Estudos no resultado principal** | **362** | `E4_estrato = 'principal'` (`E4_qualidade_total` ≥ 4,0) |

### 2.2 Coluna da direita — identificação por outros métodos (busca de citações)

As revisões aceites em E2 pela regra de 2026-09-14 (revisão alinhada ao propósito da metanálise, CO₂ citado de terceiros) não entram na síntese: os estudos que citam são catalogados na aba `estudos_secundarios` (F36, 2026-10-18) e seguem o ramo PRISMA de «outros métodos».

| Caixa | n | Filtro |
|---|---:|---|
| Registos identificados por busca de citações | **108** | aba `estudos_secundarios`: SCOPE et al. 2021 (linha 3671) 73 · NASIR et al. 2024 (3163) 22 · ONSONGO et al. 2025 (3001) 13 |
| Já estavam no banco (contados na coluna da esquerda) | 17 | `estado_extracao = 'ja_no_banco'` (`status_banco`: 11 Duplicado, 4 Rejeitado, 2 Elegível) |
| Relatórios a procurar e avaliar | **91** | `estado_extracao = 'pendente'` 65 + `'sem_doi'` 26 — tarefa #1811 (Could); nenhum avaliado ainda |
| Incluídos por este ramo | 0 | — (até a #1811 e o passo 2 da F36: as 58 `Revisao` como nós do mapa) |

Nota: a ONSONGO (3001) foi depois **rejeitada em E3** (2026-09-28, enquadramento «for the African Region»); os seus 13 secundários continuam catalogados mas o ramo deve ser revisto quando a #1811 for decidida. O desenho antigo tinha aqui CELIK 2015 (hoje linha 3055, `Elegível`, com as duplicatas 2134/2535 marcadas) e HABERT 2012 (rejeitado em 2026-05-23) — ambos já absorvidos pelo fluxo principal.

### 2.3 Aritmética verificada (saída do script)

```
5.093 − 2.630 = 2.463   triados                      ✓
2.463 −   272 = 2.191   textos completos procurados  ✓
2.191 −     6 = 2.185   textos completos avaliados   ✓
2.185 − 1.643 =   542   aceites em E2                ✓
  542 −    18 =   524   passam E3                    ✓
  524 −    58 =   466   corpus (Elegível)            ✓
  466 −   104 =   362   resultado principal          ✓
```

Metanálise alimentada por este corpus (painel `kielima.com/metanalise`, 2026-11-22): **1.498 pares fck × CO₂ de 398 estudos** (`metanalise-export.py`, `FCK_MIN = 20`, F47); 68 dos 466 artigos não têm par convertível e ficam no corpus sem entrar no gráfico.

## 3. As cinco mudanças obrigatórias da #1336 e como ficaram

1. **Caixa de exclusão por qualidade = exclusão do RESULTADO PRINCIPAL, não do corpus.** A caixa «Estrato de sensibilidade» (104) está ligada à caixa do corpus (466), não a uma saída: os 104 continuam descritos no texto e entram na análise de sensibilidade. Hoje o estrato é definido pelo **corte 4,0/7** (`apply_e4_estrato.py`); a regra dos **terços** com empates a subir (#1333, #1337, decisão de 24/08) ainda não foi executada — quando for (#0042 → #1337), o conteúdo da caixa passa a ser «o terço mais fraco» e o número muda, a definição ao lado também. Com 104 de 466 (22 %) o corte actual é mais permissivo do que um terço.
2. **«Reports not retrieved» em caixa própria.** Os 6 `Sem acesso` com E1 completo aparecem em «Texto completo não obtido», separados das exclusões de elegibilidade. ⚠️ `E1_acesso` continua vazio nas 5.093 linhas (furo conhecido): a caixa é derivada de `E2_resistencia` vazia, não de um campo próprio.
3. **Exclusões por falta de dado separadas.** A caixa de E2 (1.643 = 1.303 + 340) é uma categoria própria — artigos que passaram todos os filtros temáticos e caíram só por não declarar fck pareável ou CO₂ absoluto. É o número que a #1331 (viés de relato) cita.
4. **Duplicados antes da triagem.** 2.630 (eram 2.622 a 24/08; +8 depois: 2813, 2824, 2854, 3543, 3580, 4027, 4119, 4569 — §5), contados por `status_triagem`, não como critério.
5. **Uma caixa por etapa e por critério, por contagem dos campos.** Feito pelo script; os campos `etapa_saida`/`criterio_saida` servem de conferência, mas a contagem usa os campos de decisão E1–E4 (ver §5 para os desacordos).

## 4. Figura de exclusões por critério (#0594)

`EXCLUSOES_POR_CRITERIO.svg` (gerado pelo script): barras horizontais com E2 resistência 1.303 · E2 CO₂ 340 · E1 construção 190 · E4 sensibilidade 104* · E1 moldável 72 · E3 regional 18 · E1 tipo de documento 9 · E1 ano 1 (* sai do resultado principal, não do corpus). Duplicados (2.630) e não recuperados (6) ficam fora da figura por não serem critérios de exclusão. Formato por decidir pela Kiê (barras ou só o fluxograma — pergunta de 02/11 na #0594).

## 5. Regularizações pendentes no banco (não mudam as contagens; mudam só `etapa_saida`/`criterio_saida`)

Dados do banco só mudam por PR com o «pode» da Kiê (`COORDENACAO_AGENTES.md` §5). Lista do script em 2026-11-22:

| Linhas | O que está | O que falta |
|---|---|---|
| 2805, 4707, 4720, 4938 | `status_triagem = Rejeitado`, `E2_resistencia = Aceito`, `E3_regional` vazia, `etapa_saida` vazia; rejeitadas por restrição geográfica na cascata antiga (`C6 = P:Rejeitado`) | preencher `E3_regional = Rejeitado`, `etapa_saida = 3`, `criterio_saida = E3_regional` (pergunta na #1705, 10/11, sem resposta) |
| 3002 (Pacheco-Torgal 2013, capítulo de livro, `Sem acesso`) | `E1_moldavel` e `E1_construcao` vazias; contada em «excluídos na E1» porque `<> 'Aceito'` | decidir se é E1 (decisão por metadados) ou «não recuperado» (7 em vez de 6) |
| 2813, 2824, 2854, 3543, 3580, 4027, 4119, 4569 | `Duplicado` marcados depois de 24/08 sem `etapa_saida = 'duplicado'` | preencher `etapa_saida`/`criterio_saida` como nos outros 2.622 |
| 4125 (El Berdai 2024) | `criterio_saida = E3_regional` mas `E2_co2 = Rejeitado` (saiu em E3 a 26/09; o CO₂ foi rejeitado depois, F18) | pelo princípio «primeiro critério que exclui», o script conta-a em E2; `criterio_saida` deveria dizer `E2_co2` ou a decisão E2 ser revista |
| 3101, 3673, 4260, 4402, 4647 | `etapa_saida = 'E1'`, `criterio_saida = 'moldavel'` (formato diferente dos outros) | normalizar para `1` / `E1_moldavel` |
| 506 linhas com `'2'` (texto) e 1 com `'1'` | `etapa_saida` em texto em vez de número | normalizar o tipo (o script não depende disso) |
| 127 linhas `Rejeitado` (99 principal + 28 sensibilidade) e 3 `Duplicado` | `E4_estrato`/`E4_qualidade_total` preenchidos em linhas fora do corpus (os 58 artigos retro-rejeitados pela regra E2 de 21/09 e os pontuados antes de saírem) | ficam como histórico; qualquer recálculo de estratos tem de filtrar `status_triagem = 'Elegível'` (o script já filtra) |

## 6. Como regenerar e onde actualizar

1. `python3 00_REFERENCIAS/PRISMA/contar_funil_prisma.py` na raiz do repositório (precisa de `openpyxl`). Imprime a tabela, a aritmética e as regularizações; reescreve `FUNIL_PRISMA.csv` e `EXCLUSOES_POR_CRITERIO.svg`.
2. Se algum número mudou, actualizar **(a)** a tabela da §2 deste ficheiro e a data, **(b)** o vector `STEPS` e os textos de `public/assets/metanalise-prisma.js` no `kielima-site` (PT/EN/ZH; a data da «fotografia» em `updated`), **(c)** o parágrafo de métodos da dissertação que cita o funil (#1331, #1336 na Fase D do plano do agente RSL).
3. O painel `/metanalise` conta o funil ao vivo a partir do `banco.json` exportado (`metanalise-export-banco.py`); a página `/metanalise/prisma` é uma fotografia manual. Os dois têm de dizer o mesmo.

## 7. Histórico

| Data | Mudança |
|---|---|
| 2026-05-14 → 2026-05-24 | Documentação do fluxograma do desenho antigo (HTML, 173 → 75 → 69), auditoria em duas passagens, decisão HABERT — preservada no git (`fb2c7f4`). |
| 2026-08-24 | Triagem reestruturada em 4 etapas; o fluxograma antigo fica inválido (nota da #1336). |
| 2026-11-10 | Página `kielima.com/metanalise/prisma` com o fluxo de 4 etapas e o filtro ao lado de cada número (#1705, PR 161 do site). |
| 2026-11-22 | Este documento reescrito para o desenho de 4 etapas, com script de contagem, CSV, SVG de exclusões por critério (#0594) e a lista de regularizações pendentes (#1336, F56). |
