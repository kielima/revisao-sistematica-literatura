"""Geometria do mapa-mundo do painel (kielima.com/metanalise) — gerada uma vez.

Fonte: world-atlas@2.0.2 (countries-110m.json, Natural Earth 1:110m, dominio publico; pacote npm, licenca ISC).
Obter com `npm pack world-atlas@2.0.2` numa pasta de trabalho e passar o caminho do countries-110m.json.
Projeccao Equal Earth (area igual), largura 1000. Antarctica omitida. Cada pais sai com o ISO3 e o ISO2
(pycountry, a partir do codigo numerico ISO 3166 do world-atlas) e o caminho SVG.

Uso: python3 metanalise/mapa/gerar_mundo.py <countries-110m.json> <saida mundo.json>
"""
import json
import math
import sys

import pycountry

A1, A2, A3, A4 = 1.340264, -0.081106, 0.000893, 0.003796
M = math.sqrt(3) / 2
W = 1000.0


def ee(lon, lat):
    lam, phi = math.radians(lon), math.radians(lat)
    t = math.asin(M * math.sin(phi))
    t2 = t * t
    t6 = t2 * t2 * t2
    x = lam * math.cos(t) / (M * (A1 + 3 * A2 * t2 + t6 * (7 * A3 + 9 * A4 * t2)))
    y = t * (A1 + A2 * t2 + t6 * (A3 + A4 * t2))
    return x, y


XMAX = ee(180, 0)[0]
YMAX = ee(0, 90)[1]
S = W / (2 * XMAX)
H = 2 * YMAX * S


def proj(lon, lat):
    x, y = ee(lon, lat)
    return (x + XMAX) * S, (YMAX - y) * S


def main(src, out):
    topo = json.load(open(src))
    sc, tr = topo['transform']['scale'], topo['transform']['translate']
    arcs = []
    for arc in topo['arcs']:
        x = y = 0
        pts = []
        for dx, dy in arc:
            x += dx
            y += dy
            pts.append((x * sc[0] + tr[0], y * sc[1] + tr[1]))
        arcs.append(pts)

    def ring(idx):
        pts = []
        for i in idx:
            a = arcs[i] if i >= 0 else arcs[~i][::-1]
            pts.extend(a if not pts else a[1:])
        return pts

    paises = []
    for g in topo['objects']['countries']['geometries']:
        if g.get('id') == '010' or not g.get('arcs'):
            continue
        polys = g['arcs'] if g['type'] == 'MultiPolygon' else [g['arcs']]
        d = []
        for poly in polys:
            for r in poly:
                rr = ring(r)
                if any(abs(a[0] - b[0]) > 180 for a, b in zip(rr, rr[1:])):
                    # anel que atravessa o antimeridiano (Russia, Fiji): os pontos do lado minoritario
                    # ficam presos a +-180, em vez de riscarem o mapa de um lado ao outro
                    pos = sum(1 for lon, _ in rr if lon > 0) >= len(rr) / 2
                    rr = [((180.0 if pos else -180.0) if (lon < 0) == pos else lon, lat) for lon, lat in rr]
                pts = [proj(lon, lat) for lon, lat in rr]
                seg = 'M' + 'L'.join(f'{x:.1f},{y:.1f}' for x, y in pts) + 'Z'
                d.append(seg)
        c = pycountry.countries.get(numeric=g.get('id')) if g.get('id') else None
        paises.append({'iso3': c.alpha_3 if c else None, 'iso2': c.alpha_2 if c else None,
                       'nome': g['properties']['name'], 'd': ''.join(d)})
    json.dump({'fonte': 'Natural Earth 1:110m via world-atlas@2.0.2; projeccao Equal Earth',
               'largura': W, 'altura': round(H, 1), 'paises': paises},
              open(out, 'w'), ensure_ascii=False, separators=(',', ':'))
    print(len(paises), 'paises', round(H, 1))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
