# Prompts

Prompts are organized by model/tool family.

| Folder | Contents |
|--------|----------|
| `claude/` | Prompts and system prompts for Claude (Anthropic) |
| `general/` | Model-agnostic prompts that work across LLMs |

## File format

Each prompt is a plain `.md` file.

Files follow this structure:

```
# Prompt Name

**Use case:** One-line description of what this prompt does.
**Works with:** Claude 3+ / GPT-4+ / any LLM

---

[SYSTEM or USER prompt text begins here]
```

Placeholders for values you need to fill in are written as `[YOUR VALUE]` in all caps.
