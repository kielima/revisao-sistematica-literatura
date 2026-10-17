"""Recalcula as colunas ci e cit de dados_fck (meta_analysis_base.xlsx) a partir
de co2_kg_m3 (a coluna-base de todos os graficos de emissoes, 2026-09-26).

Definicoes (F22 e F24, Kie 2026-10-16):
    ci  [kg CO2-eq/(m3.MPa)]       = co2_kg_m3 / fck_mpa            (Damineli et al. 2010)
    cit [kg CO2-eq/(m3.MPa.ano)]   = ci / vida_util_anos
Sem vida util -> cit fica vazio; nunca se usa uma vida util convencionada.
O antigo ci_mpa (co2_kg_m3 x volume / fck, kg CO2-eq/MPa) foi removido do projecto na
F24 («Pode remover ci_mpa completamente, nao vou usar ele nem descritivo»); a col 38
passou a guardar o ci de Damineli.

Uso: python3 recalcular_ci.py   (grava por cima de meta_analysis_base.xlsx)
Correr sempre depois de mexer em co2_kg_m3, fck_mpa, vol_corpo_prova_m3 ou
vida_util_anos.
"""
import openpyxl

BASE = 'meta_analysis_base.xlsx'
C = dict(fck=8, vida=19, vida_ci_t=52, co2_kg_m3=37, ci=38, cit=39)  # F33: ci_t usa a vida da hierarquia (col 52)


def num(v):
    if isinstance(v, bool) or v is None:
        return None
    if isinstance(v, (int, float)):
        return float(v)
    try:
        return float(str(v).replace(',', '.'))
    except ValueError:
        return None


def main():
    wb = openpyxl.load_workbook(BASE)
    ws = wb['dados_fck']
    assert ws.cell(1, C['co2_kg_m3']).value == 'co2_kg_m3'
    assert ws.cell(1, C['ci']).value in ('ci_kgco2_mpa', 'ci_kgco2_m3_mpa')
    ws.cell(1, C['ci']).value = 'ci_kgco2_m3_mpa'   # F24: ci de Damineli no lugar do ci_mpa
    assert ws.cell(1, C['cit']).value in ('cit_kgco2_mpa_ano', 'cit_kgco2_m3_mpa_ano')
    ws.cell(1, C['cit']).value = 'cit_kgco2_m3_mpa_ano'   # F22: unidade kg/(m3.MPa.ano)
    n_ci = n_cit = 0
    for r in range(2, ws.max_row + 1):
        co2 = num(ws.cell(r, C['co2_kg_m3']).value)
        fck = num(ws.cell(r, C['fck']).value)
        vida = num(ws.cell(r, C['vida_ci_t']).value) or num(ws.cell(r, C['vida']).value)
        ci = cit = None
        if co2 is not None and fck:
            ci = co2 / fck
            n_ci += 1
            if vida:
                cit = ci / vida
                n_cit += 1
        ws.cell(r, C['ci']).value = ci
        ws.cell(r, C['cit']).value = cit
    wb.save(BASE)
    print(f'ci preenchido em {n_ci} linhas, cit em {n_cit}')


if __name__ == '__main__':
    main()
