"""F52 (tarefa #1830, decisao da Kie em 2026-11-17: «Aceito todas sua proposicoes, pode aplicar»): aplica em dados_fck
a decisao sobre os 10 estudos da fase 2 do A4 classificados so pelo enquadramento (F44; releitura F50).
- 8 «betao fresco de betoneira» so pelo enquadramento ready-mix/central (RIGON 2841, MAHDI 3155, BASAVARAJ 4138,
  LI 4161, HOSSAIN 3173, ALMEIDA 2836, RATHNARAJAN 2999, SANCHEZ-PANTOJA 2785): tipo mantido em col 87, confianca
  «provavel» (F38: fora da opcao principal do A4) — carimbo na a4_leitura_nota (col 97).
- ESPARHAM 4450: col 87 nao_transportado_in_situ -> indeterminado (so «construction workshop»/«on-site»; nunca afirma
  mistura no local de aplicacao); modo padrao do motor passa a betoneira; confianca «provavel».
- SKIBICKI 4512: in situ DECLARADO (Tab.5 p.17 «transport from raw material production to the mixing and printing
  location»); col 87 mantida, A4 = 0; carimbo.
So toca nas linhas listadas em ALVOS (col 87 preenchida), col 87 (ESPARHAM) e col 97 (carimbo em todas); idempotente
(nao repete o carimbo). O rotulo de confianca em si e calculado pelo motor (metanalise/motor_a4.py, a4_tipo_confianca).
Uso: /usr/bin/python3 lotes_transporte/aplicar_1830.py [--gravar]
"""
import sys
import openpyxl
PROVAVEL = {2841, 3155, 4138, 4161, 3173, 2836, 2999, 2785}
ESPARHAM, SKIBICKI = 4450, 4512
CARIMBO = {
    'provavel': '[#1830 2026-11-17 (F52), decisao da Kie: betao de betoneira so pelo enquadramento ready-mix/central -> '
                'confianca PROVAVEL (F38: fora da opcao principal do A4); releitura integral F50 confirmou que a entrega a obra nao e modelada]',
    'esparham': '[#1830 2026-11-17 (F52), decisao da Kie: a4_transporte_tipo nao_transportado_in_situ -> indeterminado; o artigo so diz '
                '"construction workshop" (p.5) e "electricity consumed on-site" (p.7), nunca afirma mistura no local de aplicacao (releitura F50); '
                'modo padrao betoneira, confianca PROVAVEL]',
    'skibicki': '[#1830 2026-11-17 (F52), decisao da Kie: in situ DECLARADO — Tab.5 p.17 "transport from raw material production to the mixing '
                'and printing location" (mistura e impressao no mesmo local; releitura F50); A4 = 0. Ressalva: o artigo nao diz se o local e obra ou fabrica]',
}
gravar = '--gravar' in sys.argv
wb = openpyxl.load_workbook('meta_analysis_base.xlsx'); ws = wb['dados_fck']
h = [c.value for c in ws[1]]
C_TIPO, C_NOTA = h.index('a4_transporte_tipo') + 1, h.index('a4_leitura_nota') + 1
assert (C_TIPO, C_NOTA) == (87, 97), (C_TIPO, C_NOTA)
n = {'provavel': 0, 'esparham_tipo': 0, 'esparham': 0, 'skibicki': 0, 'ja_carimbadas': 0}
linhas = []
for r in range(2, ws.max_row + 1):
    rid = ws.cell(r, 1).value
    try: rid = int(rid)
    except (TypeError, ValueError): continue
    tipo = ws.cell(r, C_TIPO).value
    if rid in PROVAVEL and tipo == 'betao_fresco_betoneira': k = 'provavel'
    elif rid == ESPARHAM and tipo in ('nao_transportado_in_situ', 'indeterminado'): k = 'esparham'
    elif rid == SKIBICKI and tipo == 'nao_transportado_in_situ': k = 'skibicki'
    else: continue
    nota = ws.cell(r, C_NOTA).value or ''
    if '#1830 2026-11-17 (F52)' in nota:
        n['ja_carimbadas'] += 1; continue
    if k == 'esparham' and tipo == 'nao_transportado_in_situ':
        ws.cell(r, C_TIPO).value = 'indeterminado'; n['esparham_tipo'] += 1
    ws.cell(r, C_NOTA).value = (nota + ' ' if nota else '') + CARIMBO[k]
    n[k] += 1; linhas.append((r, rid, k))
print('linhas tocadas:', n, '| total', len(linhas))
print('sheet_rows:', [l[0] for l in linhas])
if gravar:
    wb.save('meta_analysis_base.xlsx'); print('GRAVADO meta_analysis_base.xlsx')
else:
    print('ensaio (sem --gravar): nada gravado')
