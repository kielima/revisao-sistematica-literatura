# ================================================================
# Resultados do modelo (rma.mv REML) para o forest «ci por familia de material» do painel
# kielima.com/metanalise — pedido da Kie, 2026-10-16 (F28): «Coloque os resultados do modelo em R
# no forestplot do site».
#
# O painel tem filtros (estrato, base do ligante, cenario do CO2) e o botao ci / ci_t; para o
# forest mostrar sempre o modelo do subconjunto que esta no ecra, o modelo e ajustado em cada
# combinacao: estrato {p, s, ps} x base {todos, portland} x CO2 {sem, com} x indicador {ci, cit}
# = 24 cenarios (60 desde a F33: o indicador ci_t tem 4 formas de vida util). Em cada um: modelo sem moderadores (media global, IC95, IP95, I2) e modelo com
# a familia como moderador sem intercepto (media por familia, IC95) — o mesmo da secao 7 do v5.
# Mesmo vi e mesmo ajuste do v5 (metanalise/funcoes_modelo.R).
#
# Correr da raiz do repo, depois de python3 metanalise/preparar_dados.py:
#   Rscript metanalise/exportar_forest_site.R
# Saida: metanalise/resultados/forest_site.json (o metanalise.js do kielima-site recebe-o na linha
# `var MODELO = ...`).
# ================================================================

suppressPackageStartupMessages({
  library(metafor)
  library(dplyr)
  library(jsonlite)
})
source("metanalise/funcoes_modelo.R")

d <- read.csv("metanalise/dados_metanalise.csv", encoding = "UTF-8", stringsAsFactors = FALSE)
d$estudo <- factor(d$estudo)
d$obs_id <- factor(d$obs_id)
d <- prepara_base(d)
# F33 (Kie, 2026-10-17): ci_t em todos os pares. Indicadores: ci, cit (vida pela hierarquia: declarada >
# citada > norma pela aplicacao > 50 anos) e, como sensibilidade, citf (vida media por familia, valores dos
# estudos), citm (so os de base «modelo») e citn (so os de base «norma» ou a norma pela aplicacao).
# Cada um tem a versao sem desconto (ci_t*) e com desconto (ci_t*_com).
vida_ind <- list(cit = "vida_util", citf = "vida_fam", citm = "vida_fam_modelo", citn = "vida_fam_norma")
for (k in names(vida_ind)) {
  v <- d[[vida_ind[[k]]]]
  ok <- !(is.na(v) | v <= 0)
  d[[paste0("y_", k, "_sem")]] <- ifelse(ok, d$ci / v, NA_real_)
  d[[paste0("y_", k, "_com")]] <- ifelse(ok, d$ci_com_desconto / v, NA_real_)
}

subconjunto <- function(estrato, base, co2, ind) {
  dd <- d
  if (estrato == "p") dd <- subset(dd, estrato == "principal")
  if (estrato == "s") dd <- subset(dd, estrato == "sensibilidade")
  if (base == "portland") dd <- subset(dd, base_portland == "sim")
  if (co2 == "sem") dd <- subset(dd, sem_bruto == 0)          # F9
  col <- if (ind == "ci") (if (co2 == "sem") "ci" else "ci_com_desconto") else
    paste0("y_", ind, "_", co2)
  dd$yi <- dd[[col]]
  dd <- subset(dd, !is.na(yi))
  droplevels(dd)
}

num <- function(x) if (is.null(x) || length(x) == 0 || is.na(x)) NULL else signif(as.numeric(x), 6)

um_cenario <- function(estrato, base, co2, ind) {
  dd <- subconjunto(estrato, base, co2, ind)
  out <- list(k = nrow(dd), estudos = length(unique(dd$estudo)))
  if (nrow(dd) < 3 || length(unique(dd$estudo)) < 2) return(out)
  m <- tryCatch(ajusta(dd), error = function(e) NULL)
  if (!is.null(m)) {
    p <- predict(m)
    out$global <- list(mu = num(m$b[1]), lb = num(m$ci.lb[1]), ub = num(m$ci.ub[1]),
                       pi_lb = num(p$pi.lb[1]), pi_ub = num(p$pi.ub[1]), i2 = num(i2_multinivel(m)))
  }
  dd$familia <- factor(dd$familia)
  mf <- if (nlevels(dd$familia) > 1) tryCatch(ajusta(dd, mods = "familia - 1"), error = function(e) NULL) else NULL
  fam <- list()
  if (!is.null(mf)) {
    nomes <- sub("^familia", "", rownames(mf$b))
    for (i in seq_along(nomes)) {
      sub_d <- dd[dd$familia == nomes[i], ]
      fam[[nomes[i]]] <- list(mu = num(mf$b[i]), lb = num(mf$ci.lb[i]), ub = num(mf$ci.ub[i]),
                              k = nrow(sub_d), estudos = length(unique(sub_d$estudo)))
    }
  }
  out$familias <- fam
  out
}

grade <- expand.grid(estrato = c("ps", "p", "s"), base = c("todos", "portland"), co2 = c("sem", "com"),
                     ind = c("ci", "cit", "citf", "citm", "citn"), stringsAsFactors = FALSE)
res <- parallel::mclapply(seq_len(nrow(grade)), function(i) {
  g <- grade[i, ]
  t0 <- Sys.time()
  r <- um_cenario(g$estrato, g$base, g$co2, g$ind)
  message(sprintf("%s|%s|%s|%s k=%d %.0fs", g$estrato, g$base, g$co2, g$ind, r$k,
                  as.numeric(difftime(Sys.time(), t0, units = "secs"))))
  r
}, mc.cores = max(1, parallel::detectCores()))
names(res) <- with(grade, paste(estrato, base, co2, ind, sep = "|"))

saida <- list(gerado = format(Sys.Date()), metodo = "rma.mv REML, random = ~1 | estudo/obs_id (metafor)",
              pares = nrow(d), cenarios = res)
write_json(saida, "metanalise/resultados/forest_site.json", auto_unbox = TRUE, null = "null", digits = NA)
message("ok -> metanalise/resultados/forest_site.json")
