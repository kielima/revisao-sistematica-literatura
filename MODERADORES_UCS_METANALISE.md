---
titulo: Moderadores para agregação de UCS e fck na metanálise
descricao: Justificação metodológica da inclusão de materiais geotécnicos e de terra medidos por UCS, e lista dos moderadores que têm de ser registados para explicar a heterogeneidade do grupo em vez de a esconder.
tags: [academico-e-pesquisa, meta-analise, metodologia, revisao-sistematica]
status: revisado
ultima_atualizacao: 2026-08-13
---

# Moderadores para agregação de UCS e fck na metanálise

> **Decisão da Kiê, 2026-08-13.** Materiais geotécnicos e de terra cuja resistência é reportada em **UCS** deixam de ser excluídos da RSL. Passam a entrar, com a resistência registada tal como publicada, e a heterogeneidade que introduzem é tratada por **moderadores na análise**, não por exclusão na triagem.
>
> Esta decisão anula a varredura `M:Rejeitado` de 2026-06-22 nas linhas geotécnicas e de terra. Ver o registo linha a linha no fim deste ficheiro.

---

## 1. Porque é legítimo agregar

O UCS (*Unconfined Compressive Strength*, resistência à compressão simples, símbolo `qu` em mecânica dos solos) e o `fc` do concreto **não são grandezas diferentes**. São o mesmo ensaio, com a mesma condição de contorno:

| | UCS (solo / solo-cimento / terra) | fc (concreto) |
|---|---|---|
| Confinamento | `σ₃ = 0` | `σ₃ = 0` — **igual** |
| Grandeza | força ÷ área → kPa ou MPa | força ÷ área → MPa — **igual** |
| Esbeltez do corpo de prova | h/d = 2 (38×76, 50×100, 100×200 mm) | h/d = 2 (100×200, 150×300 mm) — **igual em proporção** |
| Moldagem | compactação na humidade óptima (energia Proctor) | adensamento por vibração ou haste |
| Idade típica | 7 dias, também 28 | 28 dias |
| Modo de carregamento | deformação controlada (≈1 %/min) | tensão controlada (0,45 ± 0,15 MPa/s) |
| Área usada no cálculo | **corrigida** pela deformação axial, `A_c = A₀/(1−ε)` | **inicial**, `A₀` |
| Normas | ASTM D2166, ASTM D1633, NBR 12025 | NBR 5739, EN 12390-3 |

A esbeltez ser a mesma é o ponto decisivo: é h/d que governa o efeito de atrito nos pratos da prensa e a forma do cone de ruptura, e é por isso que existem factores de correcção para h/d ≠ 2. Com h/d igual, esse factor não é necessário e **não há conversão a fazer** — o número já está na unidade certa.

O que existem são **diferenças de protocolo**, todas conhecidas e todas direccionais. Não invalidam a agregação; obrigam a registá-las.

## 2. Vieses conhecidos e a sua direcção

- **Área corrigida.** `A_c` é sempre maior do que `A₀`, logo o UCS calculado é **sistematicamente mais conservador** do que seria pela convenção do concreto. Em materiais rígidos (solo-cimento, taipa estabilizada) a deformação na ruptura é pequena e o efeito também, mas é sempre no mesmo sentido — subestima.
- **Idade.** Muito ensaio geotécnico é a 7 dias. Comparar 7 dias com 28 dias sem registar a idade subestima o material geotécnico.
- **Velocidade de carregamento.** Deformação controlada versus tensão controlada altera o valor em poucos por cento, geralmente para menos no ensaio mais lento.
- **Média versus característico.** Formalmente `fck` é o quantil de 5 % (`fck = fcm − 1,645·σ`, ou a aproximação `fcm − 8 MPa` do Eurocódigo 2) e `fcm` é a média. Na prática, a esmagadora maioria dos artigos experimentais reporta a **média de três corpos de prova** e chama-lhe `fc` ou `fck`. O UCS reportado também é média. **Incluir UCS não introduz um viés novo neste eixo — introduz o mesmo que a base já tem.** O que é preciso é registar qual dos dois é, sempre que o artigo o diga.

## 3. Moderadores a registar

Estes campos são o que permite, na análise, decidir se se agrega, se se estratifica ou se se corre sensibilidade. Sem eles a heterogeneidade aparece no modelo mas não se consegue atribuir a nada.

| Moderador | Valores | Porquê |
|---|---|---|
| `metrica_resistencia` | `fck` \| `fcm` \| `UCS` \| `outro` | eixo principal da estratificação |
| `classe_material` | `concreto estrutural` \| `solo-cimento` \| `solo estabilizado` \| `backfill` \| `terra crua (taipa/adobe)` \| `argamassa` \| `outro` | separa populações com ordens de grandeza distintas (0,5–5 MPa vs 20–50+ MPa) |
| `norma_ensaio` | NBR 5739, EN 12390-3, ASTM D2166, ASTM D1633, NBR 12025… | captura protocolo inteiro num só campo |
| `geometria_cp` | ex. `cilindro 50×100`, `cilindro 150×300`, `cubo 100`, `prisma` | h/d e efeito de escala |
| `area_no_calculo` | `inicial` \| `corrigida` \| `nao informado` | viés direccional da secção 2 |
| `idade_dias` | inteiro | **já existe** na base |
| `tipo_estatistico` | `media` \| `caracteristico` \| `valor unico` \| `nao informado` | evita comparar quantil de 5 % com média |
| `n_corpos` | inteiro | precisão do estimador |
| `desvio_padrao` | MPa | única via de converter média em característico quando for preciso |
| `modo_carregamento` | `tensao controlada` \| `deformacao controlada` \| `nao informado` | |
| `moldagem` | `vibracao/adensamento` \| `compactacao Proctor` \| `prensagem` \| `outro` | |
| `cura` | `camara humida` \| `imersao` \| `ao ar` \| `selada` \| `nao informado` | |
| `teor_aglomerante` | % em massa | dose de ligante é o preditor mais forte dentro do grupo geotécnico |
| `funcao_estrutural` | `elemento portante` \| `camada de pavimento` \| `preenchimento` \| `parede monolitica` | liga a resistência ao uso real |

**Regra de preenchimento:** campo não informado no artigo escreve-se `nao informado`, nunca se deixa em branco e nunca se presume. Um campo em branco é ambíguo — não se distingue "o artigo não diz" de "ainda não foi extraído".

## 4. Como usar na análise

- **Modelo de efeitos aleatórios**, que já é o adoptado no vault (ver `Justificativa_Modelo_Efeitos_Aleatorios`). A inclusão do grupo UCS reforça a justificação: as populações são reconhecidamente distintas, portanto o efeito verdadeiro não é único.
- **Análise por subgrupo** com `classe_material` e `metrica_resistencia`. Reportar `τ²` e `I²` **por subgrupo**, não só global — um `I²` global alto deixa de ser informativo quando se sabe que há duas populações dentro.
- **Meta-regressão** com `idade_dias`, `teor_aglomerante` e `classe_material` como covariáveis, quando o número de estudos por célula o permitir.
- **Análise de sensibilidade** repetindo o modelo sem o grupo UCS. Se a conclusão não muda, a inclusão está justificada e é ganho de potência; se muda, a mudança é em si um resultado a reportar.
- **No PRISMA e na redacção:** declarar explicitamente que o critério de inclusão é a resistência à compressão uniaxial em unidade de tensão, e não a designação `fck`. Isso torna a decisão auditável por quem ler a dissertação.

## 5. Linhas afectadas pela decisão de 2026-08-13

`M:Rejeitado` anulado; `status_triagem` reposto (`Inconclusivo`, ou `Elegível` quando o C2 já tinha `P:Aceito`):

| Linha | Material | Aplicação |
|---|---|---|
| 2655 | cimentício OPC/SAC/AAC | preenchimento de cavas mineiras |
| 2728 | geopolímero one-part | estabilização de argila mole |
| 2746 | cimento + GGBFS + gesso fosfático | solidificação de lodo dragado |
| 3120 | terra compactada com SCMs | construção em terra |
| 3149 | agregados leves álcali-ativados | rejeitos de mina + cinza volante F |
| 3159 | taipa estabilizada com fibras naturais | construção em terra |
| 3169 | RCD estabilizado com cal/cimento/escória | sub-base de pavimento |
| 3220 | estabilizador álcali-ativado (GFRP + escória) | estabilização de solo argiloso |
| 3516 | MgO + GGBFS | estabilização de rejeitos de mina |
| 3522 | álcali-ativado de rejeitos de mina | aglomerante geotécnico |
| 3597 | escória de cobre | *cemented paste backfill* |
| 3997 | solo expansivo + cal / geogrid | estabilização de talude |
| 4415 | solo-cimento (*deep mixing*) | estabilização geotécnica |

**Casos de fronteira, deliberadamente não incluídos** — aguardam decisão própria porque colidem com regras já documentadas:

- **3311 e 3431** — solidificação/estabilização de resíduos perigosos para aterro. A regra C4 de 2026-06-14 rejeita explicitamente o cimento usado só para imobilizar resíduo com vista a descarte. A decisão do UCS não anula essa regra por si só.
- **4243** — materiais substitutos para cobertura de aterro sanitário; mesma família.
- **4261 e 4271** — revisões sobre estabilização de solo argiloso; têm `C2 = R:Rejeitado`, portanto incluí-las exigiria reverter uma decisão de triagem por resumo, não apenas remover o `M:`.

---

## Manutenção

Registar aqui qualquer novo moderador que a extração revele ser necessário, e manter sincronizado com a secção 7.2 do `CRITERIOS_E_NUANCES_RSL.md`.
