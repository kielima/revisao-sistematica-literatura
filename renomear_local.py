# -*- coding: utf-8 -*-
"""Aplica na pasta local os mesmos nomes ja aplicados no Google Drive.

Correr com a pasta dos PDFs como argumento, por exemplo:

    python renomear_local.py "C:\\...\\00_REFERENCIAS\\ARTIGOS ACEITOS APOS REMOCAO DAS DUPLICATAS"

Sem argumento faz apenas simulacao (nao renomeia nada) e diz o que faria.
A lista vem de RENOMEACAO_PDFS_2026-08-16.csv, que fica ao lado deste script.
"""
import csv, os, sys

pasta = sys.argv[1] if len(sys.argv) > 1 else None
lista = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     'RENOMEACAO_PDFS_2026-08-16.csv')

ok = falta = ja = 0
for r in csv.DictReader(open(lista, encoding='utf-8')):
    if pasta is None:
        print('%s  ->  %s' % (r['antigo'], r['novo']))
        continue
    a = os.path.join(pasta, r['antigo'])
    b = os.path.join(pasta, r['novo'])
    if os.path.exists(b):
        ja += 1
    elif os.path.exists(a):
        os.rename(a, b)
        ok += 1
    else:
        falta += 1
        print('NAO ENCONTRADO: %s' % r['antigo'])

if pasta is not None:
    print('renomeados: %d | ja estavam: %d | nao encontrados: %d' % (ok, ja, falta))
