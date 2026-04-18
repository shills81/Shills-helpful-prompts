# Full Codebase Audit (Single-Shot)

**Use case:** Comprehensive review of a web app across ten dimensions in one pass — returns findings, severity, and a prioritized action list.
**Works with:** Claude (any version)

---

Perform a comprehensive review of [YOUR APP NAME] at HEAD across ten dimensions:

1. **Build and deploy health** — netlify.toml / deploy config, service worker, manifest, build scripts
2. **Architecture vs docs** — does the code match ARCHITECTURE.md (or equivalent)?
3. **State management** — global mutable state, localStorage keys, race conditions
4. **Core flows** — first load, dashboard → module, create/edit record, [YOUR KEY FLOW], demo/onboarding
5. **Loading/empty/error states** — every data-fetching module
6. **Design system and multi-brand consistency** — CSS tokens, hardcoded values, brand presentation
7. **Accessibility** — semantic HTML, heading order, color contrast, keyboard nav, ARIA
8. **Navigation and IA** — routes/views reachable, orphaned views, deep linking
9. **Security** — secrets in code, XSS risks, CSP, CORS, localStorage PII
10. **Performance** — render blocking, bundle size, O(n²) loops, event listener leaks

For each dimension return:
- Top 3 findings with severity (Critical / High / Medium / Low)
- One `file:line` example per finding
- The single highest-ROI fix

End with a prioritized list of the **top 10 actions** ordered by impact-per-effort.

Entry files: [e.g., index.html, dashboard.html]
Module directory: [PATH TO MODULES]
Docs directory: [PATH TO DOCS]
