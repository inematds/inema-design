# 🎨 INEMA Design

[![INEMA Design](guia/assets/banner-en.jpg)](https://inematds.github.io/inema-design/guia/en/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## What it is

INEMA Design is a folder of text files with the visual rules of the INEMA ecosystem: colors, fonts, writing style, video camera and the list of what Nei has already rejected. It is for anyone who builds pages, guides, courses, banners, explicavideos, shorts and reels with agents like Claude Code and Codex. The agent reads the folder before it starts, and the piece follows the brand standard without repeating old mistakes. To use it, copy the folder and ask the agent to read its CLAUDE.md first.

## 📖 User guide

Full guide (landing + step by step): **https://inematds.github.io/inema-design/guia/en/**

## Structure

```
inema-design/
  CLAUDE.md                 reading order and way of working
  DESIGN.md                 the brand: common core + one section per line (guide, course v2/v5/v6, banner, thumb, video)
  DECISOES.md               conflicts between sources and gaps — the owner chooses
  MAPA-PROJETOS.md          where each resource fits in each project
  regras/
    pagina-20.md            20 points before publishing a page + INEMA points
    texto.md                writing that sounds human (PT)
    bar.md                  template "what the reference does well" + critic loop
  video/
    style.md                INEMA standard 16:9 and 9:16 + template to extract from a reference
    camera.md               camera words with numbers and INEMA limits
    revisao-5-quadros.md    frames at 0/25/50/75/100% scored from 0 to 10
  memoria/correcoes.md      everything already rejected, one line per rule
  checks/preship.py         static check for HTML
  fonte/blueprint/          the original Claude Design Blueprint files (EN)
  guia/                     this page (PT/EN/ES)
```

## Quick start

```bash
git clone https://github.com/inematds/inema-design ~/projetos/inema-design
python3 ~/projetos/inema-design/checks/preship.py guia/index.html
```

And in the agent: *"Read ~/projetos/inema-design/CLAUDE.md and follow the reading order before making the piece."*

## Stages

1. **Base kit** — done (10/10/2026). Files only.
2. **Video** — 5-frame review and a reference-based style.md in refazvideo, then in the other engines.
3. **Pages and courses** — the guide skill and the course formats start reading DESIGN.md.

## Credits

Method and base files from the **Claude Design Blueprint** (shared for free use). Checklist and AI-signs list from **Power Design** and **SlopMonster** (ItsssssJack, MIT). DESIGN.md format from Google Labs. Plain writing inspired by ASD-STE100.

---
Made by [INEMA.CLUB](https://inema.club)
