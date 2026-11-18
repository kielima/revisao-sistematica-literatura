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

# Pares fora dos lotes 20/21, lidos pessoalmente no PDF (2026-11-18): 3112 HUSSAIN (Cleaner Waste Systems 11, 100278)
# tinha na col 10 o texto '28/56/91 (por mistura, ver fck_mpa)'. Sec.4.1 do artigo: M3 «achieved a compressive strength of
# 40.6 MPa at 28 days», M4 «42.2 MPa at 28 days» = os fck gravados (ensaio proprio aos 28 d). O betao de referencia
# e «a 35 MPa cement concrete … designed for similar mechanical properties» (resumo e sec.5.1): resistencia de projecto
# solta em MPa, sem idade e sem norma -> classe_sem_idade.
LIMPAR = {843}  # celulas cujo texto legado deve ser apagado (o painel lia o numero inicial como idade)
EXTRA = {  # sheet_row: (row_id, idade|None, tipo, citacao)
    # a celula 843 fica VAZIA (LIMPAR): o texto legado '28/56/91 (...)' era lido pelo painel (tofloat) como 28 d.
    843:  ('3112', None, 'classe_sem_idade', 'Resumo e sec.5.1: «compares them with a 35 MPa cement concrete … designed for '
                                             'similar mechanical properties»; valor solto em MPa, sem idade nem norma'),
    2097: ('3112', 28, 'ensaio', 'Sec.4.1 p.6: «Mix M3 … achieved a compressive strength of 40.6 MPa at 28 days and … 55.9 MPa at 91 days»'),
    2098: ('3112', 28, 'ensaio', 'Sec.4.1 p.6: «mix M4 … achieved a compressive strength of 42.2 MPa at 28 days and 65.1 MPa at 91 days»'),
}


def _numero(v):
    try:
        float(str(v).replace(',', '.'))
        return True
    except ValueError:
        return False


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
    for r, (rid, idade, tipo, cit) in EXTRA.items():
        res[r] = (rid, {'sheet_row': r, 'idade_dias': idade, 'tipo': tipo, 'citacao': cit + ' [leitura pessoal 2026-11-18]'})
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
        atual = ws.cell(r, COL_IDADE).value
        if atual not in (None, '') and _numero(atual):
            ja += 1
            continue
        # texto legado na celula ('nao informado', 'nao especificado'...): o painel (tofloat) ja o le como vazio;
        # fica no carimbo e a celula recebe o numero quando o ha, senao mantem o texto.
        legado = f" (celula tinha o texto '{atual}')" if atual not in (None, '') else ''
        obs = ws.cell(r, COL_OBS).value or ''
        if '[idade 2026-11-18 (#1810)' in obs:
            if r in LIMPAR and atual not in (None, ''):
                ws.cell(r, COL_IDADE).value = None
                print(f'{r:5d} {rid} celula limpa (texto legado {atual!r})')
            ja += 1
            continue
        if idade is not None and tipo in ('ensaio', 'classe_28d_declarada', 'classe_28d_notacao'):
            ws.cell(r, COL_IDADE).value = int(idade)
            gravadas += 1
        else:
            vazias += 1
            if r in LIMPAR:
                ws.cell(r, COL_IDADE).value = None
        carimbo = clean_str(sem_acentos(CARIMBO.format(tipo=tipo, cit=cit + legado)))[:450]
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
