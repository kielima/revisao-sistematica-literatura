# ================================================================
# F63 (#1808 parte painel) — grelha do modelo com A4 para o controlo
# interactivo do painel kielima.com/metanalise.
# Decisão da Kiê (2026-11-27): A4 entra na dissertação como tabela
# (sensibilidade_a4.R) e no site como controlo interactivo distância × modo.
#
# Mesmas regras da F59 (sensibilidade_a4.R): estrato principal, CO2 sem
# desconto (F9), A4 somado só ao grupo `sim` (F38) — os «prováveis» numa
# opção à parte (D1, F59); factor SIDAC ×1 / ×1,5 / ×2,5 (D1).
# Diferença: aqui o modo é escolhido pelo leitor (o mesmo para todos os
# pares somados), em vez do modo padrão do tipo transportado.
#   A4 [kg CO2-eq/m3] = factor × coef_<modo> [kg CO2-eq/(m3·km)] × km
# (coef_<modo> = factor SIDAC × massa volúmica, do motor_a4.py).
#
# Entrada: dados_metanalise.csv + transporte_a4_motor.csv (por obs_id).
# Saída: resultados/a4_site.json  →  inserir_a4_site.py
# Uso: Rscript metanalise/exportar_a4_site.R  (da raiz do repositório)
# ================================================================
suppressPackageStartupMessages({ library(metafor); library(dplyr); library(parallel) })
source("metanalise/funcoes_modelo.R")

d <- read.csv("metanalise/dados_metanalise.csv", stringsAsFactors = FALSE)
m4 <- read.csv("metanalise/transporte_a4_motor.csv", stringsAsFactors = FALSE)
modos <- c("betoneira", "truck_3e", "carreta_4e", "carreta_5e")
cols <- paste0("coef_", modos, "_kg_m3_km")
m4 <- m4[, c("obs_id", "a4_grupo", cols)]
d <- left_join(d, m4, by = "obs_id")
stopifnot(!any(is.na(d$a4_grupo)))
d <- prepara_base(d)
princ <- subset(d, estrato == "principal" & sem_bruto == 0)

dist <- c(0, 10, 25, 50, 75, 100, 150, 200, 250, 300)
fac <- c(1, 1.5, 2.5)
grupos <- list(sim = "sim", sim_provavel = c("sim", "provavel"))

grid <- expand.grid(modo = modos, km = dist[dist > 0], factor = fac, grupos = names(grupos),
                    stringsAsFactors = FALSE)

fit <- function(i) {
  g <- grid[i, ]
  dd <- princ
  coef <- dd[[paste0("coef_", g$modo, "_kg_m3_km")]]
  coef[is.na(coef)] <- 0
  soma <- dd$a4_grupo %in% grupos[[g$grupos]]
  dd$yi <- ifelse(soma, (dd$co2_kg_m3 + g$factor * coef * g$km) / dd$fck, dd$ci)
  m <- ajusta(dd)
  c(mu = as.numeric(m$b[1]), lb = m$ci.lb[1], ub = m$ci.ub[1])
}

dd0 <- princ; dd0$yi <- dd0$ci
m0 <- ajusta(dd0)
ref <- c(mu = as.numeric(m0$b[1]), lb = m0$ci.lb[1], ub = m0$ci.ub[1])

r <- do.call(rbind, mclapply(seq_len(nrow(grid)), fit, mc.cores = max(1, detectCores())))
grid <- cbind(grid, r)

cen <- list()
for (i in seq_len(nrow(grid))) {
  g <- grid[i, ]
  cen[[sprintf("%s|%g|%g|%s", g$modo, g$km, g$factor, g$grupos)]] <-
    round(c(g$mu, g$lb, g$ub), 3)
}
out <- list(
  gerado = format(Sys.Date()),
  base = "estrato principal, CO2 sem desconto (F9); A4 só no grupo sim (F38) ou sim+provavel (opção à parte)",
  k = m0$k, estudos = length(unique(princ$estudo)),
  n_sim = sum(princ$a4_grupo == "sim"), n_provavel = sum(princ$a4_grupo == "provavel"),
  referencia = round(ref, 3), distancias = dist, factores = fac, modos = modos,
  cenarios = cen)
dir.create("metanalise/resultados", showWarnings = FALSE)
writeLines(jsonlite::toJSON(out, auto_unbox = TRUE, digits = NA),
           "metanalise/resultados/a4_site.json")
message("cenarios: ", length(cen))
