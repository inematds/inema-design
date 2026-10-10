# inema-design — leia antes de qualquer peça visual

Kit de design do ecossistema INEMA: páginas, guias, cursos, banners, thumbs, explicavideos, shorts e reels.
Baseado no método "design-os" do Claude Design Blueprint (originais em `fonte/blueprint/`), adaptado ao que o Nei já aprovou e reprovou.

## Ordem de leitura

1. `DESIGN.md` — a marca. Vence o gosto do modelo. Ache a **linha** do produto (guia, curso v2/v5/v6, banner, thumb, vídeo) e use só os tokens dela.
2. `memoria/correcoes.md` — o que o Nei já reprovou. Não repetir.
3. Conforme a peça:
   - página/guia/curso → `regras/pagina-20.md` + `regras/texto.md`
   - vídeo (16:9 ou 9:16) → `video/style.md` + `video/camera.md` + `video/revisao-5-quadros.md` + `regras/texto.md` (fala e legenda)
   - peça a partir de uma referência → `regras/bar.md`
4. `MAPA-PROJETOS.md` — onde cada recurso entra em cada projeto.
5. `DECISOES.md` — conflitos ainda em aberto. Se a peça cair num deles, **pergunte ao Nei**, não escolha sozinho.

## Como trabalhar

- Diga em até seis linhas o que leu e quais regras valem para a peça.
- Nunca invente cor, fonte, logo ou ícone. Use `DESIGN.md`. Se faltar, é lacuna: pergunte.
- Pedido que bate de frente com `DESIGN.md` ou `correcoes.md`: pare e pergunte.
- Página: antes de dizer pronto, rode `python3 checks/preship.py <arquivo.html>` e responda os 20 pontos.
- Vídeo: antes de entregar, faça a revisão de 5 quadros com nota.
- Quando o Nei corrigir algo visual, acrescente **uma linha** em `memoria/correcoes.md` (data + regra) antes de continuar.

## O que este kit NÃO é

- Não substitui as skills (`projetos-landing-guia`, `formato-curso-v*`, `makeshorts`, `reel-edita-inema`, explicavideos v2). Elas continuam donas do código e dos modelos; o kit é a fonte das regras que elas devem ler.
- Não autoriza API nem render pago. Regras de crédito e assinatura continuam nas instruções globais.
