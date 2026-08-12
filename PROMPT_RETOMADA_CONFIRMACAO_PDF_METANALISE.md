---
titulo: Prompt de Retomada — Confirmação C2–C8 por PDF + Extração de Metanálise
descricao: Prompt para continuar a tarefa #7 (confirmar por PDF os artigos Elegível/Inconclusivo e extrair dados de fck/CO2/durabilidade para meta_analysis_base.xlsx) em uma nova sessão
tags: [academico-e-pesquisa, revisao-sistematica, UHPC, meta-analise]
status: ativo
ultima_atualizacao: 2026-08-14
---

# Prompt de Retomada — Confirmação por PDF + Extração de Metanálise

Cole este prompt em uma nova sessão para continuar exatamente de onde a anterior parou.

---

## PROMPT

Estou continuando a tarefa #7 da minha RSL (Revisão Sistemática de Literatura) no vault `REVISÃO SISTEMÁTICA DE LITERATURA`: **confirmar por PDF (`P:`) os artigos Elegível/Inconclusivo que ainda não têm C2 confirmado, e extrair dados de fck/CO2/durabilidade para `meta_analysis_base.xlsx` quando aplicável.**

**Antes de fazer qualquer coisa, leia nesta ordem:**
1. `CLAUDE.md` — orientação geral do vault.
2. `CRITERIOS_E_NUANCES_RSL.md` — **arquivo principal desta tarefa.** Consolida o texto literal dos critérios C1–C8, todos os refinamentos/decisões acumulados, a lógica `R:` vs `P:`, o mapa de colunas do Excel, e (seção 7) o protocolo completo desta fase: como ler o PDF, quando extrair dado, como verificar DOI, o fallback de `pdftotext` local quando a extração do Google Drive trunca documentos longos, e os erros já cometidos para não repetir.
3. Se precisar de contexto histórico de progresso numérico (contagens por lote), `RSL_PROGRESSO.md` e `PENDENCIAS_AUDITORIA_2026-07-12.md` são as fontes canônicas — mas não são necessários para começar a trabalhar.

**Estado no momento em que esta sessão parou (2026-08-14):**

- Escopo total da tarefa #7: artigos com `status_triagem` ∈ {Elegível, Inconclusivo} e `C1 = "...P:Aceito"` mas ainda sem `P:` em `C2`.
- **Pendentes:** 1.335 linhas.
- **Próxima linha a processar: 2673** (lote seguinte seria 2673, 2674, 2675, 2678, 2679).
- Último lote concluído nesta sessão: linhas 2661–2671 (lote 8).
- `meta_analysis_base.xlsx` (aba `dados_fck`) está com 1.648 linhas de dados (+ 1 de cabeçalho).
- Branch de trabalho: `claude/vault-discussion-hqrgu9`, com PR #2 aberto em `kielima/revisao-sistematica-literatura` sendo monitorado (sem CI configurado no repositório).

**Como recalcular a lista de pendentes** (não confiar cegamente no número acima, ele muda a cada sessão):

```python
import openpyxl
wb = openpyxl.load_workbook('articles_final.xlsx')
ws = wb['Articles']
COL = {'status_triagem':20,'C1':21,'C2':22}
pending = []
for r in range(2, ws.max_row+1):
    status = ws.cell(r, COL['status_triagem']).value
    if status not in ('Elegível','Inconclusivo'):
        continue
    c1 = str(ws.cell(r, COL['C1']).value or '')
    c2 = str(ws.cell(r, COL['C2']).value or '')
    if 'P:Aceito' in c1 and 'P:' not in c2:
        pending.append(r)
print('total pending:', len(pending))
print(pending[:10])
```

**Protocolo por artigo (resumo — detalhes completos em `CRITERIOS_E_NUANCES_RSL.md` seção 7):**
1. Buscar o PDF no Google Drive, ler o corpo completo (mínimo 5 páginas do conteúdo real, nunca só abstract/título).
2. Confirmar título/primeiro autor batem com a linha antes de decidir qualquer critério.
3. Aplicar C2 usando a redação literal + refinamentos do arquivo consolidado. Casos de **material incidental** (material aparece só como pano de fundo, não como objeto de estudo) → **parar e discutir comigo antes de decidir**, não aplicar precedente automaticamente. O padrão "material simétrico comparado" (concreto comparado com traço/GWP próprios junto de outro material estrutural) já está validado e **não** precisa de discussão.
4. Se C2 aceito, confirmar a cascata restante (normalmente C3–C6/C8 já vêm com `P:` de passadas anteriores).
5. Escrever no Excel: célula C2 (e demais críticos se necessário) + comentário datado explicando a decisão + `status_triagem` atualizado.
6. Se aceito e com dado quantificável (mesmo que só GWP relativo ou fck de traço citado com CO2 calculado pelo próprio estudo), extrair para `meta_analysis_base.xlsx`. Revisão de literatura sem dado próprio → não extrai, só anota em `comments` os artigos citados com dado potencial (Regra 2).
7. Processar em lotes de 5, e ao final de cada lote: commitar e fazer push com mensagem descritiva.

**Regras de confirmação com a Kiê (não pular):**
- Caso de material incidental novo (não é o padrão simétrico já validado) → perguntar antes de decidir C2.
- Qualquer outra ambiguidade real → parar e perguntar, não adivinhar.

Leia o `CRITERIOS_E_NUANCES_RSL.md` inteiro, confirme o que entendeu, recalcule a lista de pendentes para confirmar que ainda começa em 2673 (ou me avise se mudou), e comece o próximo lote de 5.
