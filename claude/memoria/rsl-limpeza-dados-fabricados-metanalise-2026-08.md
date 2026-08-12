---
name: rsl-limpeza-dados-fabricados-metanalise-2026-08
description: "meta_analysis_base.xlsx (aba dados_fck) tinha 233 linhas com DOI inexistente ou DOI real de artigo completamente sem relação (71 delas com fck/CO2/durabilidade inventados) -- removidas em 2026-08-14 após verificação via Crossref. Sempre verificar DOI real (curl -s -w '%{http_code}' https://api.crossref.org/works/<doi>) antes de confiar em linha com dado numérico preenchido nesta planilha."
metadata:
  node_type: memory
  type: project
  originSessionId: fb2a5077-0c97-4017-a789-3068eea0b954
---

**Contexto (2026-08-14):** ao processar o lote de confirmação C1-C8 por PDF, uma linha de `meta_analysis_base.xlsx` (row_id=2586, artigo Backes et al.) tinha título/DOI de um artigo completamente diferente. Investigação ampliada revelou que isso não era isolado: **670 das 1.794 linhas (37%)** da aba `dados_fck` tinham `titulo` que não batia com o `row_id` referenciado em `articles_final.xlsx`.

## Diagnóstico (verificado via Crossref, não por suposição)

Rodado `curl -s -w '\n__HTTPSTATUS__%{http_code}' https://api.crossref.org/works/<doi>` para as 312 linhas com DOI em formato válido (`10.xxxx/...`):

| Categoria | Linhas | Status |
|---|---|---|
| Sem DOI / literalmente `"pending"` | 358 | Fila de candidatos/pendências — mantido, é legítimo |
| DOI real, tema bate (título abreviado tipo "LI 2024b — MSWI ash micro-powder in concrete") | 79 | Legítimo — mantido (são fontes externas citadas em revisões, confirmado pela Kiê) |
| **DOI não existe no Crossref (404)** | 83 | **Fabricado — removido** |
| **DOI real, mas aponta pra artigo sem NENHUMA relação com o tema** (ex.: DOI rotulado "Biochar-concrete: A comprehensive review" era na real um artigo sobre asfalto poroso com fibra de aramida) | 150 | **Fabricado — removido** |

Total removido: **233 linhas** (das quais 71 tinham valores numéricos de fck/CO2/durabilidade preenchidos — dados inventados, não apenas metadado bibliográfico errado). Aprovado pela Kiê em 2026-08-14 antes da exclusão.

**Origem provável:** não determinada com certeza (nem a Kiê lembrava). Padrão sugere geração sem verificação real contra PDF/Crossref em algum passe anterior — DOIs no formato correto do editor mas nunca conferidos.

## Regra para o futuro

- **Nunca confiar num DOI de `dados_fck` sem verificar.** Antes de usar/citar um dado numérico dessa planilha (especialmente linhas com título abreviado tipo "SOBRENOME AAAA — assunto"), rodar a verificação Crossref e conferir se o título retornado bate com o `material`/`titulo` registrado.
- Comando de verificação rápida: `curl -s -w '\n%{http_code}' "https://api.crossref.org/works/<DOI>"` — status 404 = DOI não existe; status 200 mas título sem relação = mismatch.
- Linhas com `doi="pending"` ou vazio são candidatos legítimos aguardando resolução — não são fabricação, só ainda não foram checados. Não apagar essas sem investigar individualmente.
- Ao adicionar novas linhas a `dados_fck` (extração PDF-por-PDF em andamento, tarefa #7), sempre preencher `fonte_no_pdf` com citação/trecho literal do PDF real lido — nunca preencher `co2_valor`/`fck_mpa` sem ter o PDF aberto e conferido.

Ver [[rsl-marcacao-R-vs-P]], [[rsl-c2-material-incidental-e-revisoes-sem-dados]].
