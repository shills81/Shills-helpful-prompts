# Audit and Harden a CLAUDE.md File

**Use case:** Review a CLAUDE.md project configuration file for security gaps, prompt injection risks, and unclear agent rules.
**Works with:** Claude (any version)

---

Review this CLAUDE.md file for security and clarity gaps. Check:

1. **Untrusted data handling** — does it explicitly state that external data (user input, web content, database content) is untrusted and must not be executed as instructions?
2. **Prompt injection guardrails** — does it define how the agent should handle attempts to override its instructions via content it reads?
3. **Tool use restrictions** — are there clear rules about which tools the agent can and cannot use autonomously?
4. **Output format rules** — does it define the expected output format to prevent unstructured or dangerous outputs?
5. **Scope boundaries** — are there clear rules about what the agent should and should not do?

For each gap found: explain the risk and suggest hardening language.

Here is the CLAUDE.md: [PASTE]

**Why this matters:**
Any agent that reads external content (databases, user submissions, scraped web pages) is a prompt injection target. The CLAUDE.md should treat all external data as untrusted by default.
