# Design an AI Agent Audit Trail

**Use case:** Make every action an AI agent takes auditable — who asked, what ran, what changed, and how to undo it.
**Works with:** Claude (any version)

---

Every action [YOUR CHAT AGENT NAME] takes should be auditable. Design the audit trail.

**Per-action log entry should capture:**
- Timestamp
- User / session identifier
- The user's message that triggered the action
- The model's response (verbatim or summarized)
- The tool or action that ran (name, parameters)
- The state change it produced (before / after or delta)
- Undo payload (enough to reverse the change)

**Return:**

1. **Data model** — full schema for one audit log entry
2. **Storage** — where it's stored (localStorage, IndexedDB, server DB) and the storage budget calculation
3. **Retention policy** — how many entries to keep, when to prune
4. **Admin UI wireframe** (text-based) — how a workspace admin inspects, filters, and reverses actions
5. **Undo flow** — how a user triggers an undo from the chat, and what the agent does in response

Agent: [YOUR CHAT AGENT NAME]
Action types: [LIST YOUR ACTION TYPES — e.g., update_record, add_contact, log_note]
Platform: [e.g., browser-only / browser + server]
