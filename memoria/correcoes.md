# correcoes.md — o que o Nei já reprovou

Uma regra por linha, com data. Lido antes de toda peça. Quando o Nei corrigir algo visual, acrescente aqui (mais recente no topo de cada seção).
Origem: Lessons de `~/projetos/wifi/CLAUDE.md`, memórias `feedback_*` e análises de erro, consolidadas em 10/10/2026.

## Vídeo — abertura
- 09/10 — Capa (frame 0) = o GANHO da pessoa; abrir direto no flagrante foi reprovado (Execução Longa).
- 09/10 — Clima: quadro 0 com data dd/mm/aaaa + número viral com fonte.
- 08/10 — Todo vídeo longo precisa de gancho; abrir com mapa e "Neste momento…" foi reprovado (docflow).
- 08/10 — Frame 0 vazio na trilogia gestão de agentes: cena 1 abre com shot `hook` em `@start`.
- 08/10 — Gancho: texto dentro da imagem gerada, não sobreposto; abertura < 5s = uma imagem; a fala nomeia o sujeito.
- 08/10 — Explicativo/refazvideo: capa de impacto + prévia + "no fim: …".

## Vídeo — imagem, câmera, transição
- 09/10 — Zoom 1,4–1,9 cortando texto e troca de imagem com punch: reprovados. Dissolve, imagem inteira, zoom ≤ 1,25.
- 09/10 — Tornado/ciclone em SVG de anéis ficou feio: imagem realista + sobreposições finas; troca de assunto = tela limpa + nome grande.
- 28/09 — Cards de texto sem imagem nem prova real ("nem estagiária faria"). Pelo menos 1 em 3 visuais é prova real.
- 28/09 — Ken Burns lento como único movimento de short: "sem atração".
- 28/09 — Cena de IA impossível, telejornal ou entrevista simulada ("AO VIVO", logo de emissora).

## Vídeo — voz e texto
- 09/10 — Ano em algarismo: "2024" saiu "2004". Ano sempre por extenso e conferido por Whisper.
- 08/10 — Chatterbox `nei` com exaggeration 0.85 / cfg 0.35 chiou o "s". Usar 0.6/0.6, `atempo` ≤ 1,15.
- 29/09 — Voz `rachel` falando PT ("inema" → "enema"). Narração INEMA = voz do Nei.
- 29/09 — Legenda de 7 palavras, letra solta no frame 0, render 25fps, áudio a −26 LUFS.
- 08/10 — Vídeo refeito sem "Fonte: …" escrito.

## Short / reel
- 07/10 — Short no YouTube não leva thumb.
- 28/09 — Nove assuntos num short. Uma ideia por short.
- 28/09 — Música de fundo em short didático.
- 28/09 — "Viral" feito com `video-explicativo` 16:9 reembalado. Short = makeshorts/reel-edita-inema.
- 28/09 — Lote/publicação sem protótipo aprovado.

## Banner, thumb, arte
- 08/10 — Thumb com flux + texto Pillow por cima: reprovada. Codex com o gancho desenhado; estilo variado.
- 06/10 — Banner da home: estilo MODS (cena cinematográfica); grade liso só no Atendimento.
- set/26 — Fonte "de jogo" (condensada, inflada, cartunesca, dourado+ciano) no banner.
- set/26 — Neon azul no título do banner; INEMA.PRO não é referência.
- set/26 — Texto da IA na arte com erro ("entomo", "specifiication", "inemafds"): conferir antes de publicar.

## Página, guia, curso
- 10/10 — Quadros "Últimas Atualizações" do portal saturados (tudo quase branco + repo em MAIÚSCULAS negrito). Descrição cinza-claro `#aab4c3` peso 400; repo em amarelo `#FACC15`, minúsculo; selo com opacidade .75 (portal a2251a7).
- 08/10 — Landing v6 publicada com `[colchetes]` do modelo.
- 05/10 — Guia ES com 5 imagens quebradas (caminho `assets/` não ajustado na tradução).
- 01/10 — Global de 1 letra colidiu com script de CDN e a página parou.
- 30/09 — Overflow medido em `file://` (falso). Medir por HTTP.
- 29/09 — Vitrine pública com vídeo reprovado. Só o que o Nei aprovou.
