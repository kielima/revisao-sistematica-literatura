"""Subfamilia do cimento (F12, Kie 2026-10-10) a partir da designacao e da norma escritas no artigo.

Le lotes_cimento/resultado_lote*.json (releitura integral) e devolve, por sheet_row,
(ligante, subfamilia, designacao, norma). Regras por ordem; a designacao manda sobre a norma.
"""
import glob
import json
import re

SUB = [
    # (codigo, regex sobre 'designacao | norma')
    ('cp_v_ari', r'\bCP[\s-]*V\b|ARI\b'),
    ('cp_iv', r'\bCP[\s-]*IV\b'),
    ('cp_iii', r'\bCP[\s-]*III\b'),
    ('cp_ii_e', r'\bCP[\s-]*II[\s-]*E\b(?!\s*e\s*CP)'),
    ('cp_ii_z', r'\bCP[\s-]*II[\s-]*Z\b'),
    ('cp_ii_f', r'\bCP[\s-]*II[\s-]*F\b'),
    ('cp_ii', r'\bCP[\s-]*II\b'),
    ('cp_i', r'\bCP[\s-]*I\b|\bCPI\b'),
    ('cem_v', r'\bCEM\s*V\b'),
    ('cem_iv', r'\bCEM\s*IV\b'),
    ('cem_iii', r'\bCEM\s*III\b|CEMIII'),
    ('cem_ii_b', r'\bCEM\s*II\s*/\s*B'),
    ('cem_ii_a', r'\bCEM\s*II\s*/\s*A|CEM II/A'),
    ('cem_ii', r'\bCEM\s*II\b|CEMII'),
    ('cem_i', r'\bCEM\s*(I|1)\b'),
    ('is_opc_grau', r'\b(33|43|53)\s*grade|grade\s*(33|43|53)|IS\s*(269|8112|12269)'),
    ('astm_il', r'Type\s*IL\b|\bPLC\b|limestone cement'),
    ('astm_c1157', r'C1157|\bGU\b|\bHE\b|type UG|INEN 2380'),
    ('csa_a3001', r'CSA A3001|GUb'),
    ('astm_type_ii_v', r'II\s*/\s*V'),
    ('astm_type_i_ii', r'I\s*/\s*II'),
    ('astm_type_ii', r'type\s*II\b|type II PC|Commercial type II'),
    ('astm_type_i', r'type\s*(I|1)\b'),
    ('astm_c150', r'ASTM C150'),
    ('nc_cuba', r'NC-9[56]'),
    ('gb_po', r'P\s*[·.]?\s*O\b|\bPO\s*\d|P\s*[·.]?\s*I\s*52'),
    ('as_gp', r'\bGP\b|General[- ]purpose|AS(/NZS)?\s*3972'),
    ('branco', r'white cement|branco'),
]
CODES = [c for c, _ in SUB]


def classifica(lig, des, norma):
    if lig == 'indeterminado':
        return 'nao_declarado'
    if lig != 'cimento_comercial':
        return None
    t = f"{des or ''} | {norma or ''}"
    if re.search(r'CP[\s-]*II[\s-]*E\s*(e|/)\s*CP[\s-]*II[\s-]*F', t, re.I):
        return 'cp_ii'  # o artigo junta CP II-E e CP II-F sem os separar
    for code, rx in SUB:
        if re.search(rx, t, re.I):
            return code
    return 'portland_sem_tipo'


def carrega():
    out = {}
    for f in sorted(glob.glob('lotes_cimento/resultado_lote*.json')):
        d = json.load(open(f, encoding='utf-8'))
        if isinstance(d, dict):
            d = d.get('estudos') or d.get('resultados') or next(v for v in d.values() if isinstance(v, list))
        for s in d:
            for p in s['pares']:
                lig = p.get('ligante')
                out[int(p['sheet_row'])] = dict(ligante=lig, subfamilia=classifica(lig, p.get('cimento_designacao'), p.get('norma_cimento')),
                                                designacao=p.get('cimento_designacao'), norma=p.get('norma_cimento'),
                                                citacao=p.get('citacao'), nota=p.get('nota'), row_id=s.get('row_id'))
    return out


if __name__ == '__main__':
    import collections
    r = carrega()
    c = collections.Counter(v['subfamilia'] for v in r.values())
    for k, v in c.most_common():
        print(v, k)
