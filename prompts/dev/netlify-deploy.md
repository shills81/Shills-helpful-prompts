# Deploy a Site or Function to Netlify

**Use case:** Deploy a static site, serverless function, or full-stack app to Netlify from a local directory or GitHub repo.
**Works with:** Claude (any version)

---

Deploy [PROJECT NAME] to Netlify.

- Type: [STATIC SITE / SERVERLESS FUNCTIONS / FULL-STACK]
- Source: [GITHUB REPO URL OR LOCAL DIRECTORY PATH]
- Build command: [e.g. npm run build / none for static HTML]
- Publish directory: [e.g. dist / public / . for static HTML at root]
- Environment variables needed: [LIST ANY ENV VARS]
- Custom domain: [DOMAIN OR NONE]

Output: netlify.toml config, deploy commands, and a checklist of what to set in the Netlify dashboard.

**Common patterns:**
- Static HTML with no build step: publish dir = `.`, no build command
- Vite app: build command = `npm run build`, publish dir = `dist`
- Serverless functions: add `[functions] directory = "netlify/functions"` to netlify.toml
- CORS issues: add a `_headers` file or proxy via a serverless function
