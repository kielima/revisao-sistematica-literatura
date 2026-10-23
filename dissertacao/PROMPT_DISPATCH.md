# Prompt para continuar pelo Dispatch (colar tal como está)

Continua comigo o trabalho de correções da dissertação, direto no Word, na minha máquina. Sou a Kiê; a dissertação é uma revisão sistemática de literatura sobre betão estrutural de baixo carbono (UHPC).

## Como trabalhar
- **Uma pergunta de cada vez**, em texto corrido no chat (nunca em caixas de escolha), sempre com o contexto: onde aparece no texto, o parágrafo e o que as fontes dizem. Espera a minha resposta antes de passar à seguinte.
- **Só podes usar termos e factos que estejam claramente nas fontes.** Lê as fontes por completo (100%, não por resumo) antes de propor texto. Se uma fonte não estiver acessível, pede-me o PDF em vez de assumir.
- **Edita diretamente o original, sem criar cópias**, sempre em **tracked changes** (autor «Claude») com um comentário curto a justificar e indicar a fonte. Nunca aceites nem rejeites revisões existentes. Antes de guardar, confirma que o Word não tem o ficheiro aberto em conflito; depois valida que o resto ficou intacto (parágrafos, tabelas, figuras).
- Usa as skills `docx` e `escrita científica` (e `dissertacao-tracked-changes`, se existir).
- Ficheiro: pasta `C:\Users\ttibu\Documents\03_PROFISSIONAL\PESQUISA\MINHAS_PRODUÇÕES\04_DISSERTAÇÃO\02_DOCUMENTO_PRINCIPAL`; usa o `DISSERTAÇÃO_KIÊ_vNN.docx` mais recente (em 18/10 era o v20; confirma qual é).
- Contexto completo e histórico no repositório GitHub `kielima/revisao-sistematica-literatura` (branch `main`): `dissertacao/EDICOES_DISSERTACAO.md` (registo das edições e respostas) e `dissertacao/CARTAO_E-001_MRV.md`. Se tiveres acesso ao repositório, lê-os primeiro.

## Estado das 4 perguntas das correções da banca (comentários de 19/08 no Word)

**E-001, sigla MRV — APROVADA, falta aplicar no Word.**
Capítulo «Desmaterialização da Construção Civil», secção sobre a ABCIC/SNIC, último parágrafo. Substituir a frase
«A ABCP e a ABCIC recomendam a adoção de EPDs setoriais, o uso da ferramenta RenovaCalc e a construção, no médio prazo, de um sistema de mensuração, relato e verificação (MRV) robusto, considerado pré-requisito para a eventual implantação do mercado regulado de carbono brasileiro (SNIC, 2015; Penna, 2025).»
por
«O setor defende que, antes da entrada em vigor de uma política de precificação de carbono, seja implementado um sistema de Monitoramento, Relato e Verificação (MRV) robusto e confiável (SNIC, 2020).»
Motivo: o SNIC (SEGS, 01/12/2020) define MRV como Monitoramento, Relato e Verificação; Penna (2025) e o Roadmap Net Zero 2025 (ABCP) não contêm MRV, RenovaCalc nem EPD. Depois de aplicar, diz-me e passa à seguinte.
Pendentes à parte, a perguntar-me depois: (1) a referência «SNIC, 2015» devia ser 2020 segundo o documento; (2) o texto e o cabeçalho da secção usam «ABCIC», mas a fonte nomeia o SNIC e a ABCP.

**#1100, simplificar as strings de busca — AGUARDA A MINHA APROVAÇÃO (opção b).**
Capítulo da metodologia, secção «Strings de Busca». O trecho narra 4 passos: busca prévia no Scopus ("Systematic Review" AND "Meta-analysis" AND "Concrete" AND "Life Cycle Assessment", zero resultados); segunda busca sem "Meta-analysis" (24 documentos, Gráfico 5); busca ampla "Life Cycle" AND ("concrete" OR "cement" OR "UHPC" OR "Alkali-Activated") com mais de dez mil resultados analisados no VOSviewer (Figura 9); string final "Life Cycle Assessment" AND (…). Proposta (b): manter o relato do processo iterativo mais curto, sem as strings intermédias:
«A string foi definida de forma iterativa. Uma busca prévia no Scopus não identificou nenhuma revisão sistemática com meta-análise sobre concreto e ACV, e uma busca ampla com o termo "Life Cycle" retornou mais de dez mil documentos. A análise desses resultados no VOSviewer (Figura 9) mostrou que "Life Cycle Assessment" era a variação mais alinhada ao objetivo da pesquisa, e esse termo foi adotado na string final, apresentada no Quadro X.»
A string final já aparece no quadro do protocolo. Perguntar-me se aprovo; se sim, aplicar. Perguntar também se o Gráfico 5 (que só serve a 2.ª busca) sai do capítulo e da lista de figuras.

**#1105, origem de fck = 29 MPa (CC) e 121 MPa (UHPC) no fim de «Unidade Funcional» — POR RESOLVER.**
A Lia (banca) pediu para citar a origem acima da secção 4.2. UHPC 121 MPa coincide com a mediana do fck das 39 observações UHPC da metanálise (121,5 MPa). CC 29 MPa não coincide com nenhuma mediana atual da metanálise (cimento Portland 35,0; betão armado 34,5; reciclado 34,1; todos os pares 39,4). Preciso de saber de onde vem o 29 (estudo específico ou versão antiga do banco). Pergunta-me; se eu não souber, propõe citar a mediana atual da metanálise para ambos e atualizar o valor de CC, só se eu aprovar.

**#1126, siglas IPCC e ONU nas referências — POR RESOLVER.**
A banca (Renata) pediu o nome completo das siglas nas referências. Hoje aparecem «IPCC.» (2 entradas) e «ONU.» (1 entrada) só como sigla. A ABNT permite as duas formas. Proposta: «INTERGOVERNMENTAL PANEL ON CLIMATE CHANGE (IPCC).» e «ORGANIZAÇÃO DAS NAÇÕES UNIDAS (ONU).» nas 3 entradas. Perguntar-me se aprovo; se sim, aplicar.

Começa por aplicar a E-001 e depois faz-me a pergunta do #1100.
