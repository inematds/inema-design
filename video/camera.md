# Palavras de câmera (com número)

Fonte: Claude Design Blueprint, hack 1 — "Camera words". Use estas palavras no roteiro/plano de cena SEMPRE com número. "Deixa bonito" não é direção.
Os limites INEMA (coluna da direita) vêm do que o Nei aprovou/reprovou e valem acima da sugestão do Blueprint.

| Palavra | O que é | Como pedir | Limite INEMA |
|---|---|---|---|
| **Push in** (aproximar) | câmera chega perto | "push in 8% em 3s" | ilustração com texto: zoom final ≤ 1,25 (EXV2:120) |
| **Pull back** (afastar) | câmera se afasta e mostra mais | "pull back de 1,2 para 1,0 em 4s" | — |
| **Zooms a 0,7×** | todo zoom a 70% da velocidade | "todos os zooms a 0,7×" | padrão bom para 16:9 calmo |
| **Corte no tempo** | troca de cena na batida, sem fade | "corte seco no tempo forte" | reel; no explicativo ilustrado prefira dissolve (`calm`) |
| **Dissolve** | uma imagem funde na outra | "dissolve de 0,6s" | padrão do explicativo ilustrado (`calm: true`) |
| **Whip pan** | chicote lateral borrado que esconde o corte | "whip pan para a próxima cena" | só reel, só com função; nunca no explicativo calmo |
| **Match cut** | a próxima cena começa com a mesma forma no mesmo lugar | "match cut do círculo do logo para o sol" | — |
| **Rack focus** | o foco passa de um objeto a outro | "rack focus do avatar para a tela" | — |
| **Parallax** | camadas em velocidades diferentes dão profundidade | "parallax com 3 camadas" | pixflow faz 2.5D real |
| **Hold** (segurar) | parar no último quadro | "hold 1,5s no último quadro" | CTA final |
| **Ease out** | começa rápido, termina devagar | "ease out em todo movimento" | — |
| **Continuar** (`cont` + `from`) | mesma imagem, câmera segue de onde parou | `cont: true, from: {focus, zoom}` | único jeito de re-enquadrar a mesma imagem (EXV2:118) |

## Nunca
- Punch-in ou close forte que corta o texto da ilustração (zoom 1,4–1,9 reprovado, 09/10).
- Troca de imagem "com choque" no explicativo.
- Pulso de brilho/flash/zoom na mesma imagem contando como "troca" no reel.
- Ken Burns lento de ~4,5% como único movimento de um short (lote de 28/09 reprovado: "sem atração").

## Onde os motores guardam a câmera hoje
- explicavideos v2: `focus`, `zoom [z0,z1]`, `calm`, `cont`/`from` no JSON do bloco.
- docflow `motores/reais.py`: lista fixa de 5 movimentos (zoom-in, esquerda, zoom-out, direita, subir), zoompan linear.
- eventosextremospub: zoom/pan do deck.gl em `mapa.html` / `cena.js`.
- reelcomenta: `lento` e zoom de `fundo_reel()`.
