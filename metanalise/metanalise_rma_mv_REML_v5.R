# ================================================================
# Metanálise multinível da intensidade de carbono por resistência — v5
# ----------------------------------------------------------------
# Dissertação: Kiê — PUC-Campinas (2026)
# Sucede ao v4 (00_REFERENCIAS/METODOLOGIA_ESTATÍSTICA/), que lia o
# snapshot de maio (139 linhas, 37 estudos). O v5 lê o banco actual
# através de metanalise/preparar_dados.py (mesmos pares do painel).
#
# Todas as decisões estão em metanalise/DECISOES_METANALISE.md
# (códigos A1–A10 = Kiê; B1–B6 = implementação por confirmar).
#
# Correr da raiz do repo:
#   python3 metanalise/preparar_dados.py
#   Rscript metanalise/metanalise_rma_mv_REML_v5.R
# ================================================================

suppressPackageStartupMessages({
  library(metafor)
  library(dplyr)
})
set.seed(20260513)

entrada <- "metanalise/dados_metanalise.csv"
out_dir <- "metanalise/resultados"
dir.create(file.path(out_dir, "figuras"), showWarnings = FALSE, recursive = TRUE)

d <- read.csv(entrada, encoding = "UTF-8", stringsAsFactors = FALSE)
d$estudo <- factor(d$estudo)
d$obs_id <- factor(d$obs_id)
d$yi <- d$ci                                   # A2

# ----------------------------------------------------------------
# 2. vi
# ----------------------------------------------------------------
# B3 — classes de resistência a partir do fck numérico (grupos do v4)
classe_grupo <- function(f) {
  cut(f, breaks = c(-Inf, 22.5, 27.5, 32.5, 37.5, 42.5, 47.5, 52.5, 57.5, 90, Inf),
      labels = c("C<=20", "C25", "C30", "C35", "C40", "C45", "C50", "C55", "C60-C90", "UHPC"))
}
d$classe <- classe_grupo(d$fck)

# B1/B2 — CV publicado (só desvio_padrao e cv_percentual)
cv_pub <- function(valor, tipo, media) {
  ifelse(tipo == "desvio_padrao" & !is.na(valor) & media != 0, abs(valor / media),
         ifelse(tipo == "cv_percentual" & !is.na(valor), valor / 100, NA_real_))
}
d$cv_fck <- cv_pub(d$ic_fck_valor, d$ic_fck_tipo, d$fck)
d$cv_co2 <- cv_pub(d$ic_co2_valor, d$ic_co2_tipo, d$co2_kg_m3)
n_or_1 <- function(n) ifelse(is.na(n) | n < 1, 1, n)
# variancia relativa publicada (vi = yi^2 * relvar, metodo delta) — vale para ci e ci_mpa
d$relvar_pub <- with(d, ifelse(is.na(cv_fck) & is.na(cv_co2), NA_real_,
  ifelse(is.na(cv_fck), 0, cv_fck^2 / n_or_1(ic_fck_n)) +
  ifelse(is.na(cv_co2), 0, cv_co2^2 / n_or_1(ic_co2_n))))

VI_MIN <- 1e-8                                 # B4

vi_hibrido <- function(dd) {                   # A3, calculado no subconjunto analisado
  g <- dd |> group_by(classe) |> summarise(n_g = n(), var_g = var(yi), .groups = "drop")
  dd <- left_join(dd, g, by = "classe")
  ifelse(dd$n_g >= 4 & !is.na(dd$var_g) & dd$var_g > 0, dd$var_g, (0.05 * dd$yi)^2)
}

monta_vi <- function(dd, cv_assumido = NULL) {  # A4 (+ A5 quando cv_assumido)
  base <- if (is.null(cv_assumido)) vi_hibrido(dd) else (cv_assumido * dd$yi)^2
  vi <- ifelse(!is.na(dd$relvar_pub), dd$yi^2 * dd$relvar_pub, base)
  pmax(vi, VI_MIN)
}

ajusta <- function(dd, yi = "yi", cv_assumido = NULL, mods = NULL) {
  dd$yi_ <- dd[[yi]]
  dd$yi <- dd$yi_
  dd$vi <- monta_vi(dd, cv_assumido)
  if (is.null(mods))
    return(rma.mv(yi_, vi, random = ~ 1 | estudo / obs_id, data = dd, method = "REML"))
  rma.mv(yi_, vi, mods = as.formula(paste("~", mods)), random = ~ 1 | estudo / obs_id,
         data = dd, method = "REML")
}

resumo <- function(nome, m, dd) {
  W <- diag(1 / m$vi)
  X <- model.matrix(m)
  P <- W - W %*% X %*% solve(t(X) %*% W %*% X) %*% t(X) %*% W
  i2 <- 100 * sum(m$sigma2) / (sum(m$sigma2) + (m$k - m$p) / sum(diag(P)))
  data.frame(analise = nome, k = m$k, estudos = length(unique(dd$estudo)),
             mu = as.numeric(m$b[1]), ic95_inf = m$ci.lb[1], ic95_sup = m$ci.ub[1],
             pi95_inf = predict(m)$pi.lb[1], pi95_sup = predict(m)$pi.ub[1],
             tau2_estudos = m$sigma2[1], tau2_formulacoes = m$sigma2[2], I2_total = i2,
             QE = m$QE, QEp = m$QEp)
}

princ <- subset(d, estrato == "principal")       # A7
tudo <- d

# ----------------------------------------------------------------
# 4. Modelo principal (A1, A2, A4, A7)
# ----------------------------------------------------------------
m_princ <- ajusta(princ)
res <- resumo("principal (ci, vi publicado + hibrido)", m_princ, princ)

# ----------------------------------------------------------------
# 5. Sensibilidade
# ----------------------------------------------------------------
res <- rbind(res, resumo("principal + sensibilidade (A7)", ajusta(tudo), tudo))
for (k in c(0.05, 0.10, 0.15)) {                 # A5
  res <- rbind(res, resumo(sprintf("principal, CV assumido %d%% (A5)", round(100 * k)),
                           ajusta(princ, cv_assumido = k), princ))
}
port <- subset(princ, base_portland == "sim")
res <- rbind(res, resumo("principal, so cimento Portland", ajusta(port), port))

# ----------------------------------------------------------------
# 6. Analise secundaria — ci_mpa (A6)
# ----------------------------------------------------------------
sec <- subset(princ, !is.na(ci_mpa))
sec$yi <- sec$ci_mpa
res <- rbind(res, resumo("secundaria: ci_mpa (kg CO2-eq/MPa), principal com volume", ajusta(sec), sec))

write.csv(res, file.path(out_dir, "resumo_modelos.csv"), row.names = FALSE)

# ----------------------------------------------------------------
# 7. Moderadores (A8, B5) — estrato principal
# ----------------------------------------------------------------
princ$idade_cat <- ifelse(is.na(princ$idade_dias), "nao_declarada",
                          ifelse(princ$idade_dias == 28, "28d", "outra"))
princ$familia <- relevel(factor(princ$familia), ref = "opc")
princ$base_portland <- relevel(factor(princ$base_portland), ref = "sim")
princ$idade_cat <- relevel(factor(princ$idade_cat), ref = "28d")
mods_res <- list()
for (mo in c("familia", "base_portland", "idade_cat")) {
  mm <- ajusta(princ, mods = mo)
  mods_res[[mo]] <- data.frame(moderador = mo, termo = rownames(mm$b), estimativa = as.numeric(mm$b),
                               ic95_inf = mm$ci.lb, ic95_sup = mm$ci.ub, p = mm$pval,
                               QM = mm$QM, QMp = mm$QMp, k = mm$k)
}
write.csv(do.call(rbind, mods_res), file.path(out_dir, "moderadores.csv"), row.names = FALSE)

# Media por familia (subgrupos, sem intercepto)
mf <- ajusta(princ, mods = "familia - 1")
write.csv(data.frame(familia = sub("^familia", "", rownames(mf$b)), mu = as.numeric(mf$b),
                     ic95_inf = mf$ci.lb, ic95_sup = mf$ci.ub,
                     k = as.numeric(table(princ$familia)[sub("^familia", "", rownames(mf$b))])),
          file.path(out_dir, "subgrupos_familia.csv"), row.names = FALSE)

# ----------------------------------------------------------------
# 8. Vies de publicacao (B6)
# ----------------------------------------------------------------
princ$vi <- monta_vi(princ)
princ$sei <- sqrt(princ$vi)
egger <- rma.mv(yi, vi, mods = ~ sei, random = ~ 1 | estudo / obs_id, data = princ, method = "REML")
write.csv(data.frame(termo = rownames(egger$b), estimativa = as.numeric(egger$b),
                     se = egger$se, p = egger$pval),
          file.path(out_dir, "egger_multinivel.csv"), row.names = FALSE)

png(file.path(out_dir, "figuras", "funil_principal.png"), width = 1600, height = 1200, res = 200)
funnel(m_princ, xlab = "ci (kg CO2-eq / m3 / MPa)")
dev.off()

writeLines(capture.output(print(m_princ), sessionInfo()), file.path(out_dir, "modelo_principal.txt"))
print(res, digits = 4)

# Leave-one-study-out (influencia de cada estudo na media principal).
# B7: em paralelo (mclapply) e com os sigma2 do modelo completo como valores iniciais —
# a corrida sequencial passava dos 30 min. Desligar com LOO=0.
if (Sys.getenv("LOO", "1") != "0") {
  ini <- m_princ$sigma2
  princ$vi <- monta_vi(princ)          # vi do modelo completo (as classes de A3 nao mudam ao tirar um estudo)
  loo <- parallel::mclapply(levels(droplevels(princ$estudo)), function(s) {
    dd <- droplevels(subset(princ, estudo != s))
    mm <- tryCatch(rma.mv(yi, vi, random = ~ 1 | estudo / obs_id, data = dd, method = "REML",
                          control = list(sigma2.init = ini)), error = function(e) NULL)
    if (is.null(mm)) return(data.frame(estudo_omitido = s, mu = NA, ic95_inf = NA, ic95_sup = NA))
    data.frame(estudo_omitido = s, mu = as.numeric(mm$b), ic95_inf = mm$ci.lb, ic95_sup = mm$ci.ub)
  }, mc.cores = max(1, parallel::detectCores()))
  write.csv(do.call(rbind, loo), file.path(out_dir, "leave_one_study_out.csv"), row.names = FALSE)
}
