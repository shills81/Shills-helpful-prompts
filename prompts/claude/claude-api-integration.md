# Build a Claude API Integration

**Use case:** Integrate the Anthropic Claude API into a Node.js, Python, or browser-based application.
**Works with:** Claude (any version)

---

Build a [NODE.JS / PYTHON / BROWSER] integration with the Anthropic Claude API.

- Model: [claude-sonnet-4-6 for quality tasks / claude-haiku-4-5 for speed and high-volume tasks]
- Task: [DESCRIBE WHAT THE AI SHOULD DO]
- System prompt: [PASTE OR DESCRIBE]
- Input: [DESCRIBE THE USER MESSAGE FORMAT]
- Output: [DESCRIBE HOW TO HANDLE AND DISPLAY THE RESPONSE]
- Include error handling and basic rate limit awareness

**Guidelines:**
- Never expose the API key client-side — use a serverless function as proxy for browser apps
- Stream responses (`stream: true`) for better UX on long outputs
- Use claude-haiku-4-5 for high-volume or low-stakes tasks to control cost
- Use claude-sonnet-4-6 for quality-critical outputs
- Include a system prompt — it significantly improves output quality and consistency
- Handle the most common errors: 401 (bad key), 429 (rate limit), 529 (overloaded)
