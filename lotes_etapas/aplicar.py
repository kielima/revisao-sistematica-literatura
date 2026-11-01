"""F39: grava o CO2 por etapa EN 15804 em dados_fck (cols 77-87). So preenche celulas vazias.
Uso: python3 lotes_etapas/aplicar.py [--gravar]   (sem --gravar = ensaio, so conta)
Fonte: resultado_lote*.json, sobrepostos por recorte_resultado*.json (por row_id)."""
import glob, json, sys, collections
import openpyxl
NOVAS = ['co2_a1','co2_a2','co2_a3','co2_a4','co2_a1a3_agregado','etapas_tipo','soma_confere','etapas_local','etapas_citacao','etapas_nota']
est = {}
for f in sorted(glob.glob('lotes_etapas/resultado_lote*.json')) + sorted(glob.glob('lotes_etapas/recorte_resultado*.json')):
    d = json.load(open(f)); d = d if isinstance(d, list) else d.get('estudos', d.get('studies', []))
    for e in d: est[e['row_id']] = e
gravar = '--gravar' in sys.argv
wb = openpyxl.load_workbook('meta_analysis_base.xlsx'); ws = wb['dados_fck']
h = [c.value for c in ws[1]]
col0 = h.index('fronteira_revisao') + 2 if NOVAS[0] not in h else h.index(NOVAS[0]) + 1
if NOVAS[0] not in h:
    for i, n in enumerate(NOVAS): ws.cell(1, col0 + i, n)
c = collections.Counter(); erros = []
for e in est.values():
    for p in e['pares']:
        r = p['sheet_row']
        if ws.cell(r, 1).value != e['row_id']: erros.append((e['row_id'], r)); continue
        vals = [p.get(k) for k in ('co2_a1','co2_a2','co2_a3','co2_a4','co2_a1a3_agregado','etapas_tipo','soma_confere','local','citacao','nota')]
        for i, v in enumerate(vals):
            cell = ws.cell(r, col0 + i)
            if v in (None, '') or cell.value not in (None, ''): continue
            cell.value = v; c[NOVAS[i]] += 1
print('estudos', len(est), 'colunas a partir de', col0, dict(c), 'erros de linha', erros)
if gravar: wb.save('meta_analysis_base.xlsx'); print('gravado')
