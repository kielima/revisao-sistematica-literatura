"""F42/F43 (tarefa #1805): grava em dados_fck os dados do transporte A4 lidos por estudo
(lotes_transporte/resultado_lote*.json = F44, os 86 estudos; resultado_comum_lote*.json = F45, os 60
em comum com o F40, relidos pelo mesmo prompt por decisao da Kie em #1828; resultado_fase2b_lote*.json = F51, tarefa
#1860, os 124 estudos somaveis que ficaram fora das 14 listas). So preenche celulas vazias; idempotente.
F51 (2026-11-17): na fase 2b a retencao da massa volumica e automatica, pela mesma regra da F46 — par cuja citacao
comeca por 'SUSPEITO' fica a aguardar #1832; par com 'seca_endurecido' na citacao fica a aguardar #1831.
Uso: python3 lotes_transporte/aplicar.py [--gravar]   (sem --gravar = ensaio, so conta)
Colunas novas (a seguir a etapas_nota, col 86): ver NOVAS. A premissa de 2.400 kg/m3 (F43)
NAO e gravada aqui: e do motor de calculo (#1806), que a aplica onde massa_volumica_origem = nao_disponivel.
Regra de coordenacao (COORDENACAO_AGENTES.md §5): so o integrador corre --gravar, depois de git fetch
e de confirmar que nenhum ramo aberto alterou o .xlsx.
Gravacao (F46, 2026-11-15, decisao da Kie em #1829: opcao a, o agente RSL grava por PR): as 3 colunas da massa
volumica (massa_volumica_kg_m3, massa_volumica_origem, massa_volumica_citacao) ficam EM BRANCO nos pares RETIDOS
abaixo, cujo valor depende de decisao ainda aberta da Kie (#1831 massa seca do endurecido; #1832 somas SUSPEITO;
RONNING 3872: os 2.400 kg/m3 sao premissa do proprio artigo, por confirmar). O valor lido e a origem ficam na
a4_leitura_nota, e os JSON mantem tudo: decidida a tarefa, um script pequeno preenche so essas celulas (vazias)."""
import glob, json, sys, collections
import openpyxl
NOVAS = ['a4_transporte_tipo', 'massa_volumica_kg_m3', 'massa_volumica_origem', 'massa_volumica_citacao',
         'a4_distancia_km', 'a4_modo', 'a4_capacidade', 'a4_regresso_vazio', 'a4_publicado_leitura',
         'a4_leitura_frente', 'a4_leitura_nota']
# sheet_row -> motivo (tarefa Supabase) da retencao da massa volumica
RETIDOS = {}
for r in (1691, 1083, 304, 316, 2091, *range(1937, 1949)):        # RABIE, BAYKARA, GRENGG, DU LT5S0, SAHMENKO GCP3, IRSHIDAT WCB
    RETIDOS[r] = 'aguarda #1832 (soma do traco SUSPEITO)'
for r in (886, 139, 140, 765, 766, 767, 768, 769, 770, 1480, 1482, 1485, 1210, 1211, 1658, 1142):  # IRSHIDAT ctrl, CHOI, LYRA, SKIBICKI, NASR, FORT, PAVLIK
    RETIDOS[r] = 'aguarda #1831 (massa volumica seca do endurecido)'
for r in (1126, 1127, 1128):                                         # RONNING: 2.400 e premissa do proprio artigo
    RETIDOS[r] = 'por confirmar (F45): 2.400 kg/m3 e premissa do proprio artigo, nao medicao'
MASSA = {'massa_volumica_kg_m3', 'massa_volumica_origem', 'massa_volumica_citacao'}
est = {}; frente = {}
for f in (sorted(glob.glob('lotes_transporte/resultado_lote*.json')) + sorted(glob.glob('lotes_transporte/resultado_comum_lote*.json'))
          + sorted(glob.glob('lotes_transporte/resultado_fase2b_lote*.json'))):
    for e in json.load(open(f)):
        est[int(e['row_id'])] = e
        frente[int(e['row_id'])] = 'F51 2026-11-17' if 'fase2b' in f else ('F45 2026-11-15' if 'comum' in f else 'F44 2026-11-11')
        if 'fase2b' in f:   # F51: retencao automatica (mesma regra da F46)
            for p in e.get('por_par', []):
                cit = (p.get('citacao') or '')
                if cit.startswith('SUSPEITO'):
                    RETIDOS.setdefault(int(p['sheet_row']), 'aguarda #1832 (soma do traco SUSPEITO, fase 2b F51)')
                elif 'seca_endurecido' in cit:
                    RETIDOS.setdefault(int(p['sheet_row']), 'aguarda #1831 (massa volumica seca do endurecido, fase 2b F51)')
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
        if r in RETIDOS:
            nota = 'MASSA VOLUMICA RETIDA na gravacao de %s - %s; valor lido %s, origem %s; citacao: %s. %s' % (
                '2026-11-17 (F51)' if frente[rid].startswith('F51') else '2026-11-15 (F46)',
                RETIDOS[r], mv, mo, p.get('citacao') or e.get('citacao'), nota)
            c['retidos'] += 1
        vals = [s(e.get('o_que_se_transporta')), s(mv), s(mo), s(p.get('citacao') or e.get('citacao')),
                s(e.get('distancia_betao_km')), s(e.get('modo_transporte')), s(e.get('capacidade')),
                s(e.get('regresso_vazio')), s(e.get('a4_publicado')),
                frente[rid] + ' leitura integral (prompt F42)' + ('' if e.get('texto_completo_lido') else ' (texto parcial)') + ('' if e.get('figuras_vistas') else ' (figuras nao vistas)'),
                s(nota)]
        for i, v in enumerate(vals):
            cell = ws.cell(r, col0 + i)
            if v is None or cell.value not in (None, ''): continue
            if r in RETIDOS and NOVAS[i] in MASSA: continue
            cell.value = v; c[NOVAS[i]] += 1
print('estudos', len(est), 'pares', sum(len(e.get('por_par', [])) for e in est.values()),
      'colunas a partir de', col0, dict(c), 'erros de linha', erros)
if gravar: wb.save('meta_analysis_base.xlsx'); print('gravado')
