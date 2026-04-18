# Write a Netlify Serverless Function

**Use case:** Create a Netlify serverless function to proxy an API, handle webhooks, or keep secrets server-side.
**Works with:** Claude (any version)

---

Write a Netlify serverless function at netlify/functions/[FUNCTION NAME].js that [DESCRIBE WHAT IT DOES].

- Accepts: [GET / POST] requests with [DESCRIBE PARAMS OR BODY]
- Calls: [EXTERNAL API OR SERVICE]
- Returns: [DESCRIBE JSON RESPONSE SHAPE]
- Handle CORS with appropriate headers so it can be called from the browser

**Common use cases:**
- API proxy: keeps secret keys server-side, calls third-party API, returns result to frontend
- Webhook receiver: accepts POST from a service (Stripe, GitHub, etc.), processes payload
- Form handler: captures form submissions and forwards to email or database

**Notes:**
- Always add CORS headers (`Access-Control-Allow-Origin`, handle OPTIONS preflight)
- Test locally with `netlify dev` before deploying
- Store secrets as environment variables in the Netlify dashboard, not in code
- Function timeout is 10s on free plan, 26s on paid — keep processing lean
