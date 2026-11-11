"""F42/F43 (tarefa #1805): grava em dados_fck os dados do transporte A4 lidos por estudo
(lotes_transporte/resultado_lote*.json). So preenche celulas vazias; idempotente.
Uso: python3 lotes_transporte/aplicar.py [--gravar]   (sem --gravar = ensaio, so conta)
Colunas novas (a seguir a etapas_nota, col 86): ver NOVAS. A premissa de 2.400 kg/m3 (F43)
NAO e gravada aqui: e do motor de calculo (#1806), que a aplica onde massa_volumica_origem = nao_disponivel.
Regra de coordenacao (COORDENACAO_AGENTES.md §5): so o integrador corre --gravar, depois de git fetch
e de confirmar que nenhum ramo aberto alterou o .xlsx."""
import glob, json, sys, collections
import openpyxl
NOVAS = ['a4_transporte_tipo', 'massa_volumica_kg_m3', 'massa_volumica_origem', 'massa_volumica_citacao',
         'a4_distancia_km', 'a4_modo', 'a4_capacidade', 'a4_regresso_vazio', 'a4_publicado_leitura',
         'a4_leitura_frente', 'a4_leitura_nota']
est = {}
for f in sorted(glob.glob('lotes_transporte/resultado_lote*.json')):
    for e in json.load(open(f)):
        est[int(e['row_id'])] = e
gravar = '--gravar' in sys.argv
wb = openpyxl.load_workbook('meta_analysis_base.xlsx'); ws = wb['dados_fck']
h = [c.value for c in ws[1]]
col0 = h.index('etapas_nota') + 2 if NOVAS[0] not in h else h.index(NOVAS[0]) + 1
if NOVAS[0] not in h:
    for i, n in enumerate(NOVAS): ws.cell(1, col0 + i, n)
c = collections.Counter(); erros = []
def s(v):
    return None if v in (None, '', []) else (v if isinstance(v, (int, float)) else str(v))
for rid, e in est.items():
    por_par = {int(p['sheet_row']): p for p in e.get('por_par', [])}
    for r, p in por_par.items():
        if ws.cell(r, 1).value != rid: erros.append((rid, r)); continue
        mv = p.get('massa_volumica_kg_m3'); mo = p.get('massa_volumica_origem') or e.get('massa_volumica_origem')
        if mv is None and e.get('massa_volumica_kg_m3') is not None and (p.get('massa_volumica_origem') in (None, '')):
            mv = e['massa_volumica_kg_m3']
        nota = '; '.join(x for x in (e.get('nota'), p.get('nota')) if x)
        vals = [s(e.get('o_que_se_transporta')), s(mv), s(mo), s(p.get('citacao') or e.get('citacao')),
                s(e.get('distancia_betao_km')), s(e.get('modo_transporte')), s(e.get('capacidade')),
                s(e.get('regresso_vazio')), s(e.get('a4_publicado')),
                'F42 2026-11-11 leitura integral' + ('' if e.get('texto_completo_lido') else ' (texto parcial)') + ('' if e.get('figuras_vistas') else ' (figuras nao vistas)'),
                s(nota)]
        for i, v in enumerate(vals):
            cell = ws.cell(r, col0 + i)
            if v is None or cell.value not in (None, ''): continue
            cell.value = v; c[NOVAS[i]] += 1
print('estudos', len(est), 'pares', sum(len(e.get('por_par', [])) for e in est.values()),
      'colunas a partir de', col0, dict(c), 'erros de linha', erros)
if gravar: wb.save('meta_analysis_base.xlsx'); print('gravado')
