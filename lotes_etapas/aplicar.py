"""F39 (NAO voltar a correr sozinho: repoe celulas que aplicar_verif.py deixou vazias; correr sempre aplicar.py e a seguir aplicar_verif.py): grava o CO2 por etapa EN 15804 em dados_fck (cols 77-87). So preenche celulas vazias.
Uso: python3 lotes_etapas/aplicar.py [--gravar]   (sem --gravar = ensaio, so conta)
Fonte: resultado_lote*.json, sobrepostos por recorte_resultado*.json (por row_id)."""
import glob, json, sys, collections
import openpyxl
NOVAS = ['co2_a1','co2_a2','co2_a3','co2_a4','co2_a1a3_agregado','etapas_tipo','soma_confere','etapas_local','etapas_citacao','etapas_nota']
est = {}
for f in sorted(glob.glob('lotes_etapas/resultado_lote*.json')) + sorted(glob.glob('lotes_etapas/recorte_resultado*.json')) + sorted(glob.glob('lotes_etapas/resultado_reextr*.json')):
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
        if ws.cell(r, col0 + 5).value == 'retirado': continue  # nao repor o que a verificacao retirou
        vals = [p.get(k) for k in ('co2_a1','co2_a2','co2_a3','co2_a4','co2_a1a3_agregado','etapas_tipo','soma_confere','local','citacao','nota')]
        for i, v in enumerate(vals):
            cell = ws.cell(r, col0 + i)
            if v in (None, '') or cell.value not in (None, ''): continue
            cell.value = v; c[NOVAS[i]] += 1
print('estudos', len(est), 'colunas a partir de', col0, dict(c), 'erros de linha', erros)
# Retiradas apos revisao (2026-11-01): campos cujo conteudo nao e o que o nome diz.
LIMPAR = {
 (4292,'co2_a1a3_agregado'):'e A1-A4 agregado (Tab.5), nao A1-A3',
 (3911,'co2_a1a3_agregado'):'e A1+A2 e inclui aco, nao A1-A3 do betao',
 (4098,'co2_a1a3_agregado'):'e A1-A4 agregado (inclui transporte do betao a obra)',
 (4785,'co2_a1a3_agregado'):'e so A1+A2 de uma argamassa',
 (4297,'co2_a4'):'A4 calculado com factor/distancia nao confirmados como impressos no artigo',
}
for k in ('co2_a1','co2_a2','co2_a3'):
    LIMPAR[(3904,k)]='lido por pixel numa figura sem rotulos numericos (regra: so pixel com rotulos/escala clara)'
for k in ('co2_a2','co2_a1a3_agregado'):
    LIMPAR[(3153,k)]='lido por pixel numa figura sem rotulos (+-10); texto mistura materias-primas e fabrico'
for k in ('co2_a1','co2_a2','co2_a3','co2_a4','co2_a1a3_agregado'):
    LIMPAR[(3657,k)]='derivado de percentagens inteiras da Fig.8b x valor gravado (que nao bate com o artigo); nao fiavel'
nl=0
for r in range(2, ws.max_row+1):
    rid=ws.cell(r,1).value
    for (i,k),mot in LIMPAR.items():
        if rid==i:
            cell=ws.cell(r,col0+NOVAS.index(k))
            if cell.value not in (None,''):
                cell.value=None; nl+=1
                nt=ws.cell(r,col0+NOVAS.index('etapas_nota'))
                nt.value=((nt.value or '')+f' [retirado {k}: {mot}]').strip()
print('campos retirados',nl)
if gravar: wb.save('meta_analysis_base.xlsx'); print('gravado')
