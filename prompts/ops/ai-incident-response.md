# AI Incident Response Runbook

**Use case:** Define what to do when an AI agent produces harmful output, gets compromised, hallucinates at scale, or causes user harm.
**Works with:** Claude (any version)

---

Write an incident response runbook for [AGENT NAME OR SYSTEM NAME].

- System description: [WHAT THE AGENT DOES AND WHO IT SERVES]
- Risk level: [LOW / MEDIUM / HIGH — e.g., HIGH if it handles money, health, or legal decisions]
- Stakeholders: [WHO NEEDS TO BE NOTIFIED IN AN INCIDENT]

The runbook must cover:

**1. Incident classification**
Define what qualifies as an incident:
- P1 (Critical): agent produces harmful, illegal, or discriminatory output at scale
- P2 (High): hallucinated data reaches users; agent takes unauthorized actions
- P3 (Medium): repeated refusal failures; significant output quality degradation
- P4 (Low): isolated incorrect output; minor formatting or tone violations

**2. Detection**
- How will incidents be detected? (user reports, automated monitoring, output sampling)
- What metrics trigger an alert? (error rate threshold, complaint volume, specific output patterns)
- Who is on call and how are they notified?

**3. Containment**
- Immediate steps to stop harm (disable agent, rate-limit, switch to fallback)
- How to preserve evidence (log exports, session captures)
- How to notify affected users

**4. Investigation**
- Root cause analysis process
- How to reproduce the failure
- Who reviews the logs and outputs

**5. Remediation**
- System prompt correction or model config change
- Retest against the failure scenario before re-enabling
- Sign-off required before returning to production

**6. Communication**
- Internal: what to tell the team and leadership
- External: what to tell affected users (if any)
- Regulatory: whether the incident requires disclosure under GDPR, AI Act, or sector regulations

**7. Post-incident review**
- What failed in the detection, containment, or design?
- What guardrail would have prevented it?
- Update the eval harness to catch this class of failure going forward

Output: a complete runbook document ready to hand to an on-call engineer.

---
