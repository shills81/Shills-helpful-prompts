# Add Observability to a Chat Agent

**Use case:** Instrument a chat agent with per-turn token usage, latency, cost, and error tracking — surfaced as a debug panel.
**Works with:** Claude (any version)

---

Design an observability layer for [YOUR CHAT AGENT].

Track per turn:
- Input tokens / output tokens / total tokens
- Latency (time from send to first token, time to stream complete)
- Estimated cost (based on model pricing)
- Tool-use calls (count and types)
- Error type (none / network / auth / rate-limit / content-filter)

Surface as:
- An optional debug panel (keyboard shortcut to toggle, e.g., `Shift+D`)
- A small persistent stats bar at the bottom of the chat panel (optional)

Persist:
- A 7-day rolling log (capped at N entries to stay within `localStorage` budget)
- Aggregates: total turns, total cost this week, error rate

Return:
- The log schema
- Where it's stored and the storage budget calculation
- The minimum UI (text-based description of the debug panel layout)
- The keyboard shortcut wiring

Agent file: [PATH TO YOUR AGENT FILE]
