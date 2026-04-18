# Write a GitHub Actions Workflow

**Use case:** Create a CI/CD workflow for testing, deploying, or scanning a repository.
**Works with:** Claude (any version)

---

Write a GitHub Actions workflow for [REPO NAME] that [DESCRIBE WHAT IT DOES, e.g. runs tests on PR / scans for secrets on push / deploys to Netlify on merge to main].

- Trigger: [PUSH TO MAIN / PULL REQUEST / SCHEDULE / MANUAL]
- Key steps: [LIST THE STEPS]
- Secrets needed: [LIST ENV VAR NAMES — store these in GitHub repo Settings > Secrets]

**Common workflow types:**
- Secret scanning: use `gitleaks/gitleaks-action` to catch leaked credentials on every push
- Auto-deploy to Netlify: trigger on push to main, use `netlify/actions/cli`
- Run tests: trigger on PR, run `npm test` or `pytest`
- Lint and type-check: trigger on PR, run ESLint / TypeScript / Ruff

**Notes:**
- Always set `permissions: contents: read` unless the workflow needs to write
- Store all secrets in GitHub repo settings, reference as `${{ secrets.NAME }}`
- Use `actions/checkout@v4` and pin other actions to a commit SHA for security
