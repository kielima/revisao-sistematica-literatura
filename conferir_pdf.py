#!/usr/bin/env python3
"""Extrai titulo, autores e DOIs de um resultado guardado do read_file_content.

Uso: conferir_pdf.py <ficheiro-do-tool-result> [doi_do_banco]
Imprime so o essencial para o veredito, sem despejar o artigo todo no contexto.
"""
import json, re, sys, unicodedata

def carregar(p):
    t = open(p, encoding='utf-8', errors='replace').read()
    try:
        return json.loads(t).get('fileContent', '')
    except Exception:
        m = re.search(r'"fileContent"\s*:\s*"', t)
        if not m:
            return t
        return json.loads(t[m.start()-1:].split('\n')[0] if False else t)['fileContent']

def limpa(s):
    s = re.sub(r'\n{2,}', '\n', s)
    return re.sub(r'[ \t]{2,}', ' ', s).strip()

def main():
    p = sys.argv[1]
    doi_banco = (sys.argv[2] if len(sys.argv) > 2 else '').strip().lower()
    txt = carregar(p)
    n = len(txt)
    print(f'== {n} caracteres extraidos ==')
    if n == 0:
        print('VAZIO -> provavelmente digitalizado, precisa de OCR')
        return
    print('\n--- inicio (titulo/autores/afiliacao) ---')
    print(limpa(txt[:1400]))
    dois = re.findall(r'10\.\d{4,9}/[-._;()/:A-Za-z0-9]+', txt)
    dois = [d.rstrip('.,;)>]').lower() for d in dois]
    print(f'\n--- DOIs no ficheiro: {len(dois)} ocorrencias, {len(set(dois))} distintos ---')
    vistos = {}
    for d in dois:
        vistos.setdefault(d, txt.lower().find(d))
    for d, pos in sorted(vistos.items(), key=lambda x: x[1])[:12]:
        zona = 'FRENTE' if pos < n * 0.12 else ('meio' if pos < n * 0.75 else 'referencias')
        print(f'  {pos:7} {zona:12} {d}')
    if doi_banco:
        pos = txt.lower().find(doi_banco)
        print(f'\n--- DOI do banco: {doi_banco} ---')
        if pos < 0:
            print('  AUSENTE do texto')
        else:
            zona = 'FRENTE' if pos < n * 0.12 else ('meio' if pos < n * 0.75 else 'referencias')
            print(f'  presente na posicao {pos} ({zona}), {dois.count(doi_banco)} ocorrencia(s)')

main()
