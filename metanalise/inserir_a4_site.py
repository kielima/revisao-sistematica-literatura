"""F63 (#1808 parte painel): insere no metanalise.js do kielima-site os dados do controlo do A4.

- `var A4 = [...]`: por par do painel, alinhado com `var DATA` (mesma ordem de
  dados_metanalise.csv / transporte_a4_motor.csv), [grupo, coef betoneira, coef
  truck 3e, coef carreta 4e, coef carreta 5e] em kg CO2-eq/(m3.km).
  grupo: s = sim (F38), p = provavel, n = nao, i = incerto.
- `var A4MODELO = {...}`: grelha do modelo de metanalise/resultados/a4_site.json
  (exportar_a4_site.R).

Confere, par a par, que fck e CO2 do motor batem com DATA (tolerância 0,01,
porque o site arredonda a 2 casas); aborta se não baterem.

Uso: python3 metanalise/inserir_a4_site.py ../kielima-site/public/assets/metanalise.js
Correr de novo sempre que mudarem pares (depois de motor_a4.py e exportar_a4_site.R).
"""
import csv, json, re, sys

js_path = sys.argv[1]
js = open(js_path, encoding='utf-8').read()
data = json.loads(re.search(r'^  var DATA = (\[.*?\]);$', js, re.M).group(1))
motor = list(csv.DictReader(open('metanalise/transporte_a4_motor.csv', encoding='utf-8')))
assert len(data) == len(motor), (len(data), len(motor))
for i, (d, m) in enumerate(zip(data, motor)):
    assert abs(d[0] - float(m['fck'])) < 0.01 and abs(d[1] - float(m['co2_kg_m3'])) < 0.01, (i, d[:2], m['fck'], m['co2_kg_m3'])

COD = {'sim': 's', 'provavel': 'p', 'nao': 'n', 'incerto': 'i'}
modos = ['betoneira', 'truck_3e', 'carreta_4e', 'carreta_5e']
a4 = []
for m in motor:
    row = [COD[m['a4_grupo']]]
    for mo in modos:
        v = m['coef_%s_kg_m3_km' % mo]
        row.append(round(float(v), 5) if v not in ('', 'NA') else 0)
    a4.append(row)

grid = json.load(open('metanalise/resultados/a4_site.json', encoding='utf-8'))

def put(s, var, val):
    new = '  var %s = %s;' % (var, json.dumps(val, ensure_ascii=False, separators=(',', ':')))
    s, n = re.subn(r'^  var %s = .*;$' % var, lambda _: new, s, count=1, flags=re.M)
    assert n == 1, var
    return s

js = put(js, 'A4', a4)
js = put(js, 'A4MODELO', grid)
open(js_path, 'w', encoding='utf-8').write(js)
print('A4: %d pares (s=%d, p=%d); A4MODELO: %d curvas km 0-300' % (
    len(a4), sum(r[0] == 's' for r in a4), sum(r[0] == 'p' for r in a4), sum(len(v) for v in grid['superficie'].values())))
