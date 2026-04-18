# Add Streaming Responses to a Chat Agent

**Use case:** Refactor a chat agent from waiting for full API responses to streaming tokens as they arrive.
**Works with:** Claude (any version)

---

Refactor [YOUR CHAT AGENT FILE] to stream responses from the Anthropic Messages API (or equivalent LLM API).

Current state: [YOUR AGENT] uses a plain `XMLHttpRequest` or `fetch` call waiting for the full response before rendering anything.

Target state:
1. Implement SSE / fetch-based streaming
2. Render tokens into the message bubble as they arrive
3. Keep the typing indicator visible until the stream ends
4. Handle abort (user cancels mid-stream)
5. Preserve any action/tool-call parsing — buffer the stream, only run action handlers once the stream completes

Return:
- The code diff
- A test plan covering: normal stream, mid-stream abort, partial action block, API error mid-stream

Agent file: [PATH TO YOUR AGENT FILE]
Current API call location: [e.g., the callAPI function or equivalent]
