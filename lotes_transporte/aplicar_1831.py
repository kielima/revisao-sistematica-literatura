"""F55 (tarefa #1831, decisao da Kie em 2026-11-22: «C»): massa volumica transportada no A4 por TIPO de fabricacao.
Preenche em dados_fck as celulas da massa volumica (cols 88-90) que a F46/F51 deixaram EM BRANCO a aguardar a #1831
(27 pares de 11 estudos, carimbo «aguarda #1831» na a4_leitura_nota, col 97), pela regra (c) proposta em 20/11 e
aprovada em 22/11:
  - betao fresco (betoneira) / indeterminado -> massa FRESCA: impressa fresca > soma do traco impresso > premissa F43
    (2.400 kg/m3, do motor). A massa seca em estufa do endurecido NAO serve (ensaio de laboratorio: ASTM C642,
    NBR 9778, EN 1015-10, ASTM C1754; 4-8 % abaixo da fresca em betao corrente, 20-30 % nos porosos);
  - elemento pre-fabricado -> massa do ELEMENTO: densidade endurecida impressa (ao ar, saturada ou do fabricante) >
    soma do traco > seca em estufa marcada «seca_endurecido» > 2.400; veiculo carreta (MODO_PADRAO do motor);
  - pre-mistura seca -> soma dos solidos do traco (nenhum par desta lista);
  - coerencia: quando o CO2 do par foi convertido com uma massa volumica, o A4 usa a mesma (FORT 4623: 1.668).
Resultado por par (sheet_row):
  soma_do_traco (8): CHOI 2608 l.139/140; SKIBICKI 4512 l.1480/1482/1485 (in situ, A4 = 0 — massa so para registo);
                     FORT 4623 l.1658 (coerencia CO2/A4); MASI 4039 l.1167/1168.
  seca_endurecido (8, pre-fabricado): SPOSITO 2672 l.145/2101-2105 (pastas para paineis de fachada; so densidade seca
                     ASTM C948, sem traco em kg/m3); PAULA JUNIOR 4365 l.1324/1325 (pecas de pavimento intertravado
                     NBR 9781: densidade medida nas proprias pecas; col 87 indeterminado -> elemento_prefabricado).
  nao_disponivel (10): LYRA 2847 l.765-770, NASR 4160 l.1210/1211, PAVLIK 3924 l.1142 (argamassas de laboratorio so
                     com densidade seca e traco em razoes, sem kg/m3); SAHMENKO 2666 l.143 (2.400 = densidade seca do
                     fabricante; traco sem agua). O motor aplica a premissa F43 (2.400).
  passa a #1832 (1): IRSHIDAT 3176 l.886 — a seca do controlo cai; a unica alternativa e a soma do traco SUSPEITO
                     (3.101 kg/m3, tabela nao normalizada a 1 m3), que e a decisao da #1832.
So toca nas 27 linhas listadas (cols 88, 89, 90, 97 e, em 1324/1325, col 87); idempotente (nao repete o carimbo).
Verificacao: diff celula a celula contra o main (so estas celulas), LEGENDA intacta. Depois correr metanalise/motor_a4.py.
Uso: /usr/bin/python3 lotes_transporte/aplicar_1831.py [--gravar]
"""
import sys
import openpyxl

MARCA = '#1831 2026-11-22 (F55)'
SOMA, SECA, ND, R1832 = 'soma_do_traco', 'seca_endurecido', 'nao_disponivel', None

NOTA_C = ('decisao da Kie «C» (regra (c): massa por tipo de fabricacao — fresco = massa fresca/soma do traco; '
          'pre-fabricado = massa do elemento, seca marcada; coerencia CO2/A4)')

# sheet_row: (row_id, origem, massa, citacao, carimbo_resumo, novo_tipo_col87)
ALVOS = {
    # --- CHOI 2608: UHPC de laboratorio, indeterminado -> betao fresco por defeito -> soma do traco
    139: (2608, SOMA, 2391.4,
          "Soma do traco Tab.8 (p.9) RS-U-20: OPC 818 + FA 72,1 + SF 80,1 + QP 95,6 + RS 1084 + W 199 + SP 42,6 = 2.391,4 kg/m3. "
          "A 'apparent density' ASTM C642 do endurecido aos 28 d (Sec.4.1.2 p.10, Fig.7a: 2.241 kg/m3) e seca e nao serve como massa transportada (F55/#1831)",
          'betao fresco -> soma do traco 2.391,4 (a seca 2.241 ASTM C642 nao serve)', None),
    140: (2608, SOMA, 2478.2,
          "Soma do traco Tab.8 (p.9) NS-U-20: OPC 891 + SF 39,3 + QP 141 + NS 1150 + W 214 + SP 42,9 = 2.478,2 kg/m3. "
          "A 'apparent density' ASTM C642 do endurecido aos 28 d (Sec.4.1.2 p.10, Fig.7a: 2.372 kg/m3) e seca e nao serve (F55/#1831)",
          'betao fresco -> soma do traco 2.478,2 (a seca 2.372 ASTM C642 nao serve)', None),
    # --- SKIBICKI 4512: in situ declarado (F52), A4 = 0; a massa fica registada pela soma do traco
    1480: (4512, SOMA, 2293.2,
           "Soma do traco Tab.2 R0: 560 + 160 + 80 + 1266 + 0 + 225 + 2,2 = 2.293,2 kg/m3. A oven-dry density aos 28 d da Tab.3 (p.15), "
           "2.178 kg/m3, e seca em estufa e nao serve (F55/#1831). In situ declarado (F52): A4 = 0, massa so para registo",
           'soma do traco 2.293,2 (oven-dry 2.178 nao serve; in situ, A4 = 0)', None),
    1482: (4512, SOMA, 2269.2,
           "Soma do traco Tab.2 R20: 448 + 160 + 80 + 1266 + 88 + 225 + 2,2 = 2.269,2 kg/m3. Oven-dry density Tab.3 (p.15) 1.994 kg/m3 e seca "
           "e nao serve (F55/#1831). In situ declarado (F52): A4 = 0",
           'soma do traco 2.269,2 (oven-dry 1.994 nao serve; in situ, A4 = 0)', None),
    1485: (4512, SOMA, 2233.2,
           "Soma do traco Tab.2 R50: 280 + 160 + 80 + 1266 + 220 + 225 + 2,2 = 2.233,2 kg/m3. Oven-dry density Tab.3 (p.15) 1.736 kg/m3 e seca "
           "(mistura porosa, 22 % abaixo da soma) e nao serve (F55/#1831). In situ declarado (F52): A4 = 0",
           'soma do traco 2.233,2 (oven-dry 1.736 nao serve; in situ, A4 = 0)', None),
    # --- FORT 4623: coerencia CO2/A4 — a massa ja usada na conversao do CO2 e a soma do traco
    1658: (4623, SOMA, 1668.0,
           "Soma do traco Tab.3 (p.5): cimento 219,5 + BFA 146,3 + agregado 1.097,4 + agua por w/b 0,56 x 365,8 = 204,8 -> 1.668,0 kg/m3, "
           "igual a 'bulk density' BFA40 da Tab.6 (p.9) e a massa ja usada na conversao do CO2 (kg/t x 1,668 t/m3, ver co2_conversao): "
           "regra de coerencia CO2/A4 (F55/#1831) — usar 2.400 no A4 do mesmo par seria incoerente",
           'soma do traco 1.668,0 = massa da conversao do CO2 (coerencia CO2/A4)', None),
    # --- MASI 4039: betao de betoneira (batching plant) -> soma do traco
    1167: (4039, SOMA, 2316.9,
           "Soma do traco Tab.1 CNAT: cimento 375 + agua 127 + aditivos 3,86 + brita 971 + areia 840 = 2.316,9 kg/m3 (agua da tabela; a/c 0,448 "
           "inclui humidade dos agregados). A 'geometric density' seca aos 28 d da Tab.3 (p.2835), 2,20 g/cm3, nao serve como massa fresca (F55/#1831)",
           'betao fresco de betoneira -> soma do traco 2.316,9 (geometric density seca 2.200 nao serve)', None),
    1168: (4039, SOMA, 2305.6,
           "Soma do traco Tab.1 CRAP: cimento 380 + agua 137 + aditivos 3,58 + brita 461 + areia 628 + RAP 696 = 2.305,6 kg/m3. A 'geometric density' "
           "seca aos 28 d da Tab.3 (p.2835), 2,02 g/cm3, nao serve como massa fresca (F55/#1831)",
           'betao fresco de betoneira -> soma do traco 2.305,6 (geometric density seca 2.020 nao serve)', None),
}
# --- SPOSITO 2672: pastas alcali-activadas para paineis de fachada (Cap.5; aplicacao pre_fabricado_corrente) -> elemento
#     pre-fabricado; sem densidade endurecida ao ar nem traco em kg/m3 -> seca em estufa marcada «seca_endurecido»
for r, mix, g in ((145, 'NH-SS1.5', '1,87'), (2101, 'NH-SS1.0', '1,81'), (2102, 'NH-SS2.0', '1,86'),
                  (2103, 'NH-BLA1.0', '1,85'), (2104, 'NH-BLA1.5', '1,92'), (2105, 'NH-BLA2.0', '1,83')):
    massa = round(float(g.replace(',', '.')) * 1000, 1)
    ALVOS[r] = (2672, SECA, massa,
                f"Tab.14 (p.94, Sec.4.1.6.1.3) bulk density BD (ASTM C948) aos 28 d, pasta endurecida {mix}: {g} g/cm3 = {massa:.0f} kg/m3 — "
                "seca em estufa, marcada 'seca_endurecido' (F55/#1831: elemento pre-fabricado [paineis de fachada, Cap.5] sem densidade endurecida "
                "ao ar nem traco em kg/m3 (Tab.10 so em razoes); a massa seca e o piso da massa do elemento transportado; veiculo carreta)",
                f'pre-fabricado -> seca marcada {massa:.0f} (sem densidade ao ar nem traco em kg/m3)', None)
# --- PAULA JUNIOR 4365: pecas pre-fabricadas de pavimento intertravado (NBR 9781) -> elemento pre-fabricado, carreta;
#     a densidade endurecida medida nas proprias pecas prefere-se a soma do traco de PROJECTO (1.600), contradita pelo medido
for r, dim, massa, dp in ((1324, '10x20x6 cm', 2006.57, '104,28'), (1325, '10x20x8 cm', 1840.24, '98,65')):
    ALVOS[r] = (4365, SECA, massa,
                f"Tab.8 (p.14) pieces {dim}, hardened density average {massa:.2f} kg/m3 (DP {dp}), ASTM C1754 com massa seca — marcada "
                "'seca_endurecido' (F55/#1831: pecas pre-fabricadas de pavimento intertravado, NBR 9781 -> elemento pre-fabricado, veiculo carreta; "
                "a densidade medida nas proprias pecas prefere-se a soma do traco PC-R100 da Tab.3 = 312 + 1179 + 109 = 1.600 kg/m3, que e a "
                "densidade de PROJECTO (p.5) e fica 15-25 % abaixo do medido; a fresca 1.678,9 (Sec.3.3) e do caso-piloto moldado in situ, outro objecto)",
                f'pecas pre-fabricadas (NBR 9781) -> tipo elemento_prefabricado/carreta; seca marcada {massa:.2f}', 'elemento_prefabricado')
# --- LYRA 2847: argamassas de laboratorio; so massa especifica seca (NBR 9778) e traco relativo -> nao_disponivel
for r, mix, g in ((765, 'CCAC-L 5 %', '2,06'), (766, 'CCAC-L 10 %', '2,04'), (767, 'CCAC-L 20 %', '2,02'),
                  (768, 'V5-L 5 %', '~1,96'), (769, 'V5-L 10 %', '~1,96'), (770, 'V5-L 20 %', '~1,96')):
    ALVOS[r] = (2847, ND, None,
                f"nao_disponivel (F55/#1831): a massa especifica aparente aos 28 d de {mix} (Sec.5.6.1 p.133: {g} g/cm3; NBR 9778, provetes secos em "
                "estufa a 105 C, Sec.4.10.1.1 p.77-78) e seca e nao serve como massa fresca transportada; o traco 1:2,5:0,5 e so em massa relativa, "
                "sem kg/m3 (Sec.4.10.1 p.77) -> o motor aplica a premissa F43 (2.400 kg/m3)",
                f'betao fresco sem traco em kg/m3 -> nao_disponivel (seca {g} g/cm3 nao serve; premissa F43 no motor)', None)
# --- NASR 4160, PAVLIK 3924: argamassas de laboratorio, densidade seca e traco em razoes -> nao_disponivel
ALVOS[1210] = (4160, ND, None,
               "nao_disponivel (F55/#1831): a 'dry bulk density' ASTM C642 aos 28 d da Fig.6 (p.48), Control 2.194,8 kg/m3, e seca e nao serve como "
               "massa fresca; a Tab.2 so da proporcoes relativas (areia 2,75 : ligante 1 : a/l 0,30 : SP 0,0186), sem kg/m3 -> premissa F43 (2.400) no motor",
               'betao fresco sem traco em kg/m3 -> nao_disponivel (seca 2.194,8 nao serve; premissa F43)', None)
ALVOS[1211] = (4160, ND, None,
               "nao_disponivel (F55/#1831): a 'dry bulk density' ASTM C642 aos 28 d da Fig.6 (p.48), GT15CWP30 2.164,1 kg/m3, e seca e nao serve; "
               "Tab.2 so em proporcoes relativas, sem kg/m3 -> premissa F43 (2.400) no motor",
               'betao fresco sem traco em kg/m3 -> nao_disponivel (seca 2.164,1 nao serve; premissa F43)', None)
ALVOS[1142] = (3924, ND, None,
               "nao_disponivel (F55/#1831): rho_b = 2.031 kg/m3 (Tab.1 p.3) e a massa volumica aparente seca do endurecido (EN 1015-10, provetes secos "
               "em vacuo a 60 C) e nao serve como massa fresca; o traco e so em razoes (w/b 0,5, s/b 3), sem kg/m3 -> premissa F43 (2.400) no motor",
               'betao fresco sem traco em kg/m3 -> nao_disponivel (seca 2.031 nao serve; premissa F43)', None)
# --- SAHMENKO 2666: parede de betao normal; 2.400 = densidade seca do fabricante; traco sem agua -> nao_disponivel
ALVOS[143] = (2666, ND, None,
              "nao_disponivel (F55/#1831): os 2.400 kg/m3 da Tab.1 (p.921) e Tab.2 (p.927) sao 'rho_o - material dry density' do fabricante (seca) e nao "
              "servem como massa fresca; o traco da Tab.1 nao tem agua (330 + 750 + 1.000 = 2.080) e nao e somavel -> premissa F43 (2.400, o mesmo numero) "
              "no motor. A conversao do CO2 (F18) nao usou esta massa como divisor (95,5 kg/m2 / 0,12 m3; os 2.400 so entraram na verificacao)",
              'betao fresco; 2.400 e densidade seca do fabricante -> nao_disponivel (premissa F43 da o mesmo 2.400)', None)
# --- IRSHIDAT 3176 l.886: a seca cai; a alternativa (soma do traco 3.101) e SUSPEITO -> passa a aguardar #1832
RETAG_1832 = {886: (3176, "a densidade seca do controlo (1,97 g/cm3, ASTM C642, Sec.4.3 p.11) nao serve como massa fresca; a unica alternativa e a soma "
                          "do traco M14 da Tab.2 = 3.101 kg/m3, marcada SUSPEITO (tabela nao normalizada a 1 m3, como os pares WCB l.1937-1948) -> "
                          "este par passa a aguardar #1832; massa continua em branco")}

assert len(ALVOS) == 26 and len(RETAG_1832) == 1

gravar = '--gravar' in sys.argv
wb = openpyxl.load_workbook('meta_analysis_base.xlsx'); ws = wb['dados_fck']
h = [c.value for c in ws[1]]
C_TIPO, C_M, C_O, C_C, C_NOTA = (h.index(k) + 1 for k in ('a4_transporte_tipo', 'massa_volumica_kg_m3', 'massa_volumica_origem',
                                                           'massa_volumica_citacao', 'a4_leitura_nota'))
assert (C_TIPO, C_M, C_O, C_C, C_NOTA) == (87, 88, 89, 90, 97), (C_TIPO, C_M, C_O, C_C, C_NOTA)
n = {'massa': 0, 'origem': 0, 'citacao': 0, 'tipo87': 0, 'carimbo': 0, 'retag_1832': 0, 'ja_feitas': 0}
tocadas = []
for r, (rid, origem, massa, cit, resumo, novo_tipo) in sorted(ALVOS.items()):
    assert ws.cell(r, 1).value == rid, (r, ws.cell(r, 1).value, rid)
    nota = ws.cell(r, C_NOTA).value or ''
    assert 'aguarda #1831' in nota, (r, nota[:80])
    if MARCA in nota:
        n['ja_feitas'] += 1; continue
    assert ws.cell(r, C_M).value in (None, '') and ws.cell(r, C_O).value in (None, '') and ws.cell(r, C_C).value in (None, ''), r
    if massa is not None:
        ws.cell(r, C_M).value = massa; n['massa'] += 1
    ws.cell(r, C_O).value = origem; n['origem'] += 1
    ws.cell(r, C_C).value = cit; n['citacao'] += 1
    if novo_tipo:
        assert ws.cell(r, C_TIPO).value == 'indeterminado', (r, ws.cell(r, C_TIPO).value)
        ws.cell(r, C_TIPO).value = novo_tipo; n['tipo87'] += 1
    ws.cell(r, C_NOTA).value = nota + f' [{MARCA}, {NOTA_C}: {resumo}]'; n['carimbo'] += 1
    tocadas.append((r, rid, origem, massa))
for r, (rid, txt) in RETAG_1832.items():
    assert ws.cell(r, 1).value == rid
    nota = ws.cell(r, C_NOTA).value or ''
    if MARCA in nota:
        n['ja_feitas'] += 1; continue
    assert 'aguarda #1831' in nota and ws.cell(r, C_M).value in (None, '')
    ws.cell(r, C_NOTA).value = nota.replace('aguarda #1831 (massa volumica seca do endurecido)',
                                            'aguarda #1832 (soma do traco SUSPEITO; era #1831 ate 2026-11-22)') + f' [{MARCA}, {NOTA_C}: {txt}]'
    n['retag_1832'] += 1; n['carimbo'] += 1; tocadas.append((r, rid, 'retag->#1832', None))
print('celulas:', n, '| linhas tocadas', len(tocadas))
for t in tocadas:
    print('  ', t)
if gravar:
    wb.save('meta_analysis_base.xlsx'); print('GRAVADO meta_analysis_base.xlsx')
else:
    print('ensaio (sem --gravar): nada gravado')
