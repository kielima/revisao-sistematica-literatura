"""
Script de padronização: fck medido → fck nominal na METANÁLISE.

Aplica f'c = f'cm,28 - Δ (Δ depende do código adotado pelo estudo) e arredonda
à classe nominal mais próxima entre as classes EN 206/EC2/NBR 6118 (cilindro):
12, 16, 20, 25, 30, 32, 35, 40, 45, 50, 55, 60, 70, 80, 90, 100, 120, 150, 200.

Recalcula:
  - col J (ci) na METANÁLISE: novo ci = ci_velho × fck_velho / fck_nominal
  - col K (ci_t)               : novo ci_t = novo ci / vida_útil
  - col R/S na ANÁLISE         : médias por artigo

Adiciona col O "Classe nominal (EN/NBR)" na METANÁLISE.

Executado em: 2026-05-12 / Kiê / Cowork.
"""
from copy import copy
import csv
import openpyxl

CAMINHO = "BANCO DE DADOS DA RSL.xlsx"
LOG_NEW = "LOG_AUDITORIA_NORMALIZACAO_CO2EQ_v2.csv"

CONVERSOES = {
    # ASSUNCAO 2020 — argamassa, NBR 6118, Δ=8 MPa
    2:  (40, "C40/50",   "fck NOMINAL — convertido de medido fcm=47.4 MPa via Δ=8 MPa (NBR 6118). 47.4-8=39.4 → C40"),
    3:  (45, "C45/55",   "fck NOMINAL — convertido de medido fcm=52.7 MPa via Δ=8 MPa (NBR 6118). 52.7-8=44.7 → C45"),
    4:  (40, "C40/50",   "fck NOMINAL — convertido de medido fcm=48.4 MPa via Δ=8 MPa (NBR 6118). 48.4-8=40.4 → C40"),
    # DU et al. 2024 — China, cita EN 206-1, Δ=8 MPa
    5:  (12, "LC12/13",  "fck NOMINAL — convertido de medido fcm=17.97 MPa via Δ=8 MPa (EN 206-1). 17.97-8=9.97 → LC12 (concreto leve)"),
    6:  (30, "C30/37",   "fck NOMINAL — convertido de medido fcm=38.72 MPa via Δ=8 MPa (EN 206-1). 38.72-8=30.72 → C30"),
    # LI et al. 2024 — China, AAM equivalente OPC, Δ=8 MPa
    12: (45, "C45/55",   "fck NOMINAL — convertido de medido fcm=51.1 MPa via Δ=8 MPa (EN 206/GB 50010). 51.1-8=43.1 → C45"),
    13: (45, "C45/55",   "fck NOMINAL — convertido de medido fcm=51.1 MPa via Δ=8 MPa (EN 206/GB 50010). 51.1-8=43.1 → C45"),
    # SOLTANZADEH et al. 2022 — Portugal, autor declara C50
    14: (50, "C50/60",   "fck NOMINAL — autor declara classe alvo C50 (Tabela 2 e texto: 'designed to pertain to the C50 strength class', fcm,target=60 MPa). Valor medido fcm=58.10 substituído por nominal 50."),
    # HABIBI et al. 2024 — UK, EN 206, Δ=8 MPa
    15: (25, "C25/30",   "fck NOMINAL — convertido de medido fcm=33.9 MPa via Δ=8 MPa (EN 206). 33.9-8=25.9 → C25 (fcm,EC2 para C25/30 = 33 MPa)"),
    16: (25, "C25/30",   "fck NOMINAL — convertido de medido fcm=33.4 MPa via Δ=8 MPa (EN 206). 33.4-8=25.4 → C25"),
    # BHAGAT et al. 2021 — Índia, IS/EN, Δ=8 MPa. Banco grava 55.8 para todos (M1-OPC pico); manter classe alvo C50.
    18: (50, "C50/60",   "fck NOMINAL — convertido de medido fcm=55.8 MPa (M1-OPC) via Δ=8 MPa. 55.8-8=47.8 → C50"),
    19: (50, "C50/60",   "fck NOMINAL — banco grava fcm=55.8 (pico M1); Δ=8 → C50. ATENÇÃO: PDF Tabela 4 reporta M2=40.2 MPa — possível erro de cadastro do fck medido (revisar)"),
    20: (50, "C50/60",   "fck NOMINAL — banco grava fcm=55.8 (pico M1); Δ=8 → C50. ATENÇÃO: PDF Tabela 4 reporta M3=24.0 MPa — possível erro de cadastro do fck medido (revisar)"),
    21: (50, "C50/60",   "fck NOMINAL — convertido de medido fcm=55.8 MPa via Δ=8 MPa. 55.8-8=47.8 → C50"),
    22: (50, "C50/60",   "fck NOMINAL — banco grava fcm=55.8 (pico M1); Δ=8 → C50. ATENÇÃO: PDF Tabela 4 reporta M6=42.0 MPa — possível erro de cadastro do fck medido (revisar)"),
    # CHOI et al. 2023 — Coreia do Sul, cita BS EN 206, UHPC. Δ=8 MPa.
    27: (120, "C120 (UHPC)", "fck NOMINAL — convertido de medido fcm=128 MPa via Δ=8 MPa (BS EN 206:2013). 128-8=120 → C120 (faixa UHPC). Faixa medida 86.3-128; pico declarado RS-F-17-2.0."),
    # COELHO 2016 — Brasil, NBR. Autor agrupa em 3 classes faixa: 1A(20-35), 1B(35-50), 2(50-80). Uso valor mediano da faixa.
    28: (25, "C25/30 (Classe 1A)", "fck NOMINAL — autor agrupa em Classe 1A (faixa 20-35 MPa); mediana → C25"),
    29: (40, "C40/50 (Classe 1B)", "fck NOMINAL — autor agrupa em Classe 1B (faixa 35-50 MPa); mediana → C40"),
    30: (60, "C60/75 (Classe 2)",  "fck NOMINAL — assumido Classe 2 (faixa 50-80 MPa); mediana → C60. ATENÇÃO: 'caso' precisa confirmação de mapeamento Classe 1A/1B/2 (revisar com autor)"),
    # MIR et al. 2022 — Qatar, BS 8500 (deriva de EN 206), Δ=8 MPa.
    39: (45, "C45/55",   "fck NOMINAL — convertido de medido fcm=52.3 MPa via Δ=8 MPa (BS 8500/EN 206). 52.3-8=44.3 → C45"),
    41: (50, "C50/60",   "fck NOMINAL — convertido de medido fcm=56.5 MPa via Δ=8 MPa (BS 8500/EN 206). 56.5-8=48.5 → C50"),
    # TEPLY et al. 2018 — Tcheca, EN 206, Δ=8 MPa. Cubos 60-day já convertidos para cilindro via ×0.8.
    47: (50, "C50/60",   "fck NOMINAL — cube 60d=71.9 MPa → cyl×0.8=57.52 fcm; Δ=8 (EN 206) → 49.52 → C50"),
    48: (30, "C30/37",   "fck NOMINAL — cube 60d=47.2 MPa → cyl×0.8=37.76 fcm; Δ=8 (EN 206) → 29.76 → C30"),
    49: (50, "C50/60",   "fck NOMINAL — cube 60d=70.5 MPa → cyl×0.8=56.4 fcm; Δ=8 (EN 206) → 48.4 → C50"),
}


def fck_para_classe(fck):
    if fck is None:
        return None
    try:
        fck = float(fck)
    except (TypeError, ValueError):
        return None
    mapa = {
        12: "LC12/13", 16: "LC16/18", 20: "C20/25", 25: "C25/30",
        30: "C30/37", 32: "C32/40", 35: "C35/45", 40: "C40/50",
        45: "C45/55", 50: "C50/60", 55: "C55/67", 60: "C60/75",
        70: "C70/85", 80: "C80/95", 90: "C90/105", 100: "C100/115",
        120: "C120 (UHPC)", 150: "C150 (UHPC)", 200: "C200 (UHPC)"
    }
    if fck in mapa:
        return mapa[fck]
    if abs(fck - round(fck)) < 1e-6 and int(round(fck)) in mapa:
        return mapa[int(round(fck))]
    return f"C{int(round(fck))} (não-padrão)"


def main():
    wb = openpyxl.load_workbook(CAMINHO)
    meta = wb["METANÁLISE"]
    anal = wb["ANÁLISE"]

    cabecalho_classe = "Classe nominal (EN/NBR)"
    nova_col_idx = 15  # O
    existe = False
    for c in range(1, meta.max_column + 1):
        if meta.cell(row=1, column=c).value == cabecalho_classe:
            nova_col_idx = c
            existe = True
            break
    if not existe:
        font_h = copy(meta.cell(row=1, column=14).font)
        align_h = copy(meta.cell(row=1, column=14).alignment)
        fill_h = copy(meta.cell(row=1, column=14).fill)
        meta.cell(row=1, column=nova_col_idx).value = cabecalho_classe
        meta.cell(row=1, column=nova_col_idx).font = font_h
        meta.cell(row=1, column=nova_col_idx).alignment = align_h
        meta.cell(row=1, column=nova_col_idx).fill = fill_h

    log_rows = [[
        "linha", "ID_observacao", "estudo", "fck_velho_MPa", "fck_novo_MPa",
        "delta_MPa", "norma", "classe_nominal", "ci_velho", "ci_novo",
        "ci_t_velho", "ci_t_novo", "vida_util_anos", "comentario_aplicado",
        "alterado"
    ]]

    distribuicao = {}
    linhas_alteradas = 0

    for r in range(2, meta.max_row + 1):
        idobs = meta.cell(row=r, column=1).value
        estudo = meta.cell(row=r, column=2).value
        fck_velho = meta.cell(row=r, column=4).value
        vu = meta.cell(row=r, column=9).value
        ci_velho = meta.cell(row=r, column=10).value
        cit_velho = meta.cell(row=r, column=11).value
        coment_velho = meta.cell(row=r, column=14).value or ""

        if r in CONVERSOES:
            fck_novo, classe_nom, justificativa = CONVERSOES[r]
            try:
                fck_v = float(fck_velho)
                ci_v = float(ci_velho) if ci_velho is not None else None
                ci_novo = round(ci_v * fck_v / fck_novo, 5) if ci_v is not None else None
            except (TypeError, ValueError):
                ci_novo = None
            try:
                vu_n = float(vu) if vu is not None else None
                cit_novo = round(ci_novo / vu_n, 5) if (ci_novo is not None and vu_n is not None and vu_n > 0) else None
            except (TypeError, ValueError):
                cit_novo = None

            if "Δ=8" in justificativa:
                delta_str = "8"
            elif "autor declara" in justificativa.lower() or "autor agrupa" in justificativa.lower() or "assumido" in justificativa.lower():
                delta_str = "0"
            else:
                delta_str = "—"

            meta.cell(row=r, column=4).value = fck_novo
            meta.cell(row=r, column=10).value = ci_novo
            if cit_novo is not None:
                meta.cell(row=r, column=11).value = cit_novo
            stamp = f"[{justificativa}]"
            if coment_velho and stamp not in coment_velho:
                meta.cell(row=r, column=14).value = (coment_velho + " | " + stamp).strip(" |")
            else:
                meta.cell(row=r, column=14).value = stamp
            meta.cell(row=r, column=nova_col_idx).value = classe_nom
            linhas_alteradas += 1

            log_rows.append([
                r, idobs, estudo, fck_velho, fck_novo, delta_str,
                "EN 206/EC2 (default)" if delta_str == "8" else ("autor" if delta_str == "0" else "—"),
                classe_nom, ci_velho, ci_novo, cit_velho, cit_novo, vu,
                justificativa, "SIM"
            ])
        else:
            classe_nom = fck_para_classe(fck_velho)
            meta.cell(row=r, column=nova_col_idx).value = classe_nom
            log_rows.append([
                r, idobs, estudo, fck_velho, fck_velho, "—", "—",
                classe_nom, ci_velho, ci_velho, cit_velho, cit_velho, vu,
                "(já nominal — sem conversão)", "NÃO"
            ])

        cn = meta.cell(row=r, column=nova_col_idx).value
        distribuicao[cn] = distribuicao.get(cn, 0) + 1

    # --- Atualizar col R/S na ANÁLISE com novas médias por estudo ---
    por_estudo = {}
    for r in range(2, meta.max_row + 1):
        est = meta.cell(row=r, column=2).value
        ci = meta.cell(row=r, column=10).value
        cit = meta.cell(row=r, column=11).value
        inc = meta.cell(row=r, column=13).value
        if est is None:
            continue
        por_estudo.setdefault(est, []).append((ci, cit, inc))

    atualizados_anal_R = 0
    atualizados_anal_S = 0
    for r in range(2, anal.max_row + 1):
        est = anal.cell(row=r, column=1).value
        if est is None or est not in por_estudo:
            continue
        cis = [t[0] for t in por_estudo[est] if t[2] is True and t[0] is not None and isinstance(t[0], (int, float))]
        cits = [t[1] for t in por_estudo[est] if t[2] is True and t[1] is not None and isinstance(t[1], (int, float))]
        R_val = anal.cell(row=r, column=18).value
        S_val = anal.cell(row=r, column=19).value
        if R_val is not None and cis:
            anal.cell(row=r, column=18).value = round(sum(cis) / len(cis), 5)
            atualizados_anal_R += 1
        if S_val is not None and cits:
            anal.cell(row=r, column=19).value = round(sum(cits) / len(cits), 5)
            atualizados_anal_S += 1

    wb.save(CAMINHO)

    with open(LOG_NEW, "w", encoding="utf-8", newline="") as f:
        wr = csv.writer(f, delimiter=";")
        wr.writerows(log_rows)

    print(f"Linhas METANÁLISE alteradas: {linhas_alteradas}")
    print(f"Linhas ANÁLISE col R atualizadas: {atualizados_anal_R}")
    print(f"Linhas ANÁLISE col S atualizadas: {atualizados_anal_S}")
    print(f"Coluna 'Classe nominal' inserida na col {nova_col_idx} ({openpyxl.utils.get_column_letter(nova_col_idx)})")
    print("\nDistribuição final por classe nominal:")
    for k, v in sorted(distribuicao.items(), key=lambda kv: (str(kv[0]) if kv[0] is not None else "")):
        print(f"  {k!r:35} → {v}")


if __name__ == "__main__":
    main()
