# -*- coding: utf-8 -*-
"""
Aplica na pasta LOCAL os mesmos movimentos que ja foram feitos no Google Drive
a 2026-08-21: renomear os 3 PDFs descarregados e move-los de
BAIXADOS MANUALMENTE para a pasta principal.

Correr a partir da pasta 'REVISÃO SISTEMÁTICA DE LITERATURA'.
Nao apaga nada; se o destino ja existir, avisa e nao mexe.
"""
import os, shutil

DEST = os.path.join('00_REFERENCIAS', 'ARTIGOS ACEITOS APÓS REMOÇÃO DAS DUPLICATAS')
ORIG = os.path.join(DEST, 'BAIXADOS MANUALMENTE')

RENOMEAR = [
    ('JSDEWES_d12.0488.pdf',        'KUMAR et al., 2024 - j.sdewes.d12.0488.pdf'),
    ('1-s2.0-S23527102240249.pdf',  'YU et al., 2024 - j.jobe.2024.110929.pdf'),
    ('materials-16-02020-v2.pdf',   'MOHAMMED et al., 2023 - ma16052020.pdf'),
]

for antigo, novo in RENOMEAR:
    src = os.path.join(ORIG, antigo)
    dst = os.path.join(DEST, novo)
    if not os.path.exists(src):
        print('NAO ENCONTRADO (talvez ja movido):', antigo); continue
    if os.path.exists(dst):
        print('DESTINO JA EXISTE, nao mexi:', novo); continue
    shutil.move(src, dst)
    print('movido:', antigo, '->', novo)

print()
print('NAO integrado, de proposito: Avaliacao_do_ciclo_de_.pdf')
print('  E o ARTIGO derivado (DOI 10.6008/CBPC2179-6858.2021.006.0031), nao a tese')
print('  da linha 4999. Fica em BAIXADOS MANUALMENTE ate a Kie decidir.')
