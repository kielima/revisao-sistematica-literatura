---
titulo: "PROMPT RETOMADA C7"
descricao: "Prompt de retomada para triagem C7 — ARQUIVADO (C7 REMOVIDO da RSL em 2026-06-22)"
tags: [academico-e-pesquisa, revisao-sistematica]
status: arquivado
ultima_atualizacao: 2026-06-22
---

> ⚠️ **~~C7 REMOVIDO DA RSL (decisão Kiê, 2026-06-22)~~**
> Artigos com foco exclusivo em energia operacional são rejeitados via C2 ou C3, tornando este critério redundante. O funil vai de C6 directo para C8. As 200 células `P:Aceito` do Lote 1 foram removidas do xlsx. Este ficheiro é mantido apenas como referência histórica.

# ~~Prompt de retomada — Triagem C7 (RSL) — Foco em energia operacional~~ [ARQUIVADO]

Cole o texto abaixo numa nova conversa para continuar.

---

Você vai continuar a triagem por critério da minha Revisão Sistemática de Literatura (RSL) sobre concreto/cimento e emissões. **Leia primeiro o `CLAUDE.md` e o `RSL_PROGRESSO.md`** da pasta do projeto. Banco: `articles_final.xlsx` (aba `Articles`). Trabalhe sempre com `openpyxl` (não há leitura direta do xlsx).

## Estado atual (2026-06-21)

**C1–C6 CONCLUÍDOS.** Próximo critério: **C7**.
- **C6 concluído:** 1.488 P:Aceito + 8 P:Rejeitado.
- **Limpeza de cascata (2026-06-21):** corrigidos 246 rows com veredito Rejeitado anterior que tinham status errado (maioria C2-Rejeitado por resumo = telhas/drenagem/isolamento não-estruturais, vazados pela cascata) + removidos 7 P:Aceito vazados em C5/C6. status_triagem agora: Duplicado 2.621 · Rejeitado 928 · Inconclusivo 1.078 · Elegível 398 · Sem acesso 68.
- **Universo C7 LIMPO = 1.476** (ver definição correta abaixo). Começar pelo primeiro pendente na ordem com C7 sem P:.

## Critério C7 — definição literal (aba Critérios)

- **Título:** *"Foco em energia operacional (sem emissões de produção)"*
- **Descrição:** *"LCA de edifícios cujo foco principal são emissões de energia na fase de uso (B6/B7), sem dados de emissões incorporadas na produção do material (A1-A3/cradle-to-gate)."*
- **Exemplo:** *"Artigos de desempenho energético de edifícios (HVAC, thermal performance, U-value) sem embodied carbon ou cradle-to-gate."*
- **Justificativa:** *"Emissões incorporadas na produção do material são a unidade essencial para comparação entre materiais estruturais."*
- **Refinamentos (col 6):**
  - **ACEITO:** contém embodied carbon, embodied energy, cradle-to-gate, A1-A3, manufacturing/production phase, upstream.
  - **REJEITADO:** foco em operational energy, HVAC, thermal performance, heating & cooling, energy performance of buildings — SEM nenhum padrão ACEITO.
  - **BRANCO/A revisar:** ambíguo.

## ⚠️ MÉTODO OBRIGATÓRIO (regra Kiê, inviolável)

- **Ler de fato as 3 primeiras páginas de CADA artigo** (mais se preciso para decidir). Pre-screen por regex é só AUXILIAR — NUNCA substitui a leitura. (O atalho de regex causou o erro do micélio 3275 no C6.)
- Conferir título + 1º autor na 1ª página antes de avaliar.
- **Casos ambíguos / dúvida → PARAR e perguntar à Kiê antes de classificar.**
- A maioria dos artigos do universo são LCA cradle-to-gate de concreto/cimento (têm embodied carbon) → tendem a ACEITO. O C7 elimina os que focam SÓ energia operacional (fase de uso) sem embodied/produção.

## Mapa de colunas (1-based, verificado)

C1=21, C2=22, **material_C2=23 (no meio!)**, C3=24, C4=25, C5=26, C6=27, **C7=28**, C8=29; status_triagem=20, pdf=11, comments=32, rastreio_potencial_futuro=33.
⚠️ NUNCA usar `zip(range(21,29),["C1".."C8"])` — pula material_C2 e desloca tudo. Usar dict explícito: `COL={"C1":21,"C2":22,"C3":24,"C4":25,"C5":26,"C6":27,"C7":28,"C8":29}`.

## Lógica R: / P: e cascata — VEREDITO FINAL (⚠️ ler com atenção)

- **R:** = decisão por título/resumo; **P:** = decisão por PDF completo. `P:` é o histórico de quem foi triado por PDF.
- **VEREDITO FINAL de uma célula de critério:** `P:` SUPERA `R:`. Ou seja, se a célula tem `P:`, vale o `P:`; senão vale o `R:`. Exemplos: `R:Rejeitado | P:Aceito` → veredito **Aceito** (o PDF reverteu o resumo); `R:Rejeitado` (sem P:) → veredito **Rejeitado**; `R:Aceito | P:Rejeitado` → veredito **Rejeitado**.
- **Universo correto do C7** = rows na cascata (status ∈ {Elegível, Inconclusivo}) **E** veredito final de C6 = Aceito **E** **NENHUM critério anterior (C1–C6) com veredito final Rejeitado** (cobre tanto `R:Rejeitado` quanto `P:Rejeitado`!) **E** C7 sem P:. → deve dar **1.476**.
- ⚠️ **NÃO basta checar `P:Rejeitado`** — tem que checar o VEREDITO (inclui `R:Rejeitado` sem P:). Foi esse o erro que deixou ~200 rows rejeitados-por-resumo (C2 telhas/drenagem não-estruturais) vazarem para C5/C6. Use a função `verdict()` abaixo.

```python
def verdict(v):
    s=str(v) if v is not None else ""
    if not s.strip(): return None
    if "P:Rejeitado" in s: return "Rejeitado"
    if "P:Aceito" in s: return "Aceito"
    if "P:A revisar" in s: return "A revisar"
    if "R:Rejeitado" in s: return "Rejeitado"
    if "R:Aceito" in s: return "Aceito"
    if "R:A revisar" in s: return "A revisar"
    return None
# universo C7:
COL={"C1":21,"C2":22,"C3":24,"C4":25,"C5":26,"C6":27,"C7":28,"C8":29}
# para cada row na cascata: verdict(C6)=="Aceito" AND nenhum verdict(C1..C6)=="Rejeitado" AND "P:" not in C7
```
- Formato da célula C7: preservar o `R:` existente e acrescentar `P:Aceito`/`P:Rejeitado` separado por ` | `.
- Carimbo nos comments (col 32): `[C7 Aceito 2026-MM-DD: <evidência embodied/cradle-to-gate>]` ou `[C7 Rejeitado 2026-MM-DD: <foco operacional, sem embodied>]`.

## Regras operacionais (sempre vigentes)

- **Lotes de 200.** Ao FIM de cada lote: (1) salvar; (2) **atualizar `status_triagem`→`Rejeitado`** em todo row com C7 P:Rejeitado; (3) reportar. **Backup antes de escrever** (cp para `02_ARQUIVOS ANTERORES/`).
- **rastreio_potencial_futuro (col 33):** continuar preenchendo para tecnologias de interesse, mesmo em rejeitados.
- **PDF ilegível / cid-encoded:** OCR (pdf2image+tesseract) antes de classificar; nunca rejeitar sem ler o conteúdo real.
- Limpeza de caracteres de controle antes de escrever no xlsx (IllegalCharacterError).

## Ferramentas

- Scripts Python com `openpyxl`.
- `pdftotext -layout` (poppler) para extração de texto.
- `fitz`/`pdf2image` para renderizar páginas de PDFs digitalizados.
- PDFs em: `00_REFERENCIAS\ARTIGOS ACEITOS APÓS REMOÇÃO DAS DUPLICATAS\`

## Antes de começar

1. Confirme o mapa de colunas pelo cabeçalho (linha 1) — atenção ao `material_C2` na col 23.
2. Recompute o universo C7 usando `verdict()` (veredito final, P: supera R:; excluir quem tem veredito Rejeitado em C1–C6, inclusive R:Rejeitado sem P:) — deve dar **1.476** pendentes.
3. Comece pelo primeiro pendente na ordem.
4. Ao fim de cada lote: salvar + atualizar status→Rejeitado dos C7 P:Rejeitado + reportar + parar para confirmação.
