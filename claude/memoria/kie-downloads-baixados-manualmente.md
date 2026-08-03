---
name: kie-downloads-baixados-manualmente
description: Kiê sempre baixa PDFs para a pasta BAIXADOS MANUALMENTE; Claude integra de lá
metadata: 
  node_type: memory
  type: feedback
  originSessionId: fb2a5077-0c97-4017-a789-3068eea0b954
---

Na RSL, a Kiê **sempre** salva os PDFs que baixa manualmente (via proxy CAPES) na pasta `00_REFERENCIAS/ARTIGOS ACEITOS APÓS REMOÇÃO DAS DUPLICATAS/BAIXADOS MANUALMENTE/` — nunca em outro lugar.

**Why:** ela já reforçou isso várias vezes; instruí-la a salvar direto na pasta de destino a irrita e contradiz o fluxo dela.

**How to apply:** ao pedir um download, dizer apenas o nome do arquivo, não a pasta de destino. Depois que ela confirmar o download, Claude localiza o PDF em `BAIXADOS MANUALMENTE/`, verifica `%PDF` + título/autor, renomeia para o padrão ABNT e **move** para `ARTIGOS ACEITOS APÓS REMOÇÃO DAS DUPLICATAS/`, atualizando a coluna `pdf` no `articles_final.xlsx`. Ver fluxo de integração no CLAUDE.md. Nunca apagar arquivos de BAIXADOS MANUALMENTE.
