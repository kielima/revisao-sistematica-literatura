"""F17 — fila de perguntas F14/F16 respondidas pela Kie, uma a uma (2026-10-13 a 2026-10-15).

Cada caso foi relido pessoalmente no PDF (texto + figuras/tabelas) antes de ser levado a Kie.

1. 3372 MADDALENA: fica fora (decisao «Mantem fora, como a McDONALD»). Sem alteracao de dados.
   3418 McDONALD: exclusao confirmada (massa volumica endurecida nao e divisor aceitavel).
2. 4650 KIM: co2_valor das linhas 1665-1667 estava 10x o da figura -> 1,2 / 0,526 / 0,0689. Continua
   NAO CONVERTIDO (unidade impossivel e CO2 so do cimento).
3. 3069 JATIVA: E2_co2 Rejeitado (precedente UNGUREANU 3917: o unico CO2 e o factor de literatura
   0,86 t CO2/t de cimento, sem ACV propria).
4. 4718 ALBERTI: E2_co2 Rejeitado pela regra 12 (precedente RAJAGOPAL 4550): kg CO2-eq sem unidade de
   referencia impressa; os valores batem com a armadura por m2, nao com o betao.
6. 2582 ASSUNCAO: convertido pela excepcao 5b (precedente HAN 3881). Tab.5 lida como kg CO2-eq/kg de
   argamassa (rotulo «/(m3.MPa)» incoerente) x massa especifica da Tab.4 (p.66, procedimento descrito pela
   propria autora) -> 485,0 / 417,6 / 343,2. QA 1 -> 0,5 (UF impressa nao e inequivoca).
7. 4511 LOS SANTOS-ORTEGA: regra MULLER. fck aos 28 d da ref.[16] (Fraile-Garcia et al. 2017, Materials 10,
   817, Tab.5): H-0 39,54 e H-50 31,21 MPa; mesmos autores, central, RCA, niveis, cimento e agua; agregados
   diferem (areia 765 vs 833,3; brita 6/12 405,6 vs 400). QF 0 -> 0,5.
8. 3414 ABDULKAREEM: S0, S1 e S2 (Kie: «Pode aceitar os 3»). Volume do modulo pelas cotas da Fig.3
   (0,13862 m3; 45 modulos = 6,238 m3); GWP da fase de producao lido por pixel na Fig.5. S1 com fck 19,96
   lido por pixel, gravado 20,0 por decisao da Kie.
9. 2731 MA: as 7 classes da Tab.A1 (Kie: «aceitar as 7 classes»). CO2 = exergia «Climate warming» x 1.000
   (reconciliacao com a Tab.6: 33,11 vs 33,16 TJ) / 4.400 kJ/kg CO2 (Tab.A5).
10. 3285 AMIRI: par do cenario Con (Kie). ~1.650 t CO2 eq do sistema Structures (Fig.3 por pixel; confere com
   a Fig.5) / 2.818 m3 de betao (Tab.1) = 585,5 kg/m3, familia concreto_armado. QF 0 -> 0,5.
11. 3852 MILLER: medianas Monte Carlo lidas da Fig.2 (Kie: «aceitar os 2 pares»), IQR como ic_co2.
   QF 0 -> 1,0.
"""
import json
import re

import openpyxl

BASE = 'meta_analysis_base.xlsx'
ART = 'articles_final.xlsx'
FAM = 'lotes_familia/familias_revarredura.json'
HOJE = '2026-10-15'


def clean(s):
    return re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', str(s))


def obs(ws, r, txt):
    ws.cell(r, 13).value = clean(f'{ws.cell(r, 13).value or ""} [F17 {HOJE}: {txt}]'.strip())


def nova_linha(ws, modelo_r):
    ncol = ws.max_column
    r = ws.max_row + 1
    for c in range(1, ncol + 1):
        ws.cell(r, c).value = ws.cell(modelo_r, c).value
    for c in list(range(23, 34)) + list(range(38, 42)) + list(range(44, 52)):
        ws.cell(r, c).value = None
    return r


def m3(ws, r, co2, unidade, original, local, conversao):
    ws.cell(r, 14).value = co2
    ws.cell(r, 15).value = unidade
    ws.cell(r, 34).value = clean(original)
    ws.cell(r, 35).value = clean(local)
    ws.cell(r, 36).value = clean(conversao)
    ws.cell(r, 37).value = co2
    ws.cell(r, 45).value = 'nenhum'
    ws.cell(r, 47).value = 'sim'


def main():
    wb = openpyxl.load_workbook(BASE)
    ws = wb['dados_fck']
    fam = json.load(open(FAM, encoding='utf-8'))
    log = []

    # --- 2. KIM 4650 ---
    for r, antes, depois in ((1665, 12, 1.2), (1666, 5.26, 0.526), (1667, 0.689, 0.0689)):
        assert ws.cell(r, 1).value == 4650 and ws.cell(r, 14).value == antes, r
        ws.cell(r, 14).value = depois
        obs(ws, r, f'co2_valor {antes} -> {depois} (o banco tinha 10x o valor da figura); continua NAO CONVERTIDO')
        log.append((r, 4650, 'co2_valor', depois))

    # --- 6. ASSUNCAO 2582 ---
    for r, traco, publ, dens in ((80, 'C', 0.243, 1996), (81, 'B-15', 0.209, 1998), (3, 'B-30', 0.176, 1950)):
        assert ws.cell(r, 1).value == 2582 and abs(ws.cell(r, 14).value - publ) < 1e-9, r
        val = round(publ * dens, 1)
        ws.cell(r, 34).value = f'{publ} «kg CO2-eq/(m3.MPa)» (Tab.5 p.67, traco {traco}), rotulo incoerente'
        ws.cell(r, 35).value = 'Tab.5 p.67 (Mudancas climaticas); Tab.4 p.66 (massa especifica no estado fresco); p.66'
        ws.cell(r, 36).value = clean(
            f'reconstituido (excepcao 5b, precedente HAN 3881; decisao da Kie {HOJE}): o valor da Tab.5 e kg CO2-eq '
            f'por kg de argamassa (Fig.16: traco «para 1 kg de argamassa»; p.66: GaBi «por MPa em 1 kg de argamassa», '
            f'depois x massa especifica). {publ} x {dens} kg/m3 (Tab.4) = {val} kg CO2-eq/m3. Verificacao: '
            f'{publ}/kg de cimento do traco = 0,97-1,01 kg CO2/kg (CP V-ARI). Confianca baixa: o rotulo impresso '
            '«/(m3.MPa)» contradiz esta leitura')
        ws.cell(r, 37).value = val
        ws.cell(r, 45).value = 'nenhum'
        ws.cell(r, 47).value = 'sim'
        obs(ws, r, f'CO2 reconstituido {val} kg/m3 (excepcao 5b), confianca baixa; ver co2_conversao')
        log.append((r, 2582, traco, val))

    # --- 7. LOS SANTOS-ORTEGA 4511 ---
    fonte16 = ('ref.[16] do artigo: Fraile-Garcia, Ferreiro-Cabello, Lopez-Ochoa, Lopez-Gonzalez (2017), '
               'Materials 10, 817, Tab.5 (Hormigones Ebro, 28 d)')
    for r, cod, fck, sd in ((1478, 'H-0', 39.54, 1.43), (1479, 'H-50', 31.21, 1.23)):
        assert ws.cell(r, 1).value == 4511, r
        ws.cell(r, 8).value = fck
        ws.cell(r, 10).value = 28
        ws.cell(r, 12).value = clean(f'[FONTE EXTERNA - regra MULLER] {fonte16}: {cod} {fck} +- {sd} MPa')
        obs(ws, r, f'fck {fck} MPa da ref.[16] (regra MULLER, decisao da Kie): mesmos autores, central, RCA, niveis '
                   'de substituicao, cimento (300 kg) e agua (163 kg); agregados diferem (areia 765 vs 833,3; brita '
                   '6/12 405,6 vs 400 kg/m3) - confianca media. fonte_externa_resistencia = ref.[16] (ramo de '
                   'citacao do PRISMA). DP da ref.[16] nao gravado como IC (outro estudo, regra do QG)')
        log.append((r, 4511, cod, fck))

    # --- 8. ABDULKAREEM 3414 ---
    r0 = 419
    assert ws.cell(r0, 1).value == 3414
    vol = 6.238
    vol_cit = ('Fig.3 p.4: modulo macico de 900 mm de altura, planta em L 500x400 mm menos recorte trapezoidal '
               '(350+263)/2 x 150 mm = 0,15403 m2 -> 0,13862 m3/modulo; 45 modulos por 20 m (p.4) = 6,238 m3. '
               'Verificacao: 330 kg/modulo (p.4) / 0,13862 = 2.381 kg/m3')
    cen = [  # (linha, mistura, fck, fonte_fck, gwp_20m, co2, familia)
        (r0, 'S0 -- barreira acustica pre-fabricada de betao Portland (cenario de referencia)', 32.0,
         "texto p.6, sec.3: 'S0 having the highest strength (32 MPa)'; Fig.5 'MPa (28 days)'", 4062, 651.2, 'opc'),
        (None, 'S1 -- barreira acustica pre-fabricada de geopolimero (CFA+GBFS, 10% activador, Tab.1)', 20.0,
         'Fig.5 p.7, marcador no eixo secundario «Compressive strength (MPa)», «MPa (28 days)», lido por pixel = '
         '19,96; gravado 20,0 por decisao da Kie (2026-10-14: «Pode aceitar os 3»)', 2264, 362.8, 'geopolimero'),
        (None, 'S2 -- barreira acustica pre-fabricada de geopolimero (GBFS+metacaulino, 15% activador, Tab.1)', 24.9,
         'Fig.5 p.7, marcador no eixo secundario, «MPa (28 days)», lido por pixel = 24,93', 3773, 604.8,
         'geopolimero'),
    ]
    for r, mat, fck, ffck, gwp, co2, familia in cen:
        if r is None:
            r = nova_linha(ws, r0)
        ws.cell(r, 7).value = mat
        ws.cell(r, 8).value = fck
        ws.cell(r, 10).value = 28
        ws.cell(r, 12).value = clean(ffck)
        m3(ws, r, co2, 'kg CO2-eq/m3 (GWP da producao de 20 m de barreira / volume de betao dos 45 modulos)',
           f'{gwp} kg CO2 eq./20 m (fase «LHNB production», Fig.5 p.7, leitura por pixel)',
           'Fig.5 p.7 (GWP); Fig.3 e texto p.4 (modulo e n.o de modulos)',
           f'calculado: {gwp} / {vol} m3 = {co2} kg CO2-eq/m3 (total / divisor das cotas impressas; confere com as '
           'percentagens do texto p.6: S1 -44%, S2 -7% face a S0)')
        ws.cell(r, 23).value = vol
        ws.cell(r, 24).value = 'medido_elemento_real'
        ws.cell(r, 25).value = clean(vol_cit)
        obs(ws, r, 'par da releitura F14 aceite pela Kie (S0 confianca media; S1/S2 confianca baixa: fck e GWP so por '
                   'pixel, mesmo modulo da Fig.3 aplicado aos tres pre-fabricados, p.4 e p.6)')
        fam[f'3414|{mat}'] = familia
        log.append((r, 3414, mat[:3], fck, co2, familia))

    # --- 9. MA 2731 ---
    r0 = 169
    assert ws.cell(r0, 1).value == 2731
    ma = [('C50', 2471.09), ('C20', 1456.04), ('C25', 1709.52), ('C30', 1871.19), ('C35', 2102.21),
          ('C40', 2240.58), ('C45', 2332.72)]
    for i, (cls, ex) in enumerate(ma):
        r = r0 if i == 0 else nova_linha(ws, r0)
        co2 = round(ex * 1000 / 4400, 1)
        mat = f'Betao {cls} (classe chinesa; factor da Tabela A1 calculado pelos autores)'
        ws.cell(r, 7).value = mat
        ws.cell(r, 8).value = float(cls[1:])
        ws.cell(r, 9).value = cls
        ws.cell(r, 10).value = None
        ws.cell(r, 11).value = None
        ws.cell(r, 12).value = f'Tabela A1 p.14 (e Tabela A8 p.17), «Concrete {cls}» - classe de projecto, sem ensaio'
        m3(ws, r, co2, 'kg CO2/m3 (exergia «Climate warming» convertida)',
           f'{ex} kJ («Climate warming», Tabela A1, unidade impressa «kJ/kg or kJ/m3») - Concrete {cls}',
           'Tabela A1 p.14; Tabela A5 p.15 (4.400 kJ/kg CO2); Tabela 6 p.10 e Tabela A8 p.17 (reconciliacao)',
           f'calculado: {ex} x 1.000 / 4.400 = {co2} kg CO2/m3. O x1.000 (valor por dm3) sai da reconciliacao com a '
           'Tab.6: 54,8 TJ de Climate warming na producao de materiais - aco/chapa/tubo/cordao/PVC/tinta (Tab.A8 x '
           'Tab.A1) 21,64 TJ = 33,16 TJ, e o betao (m3 da Tab.A8 x factores x 1.000) da 33,11 TJ (0,15%). O factor '
           '4.400 kJ/kg CO2 confere no cimento (Tab.A7 = 4.295,19 = Climate warming do OPC 42,5)')
        if i == 0:
            obs(ws, r, 'linha passa a C50 do betao (o 0,532 gravado era o factor do CIMENTO, Tab.A6); +6 classes')
        else:
            ws.cell(r, 13).value = clean(f'[F17 {HOJE}: classe {cls} da Tab.A1 (decisao da Kie: aceitar as 7 classes); '
                                         'confianca baixa: factor x1.000 inferido da reconciliacao, sem traco impresso]')
        fam[f'2731|{mat}'] = 'opc'
        log.append((r, 2731, cls, co2))

    # --- 10. AMIRI 3285 ---
    r = 338
    assert ws.cell(r, 1).value == 3285
    mat = ('Edificio Veroeld (Reykjavik), cenario Con - sistema Structures em betao armado (30-32 MPa 2.780 m3 + '
           '50 MPa 38 m3, armadura, serralharia, EPS, madeira)')
    ws.cell(r, 7).value = mat
    m3(ws, r, 585.5, 'kg CO2-eq/m3 de betao do sistema Structures (inclui armadura e restantes materiais; A1-A4)',
       '~1.650 t CO2 eq (Fig.3 p.8, barra «Structures» do cenario Con, sem rotulo; leitura por pixel)',
       'Fig.3 p.8; Fig.5 p.9 (verificacao); Tabela 1 p.3 (volumes)',
       'calculado: 1.650.000 kg / 2.818 m3 (Tab.1: 2.780 + 38) = 585,5 kg CO2-eq/m3. Verificacao: barra total Con '
       '2.667 t vs 2.666,3 t impressos (Fig.5); Con -> ConWood nas estruturas 833 t vs 830,9 t impressos. O total '
       'inclui 285 t de armadura, 37,0 t de steel works, 3,4 t de EPS e 40 m de madeira, nao separaveis')
    ws.cell(r, 23).value = 2818
    ws.cell(r, 24).value = 'medido_elemento_real'
    ws.cell(r, 25).value = 'Tabela 1 p.3: sistema 2. Structures, Concrete 30-32 MPa 2780 m3 + Concrete 50 MPa 38 m3'
    obs(ws, r, 'par do cenario Con aceite pela Kie (regra de 26/09: total de sistema estrutural / volume de betao '
               'impresso, familia concreto_armado); confianca baixa (pixel; materiais nao separaveis); fck 31 = ponto '
               'medio da faixa impressa 30-32 MPa. OptCon/ConWood/Wood continuam NAO CONVERTIDO')
    fam[f'3285|{mat}'] = 'concreto_armado'
    log.append((r, 3285, 'Con', 585.5))

    # --- 11. MILLER 3852 ---
    r0 = 1124
    assert ws.cell(r0, 1).value == 3852
    mil = [  # (linha, mistura, co2, iqr, iqr_cit)
        (r0, 'Concreto CA-HC (475 kg/m3 de cimenticios: 403 PC + 71 FA, Tab.1; especificacao Caltrans, 25 MPa aos 28 d)',
         334.1, 'P25-P75 = 240-466 kg CO2-eq/m3 (impresso p.9; leitura da Fig.2: 240,0-467,4; mediana 334,1)',
         'p.9: «The range between the 25% and the 75% quantiles of GHG emissions for the CA-HC mixture is 240-466 kg '
         'CO2-eq m-1» (gralha de unidade; a Fig.2 e por m3); Monte Carlo n = 100.000 (sec.2.2.1)'),
        (None, 'Concreto 300C-15FA (300 kg/m3 de cimenticios: 255 PC + 45 FA, Tab.1; mesmo alvo de 25 MPa aos 28 d)',
         224.5, 'P25-P75 = 160,7-314,0 kg CO2-eq/m3 (leitura da Fig.2; mediana 224,5)',
         'Fig.2 p.10 lida por pixel; texto p.9: amplitude «2/3rds» da do CA-HC (lida: 0,68); Monte Carlo n = 100.000'),
    ]
    for r, mat, co2, iqr, cit in mil:
        if r is None:
            r = nova_linha(ws, r0)
        ws.cell(r, 7).value = mat
        ws.cell(r, 8).value = 25
        ws.cell(r, 10).value = 28
        m3(ws, r, co2, 'kg CO2-eq/m3 (mediana da distribuicao Monte Carlo)',
           'distribuicao Monte Carlo de 100.000 simulacoes por m3 (Fig.2 p.10); sem valor central impresso',
           'Fig.2 p.10 (histograma); p.9 (IQR); Fig.4 p.11 (reducao media)',
           f'mediana lida da Fig.2: acumulado das barras ate 50.000 simulacoes = {co2} kg CO2-eq/m3. Calibracao validada '
           'pelo IQR impresso do CA-HC (240-466 vs 240,0-467,4 lido); razao das medianas 224,5/334,1 = -32,8% vs '
           '-33% da media na Fig.4. A media nao e recuperavel (cauda > 1.000 kg/m3 fora do eixo)')
        ws.cell(r, 30).value = iqr
        ws.cell(r, 31).value = 'intervalo_interquartil'
        ws.cell(r, 32).value = 100000
        ws.cell(r, 33).value = clean(cit)
        obs(ws, r, 'mediana Monte Carlo aceite pela Kie (2 pares); confianca baixa: lida do histograma, fck de projecto')
        fam[f'3852|{mat}'] = 'scm'  # F12: cinza volante juntada na mistura -> scm
        log.append((r, 3852, mat[9:18], co2))

    wb.save(BASE)
    with open(FAM, 'w', encoding='utf-8') as f:
        json.dump(fam, f, ensure_ascii=False, indent=0)

    # --- articles_final: rejeicoes e itens E4 ---
    wa = openpyxl.load_workbook(ART)
    wsa = wa['Articles']
    rej = {
        3069: 'E2_co2 Rejeitado (Kie): o unico CO2 e o factor de literatura 0,86 t CO2/t de cimento, sem ACV propria '
              'do estudo - precedente UNGUREANU 3917',
        4718: 'E2_co2 Rejeitado (Kie), regra 12 (precedente RAJAGOPAL 4550): Tab.1 p.4 da GWP 2,39/5,30 kg CO2 eq sem '
              'unidade de referencia impressa; os valores batem com a armadura (fibra vs malha) por m2, nao com o betao',
    }
    for r, txt in rej.items():
        assert wsa.cell(r, 20).value == 'Elegível', r
        wsa.cell(r, 20).value = 'Rejeitado'
        wsa.cell(r, 40).value = 'Rejeitado'
        wsa.cell(r, 43).value = 2
        wsa.cell(r, 44).value = 'E2_co2'
        wsa.cell(r, 32).value = clean(f'{wsa.cell(r, 32).value or ""} [F17 {HOJE}: {txt}]'.strip())
    e4 = {2582: (47, 0.5, 'QA 1 -> 0,5: a UF impressa «/(m3.MPa)» contradiz a leitura usada (excepcao 5b)'),
          4511: (52, 0.5, 'QF 0 -> 0,5: fck da ref.[16] ligado ao CO2 pelo nome do traco, agregados diferentes'),
          3285: (52, 0.5, 'QF 0 -> 0,5: CO2 do sistema Structures ligado a classe 30-32 MPa por inferencia'),
          3852: (52, 1.0, 'QF 0 -> 1,0: cada mediana pertence a uma mistura identificada com o seu alvo de 25 MPa')}
    novo_e4 = {}
    for r, (c, v, txt) in e4.items():
        wsa.cell(r, c).value = v
        tot = sum(float(wsa.cell(r, k).value or 0) for k in (47, 48, 49, 50, 51, 52, 55))
        wsa.cell(r, 53).value = tot
        wsa.cell(r, 54).value = 'principal' if tot >= 4.0 else 'sensibilidade'
        wsa.cell(r, 32).value = clean(f'{wsa.cell(r, 32).value or ""} [F17 {HOJE}: {txt}; E4 = {tot}]'.strip())
        novo_e4[r] = (tot, wsa.cell(r, 54).value)
    wa.save(ART)

    wb = openpyxl.load_workbook(BASE)
    ws = wb['dados_fck']
    for r in range(2, ws.max_row + 1):
        rid = ws.cell(r, 1).value
        if rid in novo_e4:
            ws.cell(r, 21).value, ws.cell(r, 22).value = novo_e4[rid]
    wb.save(BASE)

    for x in log:
        print(x)
    print('E4:', novo_e4)


if __name__ == '__main__':
    main()
