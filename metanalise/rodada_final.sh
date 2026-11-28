#!/usr/bin/env bash
# ================================================================
# Rodada final da metanálise (#1976, F62/F64) — um só comando, pela ordem certa.
# Kiê (2026-11-28): «Pode fazer o script único da rodada final.»
#
# Uso (da raiz do repositório):
#   bash metanalise/rodada_final.sh [--site ../kielima-site] [--recalcular] [--sem-superficie-a4]
#
#   --site DIR            também actualiza o painel (DATA, funil, KPI, MODELO, A4, mapa, banco)
#                         no clone do kielima-site em DIR — não faz commit nem PR.
#   --recalcular          corre antes recalcular_ci.py e classificar_base_portland.py (escrevem
#                         meta_analysis_base.xlsx; só o integrador, depois do corte). Se nada
#                         mudar, o .xlsx é reposto byte a byte (sem commit inútil de 6 MB).
#   --sem-superficie-a4   salta exportar_a4_site.R (27 min); usa o a4_site.json existente.
#
# Passos: (0) dependências → (1) [recalcular] → (2) PRISMA → (3) pares do modelo e do A4 →
# (4) modelo v5 com leave-one-out → (5) sensibilidades → (6) forest e superfície do A4 →
# (7) [site] → (8) conferência (metanalise/resultados/CONFERENCIA_RODADA.md).
# Pára no primeiro erro. Registo de cada passo em metanalise/resultados/rodada_logs/ (não versionado).
# Tempo com sparse = TRUE (F64): ~3 min + 27 min da superfície do A4.
# ================================================================
set -euo pipefail
cd "$(dirname "$0")/.."

SITE=""; RECALC=0; SUP=1
while [ $# -gt 0 ]; do
  case "$1" in
    --site) SITE="$(cd "$2" && pwd)"; shift 2 ;;
    --recalcular) RECALC=1; shift ;;
    --sem-superficie-a4) SUP=0; shift ;;
    *) echo "opção desconhecida: $1" >&2; exit 2 ;;
  esac
done

PY=/usr/bin/python3            # o python do sistema tem o openpyxl
LOGS=metanalise/resultados/rodada_logs
mkdir -p "$LOGS"
T0=$(date +%s)

passo() {  # passo "nome" comando...
  local nome="$1"; shift
  local s; s=$(date +%s)
  printf '▶ %-48s' "$nome"
  if "$@" > "$LOGS/$(echo "$nome" | tr ' /' '__').log" 2>&1; then
    printf '✓ %4ss\n' "$(( $(date +%s) - s ))"
  else
    printf '✗\n'; echo "Falhou: $nome — ver $LOGS/$(echo "$nome" | tr ' /' '__').log" >&2
    tail -20 "$LOGS/$(echo "$nome" | tr ' /' '__').log" >&2; exit 1
  fi
}

# (0) dependências
if ! Rscript -e 'suppressMessages({library(metafor); library(dplyr); library(jsonlite)})' >/dev/null 2>&1; then
  echo "A instalar R + metafor (uma vez por máquina)…"
  apt-get update -qq && apt-get install -y -qq r-base-core r-cran-metafor r-cran-dplyr r-cran-jsonlite >/dev/null
fi
$PY -c 'import openpyxl' || { echo "falta openpyxl em $PY" >&2; exit 1; }
if [ -n "$SITE" ] && ! $PY -c 'import pycountry' 2>/dev/null; then   # metanalise-export-mapa.py
  apt-get install -y -qq python3-pycountry >/dev/null 2>&1 || $PY -m pip install -q --break-system-packages pycountry
fi

# (1) colunas derivadas no xlsx (opcional)
if [ $RECALC = 1 ]; then
  ANTES=$($PY - <<'EOF'
import openpyxl, hashlib
ws = openpyxl.load_workbook('meta_analysis_base.xlsx', read_only=True)['dados_fck']
print(hashlib.sha256(repr(list(ws.iter_rows(values_only=True))).encode()).hexdigest())
EOF
)
  passo "recalcular_ci" $PY recalcular_ci.py
  passo "classificar_base_portland" $PY classificar_base_portland.py
  DEPOIS=$($PY - <<'EOF'
import openpyxl, hashlib
ws = openpyxl.load_workbook('meta_analysis_base.xlsx', read_only=True)['dados_fck']
print(hashlib.sha256(repr(list(ws.iter_rows(values_only=True))).encode()).hexdigest())
EOF
)
  if [ "$ANTES" = "$DEPOIS" ]; then
    git checkout -- meta_analysis_base.xlsx; echo "  (dados_fck sem alterações — .xlsx reposto)"
  else
    echo "  ⚠ dados_fck mudou com o recálculo — rever e fazer commit do .xlsx"
  fi
fi

# (2) PRISMA
passo "PRISMA (contar_funil_prisma)" $PY 00_REFERENCIAS/PRISMA/contar_funil_prisma.py

# (3) pares do modelo e do A4
passo "preparar_dados" $PY metanalise/preparar_dados.py
passo "motor_a4" $PY metanalise/motor_a4.py
passo "exportar_a2" $PY metanalise/exportar_a2.py
passo "exportar_corpo_prova" $PY metanalise/exportar_corpo_prova.py

# (4) modelo
passo "modelo v5 com leave-one-out" Rscript metanalise/metanalise_rma_mv_REML_v5.R

# (5) sensibilidades
for s in a2 corpo_prova a4 secundarios; do
  passo "sensibilidade_$s" Rscript metanalise/sensibilidade_$s.R
done

# (6) painel: forest e superfície do A4
passo "exportar_forest_site" Rscript metanalise/exportar_forest_site.R
if [ $SUP = 1 ]; then
  passo "superfície do A4 (27 min)" Rscript metanalise/exportar_a4_site.R
else
  echo "▷ superfície do A4 saltada (--sem-superficie-a4)"
fi

# (7) site
JS=""
if [ -n "$SITE" ]; then
  JS="$SITE/public/assets/metanalise.js"
  EXP=$(mktemp)
  passo "metanalise-export" bash -c "$PY metanalise-export.py > '$EXP'"
  passo "site: DATA, funil e KPI" $PY metanalise/inserir_dados_site.py "$EXP" "$JS"
  passo "site: MODELO" $PY metanalise/inserir_modelo_site.py metanalise/resultados/forest_site.json "$JS"
  passo "site: A4" $PY metanalise/inserir_a4_site.py "$JS"
  # escreve primeiro num temporário: um erro nunca deixa o ficheiro do site vazio
  D="$SITE/public/metanalise/dados"
  passo "site: mapa" bash -c "$PY metanalise-export-mapa.py > '$EXP.mapa' && mv '$EXP.mapa' '$D/mapa.json'"
  passo "site: banco" bash -c "$PY metanalise-export-banco.py > '$EXP.banco' && mv '$EXP.banco' '$D/banco.json'"
  rm -f "$EXP" "$EXP.mapa" "$EXP.banco"
fi

# (8) conferência
echo
if $PY metanalise/conferir_rodada.py $JS > "$LOGS/conferencia.log" 2>&1; then
  sed -n '5,7p' metanalise/resultados/CONFERENCIA_RODADA.md
  echo "✓ Rodada completa em $(( ($(date +%s) - T0) / 60 )) min — metanalise/resultados/CONFERENCIA_RODADA.md"
else
  cat "$LOGS/conferencia.log"; echo "✗ A conferência falhou — NÃO congelar." >&2; exit 1
fi
[ -n "$SITE" ] && echo "Site actualizado em $SITE (sem commit): correr 'npm run testar' e abrir o PR."
exit 0
