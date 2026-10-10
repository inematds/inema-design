# Revisão de 5 quadros com nota

Fonte: Claude Design Blueprint, hack 1 (passo E do "motion brief"). Complementa o QA técnico que já existe (`qa_short.py`, `build_block.py --strict`, `produce.py`), que mede formato, áudio e ritmo, mas não dá nota ao visual.

## Antes do render (barato)
1. Uma imagem parada por cena (ou a folha de quadros da prévia) mostrada ao Nei.
2. Só renderiza com "pode fazer". Nos projetos que já têm portão (refazvideo `APROVADO_HEYGEN`, reelcomenta `previa`), este é o mesmo portão — não criar outro.

## Depois do render
1. Extrair os quadros em 0%, 25%, 50%, 75% e 100% da duração:
   ```bash
   V=video.mp4; D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$V")
   for p in 0 25 50 75 100; do
     t=$(python3 -c "print(min($D*$p/100, $D-0.05))")
     ffmpeg -v error -y -ss "$t" -i "$V" -frames:v 1 "quadro-$p.jpg"
   done
   ffmpeg -v error -y -i quadro-0.jpg -i quadro-25.jpg -i quadro-50.jpg -i quadro-75.jpg -i quadro-100.jpg \
     -filter_complex "[0][1][2][3][4]hstack=5,scale=2000:-1" folha-5.jpg
   ```
2. Olhar a folha e dar nota de 0 a 10 em três eixos:
   - **Visual**: imagem inteira, sem corte de texto, sem letra quebrada, legenda dentro da área segura, avatar sem cabeça cortada.
   - **Ritmo**: cada quadro mostra algo diferente; nada parado; o quadro 0 já é a capa.
   - **Marca**: cores e fontes da linha certa do `DESIGN.md`; nada da lista de `memoria/correcoes.md`.
3. Registrar num `revisao.md` ao lado do vídeo: as três notas + uma frase de motivo para cada nota < 8.
4. Nota < 8 em qualquer eixo: corrigir e renderizar de novo (se o render for gratuito). Se refazer custar crédito (HeyGen, Kling, Agnes), **parar e perguntar ao Nei**.

## O que olhar com mais peso
- Quadro 0: é capa? tem a promessa/manchete legível? (falha mais repetida: frame 0 vazio — 08/10)
- Texto acentuado cortado no drawtext; `%` sumindo. (docflow, eventosextremospub FALHAS)
- Legenda cortada na borda ou "-feira" solto. (finviral FALHAS 10/10)
- Cabeçalho ou elemento sobreposto à capa. (finviral FALHAS 10/10)

## Projetos automáticos (finviral)
A revisão só **grava a nota em log e avisa** (bot v3). Nunca bloqueia nem refaz sozinha às 02:00. Entra atrás de flag opt-in, testada com `SEM_BOT=1 SEM_AVATAR=1`. Ver `MAPA-PROJETOS.md`.
