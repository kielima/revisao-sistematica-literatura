"""F14 — pares novos da releitura dos Elegiveis sem par (2026-10-11), so os verificados pessoalmente.

Kie (2026-10-11): «Quero revisar esses 129 artigos. Reler com mais detalhamento mais uma vez para realmente
ter certeza de que nao da para converter em CO2/m3 e/ou CO2/MPa.» Os subagentes (resultado_loteNN.json)
propuseram pares; aqui so entram os que conferi pessoalmente no PDF (texto + figuras renderizadas) e que
usam apenas numeros impressos no proprio artigo (regra «nao vamos assumir nada»):

- 3095 TEFA: linha legada 839 desdobrada nos 4 ligantes cimenticios. CO2 nativo em kg CO2-eq/m3 de ligante
  (pasta) da tabela sob a Fig.9a (p.10); fck aos 28 d da tabela sob a Fig.5 (p.8), cubos de pasta de 20 mm.
  Os alcali-ativados (AA-*) ficam fora: fck 3,0-8,6 MPa < 20 MPa (regra da purga de 2026-09-08).
- 3170 SAMUVEL: CO2 = soma Tab.2 (traco, kg/m3) x Tab.4 (factores t-CO2/t), sem agua (sem factor no artigo);
  confere com as percentagens da Fig.10d. fck aos 28 d do texto sec.4.2.2 (nGS6 e nGS9 = 40,69 x (1 + %
  impresso)). Linha 880 (que tinha a soma dos factores 3,2628) passa a nGS12; +5 linhas.
- 3237 KANAGARAJ: misturas ECA0 (sem argila expandida). CO2 = soma Tab.2 x factores impressos na sec.6.3.3
  (FA 0,004; GGBS 0,052; agregados 0,0048; SH 1,915; SS 1,222), sem agua nem superplastificante (sem factor);
  confere com os 0,164 (4 M) e 0,46 (12 M) que o artigo imprime. fck lido por pixel da Fig.7 (p.7), escala
  0-60 MPa. Idade nao impressa; provete ambiguo (cilindros 150x300 E cubos 150, sec.3.2.1) -> volume vazio.
  A linha legada 937 continua NAO CONVERTIDO (par misturado, F10).
"""
import json
import re

import openpyxl

BASE = 'meta_analysis_base.xlsx'
FAM = 'lotes_familia/familias_revarredura.json'
HOJE = '2026-10-11'


def clean(s):
    return re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', str(s))


TEFA_CONV = 'nenhuma - publicado em kg CO2-eq/m3 de ligante (pasta), tabela sob a Fig.9a p.10'
TEFA = [  # (mistura, fck, co2, familia, subfamilia, designacao)
    ('C-II/B', 'pasta de cimento CEM II/B-L 32.5R (referencia), l/s 0,4', 45.4, 1212, 'opc', 'cem_ii_b',
     'CEM II/B-L 32.5R'),
    ('C-IV/A', 'pasta de cimento CEM IV/A 32.5N, l/s 0,4', 48.7, 1193, 'opc', 'cem_iv', 'CEM IV/A 32.5N'),
    ('C-IV/B', 'pasta de cimento CEM IV/B 32.5N, l/s 0,4', 45.9, 895, 'opc', 'cem_iv', 'CEM IV/B 32.5N'),
    ('C-IV/H', 'pasta 50% CEM IV/B 32.5N + 50% argila residual (substituicao feita no estudo), l/s 0,4', 35.8, 458,
     'scm', None, None),
]

SAMUVEL_FATORES = 'FA 0,004; GGBFS 0,052; nGS 0,065; fillers 0,0048; Na2SiO3 1,222; NaOH 1,915 t-CO2/t (Tab.4 p.16)'
SAMUVEL = [  # (codigo, FA, nGS, fck, fonte_fck, co2)
    ('nGS0', 280, 0, 40.69, '40,69 MPa impresso (p.7)', 348.94),
    ('nGS3', 268, 12, 47.07, '47,07 MPa impresso (p.7)', 349.67),
    ('nGS6', 256, 24, 53.81, 'derivado: 40,69 x 1,3224 (aumento de 32,24% impresso, p.7)', 350.41),
    ('nGS9', 244, 36, 58.14, 'derivado: 40,69 x 1,4289 (aumento de 42,89% impresso, p.7)', 351.14),
    ('nGS12', 232, 48, 60.37, '60,37 MPa impresso (p.7 e Tab.5 p.17)', 351.87),
    ('nGS15', 220, 60, 56.26, '56,26 MPa impresso (p.7)', 352.60),
]

# Fig.7 p.7 a 400 dpi: rotulo 0 em y=916,5 px, rotulo 60 em y=85,5 px (13,85 px/MPa); topo de cada barra
KANA = [  # (mistura, SH, SS, topo_px, fck)
    ('ECA0-4-A', 29, 74, 394, 37.7), ('ECA0-4-S', 29, 74, 370, 39.5),
    ('ECA0-8-A', 59, 147, 346, 41.2), ('ECA0-8-S', 59, 147, 323, 42.9),
    ('ECA0-12-A', 88, 221, 309, 43.9), ('ECA0-12-S', 88, 221, 271, 46.7),
]


def kana_co2(sh, ss):
    return round(275 * 0.004 + 275 * 0.052 + (510 + 999) * 0.0048 + sh * 1.915 + ss * 1.222, 1)


def preencher(ws, r, modelo, ncol):
    for c in range(1, ncol + 1):
        ws.cell(r, c).value = modelo[c - 1]


def main():
    wb = openpyxl.load_workbook(BASE)
    ws = wb['dados_fck']
    fam = json.load(open(FAM, encoding='utf-8'))
    ncol = ws.max_column
    novas = []

    # --- 3095 TEFA ---
    r0 = 839
    assert ws.cell(r0, 1).value == 3095
    modelo = [ws.cell(r0, c).value for c in range(1, ncol + 1)]
    obs0 = str(modelo[12] or '')
    destino = [r0] + [ws.max_row + i for i in range(1, len(TEFA))]
    for (cod, desc, fck, co2, familia, sub, desig), r in zip(TEFA, destino):
        preencher(ws, r, modelo, ncol)
        mat = clean(f'Ligante puro (pasta) para estabilizacao de agregados reciclados de RCD: {cod} - {desc}')
        ws.cell(r, 7).value = mat
        ws.cell(r, 8).value = fck
        ws.cell(r, 10).value = 28
        ws.cell(r, 11).value = 'cubo de pasta 20 mm (moldes plasticos, 10 replicas, sec.2.3 p.5)'
        ws.cell(r, 12).value = f'tabela sob a Fig.5 p.8, sigma_c,max aos 28 d: {cod} {fck}'
        ws.cell(r, 13).value = clean(f'{obs0} [F14 {HOJE}: linha legada desdobrada por ligante; esta linha = {cod}. '
                                     'Os alcali-ativados AA-* ficam fora (fck 3,0-8,6 MPa < 20)]')
        ws.cell(r, 14).value = co2
        ws.cell(r, 15).value = 'kg CO2-eq/m3 de ligante (pasta), FU = 1 m3 de ligante'
        ws.cell(r, 16).value = 'tabela sob a Fig.9a p.10'
        ws.cell(r, 34).value = f'{co2} kg CO2-eq/m3 de ligante ({cod})'
        ws.cell(r, 35).value = 'tabela sob a Fig.9a p.10 (percentagens da mesma figura face a 1212)'
        ws.cell(r, 36).value = TEFA_CONV
        ws.cell(r, 37).value = co2
        ws.cell(r, 45).value = 'nenhum'
        ws.cell(r, 47).value = 'sim'
        for c in (48, 49, 50, 51):
            ws.cell(r, c).value = None
        if sub:
            ws.cell(r, 48).value = sub
            ws.cell(r, 49).value = desig
            ws.cell(r, 50).value = 'EN 197-1 (citada pelo artigo)'
            ws.cell(r, 51).value = 'sec.2.1 p.3 (Reference and low-clinker cements), conforming to EN 197-1; F14 2026-10-11'
        fam[f'3095|{mat}'] = familia
        novas.append((r, 3095, cod, fck, co2, familia))

    # --- 3170 SAMUVEL ---
    r0 = 880
    assert ws.cell(r0, 1).value == 3170
    modelo = [ws.cell(r0, c).value for c in range(1, ncol + 1)]
    obs0 = str(modelo[12] or '')
    ordem = sorted(SAMUVEL, key=lambda m: m[0] != 'nGS12')  # nGS12 reaproveita a linha 880
    destino = [r0] + [ws.max_row + i for i in range(1, len(ordem))]
    for (cod, fa, ngs, fck, fonte, co2), r in zip(ordem, destino):
        preencher(ws, r, modelo, ncol)
        conta = (f'FA {fa}x0,004 + GGBFS 120x0,052 + nGS {ngs}x0,065 + fillers 1583x0,0048 + Na2SiO3 168x1,222 '
                 f'+ NaOH 67,2x1,915 = {co2} kg CO2-eq/m3')
        mat = clean(f'concreto alcali-ativado com nano-GGBFS (AANC), traco {cod} ({ngs} kg/m3 de nGS)')
        ws.cell(r, 7).value = mat
        ws.cell(r, 8).value = fck
        ws.cell(r, 10).value = 28
        ws.cell(r, 11).value = 'cubo 150 mm (IS 516), media de 3'
        ws.cell(r, 12).value = f'texto sec.4.2.2 p.7: {fonte}'
        ws.cell(r, 13).value = clean(f'{obs0} [F14 {HOJE}: CO2 por soma Tab.2 x Tab.4 (agua sem factor no artigo, '
                                     'excluida tambem pelos autores); confere com as percentagens da Fig.10d. '
                                     f'Esta linha = {cod}]')
        ws.cell(r, 14).value = co2
        ws.cell(r, 15).value = 'kg CO2-eq/m3 (soma traco x factores)'
        ws.cell(r, 16).value = 'Tab.2 p.5 (traco) x Tab.4 p.16 (factores)'
        ws.cell(r, 34).value = f'factores {SAMUVEL_FATORES}; traco Tab.2 p.5 ({cod})'
        ws.cell(r, 35).value = 'Tab.2 p.5 e Tab.4 p.16; verificacao Fig.10d'
        ws.cell(r, 36).value = f'calculado: {conta}'
        ws.cell(r, 37).value = co2
        ws.cell(r, 45).value = 'nenhum'
        ws.cell(r, 47).value = 'sim'
        fam[f'3170|{mat}'] = 'geopolimero'
        novas.append((r, 3170, cod, fck, co2, 'geopolimero'))

    # --- 3237 KANAGARAJ ---
    r0 = 937
    assert ws.cell(r0, 1).value == 3237
    modelo = [ws.cell(r0, c).value for c in range(1, ncol + 1)]
    base = ws.max_row
    for i, (cod, sh, ss, topo, fck) in enumerate(KANA, start=1):
        r = base + i
        preencher(ws, r, modelo, ncol)
        co2 = kana_co2(sh, ss)
        cura = 'cura ambiente' if cod.endswith('A') else 'cura solar'
        mol = cod.split('-')[1]
        conta = (f'FA 275x0,004 + GGBS 275x0,052 + areia 510x0,0048 + brita 999x0,0048 + SH {sh}x1,915 '
                 f'+ SS {ss}x1,222 = {co2} kg CO2-eq/m3')
        mat = clean(f'SCLGC geopolimerico autocompactavel sem argila expandida, mistura {cod} (NaOH {mol} M, {cura})')
        ws.cell(r, 7).value = mat
        ws.cell(r, 8).value = fck
        ws.cell(r, 10).value = None
        ws.cell(r, 11).value = 'nao especificado (sec.3.2.1 cita cilindros 150x300 e cubos 150)'
        ws.cell(r, 12).value = (f'Fig.7 p.7 lida por pixel a 400 dpi (rotulo 0 em y=916,5; 60 em y=85,5; '
                                f'topo da barra y={topo}) = {fck} MPa')
        ws.cell(r, 13).value = clean(f'[F14 {HOJE}: mistura ECA0 da Tab.2 p.4; CO2 por soma com factores impressos '
                                     'na sec.6.3.3; confere com 0,164 (4 M) e 0,46 (12 M) do texto p.15. Idade do '
                                     'ensaio nao impressa. Cura A e S com o mesmo traco e o mesmo CO2]')
        ws.cell(r, 14).value = co2
        ws.cell(r, 15).value = 'kg CO2-eq/m3 (soma traco x factores)'
        ws.cell(r, 16).value = 'Tab.2 p.4 (traco) x sec.6.3.3 p.15 (factores)'
        ws.cell(r, 23).value = None
        ws.cell(r, 24).value = 'indisponivel'
        ws.cell(r, 25).value = ('sec.3.2.1: cilindros 150x300 E cubos 150 para a compressao; nao diz qual deu a Fig.7')
        for c in (26, 27, 28, 29, 30, 31, 32, 33):
            ws.cell(r, c).value = None
        ws.cell(r, 34).value = ('factores sec.6.3.3 p.15: FA 0,004; GGBS 0,052; agregados 0,0048; SH (100% solido) '
                                f'1,915; SS 1,222 t-CO2/t; traco Tab.2 p.4 ({cod})')
        ws.cell(r, 35).value = 'Tab.2 p.4 e sec.6.3.3 p.15'
        ws.cell(r, 36).value = f'calculado: {conta}'
        ws.cell(r, 37).value = co2
        ws.cell(r, 45).value = 'nenhum'
        ws.cell(r, 47).value = 'sim'
        fam[f'3237|{mat}'] = 'geopolimero'
        novas.append((r, 3237, cod, fck, co2, 'geopolimero'))

    wb.save(BASE)
    with open(FAM, 'w', encoding='utf-8') as f:
        json.dump(fam, f, ensure_ascii=False, indent=0)
    for n in novas:
        print(n)


if __name__ == '__main__':
    main()
