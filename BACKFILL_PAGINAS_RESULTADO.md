# Recuperacao de paginas dos valores extraidos — resultado

**Concluida em 2026-08-25. 174 valores, 12 passagens.**

## Porque se fez

Pedido explicito da Kie: «Eu preciso que a pagina esteja sendo rastreada para
conferencia.» A meio da Etapa 2 mediu-se que so 76 de 170 valores extraidos
tinham pagina de origem registada. Passou a ser obrigatorio, e esta serie de
12 lotes recuperou a pagina dos que ja tinham sido extraidos antes da regra
entrar em vigor.

## O que se fez

Para cada valor ja registado, localizar a pagina onde esta impresso no PDF —
**nunca voltar a julgar o criterio**. Se o valor nao aparece, `NAO LOCALIZADO`;
se aparece com outro numero, `VALOR DIVERGENTE`; se nao ha numeracao impressa,
`NAO IMPRESSO` mais a pagina do ficheiro.

## Resultado

| | |
|---|---|
| Valores processados | **174** |
| `NAO LOCALIZADO` | 3 |
| `VALOR DIVERGENTE` | 1 |
| `NAO IMPRESSO` | 1 |
| Localizados com sucesso | 169 |
| Avisos `[!! ]` levantados | **29** |

A passagem virou tambem uma auditoria de dados: os avisos incluem valores
calculados que o artigo nao imprime, tectos de espaco de busca tomados por
resultado, intervalos com pontas de tabelas diferentes, leituras de eixo sem
rotulo, e um valor de tabela atribuido a linha errada.

## Os achados mais graves, para referencia rapida

- **Valores inventados por aritmetica.** Uma divisao pela unidade funcional
  registada como se estivesse impressa (24,3 kg CO2/m2, quando so os 31,9 kg
  o estao). Uma conversao de unidade (2267,32 kPa registados como 2,27 MPa
  sem dizer que era conversao).
- **Alvo de projecto tomado por resultado.** «Designed to attain 65 MPa» e
  meta de dosagem, nao ensaio.
- **Valor de tabela na linha errada.** Um 337 atribuido a classe C180, quando
  pertence a classe vizinha C100 na mesma tabela.
- **Intervalos mal fechados.** Pontas que vem de tabelas diferentes, ou que
  deixam de fora o caso mais baixo/mais alto da propria tabela.
- **Incoerencias do proprio artigo, nao da extracao.** Uma tabela cujo total
  nao bate com o texto corrido da mesma pagina, por 111 unidades — exactamente
  a linha de transporte que falta somar.

## Armadilhas de notacao catalogadas

Vale reter para trabalho futuro: virgula de milhares; potencia escrita por
extenso (`4.88 × 10²`, invisivel a uma busca por «488»); notacao cientifica
com virgula decimal (`7,29E+02`, invisivel a uma busca por «729»); ponto e
virgula decimal misturados no mesmo grafico; unidade escrita por extenso
(«megapascals», sem a sigla MPa aparecer nunca); artigos que so usam
`N/mm²`; tabelas que sao imagem, sem camada de texto.

## Ficheiros

- `lotes_etapa2/BACKFILL_PAGINAS.csv` — a lista de trabalho original.
- `lotes_etapa2/PROMPT_BACKFILL.md` — o metodo.
- `lotes_etapa2/BACKFILL_0[1-9]_RESULTADO.csv`, `BACKFILL_1[0-2]_RESULTADO.csv`
  — o veredito linha a linha.
