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
# 2. vi — funcoes em metanalise/funcoes_modelo.R (B1–B4, A3–A5), partilhadas com exportar_forest_site.R
# ----------------------------------------------------------------
source("metanalise/funcoes_modelo.R")
d <- prepara_base(d)

# F9 (Kie, 2026-10-07): os pares cujo artigo so publica o CO2 ja com desconto (sem_bruto = 1)
# ficam fora do cenario sem desconto e so entram no cenario com desconto
princ_todos <- subset(d, estrato == "principal")
princ <- subset(princ_todos, sem_bruto == 0)     # A7 + F9
tudo <- subset(d, sem_bruto == 0)

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
# F1 (2026-10-07): cenario com os descontos que o proprio artigo declara (carga evitada, carbonatacao,
# biogenico, modulo D) e cenario so com pares que publicam o bruto
comd <- princ_todos; comd$yi <- comd$ci_com_desconto
res <- rbind(res, resumo("principal, CO2 com desconto (F1, F9: inclui os pares so com desconto)",
                         ajusta(comd, yi = "ci_com_desconto"), comd))
port <- subset(princ, base_portland == "sim")
res <- rbind(res, resumo("principal, so cimento Portland", ajusta(port), port))

# ----------------------------------------------------------------
# 6. ci_t (F22). O ci_mpa foi removido do projecto (F23/F24, Kie 2026-10-16).
# ----------------------------------------------------------------
# F22 (Kie, 2026-10-16): ci_t = ci de Damineli / vida util de projecto, kg CO2-eq/(m3.MPa.ano),
# so nos pares com vida util declarada pelo proprio artigo (QD). O vi segue a mesma regra do ci
# (A3/A4): variancia relativa publicada x yi^2, ou hibrido por classe de resistencia.
ct <- subset(princ, !is.na(ci_t))
ct$yi <- ct$ci_t
res <- rbind(res, resumo("ci_t (kg CO2-eq/(m3.MPa.ano)), principal com vida util", ajusta(ct, yi = "ci_t"), ct))
ctci <- ct; ctci$yi <- ctci$ci
res <- rbind(res, resumo("ci no mesmo subconjunto com vida util (comparacao com ci_t)", ajusta(ctci), ctci))

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
