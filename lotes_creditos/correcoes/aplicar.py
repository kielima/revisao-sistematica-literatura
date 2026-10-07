"""Aplica as correccoes de valor de CO2 verificadas pessoalmente (2026-10-07).

Pedido da Kie (2026-10-07): «corrigir os valores de CO2 errados que a releitura encontrou».
Fonte: lotes_creditos/correcoes/verificadas.json (cada caso conferido no PDF; ver PROMPT.md).
Escreve em meta_analysis_base.xlsx (aba dados_fck): 37 co2_kg_m3 (e 14 co2_valor), 44 com desconto,
23 volume, 8 fck, 36 co2_conversao (NAO CONVERTIDO), 13 observacoes; e a familia em
lotes_familia/familias_revarredura.json quando muda. Correr depois: recalcular_ci.py,
classificar_base_portland.py, metanalise/preparar_dados.py, exportacao.
"""
import json
import re

import openpyxl

HOJE = '2026-10-07'
V = json.load(open('lotes_creditos/correcoes/verificadas.json', encoding='utf-8'))
FAM = 'lotes_familia/familias_revarredura.json'


def clean(s):
    return re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', str(s))


def main():
    wb = openpyxl.load_workbook('meta_analysis_base.xlsx')
    ws = wb['dados_fck']
    fam = json.load(open(FAM, encoding='utf-8'))
    n = 0
    for r, c in sorted(V.items(), key=lambda x: int(x[0])):
        r = int(r)
        obs = ws.cell(r, 13).value or ''
        antes = ws.cell(r, 37).value
        if c.get('co2') == 'NAO':
            ws.cell(r, 37).value = None
            ws.cell(r, 44).value = None
            ws.cell(r, 36).value = clean(f'NAO CONVERTIDO - {c["motivo"]}')[:1500]
            obs = f'{obs} [CO2 {antes} -> NAO CONVERTIDO {HOJE} (verificacao pessoal): {c["motivo"]}]'
        elif 'co2' in c:
            ws.cell(r, 37).value = c['co2']
            ws.cell(r, 14).value = c['co2']
            ws.cell(r, 44).value = c.get('com')
            if c.get('com') is not None:
                ws.cell(r, 45).value = ws.cell(r, 45).value if ws.cell(r, 45).value not in (None, 'nenhum') else 'carbonatacao'
                ws.cell(r, 47).value = 'sim'
            ws.cell(r, 36).value = clean(f'correcao {HOJE}: {c["motivo"]}')[:1500]
            obs = f'{obs} [CO2 {antes} -> {c["co2"]} {HOJE} (verificacao pessoal): {c["motivo"]}]'
        else:
            obs = f'{obs} [{HOJE} verificacao pessoal: {c.get("motivo") or c.get("nota")}]'
        if 'vol' in c:
            ws.cell(r, 23).value = c['vol']
        if 'fck' in c:
            obs = f'{obs} [fck {ws.cell(r, 8).value} -> {c["fck"]} {HOJE}]'
            ws.cell(r, 8).value = c['fck']
        if 'familia' in c:
            k = f'{ws.cell(r, 1).value}|{ws.cell(r, 7).value}'
            fam[k] = c['familia']
        ws.cell(r, 13).value = clean(obs.strip())
        n += 1
    wb.save('meta_analysis_base.xlsx')
    json.dump(fam, open(FAM, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print(n, 'linhas')


if __name__ == '__main__':
    main()
