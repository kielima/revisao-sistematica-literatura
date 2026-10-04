"""Aplica a revarredura das familias e do betao armado (2026-10-04) ao painel e ao modelo.

1. Le as respostas dos 43 lotes (resultado_loteNN.json) e mapeia cada par para uma familia pelas
   regras D1-D8 de metanalise/DECISOES_METANALISE.md (mapear.py), com os ajustes manuais de MANUAL.
2. Grava lotes_familia/familias_revarredura.json  {"row_id|material": familia}, que o
   metanalise-export.py consulta antes do OVERRIDE antigo e das regex.
3. Regista cada mudanca em lotes_familia/MUDANCAS_FAMILIA_2026-10-04.csv.
Correr da raiz do repo DEPOIS de lotes_familia/aplicar_valores.py.
"""
import csv
import glob
import importlib.util
import json
import os
import sys

import openpyxl

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import aplicar_valores  # noqa: E402
import mapear  # noqa: E402

spec = importlib.util.spec_from_file_location('mexp', 'metanalise-export.py')
mexp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mexp)

SAIDA = 'lotes_familia/familias_revarredura.json'
LOG = 'lotes_familia/MUDANCAS_FAMILIA_2026-10-04.csv'

# sheet_row -> (familia, motivo). Ajustes onde as quatro respostas nao chegam (decisoes minhas, por confirmar).
MANUAL = {}
for r in range(1891, 1903):  # 2827 ZHANG 2023e: tubos/flowlines/umbilicais desmantelados embebidos no betao
    MANUAL[r] = ('reciclado', 'D7: componente petrolifero desmantelado embebido (residuo que substitui volume de betao)')
MANUAL[247] = ('reciclado', 'D7: cinza de cal da industria de papel substitui o filer calcario natural (nao o cimento)')


def main():
    res = mapear.carregar()
    wl = {}
    for f in glob.glob('lotes_familia/lote[0-9]*.json'):
        for s in json.load(open(f, encoding='utf-8')):
            for p in s['pares']:
                wl[p['sheet_row']] = (s['row_id'], p)
    ws = openpyxl.load_workbook(mexp.BASE, read_only=True)['dados_fck']
    linhas = {r: row for r, row in enumerate(ws.iter_rows(min_row=1, values_only=True), start=1)}
    corrigidas = set(aplicar_valores.CO2)
    fam_map, log, conflitos = {}, [], []
    for r, p in sorted(res.items()):
        row = linhas[r]
        rid, material = row[0], row[6]
        co2 = mexp.tofloat(row[36])
        if r in MANUAL:
            fam, motivo = MANUAL[r]
            rev = None
        else:
            # linhas ja corrigidas para o valor so do betao: o gravado ja nao inclui aco
            fam, motivo, rev = mapear.familia(p, None if r in corrigidas else co2)
        antes = mexp.classify(rid, material, row[2])
        key = f'{rid}|{material}'
        if key in fam_map and fam_map[key] != fam:
            conflitos.append((key, fam_map[key], fam))
        fam_map[key] = fam
        if fam != antes or rev:
            log.append({'sheet_row': r, 'row_id': rid, 'material': str(material)[:120], 'familia_antes': antes,
                        'familia_nova': fam, 'regra': motivo, 'a_rever': rev or '', 'lote': p['lote']})
    if conflitos:
        raise SystemExit(f'conflitos de familia no mesmo (row_id, material): {conflitos[:5]}')
    with open(SAIDA, 'w', encoding='utf-8') as f:
        json.dump(fam_map, f, ensure_ascii=False, indent=0, sort_keys=True)
    with open(LOG, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(log[0]))
        w.writeheader()
        w.writerows(log)
    sem = set(wl) - set(res)
    print(f'{len(res)} pares mapeados, {len(log)} mudancas/alertas, sem resposta: {len(sem)}')


if __name__ == '__main__':
    main()
