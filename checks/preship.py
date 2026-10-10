#!/usr/bin/env python3
"""preship.py (fonte: Claude Design Blueprint, hack 15 / Power Design, MIT): static checks for one HTML file. Python 3 only, no installs.
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
