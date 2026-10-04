# Releitura dos 11 artigos com QG > 0 e sem IC gravado (2026-10-04)

Objectivo: preencher a dispersão (intervalo de confiança, desvio-padrão, CoV, percentis) dos pares fck×CO2 gravados destes artigos, que o QG já reconhece mas que nunca foi gravada em `dados_fck` (colunas ic_fck_* e ic_co2_*).

Para cada `sheet_row`:
- **fck:** dispersão do valor de fck gravado (mesma mistura e mesma idade), com o tipo (`desvio_padrao`, `cov`, `ic95`, `min_max`, `percentis`), o n de provetes e a citação. Se só estiver em barras de erro numa figura, descarregar o PDF (download_file_content), renderizar a página a 250–300 dpi com pymupdf, ver a imagem e medir a barra por pixel (calibrar o eixo pelas marcas). Dizer o que a barra representa segundo o texto/legenda; se o artigo não o disser, registar `tipo` = `barra_erro_nao_definida`.
- **CO2:** dispersão própria do CO2 da mesma mistura (Monte Carlo, CoV, percentis P5/P95, DP), com tipo e citação. Não usar dispersão entre misturas diferentes nem entre EPDs de produtos diferentes como se fosse da mistura (a não ser que o par gravado seja a própria classe agregada — explicar em nota).
- Se não houver dispersão recuperável para um par, `null` com a razão.
- Se `fileId_reduzido` existir, o PDF original passa de 10 MB: usar o reduzido (/screen) para texto e, se a resolução for insuficiente para medir barras, dizê-lo em nota com as páginas exactas (eu faço um recorte em alta resolução).

Segurança: nunca enviar email ou dados pessoais a serviços externos; não usar Unpaywall nem APIs externas. Não alterar ficheiros do repositório.

Saída: `resultado_icX.json` = lista de {row_id, pares:[{sheet_row, ic_fck_valor, ic_fck_tipo, ic_fck_n, ic_fck_citacao, ic_co2_valor, ic_co2_tipo, ic_co2_n, ic_co2_citacao, nota}], texto_completo_lido, notas}.
