# Poster in code: starter
One HTML file that draws a true-size print poster, with bleed and safe-zone guides. It prints to a one-page vector PDF.
Tested 5 Oct 2026 in Chrome 154: one page, about 426 x 600 mm (A2 with 3 mm bleed), fonts embedded, no raster images.

## 1. The starter prompt
Paste this into Claude Code or Claude Design. Save poster.html (section 2) in the folder first.

```
Make a poster in code. Use poster.html in this folder as the base. Do not change the sheet, bleed or safe-zone setup.
Subject: [what the poster is for].
Facts: [title, date, place, one line]. Use only these facts. Invent nothing else.
Style: [one reference image or link, or three plain words].
Rules: draw in HTML, CSS and inline SVG only. Size everything in mm. Art may run into the bleed. Text stays inside the safe margin. One big thing to look at first. Two typefaces at most.
Show me a small preview first. Then press G to show the guides and check them. Then export the PDF.
```

## 2. poster.html
Open it in a browser. Press G to show the guides: red is the trim line, blue is the safe line. The guides never print.
For another size, change --trim-w, --trim-h and the @page line. The @page line cannot read variables.

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Poster starter</title>
<style>
/* A2 portrait: 420 x 594 mm trim, 3 mm bleed, 6 mm safe margin.
   Another size? Change --trim-w, --trim-h, and the @page line (it cannot read variables). */
:root { --trim-w: 420mm; --trim-h: 594mm; --bleed: 3mm; --safe: 6mm; --paper: #f3efe6; --ink: #151515; --accent: #e5532d; }
@page { size: 426mm 600mm; margin: 0; }          /* trim + 2 x bleed */

* { box-sizing: border-box; margin: 0; padding: 0; }
html, body { background: #2a2a2c; }
body { font-family: "Helvetica Neue", Arial, sans-serif; color: var(--ink); }

/* The sheet is the full file: trim size plus bleed on every side. */
.sheet { position: relative; overflow: hidden; background: var(--paper);
  width: calc(var(--trim-w) + 2 * var(--bleed)); height: calc(var(--trim-h) + 2 * var(--bleed)); }

/* Art goes here. It may run all the way to the edge of the sheet, so it bleeds. */
.art { position: absolute; inset: 0; }
.art .disc { position: absolute; width: 300mm; height: 300mm; border-radius: 50%; background: var(--accent);
  right: -60mm; top: 250mm; }

/* Text goes here. It stays inside the safe margin, so nothing is cut at the trim. */
.safe { position: absolute; inset: calc(var(--bleed) + var(--safe)); display: flex; flex-direction: column; }
h1 { font-size: 74mm; line-height: .86; letter-spacing: -.02em; font-weight: 800; }
.line { font-size: 12mm; line-height: 1.15; max-width: 250mm; margin-top: 12mm; }
.facts { margin-top: auto; display: grid; grid-template-columns: repeat(3, 1fr); gap: 8mm; font-size: 6.5mm; line-height: 1.3; border-top: .6mm solid var(--ink); padding-top: 5mm; }
.facts b { display: block; font-size: 4.2mm; letter-spacing: .08em; text-transform: uppercase; opacity: .65; }

/* Guides: add ?guides to the address, or press G. They never print. */
.guides::before, .guides::after { content: ""; position: absolute; pointer-events: none; z-index: 5; }
.guides::before { inset: var(--bleed); outline: .4mm dashed #e11; }                          /* trim line */
.guides::after  { inset: calc(var(--bleed) + var(--safe)); outline: .4mm dashed #19c; }      /* safe line */

/* On screen, shrink the sheet to fit the window. */
@media screen { .sheet { zoom: var(--fit, .35); margin: 0 auto; } }
@media print  { html, body { background: none; } .guides::before, .guides::after { display: none; } }
</style>
</head>
<body>
<main class="sheet" id="sheet">
  <div class="art"><div class="disc"></div></div>
  <div class="safe">
    <h1>Your<br>title<br>here</h1>
    <p class="line">One line that says what this poster is for.</p>
    <div class="facts">
      <div><b>When</b>[Date and time]</div>
      <div><b>Where</b>[Place]</div>
      <div><b>More</b>[Web address]</div>
    </div>
  </div>
</main>
<script>
const sheet = document.getElementById('sheet');
const fit = () => {
  // Measure the sheet at full size, then scale it to fit the window. Works for any poster size.
  sheet.style.setProperty('--fit', 1);
  const r = sheet.getBoundingClientRect();
  sheet.style.setProperty('--fit', Math.min(1, (innerWidth - 32) / r.width, (innerHeight - 32) / r.height));
};
addEventListener('resize', fit); fit();
if (location.search.includes('guides')) sheet.classList.add('guides');
addEventListener('keydown', e => { if (e.key.toLowerCase() === 'g') sheet.classList.toggle('guides'); });
</script>
</body>
</html>
```

## 3. Export
Mac, with Chrome installed:

```
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --no-pdf-header-footer --print-to-pdf=poster.pdf poster.html
```

Optional: a 300 dpi PNG from the PDF. It needs poppler (brew install poppler).

```
pdftoppm -r 300 -png -singlefile poster.pdf poster
```

The PDF page can be about 0.1 mm wider than the sheet. That sliver sits inside the bleed and is cut off.
Send the PDF to the printer. Use the PNG for a preview or a social post. Make the social crop separately: see poster-sizes-and-bleed.md.