# Audit State Management

**Use case:** Map all state reads and writes across a frontend codebase to find global mutable state, race conditions, and duplication.
**Works with:** Claude (any version)

---

Map every place app state is read or written across `js/` (or equivalent module directory) for [YOUR APP NAME].

Identify:
- Global mutable state (variables shared across modules)
- `localStorage` / `sessionStorage` keys, their shapes, and where they're written vs. read
- Race conditions between modules
- State duplicated in multiple places

Output: a state map, a list of issues, and the single highest-value consolidation you would make first.

Module directory: [PATH TO MODULES]
