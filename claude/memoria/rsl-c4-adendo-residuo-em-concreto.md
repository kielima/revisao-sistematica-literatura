---
name: rsl-c4-adendo-residuo-em-concreto
description: "No C4 da RSL: resíduo/material de setor off-topic USADO para melhorar/substituir o concreto = ACEITO; re-revisar os 228 pré-marcados; dúvida = perguntar"
metadata:
  node_type: memory
  type: feedback
  originSessionId: c4-triagem
---

Critério **C4 (não relacionado a construção civil)** da RSL — regras confirmadas pela Kiê em 2026-06-13:

**⭐ ADENDO DE ACEITAÇÃO:** mesmo que o artigo seja de setor off-topic (medicina, agricultura, alimentos, eletrônica, energia eólica/solar, etc.), se ele **usa um material/resíduo desse setor com o propósito de melhorar ou substituir o concreto** → **C4 ACEITO**. Ex.: partes de turbina eólica trituradas como agregado no concreto; casca de arroz/bagaço/lodo/cinza como SCM ou agregado. O que decide é a **aplicação como material para substituto/componente do concreto**, NÃO o setor de origem do resíduo. Só rejeitar quando o estudo é do setor off-topic SEM essa ponte para material de construção (ex.: microalgas para biocombustível, poço de petróleo, pesca, tratamento de água sem uso do material em concreto).

**Re-revisão dos 228 pré-marcados:** os ~228 artigos marcados `[C4 Rejeitado]` nas passadas de C2/C3 (nível resumo) **devem ser re-revisados nesta passada por PDF** com o adendo acima — vários podem virar Aceito. Universo C4 = todos os 1.631 C3-Aceito. Indicador de "revisado nesta passada" = carimbo `2026-06-13` na nota C4.

**Dúvida → PARAR e perguntar à Kiê antes de classificar.**

**📖 MÉTODO DE LEITURA C4 (decisão Kiê 2026-06-14, após anular a 1ª passada por resumo):** NUNCA classificar por resumo/título/metadados. Ler as **3 PRIMEIRAS PÁGINAS do PDF**; se não der para aplicar o critério, **continuar lendo as páginas seguintes** até ter conteúdo suficiente, ou então parar e perguntar. Verificar SEMPRE se o material/resíduo é usado em/para concreto antes de rejeitar (a 1ª passada rejeitou indevidamente 3311 = cinza p/ construção e 3257 = carbonação→agregado). Carimbo da passada válida do C4 = `2026-06-14`.

**🏷️ Rastreio em rejeitados de C4 (decisão Kiê 2026-06-13):** quando um artigo for REJEITADO no C4 mas trouxer **tecnologia relacionada a concreto/cimento** (clínquer, descarbonização do cimento via combustível alternativo, captura de CO2 no cimento, aglomerante alternativo, energia COM tecnologia de concreto), anotar na coluna `rastreio_potencial_futuro` (col 33) a tag adequada: clínquer→`fator_clinquer`; combustível alternativo/descarbonização do cimento→`outra`; captura/mineralização CO2→`carbonatacao_captura`; aglomerante→`aglomerante_alternativo`. Se o item de energia NÃO tiver tecnologia de concreto (ex.: eólica→hidrogênio, concreto só como fundação no inventário) → sem tag. Casos: 2640 (clínquer→fator_clinquer), 2676 (combustível em planta de cimento→outra).

**🏗️ ACV de instalação de saneamento (decisão Kiê 2026-06-14, caso 3252):** ACV de **estação de tratamento de água/esgoto (ETA/ETE) ou instalação semelhante**, cobrindo fases de construção + operação, com concreto/armadura apenas como item de inventário da obra → **C4 ACEITO** como infraestrutura/obra civil (BRANCO + nota "A revisar"). Regra geral para ETAs/ETEs/instalações de infraestrutura urbana — coerente com aceitar redes de esgoto (2955) e planejamento urbano (2907). Casos: 3252 (ETA), 3473 (ETE pequena), 3644 (ETE fase de construção).

**📋 Critério decisivo p/ instalações/sistemas (decisão Kiê 2026-06-14, caso 3699 — aterro sanitário de RSU):** quando uma ACV é de uma instalação/sistema (mesmo de gestão de resíduos, que normalmente seria Rejeitado), **verificar se o inventário (LCI) documenta o concreto com fluxos de entrada/saída** (quantidades, processo ecoinvent, etc.). **Se sim → C4 ACEITO** (A revisar). 3699 foi aceito porque o LCI tinha 3,10 kg de concreto por tonelada de resíduo + processo "Cement at plant" + aço/asfalto/brita. Aplicar esse teste a aterros/instalações ambíguas: sem fluxos documentados do concreto = volta a ser gestão de resíduo (Rejeitado, como 3376/3415).

**♻️ Resíduo em estudo de valorização multirota (decisão Kiê 2026-06-14, caso 4165):** se um estudo de valorização/gestão de resíduo off-topic avalia VÁRIAS rotas e UMA delas usa o resíduo como **MATERIAL/INSUMO em cimento/concreto/asfalto** (ex.: plástico de resíduo de saúde como feedstock de *reinforced cement*; cinza/lodo incorporado como matéria-prima na produção de cimento) → **C4 ACEITO** (adendo; o dado da rota cimentícia é extraível). **MAS** resíduo usado só como **COMBUSTÍVEL** no forno (RDF, biossólido como fuel) ou cimento usado só para **IMOBILIZAR/descartar** o resíduo (S/S para aterro, ex. 3383) → **REJEITADO**. Divisor: resíduo vira MATERIAL do cimento/concreto (Aceito) vs vira ENERGIA / é apenas imobilizado para descarte (Rejeitado).

**Demais regras C4:** REJEITADO = setor off-topic sem ponte p/ construção; precursor sem ACV do elemento final (clínquer isolado, forno de cimento, mineração de agregado sem produto). ACEITO = concreto/cimento/UHPC/cimentícios em construção. BRANCO (infra genérica/sistema sem material) → Aceito + nota "A revisar". Ver [[rsl-criterios-verbatim]] e [[rsl-argamassa-revestimento-e-taipa]].
