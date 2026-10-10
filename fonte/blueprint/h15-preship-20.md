# Pre-ship checklist: 20 points
Twenty yes-or-no checks to run on a page before it goes live. They come from the 20 web rules in Jack's Power Design repo (principles/web-principles.md). Each point names its rule.

How to use it: paste this list under your page and ask Claude to answer yes or no for every point, with proof. Fix every no. Run it again until all 20 are yes.

1. [ ] Mobile first. The 360 px layout works with no media queries. The page shell stops at 1440 px wide. Text blocks stop at 75 characters wide. (Rule 1)
2. [ ] You tested at 320, 390, 768, 1024 and 1440 px. Nothing scrolls sideways. Every breakpoint has a visible reason. (Rule 2)
3. [ ] Type and spacing use clamp(). No raw vw units on type. Text still zooms to 200%. The viewport tag does not block zoom. (Rule 3)
4. [ ] Body text is 16 px or more. Tap targets are 44 by 44 px or more, 8 px apart. (Rule 4. 44 is Apple's size. The WCAG AA minimum is 24 by 24.)
5. [ ] One main button per screen, in the accent colour. Repeat the same button down a long page. (Rule 5)
6. [ ] The first screen says what this is, who it is for and what to do next. True on a 1366 by 768 laptop and on a 390 px phone. (Rule 6)
7. [ ] Body text is left-aligned. Nothing is justified. A hero reads in a Z, with the button at the end. (Rule 7)
8. [ ] Lines are 45 to 75 characters long. (Rule 8)
9. [ ] Body line height is 1.5 or more. Headlines are 1.0 to 1.2. (Rule 9)
10. [ ] Spacing sits on an 8-point grid. Sizes come from one scale. No odd sizes such as 13 or 27 px. (Rule 10)
11. [ ] Text contrast is 4.5 to 1, or 3 to 1 for large text. Icons and focus rings are 3 to 1. Colour never carries meaning alone. (Rule 11. WCAG 1.4.3)
12. [ ] Colours are named tokens such as --bg and --accent. No loose hex codes in the styles. Dark mode reuses the same names. (Rule 12)
13. [ ] Every button, link and field has five states: default, hover, focus, pressed and disabled. The keyboard focus ring is visible. (Rule 13)
14. [ ] Empty, loading and error states are designed. Errors sit next to the field. (Rule 14)
15. [ ] Motion runs 150 to 300 ms and eases out. Reduced motion is respected. Nothing autoplays without a pause button. (Rule 15)
16. [ ] Images and embeds have a set size, so the page does not jump while it loads. (Rule 16)
17. [ ] On a mid-range phone: LCP 2.5 s or less, INP 200 ms or less, CLS 0.1 or less. Jack's budget: hero image 200 KB, JavaScript 300 KB. (Rule 17. Core Web Vitals, measured at the 75th percentile.)
18. [ ] One h1. Real header, nav, main and footer. A skip link. The tab order matches the page. (Rule 18)
19. [ ] Forms: every field has a visible label, the right input type and an inline error. No extra fields. (Rule 19)
20. [ ] The share layer is set: title 60 characters or fewer, description 155 or fewer, a 1200 by 630 share image, a theme colour and a favicon. (Rule 20)

## What a script can check
checks/preship.py (in the design folder scaffold) tests part of points 3, 16, 18, 19 and 20. It cannot judge contrast, taste or speed. Check those by eye, with Lighthouse, or with a second agent.

## Sources
- Jack's 20 web rules: https://github.com/ItsssssJack/power-design/blob/main/principles/web-principles.md
- Core Web Vitals thresholds: https://web.dev/articles/vitals
- Text contrast (WCAG 1.4.3): https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
- Minimum target size (WCAG 2.5.8, 24 by 24 px): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- Apple's 44 by 44 point tap size: https://developer.apple.com/design/tips/