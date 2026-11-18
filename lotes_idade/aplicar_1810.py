"""#1810 (2026-11-18): aplica a dados_fck (col 10 idade_dias) os resultados dos lotes 20 e 21 de idade do ensaio.

Sao os 16 estudos (45 pares do painel) que entraram no painel DEPOIS da ronda de 2026-10-04
(F11-F18: elementos convertidos, F14/F17 pares novos) e por isso nunca tinham sido lidos para a idade.
Mesmas regras do lotes_idade/aplicar.py de 04/10:
  - so preenche idade_dias quando a celula esta vazia (nunca apaga valor gravado);
  - so grava idade quando o subagente a encontrou ('ensaio' ou 'classe_28d_declarada');
    'classe_sem_idade' e 'nao_declarada' ficam vazias, so com a nota;
  - acrescenta a observacoes (col 13) o carimbo [idade 2026-11-18 (#1810): tipo; citacao];
  - SOBREPOR / IGNORAR: correcoes da auditoria pessoal aos resultados dos lotes.
Nao reexecuta o desdobramento SPOSITO nem as correccoes de 04/10 (ja em main).
Correr da raiz do repo: /usr/bin/python3 lotes_idade/aplicar_1810.py [--gravar]
"""
import json
import re
import sys
import unicodedata

import openpyxl

BASE = 'meta_analysis_base.xlsx'
LOTES = ['lotes_idade/resultado_lote20.json', 'lotes_idade/resultado_lote21.json']
COL_ROWID, COL_IDADE, COL_OBS = 1, 10, 13
CARIMBO = '[idade 2026-11-18 (#1810): {tipo}; {cit}]'

# Auditoria pessoal (2026-11-18):
#  - 4297 PUSHKAR l.1264: o artigo imprime «C 20/25» (dataset Ecoinvent, Tab.5) para os pilares «C20» -- notacao
#    Cxx/yy da EN 206, que define a classe aos 28 d -> regra da notacao de norma (decisao da Kie, 2026-10-04,
#    lotes_idade/aplicar_notacao.py). O subagente deixou classe_sem_idade por falta de norma citada.
SOBREPOR = {   # sheet_row -> (idade|None, tipo, citacao)
    1264: (28, 'classe_28d_notacao', 'Tab.5 p.11 dataset Ecoinvent «C 20/25» para os pilares C20 -- notacao Cxx/yy da EN 206, '
                                     'regra da notacao de norma (Kie 2026-10-04); sem norma citada e sem «28 d» no texto'),
}
IGNORAR = set()


def clean_str(s):
    return re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', str(s))


def sem_acentos(s):
    return ''.join(c for c in unicodedata.normalize('NFKD', s) if not unicodedata.combining(c))


def main(gravar):
    res = {}
    for f in LOTES:
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
        obs = ws.cell(r, COL_OBS).value or ''
        if '[idade 2026-11-18 (#1810)' in obs:
            ja += 1
            continue
        if idade is not None and tipo in ('ensaio', 'classe_28d_declarada', 'classe_28d_notacao'):
            ws.cell(r, COL_IDADE).value = int(idade)
            gravadas += 1
        else:
            vazias += 1
        carimbo = clean_str(sem_acentos(CARIMBO.format(tipo=tipo, cit=cit)))[:400]
        ws.cell(r, COL_OBS).value = f'{obs} {carimbo}'.strip()
        print(f'{r:5d} {rid} {str(idade):>5} {tipo}')
    print(f'gravadas {gravadas} | sem idade {vazias} | ja preenchidas/carimbadas {ja} | total {len(res)}')
    if gravar:
        wb.save(BASE)
        print('gravado em', BASE)
    else:
        print('(ensaio; use --gravar para escrever)')


if __name__ == '__main__':
    main('--gravar' in sys.argv)
