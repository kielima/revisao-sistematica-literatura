"""Junta os resultados dos lotes de rastreio de citacoes (F35) em lotes_paises/ligacoes_extra.csv e
lotes_paises/fontes_externas.csv. Idempotente: nao repete (de,para) nem (id_fonte,row_id).
Uso: python3 lotes_citacoes/aplicar.py"""
import csv
import glob
import json
import re

HOJE = '2026-10-17'
LIG, EXT = 'lotes_paises/ligacoes_extra.csv', 'lotes_paises/fontes_externas.csv'


def limpa(s, n=400):
    return re.sub(r'\s+', ' ', str(s or '')).strip()[:n]


lig = list(csv.DictReader(open(LIG, encoding='utf-8')))
ext = list(csv.DictReader(open(EXT, encoding='utf-8')))
tem_l = {(int(r['de']), int(r['para'])) for r in lig}
tem_e = {(r['id_fonte'], int(r['row_id'])) for r in ext}
nomes = {r['id_fonte']: (r['nome'], r['tipo']) for r in ext}
nl = ne = 0
for f in sorted(glob.glob('lotes_citacoes/resultado_lote*.json')):
    for r in json.load(open(f, encoding='utf-8')):
        rid = int(r['row_id'])
        for l in r.get('ligacoes') or []:
            k = (rid, int(l['para']))
            if k in tem_l or k[0] == k[1]:
                continue
            tem_l.add(k)
            lig.append({'de': rid, 'para': l['para'], 'via': 'pdf_lista_referencias',
                        'citacao': limpa(f"{l.get('local', '')}: {l.get('citacao', '')}"), 'data': HOJE})
            nl += 1
        for e in r.get('externas') or []:
            idf = re.sub(r'[^a-z0-9_]+', '_', str(e.get('id_fonte') or '').lower()).strip('_')
            if not idf or (idf, rid) in tem_e:
                continue
            tem_e.add((idf, rid))
            nome, tipo = nomes.setdefault(idf, (limpa(e.get('nome'), 200), limpa(e.get('tipo'), 30)))
            ext.append({'id_fonte': idf, 'nome': nome, 'tipo': tipo, 'row_id': rid,
                        'citacao': limpa(f"{e.get('local', '')}: {e.get('citacao', '')}"), 'via': 'pdf_lista_referencias',
                        'data': HOJE})
            ne += 1
for path, rows, cols in ((LIG, lig, ['de', 'para', 'via', 'citacao', 'data']),
                         (EXT, ext, ['id_fonte', 'nome', 'tipo', 'row_id', 'citacao', 'via', 'data'])):
    with open(path, 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, cols)
        w.writeheader()
        w.writerows(rows)
print('ligacoes novas', nl, 'fontes externas novas', ne)
