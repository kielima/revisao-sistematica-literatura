#!/usr/bin/env python3
"""Integra o resultado de um lote da Segunda Conferencia PDF x banco.

Uso: python3 merge_lote_result.py /tmp/loteN_result.txt
Formato de cada linha do ficheiro de entrada (pipe-separated):
fileId | pdf | veredito | titulo_pdf | doi_bate | autor_bate | publisher_bate | resumo_bate | nota(opcional)
"""
import csv, sys, re
from datetime import date

MASTER = 'VERIFICACAO_TITULO_AUTOR_DOI.csv'
PENDENTE = 'VERIFICACAO_PENDENTE_2026-08-31.csv'

def parse_result_file(path):
    rows = []
    with open(path, encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')
            if not line.strip():
                continue
            parts = [p.strip() for p in line.split('|')]
            while len(parts) < 9:
                parts.append('')
            fileId, pdf, veredito, titulo_pdf, doi_bate, autor_bate, publisher_bate, resumo_bate, nota = parts[:9]
            rows.append(dict(fileId=fileId, pdf=pdf, veredito=veredito, titulo_pdf=titulo_pdf,
                              doi_bate=doi_bate, autor_bate=autor_bate, publisher_bate=publisher_bate,
                              resumo_bate=resumo_bate, nota=nota))
    return rows

def main(result_path):
    results = parse_result_file(result_path)
    by_fileid = {r['fileId']: r for r in results}

    pendente_rows = []
    with open(PENDENTE, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        pendente_fields = reader.fieldnames
        for row in reader:
            pendente_rows.append(row)

    matched = []
    remaining = []
    for row in pendente_rows:
        fid = row['fileId_conhecido']
        if fid in by_fileid:
            matched.append((row, by_fileid[fid]))
        else:
            remaining.append(row)

    print(f'Lote: {len(by_fileid)} resultados recebidos, {len(matched)} casados com o worklist pendente, {len(pendente_rows)-len(remaining)} linhas removidas do pendente.')
    if len(matched) != len(by_fileid):
        unmatched_ids = set(by_fileid) - {m[0]['fileId_conhecido'] for m in matched}
        print('AVISO: fileIds no resultado sem correspondencia no pendente:', unmatched_ids)

    # master CSV: read, extend schema, append
    with open(MASTER, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        master_fields = reader.fieldnames
        master_rows = list(reader)

    extra_cols = ['publisher_bate', 'resumo_bate']
    new_fields = master_fields + [c for c in extra_cols if c not in master_fields]
    for row in master_rows:
        for c in extra_cols:
            row.setdefault(c, '')

    today = date.today().isoformat()
    non_confere = []
    for pend_row, res in matched:
        new_row = {c: '' for c in new_fields}
        new_row['pdf'] = pend_row['pdf']
        new_row['linhas'] = pend_row['linhas']
        new_row['doi_banco'] = pend_row['doi_banco']
        new_row['multi_doi'] = ''
        new_row['titulo_banco'] = pend_row['titulo_banco']
        new_row['primeiro_autor'] = pend_row['autor_banco'].split(' and ')[0] if pend_row['autor_banco'] else ''
        new_row['ano'] = pend_row['ano']
        new_row['journal'] = pend_row['journal']
        new_row['status'] = pend_row['status_triagem']
        new_row['sonda_anterior'] = ''
        new_row['veredito'] = res['veredito']
        new_row['titulo_pdf'] = res['titulo_pdf']
        new_row['autor_bate'] = res['autor_bate']
        new_row['doi_bate'] = res['doi_bate']
        new_row['nota'] = res['nota']
        new_row['verificado_em'] = today
        new_row['publisher_bate'] = res['publisher_bate']
        new_row['resumo_bate'] = res['resumo_bate']
        master_rows.append(new_row)
        if res['veredito'] != 'CONFERE':
            non_confere.append((pend_row, res))

    with open(MASTER, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=new_fields)
        w.writeheader()
        w.writerows(master_rows)

    with open(PENDENTE, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=pendente_fields)
        w.writeheader()
        w.writerows(remaining)

    print(f'Master CSV atualizado: +{len(matched)} linhas (total {len(master_rows)}).')
    print(f'Pendente CSV atualizado: restam {len(remaining)} ficheiros.')
    if non_confere:
        print(f'\n*** {len(non_confere)} NAO-CONFERE neste lote — requer atencao manual: ***')
        for pend_row, res in non_confere:
            linhas = pend_row['linhas']
            pdf = pend_row['pdf']
            veredito = res['veredito']
            nota = res['nota']
            print(f'  linha(s) {linhas} | {pdf} | veredito={veredito} | nota={nota}')

if __name__ == '__main__':
    main(sys.argv[1])
