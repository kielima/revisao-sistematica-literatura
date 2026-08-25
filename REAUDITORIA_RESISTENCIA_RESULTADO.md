# Reauditoria dos rejeitados por resistencia — resultado

**Concluida em 2026-08-25. 69 artigos, zero reaberturas.**

## Porque se fez

Os lotes 1 a 12 da Etapa 2 correram com um padrao de busca incompleto. Quatro
formas legitimas de declarar resistencia escapavam-lhe:

1. a classe chinesa de um so numero — `C45`, `C30`;
2. a unidade escrita por extenso — `megapascal`;
3. a classe sem prefixo — `25/30`;
4. a classe com espacos — `C 25/30`.

Qualquer uma podia ter feito rejeitar um artigo que declara resistencia. Como a
rejeicao num criterio fecha o artigo, o erro seria silencioso e definitivo.

## O que se fez

Os 69 artigos rejeitados por `E2_resistencia` nesses lotes foram todos
descarregados e passados pelo padrao corrigido, em cinco partes. A passagem
**nao** retriou os artigos: nao releu o corpo, nao julgou o CO2, e nao reverteu
rejeicoes por valor baixo — essas continuam certas, e sao os artigos em que
nenhuma mistura chega aos 20 MPa.

A meio da passagem juntou-se um segundo teste, o do texto ilegivel, descrito
mais abaixo.

## Resultado

| | |
|---|---|
| Artigos reauditados | **69** |
| `REABRIR` | **0** |
| `MANTEM` | 62 |
| `MANTEM_VALOR_BAIXO` | 7 |
| Ficheiros ilegiveis | 0 |
| Sem acesso | 0 |

**As quatro formas em falta no padrao original nao custaram nenhum artigo a
esta revisao.** A mais promissora — a classe chinesa de um numero — nao
apareceu genuinamente uma unica vez.

## Todos os acertos das formas novas foram falsos positivos

Vale a pena catalogar as familias, porque voltarao a aparecer:

- **Datas dentro de referencias.** De longe a maior fonte. O formato da
  Elsevier (`2022/03/01/2022`) deu 59 acertos num so artigo. Tambem datas de
  acesso (`25/04/2014`), de cabecalho editorial de submissao («Recebido em
  15/03/14», que esta no rodape da p.1 e nao na bibliografia), e datas dentro
  de URLs de jornais e de diarios oficiais.
- **Modulos da norma EN 15978** — `C1` a `C4`, as fases de fim de vida. Sao
  nomenclatura de metodo de ACV a fazer-se passar por classe de material.
- **Normas ASTM** — `C618` da cinza volante, `C695`.
- **Rotulos de cenario de metodo** — `LD 56/33/11`, de um esquema de alocacao.
- **Codigos de financiamento** — `AAC nº 03/C05-i02/2022`.
- **A razao molar `44/12`** do carbono biogenico da madeira.
- **`C02`** — «CO2» escrito com zero em vez de o. Acerta em qualquer padrao de
  classe, e qualquer artigo com essa gralha o produz.
- **Pares de valores de tabela** — `10 / 65` de uma coluna de densidade e custo.
- **Classes de outro material** — um `C18` que e classe de flexao de madeira
  pela EN 338, impressa so para dar a densidade de uma viga.

Duas notas de metodo que daqui saem:

- **O `\s` do padrao casa a mudanca de linha.** `50 °C` no fim de uma linha e
  `30 bar` no inicio da seguinte produziram um `C 30` fantasma.
- **`\bC\s?\d{2}\b` exige dois digitos**, pelo que os modulos `C1`–`C4` so
  acertam em padroes mais largos.

## O achado colateral, que era maior do que a propria reauditoria

Na parte 2 descobriu-se que a linha 2673 tinha sido rejeitada **sobre texto que
nao se le**. O ficheiro extrai inteiramente como cifra: 52.116 caracteres de
controlo em 71.896, ou seja 72,5% de ruido, e zero palavras reconheciveis em
quinze paginas. O «zero ocorrencias de MPa» registado **nao media o artigo,
media o ruido** — teria dado zero fosse qual fosse o conteudo do PDF.

As quinze paginas foram renderizadas e estao perfeitamente legiveis: o defeito
e da extracao, nao do documento. A rejeicao mantem-se, mas passou a assentar em
prova visual: a unica tabela que descreve as estruturas da so dimensoes, e o
texto diz que vieram de pratica corrente, o que «eliminated the need to perform
any structural calculations».

Isto so ameaca **rejeicoes** — um artigo aceite encontrou valores, logo o texto
lia-se. Mas ha **217 linhas** rejeitadas com uma nota que invoca ausencia, e
qualquer uma podia estar no mesmo caso. Dai a varredura de texto ilegivel, que
corre em separado.

O teste passou a correr tambem dentro da reauditoria, nos 27 artigos das partes
4 e 5: nenhum outro caso.

## Ficheiros

- `lotes_etapa2/REAUDITORIA_RESISTENCIA.csv` — a lista de trabalho, 69 linhas.
- `lotes_etapa2/PROMPT_REAUDITORIA.md` — o metodo.
- `lotes_etapa2/REAUD_0[1-5]_RESULTADO.csv` — o veredito linha a linha.
