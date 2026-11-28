"""Rodada final (#1976): insere no metanalise.js do kielima-site os dados do painel que
até aqui se copiavam à mão (docstring do metanalise-export.py: «injectar manualmente»).

- `var DATA`, `var UNIT_STATS`, `var UNIT_EXCLUDED`, `var VIDA_FAM` <- saída do metanalise-export.py
  (chaves pairs, unit_stats, excluded, vida_familia).
- `var FUNNEL` (números das etapas) <- 00_REFERENCIAS/PRISMA/FUNIL_PRISMA.csv (contar_funil_prisma.py):
  universo = ident, e1 = ret, e2 = e3 (aceites na E2), e3 = e4 (passam a E3), e4 = fin, com
  principal = main e sensibilidade = tier.
- `KPI_VALUES.funil` = fin; `KPI_VALUES.releitura` = estudos distintos de metanalise/dados_metanalise.csv.
  `KPI_VALUES.vida` não é tocado (contagem de artigos com vida útil declarada, manual).

Uso: python3 metanalise/inserir_dados_site.py export.json ../kielima-site/public/assets/metanalise.js
Testado a 2026-11-28: com os dados de 21/11 não muda nenhum byte do metanalise.js publicado.
"""
import csv, json, re, sys

exp_path, js_path = sys.argv[1], sys.argv[2]
e = json.load(open(exp_path, encoding='utf-8'))
js = open(js_path, encoding='utf-8').read()


def put(s, var, val):
    old = re.search(r'^  var %s = (.*);$' % var, s, re.M)
    assert old, var
    if json.loads(old.group(1)) == val:  # mesmo conteúdo (só a ordem das chaves pode diferir): não mexer
        return s
    new = '  var %s = %s;' % (var, json.dumps(val, ensure_ascii=False, separators=(',', ':')))
    s, n = re.subn(r'^  var %s = .*;$' % var, lambda _: new, s, count=1, flags=re.M)
    assert n == 1, var
    return s


for var, key in [('DATA', 'pairs'), ('UNIT_STATS', 'unit_stats'), ('UNIT_EXCLUDED', 'excluded'),
                 ('VIDA_FAM', 'vida_familia')]:
    js = put(js, var, e[key])

f = {r['id']: int(r['n']) for r in csv.DictReader(open('00_REFERENCIAS/PRISMA/FUNIL_PRISMA.csv', encoding='utf-8'))}
funil = [('universo', f['ident']), ('e1', f['ret']), ('e2', f['e3']), ('e3', f['e4'])]
for key, n in funil:
    js, k = re.subn(r"(\{ key: '%s', n: )\d+( \})" % key, r'\g<1>%d\g<2>' % n, js, count=1)
    assert k == 1, key
js, k = re.subn(r"\{ key: 'e4', n: \d+, principal: \d+, sensibilidade: \d+ \}",
                "{ key: 'e4', n: %d, principal: %d, sensibilidade: %d }" % (f['fin'], f['main'], f['tier']), js, count=1)
assert k == 1, 'e4'

estudos = len({r['estudo'] for r in csv.DictReader(open('metanalise/dados_metanalise.csv', encoding='utf-8'))})
js, k = re.subn(r'(\n    funil: )\d+(,)', r'\g<1>%d\g<2>' % f['fin'], js, count=1)
assert k == 1, 'kpi funil'
js, k = re.subn(r'(\n    releitura: )\d+(,)', r'\g<1>%d\g<2>' % estudos, js, count=1)
assert k == 1, 'kpi releitura'

open(js_path, 'w', encoding='utf-8').write(js)
print('DATA %d pares; FUNNEL %s; e4 %d (%d + %d); estudos com par %d' % (
    len(e['pairs']), [n for _, n in funil], f['fin'], f['main'], f['tier'], estudos))
