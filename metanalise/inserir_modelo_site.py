"""Insere metanalise/resultados/forest_site.json na linha `var MODELO = ...;` do metanalise.js do kielima-site (F28).

Uso: python3 metanalise/inserir_modelo_site.py metanalise/resultados/forest_site.json ../kielima-site/public/assets/metanalise.js
"""
import json, re, sys
src, js = sys.argv[1], sys.argv[2]
m = json.load(open(src, encoding='utf-8'))
s = open(js, encoding='utf-8').read()
new = '  var MODELO = %s;' % json.dumps(m, ensure_ascii=False, separators=(',', ':'))
s, n = re.subn(r'^  var MODELO = .*;$', lambda _: new, s, count=1, flags=re.M)
assert n == 1
open(js, 'w', encoding='utf-8').write(s)
print('MODELO inserido:', len(m['cenarios']), 'cenarios')
