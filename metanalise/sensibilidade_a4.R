# ================================================================
# #1808 (parte R) — sensibilidade do ci ao transporte do betao (A4).
# Linha critica de 26/11 (metanalise/LINHA_CRITICA_2026-12-02.md, §2).
#
# Regras ja decididas que este script segue:
#   - F38 (Kie, 2026-10-31): A4 so somado onde a4_somavel = sim (grupo
#     `sim` do motor); os pares «provaveis» so numa opcao a parte.
#   - F48/F55: A4 = factor SIDAC x massa volumica x distancia, com o modo
#     padrao do tipo transportado (motor_a4.py -> transporte_a4_motor.csv).
#   - F9: estrato principal, so pares com CO2 sem desconto (sem_bruto = 0).
# Por confirmar (D1 da linha critica / F49): factor SIDAC x1,5 e x2,5
# como sensibilidade de factor. O script calcula-os sempre; se a Kie
# disser que nao, basta nao os reportar.
#
# Os pares fora do grupo somado entram SEM A4 (como no resultado
# principal): mede-se o efeito de somar o A4 onde ele pode ser somado,
# sem tirar estudos do modelo. O cenario «so grupo sim» compara o mesmo
# subconjunto com e sem A4.
#
# Entrada: dados_metanalise.csv + transporte_a4_motor.csv (por obs_id).
# Saida: resultados/sensibilidade_a4.csv
# Uso: Rscript metanalise/sensibilidade_a4.R  (a partir da raiz do repositorio)
# ================================================================
suppressPackageStartupMessages({ library(metafor); library(dplyr) })
source("metanalise/funcoes_modelo.R")

d <- read.csv("metanalise/dados_metanalise.csv", stringsAsFactors = FALSE)
m4 <- read.csv("metanalise/transporte_a4_motor.csv", stringsAsFactors = FALSE)
m4 <- m4[, c("obs_id", "a4_grupo", "a4_50km", "a4_100km", "a4_200km", "a4_300km")]
d <- left_join(d, m4, by = "obs_id")
stopifnot(!any(is.na(d$a4_grupo)))          # todos os pares do painel estao no motor
d <- prepara_base(d)

princ <- subset(d, estrato == "principal" & sem_bruto == 0)   # A7 + F9

# ci com A4 somado aos pares dos grupos indicados (os outros ficam sem A4)
com_a4 <- function(dd, km, factor = 1, grupos = "sim") {
  a4 <- dd[[paste0("a4_", km, "km")]]
  a4[is.na(a4)] <- 0
  soma <- dd$a4_grupo %in% grupos
  dd$yi <- ifelse(soma, (dd$co2_kg_m3 + factor * a4) / dd$fck, dd$ci)
  dd
}
sem_a4 <- function(dd) { dd$yi <- dd$ci; dd }

cen <- list()
cen[["principal, sem A4 (referencia)"]] <- sem_a4(princ)
for (km in c(50, 100, 200, 300))
  cen[[sprintf("principal, A4 grupo sim, %d km, SIDAC x1", km)]] <- com_a4(princ, km)
for (f in c(1.5, 2.5))
  cen[[sprintf("principal, A4 grupo sim, 100 km, SIDAC x%s", f)]] <- com_a4(princ, 100, f)
cen[["principal, A4 grupo sim, 300 km, SIDAC x2.5 (pior caso)"]] <- com_a4(princ, 300, 2.5)
cen[["principal, A4 grupos sim+provavel, 100 km, SIDAC x1 (opcao a parte, F38)"]] <-
  com_a4(princ, 100, 1, c("sim", "provavel"))
so_sim <- subset(princ, a4_grupo == "sim")
cen[["so grupo sim, sem A4"]] <- sem_a4(so_sim)
cen[["so grupo sim, A4 100 km, SIDAC x1"]] <- com_a4(so_sim, 100)

res <- do.call(rbind, lapply(names(cen), function(n) {
  dd <- cen[[n]]
  message(sprintf("%s: k=%d", n, nrow(dd)))
  resumo(n, ajusta(dd), dd)
}))
ref <- res$mu[1]
res$dif_vs_referencia_pct <- round(100 * (res$mu / ref - 1), 2)
res$dif_vs_referencia_pct[grepl("^so grupo sim", res$analise)] <- NA

write.csv(res, "metanalise/resultados/sensibilidade_a4.csv", row.names = FALSE)
print(res[, c("analise", "k", "estudos", "mu", "ic95_inf", "ic95_sup", "dif_vs_referencia_pct")])
