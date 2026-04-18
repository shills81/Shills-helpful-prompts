# Design a Multi-Agent Workflow

**Use case:** Design the architecture for a system where multiple AI agents work together on a complex task.
**Works with:** Claude (any version)

---

Design a multi-agent workflow for [DESCRIBE THE OVERALL TASK].

- Agents needed: [LIST EACH AGENT WITH ITS ROLE]
- Orchestration pattern: [SEQUENTIAL / PARALLEL / HIERARCHICAL]
- Data flow: describe what each agent receives as input and produces as output
- Failure handling: what happens if one agent fails or returns an unexpected result
- Tools each agent needs: [LIST PER AGENT]

Output: a workflow diagram description, then the implementation plan in order of what to build first.

**Orchestration patterns:**
- Sequential: Agent A → Agent B → Agent C. Simple, easy to debug. Best when each step depends on the previous.
- Parallel: multiple agents run simultaneously, results merged. Best for independent subtasks.
- Hierarchical: an orchestrator agent delegates to specialist agents. Best for complex tasks with variable paths.

**Key design rule:**
Define the input/output contract (schema) for each agent before building any of them. Mismatched expectations between agents are the most common failure mode.
