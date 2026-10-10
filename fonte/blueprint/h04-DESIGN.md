---
version: alpha
name: Your Brand Name
description: One sentence. Who it is for and how it should feel.
colors:
  primary: "#111827"      # main ink: headlines and body text. Replace.
  secondary: "#6B7280"    # muted text and borders. Replace.
  tertiary: "#2563EB"     # your ONE accent: buttons and links only. Replace.
  neutral: "#F9FAFB"      # page background. Replace.
  surface: "#FFFFFF"      # cards and inputs. Replace.
  on-tertiary: "#FFFFFF"  # text that sits on the accent. Replace.
typography:
  headline-lg:
    fontFamily: Fraunces  # your headline font. Replace.
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.02em
  body-md:
    fontFamily: Inter     # your body font. Replace.
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.02em
rounded:
  sm: 4px
  md: 8px
  lg: 16px
  full: 9999px
spacing:
  sm: 8px
  md: 16px
  lg: 32px
  xl: 64px
components:
  page:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.primary}"
    typography: "{typography.body-md}"
  button-primary:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.on-tertiary}"
    typography: "{typography.label-md}"
    rounded: "{rounded.md}"
    padding: 12px
  button-primary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-tertiary}"
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    rounded: "{rounded.lg}"
    padding: 32px
  caption:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.secondary}"
    typography: "{typography.body-md}"
---

# Your Brand Name

Fill in every line. Use numbers and hex codes, never "nice" or "clean". If a brand book does not say, write TODO. Never guess.

## Overview

[Two or three sentences. Who is it for? Calm or loud? Dense or spacious? Photo, illustration or type-led? Name one real brand it should feel close to.]

## Colors

- **Primary (#111827):** Main ink. Headlines and body text.
- **Secondary (#6B7280):** Muted text, borders, captions.
- **Tertiary (#2563EB):** The only accent. Buttons and links. Nothing else.
- **Neutral (#F9FAFB):** Page background.
- **Surface (#FFFFFF):** Cards and inputs.

[Add the rule for how often the accent appears, for example: once per screen.]

## Typography

Two fonts only. **Fraunces** (600) for headlines. **Inter** (400 and 600) for everything else. Body text is 16px with lines under 75 characters. Both fonts are free for commercial use. Link: [paste your Google Fonts or Fontshare link].

## Layout

[Grid and page width, for example: 12 columns, 1120px maximum.] The spacing scale is 8, 16, 32 and 64px. Keep sections 64px apart.

## Elevation & Depth

[Shadows or flat? For example: no shadows. Depth comes from a 1px border in the secondary colour.]

## Shapes

Corners are 8px on buttons and 16px on cards. Pills (9999px) only for tags.

## Components

- **Buttons:** accent fill, label-md text, 12px padding. The hover state darkens to the primary colour.
- **Cards:** white surface, 16px corners, 32px padding.
- **Inputs:** [border, height, focus ring, error state.]

## Do's and Don'ts

- Do use the accent once per screen, on the main action.
- Do keep text contrast at 4.5:1 or better.
- Don't add a second accent colour.
- Don't use a third font.
- Don't [add one more rule your brand book shows. Copy it from the misuse page.]

## Iconography

One icon set: [Lucide]. 24px, 2px stroke, text colour. No decorative icons. Company logos come from the real mark, never drawn by hand.

## Voice

[Three words for the tone. Two real example lines from the brand. Five words to never use.]