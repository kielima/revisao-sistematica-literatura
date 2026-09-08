"""Exporta dados_fck (meta_analysis_base.xlsx) para o dataset compacto usado em
kielima.com/metanalise (public/assets/metanalise.js no repositório kielima-site).

Uso:
    python3 metanalise-export.py > metanalise_compact.json

Cada ponto exportado é [fck_MPa, co2_kg_m3, categoria_1_letra, estrato_1_letra].
Filtra a pares comparáveis por m3 (exclui totais de estrutura inteira, que nao
tem a mesma unidade de analise) e classifica o material por palavras-chave no
campo `material`+`titulo`, com um dicionario OVERRIDE por row_id para os casos
que nao seguem um padrao regex generico (julgamento caso a caso feito sobre a
amostra completa dos 381 materiais que caiam em "outros" ate 2026-09-08 -- ver
CLAUDE.md / conversa da sessao 2026-09-08: a Kie pediu para zerar "outros",
classificando cada um na familia certa e confirmando que agregado de pneu
triturado entra em "reciclado").

Depois de gerar o JSON, injectar manualmente em public/assets/metanalise.js
(substituir o array `var DATA = [...]`) e reconferir os textos que citam
contagens (KPI de pares, tier-n-p/tier-n-s) no mesmo ficheiro.
"""
import json
import re
import sys

import openpyxl

BASE = 'meta_analysis_base.xlsx'

CATCODE = {
    'geopolimero': 'g', 'uhpc': 'u', 'scm': 's', 'reciclado': 'r', 'opc': 'o',
    'ligantes': 'l', 'alvenaria': 'a', 'biobase': 'b',
}
TIERCODE = {'principal': 'p', 'sensibilidade': 's'}

# Domínio "plausível" por m³ de material -- exclui totais de estrutura inteira
# (edifício, ponte), que aparecem em kg absolutos muito acima da escala por m³
# e não são a mesma unidade de análise dos demais pares.
FCK_MIN, FCK_MAX = 1, 300
CO2_MIN, CO2_MAX = -1000, 5000

# Overrides explicitos pela linha da folha dados_fck (NAO o row_id da coluna
# 1, que referencia articles_final.xlsx -- este dict foi construido sobre o
# indice de iteracao da folha, ver classify_v2.py da sessao 2026-09-08), para
# os casos que nao seguem um padrao regex generico (julgamento caso a caso
# sobre a amostra completa dos 381 materiais que caiam em "outros" ate
# 2026-09-08).
OVERRIDE = {}

# --- ligantes alternativos (nao-OPC, nao-geopolimero: quimica de ligante distinta)
for r in [143, 144, 167, 620, 622, 624, 626, 647, 648, 649, 650, 713, 714, 1022, 1023, 1024, 1025, 1026,
          1047, 1048, 1049, 1050, 1173, 1174, 1945, 1946]:
    OVERRIDE[r] = 'ligantes'

# --- bio-base (materiais organicos/agricolas como componente principal do estudo)
for r in [338, 521, 522, 523, 524, 607, 919, 651, 1184]:
    OVERRIDE[r] = 'biobase'

# --- alvenaria (unidades de alvenaria: tijolo, bloco, painel -- nao concreto moldado)
for r in [322, 323, 347, 348, 350, 360, 1424, 1425, 1426, 1427, 1428]:
    OVERRIDE[r] = 'alvenaria'

# --- reciclado (residuo/agregado reciclado -- inclui agregado de pneu
# triturado, confirmado pela Kie 2026-09-08; e-waste, vidro moido como
# agregado, residuo de mina, residuo de pa de turbina eolica)
for r in [174, 370, 371, 372, 373, 451, 452, 453, 454, 455, 483, 484, 485, 486, 487, 570, 571, 572, 573, 574, 575,
          630, 631, 632, 633, 634, 635, 638, 926, 927, 928, 929, 930, 931, 932, 933, 960, 980, 981, 1043, 1093,
          1188, 1267, 1292, 1293, 1316, 1320, 1351, 1430, 1431, 1432, 1433, 1434, 1677, 1678, 1679, 1680, 1681,
          1682, 1683, 1684, 1685, 1686, 1687, 1688, 1689, 1690, 1691, 1692, 1693, 1694, 1695, 1696, 1824, 1825,
          1851, 1943, 1182, 1183]:
    OVERRIDE[r] = 'reciclado'

# --- scm (pozolana/cimento composto -- substitui CIMENTO, nao agregado)
for r in [331, 389, 390, 423, 424, 425, 906, 907, 908, 1000, 1263, 1572, 1573, 1613, 1614, 1615, 1616, 1617,
          1618, 1619, 1620, 1621, 1622, 1953, 1106, 1107, 1108]:
    OVERRIDE[r] = 'scm'

# --- ronda final (residuo classificado por leitura directa, sem padrao regex generico)
for r in [82, 83, 85, 87, 180, 181, 182, 184, 646, 699, 700, 701, 702, 703, 1707, 1708, 1709, 1710, 1730, 1731,
          1853, 1855, 1854]:
    OVERRIDE[r] = 'opc'


def classify(sheet_row, material, titulo):
    if sheet_row in OVERRIDE:
        return OVERRIDE[sheet_row]
    t = ((material or '') + ' ' + (titulo or '')).lower()
    if re.search(r'geopolim|geopolym|alcali[- ]ativad|alkali[- ]activ|\bAAM\b|\bAAC\b', t):
        return 'geopolimero'
    if re.search(r'\buhpc\b|\buhpfrc\b|ultra[- ]high[- ]performance|ultra[- ]alta[- ]resist', t):
        return 'uhpc'
    if re.search(
        r'reciclad|recycled aggregate|\brca\b|residuo de construcao|'
        r'construction (and demolition )?waste|\brcd\b|debris aggregate|\bgcba\b|\bcba\b|'
        r'e-waste|residuo de mina|residuo de pa de turbina|'
        r'vidro (triturado|moido) como agregado|concreto existente reutilizado',
        t,
    ):
        return 'reciclado'
    if re.search(
        r'cinza volante|fly ash|escoria|slag|silica ativa|silica fume|metacaulim|metakaolin|'
        r'argila calcinada|calcined clay|pozolan|pozzolan|\blc3\b|\bscm\b|\bggbs\b|\bggbfs\b|'
        r'cinza co-queimada|co-fired ash|cinza de casca de arroz|rice husk ash|'
        r'residuo de po de ceramica|\bcwp\b|po de vidro|glass powder|palm oil clinker|\bpoc\b',
        t,
    ):
        return 'scm'
    if re.search(r'\balvenaria\b|masonry|\btijolo', t):
        return 'alvenaria'
    # Referencia/OPC: nome explicito OU classe normativa de concreto convencional
    # (europeia C##/##, espanhola HA-##) OU descricao generica "concreto armado/estrutural"/
    # "betao"/"concreto"/"argamassa" -- a maioria dos concretos convencionais no banco
    # esta descrita assim, nao por "OPC"/"portland".
    if re.search(r'\bopc\b|portland|\breferencia\b|\bcontrole\b|\bcontrolo\b|convencional|conventional concrete', t):
        return 'opc'
    if re.search(r'\bc\d{2}\s*/?\s*\d{0,2}\b|\bha[- ]?\d{2}\b', t):
        return 'opc'
    if re.search(
        r'\bconcreto (armado|estrutural)\b|\bbetao\b|\bconcreto\b|\bbeton\b|'
        r'ready-?mix|usinado|pronto|pre-?fabricad|pre-?moldad|precast',
        t,
    ):
        return 'opc'
    if re.search(r'\bargamassa\b|\bmortar\b|\bpasta\b', t):
        return 'opc'
    return 'outros'


def tofloat(v):
    if v is None:
        return None
    if isinstance(v, (int, float)):
        return float(v)
    s = str(v).strip().replace(',', '.')
    m = re.search(r'-?\d+\.?\d*', s)
    return float(m.group()) if m else None


def main():
    wb = openpyxl.load_workbook(BASE)
    ws = wb['dados_fck']

    compact = []
    for r in range(2, ws.max_row + 1):
        row_id = ws.cell(r, 1).value
        titulo = ws.cell(r, 3).value
        material = ws.cell(r, 7).value
        fck = tofloat(ws.cell(r, 8).value)
        co2 = tofloat(ws.cell(r, 14).value)
        estrato = ws.cell(r, 22).value  # e4_estrato: "principal" | "sensibilidade"

        if fck in (None, 0) or co2 is None:
            continue
        if not (FCK_MIN <= fck <= FCK_MAX and CO2_MIN <= co2 <= CO2_MAX):
            continue
        if estrato not in TIERCODE:
            # dados_fck só deve conter linhas Elegível (ver LEGENDA); um
            # estrato em falta aqui é sinal de que apply_e4_estrato.py
            # precisa de correr de novo antes de exportar.
            print(f'AVISO: linha {r} (row_id={row_id}) sem e4_estrato, ignorada', file=sys.stderr)
            continue

        cat = classify(r, material, titulo)
        if cat == 'outros':
            print(f'AVISO: linha {r} (row_id={row_id}) caiu em outros -- material={material!r}', file=sys.stderr)
        compact.append([round(fck, 2), round(co2, 2), CATCODE[cat], TIERCODE[estrato]])

    json.dump(compact, sys.stdout, separators=(',', ':'))


if __name__ == '__main__':
    main()
