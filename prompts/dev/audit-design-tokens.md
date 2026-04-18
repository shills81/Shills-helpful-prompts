# Audit Design System and Tokens

**Use case:** Extract the design tokens actually in use, find hardcoded values that should be tokens, and report inconsistencies.
**Works with:** Claude (any version)

---

Review the CSS files for [YOUR APP NAME] (e.g., `css/brand.css`, `css/layout.css`).

Extract the design tokens actually in use: colors, spacing, typography, border radii, shadows.

Cross-reference against the HTML templates and inline styles in JS modules.

Report:
1. Tokens defined in CSS but never used
2. Hardcoded values in HTML/JS that should be CSS tokens
3. Inconsistent spacing or typography (same concept, different values in different places)
4. Brand or header inconsistencies across pages

Output: grouped findings with file:line citations. One recommended consolidation to run first.

CSS files: [e.g., css/brand.css, css/layout.css]
Templates: [e.g., index.html, dashboard.html]
