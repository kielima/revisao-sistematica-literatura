---
name: rsl-links-capes
description: "Ao mandar links de download de artigos da RSL, SEMPRE no formato proxy CAPES (host reescrito + ezNNN), nunca link direto do editor"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 765c97a3-90ca-4417-87d0-42553152c8a7
---

Quando a Kiê precisa baixar um PDF de artigo (RSL), Claude deve **sempre** fornecer o link no **formato proxy CAPES**, não o link direto do editor. Ela já reclamou disso 2+ vezes ("o link está sem o link capes como foi pedido... de novo").

**Why:** sem o proxy CAPES, os editores (Springer, Elsevier, ACS, RSC, etc.) bloqueiam o acesso pago. Unpaywall pode marcar `is_oa=true` (bronze) incorretamente para artigos que na prática estão atrás de paywall — não confiar; dar o link CAPES.

**How to apply — formato:** reescrever o host (pontos→hífens) + sufixo `.ezNNN.periodicos.capes.gov.br`, usando a **página do artigo** (não `content/pdf`), pois é a página que renderiza o botão "Download PDF / Access provided by CAPES". O número `ezNNN` é atribuído por sessão (atual: **ez128**; confirmar com a Kiê se mudar).
- Springer/Nature: `https://link-springer-com.ez128.periodicos.capes.gov.br/article/{DOI}`
- Elsevier/ScienceDirect: `https://www-sciencedirect-com.ez128.periodicos.capes.gov.br/science/article/pii/{PII}`
- ACS: `https://pubs-acs-org.ez128.periodicos.capes.gov.br/doi/{DOI}` (pode dar 404 — então buscar pelo DOI no Portal CAPES)
- RSC: `https://pubs-rsc-org.ez128.periodicos.capes.gov.br/en/content/articlelanding/{ano}/{cc}/{doi-suffix}`

Sempre que houver, oferecer também a cópia OA de repositório (PMC, Zenodo, handle institucional) como alternativa livre — essas abrem sem proxy. Ver [[kie-downloads-baixados-manualmente]] e [[rsl-pdf-ilegivel]].
