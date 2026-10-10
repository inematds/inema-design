# Type and icons block for DESIGN.md
Two parts go into your DESIGN.md. The third part is for you. Swap the names for yours. Keep the rules.

## Part 1: tokens (top of the file, replace the typography: group)
```yaml
typography:
  headline-lg:
    fontFamily: Fraunces
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.02em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.02em
```

## Part 2: words (replace the Typography section, then add or replace Iconography)
```md
## Typography

Two fonts only. Both are free for commercial use.

- **Headlines:** Fraunces 600.
- **Body and labels:** Inter 400 and 600.
- Body is 16px with a 1.6 line height. Lines stay under 75 characters.
- Use no more than three weights anywhere.
- Load both with one link: <link href="https://fonts.googleapis.com/css2?family=Fraunces:wght@600&family=Inter:wght@400;600&display=swap" rel="stylesheet">
- Set --font-head (Fraunces) and --font-body (Inter) once. Never write a font name anywhere else.
- If the link does not load in the preview, say so. Never swap in a system font without telling me.

## Iconography

- One icon set: Lucide. 24px, 2px stroke. Icons take the text colour.
- Load it with <script src="https://unpkg.com/lucide@latest"></script>. Write <i data-lucide="rocket"></i>. Call lucide.createIcons() once.
- Company logos: Simple Icons, https://cdn.simpleicons.org/NAME/HEX. For AI companies: Lobe Icons, https://unpkg.com/@lobehub/icons-static-svg@latest/icons/NAME.svg
- Never draw a logo by hand. If neither source has it, write the company name as plain text and tell me.
- No decorative icons. No sparkles. Every icon sits next to visible text or has an aria-label.
- If the preview blocks the script, paste the SVG markup inline. Same set, same size.
```

## Part 3: where each one comes from (for you, not for Claude)
Checked 5 Oct 2026. Read the licence line before you ship.

Fonts
- Google Fonts, https://fonts.google.com . Free for commercial use. Mostly SIL Open Font License. A few use Apache or Ubuntu licences.
- Fontshare, https://www.fontshare.com . Free for personal and commercial use. Licence v2.0 (17 Aug 2026) lets you self-host on your own sites. You may not edit, subset or convert the files. Never hand the files to other people.
- Google Fonts MCP (pairings), https://github.com/sliday/google-fonts-skill . MIT. 73 pairings. Small project (16 stars), so read the code first.
- Fonts In Use, https://fontsinuse.com . Real fonts in real work. Nothing to download. Check each font's licence.
- Typewolf, https://www.typewolf.com/google-fonts . The 40 best free Google Fonts, with real sites using each. Nothing to download.

Icons
- Lucide, https://lucide.dev . ISC licence. About 150 icons from Feather are MIT. Keep the licence notice if you copy the source.
- Phosphor, https://phosphoricons.com . MIT. Six weights, so you change the feel by changing one weight.
- Iconify, https://iconify.design . Search many open icon sets at once. Each set has its own licence. Read it on the set page.
- Simple Icons, https://simpleicons.org . Real brand logos. The collection is CC0. Brands keep their trademarks. It has no OpenAI, LinkedIn, Microsoft or Slack mark today.
- Lobe Icons, https://icons.lobehub.com . Logos for AI companies, including OpenAI and Claude. The package is MIT. The logos stay trademarks of their owners.

Before you ship, pin the Lucide version: https://unpkg.com/lucide@1.52.0