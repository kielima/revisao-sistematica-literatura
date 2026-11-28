"""Rodada final (#1976): confere que modelo, painel, A4 e PRISMA contam os mesmos pares e estudos.

Escreve metanalise/resultados/CONFERENCIA_RODADA.md e sai com código 1 se alguma verificação falhar.
Uso: python3 metanalise/conferir_rodada.py [../kielima-site/public/assets/metanalise.js]
(sem o caminho do site, as verificações do painel ficam de fora).
"""
import csv, json, re, sys, datetime

R = 'metanalise/resultados/'
linhas, falhas = [], []


def ok(nome, cond, detalhe):
    linhas.append('| %s | %s | %s |' % ('✅' if cond else '❌', nome, detalhe))
    if not cond:
        falhas.append(nome)


def ler(p):
    return list(csv.DictReader(open(p, encoding='utf-8')))


dados = ler('metanalise/dados_metanalise.csv')
n_pares = len(dados)
estudos = {d['estudo'] for d in dados}
princ = [d for d in dados if d['estrato'] == 'principal' and d['sem_bruto'] in ('0', '0.0', 'FALSE', 'False')]

# 1. mesmos pares em todas as saídas por par
for nome, p in [('motor do A4', 'metanalise/transporte_a4_motor.csv'), ('A2 por par', R + 'a2_por_par.csv'),
                ('corpo de prova por par', R + 'corpo_prova_por_par.csv')]:
    n = len(ler(p))
    ok('pares: dados_metanalise = %s' % nome, n == n_pares, '%d vs %d' % (n_pares, n))
motor = ler('metanalise/transporte_a4_motor.csv')
ordem = all(abs(float(a['fck']) - float(b['fck'])) < 1e-6 and abs(float(a['co2_kg_m3']) - float(b['co2_kg_m3'])) < 1e-6
            for a, b in zip(dados, motor))
ok('pares: mesma ordem e valores (dados_metanalise × motor A4)', ordem, 'fck e CO₂ par a par')

# 2. resultado principal igual em todos os ficheiros
res = ler(R + 'resumo_modelos.csv')[0]
k0, e0, mu0 = int(res['k']), int(res['estudos']), float(res['mu'])
ok('principal: k e estudos dos dados = modelo', (len(princ), len({d['estudo'] for d in princ})) == (k0, e0),
   'dados %d / %d; modelo %d / %d' % (len(princ), len({d['estudo'] for d in princ}), k0, e0))
for f in ['sensibilidade_a2', 'sensibilidade_corpo_prova', 'sensibilidade_a4', 'sensibilidade_secundarios']:
    r = ler(R + f + '.csv')[0]
    ok('principal: modelo = %s (referência)' % f,
       int(r['k']) == k0 and int(r['estudos']) == e0 and abs(float(r['mu']) - mu0) < 1e-4,
       'k %s, estudos %s, μ %.4f' % (r['k'], r['estudos'], float(r['mu'])))
forest = json.load(open(R + 'forest_site.json', encoding='utf-8'))
c = forest['cenarios']['p|todos|sem|ci']
ok('principal: modelo = forest do painel', c['k'] == k0 and c['estudos'] == e0 and abs(c['global']['mu'] - mu0) < 1e-3,
   'k %d, estudos %d, μ %.4f' % (c['k'], c['estudos'], c['global']['mu']))
a4 = json.load(open(R + 'a4_site.json', encoding='utf-8'))
ok('principal: modelo = superfície do A4', a4['k'] == k0 and a4['estudos'] == e0 and abs(a4['referencia'][0] - mu0) < 1e-3,
   'k %d, estudos %d, μ %.3f' % (a4['k'], a4['estudos'], a4['referencia'][0]))
ok('forest: todos os pares do painel', forest['cenarios']['ps|todos|sem|ci']['k'] + 0 <= n_pares, 'k p+s sem desconto %d ≤ %d pares'
   % (forest['cenarios']['ps|todos|sem|ci']['k'], n_pares))

# 3. PRISMA
fun = {r['id']: int(r['n']) for r in ler('00_REFERENCIAS/PRISMA/FUNIL_PRISMA.csv')}
ok('PRISMA: corpus = principal + sensibilidade', fun['fin'] == fun['main'] + fun['tier'],
   '%d = %d + %d' % (fun['fin'], fun['main'], fun['tier']))
ok('PRISMA: estudos com par ≤ corpus', len(estudos) <= fun['fin'], '%d ≤ %d' % (len(estudos), fun['fin']))
ok('PRISMA: estudos no modelo principal ≤ estudos do estrato principal', e0 <= fun['main'], '%d ≤ %d' % (e0, fun['main']))

# 4. painel publicado
if len(sys.argv) > 1:
    js = open(sys.argv[1], encoding='utf-8').read()

    def var(v):
        return json.loads(re.search(r'^  var %s = (.*);$' % v, js, re.M).group(1))
    data = var('DATA')
    ok('painel: nº de pares = dados_metanalise', len(data) == n_pares, '%d vs %d' % (len(data), n_pares))
    ok('painel: mesmos pares e ordem', all(abs(p[0] - float(d['fck'])) < 0.01 and abs(p[1] - float(d['co2_kg_m3'])) < 0.01
                                          for p, d in zip(data, dados)), 'fck e CO₂ par a par (2 casas)')
    ok('painel: MODELO = forest_site.json', var('MODELO') == forest, 'var MODELO')
    ok('painel: A4MODELO = a4_site.json', var('A4MODELO') == a4, 'var A4MODELO')
    ok('painel: A4 tem um registo por par', len(var('A4')) == n_pares, '%d' % len(var('A4')))
    m = re.search(r"\{ key: 'e4', n: (\d+), principal: (\d+), sensibilidade: (\d+) \}", js)
    ok('painel: funil = PRISMA', tuple(map(int, m.groups())) == (fun['fin'], fun['main'], fun['tier']), m.group(0))
    rel = int(re.search(r'\n    releitura: (\d+),', js).group(1))
    ok('painel: KPI de estudos com par = dados', rel == len(estudos), '%d vs %d' % (rel, len(estudos)))

rel = ['# Conferência da rodada', '', 'Gerado por `metanalise/conferir_rodada.py` em %s.' % datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),
       '', '**Resultado principal:** μ %.2f [%.2f–%.2f], k %d, %d estudos · %d pares no painel, %d estudos com par · corpus %d (%d principal + %d sensibilidade).'
       % (mu0, float(res['ic95_inf']), float(res['ic95_sup']), k0, e0, n_pares, len(estudos), fun['fin'], fun['main'], fun['tier']),
       '', '**%s**' % ('Tudo confere.' if not falhas else '%d verificação(ões) falharam: %s' % (len(falhas), '; '.join(falhas))),
       '', '| | Verificação | Valores |', '|---|---|---|'] + linhas
open(R + 'CONFERENCIA_RODADA.md', 'w', encoding='utf-8').write('\n'.join(rel) + '\n')
print('\n'.join(rel))
sys.exit(1 if falhas else 0)
