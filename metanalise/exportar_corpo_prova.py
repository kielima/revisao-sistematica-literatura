"""#1454 (agente RSL, 2026-11-25; por confirmar pela Kie): escreve
resultados/corpo_prova_por_par.csv com a base de medicao do fck de cada par
de dados_metanalise.csv, lida da col 11 `tipo_corpo_prova` de dados_fck
(obs_id = linha da folha). So leitura do xlsx; nada e convertido.

Classificacao estrita (regra «nao vamos assumir nada», Kie 2026-10-04):
so conta o formato ESCRITO na celula. Texto marcado como inferencia
(«inferido», «pratica us», «nao_dito») ou vazio -> `indeterminado`.
  cilindro  : contem «cilindr»
  cubo      : contem «cub» (cubo, cubico)
  prisma    : contem «prism»
  outro     : pasta/argamassa sem formato, modelo, catalogo, n/a
  indeterminado : vazio, nao especificado/declarado/informado, inferido
"""
import csv
import re
import unicodedata
import openpyxl


def norm(s):
    s = unicodedata.normalize('NFKD', str(s or '')).encode('ascii', 'ignore').decode()
    return s.strip().lower()


def classifica(txt):
    t = norm(txt)
    if not t:
        return 'indeterminado'
    if re.search(r'inferid|pratica us|nao_dito|nao dito', t):
        return 'indeterminado'
    if 'cilindr' in t and re.search(r'prism\w*[^;]*\(flexao\)', t):
        return 'cilindro'          # prisma so para flexao; compressao em cilindro
    tem = [k for k, p in (('cilindro', 'cilindr'), ('cubo', 'cub'), ('prisma', 'prism')) if p in t]
    if len(tem) == 1:
        return tem[0]
    if len(tem) > 1:
        return 'misto'
    if re.search(r'nao (especificad|declarad|informad|aplicavel)|^n/?a\b|nao_', t):
        return 'indeterminado'
    return 'outro'


ws = openpyxl.load_workbook('meta_analysis_base.xlsx', read_only=True)['dados_fck']
tipo = {r: row[10] for r, row in enumerate(ws.iter_rows(min_row=2, values_only=True), start=2)}
pares = list(csv.DictReader(open('metanalise/dados_metanalise.csv', encoding='utf-8')))
with open('metanalise/resultados/corpo_prova_por_par.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['obs_id', 'estudo', 'base_fck', 'tipo_corpo_prova'])
    for p in pares:
        t = tipo.get(int(p['obs_id']))
        w.writerow([p['obs_id'], p['estudo'], classifica(t), norm(t)])
print(f'{len(pares)} pares -> metanalise/resultados/corpo_prova_por_par.csv')
