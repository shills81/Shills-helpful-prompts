# Audit Architecture vs Reality

**Use case:** Find where a codebase has drifted from its documented architecture, and identify leaky module boundaries.
**Works with:** Claude (any version)

---

Read `ARCHITECTURE.md` (or equivalent architecture doc), then read the main entry files and every module in `js/` (or equivalent module directory).

Tell me:
1. Where does the code drift from `ARCHITECTURE.md`? Cite `file:line`.
2. Which module boundaries are leaky — i.e., one module reaching into another's internals?
3. Which modules carry too much responsibility?

Output: specific findings with file:line citations, and the single highest-value refactor to run first.

App: [YOUR APP NAME]
Module directory: [PATH TO MODULES]
Architecture doc: [PATH TO ARCHITECTURE DOC]
