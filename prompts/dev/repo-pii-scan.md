# Scan a GitHub Repo for Exposed PII and Sensitive Data

**Use case:** Audit any public or pre-publish GitHub repository for personally identifiable information, credentials, or sensitive data before it goes live or as a routine privacy check.
**Works with:** Claude (any version with web fetch access)

---

Perform a full privacy and PII audit on the GitHub repository at [REPO URL].

Fetch and read every file in the repo. For each file, check for:

1. **Personal identifiers** — real names, email addresses, phone numbers, physical addresses, usernames tied to real identities, social media handles
2. **Third-party PII** — names, contact info, or identifying details about clients, colleagues, or other individuals who have not consented to public exposure
3. **Credentials and secrets** — API keys, tokens, passwords, auth headers, private environment variables
4. **Financial data** — account numbers, revenue figures, pricing tied to specific clients, payment details
5. **Private links** — internal Notion, Google Docs, Slack, or other workspace URLs that expose private systems
6. **Business-sensitive data** — client names, contract terms, internal tool names, private subdomains or endpoints
7. **Filesystem paths** — local paths that reveal personal directory structures, custom tool names, or internal infrastructure

For each file, output one of:
- **CLEAN** — no sensitive data found
- **FINDING** — with: file name, line or section, what was found, severity (HIGH / MEDIUM / LOW), and a recommended fix

At the end, provide:
- Overall verdict (Clean / Minor Issues / Action Required)
- A prioritized action list for any findings
- Confirmation that no credentials or API keys were found

**Severity guide:**

HIGH — live credentials, API keys, or tokens in any file; real names or contact info for individuals who did not consent to public exposure; client-identifying data tied to real business relationships

MEDIUM — personal subdomains or endpoints tied to identifiable individuals; filesystem paths revealing private tooling or infrastructure names; private workspace links (Notion, Slack, etc.)

LOW — GitHub username attribution in LICENSE or README (expected on public repos); generic placeholder text that resembles a name or email

---
