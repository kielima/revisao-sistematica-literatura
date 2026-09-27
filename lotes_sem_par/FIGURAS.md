# Ronda de figuras (PDFs reduzidos com /screen)
Cada ficheiro TMP e uma copia comprimida do PDF original. Descarrega com download_file_content (um de cada vez), renderiza as paginas a 200-300 dpi e VE as figuras/tabelas indicadas. O resultado anterior de cada artigo esta em resultado_lote_XX.json (procura pelo row_id) — le-o primeiro.

| row_id | fileId TMP | lote | o que ver |
|---|---|---|---|
| 3105 ABDEL-GAWWAD | 1NAAdz6OaVryEt_5EqiUwe04JE_aaqMi_ | 05 | Fig.15 (resistencias das 11 misturas) e Fig.21 (CO2-eq por m3 das 11 misturas) |
| 2895 SIRICO | 1__WJu9tEr_gbrXGK70WmumrHtuOCPHbc | 04 | Fig.10 (fck 28 d em cubo, eixo 0-80 MPa) para V0, V10, V15, V20 (linhas 786-789) |
| 3120 NARAYANASWAMY | 1d6pd-q5pGfDGj5820btDpAAYaJX6D3gL | 06 | Fig.10 (CO2 por m2 ou por metro linear? confirmar os 4 valores 42,5/..., o rotulo do eixo) |
| 3153 KANAGARAJ | 1xxPvNNmI9Jiq0W5sSFV0ODyiqLY19lBs | 06 | Fig.25 (CO2 da mistura FG; unidade do eixo) |
| 3238 PYO | 1khhkrAA5426EMkNidSG0c5lOyPM-JWv_ | 08 | Fig.9 (resistencia AcLM50) — confirmar ~36,7 MPa |
| 3133 KROMOSER | 1hIjPAt0wmn4ib2zZYh_3FsXCCPrihSFW | 06 | Fig.7b e Fig.10 (parte estrutural do CO2 da parede; espessura/volume) |
| 3420 BERTIN | 1JBqq5hLGGSRvRh2zGoNHCsNbpjSaYxqI | 11 | Fig.7, 8, 12 (CO2 absoluto do portico de 0,44 m3, C60/75?) |
| 4033 TIAN | 1qf0RvQbf-mZGF93A8fDBMhtxJ1dlK0tu | 16 | Fig.16 (GWP; unidade/UF) e Fig.4 |
| 3439 JONES | 1Dz-h2Fef0Kvp3J6_Xsk3vAPRbCt_qLNL | 11 | Fig.7 (GWP de 1 m3 de cada betao: 35 MPa, 78 MPa, 3D) e Fig.6 |
| 3203 VACLAVIK | 1KHZ2J23U2hXL-t_OoLMk0LpQ5aebtXWH | 07 | Figs.7, 8, 10 (fck de cada uma das 16 misturas x escoria fina/grossa) |
| 3176 IRSHIDAT | 1r5ZEWkGrPYeafChjgkA6yTqKA-3-xSoC | 07 | Fig.16a (CO2 por m3, eixo 165-195) das 13 misturas |

Regras: le valores so de eixos com escala numerica (mede por pixel e calibra com 2 marcas do eixo); regista a leitura e a incerteza; se a resolucao nao permitir ler, diz. Nunca inventes. Nao envies dados pessoais a servicos externos; nao consultes servicos externos.
Saida: resultado_figuras.json na pasta sempar/ com, por row_id: {row_id, figuras_vistas, leituras:[{mistura, fck_mpa?, co2_kg_m3?, unidade_eixo, local, incerteza}], veredicto_final (PAR_CONVERTIVEL/PAR_NAO_CONVERTIVEL/SEM_FCK/SEM_CO2), notas}. Guarda as imagens em sempar/lfig/.
