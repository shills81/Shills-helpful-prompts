# Move Chat Agent API Key to a Server Proxy

**Use case:** Remove an LLM API key from the browser and route calls through a serverless function proxy.
**Works with:** Claude (any version)

---

[YOUR CHAT AGENT] currently stores the Anthropic API key in `localStorage` and calls the API directly from the browser using `anthropic-dangerous-direct-browser-access`. This is a critical security risk.

Design a Netlify function (or equivalent serverless) proxy to fix this.

Specify:

1. **Auth between browser and function** — how does the browser prove it's an authorized session? (session token, signed cookie, HMAC, etc.)
2. **Rate limiting** — per-user turn limits and cost ceiling enforcement at the function layer
3. **Per-user key scoping** — can users bring their own API key, or is one shared key used?
4. **Streaming passthrough** — how does the function proxy SSE streaming back to the browser?
5. **Migration path** — how do existing sessions (stored in `localStorage`) continue to work during rollout?

Return:
- The serverless function signature and implementation
- The client-side change to switch from direct browser calls to the proxy
- The environment variable setup for the server key

Agent file: [PATH TO YOUR AGENT FILE]
Current API call pattern: [e.g., direct XHR to api.anthropic.com]
Serverless platform: [e.g., Netlify Functions / Vercel Edge / Cloudflare Workers]
