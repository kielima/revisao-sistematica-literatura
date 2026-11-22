"""F57 (#1969): escreve resultados/a2_por_par.csv com o transporte das materias-primas
(dados_fck col 62 `transporte_materiais`, rastreio F37) para cada obs_id de
dados_metanalise.csv. obs_id = linha da folha dados_fck. So leitura do xlsx."""
import csv
import openpyxl

ws = openpyxl.load_workbook('meta_analysis_base.xlsx', read_only=True)['dados_fck']
a2 = {r: (row[61] if len(row) > 61 else None)
      for r, row in enumerate(ws.iter_rows(min_row=2, values_only=True), start=2)}
pares = list(csv.DictReader(open('metanalise/dados_metanalise.csv', encoding='utf-8')))
with open('metanalise/resultados/a2_por_par.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['obs_id', 'estudo', 'a2'])
    for p in pares:
        w.writerow([p['obs_id'], p['estudo'], a2.get(int(p['obs_id'])) or 'nao_lido'])
print(f'{len(pares)} pares -> metanalise/resultados/a2_por_par.csv')
