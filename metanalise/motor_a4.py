"""Motor de calculo do A4 (transporte do betao central -> obra) — fase 3 do plano da F40 (tarefa #1806).

Para cada par (fck, CO2) do painel kielima.com/metanalise (exactamente os mesmos pares que
preparar_dados.py / metanalise-export.py seleccionam: Elegivel, e4_estrato, FCK_MIN <= fck <= FCK_MAX,
co2_kg_m3 em kg CO2-eq/m3) calcula o A4 que se SOMARIA ao co2_kg_m3 numa grelha de distancias 0-300 km
x 4 modos do SIDAC (F40), com a massa volumica lida na fase 2 (F44-F46) ou a premissa F43 (2.400 kg/m3).

    A4 [kg CO2-eq/m3] = factor_SIDAC [kg CO2-eq/(t.km)] x massa_volumica [t/m3] x distancia [km]

So LE meta_analysis_base.xlsx e articles_final.xlsx (openpyxl read_only): fck, co2_kg_m3, ci e os
numeros actuais do painel nao mudam. Saidas (todas regeneraveis, versionadas em metanalise/):
  transporte_a4_motor.csv   — uma linha por par: grupo A4 (F38), tipo transportado, massa volumica e origem,
                              coeficiente kg CO2-eq/(m3.km) por modo, A4 e ci com A4 a 50/100/200/300 km no
                              modo padrao, cenario declarado (vazio: nenhum estudo imprime distancia/modo) e
                              co2_a4 publicado (para a validacao #1807).
  transporte_a4_grelha.csv  — grupo x modo x distancia: n pares, A4 medio/mediano, CO2 e ci medianos sem/com A4.
  transporte_a4_sidac.json  — factores e capacidades do SIDAC tal como registados na F40 (para o painel, #1808).

Regras aplicadas (ver metanalise/DECISOES_METANALISE.md):
  F38  o A4 so se soma aos pares com a4_somavel = sim (grupo `sim`); os pares com a4_somavel = incerto e
       fronteira A1-A3 declarada formam o grupo `provavel` (opcao a parte, ligavel no painel); `nao` = A4 ja
       no valor gravado; o resto fica `incerto` e nao recebe A4.
  F40  factores SIDAC (kg CO2-eq/t.km): betoneira 0,10; truck 3 eixos 0,07; carreta 4 eixos 0,07; carreta
       5 eixos 0,06. Grelha 0-300 km x 4 modos. O t.km do SIDAC incluir ou nao o regresso em vazio continua
       POR CONFIRMAR (ficha nao legivel por script; #1806) — o motor nao aplica factor de regresso.
  F41  tipo transportado por palavra-chave (declarado) ou pela aplicacao (provavel); a fase 2 (col 87
       a4_transporte_tipo) tem precedencia quando nao e `indeterminado`.
  F43  massa volumica: impressa > soma do traco (col 88/89, F46) > 2.400 kg/m3 premissa nossa.
  #1830 (por decidir): os `betao_fresco_betoneira` da fase 2 sao todos "so pelo enquadramento" (F44/F45) ->
       marcados `enquadramento_1830`; `nao_transportado_in_situ` recebe coeficiente 0 e fica marcado.
Uso (da raiz do repositorio):  /usr/bin/python3 metanalise/motor_a4.py
"""
import collections
import csv
import importlib.util
import json
import re
import statistics

import openpyxl

spec = importlib.util.spec_from_file_location('mexp', 'metanalise-export.py')
mexp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mexp)

SAIDA_PARES = 'metanalise/transporte_a4_motor.csv'
SAIDA_GRELHA = 'metanalise/transporte_a4_grelha.csv'
SAIDA_SIDAC = 'metanalise/transporte_a4_sidac.json'

# F40 (2026-11-02): fichas sidac.org.br/produtos/{35,32,29,31}, versao 22.04.27, "Generico", unidade t.km,
# "incluindo consumo de combustivel e emissao de CO2". Registados tal como impressos (2 casas decimais).
SIDAC = {
    'betoneira':  {'nome': 'Caminhao betoneira', 'produto': 35, 'co2_kg_tkm': 0.10, 'energia_mj_tkm': 1.48,
                   'capacidade_m3': 8.0, 'capacidade_t': 15.8},
    'truck_3e':   {'nome': 'Caminhao truck (3 eixos), basculante', 'produto': 32, 'co2_kg_tkm': 0.07,
                   'energia_mj_tkm': 1.05, 'capacidade_m3': None, 'capacidade_t': 14.0},
    'carreta_4e': {'nome': 'Carreta (4 eixos)', 'produto': 29, 'co2_kg_tkm': 0.07, 'energia_mj_tkm': 1.01,
                   'capacidade_m3': None, 'capacidade_t': 33.0},
    'carreta_5e': {'nome': 'Carreta (5 eixos)', 'produto': 31, 'co2_kg_tkm': 0.06, 'energia_mj_tkm': 0.94,
                   'capacidade_m3': None, 'capacidade_t': 41.5},
}
MODOS = list(SIDAC)
MASSA_PREMISSA = 2400.0            # F43 (Kie, 2026-11-09): premissa "nossa" quando o artigo nao da massa nem traco
DISTANCIAS = [0, 10, 25, 50, 75, 100, 150, 200, 250, 300]   # km (grelha 0-300 da F40)
DIST_PARES = [50, 100, 200, 300]   # distancias que vao como colunas no CSV por par

# Modo padrao por tipo transportado (F40 plano fase 1: betao fresco em betoneira / elemento pre-fabricado
# em plataforma / pre-mistura seca). `indeterminado` segue o betao de obra por defeito (F41), marcado.
MODO_PADRAO = {'betao_fresco_betoneira': 'betoneira', 'elemento_prefabricado': 'carreta_4e',
               'pre_mistura_seca': 'truck_3e', 'indeterminado': 'betoneira', 'nao_transportado_in_situ': None}

# F41 — mesmas expressoes de metanalise/classificar_transporte_a4.py (copiadas: aquele script corre na
# importacao e escreve o CSV da fase 1). Usadas so onde a fase 2 nao leu o par (col 87 vazia).
PREF = re.compile(r'pre-?fabric|prefabric|precast|pre-?cast|pre-?moldad|pr[eé]-?moldad|pre-?fabricad|pr[eé]-?fabricad|prestress|protendid', re.I)
SECA = re.compile(r'dry[- ]?mix|pre-?mix|premix|pr[eé]-?mistur|argamassa ensacad|bagged|ensacad', re.I)
FRESCO = re.compile(r'ready[- ]?mix|mixer truck|truck mixer|transit mixer|usinad|betoneira|central dosadora|batching plant|concrete plant|centrale de b[eé]ton|cast[- ]?in[- ]?(situ|place)|in[- ]?situ|moldad[oa] in loco', re.I)


def tipo_fase1(material, fronteira_texto, transporte_dados, fronteira_nota, aplicacao, transporte_betao_a4):
    txt = ' '.join(str(x or '') for x in (material, fronteira_texto, transporte_dados, fronteira_nota))
    for pat, c in ((PREF, 'elemento_prefabricado'), (SECA, 'pre_mistura_seca'), (FRESCO, 'betao_fresco_betoneira')):
        m = pat.search(txt)
        if m:
            return c, 'declarado_F41', f'palavra-chave "{m.group(0)}"'
    if aplicacao == 'pre_fabricado_corrente':
        return 'elemento_prefabricado', 'provavel_F41', 'aplicacao=pre_fabricado_corrente'
    if aplicacao in ('edificio', 'infraestrutura', 'pavimento', 'ponte'):
        return 'betao_fresco_betoneira', 'provavel_F41', f'aplicacao={aplicacao} (betao de obra por defeito)'
    if transporte_betao_a4 == 'incluido':
        return 'betao_fresco_betoneira', 'provavel_F41', 'A4 do betao incluido no estudo, sem outra pista'
    return 'indeterminado', 'nenhuma', ''


def grupo_a4(a4_somavel, fronteira):
    # F38: sim = soma-se; provavel = incerto com fronteira A1-A3 declarada (opcao a parte); nao = A4 ja no valor
    if a4_somavel == 'sim':
        return 'sim'
    if a4_somavel == 'nao':
        return 'nao'
    if a4_somavel == 'incerto' and fronteira == 'A1-A3':
        return 'provavel'
    return 'incerto'


def r2(x):
    return None if x is None else round(x, 2)


def main():
    status = {}
    af = openpyxl.load_workbook('articles_final.xlsx', read_only=True)['Articles']
    for i, row in enumerate(af.iter_rows(min_row=2, max_col=20, values_only=True), start=2):
        status[i] = row[19]
    ws = openpyxl.load_workbook(mexp.BASE, read_only=True)['dados_fck']
    pares = []
    for r, row in enumerate(ws.iter_rows(min_row=2, values_only=True), start=2):
        g = lambda c: row[c - 1] if c - 1 < len(row) else None
        row_id, fck, co2 = g(1), mexp.tofloat(g(8)), mexp.tofloat(g(14))
        co2m3, estrato = mexp.tofloat(g(37)), g(22)
        # selecao identica a preparar_dados.py (mesmos pares do painel e do modelo)
        if fck in (None, 0) or co2 is None or status.get(row_id) != 'Elegível':
            continue
        if estrato not in mexp.TIERCODE or co2m3 is None:
            continue
        if not (mexp.FCK_MIN <= fck <= mexp.FCK_MAX and mexp.CO2_MIN <= co2m3 <= mexp.CO2_MAX):
            continue
        a4_somavel, fronteira = g(75), g(60)
        tipo_f2 = g(87)
        if tipo_f2 and tipo_f2 != 'indeterminado':
            tipo = tipo_f2
            if tipo == 'betao_fresco_betoneira':
                conf, regra = 'enquadramento_1830', 'fase 2: so pelo enquadramento ready-mix/central (F44/F45; por decidir em #1830)'
            elif tipo == 'nao_transportado_in_situ':
                conf, regra = 'enquadramento_1830', 'fase 2: in situ so pelo enquadramento (F44; por decidir em #1830)'
            else:
                conf, regra = 'declarado_F42', 'fase 2 (leitura integral, prompt F42)'
        else:
            tipo, conf, regra = tipo_fase1(g(7), g(61), g(64), g(67), g(56), g(63))
            if tipo_f2 == 'indeterminado' and tipo == 'indeterminado':
                regra = 'fase 2: indeterminado (laboratorio/modelacao, nada transportado declarado)'
        massa, origem = mexp.tofloat(g(88)), g(89)
        if massa is None:
            massa = MASSA_PREMISSA
            if origem == 'nao_disponivel':
                origem = 'premissa_F43 (nao_disponivel na fase 2)'
            elif tipo_f2 is None:
                origem = 'premissa_F43 (par fora das 14 listas da fase 2: massa nao lida)'
            else:
                origem = 'premissa_F43 (massa retida: #1831/#1832/RONNING)'
        t_m3 = massa / 1000.0
        coef = {m: SIDAC[m]['co2_kg_tkm'] * t_m3 for m in MODOS}          # kg CO2-eq/(m3.km)
        modo_padrao = MODO_PADRAO.get(tipo, 'betoneira')
        in_situ = tipo == 'nao_transportado_in_situ'
        if in_situ:
            coef = {m: 0.0 for m in MODOS}
        grupo = grupo_a4(a4_somavel, fronteira)
        # cenario declarado: distancia central->obra e modo impressos no artigo (F44-F46: nenhum estudo)
        dist_decl = mexp.tofloat(g(91))
        modo_decl = str(g(92) or '')
        a4_decl = None
        if dist_decl is not None and not in_situ:
            modo_decl_cod = next((m for m in MODOS if m.split('_')[0] in modo_decl.lower()), modo_padrao)
            a4_decl = coef[modo_decl_cod] * dist_decl
        p = {
            'obs_id': r, 'estudo': row_id, 'rotulo': mexp.short_label(g(4), g(5)), 'estrato': estrato,
            'familia': mexp.classify(row_id, g(7), g(3)), 'fck': fck, 'co2_kg_m3': co2m3, 'ci': r2(co2m3 / fck),
            'a4_somavel': a4_somavel or '', 'fronteira': fronteira or '', 'transporte_betao_a4': g(63) or '',
            'a4_grupo': grupo, 'a4_tipo_transportado': tipo, 'a4_tipo_confianca': conf, 'a4_tipo_regra': regra,
            'massa_volumica_kg_m3': r2(massa), 'massa_volumica_origem': origem or '',
            'modo_padrao': modo_padrao or '', 'a4_declarado_kg_m3': r2(a4_decl),
            'a4_distancia_declarada_km': dist_decl, 'co2_a4_publicado': mexp.tofloat(g(80)),
        }
        for m in MODOS:
            p[f'coef_{m}_kg_m3_km'] = round(coef[m], 4)
        for d in DIST_PARES:
            a4 = coef[modo_padrao] * d if modo_padrao else 0.0
            p[f'a4_{d}km'] = r2(a4)
            p[f'ci_com_a4_{d}km'] = r2((co2m3 + a4) / fck) if grupo in ('sim', 'provavel') else None
        p['_coef'] = coef
        pares.append(p)

    # --- saida por par
    cols = [k for k in pares[0] if not k.startswith('_')]
    with open(SAIDA_PARES, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction='ignore')
        w.writeheader()
        w.writerows(pares)

    # --- grelha grupo x modo x distancia (so grupos que recebem A4: sim, provavel; e `todos_somaveis` = sim+provavel)
    def resumo(sel, modo, d):
        a4s = [p['_coef'][modo] * d for p in sel]
        co2s = [p['co2_kg_m3'] for p in sel]
        cis = [p['co2_kg_m3'] / p['fck'] for p in sel]
        cis_com = [(p['co2_kg_m3'] + a) / p['fck'] for p, a in zip(sel, a4s)]
        return {'n_pares': len(sel), 'n_estudos': len({p['estudo'] for p in sel}),
                'a4_medio': r2(statistics.fmean(a4s)), 'a4_mediano': r2(statistics.median(a4s)),
                'co2_mediano_sem_a4': r2(statistics.median(co2s)),
                'co2_mediano_com_a4': r2(statistics.median([c + a for c, a in zip(co2s, a4s)])),
                'ci_mediano_sem_a4': r2(statistics.median(cis)), 'ci_mediano_com_a4': r2(statistics.median(cis_com)),
                'acrescimo_relativo_mediano_pct': r2(100 * statistics.median([a / c for a, c in zip(a4s, co2s) if c > 0]))}
    grelha = []
    for grupo, sel in (('sim', [p for p in pares if p['a4_grupo'] == 'sim']),
                       ('provavel', [p for p in pares if p['a4_grupo'] == 'provavel']),
                       ('sim+provavel', [p for p in pares if p['a4_grupo'] in ('sim', 'provavel')])):
        for modo in MODOS:
            for d in DISTANCIAS:
                grelha.append({'a4_grupo': grupo, 'modo': modo, 'distancia_km': d, **resumo(sel, modo, d)})
    with open(SAIDA_GRELHA, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(grelha[0]))
        w.writeheader()
        w.writerows(grelha)

    with open(SAIDA_SIDAC, 'w', encoding='utf-8') as f:
        json.dump({'fonte': 'SIDAC, fichas sidac.org.br/produtos/{35,32,29,31}, versao 22.04.27, unidade t.km (F40, 2026-11-02)',
                   'regresso_em_vazio': 'por confirmar (ficha nao legivel por script) — o motor nao aplica factor de regresso',
                   'massa_premissa_kg_m3': MASSA_PREMISSA, 'distancias_km': DISTANCIAS, 'modos': SIDAC,
                   'modo_padrao_por_tipo': MODO_PADRAO}, f, ensure_ascii=False, indent=1)

    # --- relatorio
    C = collections.Counter
    print(f'{len(pares)} pares de {len({p["estudo"] for p in pares})} estudos -> {SAIDA_PARES}, {SAIDA_GRELHA}, {SAIDA_SIDAC}')
    print('grupo A4 (F38):', dict(C(p['a4_grupo'] for p in pares)))
    print('tipo transportado:', dict(C((p['a4_tipo_transportado'], p['a4_tipo_confianca']) for p in pares)))
    print('massa volumica (origem):', dict(C(p['massa_volumica_origem'] for p in pares)))
    som = [p for p in pares if p['a4_grupo'] in ('sim', 'provavel')]
    print('somaveis (sim+provavel) com massa premissa F43:',
          sum(1 for p in som if p['massa_volumica_origem'].startswith('premissa')), 'de', len(som))
    print('pares com co2_a4 publicado (para #1807):', sum(1 for p in pares if p['co2_a4_publicado'] is not None))
    print('cenario declarado (distancia impressa):', sum(1 for p in pares if p['a4_declarado_kg_m3'] is not None))
    for g in ('sim', 'sim+provavel'):
        for d in (50, 100, 300):
            row = next(x for x in grelha if x['a4_grupo'] == g and x['modo'] == 'betoneira' and x['distancia_km'] == d)
            print(f"  {g:13s} betoneira {d:3d} km: n={row['n_pares']} A4 medio {row['a4_medio']} kg/m3, "
                  f"ci mediano {row['ci_mediano_sem_a4']} -> {row['ci_mediano_com_a4']} (+{row['acrescimo_relativo_mediano_pct']}% CO2)")


if __name__ == '__main__':
    main()
