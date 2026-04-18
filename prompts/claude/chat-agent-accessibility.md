# Accessibility Spec for a Chat Agent

**Use case:** Define 15+ accessibility behaviors a chat agent must have to genuinely serve diverse users — beyond WCAG compliance.
**Works with:** Claude (any version)

---

Audit what a chat agent must do for accessibility to not just pass WCAG 2.1 AA but to actually delight blind, low-vision, motor-impaired, and cognitively diverse users.

Return a list of 15 behaviors [YOUR CHAT AGENT] should have that most chat agents skip. For each:
- The behavior
- The user group it serves
- Why most chat UIs get it wrong
- The implementation approach (ARIA, focus management, keyboard shortcut, etc.)

Organize by user group: screen reader users, keyboard-only users, motor-impaired, low vision, cognitive/attention.

Agent: [YOUR CHAT AGENT NAME]
Platform: [e.g., web app, mobile PWA, desktop app]
Current a11y state: [DESCRIBE WHAT EXISTS — e.g., no ARIA, no keyboard shortcuts, no focus trap]
