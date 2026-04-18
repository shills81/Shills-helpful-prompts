# Build a Dark-Themed Single-File HTML Tool

**Use case:** Build a self-contained, portable HTML tool or dashboard that runs without a build step. Single file, works anywhere.
**Works with:** Claude (any version)

---

Build a dark-themed [TOOL TYPE, e.g. tracker, calculator, dashboard, planner] as a single self-contained HTML file.

Color palette:
- Background: #0a0a0f
- Surface: #13131a
- Card: #1a1a25
- Border: #2a2a3a
- Accent: [YOUR ACCENT COLOR]
- Text: #e2e8f0
- Muted: #94a3b8

Font: system-ui. Mobile-first. No external dependencies unless a CDN link is acceptable.

Features needed: [LIST FEATURES]

**Guidelines:**
- All CSS and JS inline — one file, zero dependencies
- Use CSS custom properties (variables) for the color system
- Include a responsive layout that works on mobile without horizontal scroll
- If the tool stores data, use localStorage
- Avoid frameworks — vanilla JS only for portability
