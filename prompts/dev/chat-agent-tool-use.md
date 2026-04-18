# Migrate Chat Agent to Native Tool Use

**Use case:** Replace a regex-based action parsing pattern in a chat agent with Anthropic's native tool_use API.
**Works with:** Claude (any version)

---

[YOUR CHAT AGENT] currently uses a regex pattern to parse action blocks from the model's text output (e.g., `<action>{"type": "update_record", ...}</action>`) and dispatches them to handler functions.

Replace this with Anthropic's native `tool_use`.

Steps:
1. Define tool schemas for each action type your agent supports (e.g., `update_record`, `add_record`, `delete_record`, `add_contact`, `log_note`)
2. Wire the `tool_use` / `tool_result` loop: send tool result back to the model, await final response
3. Keep the same handler map so existing action logic is reused
4. Preserve the user-facing confirmation UI (e.g., "Done: [what changed]")
5. Ensure existing conversations stored in `localStorage` (or equivalent) don't break

Return:
- The tool schema definitions
- The updated API call / response loop
- Migration notes for backward compatibility

Agent file: [PATH TO YOUR AGENT FILE]
Current action types: [LIST YOUR ACTION TYPES]
