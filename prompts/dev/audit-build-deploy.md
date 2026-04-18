# Audit Build and Deploy Pipeline

**Use case:** End-to-end audit of a web app's build and deploy pipeline before or after launch.
**Works with:** Claude (any version)

---

Audit the build and deploy pipeline for [YOUR APP NAME] end-to-end.

Check:
- `netlify.toml` (or equivalent deploy config)
- Service worker (`sw.js`)
- `manifest.json`
- Build scripts and content generation files
- Serverless functions (e.g., `netlify/functions/`)

Flag:
- Broken file paths
- Cache-busting issues
- Missing or misconfigured response headers
- CSP (Content Security Policy) gaps
- Stale service worker logic that could serve outdated content
- Environment variables referenced in code but not documented

Output: a punch list grouped **Critical / Should-fix / Nice-to-have**.

Stack context: [DESCRIBE YOUR STACK — e.g., Netlify + vanilla JS + PWA / Vercel + Next.js / etc.]
