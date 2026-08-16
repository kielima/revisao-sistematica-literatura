#!/usr/bin/env python3
"""Validacoes de integridade do vault da RSL, executadas pelo CI.

Este repositorio nao e um projeto de software: e um vault de revisao sistematica
(notas .md, scripts .py de analise e planilhas .xlsx de triagem). O CI, portanto,
nao "compila" nada — verifica que os artefactos de dados continuam legiveis e que
o layout de colunas documentado no CLAUDE.md nao mudou por acidente.

Verificacoes:
  1. Todos os .py versionados compilam (sintaxe valida).
  2. As planilhas activas abrem com openpyxl e tem as abas esperadas.
  3. O mapa de colunas de articles_final.xlsx bate com o documentado no CLAUDE.md
     (a "ARMADILHA FATAL" da coluna material_C2 entre C2 e C3).
  4. Todos os .csv versionados fazem parse.
  5. Nenhum PDF foi versionado por engano (o .gitignore exclui *.pdf de proposito).

Saida: codigo 0 se tudo passar, 1 se qualquer verificacao falhar. Todas as
verificacoes correm sempre — o script nao aborta na primeira falha, para que um
unico run de CI mostre todos os problemas de uma vez.
"""

from __future__ import annotations

import csv
import py_compile
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# Planilhas activas na raiz -> abas que tem de existir. So estas sao validadas:
# as ~110 xlsx de "02_ARQUIVOS ANTERORES" sao backups congelados (ver CLAUDE.md,
# "Regra de arquivamento"), centenas de MB que nao ha valor em reabrir a cada push.
ACTIVE_WORKBOOKS = {
    "articles_final.xlsx": ["Articles", "Critérios"],
    "meta_analysis_base.xlsx": ["dados_fck", "LEGENDA"],
    "GRÁFICOS DA RSL.xlsx": ["Planilha1"],
}

# Mapa de colunas de articles_final.xlsx (aba Articles), 1-based, tal como
# documentado no CLAUDE.md. material_C2 fica ENTRE C2 e C3 — e essa a armadilha
# que ja causou um bug de deslocamento em C3-C8 (2026-06-21).
EXPECTED_COLUMNS = {
    11: "pdf",
    12: "url",
    20: "status_triagem",
    21: "C1",
    22: "C2",
    23: "material_C2",
    24: "C3",
    25: "C4",
    26: "C5",
    27: "C6",
    28: "C7",
    29: "C8",
    32: "comments",
    33: "rastreio_potencial_futuro",
}

failures: list[str] = []


def fail(msg: str) -> None:
    failures.append(msg)
    print(f"  FALHA: {msg}")


def tracked_files(pattern: str) -> list[Path]:
    """Ficheiros versionados que casam com o pattern, via git ls-files.

    Usa git em vez de glob para nao apanhar lixo nao versionado (venv, caches)
    nem os ~1.900 PDFs que existem na pasta local mas nao no repo.
    """
    out = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files", "-z", pattern],
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    return [ROOT / name for name in out.split("\0") if name]


def check_python_syntax() -> None:
    print("\n[1/5] Sintaxe dos scripts Python")
    files = tracked_files("*.py")
    if not files:
        print("  (nenhum .py versionado)")
        return
    for path in files:
        try:
            # cfile num temporario: nao queremos __pycache__ a sujar o vault.
            with tempfile.NamedTemporaryFile(suffix=".pyc", delete=True) as tmp:
                py_compile.compile(str(path), cfile=tmp.name, doraise=True)
            print(f"  ok  {path.relative_to(ROOT)}")
        except py_compile.PyCompileError as exc:
            fail(f"{path.relative_to(ROOT)} nao compila: {exc}")


def check_workbooks() -> None:
    print("\n[2/5] Planilhas activas abrem e tem as abas esperadas")
    import openpyxl

    for name, expected_sheets in ACTIVE_WORKBOOKS.items():
        path = ROOT / name
        if not path.exists():
            fail(f"planilha activa ausente: {name}")
            continue
        try:
            wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
        except Exception as exc:  # noqa: BLE001 — qualquer falha de leitura conta
            fail(f"{name} nao abre com openpyxl: {exc}")
            continue
        try:
            missing = [s for s in expected_sheets if s not in wb.sheetnames]
            if missing:
                fail(f"{name}: abas em falta {missing} (tem {wb.sheetnames})")
            else:
                print(f"  ok  {name} -> {wb.sheetnames}")
        finally:
            wb.close()


def check_column_map() -> None:
    print("\n[3/5] Mapa de colunas de articles_final.xlsx (aba Articles)")
    import openpyxl

    path = ROOT / "articles_final.xlsx"
    if not path.exists():
        fail("articles_final.xlsx ausente — mapa de colunas nao verificado")
        return

    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    try:
        if "Articles" not in wb.sheetnames:
            fail("articles_final.xlsx sem aba 'Articles'")
            return
        ws = wb["Articles"]
        header = next(ws.iter_rows(min_row=1, max_row=1, values_only=True), ())
        mismatches = 0
        for index, expected in EXPECTED_COLUMNS.items():
            actual = header[index - 1] if index <= len(header) else None
            if actual != expected:
                mismatches += 1
                fail(
                    f"coluna {index} devia ser '{expected}' mas e '{actual}' — "
                    "o mapa do CLAUDE.md ficou dessincronizado da planilha"
                )
        if mismatches == 0:
            print(f"  ok  {len(EXPECTED_COLUMNS)} colunas na posicao documentada")
    finally:
        wb.close()


def check_csvs() -> None:
    print("\n[4/5] Parse dos CSV versionados")
    files = tracked_files("*.csv")
    if not files:
        print("  (nenhum .csv versionado)")
        return
    for path in files:
        try:
            # utf-8-sig: varios destes CSV sairam do Excel e trazem BOM.
            with path.open(newline="", encoding="utf-8-sig", errors="strict") as fh:
                rows = sum(1 for _ in csv.reader(fh))
            print(f"  ok  {path.relative_to(ROOT)} ({rows} linhas)")
        except (UnicodeDecodeError, csv.Error) as exc:
            fail(f"{path.relative_to(ROOT)} nao faz parse: {exc}")


def check_no_pdfs() -> None:
    print("\n[5/5] Nenhum PDF versionado")
    pdfs = tracked_files("*.pdf") + tracked_files("*.PDF")
    if pdfs:
        for path in pdfs[:20]:
            fail(f"PDF versionado por engano: {path.relative_to(ROOT)}")
        if len(pdfs) > 20:
            fail(f"... e mais {len(pdfs) - 20} PDFs")
    else:
        print("  ok  nenhum PDF no indice do git")


def main() -> int:
    print(f"Validacao do vault RSL — raiz: {ROOT}")
    check_python_syntax()
    check_workbooks()
    check_column_map()
    check_csvs()
    check_no_pdfs()

    print()
    if failures:
        print(f"RESULTADO: {len(failures)} falha(s).")
        return 1
    print("RESULTADO: todas as verificacoes passaram.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
