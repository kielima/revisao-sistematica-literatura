# Normas de vida útil de projecto usadas no ci_t (F33, 2026-10-17)

Usadas nos passos 3 e 4 da hierarquia da vida útil do ci_t (`lotes_vidautil/`): quando o estudo não
declara nem cita uma vida útil, atribuímos a vida útil de projecto da norma conforme a aplicação.
**A vida útil atribuída é uma premissa nossa** (Kiê, 2026-10-17: «Vou deixar isso explícito na
dissertação de que a durabilidade foi assumida por nós»).

## EN 1990:2002 — Tabela 2.1 «Indicative design working life» (verificada)

| Categoria | Vida útil de projecto indicativa (anos) | Exemplos |
|---|---|---|
| 1 | 10 | Estruturas temporárias |
| 2 | 10 a 25 | Partes estruturais substituíveis (vigas de rolamento, aparelhos de apoio) |
| 3 | 15 a 30 | Estruturas agrícolas e semelhantes |
| 4 | **50** | Estruturas de edifícios e outras estruturas correntes |
| 5 | **100** | Edifícios monumentais, pontes rodoviárias e ferroviárias e outras obras de engenharia civil |

Fonte consultada (gratuita, oficial): Comissão Europeia, Joint Research Centre — H. Gulvanessian,
«EN 1990: Eurocode: Basis of structural design», workshop *Eurocodes: Background and Applications*,
Bruxelas, 18–20 Fev 2008, slides 27–28 (reprodução da tabela).
<https://eurocodes.jrc.ec.europa.eu/sites/default/files/2022-06/EN1990_2_Gulvanessian.pdf>
O slide 27 diz: «a design working life of 50 years for buildings, 100 years for bridges is recommended in EN 1990».
O texto da norma (à venda) não foi consultado; a numeração «Tabela 2.1» é a da EN 1990:2002.

## ABNT NBR 15575-1:2013 — Anexo C, Tabela C.5 (verificada pela reprodução da CBIC)

| Sistema | VUP mínima | Intermediária | Superior |
|---|---|---|---|
| Estrutura | **≥ 50 anos** | ≥ 63 | ≥ 75 |

Fonte consultada (gratuita, oficial): CBIC — *Desempenho de edificações habitacionais: guia orientativo
para atendimento à norma ABNT NBR 15575/2013*, 2.ª ed., 2013, Tabela 49, p. 197 («Fonte: Anexo C,
Tabela C.5, pág 54 da NBR 15575-1»); a Tabela C.6 (Anexo A do guia, p. 236) dá os mesmos ≥ 50 anos para
«Estrutura principal: fundações, elementos estruturais (pilares, vigas, lajes e outros), paredes estruturais».
<https://cbic.org.br/wp-content/uploads/2017/11/Guia_da_Norma_de_Desempenho_2013.pdf>
A norma (à venda) não foi consultada directamente.

## Correspondência aplicação → vida útil atribuída (passo 3)

| `aplicacao` | Vida útil | Norma |
|---|---|---|
| `edificio`, `pre_fabricado_corrente` | 50 | EN 1990 cat. 4; NBR 15575-1 Tab. C.5 (estrutura, mínimo) |
| `ponte`, `infraestrutura` | 100 | EN 1990 cat. 5 |
| `pavimento` | 50 | EN 1990 cat. 4 («outras estruturas correntes») — **por confirmar** |
| `nao_definida` | 50 (passo 4) | EN 1990 cat. 4 |
