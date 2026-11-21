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

# ---------------------------------------------------------------- 2684 HAFEZ 2024b: fck de projecto -> medido aos 28 d
# O fck gravado (40) e a classe de projecto C40/50 ("designed for a strength class of C40/50"); a Fig.3 p.5 da
# "The 28-day compressive strength results" por mistura, n=3 ("Three specimens were tested for each concrete
# mix"), e o texto confirma o LC3: "49.12 +/- 1.82 MPa". Precedente: fck de projecto trocado pelo medido
# (ALI 2951, OYEBISI 3132, BAYKARA 3731, KIM 2703 - CLAUDE.md 29/09 e 04/10). Medias lidas por pixel a 300 dpi
# (verificadas na imagem: 57 / 66 / 49 / 58), DP = meia-barra (a barra do LC3 medida 1,80 reproduz o 1,82 do texto).
HAFEZ_FCK = {  # sheet_row -> (fck gravado, fck medido 28 d, DP, mistura)
    135: (40, 56.8, 0.93, 'OPC'), 136: (40, 65.8, 0.29, 'OPC-SF'), 137: (40, 49.12, 1.82, 'LC3'), 138: (40, 57.9, 1.26, 'LC3-SF'),
}
HAFEZ_CIT = ('Fig.3 p.5 "Compressive strength results of unreinforced and steel fibre-reinforced OPC and LC3 concrete '
             'mixes" (28 d; texto: "The 28-day compressive strength results (Fig. 3)"), media {fck} e meia-barra {dp} MPa '
             'lidas por pixel a 300 dpi; n=3 ("Three specimens were tested for each concrete mix"); LC3 no texto: '
             '"49.12 +/- 1.82 MPa"; o texto chama "standard deviation" a dispersao dos ensaios')

# ---------------------------------------------------------------- 3187 YU 2022: DP contaminados de outro artigo
# Os DP gravados em 896/897/900 (3,89/2,91/2,98) e as citacoes ("Table 7, FA0SF0 92.36 +/- 3.89" etc.) NAO existem
# neste PDF (sem Tabela 7; 92.36/107.14/98.29 ausentes do texto) - conferido por mim no texto completo. Tabela 3
# (p.7) da fc aos 28 d como media +/- X (X nao definido nas notas da tabela); n por idade nao declarado
# ("720 cubes with a 100 mm edge length fabricated from 36 unique SCC mixes").
YU_FCK = {  # sheet_row -> (fck gravado, DP gravado ou None, +/- da Tabela 3, mistura)
    896: (53.5, 3.89, 3.6, 'M1 N0.3-0-0.3-20-C'), 897: (44.3, 2.91, 2.9, 'M2 N0.4-0-0.3-20-C'),
    898: (48.3, None, 3.2, 'M19 P0.4-0.5-0-20-C'), 899: (23.0, None, 1.3, 'M22 P0.4-0.5-0.6-20-C (Fase III)'),
    900: (52.4, 2.98, 3.7, 'M25 P0.4-0.5-0.3-90-C'),
}
YU_CIT = ('Tabela 3 p.7 "Workability, 28-days mechanical properties, and life cycle performance of SCC", coluna fc: '
          '{mix} {fck} +/- {dp}; o "+/-" nao e definido no artigo; n por idade nao declarado (720 cubos de 100 mm / 36 misturas)')

# ---------------------------------------------------------------- 2658 D'ORAZIO: texto numa coluna numerica
DORAZIO_LIMPAR = (631, 632, 633, 634)  # ic_co2_valor = 'NAO_TRANSCRITO' com tipo desvio_padrao -> limpar (sem DP do GWP total)

# ---------------------------------------------------------------- 3162 SPAGNUOLO 1935: tipo e n em falta
SPAG = {1935: ('desvio_padrao', 3)}


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
        if r in IGNORAR or rid in ('3732', '2684', '3187', '2658', '3162'):
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
    # HAFEZ: fck de projecto -> medido + DP
    for r, (velho, novo, dp, mix) in HAFEZ_FCK.items():
        assert str(ws.cell(r, 1).value) == '2684' and float(ws.cell(r, 8).value) == velho, (r, ws.cell(r, 8).value)
        ws.cell(r, 8).value = novo
        ws.cell(r, C_ICF).value = dp
        ws.cell(r, C_ICF_T).value = 'desvio_padrao'
        ws.cell(r, C_ICF_N).value = 3
        ws.cell(r, C_ICF_C).value = f'[{HOJE} #1812] ' + HAFEZ_CIT.format(fck=novo, dp=dp)
        nota(ws, r, f'fck corrigido {HOJE} (#1812, por confirmar): {velho} era a classe de projecto C40/50; passa ao medido aos 28 d '
                    f'da Fig.3 ({mix} {novo} MPa, n=3), precedente fck de projecto -> medido (ALI, OYEBISI, BAYKARA, KIM)')
        log.append((r, '2684', 'fck corrigido', f'{velho}->{novo}', 'ic_fck', dp))
        pco2 = res.get(r, (None, {}))[1]
        if pco2.get('ic_co2_valor') is not None and ws.cell(r, C_ICC).value in (None, ''):
            ws.cell(r, C_ICC).value = pco2['ic_co2_valor']
            ws.cell(r, C_ICC_T).value = 'barra_erro_nao_definida'
            ws.cell(r, C_ICC_N).value = None
            ws.cell(r, C_ICC_C).value = clean(f'[{HOJE} #1812] {pco2.get("ic_co2_citacao") or ""}')[:900]
            log.append((r, '2684', 'ic_co2', pco2['ic_co2_valor']))
    # YU: substituir DP contaminados e preencher os 2 em falta
    for r, (fck, velho, dp, mix) in YU_FCK.items():
        assert str(ws.cell(r, 1).value) == '3187' and float(ws.cell(r, 8).value) == fck, (r, ws.cell(r, 8).value)
        if velho is not None:
            assert float(ws.cell(r, C_ICF).value) == velho, (r, ws.cell(r, C_ICF).value)
            nota(ws, r, f'ic_fck corrigido {HOJE} (#1812): o {velho} e a citacao "Table 7 ..." nao existem neste artigo '
                        f'(contaminacao de outro PDF); Tabela 3 da {fck} +/- {dp}')
        ws.cell(r, C_ICF).value = dp
        ws.cell(r, C_ICF_T).value = 'barra_erro_nao_definida'
        ws.cell(r, C_ICF_N).value = None
        ws.cell(r, C_ICF_C).value = f'[{HOJE} #1812] ' + YU_CIT.format(mix=mix, fck=fck, dp=dp)
        log.append((r, '3187', 'ic_fck corrigido' if velho is not None else 'ic_fck', f'{velho}->{dp}' if velho is not None else dp))
    # D'ORAZIO
    for r in DORAZIO_LIMPAR:
        assert str(ws.cell(r, 1).value) == '2658' and str(ws.cell(r, C_ICC).value) == 'NAO_TRANSCRITO', (r, ws.cell(r, C_ICC).value)
        for c in (C_ICC, C_ICC_T, C_ICC_N, C_ICC_C):
            ws.cell(r, c).value = None
        nota(ws, r, f'ic_co2 limpo {HOJE} (#1812): a celula tinha o texto NAO_TRANSCRITO; o Monte Carlo do artigo so da '
                    f'distribuicoes por processo (Tabelas 7-8), nao do GWP total da argamassa')
        log.append((r, '2658', 'ic_co2 limpo', 'NAO_TRANSCRITO->vazio'))
    # SPAGNUOLO
    for r, (tipo, n) in SPAG.items():
        assert str(ws.cell(r, 1).value) == '3162' and float(ws.cell(r, C_ICF).value) == 1.99
        ws.cell(r, C_ICF_T).value = tipo
        ws.cell(r, C_ICF_N).value = n
        log.append((r, '3162', 'ic_fck tipo/n', f'{tipo}/{n}'))
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
