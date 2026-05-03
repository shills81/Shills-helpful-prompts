# Event Poster — AI Image Generation Spec

**Use case:** Generate a photorealistic 9:16 source image for an event poster compositor
**Works with:** Midjourney, Firefly, FLUX, or any photorealistic image generator

---

## Composition Rule

One third of the frame (upper or lower) must be intentionally low-detail or flat-toned.
This zone is reserved for the event typographic wordmark in post-production.

The wordmark is purely typographic: a large title word, a condensed subtitle below.
The wordmark uses white letterforms on dark backgrounds.

Smoke and figure detail should build upward from center to the opposite third,
leaving the reserved zone clean enough for white letterforms to read clearly.

---

## Palette

Primary: Black #000000 / White #FFFFFF
Secondary near-black: #0A0A0F
Optional post-production overlays: Coral Pink #F08375, Warm Beige #E2C6BB

The source image stays achromatic grayscale.
Accent colors are applied as text and overlay tints in the compositor after generation.

---

## Emotional Register

FOMO. Joy. Momentum. Electricity.
The feeling of a night you will regret missing.
Think Coachella poster meets fine art: confident, inviting, energetic.
NOT dark. NOT superhero blockbuster. NOT threshold drama.

---

## ControlNet Guidance

Recommend a source whose existing composition contains:
- A clean shadow band or gradient fade in the upper or lower third
- A figure that builds weight toward the center, not the edges

Strength: 25 to 35 percent

---

## Hard Constraints

- 9:16 vertical
- Pure achromatic grayscale (Phase 3 sepia warmth permitted)
- Photographic realism only
- No logos embedded in the prompt text
- No stock imagery
- No hyphens or em dashes in any prompt text

---

## NFC Summit Brand Reference

Official palette:
- Primary Black: #000000 — RGB 0, 0, 0 — CMYK 0%, 0%, 0%, 100% — Pantone Black C
- Primary White: #FFFFFF — RGB 255, 255, 255 — CMYK 0%, 0%, 0%, 0% — Pantone White

Logo typography:
- "NFC" — extra-bold, condensed, all-caps, large display weight
- "NFC SUMMIT" — same weight, condensed, all-caps, set smaller below "NFC"
- Both versions: black on white and white on black
- No color variants. No gradients. No decorative elements.

Compositor inputs for NFC Summit (top to bottom):
- Header credit: [PRESENTER] × NFC SUMMIT [YEAR]
- Title line 1: NFC
- Title line 2: SUMMIT
- Date / Location: [DATE] — LISBON

---

## Prompt Template

```
[SUBJECT OR SCENE DESCRIPTION], photorealistic, achromatic grayscale, 9:16 vertical,
lower third intentionally flat and low detail for typographic overlay,
figure or focal point builds toward center and upper frame,
cinematic lighting, medium format film grain, no logos, no text
```

Replace `[SUBJECT OR SCENE DESCRIPTION]` with the mood and visual concept for your event.
Use `[YOUR EVENT]` and `[PRESENTER × EVENT YEAR]` as placeholder values when building your compositor inputs.
