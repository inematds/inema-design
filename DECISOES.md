# Decisões em aberto (o Nei escolhe)

As fontes divergem nos pontos abaixo. O kit NÃO escolheu nenhum lado. Quando decidir, escreva a escolha na linha e atualize `DESIGN.md` / `video/style.md`.

## Visual
| # | Conflito | Lado A | Lado B | Decisão |
|---|---|---|---|---|
| V1 | Cor primária "âmbar" | Guia: âmbar `#E2A23B` (template.html:21) | Curso v2: amarelo `#FACC15` (SKILL:201) | **B — amarelo `#FACC15`** em toda página nova (guia e curso). Os publicados até 10/10/2026 ficam como estão. Motivo: lê melhor no escuro (~12:1 contra ~8:1) e o portal nunca foi âmbar (é ciano `#00d9ff`). Banners seguem com dourado metálico. (Nei, 10/10/2026) |
| V2 | Fundo escuro de base | Guia `#0c0c10` | v2 `#111827` · v5 `#0E0D14` · v6 escuro `#15141B` | unificar ou manter por linha? |
| V3 | Acento dos cursos | v5/v6: menta/verde (`#7CE0C6`, `#0E6B55`) | guia/v2: âmbar/amarelo | é intencional (cursos ≠ guia)? |
| V4 | Fonte de título | Guia: Sora | v2: Inter · v5/v6: Newsreader (serif) | |
| V5 | Fonte condensada | Banner proíbe (gerar-banner.sh:55,74) | Thumb "manchete" pede sans condensada (thumbviral/estilos.py:5) | thumb é exceção? |
| V6 | Azul no banner | Memória: sem neon azul (feedback_banner_estilo_live:16) | `gerar-banner.sh:40` default "ícone 3D azul-ciano"; estilo `opus` fundo azul (:88) | corrigir o script? |
| V7 | Âmbar nos vídeos | `#F5A623` (legenda reel) | `#ffd23f` (finviral, eventos, cardshorts) · `#E2A23B`/`#f0e805` (docflow) | um âmbar de vídeo só? |
| V8 | Dosagem de dourado no banner | "Contido, dourado só como acento" (SKILL landing :298) | "Luz âmbar-laranja de palco, cor viva" (gerar-banner.sh:54) | |
| V9 | Hero do guia | Capa `split` (SKILL :221) | Banner 16:9 na hero, capa só reserva (SKILL :252) | |
| V10 | Emoji | Guia (logo) e v2 (títulos de card) usam | v6 proíbe | por linha (provável) |

## Vídeo
| # | Conflito | Lado A | Lado B | Decisão |
|---|---|---|---|---|
| D1 | Ritmo do reel | 2–4s por troca (spec-reel.md:52, reel-profiles.json) | 5–7 trocas a cada 10s (reel-edita 03-sfx-e-qc.md:67) | |
| D2 | Voz padrão do reel-edita | Regra: voz do Nei | `narra.sh:28` default `rachel` | corrigir o default? |
| D3 | Teto de zoom no reel | explicativo: ≤ 1,25 | makeshorts/spec-reel sem teto | vale 1,25 também no reel? |
| D4 | Preset viral (video-plan-editor) | corte 0,8–1,5s, whip/punch, karaokê caixa alta | regras de calma do explicativo | preset viral é só para 9:16? |
| D5 | `video-explicativo` | descrição ainda cita 9:16 | análise de 29/09 propôs tirar | conferir e corrigir? |
| D6 | Caminho do contrato | AUTHORING.md:95 aponta `~/projetos/makeshorts/...` | arquivo real em `~/.claude/skills/makeshorts/references/` | corrigir caminho |

## Achado do teste (10/10/2026)
- A1 — `checks/preship.py` no modelo `~/.claude/skills/projetos-landing-guia/assets/template.html`: 8/13. Faltam `<main>`, `og:image`, `theme-color`, favicon e width/height nas imagens. Todo guia herda isso (5-mods e crunchlog 8/13; arena-capivara e ata 6/13). Corrigir no modelo é a etapa 3; nada foi alterado.

## Lacunas (não existe regra escrita)
- L1 — Arquivo oficial do logo INEMA (SVG/PNG) — não encontrado.
- L2 — Raio, sombra e largura máxima do guia.
- L3 — Tamanho mínimo de fonte no guia e no curso v2 (só o v6 tem: 14px).
- L4 — Paleta dos motores de vídeo próprios (mapa, palco, reais, cardshorts, reelcomenta) só existe no código.
- L5 — Conjunto de ícones único (hoje: traço dourado no banner, CSS no v5, emoji/SVG no v2).
