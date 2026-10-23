# Registo de edições da dissertação (tracked changes)

Gerido pela skill `dissertacao-tracked-changes`. Uma linha por pedido; estados: `pendente`, `enviado (cartão, data)`, `aplicado (tracked, data)`, `por resolver (motivo)`.

| id | data | origem | secção alvo | texto proposto | estado |
|---|---|---|---|---|---|
| — | 2026-10-18 | teste do canal (sessões locais) | introdução/metodologia (parágrafo livre) | teste de edição com tracked changes no `v20`; **por confirmar** se as revisões estão no ficheiro | aplicado e confirmado (2026-10-23, workflow `ler-revisoes-docx.yml`, run 39678132534): 3 alterações em tracked changes (autor Claude, 18/10) numa frase da Introdução do v20.docx — vírgula removida, oração redundante «, principal ligante do concreto,» removida, «insubstituível» → «dificilmente substituível» — com 3 comentários |

## Perguntas de agosto/2026 ainda abertas no v20.docx (comentários do autor «Claude», 19/08)
Respostas propostas em 2026-10-23; **nenhuma aplicada ao Word** — dependem da Kiê (e, quando aprovadas, de um cartão para a sessão local).

| id | origem | pergunta | resposta proposta | estado |
|---|---|---|---|---|
| E-001 | glossário vs. secção RenovaCalc/EPDs | MRV: «Monitoramento» ou «Mensuração»? | **Monitoramento, Relato e Verificação** — é o termo oficial brasileiro (Lei 15.042/2024 e GT de MRV do SBCE, Ministério da Fazenda). «Mensuração» é a tradução de *Measurement* (UNFCCC). Uniformizar o corpo do texto para «monitoramento»; se a secção citar documentos internacionais, manter «mensuração» só dentro de citação. | pendente (decisão da Kiê) |
| E-002 | correções da banca #1100 | «Simplificar» as strings de busca: (a) apagar o relato das 3 tentativas ou (b) só cortar redundância? | **Recomendação (b)**, com o relato condensado numa frase («testaram-se strings de maior e menor abrangência; a final recuperou N documentos») e as strings intermédias movidas para apêndice. Mantém o rigor do processo iterativo (PRISMA) e atende à banca. | pendente |
| E-003 | correções da banca #1105 | Origem de fck = 29 MPa (CC) e 121 MPa (UHPC) no fim de «Unidade Funcional» | **UHPC 121 MPa: coincide com a mediana do fck das 39 observações UHPC da metanálise (121,5 MPa; `metanalise/dados_metanalise.csv`, família `uhpc`).** **CC 29 MPa: não coincide com nenhuma mediana atual** (opc 35,0; concreto armado 34,5; reciclado 34,1; todos 39,4) — pode vir de uma versão anterior do banco ou de um estudo específico. **Por confirmar** antes de citar; sugestão: citar a mediana da metanálise para ambos e atualizar o valor de CC. | pendente (por confirmar) |
| E-004 | correções da banca #1126 | IPCC/ONU nas referências: expandir a sigla? | **Sim, expandir** — pedido da banca (Renata), a ABNT permite as duas formas e a expansão não custa nada: «INTERGOVERNMENTAL PANEL ON CLIMATE CHANGE (IPCC).» e «ORGANIZAÇÃO DAS NAÇÕES UNIDAS (ONU).» nas 3 entradas. | pendente |
