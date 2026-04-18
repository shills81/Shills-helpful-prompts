# Design a Chat Agent Memory System

**Use case:** Replace a simple rolling-window history with a proper tiered memory system: recency, compression, and pinned notes.
**Works with:** Claude (any version)

---

[YOUR CHAT AGENT] currently caps history at N messages in `localStorage` and trims the oldest when full.

Design a proper memory system with three tiers:

1. **Rolling window** — last N messages for recency (verbatim, always in context)
2. **Summarized long-term memory** — compressed summary of older conversation, updated every M turns
3. **Pinned notes** — per-topic notes the user can explicitly lock (e.g., "remember this")
4. **"Remember this" command** — user-invocable shortcut to pin the current context

For each tier, specify:
- The data model (schema)
- Where it's stored (`localStorage`, `IndexedDB`, or server — and why)
- How it's injected into the system prompt
- The compression strategy for tier 2 (prompt the model to summarize? rule-based? hybrid?)
- Storage size estimates and limits

Also define:
- How to handle `localStorage` quota limits
- What happens on first load vs. returning user
- The minimum code changes to [YOUR AGENT FILE]

Agent file: [PATH TO YOUR AGENT FILE]
Current history cap: [e.g., 40 messages]
