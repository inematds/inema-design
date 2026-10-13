# DESIGN.md — INEMA

Fonte do esqueleto: Claude Design Blueprint, hack 4 e 15 (formato DESIGN.md do Google Labs / Power Design, MIT).
Todos os valores abaixo vêm de arquivos que já existem (fonte entre parênteses). Nada foi inventado.
Onde as fontes divergem, o item aponta para `DECISOES.md`.

Abreviações: SK = `~/.claude/skills`, MEM = memórias do projeto wifi, LESSONS = `~/projetos/wifi/CLAUDE.md` › Lessons.

---

## 1. Núcleo comum (vale para tudo)

### Uma linha
INEMA ensina IA na prática, de graça, para gente comum: conteúdo aberto (INEMA.CLUB), sem hype, com prova real e a voz do Nei.

### Público
- Cursos v5: 40+ leigo. Cursos v6: iniciante 30+. Guias: quem quer usar o projeto. (SK/formato-curso-v5, v6)
- Projetos de negócio em EN/ES: ES = América Latina, EN = global. (MEM/feedback_idioma_e_mercado)

### Voz
- "Você", voz ativa, verbo concreto ("Cole o texto"). (SK/formato-curso-v6 CONTEUDO-INICIANTE.md:16)
- Promessa verificável antes do conceito; analogia do mundo real. (v5 CONTEUDO-40MAIS.md:13)
- Sem hype ("revolucionar"), sem condescendência, sem "!!". (v5 :96; v6 :21)
- Regras de frase e palavras proibidas: `regras/texto.md`.

### Cor sem significado sozinha
- Nunca passar informação só por cor; sempre rótulo ou ícone junto. (V5-DESIGN.md:18; V6-DESIGN.md:15)
- Âmbar nunca significa "errado". Errado = cor `bad` da linha. (V5-DESIGN.md:16; V6-DESIGN.md:14-15)

### Tokens, não hex solto
- Cor só por variável CSS; claro/escuro trocando o valor da mesma variável. (SK/projetos-landing-guia/SKILL.md:121)

### Forma e medidas do guia (L2, medido no template em 12/10/2026)
- Largura: conteúdo até 1160px; texto corrido 62–74ch.
- Raio: 10px botão e controles · 12px bloco de código e número de passo · 14px cartão e figura de exemplo · 16px figura da hero · 999px pílula.
- Sombra: nenhuma em cartão (separação por borda 1px `--line`); única sombra é a figura da hero (`0 30px 80px -30px #000`).

### Tamanho mínimo de letra (L3, 12/10/2026)
- Corpo 16px (guia) / 18px (v6). Texto de leitura nunca < 14px em nenhuma linha.
- Rótulo em CAIXA ALTA com espaçamento (chip, idioma, pílula) pode descer até 12px (.75rem). Hoje o chip do guia está em .72rem (11,5px): sobe para .75rem na etapa 3.

### Emoji (V10, 11/10/2026)
- Guia e curso v2: emoji só como ícone pequeno (logo, título de cartão); nunca no meio do texto nem em fecho de aula.
- Cursos v5 e v6: sem emoji (decisão pedagógica: não infantilizar o adulto iniciante).

### Ícones (L5, 12/10/2026)
- Ícone desenhado (não emoji) = estilo **traço fino de linha** tipo Lucide (MIT), SVG inline na página, cor por `currentColor`: amarelo ou branco no escuro, tinta no claro.
- Mesma linguagem dos ícones de traço dourado dos banners.
- Emoji só onde a V10 deixa (logo e cartão em guia/v2). v5 mantém a regra própria (ícones só CSS, até 10).

### Fonte (V4, 10/10/2026)
- Título de toda página nova (guia e cursos v2/v5/v6): **Sora**. Corpo: **Inter**. Código: JetBrains Mono. Serifada não entra mais em título.

### Amarelo INEMA `#FACC15` (V1 + V3, 10/10/2026)
- **Cor de marca única** de guia e de todo curso novo (v2, v5, v6). Menta, verde e ocre saem como acento.
- **Fundo escuro:** o amarelo pode ser letra (destaque de título, link, rótulo) e fundo de botão (letra `#1a1206`).
- **Fundo claro (papel, modo claro):** o amarelo **nunca é letra**. Só preenchimento:
  - botão: fundo `#FACC15`, letra `#1a1206`;
  - palavra de destaque: letra na cor da tinta + marca-texto `linear-gradient(transparent 55%, #FACC15 55%)`;
  - caixa de dica: fundo `#FEF9C3`, filete `#EAB308`;
  - link: letra `#854d0e`, sublinhado `#FACC15` 3px — a única letra colorida.
- Verde fica só como **estado** "certo/feito" (par do vermelho `bad`), com rótulo junto; nunca como cor de marca.

### Arte gerada
- Capa, hero, cena de curso e thumb: Codex image_gen pela assinatura; flux2-klein é reserva. (MEM/feedback_capa_guia_codex; V6-DESIGN.md:93)
- Texto da arte (gancho, thumb): desenhado DENTRO da imagem pelo Codex, não sobreposto. (MEM/feedback_thumb_viral_codex; LESSONS 08/10)
- Conferir o texto que a IA escreveu na imagem antes de publicar ("entomo", "specifiication", "inemafds" já passaram). (SKILL landing :302-303)
- Fenômeno natural (tornado, ciclone): imagem realista + sobreposições finas, nunca SVG desenhado. (LESSONS 09/10)

### Lacunas conhecidas
Sem arquivo oficial de logo INEMA; sem raio/sombra e largura máxima definidos para o guia. Ver `DECISOES.md`.

---

## 2. Linha padrão — Guia / landing de projeto ("dark âmbar")

**É o padrão quando a peça não diz a linha.** Dono: SK/projetos-landing-guia (assets/template.html).

| Token | Escuro | Claro (`body.light`) | Uso |
|---|---|---|---|
| `--bg` | `#0c0c10` | `#f6f7f9` | fundo |
| `--bg2` | `#14141b` | `#eceef2` | faixa alternada |
| `--card` | `#16161e` | `#ffffff` | cartão |
| `--line` | `#272730` | `#e1e3ea` | borda |
| `--txt` | `#e9e9ee` | `#1a1a22` | texto |
| `--mut` | `#9a9aa6` | `#5b5b68` | texto secundário |
| `--amb` | `#FACC15` | `#a16207` | acento único: botão, destaque (V1, 10/10/2026; antes `#E2A23B`/`#b9791d`, que continua nos guias já publicados) |
| `--amb2` | `#f0c070` | `#a16207` | acento claro |
| `--sky` | `#38bdf8` | `#0369a1` | **só** o link INEMA.CLUB |
| `--pro` | `#cbd5e1` | `#b45309` | selo PRO |

- Botão primário: fundo `--amb`, texto `#1a1206`, raio 10px. (template.html:57)
- Fontes: **Sora** (títulos, nav, botões, chips), **Inter** (corpo), **JetBrains Mono** (código). (template.html:17,35,37)
- Chip: caixa alta, letter-spacing .14em. (template.html:40)
- Hero: banner 16:9 (1400px JPG) estilo live; segundo banner "grade" no início de "O que é". (SKILL :252-262; MEM/feedback_banner_estilo_live)
- `#resumo`: 3–5 frases, 50–100 palavras, logo abaixo da hero. (SKILL :16-22)
- Sempre PT + `guia/en/` + `guia/es/`.

## 3. Linha Curso v2 ("inema-dark", Tailwind)
Dono: SK/formato-curso-v2 (SKILL.md, DESIGN-SYSTEM.md).
- Fundo `#0c0c10`, superfície `#16161e`, borda `#272730` (V2, 10/10/2026: mesmo preto do guia; antes `#111827`/`#1f2937`/`#374151`, que continua nos cursos já publicados). Texto `#e6e6e6`, secundário `#a8a8b3`. (DS:319-324) Nunca `#000`/`#fff` puros. (DS:377)
- Primária **amarela `#FACC15`** (logo, CTA, dica); no claro, texto `#a16207`. (SKILL:201) É a mesma cor do guia desde a V1 (10/10/2026).
- Sky `#38bdf8` = link INEMA.CLUB e cor secundária dos SVG. (SKILL:202,205)
- Cor por trilha: T1 emerald, T2 blue, T3 purple, T4 amber, T5 teal, T6 rose. (SKILL:188-195)
- Temas: sépia `#FBF0D9`/`#5F4B32`; alto contraste `#0A0E14`/`#F5F7FA`; claro sem gradiente. (DS:306,378-381)
- Fonte: títulos **Sora** (V4, 10/10/2026; antes Inter), corpo Inter. Botões à esquerda; numeração em círculo; SVG futurista 1 por módulo. (SKILL:140-155,255)

## 4. Linha Curso v5 ("dark editorial", 40+)
Dono: SK/formato-curso-v5 (assets/aula.css, V5-DESIGN.md).
- Escuro: bg `#0c0c10` (V2, 10/10/2026; antes `#0E0D14`), bg2 `#15131d`, painel `#1a1824`, tinta `#ECE6D9`, secundário `#948DA6`, fraco `#6C6580`, linha `#2A2637`.
- Acento amarelo `#FACC15` (V3, 10/10/2026; antes menta `#7CE0C6`, dim `#4FB79E`); atenção `--warm #F2B45C`; erro `#E0736F`. Papel e sépia seguem a regra "amarelo em fundo claro" do núcleo.
- Papel: `#F6F1E7` / tinta `#2A2620` / acento `#0F7A61` / warm `#9A6310`. Sépia: `#ECE0C9` / `#43331F` / `#0F6E58` / `#8A5A12`.
- Fontes: **Sora** em títulos e números (V4, 10/10/2026; antes Newsreader), Inter (texto), Space Mono (rótulos). Leitura 60ch.
- Ícones: até 10, só CSS, nunca decorativos (troféu, medalha, confete, mascote proibidos). (V5-DESIGN.md:22,68)

## 5. Linha Curso v6 ("papel", iniciante 30+)
Dono: SK/formato-curso-v6 (assets/aula.css, V6-DESIGN.md).
| Token | Papel (padrão) | Escuro | Sépia |
|---|---|---|---|
| bg | `#F7F3EA` | `#0c0c10` (V2; antes `#15141B`) | `#EFE3CB` |
| bg2 | `#EFE8DA` | — | — |
| painel | `#FFFFFF` | `#1F1D28` | — |
| tinta | `#221E18` | `#EFEAE0` | — |
| secundário | `#5E5546` | — | — |
| linha | `#E2D9C8` | — | — |
| accent (ação/marca) | `#FACC15` como preenchimento; link `#854d0e` (V3; antes `#0E6B55`) | `#FACC15` (antes `#7CE0C6`) | igual ao papel (antes `#0D5F4C`) |
| ok (estado "certo") | `#0E6B55` | `#7CE0C6` | `#0D5F4C` |
| warm (atenção) | `#8F520A` | `#F2B45C` | `#7E4A0C` |
| bad (exemplo ruim) | `#A83426` | `#F0918A` | `#9A3122` |
- Fontes: **Sora** no título (h1 clamp 36–60px, peso 800, -.01em; V4, 10/10/2026; antes Newsreader peso 500 -.02em), Inter 18px/1.7, JetBrains Mono só em código. Texto nunca < 14px.
- Coluna `.aula` 40rem; visual `.largo` até 54rem; gutter 16px; raio 14px; botão pílula ≥ 40px de altura.
- Cena ilustrada **sem texto dentro da imagem** (tradução é só HTML). Sem emoji.

## 6. Linha Banner (portal, eventos, guias)
Dono: `gerar-banner.sh` + MEM/feedback_banner_estilo_live, feedback_banner_portal_limpo.
- **live** (padrão): fundo preto com luz âmbar/laranja de palco; letras brancas + dourado/âmbar; ícones em traço dourado.
- **grade**: 6 cartões com objetos 3D dourados; faixa inferior escura com borda dourada. Grade liso só no Atendimento.
- Dosagem (V8, 10/10/2026): **letras contidas** (branco + UMA palavra grande em dourado) e **cena com luz quente viva** (palco âmbar/laranja, bokeh, reflexos). Nunca tudo dourado, nunca cinza/monocromático.
- Tipo: sans geométrica (Montserrat/Gotham), extra-bold × fina. **Nunca fonte de jogo** (condensada, inflada, cartunesca). (gerar-banner.sh:55,74) A thumb é a única exceção à condensada (V5).
- Sem neon azul no título; INEMA.PRO não é referência. Azul (fundo e molduras) só no estilo **opus**, opcional, que só sai quando pedido (tema de IA/chip/modelo). live e grade nunca levam azul. (V6, 10/10/2026)
- **Selo do nome em azul (V11, 13/10/2026):** quando o banner cita o projeto ou produto, o nome vai em azul `#3B9EFF` (Sora ExtraBold, brilho leve) acima do título, à esquerda (`gerar-banner.sh --selo "Nome"` ou `selo-banner.py`). Se o nome já está no título da imagem, não leva selo. É a única exceção ao "sem azul" do live/grade. Primeiro uso: área inemaSEO (eventos b5d7201, portal 4badec3).
- Banner novo da home = estilo MODS (cena cinematográfica, título dourado enorme à esquerda).

## 7. Linha Thumb (YouTube longo; short NÃO leva thumb)
Dono: `~/projetos/output/thumbviral/` + MEM/feedback_thumb_viral_codex.
- Gancho de 2–4 palavras PT, caixa alta, palavra-chave em amarelo, sujeito grande com emoção, alto contraste, etiqueta "INEMA.CLUB".
- Estilo sorteado entre os 10 de `estilos.py`; não repetir o padrão "texto branco+amarelo empilhado à esquerda".
- Fonte condensada **pode** na thumb (estilo "manchete" e outros que pedirem): ela é exceção, porque disputa atenção no feed em tamanho de selo. (V5, 10/10/2026)

## 8. Linha Vídeo
Regras completas em `video/style.md` (padrão INEMA preenchido) e `video/camera.md`.
- Legenda de reel: Montserrat Black, contorno preto 8px, palavra-chave amarelo `#FACC15` (V7, 10/10/2026; antes âmbar `#F5A623`), ≥ 64px (86px no empilhado). (MS spec-reel.md:60-64)
- Paletas dos motores próprios (hoje no código, sem arquivo):
  - eventosextremospub `motor/mapa.html`: fundo `#05080c`, vermelho `#ff2a1f`, âmbar `#ffd23f`, azul `#5ec8ff`, Inter.
  - finviral `motor/palco.html`: `--ink #0b0f14`, `--red #ff2a1f`, `--amb #ffd23f`, `--grn #2bff88`, `--blu #5ec8ff`; Archivo Black + Inter.
  - docflow `motores/reais.py`: fundo de gráfico `#0d1117`, destaque `#f0e805`/`#E2A23B`, Montserrat ExtraBold.
  - cardshorts `estilos/comum.css`: vermelho `#ff3b2f`, amarelo `#ffd23f`; zona da legenda y 1450–1720.
  - **V7 (10/10/2026):** todo vídeo novo usa um amarelo só, `#FACC15`, com contorno preto na legenda. Os tons acima (`#F5A623`, `#ffd23f`, `#E2A23B`, `#f0e805`) são o estado do código até a etapa 2; vermelho/verde/azul de dado (alta, queda, mapa) continuam.
  - reelcomenta `reelcomenta.py`: constantes AMB/VERM/BRANCO; Anton + Montserrat.
  - ⚠ quatro "âmbares" diferentes nos vídeos — `DECISOES.md` V7.
