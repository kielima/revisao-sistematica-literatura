"""Aplica os lotes do volume do provete pela norma citada (2026-10-04).

Regra da Kie (2026-10-04): assumir o provete-padrao da norma citada SO quando a norma
define um unico provete, ou quando a relacao e directa sem suposicoes; normas que
admitem mais de um provete -> volume em branco, com justificacao.

  - dimensoes declaradas pelo artigo -> volume dessas dimensoes (vol_fonte medido_ensaio)
  - notacao de classe EN 206 / EN 1992 / EHE-08 / fib MC2010 / BS 8500 (Cxx/yy, HA-xx, RCxx/yy):
      valor de cilindro -> cilindro 150x300; valor de cubo -> cubo 150
  - GB 50010 / GB/T 50081 (fcu,k) e IS 456 (grau M) -> cubo 150
  - ASTM C109 -> cubo 50 mm; EN 196-1 e EN 998-2 (via EN 1015-11) -> prisma 40x40x160
  - restantes (ASTM C39/C31, ACI 318, NBR, AS 1012/1379, KS, JIS, IS 516, EN 12390-3 sem
    tamanho, normas de dosagem, sem norma) -> em branco
So preenche linhas sem vol numerico. Escreve norma_ensaio (col 43) sempre que houver norma.
Correr da raiz do repo e depois recalcular_ci.py.
"""
import glob
import json
import math
import re

import openpyxl

BASE = 'meta_analysis_base.xlsx'
COL_VOL, COL_VFONTE, COL_VCIT, COL_NORMA, COL_TIPO, COL_OBS = 23, 24, 25, 43, 11, 13
CIL150 = round(math.pi * 0.075 ** 2 * 0.3, 7)
CIL100 = round(math.pi * 0.05 ** 2 * 0.2, 7)
CUBO150, CUBO100, CUBO50 = 0.003375, 0.001, 0.000125
PRISMA40 = 0.04 * 0.04 * 0.16

NOTACAO = re.compile(r'EN 206|EN ?1992|EHE|fib|MC ?2010|BS 8500|notac', re.I)
GB_IS = re.compile(r'GB ?50010|GB/T ?50081|IS ?456', re.I)

# sheet_row -> (vol | None, fonte, citacao)  decisoes pessoais / da Kie
OVERRIDE = {}
for r in (250, 251, 252):  # 3003 ZHANG: o proprio artigo chama "C28/35" ao C35 -> numero de cubo EN 206
    OVERRIDE[r] = (CUBO150, 'padrao_norma', 'BS EN 206-1: o artigo chama "C28/35" a classe C35, logo o numero e de cubo; cubo 150 mm de definicao da classe')
OVERRIDE[235] = (CUBO150, 'medido_ensaio', 'Tabela 4: forca de rotura / tensao = ~22.500 mm2 nas 12 leituras -> cubo de 150 mm (relacao directa, EN 12390-3)')
OVERRIDE[911] = (CIL100, 'medido_ensaio', 'o modelo do artigo normaliza todos os fc para cilindro equivalente 100x200 mm (cilindro de conversao, nao provete ensaiado)')
for r in (1036, 1037, 1038, 2099, 2100):  # 3519 NGUYEN: prisma moldado 150x40x15 (compressao nas metades)
    OVERRIDE[r] = (0.15 * 0.04 * 0.015, 'medido_ensaio', 'prisma moldado 150x40x15 mm declarado; compressao nas metades (area carregada 20x20 mm2)')
for r in (950, 951):
    OVERRIDE[r] = (None, None, 'fck gravado e o valor assumido/medio (30/45), nao o fck da classe C25/30 / C35/45; volume em branco')

TIPO_LIMPAR = {571: 'comparador SCUHPC de 140 MPa citado de Deeb & Karihaloo [93]; o cubo de 40 mm (ASTM C349) so vale para as misturas do proprio artigo',
               }
FCK_CORRIGIR = {  # 3568 BERNDT, Tabela 3 p.611 (leitura pessoal)
    1047: (38.6, '32 50BFS', 37.9),
    1049: (45.4, '35 50BFS', 44.9),
}


def clean(s):
    return re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', str(s))


def vol_dimensoes(txt, provete):
    nums = [float(x.replace(',', '.')) for x in re.findall(r'\d+(?:[.,]\d+)?', txt or '')]
    if not nums:
        return None
    if provete == 'cubo' and len(nums) >= 1:
        return round((nums[0] / 1000) ** 3, 7)
    if provete == 'cilindro' and len(nums) >= 2:
        return round(math.pi * (nums[0] / 2000) ** 2 * nums[1] / 1000, 7)
    if provete == 'prisma' and len(nums) >= 3:
        return round(nums[0] * nums[1] * nums[2] / 1e9, 9)
    return None


def decidir(p):
    tipo, norma, valor_de = p.get('tipo'), p.get('norma') or '', p.get('valor_de')
    provete = p.get('provete')
    if tipo == 'dimensoes':
        v = vol_dimensoes(p.get('dimensoes_declaradas'), provete)
        return (v, 'medido_ensaio', f'dimensoes declaradas: {p.get("dimensoes_declaradas")}') if v else (None, None, 'dimensoes declaradas mas nao convertiveis automaticamente')
    if tipo == 'norma_classe' and NOTACAO.search(norma):
        if valor_de == 'cilindro':
            return CIL150, 'padrao_norma', f'{norma}: fck de cilindro da classe -> cilindro 150x300 de definicao'
        if valor_de == 'cubo':
            return CUBO150, 'padrao_norma', f'{norma}: valor de cubo da classe -> cubo 150 de definicao'
    if GB_IS.search(norma):
        return CUBO150, 'padrao_norma', f'{norma}: classe definida em cubo de 150 mm'
    if re.search(r'C ?109', norma):
        return CUBO50, 'padrao_norma', f'{norma}: cubo de 50 mm (unico provete da norma)'
    if re.search(r'EN ?196-1|EN ?998-2', norma):
        return PRISMA40, 'padrao_norma', f'{norma}: prisma 40x40x160 mm (unico provete da norma de ensaio)'
    if norma:
        return None, None, f'norma citada ({norma}) admite mais de um provete ou nao define o provete do valor; volume em branco (regra da Kie 2026-10-04)'
    return None, None, 'sem norma nem dimensoes no artigo; volume em branco'


def main():
    res = {}
    for f in sorted(glob.glob('lotes_volnorma/resultado_lote*.json')):
        for a in json.load(open(f, encoding='utf-8')):
            for p in a['pares']:
                res[int(p['sheet_row'])] = (str(a['row_id']), p)
    wb = openpyxl.load_workbook(BASE)
    ws = wb['dados_fck']
    n_vol = n_branco = n_norma = 0
    for r, (rid, p) in sorted(res.items()):
        assert str(ws.cell(r, 1).value) == rid, (r, rid)
        if isinstance(ws.cell(r, COL_VOL).value, (int, float)):
            continue
        if p.get('norma'):
            ws.cell(r, COL_NORMA).value = clean(p['norma'])[:200]
            n_norma += 1
        v, fonte, cit = OVERRIDE.get(r) or decidir(p)
        if v:
            ws.cell(r, COL_VOL).value = v
            ws.cell(r, COL_VFONTE).value = fonte
            ws.cell(r, COL_VCIT).value = clean(f'[2026-10-04] {cit}; {p.get("citacao") or ""}')[:500]
            n_vol += 1
        else:
            ws.cell(r, COL_VFONTE).value = 'indisponivel'
            ws.cell(r, COL_VCIT).value = clean(f'[VOLUME EM BRANCO 2026-10-04] {cit}')[:500]
            n_branco += 1
    for r, motivo in TIPO_LIMPAR.items():
        ws.cell(r, COL_TIPO).value = None
        ws.cell(r, COL_OBS).value = clean(f'{ws.cell(r, COL_OBS).value or ""} [tipo_corpo_prova limpo 2026-10-04: {motivo}]').strip()
    for r, (novo, mix, velho) in FCK_CORRIGIR.items():
        assert str(ws.cell(r, 1).value) == '3568' and ws.cell(r, 8).value == velho
        ws.cell(r, 8).value = novo
        ws.cell(r, COL_OBS).value = clean(f'{ws.cell(r, COL_OBS).value or ""} [fck corrigido 2026-10-04, leitura pessoal da Tabela 3 p.611: mix "{mix}" = {novo} MPa; o {velho} gravado era da coluna vizinha]').strip()
    wb.save(BASE)
    print(f'volume gravado {n_vol} | em branco {n_branco} | norma registada {n_norma} | total {len(res)}')


if __name__ == '__main__':
    main()
