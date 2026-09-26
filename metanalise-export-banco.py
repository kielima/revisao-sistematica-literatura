"""Exporta a aba dados_fck (meta_analysis_base.xlsx) INTEIRA -- todas as linhas
e todas as colunas, sem filtro nenhum -- para o visualizador do banco de dados
em kielima.com/metanalise/dados (public/metanalise/dados/banco.json no
repositório kielima-site).

Pedido da Kiê (2026-09-26): um botão no topo do painel da metanálise, ao lado
do idioma e do modo claro/escuro, para ver o banco de dados completo.

Diferença para o metanalise-export.py: aquele gera o dataset COMPACTO dos
gráficos (só pares fck+CO2 já em kg/m3, com categoria e estrato); este gera o
banco BRUTO, tal como está na planilha, para consulta e auditoria. As linhas
fora dos gráficos (unidade de CO2 ainda por converter, sem par, etc.) aparecem
aqui na mesma.

Uso:
    python3 metanalise-export-banco.py > ../kielima-site/public/metanalise/dados/banco.json

Saída: {"gerado": "AAAA-MM-DD", "colunas": [...], "linhas": [[...], ...]}.
Os nomes das colunas são os cabeçalhos da planilha, sem tradução (são
identificadores, iguais aos citados nas notas e no protocolo).
"""
import datetime
import json
import sys

import openpyxl

BASE = 'meta_analysis_base.xlsx'


def celula(v):
    if v is None:
        return None
    if isinstance(v, float):
        # 10 casas chegam para todos os valores do banco e evitam lixo binário
        # tipo 0.30000000000000004 no JSON.
        return float(repr(round(v, 10)))
    if isinstance(v, (int, str)):
        return v
    return str(v)


def main():
    ws = openpyxl.load_workbook(BASE, read_only=True, data_only=True)['dados_fck']
    linhas = list(ws.iter_rows(values_only=True))
    colunas = [str(c) for c in linhas[0]]
    corpo = [[celula(v) for v in r] for r in linhas[1:] if any(v is not None for v in r)]
    json.dump(
        {'gerado': datetime.date.today().isoformat(), 'colunas': colunas, 'linhas': corpo},
        sys.stdout, ensure_ascii=False, separators=(',', ':'),
    )


if __name__ == '__main__':
    main()
