# Fix or Debug a Deployed Tool

**Use case:** Diagnose and fix a broken deployed tool or site. Covers common deployment issues: CORS, API errors, environment variables, and syntax bugs.
**Works with:** Claude (any version)

---

The [TOOL NAME] is broken. Error: [DESCRIBE THE ERROR OR PASTE IT]. Deployed on [NETLIFY / VERCEL / GITHUB PAGES / OTHER]. The issue is likely [CORS / API RESPONSE FORMAT / ENV VARIABLE / SYNTAX]. Here's the relevant code: [PASTE].

**Common issues this covers:**
- CORS errors on API calls from deployed frontends (fix: Netlify serverless proxy)
- API key not available in production (fix: environment variable in hosting dashboard)
- localStorage blocked in sandboxed environments (fix: in-memory fallback)
- Build succeeds locally but fails on deploy (fix: check build command and publish dir)
