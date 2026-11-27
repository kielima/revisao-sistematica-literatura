# ================================================================
# F60 (#1811) — sensibilidade do ci aos estudos secundários.
# Decisão da Kiê (2026-11-27, D2 da linha crítica): os pares dos estudos
# secundários (citados pelas revisões aceites; NASIR 2024, Tabela 4) entram
# SÓ numa análise de sensibilidade «principal + secundários», nunca no
# resultado principal.
#
# Regras seguidas:
#   - Mesmo estrato e filtros do principal: estrato principal, CO2 sem
#     desconto (F9), fck >= 20 MPa (F47).
#   - Os secundários não têm IC publicado no CSV → vi pelo híbrido de
#     funcoes_modelo.R (o mesmo dos pares sem IC do corpus).
#   - Cada estudo secundário é um estudo novo no nível «estudo» do modelo
#     (id 900000 + id_sec); obs_id «S<id_sec>_<n>».
#
# Entrada: dados_metanalise.csv + lotes_etapa2/SECUNDARIOS_E2_1811_*.csv
# Saída: resultados/sensibilidade_secundarios.csv
# Uso: Rscript metanalise/sensibilidade_secundarios.R  (da raiz do repositório)
# ================================================================
suppressPackageStartupMessages({ library(metafor); library(dplyr) })
source("metanalise/funcoes_modelo.R")

d <- read.csv("metanalise/dados_metanalise.csv", stringsAsFactors = FALSE)

fs <- Sys.glob("lotes_etapa2/SECUNDARIOS_E2_1811_*.csv")
s <- do.call(rbind, lapply(fs, read.csv, stringsAsFactors = FALSE))
s <- subset(s, !is.na(fck_mpa) & !is.na(co2_kg_m3) & fck_mpa >= 20)
s <- s |> group_by(id_sec) |> mutate(n = row_number()) |> ungroup()

sec <- data.frame(
  obs_id = paste0("S", s$id_sec, "_", s$n),
  estudo = 900000 + s$id_sec,
  rotulo = paste(s$autor_ano, "-", s$mistura),
  material = s$mistura,
  fck = s$fck_mpa,
  co2_kg_m3 = s$co2_kg_m3,
  ci = s$co2_kg_m3 / s$fck_mpa,
  estrato = "principal",
  familia = s$familia_proposta,
  base_portland = ifelse(s$base_portland == "sim", "P", "N"),
  sem_bruto = 0,
  stringsAsFactors = FALSE)
for (c in setdiff(names(d), names(sec))) sec[[c]] <- NA
sec <- sec[, names(d)]

princ <- subset(d, estrato == "principal" & sem_bruto == 0)   # A7 + F9
comb <- rbind(princ, sec)

roda <- function(nome, dd) {
  dd <- prepara_base(dd)
  dd$yi <- dd$ci
  m <- ajusta(dd)
  resumo(nome, m, dd)
}

res <- rbind(
  roda("principal (referencia)", princ),
  roda("principal + secundarios (F60)", comb),
  roda("so secundarios", prepara_base(sec)))
res$pares_secundarios <- c(0, nrow(sec), nrow(sec))
res$estudos_secundarios <- c(0, length(unique(sec$estudo)), length(unique(sec$estudo)))

dir.create("metanalise/resultados", showWarnings = FALSE)
write.csv(res, "metanalise/resultados/sensibilidade_secundarios.csv", row.names = FALSE)
print(res[, c("analise", "k", "estudos", "mu", "ic95_inf", "ic95_sup")], digits = 4)
