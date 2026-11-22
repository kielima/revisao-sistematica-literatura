# ================================================================
# F57 (Kie, 2026-11-22; tarefa #1969): o transporte das materias-primas
# NAO vira 8.o criterio de qualidade (QH) — fica como ANALISE DE
# SENSIBILIDADE. Este script ajusta o ci do estrato principal (sem
# desconto, F9) so com os pares cujo CO2 gravado inclui o transporte das
# materias-primas (A2 = `incluido`, dados_fck col 62 `transporte_materiais`,
# rastreio F37) e compara com o resultado geral.
#
# Entrada: dados_metanalise.csv (preparar_dados.py) + a col 62 lida do
# meta_analysis_base.xlsx por obs_id (= linha da folha dados_fck), passada
# num CSV `obs_id,a2` (gerado por exportar_a2.py).
# Saida: resultados/sensibilidade_a2.csv
# Uso: Rscript metanalise/sensibilidade_a2.R  (a partir da raiz do repositorio)
# ================================================================
suppressPackageStartupMessages({ library(metafor); library(dplyr) })
source("metanalise/funcoes_modelo.R")

d <- read.csv("metanalise/dados_metanalise.csv", stringsAsFactors = FALSE)
a2 <- read.csv("metanalise/resultados/a2_por_par.csv", stringsAsFactors = FALSE)
d <- left_join(d, a2[, c("obs_id", "a2")], by = "obs_id")
d <- prepara_base(d)
d$yi <- d$ci

princ <- subset(d, estrato == "principal" & sem_bruto == 0)   # A7 + F9

cenarios <- list(
  "principal, todos os pares (referencia)"            = princ,
  "principal, A2 incluido (F57)"                      = subset(princ, a2 == "incluido"),
  "principal, A2 incluido ou parcial (F57, extra)"    = subset(princ, a2 %in% c("incluido", "parcial")),
  "principal, A2 nao incluido (excluido/parcial/nao_declarado)" = subset(princ, a2 != "incluido")
)

res <- do.call(rbind, lapply(names(cenarios), function(n) {
  dd <- cenarios[[n]]
  message(sprintf("%s: k=%d", n, nrow(dd)))
  resumo(n, ajusta(dd), dd)
}))

# Diferenca por moderador (A2 incluido vs resto), no estrato principal
princ$a2_incl <- as.integer(princ$a2 == "incluido")
mm <- ajusta(princ, mods = "a2_incl")
mod <- data.frame(analise = "moderador A2 incluido (vs resto), principal",
                  coef = as.numeric(mm$b[2]), ic95_inf = mm$ci.lb[2], ic95_sup = mm$ci.ub[2],
                  pval = mm$pval[2], k = mm$k)

write.csv(res, "metanalise/resultados/sensibilidade_a2.csv", row.names = FALSE)
write.csv(mod, "metanalise/resultados/sensibilidade_a2_moderador.csv", row.names = FALSE)
print(res[, c("analise", "k", "estudos", "mu", "ic95_inf", "ic95_sup")])
print(mod)
