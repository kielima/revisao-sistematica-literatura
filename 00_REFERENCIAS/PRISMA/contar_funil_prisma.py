#!/usr/bin/env python3
"""Fluxograma PRISMA 2020 do desenho de 4 etapas -- contagem por filtro explicito.

Le `articles_final.xlsx` (aba Articles) e imprime cada caixa do fluxograma
com a DEFINICAO do filtro ao lado do numero (tarefa #1336: "definir cada
numero com um filtro explicito e verificavel, e guardar a definicao ao lado
do numero"). Cada registo e contado no PRIMEIRO criterio que o exclui.

Saidas (na mesma pasta deste script):
  FUNIL_PRISMA.csv            caixa, n, filtro (para o fluxograma e para a dissertacao)
  EXCLUSOES_POR_CRITERIO.svg  barras dos excluidos por criterio de saida (tarefa #0594)
  (stdout)                    a tabela e a lista de registos a regularizar

As definicoes sao as mesmas da pagina kielima.com/metanalise/prisma
(kielima-site, public/assets/metanalise-prisma.js) e do painel /metanalise.
Uso: python3 00_REFERENCIAS/PRISMA/contar_funil_prisma.py  (a partir da raiz do repo)
"""
import csv
import os
import sys
from collections import Counter

import openpyxl

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BANCO = os.path.join(RAIZ, 'articles_final.xlsx')
AQUI = os.path.dirname(os.path.abspath(__file__))

# Colunas de articles_final.xlsx (1-based, conferidas pelo cabecalho em 2026-11-22)
COL = dict(author=2, year=4, source=5, document_type=9, pdf=11, status=20, C6=27,
           E1_ano=34, E1_tipo_doc=35, E1_moldavel=36, E1_construcao=37, E1_acesso=38,
           E2_resistencia=39, E2_co2=40, E3_regional=41, etapa_saida=43,
           criterio_saida=44, E4_total=53, E4_estrato=54)
ACEITO = 'Aceito'
E1 = [('E1_ano', 'ano >= 2006 (ISO 14040/44)'),
      ('E1_tipo_doc', 'tipo de documento'),
      ('E1_moldavel', 'material moldavel'),
      ('E1_construcao', 'aplicacao em construcao')]


def v(r, nome):
    return r[COL[nome] - 1]


def primeiro_criterio_e1(r):
    """Nome do primeiro criterio E1 que NAO e Aceito, ou None se passa os quatro."""
    for nome, _ in E1:
        if v(r, nome) != ACEITO:
            return nome
    return None


def main():
    ws = openpyxl.load_workbook(BANCO, read_only=True)['Articles']
    linhas = list(ws.iter_rows(min_row=2, values_only=True))
    idx = {id(r): i for i, r in enumerate(linhas, start=2)}  # numero da linha no xlsx

    caixas = []  # (id, fase, tipo, n, titulo, filtro)

    def caixa(cid, fase, tipo, n, titulo, filtro):
        caixas.append((cid, fase, tipo, n, titulo, filtro))

    # ---- Identificacao -------------------------------------------------------
    fontes = Counter(v(r, 'source') for r in linhas)
    caixa('ident', 'Identificacao', 'fluxo', len(linhas), 'Registos identificados nas bases',
          'todas as linhas de articles_final.xlsx; por base: '
          + ' | '.join(f'{k} {n}' for k, n in fontes.most_common()))
    dup = [r for r in linhas if v(r, 'status') == 'Duplicado']
    caixa('dup', 'Identificacao', 'saida', len(dup), 'Duplicados removidos antes da triagem',
          "status_triagem = 'Duplicado' (remocao pre-triagem, nao e criterio de exclusao)")

    # ---- Triagem — Etapa 1 (metadados) ----------------------------------------
    nao_dup = [r for r in linhas if v(r, 'status') != 'Duplicado']
    caixa('e1', 'Triagem - Etapa 1', 'fluxo', len(nao_dup), 'Registos triados por metadados',
          "status_triagem <> 'Duplicado'")
    e1x = Counter()
    sem_decisao_e1 = []
    ret = []
    for r in nao_dup:
        c = primeiro_criterio_e1(r)
        if c is None:
            ret.append(r)
        else:
            e1x[c] += 1
            if v(r, c) is None:
                sem_decisao_e1.append((idx[id(r)], c, v(r, 'status')))
    detalhe_e1 = ' | '.join(f'{c} {e1x[c]}' for c, _ in E1 if e1x[c])
    caixa('e1x', 'Triagem - Etapa 1', 'saida', sum(e1x.values()), 'Excluidos na Etapa 1',
          "primeiro criterio E1 (ano, tipo_doc, moldavel, construcao) <> 'Aceito'; " + detalhe_e1
          + (f"; inclui {len(sem_decisao_e1)} registo(s) SEM decisao (celula vazia), ver regularizacoes"
             if sem_decisao_e1 else ''))

    # ---- Elegibilidade — Etapa 2 (texto completo) ----------------------------
    caixa('ret', 'Elegibilidade - Etapa 2', 'fluxo', len(ret), 'Textos completos procurados',
          "os quatro criterios E1 = 'Aceito'")
    retx = [r for r in ret if v(r, 'E2_resistencia') is None]
    caixa('retx', 'Elegibilidade - Etapa 2', 'saida', len(retx), 'Texto completo nao obtido',
          "E1 completo e E2_resistencia vazia (sem PDF): status_triagem = "
          + ', '.join(f"'{k}' {n}" for k, n in Counter(v(r, 'status') for r in retx).items()))
    e2 = [r for r in ret if v(r, 'E2_resistencia') is not None]
    caixa('e2', 'Elegibilidade - Etapa 2', 'fluxo', len(e2), 'Textos completos avaliados',
          "E1 completo e E2_resistencia preenchida (leitura integral do PDF)")
    e2x_res = [r for r in e2 if v(r, 'E2_resistencia') != ACEITO]
    e2_res_ok = [r for r in e2 if v(r, 'E2_resistencia') == ACEITO]
    e2x_co2 = [r for r in e2_res_ok if v(r, 'E2_co2') != ACEITO]
    caixa('e2x', 'Elegibilidade - Etapa 2', 'saida', len(e2x_res) + len(e2x_co2),
          'Excluidos na Etapa 2 - falta de dado extraivel',
          f"E2_resistencia <> 'Aceito' ({len(e2x_res)}: sem fck proprio pareavel a um CO2 proprio, "
          f"ou fck < 20 MPa) ou, com fck, E2_co2 <> 'Aceito' ({len(e2x_co2)}: sem CO2 absoluto)")
    e3 = [r for r in e2_res_ok if v(r, 'E2_co2') == ACEITO]
    caixa('e3', 'Elegibilidade - Etapa 3', 'fluxo', len(e3), 'Artigos aceites na Etapa 2',
          "E2_resistencia = 'Aceito' e E2_co2 = 'Aceito'")

    # ---- Elegibilidade — Etapa 3 (restricao geografica do material) ----------
    e3x = [r for r in e3 if v(r, 'E3_regional') != ACEITO]
    e3x_vazio = [idx[id(r)] for r in e3x if v(r, 'E3_regional') is None]
    caixa('e3x', 'Elegibilidade - Etapa 3', 'saida', len(e3x),
          'Excluidos na Etapa 3 - material geograficamente restrito',
          f"E3_regional <> 'Aceito': {len(e3x) - len(e3x_vazio)} com E3_regional = 'Rejeitado'"
          + (f" + {len(e3x_vazio)} com E3_regional vazio e status 'Rejeitado' (rejeitados por "
             f"restricao geografica na triagem antiga C6, linhas {e3x_vazio}; a regularizar)"
             if e3x_vazio else ''))
    e4 = [r for r in e3 if v(r, 'E3_regional') == ACEITO]
    caixa('e4', 'Inclusao - Etapa 4', 'fluxo', len(e4), 'Artigos que passam a Etapa 3',
          "E3_regional = 'Aceito' (" + ' + '.join(
              f"{n} {k}" for k, n in Counter(v(r, 'status') for r in e4).most_common()) + ')')

    # ---- Inclusao — Etapa 4 (qualidade) ---------------------------------------
    rev = [r for r in e4 if v(r, 'status') == 'Revisao']
    caixa('rev', 'Inclusao - Etapa 4', 'saida', len(rev), 'Revisoes sem ACV propria - ramo de citacao',
          "status_triagem = 'Revisao' (nao pontuam; as fontes primarias que citam entram pelo "
          "ramo 'outros metodos', aba estudos_secundarios)")
    fin = [r for r in e4 if v(r, 'status') == 'Elegível']
    estratos = Counter(v(r, 'E4_estrato') for r in fin)
    caixa('fin', 'Inclusao - Etapa 4', 'fluxo', len(fin), 'Artigos incluidos na revisao (corpus)',
          f"status_triagem = 'Elegível'; E4_estrato: principal {estratos.get('principal', 0)}, "
          f"sensibilidade {estratos.get('sensibilidade', 0)}")
    tier = [r for r in fin if v(r, 'E4_estrato') == 'sensibilidade']
    notas = sorted(Counter(v(r, 'E4_total') for r in tier).items(), key=lambda kv: float(kv[0] or 0))
    caixa('tier', 'Inclusao - Etapa 4', 'saida', len(tier),
          'Estrato de sensibilidade - fora do RESULTADO PRINCIPAL, dentro do corpus',
          "E4_estrato = 'sensibilidade' (E4_qualidade_total < 4,0 de 7; notas: "
          + ', '.join(f'{k} ({n})' for k, n in notas)
          + "). Exclusao do resultado principal, nao do corpus: entra na analise de sensibilidade")
    principal = [r for r in fin if v(r, 'E4_estrato') == 'principal']
    caixa('main', 'Inclusao - Etapa 4', 'fluxo', len(principal), 'Estudos no resultado principal',
          "E4_estrato = 'principal' (E4_qualidade_total >= 4,0 de 7)")

    # ---- Ramo "outros metodos": estudos secundarios das revisoes --------------
    try:
        ws2 = openpyxl.load_workbook(BANCO, read_only=True)['estudos_secundarios']
        sec = list(ws2.iter_rows(values_only=True))
        h = {k: i for i, k in enumerate(sec[0])}
        sec = sec[1:]
        por_rev = Counter(x[h['revisao']] for x in sec)
        estado = Counter(x[h['estado_extracao']] for x in sec)
        caixa('sec', 'Outros metodos', 'fluxo', len(sec),
              'Registos identificados por busca de citacoes nas revisoes catalogadas',
              'aba estudos_secundarios (F36): ' + ' | '.join(f'{k} {n}' for k, n in por_rev.most_common()))
        caixa('sec_banco', 'Outros metodos', 'saida', estado.get('ja_no_banco', 0),
              'Ja estavam no banco (contados no fluxo principal)', "estado_extracao = 'ja_no_banco'")
        caixa('sec_pend', 'Outros metodos', 'fluxo',
              estado.get('pendente', 0) + estado.get('sem_doi', 0),
              'Relatorios a procurar/avaliar (pendentes, tarefa #1811)',
              f"estado_extracao = 'pendente' ({estado.get('pendente', 0)}) ou 'sem_doi' ({estado.get('sem_doi', 0)})")
    except KeyError:
        print('AVISO: aba estudos_secundarios nao encontrada', file=sys.stderr)

    # ---- Impressao -------------------------------------------------------------
    print(f'{"id":10} {"n":>6}  caixa  --  filtro')
    for cid, fase, tipo, n, titulo, filtro in caixas:
        print(f'{cid:10} {n:>6}  [{fase} | {tipo}] {titulo}')
        print(f'{"":17}  filtro: {filtro}')
    print('\nAritmetica:')
    n = {c[0]: c[3] for c in caixas}
    checks = [('ident - dup = e1', n['ident'] - n['dup'], n['e1']),
              ('e1 - e1x = ret', n['e1'] - n['e1x'], n['ret']),
              ('ret - retx = e2', n['ret'] - n['retx'], n['e2']),
              ('e2 - e2x = e3', n['e2'] - n['e2x'], n['e3']),
              ('e3 - e3x = e4', n['e3'] - n['e3x'], n['e4']),
              ('e4 - rev = fin', n['e4'] - n['rev'], n['fin']),
              ('fin - tier = main', n['fin'] - n['tier'], n['main'])]
    for nome, a, b in checks:
        print(f'  {nome:20} {a} = {b}  {"OK" if a == b else "ERRO"}')

    # ---- Regularizacoes pendentes (nao mudam o funil; afectam etapa/criterio_saida)
    print('\nRegistos a regularizar (nao alteram as contagens acima):')
    if sem_decisao_e1:
        print(f'  E1 sem decisao, contados como excluidos em E1: {sem_decisao_e1}')
    semetapa_rej = [idx[id(r)] for r in linhas if v(r, 'status') == 'Rejeitado' and v(r, 'etapa_saida') is None]
    print(f'  Rejeitado sem etapa_saida/criterio_saida: {semetapa_rej}')
    semetapa_dup = [idx[id(r)] for r in linhas if v(r, 'status') == 'Duplicado' and v(r, 'etapa_saida') is None]
    print(f"  Duplicado sem etapa_saida = 'duplicado': {semetapa_dup}")
    fmt = Counter((type(v(r, 'etapa_saida')).__name__, v(r, 'etapa_saida')) for r in linhas)
    print(f'  Formatos de etapa_saida: {dict(fmt)}')
    crit = Counter(v(r, 'criterio_saida') for r in linhas)
    print(f'  Valores de criterio_saida: {dict(crit)}')
    # criterio_saida que nao bate com os campos E1-E3
    desacordo = []
    for r in linhas:
        cs = v(r, 'criterio_saida')
        if cs in ('E2_co2', 'E3_regional'):
            if v(r, 'E2_resistencia') != ACEITO:
                desacordo.append((idx[id(r)], cs, 'E2_resistencia=' + str(v(r, 'E2_resistencia'))))
            elif cs == 'E3_regional' and v(r, 'E2_co2') != ACEITO:
                desacordo.append((idx[id(r)], cs, 'E2_co2=' + str(v(r, 'E2_co2'))))
    print(f'  criterio_saida em desacordo com o primeiro campo que rejeita: {desacordo}')
    orf = Counter((v(r, 'E4_estrato'), v(r, 'status')) for r in linhas
                  if v(r, 'E4_estrato') and v(r, 'status') != 'Elegível')
    print(f'  E4_estrato orfao (linha fora do corpus): {dict(orf)}')

    # ---- CSV ---------------------------------------------------------------------
    with open(os.path.join(AQUI, 'FUNIL_PRISMA.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['id', 'fase', 'tipo', 'n', 'caixa', 'filtro'])
        for c in caixas:
            w.writerow(c)

    # ---- SVG: excluidos por criterio de saida (tarefa #0594) --------------------
    barras = [(f'E1 {c.split("_", 1)[1]}', e1x[c], '#8a9a5b') for c, _ in E1 if e1x[c]]
    barras += [('E2 resistencia', len(e2x_res), '#c4714f'), ('E2 CO2', len(e2x_co2), '#c4714f'),
               ('E3 regional', len(e3x), '#5b7f8a'),
               ('E4 sensibilidade*', len(tier), '#9a8a5b')]
    barras.sort(key=lambda b: -b[1])
    escrever_svg(os.path.join(AQUI, 'EXCLUSOES_POR_CRITERIO.svg'), barras,
                 f'Registos excluidos por criterio de saida (n = {n["e1x"] + n["e2x"] + n["e3x"]})',
                 f'* sai do resultado principal, nao do corpus (analise de sensibilidade). '
                 f'Duplicados ({n["dup"]}) e textos nao obtidos ({n["retx"]}) nao sao criterios e ficam fora.')
    print(f'\nEscrito: FUNIL_PRISMA.csv, EXCLUSOES_POR_CRITERIO.svg em {AQUI}')


def escrever_svg(caminho, barras, titulo, nota):
    """Grafico de barras horizontais em SVG puro (sem dependencias)."""
    W, mx, my = 860, 230, 64
    alt, gap = 30, 12
    H = my + len(barras) * (alt + gap) + 70
    vmax = max(b[1] for b in barras) or 1
    larg = W - mx - 90
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
           f'font-family="Geist, Helvetica, Arial, sans-serif" font-size="14">',
           f'<rect width="{W}" height="{H}" fill="#fbfaf7"/>',
           f'<text x="{mx}" y="30" font-size="17" font-weight="600" fill="#1f1f1f">{titulo}</text>']
    for i, (rot, val, cor) in enumerate(barras):
        y = my + i * (alt + gap)
        w = larg * val / vmax
        out.append(f'<text x="{mx - 12}" y="{y + alt / 2 + 5}" text-anchor="end" fill="#333">{rot}</text>')
        out.append(f'<rect x="{mx}" y="{y}" width="{w:.1f}" height="{alt}" rx="3" fill="{cor}"/>')
        out.append(f'<text x="{mx + w + 8:.1f}" y="{y + alt / 2 + 5}" fill="#1f1f1f" font-weight="500">'
                   f'{val:,}</text>'.replace(',', '.'))
    out.append(f'<text x="{mx}" y="{H - 28}" font-size="12" fill="#666">{nota}</text>')
    out.append(f'<text x="{mx}" y="{H - 10}" font-size="12" fill="#666">Fonte: articles_final.xlsx, '
               f'campos E1-E4 (contagem no primeiro criterio que exclui) - contar_funil_prisma.py</text>')
    out.append('</svg>')
    with open(caminho, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out))


if __name__ == '__main__':
    main()
