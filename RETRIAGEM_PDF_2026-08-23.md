---
titulo: Retriagem por PDF — 2026-08-23
descricao: Releitura completa dos 16 artigos com ficheiro novo ou decisão anulada, com o resultado de cada critério e o que ficou por decidir
tags: [academico-e-pesquisa, revisao-sistematica, triagem]
status: revisado
ultima_atualizacao: 2026-08-23
---

# Retriagem por PDF — 2026-08-23

## Porquê

Depois de as decisões `P:` tomadas sobre PDF errado terem sido anuladas (19/08) e de os
ficheiros certos terem sido reatribuídos (23/08), ficaram 16 linhas com um PDF confirmado
e sem decisão de triagem — umas porque as decisões foram anuladas, outras porque nunca
tinham sido triadas por PDF.

A Kiê decidiu: **reler todas**, em vez de migrar as decisões anuladas para as linhas a que
os artigos afinal pertenciam. Foi a decisão certa — ver a secção «Porque não se migrou».

Trabalho feito em 4 lotes de 4 por subagente, um de cada vez, com auditoria entre lotes.
Registo por lote em `lotes_retriagem/LOTE_0N_RESULTADO.csv`; o que foi aplicado ao banco
está em `lotes_retriagem/RETRIAGEM_APLICADA.csv`.

## Resultado

**14 dos 16 decididos e aplicados. 11 passaram os seis critérios, 3 foram rejeitados.**

| Linha | Artigo | Resultado |
|---|---|---|
| 2715 | Kumar — quatro casas em Jammu | ✅ C1–C6 |
| 3508 | Yu — 180 EPDs de materiais de construção | ✅ C1–C6 |
| 4081 | Li — carbono sólido da pirólise de metano em cimento | ✅ C1–C6 |
| 4200 | Onyelowe — cinza volante e sílica activa | ✅ C1–C6 |
| 4297 | Pushkar — reforço sísmico | ✅ C1–C6 |
| 4376 | Zhang — edificações rurais no Planalto de Loess | ✅ C1–C6 |
| 4501 | Mohammed — argila calcinada / LC³ | ✅ C1–C6 |
| 4580 | Pushkar — cinza de fundo de fornalha | ✅ C1–C6 |
| 4591 | Zhang — vigas com fibra de basalto | ✅ C1–C6 |
| 4609 | Park — materiais de construção rodoviária | ✅ C1–C6 |
| 4613 | Park — resíduos de construção | ✅ C1–C6 |
| 4127 | Aguiar — blendagem de resíduos perigosos | ❌ **C2** |
| 4491 | Wang — revestimento de geopolímero | ❌ **C2** |
| 4999 | Aguiar — tese sobre coprocessamento | ❌ **C4** |

**Estado depois:** funil **1.259** (era 1.248) · C2 confirmado por PDF **98** (era 87) ·
`status_triagem` Duplicado 2.622 | Inconclusivo 1.138 | Rejeitado 903 | Elegível 370 |
Sem acesso 60.

## Duas regras novas, que saíram destes casos

Ambas incorporadas no `CRITERIOS_E_NUANCES_RSL.md`.

**1. Revestimento vence a família do material (C2).** A lista de materiais aceites nomeia
«geopolímero» sem qualificador, o que parecia aceitar qualquer geopolímero. Não aceita: o
C2 decide pela **aplicação**. A própria lista qualifica «alkali-activated *em contexto
estrutural*», e a regra da argamassa já mostrava o mesmo padrão. Sinais que denunciam um
revestimento: unidade funcional em volume de *coating*, ensaios de dureza e **aderência ao
substrato** em vez de compressão, e zero ocorrências de `compressive`/`flexural`.

**2. C2 ou C4? O discriminador é a fronteira do sistema.** As linhas 4127 e 4999 são do
mesmo autor e do mesmo tema e foram rejeitadas em critérios diferentes — o que parecia
incoerência e não é:
- **Sem material cimentício dentro da fronteira → C2.** A 4127 exclui expressamente os
  fornos de clínquer; não há cimento nenhum no sistema.
- **Com material cimentício dentro, mas sem o elemento final → C4.** A 4999 tem unidade
  funcional «1 tonelada de clínquer produzida»; o clínquer está lá, falta a jusante.

O veredito final é o mesmo, mas **o critério registado muda a contagem do PRISMA por
critério** — por isso não é indiferente qual se escolhe.

## Avisos para a metanálise, carimbados nas linhas

- **4580 é a linha mais rica**: `fck` medido aos 28 dias para 20 misturas com traços
  completos. ⚠️ Mas a unidade funcional está **normalizada à resistência** — o GWP não é um
  kg CO₂/m³ directo; desfazer a normalização antes de comparar.
- **4200 tem o melhor formato de dado** (418,15 ± 49,80 kg CO₂/m³) ⚠️ mas as 330 misturas
  **não são amostras próprias** — vêm de cinco artigos anteriores. Risco de dupla contagem.
  A sondagem por apelido+ano não achou essas fontes no banco, mas **apelido+ano não é
  identidade**; cruzar pelos DOIs da lista de referências antes de extrair.
- **4591 tem `fck` medido e traço completo, mas ZERO CO₂** — os autores usaram energia (MJ)
  por falta de inventário, e dizem-no. ⚠️ E o `fck` é em **cubos** de 150 mm, não cilindros.
- **4613**: o GWP tabelado é o da **fracção perdida**, não o do concreto aplicado. Só o
  quociente por m³ (~424–437) é comparável, e bate com o da 4609 por partilharem a LCI
  coreana.
- **4609**: CO₂ em **duas unidades** — por m³ para o concreto e agregados, por kg para
  cimento, aço e asfalto. Não misturar.
- **4501 é revisão sem dados próprios**: os `fck` e o CO₂ da Tabela 2 são todos de
  terceiros. Não extrair como se fossem do artigo.
- **4376 não serve à metanálise**: nem `fck`, nem traço, nem CO₂ em unidade nenhuma — tudo
  em MJ. Entra no funil pelo C5 (Opção A aceita quem conduz ACV), mas não alimenta dados.

## Porque não se migrou, e porque isso se confirmou certo

A alternativa a reler era **migrar** as decisões anuladas para a linha a que o artigo afinal
pertencia — a decisão é um facto sobre o *artigo*, não sobre a linha. Não se migrou por se
ter encontrado uma incoerência: na 3483 o `material_C2` anulado descrevia o artigo do
*ficheiro*, mas na 4591 descrevia o título da *própria linha*, o que sugeria que essa
decisão podia ter saído do resumo do banco e não do PDF.

A releitura confirmou que a cautela valia a pena: **a 4591 acabou por passar os seis
critérios, mas com o C5 aceite por um motivo diferente do que a decisão antiga sugeria** —
o artigo não tem um único valor de CO₂ e entra pela via «conduz ACV» da Opção A. Uma
migração teria carimbado uma justificação errada.

## O que ficou por fazer

| O quê | Porquê |
|---|---|
| **3028** — o C2 | Laminado cimentício de 4–12 mm, unidade funcional 1 m², sem função estrutural declarada nem um valor de MPa. Rejeita em C2, ou aceita e deixa o C6 rejeitar pelas fibras amazónicas? **Sai da RSL de qualquer forma; muda a contagem do PRISMA.** Aguarda a Kiê. |
| **3483** — qual regra manda | A da valorização multirota (os cinco resíduos viram matéria-prima do clínquer → Aceito) ou a da imobilização (o cimento só encapsula césio para descarte → Rejeitado)? As duas aplicam-se ao mesmo artigo. Aguarda a Kiê. |
| **2790 e 2880** | Continuam sem ficheiro PDF. Não se podem reler. |

## Achado colateral

Ao varrer o banco inteiro à procura de vazamentos de cascata, apareceu **a linha 3780**,
alheia a este trabalho: o C2 foi rejeitado a 2026-07-12 mas os `P:` de C3–C6, postos em
Junho, ficaram por limpar. Removidos conforme a regra, preservando os `R:` históricos.
Registo em `VAZAMENTO_CASCATA_CORRIGIDO_2026-08-23.csv`.

**Varredura final: zero vazamentos de cascata em todo o banco.**
