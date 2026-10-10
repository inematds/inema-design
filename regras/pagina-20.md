# Página: 20 pontos antes de publicar

Fonte: Claude Design Blueprint, hack 10/15 — "Pre-ship checklist: 20 points", derivado das 20 regras web do Power Design (github.com/ItsssssJack/power-design, MIT). Adaptado para guias, landings e cursos INEMA.

Como usar: cole esta lista junto da página e peça sim/não para cada ponto, com prova (medida, print ou linha do código). Corrija todo "não" e rode de novo até os 20 serem sim.
Script: `python3 checks/preship.py <pagina.html>` confere parte dos pontos 3, 16, 18, 19 e 20. Contraste, gosto e velocidade: olho, Lighthouse ou um segundo agente.

**Sempre medir servindo por HTTP** (página com CSS/JS em caminho absoluto quebra em `file://` e dá overflow falso — LESSONS 30/09).

1. [ ] Celular primeiro. O layout de 360px funciona; a página para em 1440px; blocos de texto param em ~75 caracteres.
2. [ ] Testado em 320, 390, 768, 1024 e 1440px. Nada rola de lado. Gutter de 16px no celular.
3. [ ] Tipo e espaço com `clamp()`. Nada de `vw` cru em fonte. Zoom de 200% funciona. A meta viewport não bloqueia zoom.
4. [ ] Texto ≥ 16px (curso v6: 18px; nunca < 14px). Alvos de toque ≥ 44×44px, 8px de distância.
5. [ ] Um botão principal por tela, na cor do acento da linha (guia: `--amb`). Repetido ao longo da página longa.
6. [ ] A primeira tela diz o que é, para quem e o que fazer — num notebook 1366×768 e num celular de 390px. (Guia: `#resumo` logo abaixo da hero.)
7. [ ] Texto corrido alinhado à esquerda, nunca justificado. Botões à esquerda (curso v2).
8. [ ] Linhas de 45 a 75 caracteres.
9. [ ] Entrelinha do corpo ≥ 1,5; títulos 1,0–1,2.
10. [ ] Espaços numa grade de 8 pontos, de uma escala só. Nada de 13px ou 27px avulsos.
11. [ ] Contraste de texto 4,5:1 (3:1 em texto grande); ícones e foco 3:1. Cor nunca carrega sentido sozinha. Âmbar não vira texto em fundo claro (curso v2).
12. [ ] Cores são variáveis (`--bg`, `--amb`…). Nenhum hex solto nos estilos. Claro/escuro reaproveita os mesmos nomes.
13. [ ] Botão, link e campo têm cinco estados: normal, hover, foco, pressionado e desabilitado. Anel de foco visível no teclado.
14. [ ] Estados vazio, carregando e erro desenhados. Erro ao lado do campo.
15. [ ] Movimento de 150 a 300ms com ease-out. `prefers-reduced-motion` respeitado. Nada toca sozinho sem botão de pausa.
16. [ ] Imagens e embeds com tamanho definido (width/height); a página não pula ao carregar.
17. [ ] Celular médio: LCP ≤ 2,5s, INP ≤ 200ms, CLS ≤ 0,1. Hero ≤ 200KB, JS ≤ 300KB.
18. [ ] Um `h1`. `header`, `nav`, `main` e `footer` de verdade. Link "pular para o conteúdo". Ordem do Tab segue a página.
19. [ ] Formulários: rótulo visível em todo campo, tipo de input certo, erro na linha. Nenhum campo a mais.
20. [ ] Camada de compartilhamento: título ≤ 60 caracteres, descrição ≤ 155, imagem 1200×630, theme-color e favicon.

## Pontos só do INEMA (somar aos 20)
- [ ] PT, EN e ES publicados, com links de idioma funcionando e caminhos de imagem certos em `en/` e `es/` (`naturalWidth` > 0 no Playwright). (LESSONS 05/10)
- [ ] Nenhum `[colchete]` de modelo sobrando: `grep -c "\[Nome\|\[Resultado" landing.html` = 0. (LESSONS 08/10)
- [ ] Texto que a IA escreveu dentro das artes conferido letra a letra.
- [ ] Nenhum `pageerror` no console (global de 1 letra colide com CDN). (LESSONS 01/10)
