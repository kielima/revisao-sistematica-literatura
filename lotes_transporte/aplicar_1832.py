"""F58 (tarefa #1832, decisao da Kie em 2026-11-25: «sim para as 3»): massa volumica dos 3 casos SUSPEITO relidos na
F50 (lotes_transporte/RELEITURA_1830_1832_2026-11-16.md), pela recomendacao proposta em 16/11 e repetida em 25/11:
  GRENGG 3066 l.304  -> (b) 3.038 kg/m3, soma_do_traco: a Tab.2 (p.2) e «Mix design [kg/m3]» e fecha o volume
                        (pasta 518 L + agregado de escoria BOF 1.871 kg / 3,88 g/cm3 = 482 L -> 1.000 L); argamassa pesada.
  BAYKARA 3731 l.1083 -> (a) nao_disponivel: a Tab.2 (p.3) esta em gramas (740 + 2.035 + 355 = 3.130 g); a UF «3130 kg
                        ... equivalent to 1 m3» e a amassadura x1.000; sem massa medida nem densidades -> premissa F43 no motor.
  RABIE 4696 l.1691   -> (a) nao_disponivel: a Tab.3 (p.4) soma 3.093 kg/«m3» em todas as misturas (nao normalizada a 1 m3);
                        sem massa medida -> premissa F43 no motor.
NAO decidido (fica por confirmar, sem gravar): a pergunta extra da F50 — QA 1 -> 0,5 em BAYKARA e RABIE (precedente LI 2720)
e alerta em co2_conversao sobre o CO2 por «m3» dos autores. Os outros 24 pares retidos «aguarda #1832» (IRSHIDAT, DU,
SAHMENKO, e os 10 da F51) continuam retidos: a decisao da Kie foi sobre os 3 casos apresentados.
So toca nas cols 88-90 e 97 das 3 linhas; idempotente. Depois correr metanalise/motor_a4.py.
Uso: /usr/bin/python3 lotes_transporte/aplicar_1832.py [--gravar]
"""
import sys
import openpyxl

MARCA = '#1832 2026-11-25 (F58)'
NOTA = 'decisao da Kie «sim para as 3» (recomendacao F50: GRENGG (b), BAYKARA e RABIE (a))'
ALVOS = {
    304: (3066, 3038.0, 'soma_do_traco',
          "Soma do traco Tab.2 (p.3) A-SA = MK 303 + escoria 409 + waterglass 455 + agregado de escoria SA 1.871 = 3.038 kg/m3 (sem oleo). "
          "Real, nao SUSPEITO (F50/#1832): a Tab.2 e 'Mix design [kg/m3]' e fecha o volume — pasta 518 L/m3 (impresso) + 1.871 kg / 3,88 g/cm3 "
          "(densidade do agregado BOF impressa na p.2) = 482 L -> 1.000 L; argamassa pesada com agregado de escoria",
          '(b) 3.038 kg/m3 real, soma_do_traco (traco fecha 1.000 L)'),
    1083: (3731, None, 'nao_disponivel',
           "nao_disponivel (F50/#1832): a Tab.2 (p.3) esta em gramas (740 + 2.035 + 355 = 3.130 g de amassadura); a UF da p.2 «3130 kg of cement "
           "composite, which was equivalent to 1 m3» e a amassadura x1.000, nao uma massa volumica (3.130 g ocupam ~1,36 L com densidades tipicas); "
           "sem massa medida nem densidades dos materiais -> premissa F43 (2.400 kg/m3) no motor",
           '(a) nao_disponivel + premissa F43 (UF = amassadura x1.000)'),
    1691: (4696, None, 'nao_disponivel',
           "nao_disponivel (F50/#1832): a Tab.3 (p.4) soma 3.093 kg/'m3' em todas as 36 misturas (M25: cinza 711 + areia 1.956 + NaOH 213 + "
           "Na2SiO3 213) — proporcoes coerentes (1:2,75; F/B 0,6) mas nao normalizadas a 1 m3 (~1,34 m3 com densidades tipicas); sem massa medida "
           "-> premissa F43 (2.400 kg/m3) no motor",
           '(a) nao_disponivel + premissa F43 (traco nao normalizado a 1 m3)'),
}
gravar = '--gravar' in sys.argv
wb = openpyxl.load_workbook('meta_analysis_base.xlsx'); ws = wb['dados_fck']
h = [c.value for c in ws[1]]
C_M, C_O, C_C, C_NOTA = (h.index(k) + 1 for k in ('massa_volumica_kg_m3', 'massa_volumica_origem', 'massa_volumica_citacao', 'a4_leitura_nota'))
assert (C_M, C_O, C_C, C_NOTA) == (88, 89, 90, 97)
feitas = 0
for r, (rid, massa, origem, cit, resumo) in sorted(ALVOS.items()):
    assert ws.cell(r, 1).value == rid, (r, ws.cell(r, 1).value, rid)
    nota = ws.cell(r, C_NOTA).value or ''
    assert 'aguarda #1832' in nota, (r, nota[:80])
    if MARCA in nota:
        print('ja feita', r); continue
    assert all(ws.cell(r, c).value in (None, '') for c in (C_M, C_O, C_C)), r
    if massa is not None:
        ws.cell(r, C_M).value = massa
    ws.cell(r, C_O).value = origem
    ws.cell(r, C_C).value = cit
    ws.cell(r, C_NOTA).value = (nota.replace('aguarda #1832 (soma do traco SUSPEITO)', 'decidida em #1832 (F58, 2026-11-25)', 1)
                                + f' [{MARCA}, {NOTA}: {resumo}]')
    feitas += 1; print('  ', r, rid, origem, massa)
print('linhas tocadas:', feitas)
if gravar:
    wb.save('meta_analysis_base.xlsx'); print('GRAVADO meta_analysis_base.xlsx')
else:
    print('ensaio (sem --gravar): nada gravado')
