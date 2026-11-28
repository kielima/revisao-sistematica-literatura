"""Gera a tabela de TODOS os números da metanálise a partir dos ficheiros de resultados, para a
escrita dos capítulos (Resultados #1937, Discussão #1938, Conclusão #1939, Resumo #1940).

Pedido da Kiê (2026-11-28): o congelamento de 02/12 deixa de ser feito à mão — a rodada final
(rodada_final.sh) gera este documento e, na quarta, basta copiá-lo para
metanalise/RESULTADOS_CONGELADOS_2026-12-02.md e fazer a tag.

Uso: python3 metanalise/gerar_resultados.py [saida.md]
     (por omissão metanalise/resultados/RESULTADOS_RODADA.md)
Números em notação portuguesa (vírgula decimal), arredondados a 2 casas (ci) ou 3 (ci_t).
"""
import csv, datetime, subprocess, sys

R = 'metanalise/resultados/'
SAIDA = sys.argv[1] if len(sys.argv) > 1 else R + 'RESULTADOS_RODADA.md'


def ler(p):
    return list(csv.DictReader(open(p, encoding='utf-8')))


def n(x, d=2):
    try:
        v = float(x)
    except (TypeError, ValueError):
        return '—'
    s = '{:,.{d}f}'.format(v, d=d)
    return s.replace(',', ' ').replace('.', ',').replace(' ', '.').replace('-', '−')


def inteiro(x):
    return n(x, 0)


def p_txt(x):
    v = float(x)
    return '< 0,001' if v < 0.001 else n(v, 3)


def ic(r, d=2, a='ic95_inf', b='ic95_sup'):
    est = r.get('mu') or r.get('estimativa') or r.get('coef')
    sep = ' a ' if float(r[a]) < 0 else '–'   # «−7,39 a −4,62» em vez de «−7,39–−4,62»
    return '%s [%s%s%s]' % (n(est, d), n(r[a], d), sep, n(r[b], d))


out = []
w = out.append
commit = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True).stdout.strip()
w('# Resultados da metanálise — todos os números')
w('')
w('Gerado por `metanalise/gerar_resultados.py` em %s, commit `%s`. Fonte de cada número: os ficheiros de `metanalise/resultados/` e `00_REFERENCIAS/PRISMA/FUNIL_PRISMA.csv` dessa versão. Unidade do `ci`: kg CO₂-eq/(m³·MPa); do `ci_t`: kg CO₂-eq/(m³·MPa·ano). IC = intervalo de confiança de 95 %%; IP = intervalo de predição de 95 %%.'
  % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M'), commit))

# 1. PRISMA
w('\n## 1. Fluxo PRISMA\n')
w('| Caixa | n | Filtro |')
w('|---|---|---|')
fun = ler('00_REFERENCIAS/PRISMA/FUNIL_PRISMA.csv')
for r in fun:
    w('| %s | %s | %s |' % (r['caixa'], inteiro(r['n']), r['filtro'].replace('|', '/')))

# 2. corpus
dados = ler('metanalise/dados_metanalise.csv')
w('\n## 2. Corpus da metanálise\n')
w('- Pares fck × CO₂ no painel e no modelo: **%s**, de **%s** estudos.' % (inteiro(len(dados)), inteiro(len({d['estudo'] for d in dados}))))
for est in ['principal', 'sensibilidade']:
    sub = [d for d in dados if d['estrato'] == est]
    w('- Estrato %s: %s pares, %s estudos.' % (est, inteiro(len(sub)), inteiro(len({d['estudo'] for d in sub}))))
sem = [d for d in dados if d['sem_bruto'] in ('1', '1.0', 'TRUE', 'True')]
w('- Pares só com CO₂ publicado com desconto (fora do cenário «sem desconto», F9): %s.' % inteiro(len(sem)))

# 3. principal
res = ler(R + 'resumo_modelos.csv')
p = res[0]
w('\n## 3. Resultado principal\n')
w('Estrato principal, CO₂ sem desconto, `rma.mv` REML (metafor) com efeitos aleatórios estudo/formulação, matrizes esparsas (F64).\n')
w('| Medida | Valor |')
w('|---|---|')
w('| k (pares) / estudos | %s / %s |' % (inteiro(p['k']), inteiro(p['estudos'])))
w('| ci médio [IC 95 %%] | **%s** |' % ic(p))
w('| IP 95 %% | %s – %s |' % (n(p['pi95_inf']), n(p['pi95_sup'])))
w('| τ² entre estudos / entre formulações | %s / %s |' % (n(p['tau2_estudos']), n(p['tau2_formulacoes'])))
w('| I² total | %s %% |' % n(p['I2_total'], 2))
w('| Q (gl = %s) | %s, p %s |' % (inteiro(int(p['k']) - 1), n(p['QE'], 0), p_txt(p['QEp'])))

w('\n## 4. Todas as análises do modelo v5\n')
w('| Análise | k | Estudos | Estimativa [IC 95 %] | IP 95 % | I² |')
w('|---|---|---|---|---|---|')
for r in res:
    d = 3 if r['analise'].startswith('ci_t') else 2
    w('| %s | %s | %s | %s | %s – %s | %s %% |' % (r['analise'], inteiro(r['k']), inteiro(r['estudos']), ic(r, d),
                                                  n(r['pi95_inf'], d), n(r['pi95_sup'], d), n(r['I2_total'], 2)))

# 5. famílias e moderadores
w('\n## 5. Famílias de material (subgrupos)\n')
w('| Família | k | ci [IC 95 %] |')
w('|---|---|---|')
for r in sorted(ler(R + 'subgrupos_familia.csv'), key=lambda r: -float(r['mu'])):
    w('| %s | %s | %s |' % (r['familia'], inteiro(r['k']), ic(r)))
mods = ler(R + 'moderadores.csv')
w('\n**Moderadores** (teste omnibus QM):\n')
w('| Moderador | k | QM | p |')
w('|---|---|---|---|')
vistos = set()
for r in mods:
    if r['moderador'] in vistos:
        continue
    vistos.add(r['moderador'])
    w('| %s | %s | %s | %s |' % (r['moderador'], inteiro(r['k']), n(r['QM']), p_txt(r['QMp'])))
w('\n<details><summary>Coeficientes de cada moderador</summary>\n')
w('| Moderador | Termo | Estimativa [IC 95 %] | p |')
w('|---|---|---|---|')
for r in mods:
    w('| %s | %s | %s | %s |' % (r['moderador'], r['termo'], ic(r), p_txt(r['p'])))
w('\n</details>')

# 6. viés e robustez
eg = {r['termo']: r for r in ler(R + 'egger_multinivel.csv')}
w('\n## 6. Viés de publicação e robustez\n')
w('- Egger multinível (moderador = erro-padrão): declive %s (EP %s), p %s; intercepto %s.' % (
    n(eg['sei']['estimativa'], 3), n(eg['sei']['se'], 3), p_txt(eg['sei']['p']), n(eg['intrcpt']['estimativa'])))
loo = [r for r in ler(R + 'leave_one_study_out.csv') if r['mu'] not in ('', 'NA')]
lo = min(loo, key=lambda r: float(r['mu']))
hi = max(loo, key=lambda r: float(r['mu']))
w('- Leave-one-study-out (%s estudos): μ entre %s (sem o estudo %s) e %s (sem o estudo %s).' % (
    inteiro(len(loo)), n(lo['mu']), lo['estudo_omitido'], n(hi['mu']), hi['estudo_omitido']))

# 7. sensibilidades
for f, titulo in [('sensibilidade_a2', 'Transporte das matérias-primas (A2, F57)'),
                  ('sensibilidade_corpo_prova', 'Base de medição do fck (#1454)'),
                  ('sensibilidade_a4', 'Transporte até à obra (A4, F59)'),
                  ('sensibilidade_secundarios', 'Estudos secundários (F60)')]:
    w('\n## %s\n' % ('7.%d. %s' % (['sensibilidade_a2', 'sensibilidade_corpo_prova', 'sensibilidade_a4', 'sensibilidade_secundarios'].index(f) + 1, titulo)))
    rows = ler(R + f + '.csv')
    extra = 'dif_vs_referencia_pct' in rows[0]
    w('| Análise | k | Estudos | ci [IC 95 %%] |%s' % (' Δ vs sem A4 |' if extra else ''))
    w('|---|---|---|---|%s' % ('---|' if extra else ''))
    for r in rows:
        w('| %s | %s | %s | %s |%s' % (r['analise'], inteiro(r['k']), inteiro(r['estudos']), ic(r),
                                      (' %s |' % ('—' if r['dif_vs_referencia_pct'] in ('', 'NA') else n(r['dif_vs_referencia_pct'], 1) + ' %')) if extra else ''))
    mod = R + f + '_moderador.csv'
    try:
        mr = ler(mod)
        w('\n**Moderador** (diferença no ci): ' + '; '.join('%s: %s, p %s (k %s)' % (r['analise'], ic(r), p_txt(r['pval']), inteiro(r['k']))
                                                             for r in mr if r.get('pval') not in (None, '', 'NA')) + '.')
    except FileNotFoundError:
        pass

open(SAIDA, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('escrito', SAIDA, '(%d linhas)' % len(out))
