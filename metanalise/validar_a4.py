"""Validacao do motor do A4 (F48) contra os pares com A4 publicado — fase 4 do plano da F40 (tarefa #1807).

Le metanalise/transporte_a4_motor.csv (saida do motor, F48) e, de meta_analysis_base.xlsx (read_only),
o texto `transporte_dados` (col 64, F37) e as notas por etapa (F39) dos pares com `co2_a4` publicado.
Nao altera nada: escreve metanalise/transporte_a4_validacao.csv (um registo por par com A4 publicado)
e imprime o resumo que alimenta metanalise/VALIDACAO_A4_1807.md.

Comparacoes:
  1. factor implicito = A4 publicado / (massa [t/m3] x distancia declarada [km])  — so onde o artigo imprime a
     distancia central->obra em `transporte_dados` («betao km: N»); compara-se com os 4 factores SIDAC.
  2. distancia implicita = A4 publicado / coeficiente SIDAC do modo (kg/(m3.km)) — em todos os pares com A4 > 0;
     verifica-se se cai na grelha 0-300 km.
  3. peso do A4 publicado no CO2 do par vs. o que o motor da a 50 / 100 km.
Os pares com co2_a4 = 0 sao exclusoes explicitas do A4 pelo artigo (F39), nao medicoes: ficam fora das
comparacoes e sao contados a parte.
Uso (da raiz do repositorio):  /usr/bin/python3 metanalise/validar_a4.py
"""
import csv
import json
import re
import statistics

import openpyxl

ENTRADA = 'metanalise/transporte_a4_motor.csv'
SAIDA = 'metanalise/transporte_a4_validacao.csv'
SIDAC = json.load(open('metanalise/transporte_a4_sidac.json', encoding='utf-8'))['modos']
MODOS = list(SIDAC)


def med(xs):
    xs = [x for x in xs if x is not None]
    return round(statistics.median(xs), 3) if xs else None


def main():
    pares = [r for r in csv.DictReader(open(ENTRADA, encoding='utf-8')) if r['co2_a4_publicado'] not in ('', None)]
    ws = openpyxl.load_workbook('meta_analysis_base.xlsx', read_only=True)['dados_fck']
    H = {c.value: i for i, c in enumerate(next(ws.iter_rows(min_row=1, max_row=1)))}
    linhas = {str(r): row for r, row in enumerate(ws.iter_rows(min_row=2, values_only=True), start=2)}
    out = []
    for p in pares:
        row = linhas[p['obs_id']]
        td = str(row[H['transporte_dados']] or '')
        m = re.search(r'betao km:\s*([\d]+(?:[.,]\d+)?)', td)
        dist = float(m.group(1).replace(',', '.')) if m else None
        mf = re.search(r'factor:\s*([^;]+)', td)
        a4 = float(p['co2_a4_publicado']); co2 = float(p['co2_kg_m3']); massa_t = float(p['massa_volumica_kg_m3']) / 1000
        reg = {
            'obs_id': p['obs_id'], 'estudo': p['estudo'], 'rotulo': p['rotulo'], 'a4_grupo': p['a4_grupo'],
            'fronteira': p['fronteira'], 'a4_publicado_kg_m3': a4, 'co2_kg_m3': co2,
            'a4_publicado_pct_co2': round(100 * a4 / co2, 2) if co2 else None,
            'massa_t_m3': round(massa_t, 3), 'massa_origem': p['massa_volumica_origem'],
            'distancia_declarada_km': dist, 'factor_declarado_texto': (mf.group(1).strip()[:120] if mf else ''),
            'factor_implicito_kg_tkm': round(a4 / (massa_t * dist), 4) if (dist and a4 > 0) else None,
            'etapas_tipo': row[H['etapas_tipo']] or '', 'etapas_nota': str(row[H['etapas_nota']] or '')[:300],
            'transporte_dados': td[:300],
        }
        for mo in MODOS:
            coef = SIDAC[mo]['co2_kg_tkm'] * massa_t
            reg[f'dist_implicita_{mo}_km'] = round(a4 / coef, 1) if a4 > 0 else None
            reg[f'razao_motor_{mo}_na_dist_declarada'] = round(coef * dist / a4, 3) if (dist and a4 > 0) else None
        out.append(reg)
    with open(SAIDA, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(out[0]))
        w.writeheader(); w.writerows(out)

    pos = [o for o in out if o['a4_publicado_kg_m3'] > 0]
    zero = [o for o in out if o['a4_publicado_kg_m3'] == 0]
    est = lambda xs: len({o['estudo'] for o in xs})
    print(f'{len(out)} pares / {est(out)} estudos com co2_a4; A4 > 0: {len(pos)} pares / {est(pos)} estudos; '
          f'A4 = 0 (exclusao explicita): {len(zero)} pares / {est(zero)} estudos')
    print('grupo F38 dos pares com A4 > 0:', {g: sum(1 for o in pos if o['a4_grupo'] == g) for g in ('sim', 'provavel', 'nao', 'incerto')})
    # 1. factor implicito por estudo (um valor por estudo: mediana dos pares)
    por_est = {}
    for o in pos:
        por_est.setdefault(o['estudo'], []).append(o)
    fi = {}
    for e, os_ in por_est.items():
        v = med([o['factor_implicito_kg_tkm'] for o in os_])
        if v is not None:
            fi[e] = (os_[0]['rotulo'], os_[0]['distancia_declarada_km'], v, os_[0]['factor_declarado_texto'])
    print(f'\n1. factor implicito (estudos com distancia declarada): {len(fi)} estudos')
    for e, (rot, d, v, ft) in sorted(fi.items(), key=lambda x: x[1][2]):
        print(f'   {e} {rot[:30]:30s} {d:6.1f} km  {v:.3f} kg/(t.km)   | {ft[:70]}')
    vals = sorted(v for _, _, v, _ in fi.values())
    print(f'   mediana {med(vals)}; min {vals[0]:.3f}; max {vals[-1]:.3f}; '
          f'SIDAC betoneira 0,10 / truck e carreta 4e 0,07 / carreta 5e 0,06')
    for mo in MODOS:
        f = SIDAC[mo]['co2_kg_tkm']
        print(f'   {mo:11s}: estudos com factor implicito <= SIDAC: {sum(1 for v in vals if v <= f)}/{len(vals)}; '
              f'razao mediana motor/publicado na distancia declarada: {med([o[f"razao_motor_{mo}_na_dist_declarada"] for o in pos])}')
    # 2. distancia implicita
    print('\n2. distancia implicita (A4 publicado / coeficiente SIDAC), por estudo (mediana dos pares):')
    for mo in ('betoneira', 'carreta_5e'):
        di = [med([o[f'dist_implicita_{mo}_km'] for o in os_]) for os_ in por_est.values()]
        print(f'   {mo:11s}: mediana {med(di)} km; p10 {sorted(di)[len(di)//10]} ; p90 {sorted(di)[9*len(di)//10]}; '
              f'dentro de 0-300 km: {sum(1 for d in di if d <= 300)}/{len(di)}; > 300 km: '
              f'{[(e, round(med([o[f"dist_implicita_{mo}_km"] for o in os_]))) for e, os_ in por_est.items() if med([o[f"dist_implicita_{mo}_km"] for o in os_]) > 300]}')
    # 3. peso do A4 no CO2
    pct = [med([o['a4_publicado_pct_co2'] for o in os_]) for os_ in por_est.values()]
    print(f'\n3. A4 publicado como % do CO2 do par (por estudo): mediana {med(pct)} %, p10 {sorted(pct)[len(pct)//10]}, '
          f'p90 {sorted(pct)[9*len(pct)//10]}; o motor (grupo sim, betoneira) da +3,5 % a 50 km e +7,0 % a 100 km (F48)')
    print('\nzeros por etapas_tipo:', {k: sum(1 for o in zero if o['etapas_tipo'] == k) for k in sorted({o['etapas_tipo'] for o in zero})})


if __name__ == '__main__':
    main()
