# ================================================================
# #1454 (agente RSL, 2026-11-25; POR CONFIRMAR pela Kie): base de medicao
# do fck (cilindro / cubo / prisma) como ANALISE DE SENSIBILIDADE e
# moderador do ci. Nada e convertido (a Kie decidiu em 12/09 nao
# normalizar por factor; a razao cilindro/cubo do UHPC diverge da do
# betao convencional). Mesmo vi e mesmo ajuste do painel/v5
# (funcoes_modelo.R), estrato principal, sem desconto (A7 + F9).
#
# Entrada: dados_metanalise.csv (preparar_dados.py) +
#          resultados/corpo_prova_por_par.csv (exportar_corpo_prova.py).
# Saida:   resultados/sensibilidade_corpo_prova.csv e _moderador.csv
# Uso:     Rscript metanalise/sensibilidade_corpo_prova.R  (raiz do repo)
# ================================================================
suppressPackageStartupMessages({ library(metafor); library(dplyr) })
source("metanalise/funcoes_modelo.R")

d  <- read.csv("metanalise/dados_metanalise.csv", stringsAsFactors = FALSE)
cp <- read.csv("metanalise/resultados/corpo_prova_por_par.csv", stringsAsFactors = FALSE)
d  <- left_join(d, cp[, c("obs_id", "base_fck")], by = "obs_id")
d  <- prepara_base(d)
d$yi <- d$ci

princ <- subset(d, estrato == "principal" & sem_bruto == 0)

cenarios <- list(
  "principal, todos os pares (referencia)" = princ,
  "principal, so cilindro"                 = subset(princ, base_fck == "cilindro"),
  "principal, so cubo"                     = subset(princ, base_fck == "cubo"),
  "principal, so prisma"                   = subset(princ, base_fck == "prisma"),
  "principal, formato declarado (cil+cubo+prisma)" =
    subset(princ, base_fck %in% c("cilindro", "cubo", "prisma")),
  "principal, sem formato escrito (indeterminado/outro/misto)" =
    subset(princ, !base_fck %in% c("cilindro", "cubo", "prisma"))
)

res <- do.call(rbind, lapply(names(cenarios), function(n) {
  dd <- cenarios[[n]]
  message(sprintf("%s: k=%d", n, nrow(dd)))
  resumo(n, ajusta(dd), dd)
}))

# Moderador: cubo e prisma vs cilindro, so pares com formato declarado
dm <- subset(princ, base_fck %in% c("cilindro", "cubo", "prisma"))
dm$cubo   <- as.integer(dm$base_fck == "cubo")
dm$prisma <- as.integer(dm$base_fck == "prisma")
mm <- ajusta(dm, mods = "cubo + prisma")
mod <- data.frame(analise = c("cubo vs cilindro", "prisma vs cilindro"),
                  coef = as.numeric(mm$b[2:3]), ic95_inf = mm$ci.lb[2:3],
                  ic95_sup = mm$ci.ub[2:3], pval = mm$pval[2:3], k = mm$k)

write.csv(res, "metanalise/resultados/sensibilidade_corpo_prova.csv", row.names = FALSE)
write.csv(mod, "metanalise/resultados/sensibilidade_corpo_prova_moderador.csv", row.names = FALSE)
print(res[, c("analise", "k", "estudos", "mu", "ic95_inf", "ic95_sup")])
print(mod)
