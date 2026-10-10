# 🎨 INEMA Design

[![INEMA Design](guia/assets/banner-es.jpg)](https://inematds.github.io/inema-design/guia/es/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## Qué es

INEMA Design es una carpeta de archivos de texto con las reglas visuales del ecosistema INEMA: colores, fuentes, forma de escribir, cámara de video y la lista de lo que Nei ya rechazó. Sirve a quien crea páginas, guías, cursos, banners, explicavideos, shorts y reels con agentes como Claude Code y Codex. El agente lee la carpeta antes de empezar y la pieza sale con el estándar de la marca, sin repetir errores antiguos. Para usarla, basta copiar la carpeta y pedirle al agente que lea primero su CLAUDE.md.

## 📖 Guía de uso

Guía completa (landing + paso a paso): **https://inematds.github.io/inema-design/guia/es/**

## Estructura

```
inema-design/
  CLAUDE.md                 orden de lectura y forma de trabajar
  DESIGN.md                 la marca: núcleo común + una sección por línea (guía, curso v2/v5/v6, banner, thumb, video)
  DECISOES.md               conflictos entre fuentes y vacíos — el dueño elige
  MAPA-PROJETOS.md          dónde entra cada recurso en cada proyecto
  regras/
    pagina-20.md            20 puntos antes de publicar una página + puntos INEMA
    texto.md                texto con voz de persona (PT)
    bar.md                  modelo "lo que la referencia hace bien" + ciclo de críticos
  video/
    style.md                estándar INEMA 16:9 y 9:16 + modelo para extraer de una referencia
    camera.md               palabras de cámara con número y límites INEMA
    revisao-5-quadros.md    cuadros 0/25/50/75/100% con nota de 0 a 10
  memoria/correcoes.md      todo lo que ya fue rechazado, una línea por regla
  checks/preship.py         revisión estática de HTML
  fonte/blueprint/          los archivos originales del Claude Design Blueprint (EN)
  guia/                     esta página (PT/EN/ES)
```

## Uso rápido

```bash
git clone https://github.com/inematds/inema-design ~/projetos/inema-design
python3 ~/projetos/inema-design/checks/preship.py guia/index.html
```

Y en el agente: *"Lee ~/projetos/inema-design/CLAUDE.md y sigue el orden de lectura antes de crear la pieza."*

## Etapas

1. **Kit base** — listo (10/10/2026). Solo archivos.
2. **Video** — revisión de 5 cuadros y style.md de referencia en refazvideo, después en los otros motores.
3. **Páginas y cursos** — la skill de guía y los formatos de curso pasan a leer DESIGN.md.

## Créditos

Método y archivos base del **Claude Design Blueprint** (compartido para uso libre). Checklist y lista de señales de IA de **Power Design** y **SlopMonster** (ItsssssJack, MIT). Formato DESIGN.md de Google Labs. Texto simple inspirado en ASD-STE100.

---
Hecho por [INEMA.CLUB](https://inema.club)
