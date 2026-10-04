"""Mapeia as respostas da revarredura (resultado_loteNN.json) para a familia de cada par,
pelas regras D1-D8 de metanalise/DECISOES_METANALISE.md. Usado por aplicar.py."""
import glob
import json
import os

DIR = os.path.dirname(os.path.abspath(__file__))


def norm(v):
    return str(v or '').strip().lower()


def familia(p, co2_gravado=None):
    """Devolve (familia, motivo, revisao) para um par."""
    aco, lig, papel = norm(p.get('co2_inclui_aco')), norm(p.get('tipo_ligante')), norm(p.get('papel_material'))
    res, uhpc = norm(p.get('material_residuo')), norm(p.get('uhpc'))
    so = p.get('co2_so_betao')
    if aco == 'sim':
        return 'concreto_armado', 'D1 aco incluido e inseparavel', None
    if aco == 'separavel' and isinstance(so, (int, float)) and co2_gravado is not None and abs(so - co2_gravado) > 0.5:
        # o valor gravado ainda inclui o aco: fica em concreto_armado ate o valor ser trocado
        return 'concreto_armado', 'D1 separavel mas valor gravado ainda inclui aco', f'trocar CO2 {co2_gravado} -> {so}'
    if lig.startswith('alcali'):
        return 'geopolimero', 'D3 alcali-ativado', None
    if lig == 'madeira':
        return 'biobase', 'D5 madeira', None
    if lig in ('csa', 'magnesiano', 'gesso', 'polimero') or (lig and lig not in ('portland',) and lig != 'outro' and not lig.startswith('alcali')):
        return 'ligantes', f'D4 {lig}', None
    if lig == 'outro':
        return 'ligantes', 'D4 outro ligante sem Portland', 'confirmar ligante "outro"'
    if uhpc == 'sim':
        return 'uhpc', 'D6 UHPC declarado', None
    if papel == 'substituicao_ligante':
        return 'scm', 'D7 substitui cimento', None
    if papel in ('agregado', 'fibra') and res == 'sim':
        return 'reciclado', f'D7 residuo como {papel}', None
    if papel == 'outro' and res == 'sim':
        return 'opc', 'D8 (papel outro com residuo)', 'rever papel "outro" com residuo'
    if papel == 'ligante_alternativo':
        return 'opc', 'D8 ligante_alternativo mas tipo portland', 'rever: ligante_alternativo com tipo portland'
    return 'opc', 'D8 restante Portland', None


def carregar():
    out = {}
    for f in sorted(glob.glob(os.path.join(DIR, 'resultado_lote*.json'))):
        d = json.load(open(f, encoding='utf-8'))
        if isinstance(d, dict):
            d = d.get('estudos') or d.get('resultados') or next(v for v in d.values() if isinstance(v, list))
        for s in d:
            for p in s.get('pares', []):
                out[int(p['sheet_row'])] = dict(p, row_id=s.get('row_id'), lote=os.path.basename(f))
    return out
