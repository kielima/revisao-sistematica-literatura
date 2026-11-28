# Conferência da rodada

Gerado por `metanalise/conferir_rodada.py` em 2026-11-28 13:02.

**Resultado principal:** μ 10.54 [9.87–11.20], k 1113, 302 estudos · 1498 pares no painel, 398 estudos com par · corpus 466 (362 principal + 104 sensibilidade).

**Tudo confere.**

| | Verificação | Valores |
|---|---|---|
| ✅ | pares: dados_metanalise = motor do A4 | 1498 vs 1498 |
| ✅ | pares: dados_metanalise = A2 por par | 1498 vs 1498 |
| ✅ | pares: dados_metanalise = corpo de prova por par | 1498 vs 1498 |
| ✅ | pares: mesma ordem e valores (dados_metanalise × motor A4) | fck e CO₂ par a par |
| ✅ | principal: k e estudos dos dados = modelo | dados 1113 / 302; modelo 1113 / 302 |
| ✅ | principal: modelo = sensibilidade_a2 (referência) | k 1113, estudos 302, μ 10.5356 |
| ✅ | principal: modelo = sensibilidade_corpo_prova (referência) | k 1113, estudos 302, μ 10.5356 |
| ✅ | principal: modelo = sensibilidade_a4 (referência) | k 1113, estudos 302, μ 10.5356 |
| ✅ | principal: modelo = sensibilidade_secundarios (referência) | k 1113, estudos 302, μ 10.5356 |
| ✅ | principal: modelo = forest do painel | k 1113, estudos 302, μ 10.5356 |
| ✅ | principal: modelo = superfície do A4 | k 1113, estudos 302, μ 10.536 |
| ✅ | forest: todos os pares do painel | k p+s sem desconto 1449 ≤ 1498 pares |
| ✅ | PRISMA: corpus = principal + sensibilidade | 466 = 362 + 104 |
| ✅ | PRISMA: estudos com par ≤ corpus | 398 ≤ 466 |
| ✅ | PRISMA: estudos no modelo principal ≤ estudos do estrato principal | 302 ≤ 362 |
| ✅ | painel: nº de pares = dados_metanalise | 1498 vs 1498 |
| ✅ | painel: mesmos pares e ordem | fck e CO₂ par a par (2 casas) |
| ✅ | painel: MODELO = forest_site.json | var MODELO |
| ✅ | painel: A4MODELO = a4_site.json | var A4MODELO |
| ✅ | painel: A4 tem um registo por par | 1498 |
| ✅ | painel: funil = PRISMA | { key: 'e4', n: 466, principal: 362, sensibilidade: 104 } |
| ✅ | painel: KPI de estudos com par = dados | 398 vs 398 |
