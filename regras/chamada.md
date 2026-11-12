# Chamada: clareza + atenção (vídeo, reel, guia, portal, Telegram)

Decisão do Nei, 12/11/2026 (D20): "não adianta ele estar claro e correto se não chama atenção, não mexe na dor ou desejo".
Caso que gerou a regra: vídeo "escrita-e-engenharia" (lives3, 12/11). Mostrou o inventário do kit ("8 frases", "um dono para
cada coisa", "número sensível com nome") e a pessoa só entendia a importância no fim. O nome do método ("prompt com prova")
não foi dito nenhuma vez, e o vídeo abriu com "Imagina…" e "Neste vídeo…", que `texto.md` já proibia.

A chamada é tudo que a pessoa vê primeiro: 1ª frase da fala, manchete do quadro 0, texto da capa/thumb, título do YouTube,
título do tópico no Telegram, card do portal, legenda do IG/TikTok, H1 + lead do guia. **Todas saem da mesma mensagem-núcleo.**

## 1. O bloco CHAMADA (vem antes do roteiro, em todo brief/ficha)

| Campo | O que é | Exemplo (escrita-e-engenharia) |
|---|---|---|
| `dor_ou_desejo` | `dor` ou `desejo`: o que mexe com a pessoa | dor |
| `quem` | a pessoa, em "você" | você, que pede coisa para a IA ou monta agente |
| `nucleo` | uma frase: o que a pessoa ganha ou deixa de perder, em língua de gente | "Seu agente nunca mais diz 'pronto' sem prova." |
| `por_que_importa` | o que custa hoje, concreto, sem número inventado | "Ele diz 'agendado', o cliente chega e não tem horário." |
| `metodo` | nome do método/kit **quando o vídeo entrega um**; `null` em notícia, tese, opinião | "prompt com prova" |
| `formato` | o gatilho da abertura (tabela da seção 2) | acusacao |

Sem esse bloco, o motor não escreve o roteiro. Se o pedido não traz a dor nem o desejo, quem monta o brief propõe um e segue
(o Nei corrige depois); nunca troca a dor pelo inventário do que foi feito.

## 2. Formatos de gatilho (escolha um por peça; peças diferentes podem usar formatos diferentes)

| Formato | Como abre | Exemplo |
|---|---|---|
| `acusacao` | revela o que está acontecendo com a pessoa | "Seu agente mente pra você. Diz que fez e não fez." |
| `promessa` | o ganho, com a garantia verdadeira | "O método para o seu agente nunca mais dizer 'pronto' sem prova." |
| `perda` | o que se perde (real ou hipotético) | "Ele disse 'agendado'. O cliente chegou e não tinha horário." |
| `contrario` | manda parar o que todo mundo faz | "Pare de pedir 'capriche e me avise'." |
| `numero` / `estatistica` | número com fonte, que dá medo ou espanto | "O mesmo pedido: nota zero de oito. Com uma mudança, oito de oito." |
| `pergunta` | pergunta sobre a vida da pessoa | "Quantas vezes a IA te disse 'feito' sem ter feito?" |
| `nome` | o nome do método como novidade | "Prompt com prova: o método que obriga a IA a mostrar o recibo." |
| `terceiro` / `noticia` / `provocacao` | (r7ex/rtex) história de alguém, fato da semana, afirmação que cutuca | — |

Promessa só com o que é verdade medida. "Nunca deixa de fazer" é promessa que o kit não cumpre; "nunca mais diz pronto sem
prova" é.

## 3. Regras que valem em todo motor

1. **Primeiros 15 s (~45 palavras):** a dor ou o desejo, falado em "você". Quem assiste sabe qual é o problema e que é com ele.
2. **Método nomeado (quando houver `metodo`):** o nome é dito até ~20 s e volta pelo menos mais 1 vez (de preferência no fecho).
3. **Inventário não é chamada:** "8 frases", "9 soluções", "N técnicas" não vão no título, na manchete nem no H1. Número de FATO
   (nota 0/8 → 8/8, 47 testes) pode; contagem do que tem no kit, não.
4. **Língua de gente:** rótulo de engenharia ("um dono para cada coisa", `PRONTO:`, preflight) não entra na fala sem a frase
   comum ao lado ("só uma porta grava na agenda"). Lista falada: no máximo 3 itens; o resto "está no kit".
5. **Aberturas proibidas** (já em `texto.md`): "Imagine…", "Pense num…", "Neste vídeo…", "Hoje vamos falar…", "Você sabia…", "Eu fiz…".
6. **Teste dos 15 s (crítico/revisor):** "lendo só a chamada ou ouvindo os primeiros 15 s, um desconhecido sabe qual é o problema,
   que é com ele, por que importa, e o nome da solução (se houver)?" Não → nota baixa e `melhorar` com a chamada reescrita.

## 4. CTA (fecho): engajamento natural, sem pedir palavra nem link

Nei, 12/11/2026: "no CTA não deve pedir para a pessoa colocar palavra ou link; deve sempre criar engajamento natural e
[dizer] que o kit está disponível free no inema.club, direto na internet."

- **Proibido:** "comenta PALAVRA", "comenta X que eu te mando", "me pede o link", "link na bio", "te mando no direct",
  "está no fixado" como recompensa.
- **Obrigatório:** uma pergunta de verdade ligada à dor/desejo, que a pessoa responde com a própria opinião ou experiência
  ("E você, já foi enganado por uma IA que disse 'feito'?"), e o lugar: "o kit está grátis no inema.club, direto na internet"
  (ou "tá tudo no inema ponto club" quando não há kit). "Grátis" só se for verdade.
- Substitui o CTA fixo antigo do r7ex ("Ou me pede o link aqui nos comentários") e o "comenta PALAVRA" do explicavideo e do
  makeshorts. Peças já publicadas não mudam.

## 5. Onde cada motor aplica

| Motor | Onde | Trava |
|---|---|---|
| explicavideo | `prompts/bot-ficha.md` (bloco `chamada.json`) | `engine/v2/checar_chamada.py` antes do avatar (`bot/avatar.sh`) |
| r7ex | `PADRAO.md`, `producao/critico-plano.md`, `COMO-PEDIR.md` | `r7ex.py checar` (tipos promessa/acusacao, CTA novo) + crítico |
| rtex | `prompts/critico.md` | `rtex.py checar` (tipos promessa/acusacao) + crítico |
| refazvideo | `AGENTS.md` (re-tese da abertura) | — (pendente) |
| guia (`projetos-landing-guia`) | hero + `#resumo` | revisor |
| portal / Telegram / Metricool | título e legenda saem do `nucleo` | — |
| revisor independente | `~/.claude/runbooks/revisor-independente.md` | pergunta dos 15 s |
