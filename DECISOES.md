# Decisões (o Nei escolhe)

**Revisão completa em 10–12/10/2026:** V1–V10, D1–D6 e L1–L5 fechadas. Só L1 aguarda o arquivo do logo. O que mudou em relação ao antes está em `HISTORICO.md`; o que falta aplicar nas skills e motores entra nas etapas 2 (vídeo) e 3 (páginas).

As fontes divergem nos pontos abaixo. O kit NÃO escolheu nenhum lado. Quando decidir, escreva a escolha na linha e atualize `DESIGN.md` / `video/style.md`. O valor antigo vai para `HISTORICO.md`.

## Visual
| # | Conflito | Lado A | Lado B | Decisão |
|---|---|---|---|---|
| V1 | Cor primária "âmbar" | Guia: âmbar `#E2A23B` (template.html:21) | Curso v2: amarelo `#FACC15` (SKILL:201) | **B — amarelo `#FACC15`** em toda página nova (guia e curso). Os publicados até 10/10/2026 ficam como estão. Motivo: lê melhor no escuro (~12:1 contra ~8:1) e o portal nunca foi âmbar (é ciano `#00d9ff`). Banners seguem com dourado metálico. (Nei, 10/10/2026) |
| V2 | Fundo escuro de base | Guia `#0c0c10` | v2 `#111827` · v5 `#0E0D14` · v6 escuro `#15141B` | **A — preto neutro `#0c0c10`** em toda página nova (guia, v2, v5, v6 escuro), com cartão `#16161e` e borda `#272730` do guia. Publicados ficam. Portal (`#0a0e27`) fora: é outro site. (Nei, 10/10/2026) |
| V3 | Acento dos cursos | v5/v6: menta/verde (`#7CE0C6`, `#0E6B55`) | guia/v2: âmbar/amarelo | **Amarelo em todo curso novo** (v5 incluído). Em fundo claro o amarelo é só preenchimento (botão, marca-texto, caixa), letra escura, link `#854d0e`. Verde fica só como estado "certo". Regra no núcleo do DESIGN.md. (Nei, 10/10/2026) |
| V4 | Fonte de título | Guia: Sora | v2: Inter · v5/v6: Newsreader (serif) | **A — Sora** no título de toda página nova; corpo Inter. (Nei, 10/10/2026) |
| V5 | Fonte condensada | Banner proíbe (gerar-banner.sh:55,74) | Thumb "manchete" pede sans condensada (thumbviral/estilos.py:5) | **A — thumb é exceção**: condensada pode na thumb, banner continua proibindo. (Nei, 10/10/2026) |
| V6 | Azul no banner | Memória: sem neon azul (feedback_banner_estilo_live:16) | `gerar-banner.sh:40` default "ícone 3D azul-ciano"; estilo `opus` fundo azul (:88) | **A — manter**: azul só no estilo `opus`, opcional, só quando pedido; live/grade sem azul (já é assim no script). (Nei, 10/10/2026) |
| V7 | Âmbar nos vídeos | `#F5A623` (legenda reel) | `#ffd23f` (finviral, eventos, cardshorts) · `#E2A23B`/`#f0e805` (docflow) | **A — `#FACC15` em todo vídeo novo**, legenda com contorno preto; troca no código dos motores na etapa 2. (Nei, 10/10/2026) **Aplicado 13/10** ("para todos"): cardshorts 27c43b1, docflow f4f7525 (motores), eventosextremospub 722e2d4 (motor/mapa.html), makeshorts 52eb799 (spec-visual), finviral d9b6f8f (palco + gerar_cena), skill reel-edita-inema (sem git). **Pendente:** explicavideos v2 (`v2.css`, `viral.css`, `v2.js`, `build_block.py`) — outra sessão com o mesmo arquivo aberto em 13/10; depois disso, sincronizar a cópia `finviral/motor/v2/`; e `docflow.py:252` (sujo de outra sessão). Edições já publicadas (`edicoes/*`) e guias não mudam. |
| V8 | Dosagem de dourado no banner | "Contido, dourado só como acento" (SKILL landing :298) | "Luz âmbar-laranja de palco, cor viva" (gerar-banner.sh:54) | **Os dois valem, cada um numa parte**: letras contidas (branco + uma palavra dourada), cena com luz quente viva; nunca tudo dourado nem cinza. Alinhar a frase da skill na etapa 3. (Nei, 10/10/2026) |
| V9 | Hero do guia | Capa `split` (SKILL :221) | Banner 16:9 na hero, capa só reserva (SKILL :252) | **Não era conflito**: `split` é o layout da capa do CATÁLOGO (`capa/capa.png`, lida pelo portal/PRO); a hero do guia é o banner live 16:9, e o `hero.png` cru é só reserva se o banner falhar. Registrado em 11/10/2026. |
| V10 | Emoji | Guia (logo) e v2 (títulos de card) usam | v6 proíbe | **A — por linha**: guia e v2 usam emoji só como ícone pequeno (logo, cartão), nunca no meio do texto; v5 e v6 sem emoji. (Nei, 11/10/2026) |

## Vídeo
| # | Conflito | Lado A | Lado B | Decisão |
|---|---|---|---|---|
| D1 | Ritmo do reel | 2–4s por troca (spec-reel.md:52, reel-profiles.json) | 5–7 trocas a cada 10s (reel-edita 03-sfx-e-qc.md:67) | **A — 1,5–3 s por troca** em reel/short; gancho pode mais rápido; explicativo 16:9 fora. Ajustar spec-reel/reel-profiles e reel-edita na etapa 2. (Nei, 11/10/2026) |
| D2 | Voz padrão do reel-edita | Regra: voz do Nei | `narra.sh:28` default `rachel` | **A — default = voz do Nei** (`voice-refs/nei.wav`, 0,6/0,6) no `narra.sh`; rachel só se pedida (ex.: inglês). Default geral do inemavox não muda. Código na etapa 2. (Nei, 11/10/2026) |
| D3 | Teto de zoom no reel | explicativo: ≤ 1,25 | makeshorts/spec-reel sem teto | **C — pela imagem**: com texto ≤ 1,25× em tudo (reel incluído); foto sem texto no reel até 1,4×. (Nei, 11/10/2026) |
| D4 | Preset viral (video-plan-editor) | corte 0,8–1,5s, whip/punch, karaokê caixa alta | regras de calma do explicativo | **Presets livres**: os 5 continuam, escolha por vídeo; D1 é o padrão sem preset; D2/D3/V7 valem para todos; `viral` só 9:16. (Nei, 12/10/2026) |
| D5 | `video-explicativo` | descrição ainda cita 9:16 | análise de 29/09 propôs tirar | **Já resolvido**: a descrição diz "NÃO use para reel/short/viral" e o 9:16 citado é só a versão vertical do mesmo explicativo. Conferido em 12/10/2026. |
| D6 | Caminho do contrato | AUTHORING.md:95 aponta `~/projetos/makeshorts/...` | arquivo real em `~/.claude/skills/makeshorts/references/` | **Não era erro**: `~/.claude/skills/makeshorts` é link para `~/projetos/makeshorts/.claude/skills/makeshorts`; o caminho do AUTHORING existe. Conferido em 12/10/2026. |

## Achado do teste (10/10/2026)
- A1 — `checks/preship.py` no modelo `~/.claude/skills/projetos-landing-guia/assets/template.html`: 8/13. Faltam `<main>`, `og:image`, `theme-color`, favicon e width/height nas imagens. Todo guia herda isso (5-mods e crunchlog 8/13; arena-capivara e ata 6/13). Corrigir no modelo é a etapa 3; nada foi alterado.

## Lacunas (não existe regra escrita)
- L1 — Arquivo oficial do logo INEMA (SVG/PNG) — não existe ainda. **Por ora a marca é o texto "INEMA.CLUB"**, como já aparece nas peças; o Nei vai passar o logo depois (12/10/2026). Quando chegar: `marca/` no kit + seção no DESIGN.md.
- L2 — Raio, sombra e largura máxima do guia. **Preenchida** pelo que o template já usa (DESIGN.md núcleo, 12/10/2026).
- L3 — Tamanho mínimo de fonte no guia e no curso v2 (só o v6 tem: 14px). **Preenchida**: leitura ≥ 14px em tudo; rótulo caixa alta ≥ 12px (DESIGN.md núcleo, 12/10/2026).
- L4 — Paleta dos motores de vídeo próprios (mapa, palco, reais, cardshorts, reelcomenta) só existe no código. **Resolvida**: as paletas estão escritas no DESIGN.md (linha Vídeo) e o amarelo foi unificado na V7; vermelho/verde/azul de dado continuam.
- L5 — Conjunto de ícones único (hoje: traço dourado no banner, CSS no v5, emoji/SVG no v2). **Fechada**: traço fino tipo Lucide para todo ícone desenhado; emoji conforme V10; v5 mantém CSS. (Nei, 12/10/2026)
