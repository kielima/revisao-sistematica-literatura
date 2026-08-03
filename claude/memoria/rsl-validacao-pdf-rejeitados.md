---
name: rsl-validacao-pdf-rejeitados
description: "Na triagem da RSL, todo artigo rejeitado deve ter nota explícita de validação do PDF nos comments"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: fb2a5077-0c97-4017-a789-3068eea0b954
---

Na triagem por PDF da RSL, **todo artigo que receber P:Rejeitado** (em qualquer critério C2–C8) deve ter, na coluna `comments`, uma nota de validação explícita registrando **como o texto foi extraído e se veio corrompido**, p.ex.:
`[Validação PDF AAAA-MM-DD: pdfplumber p.1; extração OK; sobrenome conferido no texto]`
ou, quando a extração falha/vem corrompida:
`[Validação PDF ...: extração corrompida; decisão por metadados/keyword <qual>; título conferido]`
ou, falso-negativo por caractere (ø, acento quebrado): registrar o motivo e que o título foi conferido manualmente.

**Why:** a Kiê quer rastreabilidade — saber que cada exclusão foi baseada no PDF certo e como o texto foi lido (o método extrai TEXTO via pdfplumber, não render visual; extrações corrompidas dão falso-negativo no match de sobrenome).

**How to apply:** ao rejeitar, acrescentar a nota de validação ao `comments` (separada por ` | `). Método padrão: abrir o PDF, extrair p.1 com pdfplumber, conferir que o sobrenome do arquivo aparece no texto (flag match) e ler o título. Caracteres como ø (Kløverpris) e acentos quebrados (Guzm´an) causam falso-negativo no match → confirmar pelo título. Ver [[rsl-criterios-verbatim]] e [[kie-downloads-baixados-manualmente]].
