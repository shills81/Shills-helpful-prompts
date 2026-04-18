# Audit Test Coverage Gaps

**Use case:** Find where tests would pay off most — without writing any tests, just identifying the risk map.
**Works with:** Claude (any version)

---

Read the test files for [YOUR APP NAME] (e.g., `tests/run.js`, `tests/smoke.html`, `qa.js`, or equivalent).

List:
1. What is currently tested
2. What is not tested
3. The top five untested code paths ranked by risk (likelihood of breakage × user impact)

Do not write any tests — just tell me where they'd pay off most and why.

Test files: [PATH TO TEST FILES]
Module directory: [PATH TO MODULES]
