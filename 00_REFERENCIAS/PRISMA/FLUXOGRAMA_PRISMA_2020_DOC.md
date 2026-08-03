---
titulo: FLUXOGRAMA PRISMA 2020 DOC
descricao: Documentação do Fluxograma PRISMA 2020 — atualizada após auditoria de 22/05/2026 + correção de separação bases/externas em 2026-05-24
tags: [academico-e-pesquisa, revisao-sistematica, PRISMA]
status: revisado
ultima_atualizacao: 2026-05-24
---

# Documentação — FLUXOGRAMA_PRISMA_2020.html

**Arquivo:** `FLUXOGRAMA_PRISMA_2020.html`  
**Criado em:** 2026-05-14  
**Última auditoria:** 2026-05-22 (duas passagens) + decisão HABERT 2026-05-23 + HTML atualizado 2026-05-24 + correção da separação bases/externas no card E4 (2026-05-24, segunda revisão)  
**Autora:** Kiê L. Yamamoto — PUC-Campinas  
**Referência:** Page et al. (2021) — PRISMA 2020

---

## 1. Visão geral

Fluxograma PRISMA 2020 em HTML puro (sem dependências externas) para a RSL sobre emissões de CO₂eq em materiais cimentícios estruturais. Reproduz fielmente a estética do template oficial com setas CSS, grid de duas colunas e um conector em L dinâmico (JavaScript) ligando a coluna "outros métodos" à caixa de inclusão.

**Unidade adotada após auditoria:** estudos únicos (não linhas físicas do banco). A expansão de CELIK em 13 misturas M1–M13 é etapa de extração de dados, posterior ao fluxo PRISMA, e aparece como detalhe no banco mas não no fluxograma.

---

## 2. Dados da RSL (valores atuais no diagrama — pós-auditoria 22/05/2026 + decisão HABERT 23/05/2026)

| Etapa | n |
|---|---|
| **Coluna esquerda — bases de dados** | |
| Registros identificados — bases de dados | 5.093 |
| &nbsp;&nbsp;Web of Science | 1.917 |
| &nbsp;&nbsp;Scopus | 1.427 |
| &nbsp;&nbsp;Engineering Village | 763 |
| &nbsp;&nbsp;MDPI | 475 |
| &nbsp;&nbsp;Science Direct | 411 |
| &nbsp;&nbsp;BDTD | 72 |
| &nbsp;&nbsp;SciELO | 28 |
| Registros identificados — repositórios | 0 |
| Duplicatas removidas | 2.551 |
| Registros triados | 2.542 |
| Registros excluídos na triagem (derivado: 2.542 − 173) | 2.369 |
| Publicações recuperadas (= avaliadas para elegibilidade) | **173** |
| Publicações não recuperadas | 0 |
| Excluídas pelos critérios E1–E7 | 99 |
| &nbsp;&nbsp;E1 — anterior a 2006 | 0 |
| &nbsp;&nbsp;E2 — sem dados de CO₂eq | 15 |
| &nbsp;&nbsp;E3 — sem ACV/metodologia LCA | 0 |
| &nbsp;&nbsp;E4 — material não-cimentício | 15 |
| &nbsp;&nbsp;E5 — sem aplicação estrutural | 19 |
| &nbsp;&nbsp;E6 — sem fck ou resistência à compressão | 42 |
| &nbsp;&nbsp;E7 — contexto estritamente regional | 0 |
| &nbsp;&nbsp;REV — revisão sem dados primários | 8 |
| Excluídos por qualidade (checklist < 4,0 pts) | 6 |
| Elegíveis via bases (E1–E7 aprovados) | 74 |
| **Coluna direita — outros métodos** | |
| Identificados via citação (CELIK 2015 via COELHO 2016) | 1 |
| Identificados via comunicação pessoal (HABERT 2012 via Belizário Silva) | 1 |
| Recuperadas | 2 |
| Avaliadas para elegibilidade | 2 |
| Excluídas — UF incompatível (HABERT 2012) | **1** |
| Elegíveis via fontes externas (apenas CELIK) | **1** |
| **Convergência** | |
| **Total de estudos elegíveis** (74 + 1) | **75** |
| Com checklist completo | **75** |
| Aprovados ≥ 4,0 pts (incluídos) | **69** |
| Excluídos por qualidade < 4,0 pts | 6 |
| Pendentes de checklist | 0 |
| **Total na síntese** | **69** |
| &nbsp;&nbsp;Síntese quantitativa (com c<sub>i</sub> calculável) | **69** |
| &nbsp;&nbsp;Síntese qualitativa | **0** |
| Observações na METANÁLISE | 139 |

> **Decisão 2026-05-23:** HABERT et al. (2012) **REJEITADO do PRISMA** — UF incompatível (sistema de ponte; resultados em % relativa; c<sub>i</sub> não calculável). Mantido apenas como referência bibliográfica no texto.

### 2.1 Histórico das duas passagens da auditoria de 22/05/2026

**1ª passagem (manhã):** corrigiu a mistura de unidades entre E3 e E4 (antes E3=175 estudos, E4=186 linhas). Inicialmente hipotetizou que a diferença vinha de 2 duplicatas internas detectadas pós-recuperação (consolidação SANTOS 3→1).

**2ª passagem (tarde):** rastreio formal com `03_ARTIGOS ACEITOS DA RSL/00_BD ARTIGOS ACEITOS.xlsx` (universo completo da busca, 5.089 entradas) e contagem dos PDFs em `03_ARTIGOS ACEITOS DA RSL/` (173 arquivos) refutou a hipótese das 2 duplicatas. Conclusão: o BD-origem registra **173 Accepted**, há 173 PDFs físicos, e a correspondência DOI-por-DOI com o banco atual (excluindo CELIK e HABERT) é **1:1 perfeita**. O número **175** que constava no diagrama veio da §3.1.7 da dissertação v15 e **não tem origem rastreável** nas três fontes de verdade. Valor corrigido: 173.

> ✅ **Resolvido (2026-05-24):** §3.1.6 e §3.1.7 da dissertação corrigidos em `DISSERTAÇÃO_KIÊ_v16_tracked.docx` — 7 tracked changes aplicadas (autor "Claude", 24/05/2026). Números atualizados: 173 recuperadas; 75 elegíveis (74 bases + CELIK); 69 incluídos; 6 excluídos por qualidade; 0 qualitativa.

### 2.2 Aritmética verificada

```
5.093 (identif) − 2.551 (dup) = 2.542 (triados)              ✓
2.542 (triados) − 173 (recup) = 2.369 (excluídos triagem)    ✓
173 (recuperadas) = 173 (avaliadas)  [sem perda intermediária] ✓
173 − 99 (E1-E7) = 74 (elegíveis via bases)                  ✓
74 + 1 (CELIK via FE) = 75 (total elegíveis)                 ✓
[HABERT: identificado via FE, REJEITADO — UF incompatível]
75 − 6 (qualidade) = 69 (síntese quantitativa)               ✓
Síntese qualitativa: 0                                        ✓
```

---

## 3. Arquitetura CSS

### 3.1 Sistema de cores

```css
/* Teal (coluna esquerda — bases de dados) */
#3C7B75  — fundo dos cabeçalhos, setas, bordas principais
#EAF5F3  — fundo dos boxes principais (classe .bt)
#97CECC  — borda dos boxes teal (.bt e .bts)

/* Gray (coluna direita — outros métodos) */
#888     — fundo dos cabeçalhos, setas, bordas
#F2F2F2  — fundo dos boxes principais (classe .bg)
#C4C4C4  — borda dos boxes gray (.bg e .bgs)
```

### 3.2 Classes de boxes

| Classe | Uso |
|---|---|
| `.bt`  | Box principal teal (fundo verde-claro) |
| `.bts` | Box lateral teal (fundo branco, borda teal) |
| `.bg`  | Box principal gray (fundo cinza-claro) |
| `.bgs` | Box lateral gray (fundo branco, borda cinza) |
| `.box-bottom` | Boxes finais de inclusão (fundo verde-claro, borda teal) |

### 3.3 Sistema de setas CSS (sem imagens)

Cada seta é construída com dois `<div>` aninhados:

**Seta vertical:**
```html
<div class="arr-v-inner">
  <div class="v-stem"></div>   <!-- linha de 2 px de largura, flex:1 de altura -->
  <div class="v-head"></div>   <!-- triângulo CSS apontando para baixo -->
</div>
```

**Seta horizontal:**
```html
<div class="arr-h teal">  <!-- ou .gray -->
  <div class="h-stem"></div>   <!-- linha de 2 px de altura, flex:1 de largura -->
  <div class="h-head"></div>   <!-- triângulo CSS apontando para a direita -->
</div>
```

A cor da seta é herdada pela classe `.teal` ou `.gray` no elemento pai:
```css
.teal .v-stem { background: #3C7B75; }
.teal .v-head { border-top: 8px solid #3C7B75; }
/* idem para h-stem e h-head */
```

---

## 4. Estrutura HTML

```
<body>
  .title / .subtitle          ← Título e subtítulo centralizados

  .headers                    ← Dois cabeçalhos coloridos (grid 57%/43%)
    .hdr.hdr-teal             ← "Identificação via bases de dados…"
    .hdr.hdr-gray             ← "Identificação por outros métodos"

  .main-grid                  ← Grid principal (57% | 43%), position:relative
    │
    ├── <div> (coluna esquerda, grid-col:1)
    │     E1: step-row  [box .bt | arr-h | box .bts]
    │     arr-v-row
    │     E2: step-row  [box .bt | arr-h | box .bts]
    │     arr-v-row
    │     E3: step-row  [box .bt | arr-h | box .bts]
    │     arr-v-row
    │     E4: step-row  [box .bt | arr-h | box .bts]
    │
    ├── .right-grid (coluna direita, grid-col:2)
    │     D1: box .bg id="d3-main"  [grid-col:1/-1, row:1]  ← wide
    │     rv-cell (V-arrow)          [grid-col:1, row:2]
    │     D2: box .bg               [grid-col:1, row:3]
    │     arr-h .gray               [grid-col:2, row:3]
    │     box .bgs                  [grid-col:3, row:3]
    │     rv-cell (V-arrow)          [grid-col:1, row:4]
    │     D3: box .bg id="d3-main"  [grid-col:1, row:5]  ← ORIGEM da seta ←
    │     arr-h .gray               [grid-col:2, row:5]
    │     box .bgs                  [grid-col:3, row:5]
    │
    ├── arr-v-row .teal  (grid-col:1)   ← E4 → Novos estudos
    │
    ├── step-row  (grid-col:1)          ← "Novos estudos incluídos" id="novos-box"
    │                                      DESTINO da seta ←
    ├── arr-v-row .teal  (grid-col:1)   ← entre os dois boxes finais
    │
    └── step-row  (grid-col:1)          ← "Total de estudos incluídos"

  .source                     ← Fonte bibliográfica
  .footnotes                  ← Notas a, b, c, ¹, ²
  <script>                    ← Conector em L dinâmico (ver §5)
```

### 4.1 Layout `.step-row`

Cada linha de etapa usa um grid interno `1fr 22px 1fr`:
- **Col 1 (1fr):** box principal (`.bt` ou `.bg`)
- **Col 2 (22 px):** conector horizontal `.arr-h` com a seta →
- **Col 3 (1fr):** box lateral (`.bts` ou `.bgs`)

Para os boxes finais (`#novos-box`, Total), só col 1 é preenchida; cols 2–3 ficam vazias.

### 4.2 Layout `.right-grid`

Grid interno da coluna direita: `1fr 22px 1fr` / `auto 20px auto 20px auto`.  
Cada elemento usa `style="grid-column:X; grid-row:Y"` explicitamente.

---

## 5. Conector em L dinâmico (JavaScript)

O conector liga **D3** (`id="d3-main"`) → **"Novos estudos"** (`id="novos-box"`).

### Por que JavaScript?

D3 está no `right-grid` (row 1 do `main-grid`) e "Novos estudos" está em uma row mais baixa. A distância vertical entre eles depende do conteúdo e não pode ser fixada em CSS sem quebrar o layout.

### Como funciona

```
D3 box (bottom-center)
       │  trecho vertical (v-stem)
       │
       └──────────────────────◀  "Novos estudos" (right-center, fora da borda)
          trecho horizontal (h-stem) + ponteira ◀
```

O script cria três `<div>` absolutamente posicionados dentro de `.main-grid`:

| id | elemento | posição calculada |
|---|---|---|
| `conv-vline` | linha vertical | left = centro de D3; top = base de D3; height = até endY |
| `conv-hline` | linha horizontal | top = centro de "Novos estudos"; left = borda direita da ponteira; width = até centro de D3 |
| `conv-head`  | ponteira ◀ | left = borda direita de "Novos estudos"; top = centro de "Novos estudos" − 5 px |

O script recalcula ao evento `resize` para manter a responsividade.

### Para editar o conector

- **Cor:** alterar a variável `color` no script (`#3C7B75`)
- **Espessura:** alterar a variável `sw` (padrão: `2` px)
- **Reposicionar origem:** alterar o cálculo de `startX` / `startY`
- **Reposicionar destino:** alterar o cálculo de `tipX` / `endY`

---

## 6. Tarefas pendentes / a confirmar

- [x] **Reconhecer HABERT 2012 como segunda fonte externa** (comunicação pessoal) — ✅ aplicado em 22/05/2026 (auditoria 1ª passagem)
- [x] **Corrigir mistura de unidades estudos/linhas no fluxo** — ✅ aplicado em 22/05/2026 (auditoria 1ª passagem); adotada unidade "estudos únicos"
- [x] **Investigar origem do "175"** — ✅ rastreado em 22/05/2026 (auditoria 2ª passagem); confirmado que 173 é o valor correto via correspondência 1:1 com BD-origem e PDFs físicos
- [x] **Decisão HABERT 2012** — ✅ REJEITADO do PRISMA em 2026-05-23: UF incompatível (sistema de ponte; resultados em % relativa); mantido como referência bibliográfica. HTML atualizado em 2026-05-24.
- [x] **Corrigir §3.1.6 e §3.1.7 da dissertação v15** — ✅ corrigido em `DISSERTAÇÃO_KIÊ_v16_tracked.docx` em 2026-05-24 (7 tracked changes; autor "Claude").
- [x] **Corrigir separação bases/externas no card E4** — ✅ aplicado em 2026-05-24 (segunda revisão). Removidas do card E4 (coluna esquerda) as linhas sobre checklist de qualidade (n=6) e a menção a "75 elegíveis (74 via bases + 1 via fontes externas)" — informações que violavam a regra PRISMA 2020 de que a coluna esquerda deve tratar exclusivamente das bases de dados. A nota de rodapé ² (checklist Q1–Q6) foi movida para o card de convergência "Estudos elegíveis (n=75)", onde a aplicação do checklist faz sentido conceitualmente. O card E4 agora exibe apenas os critérios E1–E7 (n=99); o número de elegíveis via bases (74) permanece implícito pela aritmética 173 − 99 = 74, conforme template oficial PRISMA 2020.
- [ ] **Inserir o fluxograma como figura no Cap. 4** — exportar HTML como PNG/PDF de alta resolução e inserir com legenda completa.

---

## 7. Guia de edições comuns

### Atualizar um número

Procure o valor no HTML dentro de `<b>…</b>` junto do rótulo correspondente. Exemplo para atualizar as duplicatas:
```html
<!-- Antes -->
Registros duplicados removidos (n =&nbsp;<b>2.551</b>)
<!-- Depois -->
Registros duplicados removidos (n =&nbsp;<b>2.600</b>)
```

### Adicionar uma base de dados na lista

Dentro do bloco `<span class="sm">` da caixa E1, adicione uma linha `<br>` e o nome:
```html
<span class="sm">
  Web of Science: 1.917<br>
  Scopus: 1.427<br>
  Nova Base: 999        ← adicionar aqui
  ...
</span>
```
Lembre de atualizar o total `Bases de dados (n = 5.093)`.

### Adicionar um external source na coluna direita

1. Atualizar D1 (box `bg`, `grid-column:1/-1, grid-row:1` do `right-grid`) com o novo estudo no `<span class="sm">`
2. Incrementar `Buscas por citações (n = X)` no mesmo box
3. Atualizar D2 e D3 com os novos totais

### Mudar o tamanho dos cabeçalhos

```css
.hdr { font-size: 13.5px; }  /* valor atual */
```

### Mudar cores globais

Substituir `#3C7B75` (teal) ou `#888` (gray) em todo o arquivo.

---

## 8. Notas de rodapé (referência rápida — pós-auditoria 22/05/2026)

| Ref | Conteúdo |
|---|---|
| `a` | Buscas em 15/04/2025; filtro ISO 14040 (≥ 2006) e acesso aberto |
| `b` | Filtro de acesso aberto aplicado na coleta → 0 não recuperadas |
| `c` | **Duas fontes externas identificadas:** (i) CELIK et al. (2015) — DOI: 10.1016/j.cemconcomp.2014.11.003, identificado nas referências de COELHO (2016) — **INCORPORADO** ao banco (13 misturas M1–M13); (ii) HABERT et al. (2012) — DOI: 10.1016/j.jclepro.2012.05.028, indicado por Belizário Silva (comunicação pessoal) — **REJEITADO do PRISMA em 2026-05-23** (UF incompatível: sistema de ponte; resultados em % relativa; c<sub>i</sub> não calculável); mantido como referência bibliográfica. Rastreamento das 16 revisões ACEITAS: 15 RECUSADAS (E1–E7); 1 ACEITA (COELHO → CELIK). |
| `¹` | Valor 2.369 derivado (2.542 − 173); `175` da v15 §3.1.7 era erro de transcrição — corrigido para **173** em `DISSERTAÇÃO_KIÊ_v16_tracked.docx` (2026-05-24). |
| `²` | Checklist Q1–Q6 (0–1 pt, corte ≥ 4,0) aplicado a **75** elegíveis (74 bases + CELIK via FE; HABERT rejeitado antes desta etapa): **69** Incluídos, **6** Excluídos, 0 pendentes. |
| `³` | Auditoria PRISMA aplicada em 2026-05-22 (unidade "estudos únicos") + decisão HABERT 2026-05-23 + HTML/docs atualizados 2026-05-24. |
