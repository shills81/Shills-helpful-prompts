# Audit Loading, Empty, and Error States

**Use case:** Find every module that fetches or loads data and check whether it handles all three UI states.
**Works with:** Claude (any version)

---

For every module in `js/` (or equivalent) for [YOUR APP NAME], find where it fetches or loads data.

Check whether each has an explicit:
- **Loading state** — something shown while data is in flight
- **Empty state** — something shown when the response is empty or has no records
- **Error state** — something shown when the fetch fails

Output: a table of modules × states (✓ / ✗ / partial), and the top three missing states ranked by user impact.

Module directory: [PATH TO MODULES]
