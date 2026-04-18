# Design an AI Agent Eval Harness

**Use case:** Build a repeatable eval system for an AI chat agent — testing action dispatch, Q&A, tone, and refusals locally and in CI.
**Works with:** Claude (any version)

---

Design an eval harness for [YOUR CHAT AGENT NAME].

For each capability (action dispatch, Q&A over app data, tone, refusal/guardrails), define:
- **Fixtures** — example inputs and expected outputs
- **Pass/fail criteria** — what constitutes a pass (exact match, semantic match, contains X, does not contain Y)
- **Automation approach** — how the eval is run (script, test runner, LLM-as-judge, deterministic check)
- **Dashboard** — how results are surfaced (CLI output, HTML report, CI badge)

Return:
1. The directory layout for the eval harness
2. The first 20 evals you would write (input, expected behavior, pass criteria)
3. How to run locally vs. in CI (e.g., GitHub Actions)

Agent: [YOUR CHAT AGENT NAME]
Agent capabilities: [LIST WHAT THE AGENT CAN DO — tools, Q&A, actions]
Tech stack: [e.g., Node.js + GitHub Actions / Python + pytest / etc.]
