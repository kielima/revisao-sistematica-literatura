# ================================================================
# Metanálise multinível da intensidade de CO2eq normalizada por fck
# ----------------------------------------------------------------
# Dissertação: Kiê — PUC-Campinas (2026)
# Arquivo: 07_ANALISES DE DADOS / REVISAO SISTEMATICA DE LITERATURA
#          / METODOLOGIA_ESTATISTICA / metanalise_rma_mv_REML.R
#
# Objetivo:
#   Estimar o efeito agregado (mu pooled) da intensidade de emissão
#   de CO2eq por unidade de resistência (ci = kgCO2eq / (m³ * MPa))
#   em concretos sustentáveis, respeitando a estrutura hierárquica
#   dos dados (formulações aninhadas dentro de estudos).
#
# Decisões metodológicas (fechadas pela autora em 2026-05-13):
#   - Modelo .............. metafor::rma.mv (multinível, 3 níveis)
#   - Estimador ........... REML (Restricted Maximum Likelihood)
#   - Estrutura aleatória.. ~ 1 | Estudo / ID_observacao
#   - Variável yi ......... ci  (col J da aba METANÁLISE)
#   - Variável vi ......... TODO — ver bloco 3 (pré-processamento)
#   - Heterogeneidade ..... tau²_1 entre estudos; tau²_2 entre
#                            formulações dentro do mesmo estudo
#
# Dependências (R >= 4.3.0 recomendado):
#   metafor (>= 4.4-0) | readxl | dplyr | tidyr | ggplot2 |
#   here    | writexl  | purrr
#
# Reprodutibilidade:
#   set.seed(20260513)  garante consistência de amostragens
#   (bootstrap, leave-one-out estocástico, etc.).
#
# AVISO:
#   O banco METANÁLISE (BANCO DE DADOS DA RSL.xlsx) ainda NÃO
#   está 100% finalizado. Confirmar inclusão de COELHO e CELIK
#   antes da rodada final. Os números abaixo (139 linhas,
#   69 estudos) refletem o snapshot atualizado de 2026-05-24.
#   (Se o banco usar "estudo único" como unidade, o correcto é
#   37 estudos — ajustar n_estudos_espera conforme verificação.)
# ================================================================


# ----------------------------------------------------------------
# 1. SETUP
# ----------------------------------------------------------------
# Carrega pacotes, instala os que faltarem e fixa a semente.

required_pkgs <- c(
  "metafor",   # rma.mv, forest, funnel, regtest, leave1out
  "readxl",    # leitura de .xlsx
  "dplyr",     # manipulação tabular
  "tidyr",     # pivots e reshape
  "ggplot2",   # gráficos customizados
  "here",      # caminhos relativos à raiz do projeto
  "writexl",   # exportação .xlsx
  "purrr"      # iteração funcional (map, etc.)
)

missing_pkgs <- setdiff(required_pkgs, rownames(installed.packages()))
if (length(missing_pkgs) > 0L) {
  install.packages(missing_pkgs, dependencies = TRUE)
}
invisible(lapply(required_pkgs, library, character.only = TRUE))

# Semente fixa — qualquer simulação a partir daqui é reproduzível.
set.seed(20260513)

# Define caminhos relativos à raiz do projeto (DISSERTAÇÃO/).
# `here::here()` encontra a raiz automaticamente desde que exista
# um arquivo de marcação (.Rproj, .here ou .git) na raiz.
#
# TODO (Kiê): se ainda não houver, criar um arquivo vazio
# chamado ".here" na pasta DISSERTAÇÃO/ para ancorar o here().
base_dir   <- here::here()

# TODO (Kiê): conferir se o .xlsx está exatamente neste caminho.
# Caso esteja em outra subpasta, ajustar a linha abaixo.
input_path <- file.path(
  base_dir,
  "07_ANÁLISES DE DADOS",
  "REVISÃO SISTEMÁTICA DE LITERATURA",
  "BANCO DE DADOS DA RSL.xlsx"
)
sheet_name <- "METANÁLISE"   # caixa alta, com acento

# Pastas de saída — criadas se não existirem.
out_dir <- file.path(
  base_dir,
  "07_ANÁLISES DE DADOS",
  "REVISÃO SISTEMÁTICA DE LITERATURA",
  "METODOLOGIA_ESTATÍSTICA",
  "resultados_metanalise"
)
fig_dir <- file.path(out_dir, "figuras")
tab_dir <- file.path(out_dir, "tabelas")
log_dir <- file.path(out_dir, "logs")
for (d in c(fig_dir, tab_dir, log_dir)) {
  dir.create(d, showWarnings = FALSE, recursive = TRUE)
}

# Stamp de execução — útil para versionar saídas.
run_stamp <- format(Sys.time(), "%Y%m%d_%H%M%S")


# ----------------------------------------------------------------
# 2. LEITURA DO BANCO
# ----------------------------------------------------------------
# Lê a aba METANÁLISE, filtra observações marcadas como incluídas
# e checa expectativas básicas (nº de linhas, nº de estudos).

stopifnot(file.exists(input_path))

banco_bruto <- readxl::read_excel(
  path  = input_path,
  sheet = sheet_name,
  guess_max = 5000      # evita inferência prematura de tipos
)

# Normaliza nomes de colunas (remove espaços/caracteres especiais).
# Mantém um dicionário Bruto->Padrão para rastrear o que mudou.
nomes_originais <- colnames(banco_bruto)
colnames(banco_bruto) <- make.names(colnames(banco_bruto), unique = TRUE)
dicionario_colunas <- data.frame(
  original    = nomes_originais,
  padronizado = colnames(banco_bruto),
  stringsAsFactors = FALSE
)
writexl::write_xlsx(
  dicionario_colunas,
  file.path(log_dir, paste0("dicionario_colunas_", run_stamp, ".xlsx"))
)

# TODO (Kiê): confirmar os nomes EXATOS das seguintes colunas-chave
# após o make.names() — ajustar abaixo se necessário.
col_estudo   <- "Estudo"
# col_idobs: NÃO definir aqui como literal — "ã" quebra após make.names().
# Definição dinâmica inserida logo após a criação do banco (bloco 2, ~linha 170).
col_ci       <- "ci"                   # col J: kgCO2eq/(m³·MPa)
col_ci_t     <- "ci_t"                 # col S: ci / vida_útil
col_fck      <- "fck_nominal"          # MPa (já padronizado)
col_classe   <- "Classe_nominal"       # C25..C60+, UHPC, etc.
col_emissao  <- "Emissao_CO2eq"        # kgCO2eq/m³
col_vu       <- "Vida_util_anos"
col_incluido <- "Incluido"             # TRUE/FALSE
col_pais     <- "Pais"
col_ano      <- "Ano"
col_scm_pct  <- "SCM_pct"              # % de material cimentício suplementar

# Filtro de inclusão.
banco <- banco_bruto |>
  dplyr::filter(.data[[col_incluido]] %in% c(TRUE, "TRUE", "Verdadeiro", 1))

# Checagens básicas — falham cedo se algo bate em ordem de grandeza.
n_obs_esperado    <- 139L
n_estudos_espera  <- 69L   # atualizado; confirmar se 37 (estudos únicos) ou 69 (referências)
n_obs_real        <- nrow(banco)
n_estudos_real    <- dplyr::n_distinct(banco[[col_estudo]])

message(sprintf("Linhas incluídas: %d (esperado: %d)",
                n_obs_real, n_obs_esperado))
message(sprintf("Estudos únicos : %d (esperado: %d)",
                n_estudos_real, n_estudos_espera))

if (n_obs_real != n_obs_esperado) {
  warning("Número de observações difere do esperado — revisar filtros.")
}
if (n_estudos_real != n_estudos_espera) {
  warning("Número de estudos difere do esperado — revisar inclusões.")
}

# ----------------------------------------------------------------
# CORRECÇÃO 1 — col_idobs resolvido dinamicamente após make.names()
# ----------------------------------------------------------------
# make.names() converte "ID_observação" em algo como "ID_observa..o"
# (o "ã" vira caracteres de escape). Usando grepl garantimos que
# col_idobs sempre aponta para a coluna certa, independente de
# acento ou capitalização residual.
col_idobs <- colnames(banco)[grepl("ID_observ", colnames(banco),
                                   ignore.case = TRUE)][1]
if (is.na(col_idobs))
  stop("Coluna 'ID_observ*' nao encontrada no banco. ",
       "Verifique o dicionario de colunas em: ",
       file.path(log_dir, "dicionario_colunas_*.xlsx"))

# ----------------------------------------------------------------
# 3. PRÉ-PROCESSAMENTO
# ----------------------------------------------------------------
# Define yi (efeito) e vi (variância). A definição de vi é a
# decisão metodológica mais delicada — discutida em detalhe abaixo.

# yi = ci (intensidade de carbono normalizada por fck).
banco$yi <- as.numeric(banco[[col_ci]])

# ----------------------------------------------------------------
# TODO (CRÍTICO — vi):
# ----------------------------------------------------------------
# A literatura de LCA de concreto raramente reporta incerteza
# explícita por formulação. As opções são, em ordem decrescente
# de preferência:
#
# (A) VARIÂNCIA EMPÍRICA INTRA-FORMULAÇÃO
#     Quando o estudo reporta múltiplas medições (CP rompidos
#     em diferentes idades, lotes, etc.), calcular:
#         vi = (sd_fck_medido)^2 / n_medicoes
#     Aplicado a um numero limitado de linhas onde o autor
#     publicou desvio-padrão.
#
# (B) DERIVAÇÃO A PARTIR DE IC OU ERRO PROPAGADO
#     Se o autor reporta intervalo de confiança em torno do CO2eq
#     ou do fck, recuperar vi por:
#         vi = ((LS - LI) / (2 * 1.96))^2
#     Lembrando de propagar variâncias para o quociente ci:
#         var(A/B) ≈ (A/B)^2 * (var(A)/A^2 + var(B)/B^2)
#
# (C) IMPUTAÇÃO POR CLASSE NOMINAL (último recurso)
#     Quando nenhuma incerteza é reportada, usar a variância
#     empírica observada entre formulações da mesma classe
#     (C25, C30, ..., UHPC) como proxy. Risco: subestima
#     heterogeneidade real e infla precisão aparente.
#
# RECOMENDAÇÃO TÉCNICA:
#   - Fazer uma coluna nova "fonte_vi" categórica
#     {"empirico", "IC_reportado", "imputado_classe"}.
#   - Rodar análise de sensibilidade tratando vi de cada fonte
#     de forma separada (subset analyses) para checar
#     robustez do mu pooled.
#
# Placeholder enquanto a decisão não está fechada:
# ----------------------------------------------------------------
banco$vi <- NA_real_

# TODO (Kiê): substituir a linha abaixo quando o método de vi
# estiver definido. Sem vi, rma.mv não roda.
if (all(is.na(banco$vi))) {
  warning("vi não calculado — bloco 5 (modelo principal) falhará. ",
          "Revisar TODO da variância em pré-processamento.")
}

# Variáveis de agrupamento e moderadoras.
banco[[col_estudo]] <- as.factor(banco[[col_estudo]])
banco[[col_idobs]]  <- as.factor(banco[[col_idobs]])
banco[[col_classe]] <- factor(
  banco[[col_classe]],
  levels = c("C25", "C30", "C35", "C40", "C45", "C50", "C55",
             "C60+", "UHPC"),
  ordered = FALSE
)


# ----------------------------------------------------------------
# 4. ESTATÍSTICAS DESCRITIVAS
# ----------------------------------------------------------------
# Sumário do banco — base da Tabela 1 da dissertação.

descritivas_geral <- banco |>
  dplyr::summarise(
    n_obs       = dplyr::n(),
    n_estudos   = dplyr::n_distinct(.data[[col_estudo]]),
    ci_media    = mean(yi, na.rm = TRUE),
    ci_mediana  = median(yi, na.rm = TRUE),
    ci_q1       = quantile(yi, 0.25, na.rm = TRUE),
    ci_q3       = quantile(yi, 0.75, na.rm = TRUE),
    ci_min      = min(yi, na.rm = TRUE),
    ci_max      = max(yi, na.rm = TRUE),
    ci_sd       = sd(yi, na.rm = TRUE)
  )

descritivas_por_estudo <- banco |>
  dplyr::group_by(.data[[col_estudo]]) |>
  dplyr::summarise(
    n_formulacoes = dplyr::n(),
    ci_media      = mean(yi, na.rm = TRUE),
    ci_mediana    = median(yi, na.rm = TRUE),
    ci_range      = paste0(round(min(yi, na.rm = TRUE), 3), " – ",
                           round(max(yi, na.rm = TRUE), 3)),
    .groups = "drop"
  )

descritivas_por_classe <- banco |>
  dplyr::group_by(.data[[col_classe]]) |>
  dplyr::summarise(
    n_obs      = dplyr::n(),
    ci_media   = mean(yi, na.rm = TRUE),
    ci_mediana = median(yi, na.rm = TRUE),
    .groups = "drop"
  )

writexl::write_xlsx(
  list(
    geral      = descritivas_geral,
    por_estudo = descritivas_por_estudo,
    por_classe = descritivas_por_classe
  ),
  file.path(tab_dir, paste0("descritivas_", run_stamp, ".xlsx"))
)


# ----------------------------------------------------------------
# 5. MODELO PRINCIPAL (rma.mv 3-níveis com REML)
# ----------------------------------------------------------------
# Notas sobre a estrutura:
#   - nível 1: erro amostral (vi, conhecido)
#   - nível 2: variância entre formulações dentro do mesmo
#              estudo  -> sigma^2.2
#   - nível 3: variância entre estudos                      -> sigma^2.1
#
# A formulação ~ 1 | Estudo / ID_observacao expande para
# random = list(~ 1 | Estudo, ~ 1 | Estudo:ID_observacao),
# que é exatamente a definição multinível de Cheung (2014)
# e Konstantopoulos (2011).
#
# 68% dos estudos e 90% das observações estão em clusters,
# o que justifica o uso de rma.mv ao invés de rma() padrão.

# Roda apenas se vi tiver sido calculado.
modelo_principal <- NULL
if (!all(is.na(banco$vi))) {

  modelo_principal <- metafor::rma.mv(
    yi     = yi,
    V      = vi,
    random = as.formula(paste0("~ 1 | ", col_estudo, "/", col_idobs)),
    data   = banco,
    method = "REML",
    sparse = TRUE,        # acelera em bancos com muitos clusters
    test   = "t",         # ajuste t-de-Student para gl pequenos
    dfs    = "contain"    # Knapp-Hartung-like para multilevel
  )

  print(summary(modelo_principal))

  # I² multilevel — Fórmula: Cheung (2014, Psychological Methods)
  # e Assink & Wibbelink (2016, TQMP) decompõem:
  #   I²_total = (sigma2.1 + sigma2.2) / (sigma2.1 + sigma2.2 + V_tipico)
  # onde V_tipico = (k-1) * sum(1/vi) / (sum(1/vi)^2 - sum(1/vi^2))
  calc_i2_multilevel <- function(m) {
    W <- diag(1 / m$vi)
    X <- model.matrix(m)
    P <- W - W %*% X %*% solve(t(X) %*% W %*% X) %*% t(X) %*% W
    typ_v <- (m$k - m$p) / sum(diag(P))
    total <- sum(m$sigma2)
    i2_total <- 100 * total / (total + typ_v)
    i2_2     <- 100 * m$sigma2[2] / (total + typ_v)  # dentro de estudo
    i2_3     <- 100 * m$sigma2[1] / (total + typ_v)  # entre estudos
    list(
      I2_total              = i2_total,
      I2_dentro_de_estudo   = i2_2,
      I2_entre_estudos      = i2_3,
      V_tipico              = typ_v
    )
  }

  i2_resultado <- calc_i2_multilevel(modelo_principal)
  print(i2_resultado)

  # Salva resultados em txt e em rds (para reuso posterior).
  capture.output(
    summary(modelo_principal),
    i2_resultado,
    file = file.path(log_dir, paste0("modelo_principal_", run_stamp, ".txt"))
  )
  saveRDS(modelo_principal,
          file = file.path(out_dir, paste0("modelo_principal_", run_stamp, ".rds")))
} else {
  message("Modelo principal NÃO foi rodado (vi pendente).")
}


# ----------------------------------------------------------------
# 6. FOREST PLOT
# ----------------------------------------------------------------
# Customização ABNT: fonte serifada, eixos em pt-BR, IC 95%,
# rótulos em ordem de classe + estudo.

if (!is.null(modelo_principal)) {

  # ATENÇÃO: forest() com 70 linhas fica apertado. Sugiro
  # gerar 2 versões: (a) completa para o apêndice da
  # dissertação, e (b) agregada por estudo para o corpo do texto.

  png(
    filename = file.path(fig_dir, paste0("forest_completo_", run_stamp, ".png")),
    width = 2400, height = 3600, res = 300
  )
  metafor::forest(
    modelo_principal,
    slab    = paste(banco[[col_estudo]], banco[[col_idobs]], sep = " – "),
    xlab    = expression("ci  [ kg CO"[2]*"eq / (m³ · MPa) ]"),
    header  = c("Estudo / Formulação", "ci [IC 95%]"),
    cex     = 0.55,
    refline = NA,
    mlab    = "Modelo multinível REML"
  )
  dev.off()

  # Versão PDF (vetorial — preferida para impressão).
  pdf(
    file   = file.path(fig_dir, paste0("forest_completo_", run_stamp, ".pdf")),
    width  = 8, height = 12
  )
  metafor::forest(
    modelo_principal,
    slab    = paste(banco[[col_estudo]], banco[[col_idobs]], sep = " – "),
    xlab    = expression("ci  [ kg CO"[2]*"eq / (m³ · MPa) ]"),
    header  = c("Estudo / Formulação", "ci [IC 95%]"),
    cex     = 0.55,
    refline = NA,
    mlab    = "Modelo multinível REML"
  )
  dev.off()

  # TODO (Kiê): considerar também um forest agregado por
  # estudo (rodando rma() nas médias intra-estudo para fins
  # ilustrativos) — versão "limpa" para o corpo do texto.
}


# ----------------------------------------------------------------
# 7. FUNNEL PLOT + TESTE DE EGGER
# ----------------------------------------------------------------
# Funnel padrão + teste de Egger adaptado para multinível.
# Em rma.mv o regtest() clássico NÃO é diretamente aplicável;
# a alternativa consagrada é incluir sqrt(vi) (ou 1/sqrt(vi))
# como moderador no próprio rma.mv e testar a significância
# desse coeficiente — equivalente à versão multinível do Egger
# (Rodgers & Pustejovsky, 2021).

if (!is.null(modelo_principal)) {

  # Funnel plot.
  png(
    filename = file.path(fig_dir, paste0("funnel_", run_stamp, ".png")),
    width = 1800, height = 1500, res = 300
  )
  metafor::funnel(
    modelo_principal,
    xlab = expression("ci  [ kg CO"[2]*"eq / (m³ · MPa) ]"),
    main = "Funnel plot — modelo multinível"
  )
  dev.off()

  # Egger multinível via meta-regressão.
  egger_ml <- metafor::rma.mv(
    yi     = yi,
    V      = vi,
    mods   = ~ sqrt(vi),
    random = as.formula(paste0("~ 1 | ", col_estudo, "/", col_idobs)),
    data   = banco,
    method = "REML",
    test   = "t",
    dfs    = "contain"
  )
  print(summary(egger_ml))
  capture.output(
    summary(egger_ml),
    file = file.path(log_dir, paste0("egger_multilevel_", run_stamp, ".txt"))
  )
  # TODO (Kiê): interpretar o coeficiente de sqrt(vi) — se p < 0,05,
  # há indício de viés de publicação ou efeito de pequenos estudos.
}


# ----------------------------------------------------------------
# 8. LEAVE-ONE-OUT POR CLUSTER (DIAGNÓSTICO DE ROBUSTEZ)
# ----------------------------------------------------------------
# Remove um estudo de cada vez e re-roda o modelo. Foca em
# estudos com peso alto: CORDOBA (18 obs), DYNAN, BHAGAT,
# SANCHEZ-PANTOJA. Pode estender para todos os 22 estudos.

if (!is.null(modelo_principal)) {

  estudos_chave <- c("CORDOBA", "DYNAN", "BHAGAT", "SANCHEZ-PANTOJA")

  # TODO (Kiê): se quiser fazer leave-one-out completo nos 22
  # estudos, troque a linha abaixo por:
  #   estudos_loop <- levels(banco[[col_estudo]])
  estudos_loop <- intersect(estudos_chave, levels(banco[[col_estudo]]))

  loo_resultados <- purrr::map_dfr(estudos_loop, function(estudo_removido) {
    sub <- banco |>
      dplyr::filter(.data[[col_estudo]] != estudo_removido)

    mod_sub <- tryCatch(
      metafor::rma.mv(
        yi     = yi,
        V      = vi,
        random = as.formula(paste0("~ 1 | ", col_estudo, "/", col_idobs)),
        data   = sub,
        method = "REML",
        test   = "t",
        dfs    = "contain"
      ),
      error = function(e) NULL
    )

    if (is.null(mod_sub)) {
      return(data.frame(
        estudo_removido = estudo_removido,
        n_restante      = nrow(sub),
        mu              = NA_real_,
        ci_lb           = NA_real_,
        ci_ub           = NA_real_,
        sigma2_estudo   = NA_real_,
        sigma2_form     = NA_real_,
        delta_mu_pct    = NA_real_
      ))
    }

    delta_mu_pct <- 100 * (mod_sub$b[1] - modelo_principal$b[1]) /
                          modelo_principal$b[1]

    data.frame(
      estudo_removido = estudo_removido,
      n_restante      = nrow(sub),
      mu              = as.numeric(mod_sub$b[1]),
      ci_lb           = mod_sub$ci.lb,
      ci_ub           = mod_sub$ci.ub,
      sigma2_estudo   = mod_sub$sigma2[1],
      sigma2_form     = mod_sub$sigma2[2],
      delta_mu_pct    = delta_mu_pct
    )
  })

  print(loo_resultados)
  writexl::write_xlsx(
    loo_resultados,
    file.path(tab_dir, paste0("leave_one_out_", run_stamp, ".xlsx"))
  )

  # TODO (Kiê): regra prática — se algum |delta_mu_pct| > 20%,
  # discutir explicitamente a influência desse estudo na seção
  # de robustez da dissertação.
}


# ----------------------------------------------------------------
# 9. ANÁLISE DE SUBGRUPOS POR CLASSE NOMINAL
# ----------------------------------------------------------------
# Sub-meta-análises por classe (C25..C60+, UHPC).
# Algumas classes podem ter n pequeno — colapsar se necessário.

if (!is.null(modelo_principal)) {

  # Conta n por classe — sinaliza onde colapsar.
  contagem_classe <- banco |>
    dplyr::count(.data[[col_classe]], name = "n_obs")
  print(contagem_classe)

  # TODO (Kiê): regra sugerida — classes com n < 5 obs
  # devem ser agrupadas (ex.: "C25–C30" ou "C55–UHPC")
  # ou excluídas da subgroup analysis.
  # Ajustar o vetor `classes_para_rodar` abaixo conforme
  # a contagem real.
  classes_para_rodar <- contagem_classe |>
    dplyr::filter(n_obs >= 5) |>
    dplyr::pull(.data[[col_classe]]) |>
    as.character()

  subgrupo_resultados <- purrr::map_dfr(classes_para_rodar, function(cl) {
    sub <- banco |>
      dplyr::filter(.data[[col_classe]] == cl)

    if (dplyr::n_distinct(sub[[col_estudo]]) < 2) {
      # rma.mv com 1 estudo só -> degenerado; pula.
      return(NULL)
    }

    mod_cl <- tryCatch(
      metafor::rma.mv(
        yi     = yi,
        V      = vi,
        random = as.formula(paste0("~ 1 | ", col_estudo, "/", col_idobs)),
        data   = sub,
        method = "REML",
        test   = "t",
        dfs    = "contain"
      ),
      error = function(e) NULL
    )
    if (is.null(mod_cl)) return(NULL)

    data.frame(
      classe          = cl,
      n_obs           = nrow(sub),
      n_estudos       = dplyr::n_distinct(sub[[col_estudo]]),
      mu              = as.numeric(mod_cl$b[1]),
      ci_lb           = mod_cl$ci.lb,
      ci_ub           = mod_cl$ci.ub,
      sigma2_estudo   = mod_cl$sigma2[1],
      sigma2_form     = mod_cl$sigma2[2]
    )
  })

  print(subgrupo_resultados)
  writexl::write_xlsx(
    subgrupo_resultados,
    file.path(tab_dir, paste0("subgrupos_classe_", run_stamp, ".xlsx"))
  )

  # Forest plot estratificado por classe (ggplot, mais flexível
  # que metafor::forest para múltiplos painéis).
  if (nrow(subgrupo_resultados) > 0) {
    p_sub <- ggplot2::ggplot(
      subgrupo_resultados,
      ggplot2::aes(x = mu, y = reorder(classe, mu))
    ) +
      ggplot2::geom_point(size = 3) +
      ggplot2::geom_errorbarh(
        ggplot2::aes(xmin = ci_lb, xmax = ci_ub), height = 0.2
      ) +
      ggplot2::geom_vline(
        xintercept = as.numeric(modelo_principal$b[1]),
        linetype = "dashed"
      ) +
      ggplot2::labs(
        x = expression("ci  [ kg CO"[2]*"eq / (m³ · MPa) ]"),
        y = "Classe nominal (fck)",
        title = "Efeito agregado por classe nominal",
        subtitle = "Linha tracejada = mu pooled global"
      ) +
      ggplot2::theme_minimal(base_size = 11)

    ggplot2::ggsave(
      file.path(fig_dir, paste0("forest_subgrupos_classe_", run_stamp, ".png")),
      plot = p_sub, width = 8, height = 5, dpi = 300
    )
    ggplot2::ggsave(
      file.path(fig_dir, paste0("forest_subgrupos_classe_", run_stamp, ".pdf")),
      plot = p_sub, width = 8, height = 5
    )
  }
}


# ----------------------------------------------------------------
# 10. ANÁLISE DE SENSIBILIDADE — ci vs ci_t
# ----------------------------------------------------------------
# Compara o modelo principal (yi = ci) com um modelo paralelo
# usando ci_t = ci / vida_util, restrito ao subset com vu
# declarada (≈ 18 obs, conforme estado atual do banco).

if (!is.null(modelo_principal) &&
    col_ci_t %in% colnames(banco) &&
    col_vu  %in% colnames(banco)) {

  sub_vu <- banco |>
    dplyr::filter(!is.na(.data[[col_vu]]) & !is.na(.data[[col_ci_t]]))

  if (nrow(sub_vu) >= 10) {

    sub_vu$yi <- as.numeric(sub_vu[[col_ci_t]])
    # vi para ci_t: aproximar por var(ci)/vu^2 (delta method);
    # como vu é tratado sem incerteza, mantemos vi de ci.
    sub_vu$vi <- as.numeric(banco$vi[match(sub_vu[[col_idobs]],
                                           banco[[col_idobs]])]) /
                 (as.numeric(sub_vu[[col_vu]])^2)

    modelo_ci_t <- metafor::rma.mv(
      yi     = yi,
      V      = vi,
      random = as.formula(paste0("~ 1 | ", col_estudo, "/", col_idobs)),
      data   = sub_vu,
      method = "REML",
      test   = "t",
      dfs    = "contain"
    )
    print(summary(modelo_ci_t))
    capture.output(
      summary(modelo_ci_t),
      file = file.path(log_dir, paste0("modelo_ci_t_", run_stamp, ".txt"))
    )

    # TODO (Kiê): comparar mu(ci_t) vs mu(ci)/vu_mediana — se
    # divergirem, discutir o impacto da vida útil na conclusão
    # de eco-eficiência.
  } else {
    message("Subset com vida útil tem n < 10 — sensibilidade ci_t adiada.")
  }
}


# ----------------------------------------------------------------
# 11. META-REGRESSÃO (OPCIONAL — ROADMAP)
# ----------------------------------------------------------------
# Variáveis candidatas a moderadores:
#   - Classe_nominal (categorica)
#   - SCM_pct        (numérica, % de substituição de cimento)
#   - Pais           (categorica)
#   - Ano            (numérica, tendência temporal)
#
# Comentado por padrão. Descomentar e ajustar conforme decisão
# da Kiê sobre o escopo da dissertação.

if (!is.null(modelo_principal)) {

  # ----------------------------------------------------------------
  # Moderador 1: Classe_nominal (categórica)
  # ----------------------------------------------------------------
  # Testa se a intensidade de carbono varia sistematicamente entre
  # classes de resistência (C25, C30, ..., UHPC).
  # A primeira categoria (C25) será o nível de referência.
  # Interprete os coeficientes como diferenças em relação a C25.
  mod_classe <- tryCatch(
    metafor::rma.mv(
      yi     = yi,
      V      = vi,
      mods   = as.formula(paste0("~ ", col_classe)),
      random = as.formula(paste0("~ 1 | ", col_estudo, "/", col_idobs)),
      data   = banco,
      method = "REML",
      test   = "t",
      dfs    = "contain"
    ),
    error = function(e) {
      message("mod_classe falhou: ", e$message)
      NULL
    }
  )
  if (!is.null(mod_classe)) {
    print(summary(mod_classe))
    capture.output(
      summary(mod_classe),
      file = file.path(log_dir, paste0("mod_classe_", run_stamp, ".txt"))
    )
  }

  # ----------------------------------------------------------------
  # Moderador 2: SCM_pct (contínua — % de material cimentício supl.)
  # ----------------------------------------------------------------
  # Testa se maior substituição de cimento reduz ci.
  # ATENÇÃO: verificar correlação com Classe_nominal antes de
  # incluir ambos no mesmo modelo (possível multicolinearidade —
  # UHPC tende a ter SCM_pct elevado).
  if (col_scm_pct %in% colnames(banco)) {
    mod_scm <- tryCatch(
      metafor::rma.mv(
        yi     = yi,
        V      = vi,
        mods   = as.formula(paste0("~ ", col_scm_pct)),
        random = as.formula(paste0("~ 1 | ", col_estudo, "/", col_idobs)),
        data   = banco,
        method = "REML",
        test   = "t",
        dfs    = "contain"
      ),
      error = function(e) {
        message("mod_scm falhou: ", e$message)
        NULL
      }
    )
    if (!is.null(mod_scm)) {
      print(summary(mod_scm))
      capture.output(
        summary(mod_scm),
        file = file.path(log_dir, paste0("mod_scm_pct_", run_stamp, ".txt"))
      )
    }
  } else {
    message("Coluna '", col_scm_pct, "' nao encontrada no banco — ",
            "mod_scm nao rodado. Verificar make.names() no dicionario.")
  }

  # ----------------------------------------------------------------
  # TODO (Kiê): moderadores adicionais (Pais, Ano, etc.)
  # ----------------------------------------------------------------
  # Para testar Pais ou Ano, duplicar um dos blocos acima e
  # trocar col_scm_pct por col_pais ou col_ano na formula de mods.
  # Se combinar Classe_nominal + SCM_pct num mesmo modelo, rodar
  # VIF (vif(lm(...))) para verificar multicolinearidade antes
  # de interpretar coeficientes individualmente.
}


# ----------------------------------------------------------------
# 12. EXPORT FINAL — TABELAS, GRÁFICOS E LOG DE SESSÃO
# ----------------------------------------------------------------
# Salva sessionInfo para auditoria de versões.

writeLines(
  capture.output(sessionInfo()),
  con = file.path(log_dir, paste0("sessionInfo_", run_stamp, ".txt"))
)

message("\n----------------------------------------------------------------")
message("Metanálise finalizada — saídas em:")
message("  Figuras: ", fig_dir)
message("  Tabelas: ", tab_dir)
message("  Logs:    ", log_dir)
message("----------------------------------------------------------------\n")

# Fim do script.
