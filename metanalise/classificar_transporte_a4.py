"""F41 fase 1 (Kie, 2026-11-08, #0619 'Pode comecar'): classifica o que e transportado
em cada par (fck, CO2) da aba dados_fck, para o motor A4 da F40 (fases 2-3).
Le SO campos ja extraidos (material, aplicacao, tipo_corpo_prova, fronteira_texto,
transporte_dados, fronteira_nota). NAO altera dados_fck nem os pares do painel:
escreve metanalise/transporte_a4_fase1.csv. Classes:
  betao_fresco_betoneira | elemento_prefabricado | pre_mistura_seca | sem_transporte_lab | indeterminado
Confianca: declarado (palavra-chave no texto do estudo) | provavel (so pela aplicacao) | nenhuma.
Uso: /usr/bin/python3 metanalise/classificar_transporte_a4.py
"""
import csv, re, collections, openpyxl
wb = openpyxl.load_workbook('meta_analysis_base.xlsx', read_only=True)
rows = list(wb['dados_fck'].iter_rows(values_only=True))
H = {n: i for i, n in enumerate(rows[0])}
def g(r, n): return str(r[H[n]] or '')
PREF = re.compile(r'pre-?fabric|prefabric|precast|pre-?cast|pre-?moldad|pr[eé]-?moldad|pre-?fabricad|pr[eé]-?fabricad|prestress|protendid', re.I)
SECA = re.compile(r'dry[- ]?mix|pre-?mix|premix|pr[eé]-?mistur|argamassa ensacad|bagged|ensacad', re.I)
FRESCO = re.compile(r'ready[- ]?mix|mixer truck|truck mixer|transit mixer|usinad|betoneira|central dosadora|batching plant|concrete plant|centrale de b[eé]ton|cast[- ]?in[- ]?(situ|place)|in[- ]?situ|moldad[oa] in loco', re.I)
LAB = re.compile(r'laborat|lab-scale|bench', re.I)
out = []
for r in rows[1:]:
    if not g(r, 'co2_kg_m3') or not g(r, 'fck_mpa'):
        continue
    txt = ' '.join(g(r, n) for n in ('material', 'fronteira_texto', 'transporte_dados', 'fronteira_nota'))
    ap = g(r, 'aplicacao')
    cls, conf, regra = 'indeterminado', 'nenhuma', ''
    for pat, c, nome in ((PREF, 'elemento_prefabricado', 'palavra-chave prefabricado/precast'),
                         (SECA, 'pre_mistura_seca', 'palavra-chave pre-mistura seca'),
                         (FRESCO, 'betao_fresco_betoneira', 'palavra-chave betao usinado/in situ')):
        m = pat.search(txt)
        if m:
            cls, conf, regra = c, 'declarado', f'{nome}: "{m.group(0)}"'
            break
    else:
        if ap == 'pre_fabricado_corrente':
            cls, conf, regra = 'elemento_prefabricado', 'provavel', 'aplicacao=pre_fabricado_corrente'
        elif ap in ('edificio', 'infraestrutura', 'pavimento', 'ponte'):
            cls, conf, regra = 'betao_fresco_betoneira', 'provavel', f'aplicacao={ap} (betao de obra por defeito)'
        elif g(r, 'transporte_betao_a4') == 'incluido':
            cls, conf, regra = 'betao_fresco_betoneira', 'provavel', 'A4 do betao incluido no estudo, sem outra pista'
    out.append([g(r, 'row_id'), g(r, 'doi'), g(r, 'autores')[:40], g(r, 'ano'), ap, g(r, 'transporte_betao_a4'),
                g(r, 'a4_somavel'), cls, conf, regra])
with open('metanalise/transporte_a4_fase1.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['row_id', 'doi', 'autores', 'ano', 'aplicacao', 'transporte_betao_a4', 'a4_somavel', 'classe', 'confianca', 'regra'])
    w.writerows(out)
c = collections.Counter((o[7], o[8]) for o in out)
print(len(out), 'pares'); [print(k, v) for k, v in sorted(c.items())]
