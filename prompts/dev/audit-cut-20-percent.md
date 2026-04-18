# Identify Code to Cut (20% Reduction)

**Use case:** Find dead code, redundant modules, and safely cuttable weight without losing user-visible functionality.
**Works with:** Claude (any version)

---

If you had to cut 20% of the [YOUR APP NAME] codebase without losing any user-visible functionality, what would you cut and why?

Be specific:
- File names
- Approximate line counts
- Why the code is safe to remove (unused, duplicate, superseded, never-reachable)
- Any risk or prerequisite for each cut

Output: a ranked cut list, biggest wins first, with a confidence level (high / medium / low) per item.

Module directory: [PATH TO MODULES]
