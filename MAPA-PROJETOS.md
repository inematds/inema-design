# Onde o kit entra em cada projeto

Levantamento só de leitura em 10/10/2026 (README, CLAUDE.md, FALHAS.md e trechos do código). Nada foi alterado nos projetos.

Recursos: **(a)** DESIGN.md lido antes · **(b)** style.md tirado de referência · **(c)** revisão de 5 quadros com nota · **(d)** imagens paradas aprovadas antes do render · **(e)** câmera com número · **(f)** texto sem cara de IA · **(g)** capa/pôster a partir de referência · **(h)** três críticos em loop.

Panorama: nenhum dos projetos tem DESIGN.md, style.md de referência, nota por quadro nem crítico estético. O QA existente é técnico ou factual, e as cores estão fixas no código de cada motor.

Ordem sugerida (do menor para o maior risco): (f) e (a) → (c) só gravando nota → (e) → (d) e (h) com portão humano, só nos manuais.

## Páginas, guias e cursos
| Onde | Encaixe |
|---|---|
| projetos-landing-guia | (a) linha "Guia" do DESIGN.md · `regras/pagina-20.md` + `checks/preship.py` antes do push · (f) no `#resumo` · (h) opcional na hero |
| formato-curso v2/v5/v6 | (a) cada linha já tem tokens; a skill passa a apontar para o DESIGN.md · (f) `regras/texto.md` nas aulas · pontos 1–20 na landing |
| banners (gerar-banner) e thumbviral | (a) linhas Banner/Thumb · (g) pôster a partir de UMA referência · conferir texto da arte |

## Vídeo
### refazvideo (manual, playbook com portão humano) — melhor encaixe para tudo
- (b) Passo 2 já baixa a referência e tira a folha de quadros: gerar `style.md` ali (`ferramentas/extrair_frames.sh`).
- (d) Passo 5 (prévia/storyboard para o dono) é o portão: incluir a imagem do `hook`.
- (c) Passo 11 (folha de 11 quadros) vira revisão com nota; refazer < 8 antes da entrega.
- (e) `visual/pt-bNN.json` usa o vocabulário de `video/camera.md`; `validar_visual.py` pode checar zoom ≤ 1,25.
- (f) Passo 4 (roteiro) e (h) roteiro + storyboard antes de gastar HeyGen.

### docflow (manual)
- (b) `docs/estilos-referencia.md` já é um style feito à mão de 4 referências (corte médio 4,4s, gancho com data+número+paradoxo). Virar `temas/<tema>.style.md` lido por `cmd_roteiro` e `motores/historia.py`.
- (e) Os 5 movimentos fixos de `motores/reais.py` viram câmera com número (push 8% em 3s, hold 1,5s, ease out).
- (d) Imagens do gancho e gráficos aprovados entre `cmd_gerar` e `cmd_montar`. (c) Depois de `cmd_montar`, antes de publicar.
- (a) `temas/DESIGN.md` com a "identidade fixa" que o próprio estilos-referencia diz faltar.

### reelcomenta (sob demanda)
- (f) Lint da `fala` no `roteiro.yaml` antes de `cmd_avatar` (que gasta estúdio HeyGen) — melhor retorno.
- (c) Ampliar `cmd_conferir` para 5 quadros com nota; refazer é barato (`montar`, sem HeyGen).
- (d) `cmd_previa` já é o portão; incluir recorte do avatar e a cena `lento`.
- (a) Tirar AMB/VERM/BRANCO/fontes do topo do `.py` para o DESIGN.md. (b)/(g) a folha de 12 quadros do reel original já existe.

### cardshorts (CLI, motor de outros)
- (a) Mais pronto do grupo: `estilos/comum.css` + 5 estilos já são tokens; o DESIGN.md só resume.
- (d) `cards` gera `previa.png`; falta o portão "aprovado" antes de `montar`.
- (c) 5 quadros do MP4 final. (f) lint das falas em `carregar()`.

### eventosextremospub (manual)
- (a) Paleta de `motor/mapa.html` + regra do quadro 0 (data + número com fonte) num arquivo.
- (c) `render.mjs --quadros 0,10,30` → trocar por 0/25/50/75/100% com nota; peso alto no quadro 0.
- (f) Lint de `falas.json` antes de `narrar.py` (tom "tu", ano por extenso). (e) zoom/pan do deck.gl com número em `gerar_cena.py`.

### finviral (AUTOMÁTICO às 02:00, publica sozinho) — cuidado
- (f) Melhor e mais seguro: regras de `regras/texto.md` no prompt `auto/roteiro.md` e em `auto/checar.py` (que já corrige 1 vez). Começa como aviso no log.
- (a) `motor/DESIGN.md` espelhando o `:root` do `palco.html`, só documentação.
- (c) Só grava nota em log e avisa no bot v3. Nunca bloqueia nem refaz sozinho.
- (d) e (h): NÃO no timer.
- Regra: tudo atrás de flag opt-in (ex.: `FINVIRAL_QA=1`), testado com `SEM_BOT=1 SEM_AVATAR=1`; nunca editar `.sh` em execução.

## Problemas repetidos em vários projetos
- Texto acentuado cortado no drawtext e `%` sumindo (docflow, eventosextremospub).
- Voz do HeyGen a −26 dB (finviral, eventosextremospub).
- Whisper errando número/nome na conferência (finviral, cardshorts, eventosextremospub).
Um QA compartilhado resolveria melhor que correções copiadas.
