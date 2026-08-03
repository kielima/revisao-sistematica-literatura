---
name: rsl-c5-criterio
description: "Critério C5 da RSL: regra FINAL (Opção A, 2026-06-15) — ACEITO = qualquer menção a LCA/CO₂/GHG/GWP com qualquer resultado; REJEITADO = zero menção no PDF inteiro"
metadata:
  node_type: memory
  type: feedback
  originSessionId: c5-triagem
---

Critério **C5 (não menciona emissões de GEE)** da RSL — regra FINAL vigente desde 2026-06-15 (Opção A).

**Texto literal da aba Critérios:**
> "Não menciona análise de ciclo de vida (ACV), emissão de CO2 ou gases do efeito estufa"

**⭐⭐⭐ OPÇÃO A — REGRA FINAL (Kiê 2026-06-15, SUPERA TODAS AS ANTERIORES):**
- **ACEITO** = qualquer artigo que conduza LCA **ou** mencione GWP/CO₂/GHG com **qualquer resultado** — mesmo % relativo, mesmo valor citado de outro estudo, mesmo resultado apenas em figura não extraível por texto.
- **REJEITADO** apenas se o PDF inteiro (texto + todas as páginas renderizadas visualmente) não tiver **nenhuma** menção a CO₂/GWP/GHG/LCA/climate change relacionada ao material estudado.
- **Exceção:** CO₂ puramente analítico-químico (ex.: picos FTIR de carbonatos sem avaliação ambiental) sem nenhuma menção a LCA ou impacto ambiental = Rejeitado.
- **OBRIGATÓRIO antes de qualquer REJEITADO:** ler 100% das páginas + renderizar figuras/gráficos visualmente.

**Regra anterior (DESCARTADA — vigeu 06-14 a 06-15):** ACEITO exigia valor numérico de CO₂/GEE no corpo. Menção qualitativa = Rejeitado. ← NÃO USAR.

**PAT regex (pdftotext scan):**
`lca|life.cycle.assess|carbon.footprint|embodied.carbon|gwp|global.warming.potential|co2.eq|co2eq|kgco2|greenhouse.gas|ghg|carbon.emission|climate.change|co2|embodied.emission|carbon.intensi|low.carbon`

**Busca robusta obrigatória:** pdftotext pode concatenar palavras (ex.: "greenhousegases"). Usar `re.sub(r'\s+','',texto)` para achatar e buscar sem espaços antes de rejeitar.

**Caso especial:** carbonatação/captura de CO₂ (Journal of CO2 Utilization etc.) = C5 Aceito pela Opção A — CO₂ é tema central. Para rastreio futuro, marcar `carbonatacao_captura` na coluna `rastreio_potencial_futuro` (col AG = col 33).

**Casos registrados:**
- Rejeitados confirmados: 2697, 2857, 2858, 2866, 2870, 2878, 3119 (LCA focada em ecotoxicidade, zero CO₂/GWP)
- Único problema não classificado: 3002 (só capa/front matter de livro Woodhead, 3 págs) — aguarda PDF correto da Kiê

**Estado:** C5 foi CONCLUÍDO em 2026-06-21 (P:Aceito=1.505 / P:Rejeitado=43) — ver [[rsl-estado-triagem]]. Esta regra fica registrada para auditoria/retomada.

Ver [[rsl-validacao-pdf-rejeitados]], [[rsl-pdf-ilegivel]], [[rsl-criterios-verbatim]], [[rsl-estado-triagem]].
