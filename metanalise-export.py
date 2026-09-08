"""Exporta dados_fck (meta_analysis_base.xlsx) para o dataset compacto usado em
kielima.com/metanalise (public/assets/metanalise.js no repositório kielima-site).

Uso:
    python3 metanalise-export.py > metanalise_compact.json

Cada ponto exportado é [fck_MPa, co2_kg_m3, categoria_1_letra, estrato_1_letra].
Filtra a pares comparáveis por m3 (exclui totais de estrutura inteira, que nao
tem a mesma unidade de analise) e classifica o material por palavras-chave no
campo `material`+`titulo`. Ver CLAUDE.md / conversa da sessao 2026-09-08 para o
porque de cada regra.

Depois de gerar o JSON, injectar manualmente em public/assets/metanalise.js
(substituir o array `var DATA = [...]`) e reconferir os textos que citam
contagens (KPI de pares, tier-n-p/tier-n-s) no mesmo ficheiro.
"""
import json
import re
import sys

import openpyxl

BASE = 'meta_analysis_base.xlsx'

CATCODE = {'geopolimero': 'g', 'uhpc': 'u', 'scm': 's', 'reciclado': 'r', 'opc': 'o', 'outros': 'x'}
TIERCODE = {'principal': 'p', 'sensibilidade': 's'}

# Domínio "plausível" por m³ de material -- exclui totais de estrutura inteira
# (edifício, ponte), que aparecem em kg absolutos muito acima da escala por m³
# e não são a mesma unidade de análise dos demais pares.
FCK_MIN, FCK_MAX = 1, 300
CO2_MIN, CO2_MAX = -1000, 5000


def classify(material, titulo):
    t = ((material or '') + ' ' + (titulo or '')).lower()
    if re.search(r'geopolim|geopolym|alcali[- ]ativad|alkali[- ]activ|\bAAM\b|\bAAC\b', t):
        return 'geopolimero'
    if re.search(r'\buhpc\b|\buhpfrc\b|ultra[- ]high[- ]performance|ultra[- ]alta[- ]resist', t):
        return 'uhpc'
    if re.search(
        r'reciclad|recycled aggregate|\brca\b|residuo de construcao|'
        r'construction (and demolition )?waste|\brcd\b|debris aggregate|\bgcba\b|\bcba\b',
        t,
    ):
        return 'reciclado'
    if re.search(
        r'cinza volante|fly ash|escoria|slag|silica ativa|silica fume|metacaulim|metakaolin|'
        r'argila calcinada|calcined clay|pozolan|pozzolan|\blc3\b|\bscm\b|\bggbs\b|\bggbfs\b|'
        r'cinza co-queimada|co-fired ash',
        t,
    ):
        return 'scm'
    # Referencia/OPC: nome explicito OU classe normativa de concreto convencional
    # (europeia C##/##, espanhola HA-##) OU descricao generica "concreto armado/estrutural"/"betao"
    # -- a maioria dos concretos convencionais no banco esta descrita assim, nao por "OPC"/"portland".
    if re.search(r'\bopc\b|portland|\breferencia\b|\bcontrole\b|convencional|conventional concrete', t):
        return 'opc'
    if re.search(r'\bc\d{2}\s*/\s*\d{2}\b|\bha[- ]?\d{2}\b', t):
        return 'opc'
    if re.search(r'\bconcreto (armado|estrutural)\b|\bbetao\b', t):
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
            print(f'AVISO: linha {r} (row_id={ws.cell(r,1).value}) sem e4_estrato, ignorada', file=sys.stderr)
            continue

        cat = classify(material, titulo)
        compact.append([round(fck, 2), round(co2, 2), CATCODE[cat], TIERCODE[estrato]])

    json.dump(compact, sys.stdout, separators=(',', ':'))


if __name__ == '__main__':
    main()
