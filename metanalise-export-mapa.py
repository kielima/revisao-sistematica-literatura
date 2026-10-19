"""Dados do mapa de publicacoes por pais e da linha temporal de citacoes (kielima.com/metanalise).

Pedido da Kie (2026-10-13): «grafico de publicacoes por paises» + «linha temporal que crie um mapa de todos
artigos da metanalise mostrando qual veio primeiro de cada um e com linha relacionando os artigos que citam
artigos dentro da mesma metanalise». Decisao F17-5 (Kie, 2026-10-14): os dois universos — todos os Elegiveis
(por omissao) e so os estudos com par no painel (botao).

- Pais: `articles_final.xlsx` col 57-60 (F15, pais do autor de correspondencia), ISO3 + ISO2.
- Ano: coluna `year`; mes do registo Crossref (`issued`) quando existe, so para ordenar dentro do ano.
- Citacoes: `lotes_paises/crossref.json` (lista de referencias por DOI). Ligacao A -> B quando um DOI da lista
  de referencias de A e o DOI de outro Elegivel B. As teses da BDTD nao tem lista de referencias no Crossref.
- Ligacoes extra (F35, Kie 2026-10-17: «todas as citacoes colocadas nesse mapa»): `lotes_paises/ligacoes_extra.csv`
  (de, para, via, citacao: citacoes estudo -> estudo que o Crossref nao entrega, por titulo ou leitura do PDF) e
  `lotes_paises/fontes_externas.csv` (bases de dados, relatorios e normas citados; mesmo `id_fonte` = fonte comum
  a varios artigos). O export leva `externas` e, por artigo, `ext` (ids) e `via` (origem de cada ligacao extra).
- «metanalise» = o artigo tem pelo menos um par no painel (mesmo filtro do `metanalise-export.py`).

Uso: python3 metanalise-export-mapa.py > ../kielima-site/public/metanalise/dados/mapa.json
"""
import csv
import importlib.util
import json
import re
import sys

import openpyxl

spec = importlib.util.spec_from_file_location('mx', 'metanalise-export.py')
mx = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mx)

import pycountry  # noqa: E402


def norm_doi(s):
    s = str(s or '').strip().lower()
    m = re.search(r'10\.\d{4,9}/\S+', s)
    return m.group(0).rstrip('.') if m else None


def main():
    ws = openpyxl.load_workbook('articles_final.xlsx', read_only=True)['Articles']
    rows = list(ws.iter_rows(values_only=True))
    h = rows[0]
    ix = {n: i for i, n in enumerate(h)}
    arts = {}
    for i, r in enumerate(rows[1:], start=2):
        if r[ix['status_triagem']] != 'Elegível':
            continue
        iso3 = r[ix['pais_iso3']]
        c = pycountry.countries.get(alpha_3=iso3) if iso3 else None
        doi = norm_doi(r[ix['doi']]) or norm_doi(r[ix['url']])
        arts[i] = {'id': i, 'rot': mx.short_label(r[ix['author']], r[ix['year']]), 'ano': int(r[ix['year']]),
                   'iso3': iso3, 'iso2': c.alpha_2 if c else None, 'doi': doi,
                   'titulo': str(r[ix['title']] or '').replace('\n', ' ')[:220]}
    # artigos com par no painel (qualquer cenario de CO2)
    wd = openpyxl.load_workbook(mx.BASE, read_only=True)['dados_fck']
    meta = set()
    for r in wd.iter_rows(min_row=2, values_only=True):
        rid = r[0]
        if rid not in arts:
            continue
        fck, co2 = mx.tofloat(r[7]), mx.tofloat(r[13])
        ck, com = mx.tofloat(r[36]), mx.tofloat(r[43])
        if fck in (None, 0) or co2 is None:
            continue
        val = ck if ck is not None else None
        ok = val is not None and mx.FCK_MIN <= fck <= mx.FCK_MAX and mx.CO2_MIN <= val <= mx.CO2_MAX
        if ok:
            meta.add(rid)
    cr = json.load(open('lotes_paises/crossref.json', encoding='utf-8'))
    por_doi = {a['doi']: a['id'] for a in arts.values() if a['doi']}
    sem_refs = 0
    for a in arts.values():
        w = cr.get(a['doi']) if a['doi'] else None
        a['meta'] = 1 if a['id'] in meta else 0
        a['mes'] = None
        cita = []
        if w:
            iss = (w.get('issued') or [[None]])[0]
            if len(iss) > 1:
                a['mes'] = iss[1]
            for d in w.get('ref_dois') or []:
                b = por_doi.get(norm_doi(d))
                if b and b != a['id']:
                    cita.append(b)
        if not w or not w.get('ref_dois'):
            sem_refs += 1
        a['cita'] = sorted(set(cita))
        a['refs'] = 1 if (w and w.get('ref_dois')) else 0
        del a['doi']
    # ligacoes extra estudo -> estudo
    for r in csv.DictReader(open('lotes_paises/ligacoes_extra.csv', encoding='utf-8')):
        de, para = int(r['de']), int(r['para'])
        if de in arts and para in arts and de != para and para not in arts[de]['cita']:
            arts[de]['cita'].append(para)
            arts[de]['cita'].sort()
            arts[de]['refs'] = 1
    # fontes externas (base de dados, relatorio, norma)
    ext, ext_nomes = {}, {}
    for r in csv.DictReader(open('lotes_paises/fontes_externas.csv', encoding='utf-8')):
        ext_nomes[r['id_fonte']] = {'id': r['id_fonte'], 'nome': r['nome'], 'tipo': r['tipo']}
        ext.setdefault(int(r['row_id']), set()).add(r['id_fonte'])
    for a in arts.values():
        a['ext'] = sorted(ext.get(a['id'], ()))
        if a['ext']:
            a['refs'] = 1
    out = sorted(arts.values(), key=lambda a: (a['ano'], a['mes'] or 0, a['id']))
    print(json.dumps({'gerado': 'metanalise-export-mapa.py', 'n': len(out), 'n_meta': len(meta),
                      'sem_refs': sem_refs, 'externas': list(ext_nomes.values()),
                      'artigos': out}, ensure_ascii=False, separators=(',', ':')))
    n_lig = sum(len(a['cita']) for a in out)
    n_lig_m = sum(1 for a in out for b in a['cita'] if a['meta'] and arts[b]['meta'])
    print(f'artigos {len(out)}, com par {len(meta)}, sem refs {sem_refs}, ligacoes {n_lig} (so metanalise {n_lig_m}), '
          f'paises {len({a["iso3"] for a in out})}', file=sys.stderr)


if __name__ == '__main__':
    main()
