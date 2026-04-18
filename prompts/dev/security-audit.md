# Security Audit a Site or Tool

**Use case:** Audit a deployed site, API integration, or Claude-powered tool for security vulnerabilities before or after launch.
**Works with:** Claude (any version)

---

Audit [TOOL OR SITE NAME] for security vulnerabilities. Check:
1. Input validation and sanitization
2. CORS configuration
3. Content Security Policy (CSP) headers
4. Prompt injection risks (for any tool using an LLM API)
5. Hardcoded or exposed credentials
6. Dependency vulnerabilities

Output: a findings list with severity (HIGH / MEDIUM / LOW) for each issue, a hardened version of any vulnerable code, and a GitHub Actions workflow to run credential scanning on future pushes.

Here is the code or site: [PASTE CODE OR DESCRIBE THE STACK]

**What to check for LLM-powered tools specifically:**
- API keys never exposed client-side (use serverless proxy)
- User input treated as untrusted data, not as instructions
- System prompt not leakable via prompt injection
- Output validated before rendering (XSS risk if rendering HTML from AI output)
