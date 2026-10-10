# The design folder: scaffold
A folder of design files that Claude reads at the start of every project. Copy the pattern. Fill it with your own taste.
Start small. DESIGN.md and taste/inspo.md already beat a blank chat. Add the rest one file at a time.

## 1. The tree
```
design-os/
  CLAUDE.md            What to read first, in order. Keep it short.
  DESIGN.md            Your brand: colour, type, space, shape, motion, voice, bans.
  taste/
    inspo.md           Links to pieces you admire. One line each: what to steal.
    references/        Screenshots of the real pieces you copy from.
  rules/
    web-20.md          The pre-ship 20-point checklist (preship-20.md).
    words.md           Plain English rules and banned phrases.
    bar.md             Checkable traits of the reference you must beat.
  assets/              Logos, one icon pack, fonts. Real files only.
  skills/              One folder per winning style: SKILL.md, a short PROMPT.md, a check.
  checks/
    preship.py         Runs the static checks on any HTML file.
  memory/
    corrections.md     Every fix you ask for, written as a rule.
  projects/
    [your-project]/    brief.md, drafts, final. One folder per piece.
```

## 2. Make it
Run this once, in your project folder:

```
mkdir -p design-os/{taste/references,rules,assets,skills,checks,memory,projects}
touch design-os/{CLAUDE.md,DESIGN.md} design-os/taste/inspo.md design-os/rules/{web-20.md,words.md,bar.md} design-os/memory/corrections.md
```

Copy preship-20.md into rules/web-20.md. Save the script in section 3 as checks/preship.py.

## 3. The starter files

### CLAUDE.md
```
# Read this first
Before any design work, read these files in this order.
1. DESIGN.md. It is the brand. It wins over your own taste.
2. taste/inspo.md and taste/references/. This is the taste to match.
3. rules/web-20.md, rules/words.md and rules/bar.md.
4. memory/corrections.md. These are past mistakes. Do not repeat them.

Then work like this.
- Say in six lines what you read and which rules apply.
- Never invent a colour, font, logo or icon. Use DESIGN.md and assets/ only.
- If my request clashes with DESIGN.md, stop and ask.
- Before you say done, run checks/preship.py and the 20-point list.
- When I correct you, add the fix to memory/corrections.md as one rule.
```

### DESIGN.md
```
# DESIGN.md: [brand name]
Fill every line. Use numbers and hex codes, not adjectives.

## One line
[What the brand is, and how it should feel, in one sentence.]

## Colour
- Background: #
- Text: #
- Muted text: #
- Accent (one only): #
- Border: #
- Never use: [colours the brand never shows]

## Type
- Font: [name and source link]
- Sizes: H1 [px], H2 [px], body [px]
- Weight and case:

## Space and shape
- Spacing unit: [4 or 8] px
- Corner radius: [px]
- Shadows: [none, or the one allowed]

## Buttons
- Primary: [fill, text colour, radius, one example label]
- Secondary: [style]

## Motion
- Speed: [ms] and easing: [ease-out]
- What may move: [list]
- Never: [list]

## Voice
- Plain English. Short sentences.
- Words to use: [list]
- Words never to use: [list]

## Bans (add one every time the output drifts)
1.
2.
3.
```

### taste/inspo.md
```
# inspo.md: taste, as links
One line each: the link, then what to steal. Steal the structure, never the content.
Last checked: [date]

## Websites
- [link]: [what to steal, for example the empty-state layout]

## Posters and print
- [Savee board link]: [what to steal]

## Flows (sign-up, checkout)
- [Mobbin or Refero link]: [what to steal]

## Motion
- [link]: [what to steal]

## Do not resemble
- [pieces you like but must not copy]
```

### rules/bar.md
```
# bar.md: what the reference does well
Read the reference. Write 5 to 7 traits you can check. A trait is a fact, not an adjective.
Good: the headline is 5 times the body size. Bad: it feels premium.

Reference: [link or file]
1. [trait]
2. [trait]
3. [trait]
4. [trait]
5. [trait]

After each draft, score every trait pass or fail. Our piece must pass them all.
```

### rules/words.md
```
# words.md: plain English
- Short, active sentences. One idea each.
- Small, common words. Say "use", not "utilise".
- No em dashes. No emoji.
- Use numbers and names, not adjectives.
- Banned words: seamless, unlock, elevate, effortless, cutting-edge, journey, game-changer.
- Banned shape: "not just X, but Y".
- Before you ship, run the copy through SlopMonster until it scores 5 of 5.
```

### memory/corrections.md
```
# corrections.md
One rule per fix. Add the date. Claude reads this before every project.

- Example: No sparkle or star icons. Use the icon pack in assets/.
```

### projects/[your-project]/brief.md
```
# Brief: [name]
Goal: [one sentence]
Who opens it, and on what device: [person, phone or laptop]
The one action they take next: [action]
Reference to beat: [link]
Facts allowed on the page: [list. Nothing else.]
Done when: all 20 points in rules/web-20.md pass.
```

### checks/preship.py
```python
#!/usr/bin/env python3
"""preship.py: static checks for one HTML file. Python 3 only, no installs.
Run:  python3 checks/preship.py path/to/page.html
It checks what a script can see (checklist points 3, 16, 18, 19 and 20, in part).
It cannot judge taste, contrast or speed. Do those by eye and with Lighthouse."""
import re, sys
from html.parser import HTMLParser

class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.tags = []; s.title = ''; s.in_title = False
        s.meta = {}; s.labels_for = set(); s.inputs = []; s.imgs = []; s.links = []
    def handle_starttag(s, tag, a):
        a = dict(a); s.tags.append(tag)
        if tag == 'title': s.in_title = True
        if tag == 'meta':
            k = a.get('name') or a.get('property')
            if k: s.meta[k.lower()] = a.get('content', '')
        if tag == 'label' and a.get('for'): s.labels_for.add(a['for'])
        if tag == 'input' and a.get('type', 'text') not in ('hidden', 'submit', 'button', 'checkbox', 'radio'):
            s.inputs.append(a)
        if tag == 'img': s.imgs.append(a)
        if tag == 'link': s.links.append(a)
        if tag == 'html': s.meta['_lang'] = a.get('lang', '')
    def handle_endtag(s, tag):
        if tag == 'title': s.in_title = False
    def handle_data(s, d):
        if s.in_title: s.title += d

def run(path):
    h = open(path, encoding='utf-8', errors='ignore').read()
    p = P(); p.feed(h); t = p.tags; m = p.meta
    labelled = [i for i in p.inputs if i.get('id') in p.labels_for or i.get('aria-label') or i.get('aria-labelledby')]
    viewport = m.get('viewport', '')
    checks = [
        ('18  html has a lang attribute', bool(m.get('_lang'))),
        ('18  exactly one h1', t.count('h1') == 1),
        ('18  main landmark present', 'main' in t),
        ('18  header or nav, and footer present', ('header' in t or 'nav' in t) and 'footer' in t),
        ('3   viewport meta present, zoom not blocked', 'width=device-width' in viewport and 'user-scalable=no' not in viewport and 'maximum-scale=1' not in viewport.replace(' ', '')),
        ('20  title is 1 to 60 characters', 1 <= len(p.title.strip()) <= 60),
        ('20  meta description is 1 to 155 characters', 1 <= len(m.get('description', '')) <= 155),
        ('20  og:image is set', bool(m.get('og:image'))),
        ('20  theme-color is set', bool(m.get('theme-color'))),
        ('20  favicon link is set', any('icon' in (l.get('rel') or '') for l in p.links)),
        ('16  every img has width and height', all(i.get('width') and i.get('height') for i in p.imgs)),
        ('18  every img has an alt attribute', all('alt' in i for i in p.imgs)),
        ('19  every form input has a visible label or aria-label', len(labelled) == len(p.inputs)),
    ]
    fails = 0
    for name, ok in checks:
        print(('PASS  ' if ok else 'FAIL  ') + name); fails += (not ok)
    print(f'\n{len(checks) - fails}/{len(checks)} pass')
    return fails

if __name__ == '__main__':
    if len(sys.argv) != 2: sys.exit('usage: python3 preship.py page.html')
    sys.exit(1 if run(sys.argv[1]) else 0)
```

## 4. How the pattern maps to Jack's own setup
Jack does not keep one folder with this name. His pieces live in separate skills and project folders. This scaffold puts the same layers in one place.

| Your folder | Jack's version |
|-------------|----------------|
| taste/inspo.md | References from Savee, Refero and Mobbin, plus his Five Shelves page of 40 sites |
| DESIGN.md | One brand-style.md per brand. Power Design holds 72, Glaido's included |
| rules/web-20.md | The 20 web rules in Power Design (principles/web-principles.md) |
| rules/bar.md | The teardown step of his Design Loop skill: 5 to 7 checkable traits of the reference |
| skills/ | Style skills made by Design DNA: a record, a 2 KB prompt and a check script per style |
| assets/ | His asset skill: a licensed icon library, Lottie files and a logo kit |
| rules/words.md | SlopMonster and a plain English (ASD-STE100 style) setup |
| checks/ | Check scripts that fail a build, for example the deck gate in his Horizon Strike skill |
| memory/corrections.md | His feedback notes: each correction saved as a rule, such as no sparkle icons |

Public parts: Power Design https://github.com/ItsssssJack/power-design and SlopMonster https://github.com/ItsssssJack/SlopMonster (both MIT licence).