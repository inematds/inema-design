# 🎨 INEMA Design

[![INEMA Design](guia/assets/banner.jpg)](https://inematds.github.io/inema-design/guia/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## O que é

O INEMA Design é uma pasta de arquivos de texto com as regras visuais do ecossistema INEMA: cores, fontes, jeito de escrever, câmera de vídeo e a lista do que o Nei já reprovou. Serve para quem cria páginas, guias, cursos, banners, explicavideos, shorts e reels com agentes como Claude Code e Codex. O agente lê a pasta antes de começar e a peça sai no padrão da marca, sem repetir erro antigo. Para usar, basta copiar a pasta e pedir ao agente que leia o CLAUDE.md dela primeiro.

## 📖 Guia de uso

Guia completo (landing + passo a passo): **https://inematds.github.io/inema-design/guia/**

## Estrutura

```
inema-design/
  CLAUDE.md                 ordem de leitura e jeito de trabalhar
  DESIGN.md                 a marca: núcleo comum + uma seção por linha (guia, curso v2/v5/v6, banner, thumb, vídeo)
  DECISOES.md               conflitos entre fontes e lacunas — o dono escolhe
  MAPA-PROJETOS.md          onde cada recurso entra em cada projeto
  regras/
    pagina-20.md            20 pontos antes de publicar página + pontos INEMA
    texto.md                texto com cara de gente (PT)
    bar.md                  modelo "o que a referência faz bem" + loop de críticos
  video/
    style.md                padrão INEMA 16:9 e 9:16 + modelo para extrair de uma referência
    camera.md               palavras de câmera com número e limites INEMA
    revisao-5-quadros.md    quadros 0/25/50/75/100% com nota de 0 a 10
  memoria/correcoes.md      tudo o que já foi reprovado, uma linha por regra
  checks/preship.py         checagem estática de HTML
  fonte/blueprint/          os arquivos originais do Claude Design Blueprint (EN)
  guia/                     esta página (PT/EN/ES)
```

## Uso rápido

```bash
git clone https://github.com/inematds/inema-design ~/projetos/inema-design
python3 ~/projetos/inema-design/checks/preship.py guia/index.html
```

E no agente: *"Leia ~/projetos/inema-design/CLAUDE.md e siga a ordem de leitura antes de criar a peça."*

## Etapas

1. **Kit base** — feito (10/10/2026). Só arquivos.
2. **Vídeo** — revisão de 5 quadros e style.md de referência no refazvideo, depois nos outros motores.
3. **Páginas e cursos** — a skill de guia e os formatos de curso passam a ler o DESIGN.md.

## Créditos

Método e arquivos de base do **Claude Design Blueprint** (compartilhado para uso livre). Checklist e lista de sinais de IA do **Power Design** e do **SlopMonster** (ItsssssJack, MIT). Formato DESIGN.md do Google Labs. Texto simples inspirado no ASD-STE100.

---
Feito por [INEMA.CLUB](https://inema.club)
