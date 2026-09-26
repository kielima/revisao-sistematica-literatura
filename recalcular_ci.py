"""Recalcula as colunas ci e cit de dados_fck (meta_analysis_base.xlsx) a partir
de co2_kg_m3 (a coluna-base de todos os graficos de emissoes, 2026-09-26).

Definicoes (PROTOCOLO_CI_MPA_2026-09-08.md):
    ci  [kg CO2-eq/MPa]        = co2_kg_m3 x vol_corpo_prova_m3 / fck_mpa
    cit [kg CO2-eq/(MPa.ano)]  = ci / vida_util_anos
Sem volume (vol_corpo_prova_fonte=indisponivel) -> ci e cit ficam vazios;
sem vida util -> so cit fica vazio. Nunca se usa um volume ou vida util
convencionados.

Uso: python3 recalcular_ci.py   (grava por cima de meta_analysis_base.xlsx)
Correr sempre depois de mexer em co2_kg_m3, fck_mpa, vol_corpo_prova_m3 ou
vida_util_anos.
"""
import openpyxl

BASE = 'meta_analysis_base.xlsx'
C = dict(fck=8, vida=19, vol=23, co2_kg_m3=37, ci=38, cit=39)


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
    assert ws.cell(1, C['ci']).value == 'ci_kgco2_mpa'
    assert ws.cell(1, C['cit']).value == 'cit_kgco2_mpa_ano'
    n_ci = n_cit = 0
    for r in range(2, ws.max_row + 1):
        co2 = num(ws.cell(r, C['co2_kg_m3']).value)
        fck = num(ws.cell(r, C['fck']).value)
        vol = num(ws.cell(r, C['vol']).value)
        vida = num(ws.cell(r, C['vida']).value)
        ci = cit = None
        if co2 is not None and fck and vol:
            ci = co2 * vol / fck
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
