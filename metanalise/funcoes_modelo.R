# ================================================================
# Funcoes comuns aos scripts do modelo (rma.mv REML) — partilhadas por
# metanalise_rma_mv_REML_v5.R e exportar_forest_site.R, para os dois
# usarem exactamente o mesmo vi e o mesmo ajuste.
# Decisoes: metanalise/DECISOES_METANALISE.md (A3, A4, A5, B1–B4).
# ================================================================

# B3 — classes de resistência a partir do fck numérico (grupos do v4)
classe_grupo <- function(f) {
  cut(f, breaks = c(-Inf, 22.5, 27.5, 32.5, 37.5, 42.5, 47.5, 52.5, 57.5, 90, Inf),
      labels = c("C<=20", "C25", "C30", "C35", "C40", "C45", "C50", "C55", "C60-C90", "UHPC"))
}

# B1/B2 — CV publicado (só desvio_padrao e cv_percentual)
cv_pub <- function(valor, tipo, media) {
  ifelse(tipo == "desvio_padrao" & !is.na(valor) & media != 0, abs(valor / media),
         ifelse(tipo == "cv_percentual" & !is.na(valor), valor / 100, NA_real_))
}
n_or_1 <- function(n) ifelse(is.na(n) | n < 1, 1, n)

# Acrescenta a classe e a variancia relativa publicada (vi = yi^2 * relvar, metodo delta) — vale para ci e ci_t
prepara_base <- function(d) {
  d$classe <- classe_grupo(d$fck)
  d$cv_fck <- cv_pub(d$ic_fck_valor, d$ic_fck_tipo, d$fck)
  d$cv_co2 <- cv_pub(d$ic_co2_valor, d$ic_co2_tipo, d$co2_kg_m3)
  d$relvar_pub <- with(d, ifelse(is.na(cv_fck) & is.na(cv_co2), NA_real_,
    ifelse(is.na(cv_fck), 0, cv_fck^2 / n_or_1(ic_fck_n)) +
    ifelse(is.na(cv_co2), 0, cv_co2^2 / n_or_1(ic_co2_n))))
  d
}

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

# I2 multinivel (Nakagawa & Santos / metafor FAQ)
i2_multinivel <- function(m) {
  W <- diag(1 / m$vi)
  X <- model.matrix(m)
  P <- W - W %*% X %*% solve(t(X) %*% W %*% X) %*% t(X) %*% W
  100 * sum(m$sigma2) / (sum(m$sigma2) + (m$k - m$p) / sum(diag(P)))
}

resumo <- function(nome, m, dd) {
  data.frame(analise = nome, k = m$k, estudos = length(unique(dd$estudo)),
             mu = as.numeric(m$b[1]), ic95_inf = m$ci.lb[1], ic95_sup = m$ci.ub[1],
             pi95_inf = predict(m)$pi.lb[1], pi95_sup = predict(m)$pi.ub[1],
             tau2_estudos = m$sigma2[1], tau2_formulacoes = m$sigma2[2], I2_total = i2_multinivel(m),
             QE = m$QE, QEp = m$QEp)
}
