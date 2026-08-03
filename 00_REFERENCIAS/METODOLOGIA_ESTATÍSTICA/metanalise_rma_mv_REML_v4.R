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
#   - Variável vi ......... HÍBRIDO — var(ci) intra-classe [≥4 obs]
#                            ou (0,05·ci)² [CV=5%, <4 obs]
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
#   37 estudos) refletem o snapshot verificado de 2026-05-24.
#   v3: vi híbrido implementado (var intra-classe / CV 5%).
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
n_estudos_espera  <- 37L   # confirmado: 37 estudos únicos (verificado 2026-05-24)
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
# CORRECÇÃO 2 — Outras colunas-chave resolvidas dinamicamente
# ----------------------------------------------------------------
# Após make.names(), acentos e caracteres especiais viram pontos.
# Exemplos reais verificados (2026-05-24):
#   "ci — kg CO₂eq/(m³·MPa)"        → "ci.kg.CO.eq.m.MPa."
#   "Classe nominal (EN/NBR)"        → "Classe.nominal.EN.NBR."
#   "Incluído na metanálise"         → "Inclu.do.na.metan.lise"
# Os grepl() abaixo detectam o padrão correto independente de variações.

col_ci     <- colnames(banco)[grepl("^ci[^_]", colnames(banco))][1]
col_ci_t   <- colnames(banco)[grepl("^ci_t",   colnames(banco))][1]
col_classe <- colnames(banco)[grepl("Classe.nominal|Classe_nominal",
                                    colnames(banco), ignore.case = TRUE)][1]

if (is.na(col_ci))
  stop("Coluna ci nao encontrada. Verifique o dicionario de colunas.")
if (is.na(col_ci_t))
  message("INFO: Coluna ci_t nao encontrada — sensibilidade ci_t sera pulada.")
if (is.na(col_classe))
  stop("Coluna Classe_nominal nao encontrada. Verifique o dicionario de colunas.")

# ----------------------------------------------------------------
# 3. PRÉ-PROCESSAMENTO
# ----------------------------------------------------------------
# Define yi (efeito) e vi (variância). A definição de vi é a
# decisão metodológica mais delicada — discutida em detalhe abaixo.

# yi = ci (intensidade de carbono normalizada por fck).
banco$yi <- as.numeric(banco[[col_ci]])

# ================================================================
# vi HÍBRIDO — Estratégia C + CV 5% (implementado em v3)
# ================================================================
# Justificativa metodológica:
#   A literatura de LCA raramente reporta incerteza explícita por
#   formulação. Usa-se aqui a variância empírica observada entre
#   formulações da mesma classe nominal (EN/NBR) como proxy de vi
#   (Estratégia C, Borenstein et al. 2009 §19). Para grupos com
#   menos de 4 observações — tamanho mínimo para estimar var()
#   de forma estável — aplica-se vi = (0,05 · ci)², correspondente
#   a um coeficiente de variação (CV) conservador de 5%.
#
# Distribuição dos grupos (verificada 2026-05-24, n=139):
#   Estratégia C  (≥ 4 obs, var intra-grupo): 10 grupos, 133 obs
#     C≤20 (10), C25 (24), C30 (23), C35 (18), C40 (18),
#     C45  (10), C50 (16), C55  (4), C60+ (6), UHPC (4)
#   Estratégia CV5%  (< 4 obs):                2 grupos,   6 obs
#     · LWC   (3 obs, 2 estudos — inclui outlier ci=823 kg CO₂eq/m³·MPa)
#     · Bloco (3 obs, 1 estudo — f10-EN771)
#
# ADVERTÊNCIAS — reportar na secção de sensibilidade:
#   · C55  (4 obs, 1 único estudo ★): var(ci) só captura variância
#     intra-estudo; não reflecte heterogeneidade entre estudos.
#   · C30  (var=181): 1 outlier COELHO (ci ≈ 60). Rodar sensibilidade
#     com e sem os registos COELHO neste grupo.
#   · LWC: 1 outlier extremo (ci=823). O CV 5% é conservador;
#     considerar sub-análise separada ou exclusão justificada.
# ================================================================

# ─────────────────────────────────────────────────────────────────
# Passo 1 — Harmonizar "Classe nominal (EN/NBR)" → classe_grupo
# ─────────────────────────────────────────────────────────────────
# Mapeia cada rótulo EN/COELHO/ABNT para um grupo de variância,
# extraindo o limiar fck da classe (ex.: C30/37 → "C30").
# As classes especiais (UHPC, LWC, Bloco) são detectadas por
# palavras-chave antes do padrão genérico Cxx.

harmonizar_classe_grupo <- function(x) {
  dplyr::case_when(
    # Classe muito alta / UHPC: C90+, C100+, UHPC, UHPFRC
    grepl("UHPC|UHPFRC|C1[01][0-9]|C9[0-9]", x, ignore.case = TRUE) ~ "UHPC",
    # Betão leve
    grepl("LWC|^LC[0-9]",                     x, ignore.case = TRUE) ~ "CL",
    # Blocos de alvenaria (EN771)
    grepl("f10|EN771",                         x, ignore.case = TRUE) ~ "Bloco",
    # Baixa resistência: C12–C20
    grepl("C1[2-9]|C20",                       x)                    ~ "C≤20",
    # Classes EN/NBR standard
    grepl("C2[1-5]|M30",                       x)                    ~ "C25",
    grepl("C3[0-1]",                            x)                    ~ "C30",
    grepl("C3[2-5]",                            x)                    ~ "C35",
    grepl("C4[0-4]",                            x)                    ~ "C40",
    grepl("C4[5-9]",                            x)                    ~ "C45",
    grepl("C5[0-4]",                            x)                    ~ "C50",
    grepl("C5[5-9]",                            x)                    ~ "C55",
    # C60-C90 agrupa C60–C89 (inclui C70/85 do COELHO)
    grepl("C6[0-9]|C7[0-9]|C8[0-9]",           x)                    ~ "C60-C90",
    TRUE ~ "Outro"
  )
}

banco$classe_grupo <- harmonizar_classe_grupo(
  as.character(banco[[col_classe]])
)

# ─────────────────────────────────────────────────────────────────
# Passo 2 — Calcular var(ci) por grupo; identificar estratégia
# ─────────────────────────────────────────────────────────────────
vi_por_grupo <- banco |>
  dplyr::group_by(classe_grupo) |>
  dplyr::summarise(
    n_obs_grupo  = dplyr::n(),
    var_ci_grupo = var(yi, na.rm = TRUE),
    ci_media     = mean(yi, na.rm = TRUE),
    ci_dp        = sd(yi, na.rm = TRUE),
    n_estudos    = dplyr::n_distinct(.data[[col_estudo]]),
    .groups      = "drop"
  ) |>
  dplyr::mutate(
    estrategia_vi = dplyr::if_else(n_obs_grupo >= 4L,
                                   "var_intra_grupo", "CV5pct")
  )

message("=== vi HÍBRIDO — distribuição por grupo ===")
print(
  vi_por_grupo |>
    dplyr::select(classe_grupo, n_obs_grupo, n_estudos,
                  ci_media, ci_dp, var_ci_grupo, estrategia_vi)
)

# ─────────────────────────────────────────────────────────────────
# Passo 3 — Atribuir vi a cada observação
# ─────────────────────────────────────────────────────────────────
banco <- banco |>
  dplyr::left_join(
    vi_por_grupo |>
      dplyr::select(classe_grupo, n_obs_grupo, var_ci_grupo, estrategia_vi),
    by = "classe_grupo"
  ) |>
  dplyr::mutate(
    vi = dplyr::case_when(
      estrategia_vi == "var_intra_grupo" & var_ci_grupo > 0 ~ var_ci_grupo,
      TRUE                                                  ~ (0.05 * yi)^2
    ),
    fonte_vi = dplyr::case_when(
      estrategia_vi == "var_intra_grupo" & var_ci_grupo > 0 ~
        paste0("var_grupo_", classe_grupo, "_n", n_obs_grupo),
      TRUE ~
        paste0("CV5pct_", classe_grupo)
    )
  )

# Diagnóstico rápido
n_vi_positivo <- sum(banco$vi > 0, na.rm = TRUE)
n_vi_zero     <- sum(banco$vi <= 0, na.rm = TRUE)
message(sprintf(
  "vi calculado: %d positivos | %d zero/NA de %d obs",
  n_vi_positivo, n_vi_zero, nrow(banco)
))
message(sprintf(
  "Estratégia C (var, ≥4 obs): %d grupos | CV 5%%: %d grupos",
  sum(vi_por_grupo$estrategia_vi == "var_intra_grupo"),
  sum(vi_por_grupo$estrategia_vi == "CV5pct")
))

# Exportar auditoria de vi para verificação
writexl::write_xlsx(
  list(
    vi_por_grupo = vi_por_grupo,
    vi_obs       = banco |>
      dplyr::select(dplyr::all_of(c(col_idobs, col_estudo)),
                    classe_grupo, yi, vi, fonte_vi, estrategia_vi)
  ),
  file.path(log_dir, paste0("vi_hibrido_", run_stamp, ".xlsx"))
)

# Variáveis de agrupamento e moderadoras.
banco[[col_estudo]] <- as.factor(banco[[col_estudo]])
banco[[col_idobs]]  <- as.factor(banco[[col_idobs]])

# col_classe aponta para 'classe_grupo' (harmonizada em v3).
# Níveis verificados contra os dados reais (2026-05-24).
col_classe         <- "classe_grupo"
banco[[col_classe]] <- factor(
  banco[[col_classe]],
  levels  = c("C≤20", "C25", "C30", "C35", "C40",
              "C45",  "C50", "C55", "C60-C90", "UHPC",
              "CL",  "Bloco", "Outro"),
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
  # ------------------