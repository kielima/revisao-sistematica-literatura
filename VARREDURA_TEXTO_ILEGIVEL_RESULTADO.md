# Varredura de texto ilegivel nas rejeicoes por ausencia — resultado

**Concluida em 2026-08-25. 217 linhas, um unico ilegivel.**

## Porque se fez

A parte 2 da reauditoria dos rejeitados por resistencia descobriu que a linha
2673 tinha sido rejeitada sobre texto que nao se le: o ficheiro extrai
inteiramente como cifra (fontes sem `ToUnicode` valido), 52.116 caracteres de
controlo em 71.896 - 72,5% de ruido - e zero palavras reconheciveis em quinze
paginas. O «zero ocorrencias de MPa» registado nao media o artigo, media o
ruido - teria dado zero fosse qual fosse o conteudo.

Isso poe em causa toda uma familia de decisoes: **217 linhas** dos lotes 1-40
foram rejeitadas com uma nota que invoca ausencia («zero ocorrencias»). Cada
uma podia estar no mesmo caso.

## O que se fez

Uma varredura deliberadamente minima: para cada linha, medir se o texto
extraido presta, sem procurar valores nem julgar criterio nenhum. So os
ficheiros que falham o teste sao renderizados e descritos. Isso permitiu
lotes de 30 em vez de 15.

## Resultado

| | |
|---|---|
| Linhas varridas | **217** |
| `TEXTO_ILEGIVEL` | **1** — a linha que motivou a varredura |
| `SUSPEITO` | 0 |
| `TEXTO_OK` | 216 |

**Nenhum caso novo de texto ilegivel apareceu.** A 2673 continua a ser o unico
caso conhecido em todo o corpus da Etapa 2.

## Calibracao do limiar (util para trabalho futuro)

Medido em 217 ficheiros: nos saos o racio de caracteres de controlo nunca
passou de 0,55% (o mais alto, por um marcador de lista mal mapeado repetido
547 vezes). O caso ilegivel tem 72,5%. A separacao e de duas a tres ordens de
grandeza — na pratica nao ha casos de fronteira.

**A contagem de palavras deve ser normalizada pelo tamanho do documento.**
Contagem bruta baixa nao e sinal de nada — um artigo curto tem menos palavras-
sonda so por ser curto. A densidade (palavras-sonda / caracteres totais) e a
grandeza estavel, e ficou sempre entre 1,17% e 2,40% nos ficheiros saos.

**Um artefacto de extracao a nao confundir com corrupcao:** alguns PDFs da
Elsevier saem do `pymupdf` com espaco extra dentro de palavras
(`Ecological\n Engineering`), o que faz uma contagem literal de palavras-sonda
falhar por nao bater o espaco simples. Nao e cifra — confirma-se lendo o
inicio do dump, e recontando com o espacamento colapsado.

## Ficheiros

- `lotes_etapa2/VARREDURA_TEXTO_ILEGIVEL.csv` — a lista de trabalho, 217 linhas.
- `lotes_etapa2/PROMPT_VARREDURA_TEXTO.md` — o metodo, com o limiar calibrado.
- `lotes_etapa2/VARR_0[1-8]_RESULTADO.csv` — o veredito linha a linha.
