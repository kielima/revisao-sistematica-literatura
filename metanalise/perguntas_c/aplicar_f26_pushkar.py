"""F26 — PUSHKAR 4580 e 4267 rejeitados em E2_co2 (decisao da Kie, 2026-10-16: «Pode retirar e rejeitar os dois»).

Pergunta aberta C3 de metanalise/DECISOES_METANALISE.md. Releitura pessoal dos dois PDFs a 2026-10-16 (texto completo
+ imagem da Tab.8 da 4580, p.6):

- 4580 PUSHKAR 2019 (Sustainability 11, 4083) e 4267 PUSHKAR 2019b (Appl. Sci. 9, 3620) modelam o cimento com o
  processo Ecoinvent «Cement mortar, at plant/CH U» (4580 Tab.7 p.6; 4267 Tab.3 p.5, «CEM I 42.4N production»).
  A Tab.8 da 4580 imprime o factor que dai sai: 0,192 kg CO2 por kg de «cement production» (CEM I ronda 0,8-0,9).
- O resultado e coerente com o proprio inventario (382 kg x 0,192 = 73 kg + agregados e transporte = ~89 kg/m3),
  por isso todas as misturas (28 a 75 MPa) dao 86-90 kg CO2/m3: o numero publicado nao e o CO2 de um betao com
  382-386 kg de cimento. Recalcular com outro factor seria assumir um dado que o artigo nao da.
- 21 pares (20 da 4580, 1 da 4267 lido no eixo sem rotulo da Fig.5), ci 1,5-3,2 (mediana geral 8,7); sem eles a
  mediana da familia «agregado reciclado» passa de 10,12 para 10,61.

Precedente: F18/F20 (CO2 que nao representa o betao descrito sai em E2_co2).
"""
import re

import openpyxl

ART = 'articles_final.xlsx'
META = 'meta_analysis_base.xlsx'
HOJE = '2026-10-16'
ROWS = (4267, 4580)
MOTIVO = ('o cimento foi modelado com o processo Ecoinvent «Cement mortar, at plant/CH U» (argamassa, nao cimento; '
          '4580 Tab.7-8 p.6: 0,192 kg CO2/kg; 4267 Tab.3 p.5) - o CO2 publicado (~86-90 kg/m3 para 382-386 kg de '
          'cimento) nao representa o betao descrito; recalcular exigiria assumir outro factor')


def clean(s):
    return re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', str(s))


def main():
    wa = openpyxl.load_workbook(ART)
    ws = wa['Articles']
    for r in ROWS:
        assert ws.cell(r, 20).value == 'Elegível' and ws.cell(r, 40).value == 'Aceito', r
        ws.cell(r, 20).value = 'Rejeitado'
        ws.cell(r, 40).value = 'Rejeitado'
        ws.cell(r, 43).value = 2
        ws.cell(r, 44).value = 'E2_co2'
        ws.cell(r, 32).value = clean(f'{ws.cell(r, 32).value or ""} [F26 {HOJE} (Kie: «Pode retirar e rejeitar os '
                                     f'dois»): E2_co2 Rejeitado - {MOTIVO}]'.strip())
    wa.save(ART)

    wb = openpyxl.load_workbook(META)
    wd = wb['dados_fck']
    n = 0
    for r in range(2, wd.max_row + 1):
        if wd.cell(r, 1).value not in ROWS or wd.cell(r, 37).value is None:
            continue
        antes = wd.cell(r, 37).value
        wd.cell(r, 37).value = None
        wd.cell(r, 44).value = None
        wd.cell(r, 36).value = clean(f'NAO CONVERTIDO - F26 {HOJE}: {MOTIVO}')[:1500]
        wd.cell(r, 13).value = clean(f'{wd.cell(r, 13).value or ""} [CO2 {antes} -> NAO CONVERTIDO {HOJE} '
                                     f'(F26, verificacao pessoal): {MOTIVO}]')
        n += 1
    wb.save(META)
    print('artigos rejeitados', len(ROWS), '| pares retirados', n)


if __name__ == '__main__':
    main()
