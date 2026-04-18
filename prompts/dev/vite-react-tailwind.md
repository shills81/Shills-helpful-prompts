# Scaffold a Vite + React + Tailwind App

**Use case:** Bootstrap a new React app with Vite and Tailwind CSS. Good starting point for standalone tools, dashboards, or client-facing apps.
**Works with:** Claude (any version)

---

Scaffold a Vite + React + Tailwind CSS app for [PROJECT NAME].

- Color palette: dark theme preferred. Extend Tailwind config with custom color tokens rather than hardcoding hex values in JSX.
- Components needed: [LIST MAIN COMPONENTS]
- Data source: [HARDCODED / API / LOCAL JSON]
- Deploy target: [NETLIFY / VERCEL / GITHUB PAGES]

Start with the full file structure, then generate: vite.config.js, tailwind.config.js, main.jsx, and App.jsx.

**Notes:**
- Set base path in vite.config.js if deploying to GitHub Pages (base: '/repo-name/')
- Use Tailwind @apply sparingly — prefer utility classes in JSX
- If deploy target is Netlify, include a netlify.toml with build command and publish dir
