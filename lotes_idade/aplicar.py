"""Aplica os resultados dos lotes de idade do ensaio a dados_fck (col 10 idade_dias).

2026-10-04. Regras:
  - so preenche idade_dias quando a celula esta vazia (nunca apaga valor gravado);
  - so grava idade quando o subagente a encontrou ('ensaio' ou 'classe_28d_declarada');
    'classe_sem_idade' e 'nao_declarada' ficam vazias, so com a nota;
  - acrescenta a observacoes (col 13) um carimbo com o tipo e a citacao;
  - SOBREPOR / IGNORAR: correcoes da auditoria pessoal aos resultados dos lotes.
Correr da raiz do repo.
"""
import glob
import json
import re

import openpyxl

BASE = 'meta_analysis_base.xlsx'
COL_ROWID, COL_FCK, COL_IDADE, COL_OBS = 1, 8, 10, 13

# sheet_row -> (idade_dias|None, tipo, citacao) que substitui o resultado do lote
SOBREPOR = {}
IGNORAR = set()  # sheet_rows cujo resultado nao se aplica


def clean_str(s):
    return re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', str(s))


def sem_acentos(s):
    import unicodedata
    return ''.join(c for c in unicodedata.normalize('NFKD', s) if not unicodedata.combining(c))


def main():
    res = {}
    for f in sorted(glob.glob('lotes_idade/resultado_lote*.json')):
        for art in json.load(open(f, encoding='utf-8')):
            for p in art['pares']:
                res[int(p['sheet_row'])] = (str(art['row_id']), p)
    wb = openpyxl.load_workbook(BASE)
    ws = wb['dados_fck']
    gravadas = vazias = ja = 0
    for r, (rid, p) in sorted(res.items()):
        if r in IGNORAR:
            continue
        idade, tipo, cit = p.get('idade_dias'), p.get('tipo'), p.get('citacao') or ''
        if r in SOBREPOR:
            idade, tipo, cit = SOBREPOR[r]
        assert str(ws.cell(r, COL_ROWID).value) == rid, (r, rid, ws.cell(r, COL_ROWID).value)
        if ws.cell(r, COL_IDADE).value not in (None, ''):
            ja += 1
            continue
        if idade is not None and tipo in ('ensaio', 'classe_28d_declarada'):
            ws.cell(r, COL_IDADE).value = int(idade)
            gravadas += 1
        else:
            vazias += 1
        carimbo = clean_str(sem_acentos(f'[idade 2026-10-04: {tipo}; {cit}]'))[:400]
        obs = ws.cell(r, COL_OBS).value
        ws.cell(r, COL_OBS).value = f'{obs} {carimbo}' if obs else carimbo
    wb.save(BASE)
    print(f'gravadas {gravadas} | sem idade {vazias} | ja preenchidas {ja} | total {len(res)}')


if __name__ == '__main__':
    main()
