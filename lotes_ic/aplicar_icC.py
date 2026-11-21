"""Aplica o lote IC-C (#1812, 2026-11-21): dispersao dos 6 estudos com QG > 0 e IC do fck incompleto
que a ronda de 04/10 nao cobriu (3732 CUNNINGHAM 2021, 2684 HAFEZ, 3095 TEFA, 3187 YU, 2658 D'ORAZIO,
3162 SPAGNUOLO).

Fontes: lotes_ic/resultado_icC.json (subagente) + leitura pessoal (CUNNINGHAM Tab.3 por texto;
figuras conferidas por imagem). Regras:
  - IC so preenche celulas vazias (ic_*_valor); tipo/n/citacao acompanham o valor;
  - SOBREPOR: leituras pessoais que substituem as do lote;
  - CORRIGIR: valores ja gravados que a leitura provou errados (CUNNINGHAM controlo 3,3 -> 3,4:
    o 3,3 era o DP dos 56 d).
Correr da raiz do repo; depois preparar_dados.py (o vi do modelo usa os IC) e exportar_forest_site.R.
"""
import json
import re
import sys

import openpyxl

BASE = 'meta_analysis_base.xlsx'
C_OBS = 13
C_ICF, C_ICF_T, C_ICF_N, C_ICF_C = 26, 27, 28, 29
C_ICC, C_ICC_T, C_ICC_N, C_ICC_C = 30, 31, 32, 33
HOJE = '2026-11-21'
TIPO = {'cov': 'cv_percentual', 'percentis': 'intervalo_interquartil'}


def clean(s):
    return re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', str(s))


def nota(ws, r, txt):
    obs = ws.cell(r, C_OBS).value
    ws.cell(r, C_OBS).value = clean(f'{obs} [{txt}]' if obs else f'[{txt}]')


# ---------------------------------------------------------------- 3732 CUNNINGHAM 2021 (leitura pessoal)
# Tab.3 p.3682 (texto do PDF): "Average Compressive Strengths (MPa) of Mortars at 7, 28, and 56 Days ...
# (n = 5)"; "Values in parentheses are the standard deviations for the mortar samples tested".
# Sec. Methods: "five replicate specimens of each mixture", cilindros 50 x 100 mm. Coluna dos 28 d.
CUNN_DP = {  # sheet_row -> (fck gravado, DP aos 28 d, mistura)
    1864: (37.1, 2.5, 'S-U-600'), 1865: (29.6, 1.9, 'S-U-850'), 1866: (31.6, 1.9, 'S-U-1100'),
    1867: (28.3, 5.7, 'S-W-600'), 1868: (27.0, 1.7, 'S-W-850'), 1869: (25.9, 1.3, 'S-W-1100'),
    1870: (22.2, 0.5, 'S-A-600'), 1871: (31.4, 1.3, 'S-A-850'),
    1872: (34.2, 2.4, 'H-U-600'), 1873: (27.2, 0.9, 'H-U-850'), 1874: (29.2, 1.7, 'H-U-1100'),
    1875: (31.4, 1.8, 'H-W-600'), 1876: (27.7, 2.1, 'H-W-850'), 1877: (23.5, 1.3, 'H-W-1100'),
    1878: (34.5, 1.3, 'H-A-600'), 1879: (27.7, 0.9, 'H-A-850'),
}
CUNN_CORRIGIR = {1084: (3.3, 3.4, 'control mortars')}  # DP gravado era o dos 56 d (42.1 (3.3)); aos 28 d: 38.2 (3.4)
CUNN_CIT = ('Tab.3 p.3682 (n = 5): "{mix}" 28 d {fck} ({dp}) MPa; "Values in parentheses are the standard '
            'deviations for the mortar samples tested"; Methods: "five replicate specimens of each mixture", '
            'cilindros 50 x 100 mm')

# ---------------------------------------------------------------- SOBREPOR / CORRIGIR do lote (preenchido apos auditoria)
SOBREPOR = {}   # sheet_row -> dict com ic_fck_valor/tipo/n/citacao (leitura pessoal substitui a do subagente)
IGNORAR = set()  # sheet_rows do lote que a auditoria rejeitou


def main(gravar):
    res = {}
    for a in json.load(open('lotes_ic/resultado_icC.json', encoding='utf-8')):
        for p in a['pares']:
            res[int(p['sheet_row'])] = (str(a['row_id']), p)
    for r, p in SOBREPOR.items():
        res[r] = (res[r][0], {**res[r][1], **p}) if r in res else res.get(r)
    wb = openpyxl.load_workbook(BASE)
    ws = wb['dados_fck']
    n_f = n_c = 0
    log = []
    # CUNNINGHAM pessoal
    for r, (fck, dp, mix) in CUNN_DP.items():
        assert str(ws.cell(r, 1).value) == '3732' and float(ws.cell(r, 8).value) == fck, (r, ws.cell(r, 8).value)
        if ws.cell(r, C_ICF).value in (None, ''):
            ws.cell(r, C_ICF).value = dp
            ws.cell(r, C_ICF_T).value = 'desvio_padrao'
            ws.cell(r, C_ICF_N).value = 5
            ws.cell(r, C_ICF_C).value = f'[{HOJE} #1812] ' + CUNN_CIT.format(mix=mix, fck=fck, dp=dp)
            n_f += 1
            log.append((r, '3732', 'ic_fck', dp))
    for r, (velho, novo, mix) in CUNN_CORRIGIR.items():
        assert str(ws.cell(r, 1).value) == '3732' and float(ws.cell(r, C_ICF).value) == velho, (r, ws.cell(r, C_ICF).value)
        ws.cell(r, C_ICF).value = novo
        ws.cell(r, C_ICF_N).value = 5
        ws.cell(r, C_ICF_C).value = f'[{HOJE} #1812] ' + CUNN_CIT.format(mix=mix, fck=38.2, dp=novo) + f'; o {velho} gravado era o DP dos 56 d (42.1 (3.3))'
        nota(ws, r, f'ic_fck corrigido {HOJE} (#1812): {velho} -> {novo}, o 3,3 era o DP dos 56 d na Tab.3; aos 28 d e 3,4')
        log.append((r, '3732', 'ic_fck corrigido', f'{velho}->{novo}'))
    # lote
    for r, (rid, p) in sorted(res.items()):
        if r in IGNORAR or rid == '3732':
            continue
        assert str(ws.cell(r, 1).value) == rid, (r, rid, ws.cell(r, 1).value)
        if p.get('ic_fck_valor') is not None and ws.cell(r, C_ICF).value in (None, ''):
            ws.cell(r, C_ICF).value = p['ic_fck_valor']
            ws.cell(r, C_ICF_T).value = TIPO.get(p['ic_fck_tipo'], p['ic_fck_tipo'])
            ws.cell(r, C_ICF_N).value = p.get('ic_fck_n')
            ws.cell(r, C_ICF_C).value = clean(f'[{HOJE} #1812] {p.get("ic_fck_citacao") or ""} | {p.get("nota") or ""}')[:900]
            n_f += 1
            log.append((r, rid, 'ic_fck', p['ic_fck_valor']))
        v = p.get('ic_co2_valor')
        if v is not None and ws.cell(r, C_ICC).value in (None, ''):
            ws.cell(r, C_ICC).value = v
            ws.cell(r, C_ICC_T).value = TIPO.get(p['ic_co2_tipo'], p['ic_co2_tipo'])
            ws.cell(r, C_ICC_N).value = p.get('ic_co2_n')
            ws.cell(r, C_ICC_C).value = clean(f'[{HOJE} #1812] {p.get("ic_co2_citacao") or ""} | {p.get("nota") or ""}')[:900]
            n_c += 1
            log.append((r, rid, 'ic_co2', v))
    for l in log:
        print(*l)
    print(f'ic_fck novos: {n_f} | ic_co2 novos: {n_c} | corrigidos: {len(CUNN_CORRIGIR)}')
    if gravar:
        wb.save(BASE)
        print('gravado', BASE)
    else:
        print('(simulacao; use --gravar)')


if __name__ == '__main__':
    main('--gravar' in sys.argv)
