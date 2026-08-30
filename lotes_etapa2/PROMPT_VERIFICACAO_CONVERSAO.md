# Verificacao das duvidas de CO2 pendentes — aplicar as regras 7/8 da Kie

## O que se pede

Estas linhas ficaram em duvida porque o CO2 (ou, nalguns casos, a resistencia) aparece so em
unidade normalizada, em percentagem, ou com alguma outra complicacao. A Kie decidiu, em
2026-08-25, as regras 1 a 8 do `PROMPT_E2.md` (le a seccao "Decisoes da Kie" la dentro, na
integra, antes de comecares). A tua tarefa e aplicar essas regras a cada linha, com o PDF
outra vez a frente — nao decidir de memoria.

**Nao e retriagem.** Nao voltes a ler o artigo inteiro do zero; volta a pagina/figura onde o
valor problematico esta, confirma o que la esta impresso, e aplica a regra correcta.

## Lista

`/home/user/revisao-sistematica-literatura/lotes_etapa2/DUVIDAS_DE_CRITERIO.csv` — 20 linhas.

## O que fazer, linha a linha

1. Confirma qual regra se aplica (7 — unidade normalizada; 8 — reducao sem base; ou outra das
   1-6, se a nota mostrar que na verdade e outro tipo de duvida).
2. Vai ao PDF (mapa `DRIVE_FILEID_MAP.csv` → `mcp__Toolkit__googledrive_download_file` → curl;
   sem tecto de tamanho, uma chamada de cada vez) e confirma:
   - Ha alguma equivalencia impressa no artigo entre a unidade normalizada e kg CO2 (regra 7,
     primeira via)? Confirma se a base de normalizacao e a mesma do valor que queres converter.
   - Ha, para a MESMA mistura/ponto, tanto o valor normalizado quanto a grandeza que o
     normaliza (ex.: Ci=kg CO2/MPa E o fc dessa mistura especifica) (regra 7, segunda via)?
   - Ha o valor de base (baseline) impresso nalgum lugar do artigo, para o caso da regra 8?
3. Se sim a alguma das vias: ACEITO, com o calculo mostrado na nota e o `[ALERTA ETAPA4: ...]`
   registado.
4. Se nao: REJEITADO, com a razao.

## Casos especiais nesta lista

- **3238 (PYO)**: ficou por falta de acesso ao ficheiro (10,2 MB, bloqueado antes do
  descarregador do Toolkit voltar a funcionar). O descarregador **nao tem tecto de tamanho**
  agora — tenta descarrega-lo normalmente e le a Fig.9 (p.6), onde os valores absolutos de
  resistencia deviam estar.
- **3192 (SHOBEIRI)**: a Fig.4 tem uma curva Ci(fc) — verifica se algum ponto especifico das
  MISTURAS DO ESTUDO (nao da base de treino da RNA) tem fc e Ci emparelhados, o que permitiria
  Ci × fc = GWP (regra 7, segunda via). Se so houver a curva generica sem pontos identificaveis
  das misturas do proprio estudo, Rejeitado.
- **3560 (BELLERI)**: nao se encaixa nas regras 1-8. O CO2 esta impresso com clareza (5915 e
  3130 kg CO2eq) mas o artigo nao diz se e por parede, por sistema ou pelo edificio inteiro de
  5 pisos. Volta a Fig.6 e ao texto a volta, e tenta esclarecer o escopo pelo contexto (ex.:
  ordem de grandeza compativel com uma parede vs. um edificio). Se conseguires decidir o
  escopo com confianca, resolve; se nao, mantem DUVIDA e explica exactamente o que falta.
- **3309 (DADD)**: nao e duvida de criterio, e limitacao tecnica de paginacao (o extractor
  perdeu folios). Confirma se a decisao registada (resistencia/CO2) ja e suficiente apesar
  disso, ou se precisa mesmo de reler.
- **2601, 2667**: duvidas cuja resolucao **nao muda o desfecho final** do artigo (o CO2 ou a
  resistencia ja rejeita por outra via). Resolve-as pela regra na mesma, para o registo ficar
  completo, mas nao sao prioritarias.

## Saida

`/home/user/revisao-sistematica-literatura/lotes_etapa2/VERIFICACAO_CONVERSAO_RESULTADO.csv`
com colunas: `linha,pdf,veredito_resistencia,veredito_co2,valor,unidade,pagina,calculo,alerta,nota`.

`veredito_resistencia` e `veredito_co2`: `Aceito`, `Rejeitado`, ou `MANTEM_DUVIDA` (só quando
genuinamente não dá para decidir com o que está impresso).

## Regras que nao podes quebrar

- Escreves APENAS este CSV. Nunca escrevas em `articles_final.xlsx`. Nunca faças commit.
- Nunca inventes um factor de conversao que nao esteja impresso no artigo.
- `calculo` mostra sempre a conta por extenso, com os dois numeros impressos e a sua origem
  (pagina, tabela ou figura).
