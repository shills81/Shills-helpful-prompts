# Build a Service Worker / PWA Manifest

**Use case:** Add offline capability and installability to a web app with a service worker and Web App Manifest.
**Works with:** Claude (any version)

---

Write a service worker (sw.js) and manifest.json for [APP NAME].

- Cache strategy: [CACHE-FIRST / NETWORK-FIRST / STALE-WHILE-REVALIDATE]
- Assets to precache: [LIST KEY FILES, e.g. index.html, styles.css, app.js]
- Theme color: [HEX]
- Icons needed: [SIZES, e.g. 192x192, 512x512]
- App should work offline for: [DESCRIBE CORE OFFLINE FEATURES]

Also include the registration snippet to add before `</body>` in the main HTML file.

**Cache strategy guide:**
- Cache-first: best for static assets that rarely change (fonts, icons, CSS)
- Network-first: best for API data where freshness matters
- Stale-while-revalidate: good middle ground — serves cache instantly, updates in background

**Notes:**
- Service workers only run on HTTPS (or localhost for dev)
- Increment the cache version name in sw.js whenever you deploy new assets
- Test offline behavior in Chrome DevTools > Application > Service Workers
