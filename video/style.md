# style.md — vídeo INEMA

Fonte do método: Claude Design Blueprint, hack 1 ("style.md" + "motion brief"). Os números abaixo são os que já estão escritos no ecossistema (fonte entre parênteses).

Dois usos:
1. **Padrão INEMA** (seções A e B): vale quando não há referência.
2. **A partir de uma referência** (seção C): copie o modelo para a pasta do vídeo e preencha a partir do vídeo que o Nei apontou. O estilo da referência entra; o conteúdo, logo e personagens dela nunca.

MS = `~/.claude/skills/makeshorts`, EXV2 = `~/projetos/explicavideos/engine/v2/AUTHORING.md`.

---

## A. Explicativo 16:9 (explicavideo v2, refazvideo, docflow, longo do finviral)

### Abertura
- Frame 0 = capa de impacto: shot `hook` em `"@start"`, imagem forte com a promessa escrita DENTRO da arte. (EXV2:100-102)
- A capa mostra o GANHO da pessoa; a provocação vem depois. (EXV2:106)
- 1ª frase falada = a de impacto, nomeando o sujeito. Proibido "Imagine que…/Pense num…/Se você…/Neste momento…". (EXV2:104)
- Abertura < 5s = UMA imagem; 5–6s cabem thumb + imagem. (EXV2:101)
- Gatilho de atenção logo depois: prévia do que vem + "no fim: …". (LESSONS 08/10)

### Ritmo
- Mais de 4s sem troca de conteúdo = aviso (palavra aparecendo, `punch_at` e `strike_at` não contam). (EXV2:128)
- Troca de assunto = tela limpa (dip preto) + nome do assunto grande antes do diagrama. (LESSONS 09/10)

### Câmera e transição (ilustração)
- `calm: true`: troca por dissolve suave, sem punch nem blur; ilustração inteira na moldura. (EXV2:117)
- Zoom ≤ 1,25 em ilustração com texto; aproximação lenta. (EXV2:120)
- Re-enquadrar a mesma imagem com `cont` + `from`, nunca shot novo com punch. (EXV2:118-119)
- Print real vale mais que card de texto. (EXV2:116)

### Texto na tela
- Legenda até 3 palavras / 22 caracteres, 70px, sem sobreposição. Sem cabeçalho de capítulo no topo. (EXV2:125-126)
- Gancho: texto dentro da imagem gerada, não legenda por cima. (EXV2:101)

### Voz e áudio
- Voz do Nei (avatar estúdio HeyGen ou `nei*` no Chatterbox 0.6/0.6, `atempo` ≤ 1,15). Nunca `rachel` em PT. (LESSONS)
- Final em −14 LUFS, true peak ≤ −1 dBTP. (EXV2 produce.py)

### Avatar do Nei (todos os formatos — D8, 15/10/2026)
- **Nunca em tela cheia.** O máximo é meia tela (16:9: metade direita; 9:16: metade de baixo). O `rosto` do explicavideos viral cresce só até meia tela.
- **9:16:** capa sem avatar (texto inicial segurado ~5 s) → avatar em **meio tamanho** no 1º bloco → **PiP** pequeno no canto do 2º bloco em diante, com a cena no quadro inteiro (explicavideos `"avatar_916": "pip"`, `"pip_cena"`, `"capa_segura"`).
- **Imagens sem repetir:** uma imagem por momento; dado de lugar vira **mapa real** (satélite NASA HLS/GIBS anotado), não foto genérica de novo.

---

## B. Short / reel 9:16 (makeshorts, reel-edita-inema, reelcomenta, cardshorts, eventosextremospub, curto do finviral)

### Abertura
- Frame 0 = capa completa: manchete de 3–6 palavras + visual do tema, visível em t=0, nada surgindo do vazio. (EXV2:109-112; MS spec-visual.md:27)
- Gancho falado ≤ 2s e já escrito na tela; gancho secundário entre 3 e 8s. (MS SKILL)
- Clima/notícia: data dd/mm/aaaa + número tipo "ATÉ 300 MM" com fonte no quadro 0. (MEM/feedback_eventos_extremos_abertura)
- Teste: "eu pararia o dedo aqui?"
- **reel7etapas (D9, 18/10/2026):** quadro 0 = GATILHO (medo, novidade ou provocação) com fato/número e fonte, imagem do flagrante nítida (sem desfoque), luz dramática liberada no gancho; o ganho/alívio só a partir da etapa 4. Exceção à "capa = ganho" das outras linhas.
- **reel7etapas (D10, 18/10/2026):** objetivo = público no inema.club; plano (público, ganho/dor/desejo, nota de potencial) antes da fala; rosto desde o quadro 0 em meia tela → PiP; ≥ 2 diagramas/visuais que ensinam; CTA "tá tudo no inema.club, ou me pede o link".
- **r7ex e r7exp (D16, 21/10/2026):** o rosto ABRE em meia tela no quadro 0 — 9:16 metade de baixo (1080x960 em y 960) na parte 1; 16:9 metade direita até o fim da capa — e depois vai para o PiP, voltando à meia tela onde o plano pedir (`avatar: meia` na parte do r7ex). Título da capa no alto (9:16) ou à esquerda (16:9), fora do rosto.
- **Reels 9:16 do r7exp (D17, 22/10/2026):** avatar no terço de baixo (1080x640 em y 1280) o reel inteiro; 2/3 de cima = título · explicativo · imagem de impacto. Quadro 0 = capa nos 2/3 de cima (imagem de impacto + título ≤ 4 palavras) até o fim da 1ª frase; legenda depois, no pé dos 2/3. O completo 16:9 do r7exp segue o D16.

### Ritmo
- Uma ideia por short. (MEM/feedback_shorts_virais)
- Troca de conteúdo a cada **1,5–3 s** (D1, 11/10/2026; antes 2–4 s no makeshorts e 5–7 trocas/10 s no reel-edita); no gancho (0–3 s) pode ser mais rápido. Pulso/brilho sobre a mesma imagem não conta como troca. Vale para reel e short 9:16; explicativo 16:9 segue o ritmo calmo.
- Reengajar perto de 25% e 65% com troca de visual ou ângulo. (spec-visual.md:55)
- Pelo menos 1 em cada 3 visuais é prova real (print, site, dado). (MS SKILL)
- Duração: divulgação 20–50s (máx. 59); tutorial 35–60s (máx. 75). ~150 palavras/min. (reel-profiles.json)

### Texto na tela
- Legenda palavra a palavra, 1–3 palavras, ≤ 22 caracteres; Montserrat Black, contorno preto 8px, palavra-chave amarelo `#FACC15` (V7, 10/10/2026; antes âmbar `#F5A623`), ≥ 64px. (spec-reel.md:60-64)
- Safe area: topo 10%, base 20%, laterais 6%, coluna direita 12%. Legenda não cobre o rosto. (reel-profiles.json)

### Áudio
- **Sem efeitos sonoros no meio** (D7, 15/10/2026): só voz + trilha baixa (`som_viral.py --sem-efeitos`).
- Sem música de fundo em short didático. SFX só para marcar ação/revelação, vindos do inemavox. (spec-visual.md:57; RE 03-sfx-e-qc.md)
- −14 LUFS ±1, true peak ≤ −1; 1080×1920, 30fps, h264/aac.

### Publicação
- Short no YouTube não leva thumb. Protótipo aprovado pelo Nei antes de lote. (MEM)

---

## C. Modelo para preencher a partir de uma referência

Passos: baixar a referência (inemavox), tirar 1 quadro a cada 0,5s, preencher abaixo com números, propor 3 storyboards e PARAR para o Nei escolher.

```
# style.md — o visual de [nome da referência]
Referência: [link]   Extraído em: [data]

## Paleta
- Fundo: #
- Tinta principal: #
- Acento 1: #
- Acento 2: #
- Nunca usar: (cores que a referência nunca mostra)
→ Na produção, as cores finais vêm da linha do DESIGN.md; a referência dá a proporção e o contraste.

## Tipo
- Fonte de título / de corpo:
- Tamanhos (título, rótulo):
- Peso e caixa:

## Cenas
- Número de cenas:
- Duração (mais curta → mais longa, em s):
- Corte médio (s):
- Segurar a última cena (s):

## Transições
- Quais (corte seco, whip, morph, wipe, dissolve) e com que frequência:

## Câmera (use as palavras de video/camera.md, com número)
- Movimentos e velocidade:

## Textura
- Grão, ruído, sombra, desfoque:

## Texto
- Como entra:
- Como sai:
- Palavras por cena:

## Gancho
- O que aparece no quadro 0:
- Primeira frase (estrutura, não o texto):

## Nunca
- Três visuais a evitar:
```

## Presets do video-plan-editor (D4, 12/10/2026)
- Os 5 presets (`acao`, `suave`, `promo`, `vendas`, `viral`) continuam como estão e são escolha por vídeo; o ritmo do preset escolhido vale.
- Sem preset escolhido, vale o padrão INEMA: troca a cada 1,5–3 s no reel/short (D1).
- Regras que valem para TODO preset (vieram de reprovação): zoom/punch nunca corta texto (D3); voz do Nei (D2); amarelo `#FACC15` (V7); `viral` só em 9:16, nunca em explicativo 16:9.
