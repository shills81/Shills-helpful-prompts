# Audit Load and Runtime Performance

**Use case:** Find the highest-ROI performance improvements for a web app — covering first-load and runtime rendering.
**Works with:** Claude (any version)

---

## Part A — Load Performance

Evaluate first-load performance of [YOUR APP NAME].

Check:
- Script tags blocking render in HTML entry files
- Total JS bundle size shipped on first load
- Large inline data files (e.g., content arrays hardcoded in JS)
- Image sizes and formats
- Service worker precache footprint

Output: the three highest-ROI optimizations, each with the file to change and expected impact.

Entry files: [e.g., index.html, dashboard.html]

---

## Part B — Runtime Performance

Find render-heavy modules (e.g., list views, grids, data tables).

Flag:
- O(n²) loops over large lists
- Full re-renders triggered by every keystroke or event
- Uncached DOM queries inside loops
- Event listeners not cleaned up when modules unmount

Output: specific findings with file:line citations, ranked by impact.

Module directory: [PATH TO MODULES]
