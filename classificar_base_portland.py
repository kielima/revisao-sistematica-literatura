"""Classifica cada linha de dados_fck quanto a base do ligante: cimento Portland ou nao.

Pedido da Kie (2026-09-28): poder ver o painel kielima.com/metanalise so com
materiais de base cimento Portland, ou com tudo.

Escreve em meta_analysis_base.xlsx, aba dados_fck:
  col 40  base_portland       'sim' | 'nao' | 'misto'
  col 41  base_portland_nota  porque (regra aplicada ou decisao manual)

Definicao (2026-09-28):
  sim   = o ligante principal e cimento Portland / clinquer Portland, incluindo
          cimentos compostos (CEM II-V, CP II-IV), substituicao parcial por SCM
          (cinza volante, escoria, LC3, silica ativa...), UHPC, betao armado e
          betao com agregado reciclado, terra estabilizada com cimento.
  nao   = ligante sem clinquer Portland como ligante principal: geopolimero /
          alcali-ativado (incluindo hibridos em que o OPC e minoritario),
          sulfoaluminato de calcio (CSA), cimentos de magnesio (MPC, MOC, M-S-H),
          belite-ye'elimite, compositos de gesso, escoria carbonatada sem
          cimento, madeira estrutural, compositos polimericos sem cimento.
  misto = a linha junta tracos Portland e nao-Portland num unico valor e nao
          da para separar (fica fora da vista "so Portland").

Ordem: decisao manual por (row_id, inicio do material) > marcador alcalino no
material > outros ligantes nao-Portland no material > familia do
metanalise-export.py (geopolimero por titulo = nao; restantes = sim).

Correr depois de mexer em material/familia; e idempotente.
"""
import importlib.util
import re

import openpyxl

BASE = 'meta_analysis_base.xlsx'
COL_FLAG, COL_NOTA = 40, 41

spec = importlib.util.spec_from_file_location('mx', 'metanalise-export.py')
mx = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mx)

NAO_OUTROS = [
    (r'sulfoaluminat|\bkcsc\b', 'cimento de sulfoaluminato de calcio (CSA), sem clinquer Portland'),
    (r'magnesi|\bm-s-h\b|\bmpc\b|\bmoc\b', 'cimento de magnesio, sem clinquer Portland'),
    (r"belite-ye|\bbyc", "cimento belite-ye'elimite, sem clinquer Portland"),
    (r'glulam|madeira lamelada', 'madeira estrutural'),
    (r'policarbonato', 'composito areia-polimero, sem cimento'),
]

# (row_id, inicio do material) -> (flag, nota). Decisoes de 2026-09-28 sobre
# linhas ambiguas (material com varios tracos, codigos opacos, hibridos).
MANUAL = {
    (2653, 'Bloco carbonatado'): ('nao', 'escoria de aco inoxidavel endurecida por carbonatacao, sem cimento'),
    (3105, 'ASS'): ('nao', 'escoria artificial ativada com sodio (Na2O), sem cimento Portland'),
    (3162, 'Aduela CSA/GFRP'): ('nao', 'betao A-CSA-CEM II: ligante principal sulfoaluminato (CSA)'),
    (3413, 'argamassa hibrida'): ('nao', 'cimento hibrido alcali-ativado de cinza volante (OPC minoritario)'),
    (4455, 'composto GCP'): ('nao', 'composito gesso-cimento-pozolana: ligante principal gesso'),
    (5012, 'Concreto base cimento Portland vs'): ('sim', 'o valor gravado (286,37) e o do concreto tradicional CPII-Z'),
    (4027, 'Concreto OPC 50 MPa vs'): ('sim', 'o valor gravado (517) e o do concreto OPC; o geopolimero tem linha propria'),
    (4026, 'Concreto OPC 50 MPa vs'): ('nao', 'o valor gravado (364) e o do geopolimero (GPC, MU-hLCA)'),
    (3099, 'geopolymer concrete auto-reparavel'): ('sim', 'o valor gravado (454,59) e o do OPCC de referencia'),
    (3225, 'argamassa de baixo carbono'): ('sim', 'o valor gravado (611,7) e o da argamassa PC'),
    (2966, 'Betao Portland Tipo I (C0-C100) e geopolimero'): ('misto', 'linha junta 8 tracos Portland e geopolimero num valor lido no grafico'),
    (3095, 'Ligantes puros'): ('misto', 'linha junta ligantes cimenticios e alcali-ativados (sem par valido)'),
}


def classificar(row_id, material, titulo):
    mat = material or ''
    for (rid, pref), res in MANUAL.items():
        if rid == row_id and mat.startswith(pref):
            return res[0], 'manual: ' + res[1]
    # 2026-10-04: a revarredura das familias (leitura integral, lotes_familia/) responde ao tipo de ligante de
    # cada par -- tem precedencia sobre as regex do material (que apanhavam "geopolimero" em descricoes de
    # tracos Portland de referencia).
    rev = mx.FAMILIA_REVARREDURA.get(f'{row_id}|{material}')
    if rev in ('geopolimero', 'ligantes', 'biobase'):
        return 'nao', f'revarredura 2026-10-04: familia {rev} (sem clinquer Portland como ligante principal)'
    if rev:
        return 'sim', f'revarredura 2026-10-04: ligante de cimento Portland (familia {rev})'
    m = mx._fold(mat)
    if re.search(mx.ALKALI, m):
        return 'nao', 'geopolimero / alcali-ativado (sem clinquer Portland como ligante principal)'
    for pat, nota in NAO_OUTROS:
        if re.search(pat, m):
            return 'nao', nota
    fam = mx.classify(row_id, material, titulo)
    if fam == 'geopolimero':
        return 'nao', 'familia geopolimero (artigo de geopolimero, traco sem marcador Portland)'
    if fam == 'outros':
        # familia nao reconhecida pelo exportador (linhas fora do grafico):
        # decide-se so pelo material
        if re.search(r'madeira|timber|wood|\bclt\b|pedra natural|stone|soil-steel', m):
            return 'nao', 'material nao cimenticio (madeira, pedra, solo-aco)'
        if re.search(r'\bcem [iv]|cimento|cement|concret|\bscc\b|\becc\b|frscc|\bsh-ecc\b', m):
            return 'sim', 'ligante de cimento Portland (material sem familia no exportador)'
        return None, None
    return 'sim', f'ligante de cimento Portland (familia {fam})'


def main():
    wb = openpyxl.load_workbook(BASE)
    ws = wb['dados_fck']
    ws.cell(1, COL_FLAG).value = 'base_portland'
    ws.cell(1, COL_NOTA).value = 'base_portland_nota'
    cont = {}
    for r in range(2, ws.max_row + 1):
        if ws.cell(r, 1).value is None:
            continue
        flag, nota = classificar(ws.cell(r, 1).value, ws.cell(r, 7).value, ws.cell(r, 3).value)
        ws.cell(r, COL_FLAG).value = flag
        ws.cell(r, COL_NOTA).value = nota
        cont[flag] = cont.get(flag, 0) + 1
    wb.save(BASE)
    print(cont)


if __name__ == '__main__':
    main()
