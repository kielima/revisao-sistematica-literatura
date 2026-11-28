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
# Saída: resultados/a4_site.json (superfície km 0–300)  →  inserir_a4_site.py
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

dist <- 0:300
fac <- c(1, 1.5, 2.5)
grupos <- list(sim = "sim", sim_provavel = c("sim", "provavel"))

# Superfície de resposta exacta (F63, Kiê 2026-11-28: «superfície de resposta com
# todos os km de 0 a 300»): um ajuste REML por km × veículo × factor × grupo, sem
# interpolação. sparse = TRUE dá o mesmo resultado que o ajuste denso (testado:
# μ e IC95 iguais até à 6.ª casa) em ~0,6 s em vez de ~39 s.
ajusta_rapido <- function(dd) {
  dd$vi <- monta_vi(dd, NULL)
  rma.mv(yi, vi, random = ~ 1 | estudo / obs_id, data = dd, method = "REML", sparse = TRUE)
}

grid <- expand.grid(km = dist[dist > 0], modo = modos, factor = fac, grupos = names(grupos),
                    stringsAsFactors = FALSE)

fit <- function(i) {
  g <- grid[i, ]
  dd <- princ
  coef <- dd[[paste0("coef_", g$modo, "_kg_m3_km")]]
  coef[is.na(coef)] <- 0
  soma <- dd$a4_grupo %in% grupos[[g$grupos]]
  dd$yi <- ifelse(soma, (dd$co2_kg_m3 + g$factor * coef * g$km) / dd$fck, dd$ci)
  m <- ajusta_rapido(dd)
  c(mu = as.numeric(m$b[1]), lb = m$ci.lb[1], ub = m$ci.ub[1])
}

dd0 <- princ; dd0$yi <- dd0$ci
m0 <- ajusta_rapido(dd0)
m0d <- ajusta(dd0)  # conferência com o ajuste denso do resto do projecto
stopifnot(abs(m0$b[1] - m0d$b[1]) < 1e-6, abs(m0$ci.lb[1] - m0d$ci.lb[1]) < 1e-6)
ref <- c(mu = as.numeric(m0$b[1]), lb = m0$ci.lb[1], ub = m0$ci.ub[1])

r <- do.call(rbind, mclapply(seq_len(nrow(grid)), fit, mc.cores = max(1, detectCores())))
grid <- cbind(grid, r)

# superficie[grupo][modo|factor] = [mu[], lb[], ub[]] com 301 valores (km 0..300)
sup <- list()
for (gr in names(grupos)) {
  sup[[gr]] <- list()
  for (mo in modos) for (f in fac) {
    s <- grid[grid$grupos == gr & grid$modo == mo & grid$factor == f, ]
    s <- s[order(s$km), ]
    sup[[gr]][[sprintf("%s|%g", mo, f)]] <- list(
      round(c(ref[1], s$mu), 3), round(c(ref[2], s$lb), 3), round(c(ref[3], s$ub), 3))
  }
}
out <- list(
  gerado = format(Sys.Date()),
  base = "estrato principal, CO2 sem desconto (F9); A4 só no grupo sim (F38) ou sim+provavel (opção à parte); um ajuste por km",
  k = m0$k, estudos = length(unique(princ$estudo)),
  n_sim = sum(princ$a4_grupo == "sim"), n_provavel = sum(princ$a4_grupo == "provavel"),
  referencia = round(ref, 3), km_max = max(dist), factores = fac, modos = modos,
  superficie = sup)
dir.create("metanalise/resultados", showWarnings = FALSE)
writeLines(jsonlite::toJSON(out, auto_unbox = TRUE, digits = NA),
           "metanalise/resultados/a4_site.json")
message("ajustes: ", nrow(grid))
