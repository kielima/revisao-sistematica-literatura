---
name: rsl-c2-material-incidental-e-revisoes-sem-dados
description: "Na fase de confirmação por PDF (C1-C6 + extração), casos de 'material incidental' (concreto/material aparece só como pano de fundo, não como objeto de estudo) exigem discussão caso a caso com a Kiê antes de decidir C2 -- não aplicar o padrão automaticamente. Revisões de literatura sem dados próprios: anotar em comments para buscar depois os artigos citados que podem ter dados extraíveis."
metadata:
  node_type: memory
  type: feedback
  originSessionId: fb2a5077-0c97-4017-a789-3068eea0b954
---

**Contexto:** durante o piloto de 5 artigos da fase "confirmar por PDF" (2026-08-04), Claude reverteu C2 de Aceito→Rejeitado em 2 linhas (2553 Abouhamad — concreto aparece só como fundação/laje genérica num edifício de aço-leve; 2557 Adams — telha de concreto é só baseline de comparação para filmes de resfriamento radiativo, não objeto de estudo) usando o raciocínio "concreto incidental" (material presente no artigo mas não é o que está sendo caracterizado/estudado).

## Regra 1 — casos de "material incidental" exigem discussão caso a caso

**Instrução da Kiê (2026-08-04):** "Faz sentido sim essa distinção mas quando tiver casos assim de novo vamos discutir um a um antes de você decidir direto."

**Como aplicar:** sempre que um artigo tiver o material estrutural aparecendo apenas como componente secundário/pano de fundo (não como objeto de caracterização do próprio estudo — sem traço, sem propriedades próprias, só citado/usado como baseline de comparação ou item de bill-of-materials genérico), **parar e apresentar o caso específico à Kiê antes de registrar a decisão C2**, mesmo que o padrão pareça igual a um caso já decidido antes. Não generalizar/auto-aplicar o precedente de Abouhamad/Adams a novos artigos sem essa conversa.

**Distinção-chave (já validada, pode citar ao apresentar o caso):** C2 = "Materiais que não são estruturais" (aba Critérios) — critério de ESCOPO TEMÁTICO (o material estrutural moldável é o que está sendo estudado?), não de disponibilidade de dado. Um número de CO2/GWP existir para o material incidental não muda a decisão C2, porque geralmente esse número não é comparável de qualquer forma (sem traço, sem classe de resistência, unidade por m² de edifício em vez de por m³ de material).

## Regra 2 — revisões de literatura sem dados próprios: anotar citações para busca posterior

**Instrução da Kiê (2026-08-04):** "se for uma revisão de literatura que não tem dados mas ele cita trabalhos que podem entrar com dados como artigos externos então ele pode ser anotado em comentários pra fazer isso depois, buscar os artigos das citações quando for uma revisão sem dados próprios."

**Como aplicar:** quando o artigo em avaliação for uma revisão de literatura (Review/Systematic Review — lembrando que C8 NÃO rejeita esses) e não tiver dados primários próprios de fck/CO2/durabilidade, mas citar estudos individuais que aparentam ter esses dados:
1. Não tentar extrair dado da própria revisão (ela não tem).
2. Registrar em `comments` (articles_final.xlsx) uma nota tipo `[Revisão sem dados próprios — candidatos p/ busca externa: <lista de referências relevantes citadas, com autor/ano/tema>]`.
3. Isso fica como pendência para revisitar depois — buscar esses artigos citados individualmente (podem já estar no banco desta RSL sob outro registro, ou podem ser "fontes externas" a adicionar).
4. Não bloquear o fluxo da RSL por causa disso — é uma nota lateral, não uma reavaliação de C2/C5 da própria revisão.

**Why:** revisões geralmente passam C1-C8 normalmente pelo próprio conteúdo (são sobre o tema), mas não geram dados extraíveis pra metanálise por não terem ensaio/medição própria. Perder esse artigo sem registrar suas referências-chave desperdiça um atalho para achar mais estudos primários relevantes que talvez não tenham aparecido nas buscas originais das bases.

Ver [[rsl-marcacao-R-vs-P]], [[rsl-criterios-verbatim]].
