# Design checklist: 20 checks in five agent jobs
Source: the web rules in Jack's Power Design repo (github.com/ItsssssJack/power-design, principles/web-principles.md). Rule numbers match that file.
Each agent owns one job of four checks. Agents read the page and report. They never edit.

How to report each problem: the rule number, where it is, how bad it is (high, medium, low) and the fix in one line.

## Agent 1: Layout and phone
- [ ] 1. Mobile first. The 360px layout is the base. The page shell is 1200 to 1440px wide at most. Text columns are 75ch at most.
- [ ] 2. Breakpoints follow content. Each one exists because the layout breaks there. Test at 320, 768, 1024 and 1440px. No sideways scroll.
- [ ] 3. Fluid type and space. Sizes use clamp(). They do not jump at breakpoints.
- [ ] 4. Body text is 16px or more. Tap targets are 44 by 44px or more, with 8px between them.

## Agent 2: Type and rhythm
- [ ] 7. Scanning. Body text is left-aligned, never justified. A hero reads in a Z, with the main button where the eye ends. Headings start with the key word.
- [ ] 8. Line length is 45 to 75 characters. Text blocks use max-width: 65ch.
- [ ] 9. Line height is 1.5 or more for body text and 1.0 to 1.2 for big headings. The gap between paragraphs is 0.75em or more.
- [ ] 10. One spacing scale and one type scale. Every gap is 4, 8, 12, 16, 24, 32, 48, 64, 96 or 128px. Type sizes come from one ratio. No odd sizes such as 13px or 27px.

## Agent 3: Colour and states
- [ ] 11. Contrast. Text is 4.5:1 or more (large text 3:1). Icons, borders and focus rings are 3:1 or more. Colour is never the only signal.
- [ ] 12. Colour tokens. Components use names such as --bg, --fg and --accent, defined in OKLCH. No raw hex in components. Dark mode changes the tokens only.
- [ ] 13. Five states. Every button, link and input has default, hover, focus-visible, active and disabled. The focus ring is 2px or more and 3:1 or more.
- [ ] 14. Empty, loading and error states are designed. Loading shows a skeleton. Empty says what goes here and what to do next. An error sits next to its field and says how to fix it.

## Agent 4: Motion, speed and access
- [ ] 15. Motion takes 150 to 300ms and eases out. Reduced motion is respected. Nothing flashes more than 3 times a second. No autoplay that cannot pause.
- [ ] 16. Space is reserved. Images and embeds have width and height, or aspect-ratio. Layout shift (CLS) is under 0.1.
- [ ] 17. Speed budget on a mid-range phone. LCP under 2.5s, INP under 200ms, CLS under 0.1. Hero image 200KB or less. JavaScript 300KB or less (gzip). Two font families at most.
- [ ] 18. Structure. Real header, nav, main and footer. A skip link. One h1. No skipped heading levels. The whole page works with a keyboard only.

## Agent 5: Message and action
- [ ] 5. One main action per screen. One filled accent button per screenful, 44px tall or more. Repeat the same button down the page.
- [ ] 6. The first screen answers three questions in five seconds: what is this, who is it for, what do I do next. Check at 1366 by 768px and at 390px wide.
- [ ] 19. Forms. A visible label on every field, not only a placeholder. The right input type and autocomplete. Check each field on blur. Ask for the fewest fields.
- [ ] 20. Share layer. Title 60 characters or fewer. Description 155 or fewer. One 1200 by 630px share image. A favicon set. theme-color. JSON-LD for the main thing on the page.

## Every agent also flags
Dead buttons, broken links and leftover placeholder text. (An idea from the @Voxyz_ai post.)