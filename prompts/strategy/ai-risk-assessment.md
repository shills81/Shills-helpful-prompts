# AI Model Risk Assessment

**Use case:** Evaluate and document the risk profile of an AI system before deployment — covering technical, operational, legal, and ethical dimensions.
**Works with:** Claude (any version)

---

Perform a risk assessment for [AI SYSTEM OR AGENT NAME].

- System description: [WHAT IT DOES, WHO IT SERVES, WHAT DATA IT USES]
- Deployment context: [INTERNAL TOOL / CUSTOMER-FACING / AUTOMATED PIPELINE / HIGH-STAKES DECISION MAKING]
- Model used: [e.g., Claude Sonnet, GPT-4, fine-tuned open-source model]

Assess risk across these dimensions:

**1. Technical risk**
- Hallucination rate: how likely is the model to produce false information in this context?
- Robustness: how does it perform on edge cases, unusual inputs, or adversarial prompts?
- Latency and reliability: what happens if the model is slow or unavailable?
- Dependency risk: what breaks if the underlying API changes or is deprecated?

**2. Operational risk**
- What is the blast radius if the system fails silently?
- Is there a human fallback if the agent produces a bad output?
- How will failures be detected — and how quickly?
- What is the cost exposure if usage spikes unexpectedly?

**3. Legal and regulatory risk**
- Does the use case touch regulated domains? (finance, health, legal, HR, credit)
- Which regulations apply? (GDPR, CCPA, EU AI Act, HIPAA, ECOA, others)
- Who is liable if the system causes harm to a user?
- Are AI-generated outputs subject to disclosure requirements?

**4. Ethical risk**
- Could this system produce outputs that disadvantage protected groups?
- Does it handle sensitive topics (mental health, immigration, criminal history)?
- Is there potential for misuse by bad actors?
- Does it respect user autonomy or create dependency?

**5. Reputational risk**
- If this system fails publicly, what is the impact on brand trust?
- Is there a scenario where a screenshot of its output goes viral for the wrong reasons?

For each dimension, output:
- Risk level: LOW / MEDIUM / HIGH / CRITICAL
- Specific risk factors identified
- Recommended mitigations
- Residual risk after mitigations are applied

Final output: a one-page risk summary suitable for a leadership review, plus a detailed appendix.

---
