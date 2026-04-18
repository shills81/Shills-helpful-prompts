# Design a Human-in-the-Loop Escalation Framework

**Use case:** Define when and how an AI agent escalates to human review — preventing automated decisions that should have a person involved.
**Works with:** Claude (any version)

---

Design a human-in-the-loop (HITL) escalation framework for [AGENT NAME OR SYSTEM].

- Agent function: [WHAT DECISIONS OR ACTIONS DOES THE AGENT TAKE]
- Stakes: [WHAT IS THE COST OF A WRONG DECISION — financial, legal, reputational, user safety]
- Current human capacity: [HOW MANY HUMANS ARE AVAILABLE FOR REVIEW AND ON WHAT SCHEDULE]

Define escalation rules across these categories:

**1. Mandatory escalation triggers**
Specific conditions that always require human review before the agent proceeds:
- [e.g., any output affecting a financial transaction over $X]
- [e.g., any response involving mental health, legal advice, or medical information]
- [e.g., any action that is irreversible — deletes, sends, publishes]
- [e.g., any time the agent's confidence score is below threshold]

**2. Soft escalation triggers**
Conditions that flag for review but do not block the agent:
- [e.g., user expresses frustration or distress]
- [e.g., agent produces an unusually long or hedged response]
- [e.g., topic is outside the agent's normal distribution of inputs]

**3. Escalation routing**
- Who receives escalations? (specific role, queue, on-call rotation)
- What information does the reviewer receive? (full context, agent response, confidence level)
- What is the SLA for human response? (immediate / within 1 hour / next business day)
- What happens to the user while waiting? (hold message, fallback response, timeout)

**4. Reviewer interface**
- How does the human reviewer approve, reject, or modify the agent's proposed response?
- Is the reviewer's decision logged for audit purposes?
- Does the reviewer's decision feed back into agent improvement?

**5. Failure mode**
- What happens if no human is available within the SLA?
- Is there a safe default response the agent falls back to?
- How is the user notified?

Output: a complete HITL framework document with escalation rules, routing logic, reviewer interface spec, and failure mode handling.

**When HITL is non-negotiable:**
Any AI system making decisions about hiring, credit, housing, healthcare, legal status, or public safety must have human review at the decision point — not just in the audit trail afterward.

---
