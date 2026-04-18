# AI Regulatory Compliance Checklist

**Use case:** Map your AI system against key regulations — EU AI Act, NIST AI RMF, GDPR, and US sector-specific rules — and identify gaps before they become violations.
**Works with:** Claude (any version)

---

Assess [AI SYSTEM OR PRODUCT NAME] for regulatory compliance.

- System description: [WHAT IT DOES, WHO IT SERVES]
- Deployment region: [US / EU / GLOBAL / OTHER]
- Industry sector: [FINANCE / HEALTH / HR / LEGAL / EDUCATION / GENERAL]
- Data processed: [TYPES OF USER DATA THE SYSTEM TOUCHES]

Evaluate compliance across these frameworks:

**1. EU AI Act**
- What risk tier does this system fall into? (Unacceptable / High / Limited / Minimal)
- If High Risk: are conformity assessments, technical documentation, and human oversight requirements met?
- Is there a registered point of contact for regulatory inquiries?
- Are users notified when interacting with an AI system?

**2. NIST AI Risk Management Framework (AI RMF)**
- GOVERN: Is there an AI governance policy in place?
- MAP: Have risks been identified and documented across technical, ethical, and operational dimensions?
- MEASURE: Are there metrics and monitoring systems tracking AI performance and risk?
- MANAGE: Are mitigation plans in place and tested for identified risks?

**3. GDPR / CCPA (Data Privacy)**
- Is user data used to train or improve the model without explicit consent?
- Can users request deletion of their interaction history?
- Is there a data processing agreement with the AI vendor?
- Are automated decisions subject to human review on request?

**4. Sector-specific regulations**
- Finance (ECOA, FCRA): does the system affect credit, lending, or insurance decisions?
- Health (HIPAA): does it process protected health information?
- Employment (EEOC): does it screen, rank, or evaluate job applicants?
- Education (FERPA): does it process student records?

**5. Transparency and disclosure**
- Are users informed they are interacting with AI?
- Are AI-generated outputs labeled as such where required?
- Is there a published model card or system card?

For each framework, output:
- Compliance status: COMPLIANT / GAP IDENTIFIED / NOT APPLICABLE
- Specific gaps found
- Recommended actions to close each gap
- Priority: IMMEDIATE / BEFORE LAUNCH / ONGOING

Final output: a compliance gap report with a prioritized remediation roadmap.

---
