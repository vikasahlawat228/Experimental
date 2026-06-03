---
name: <workflow-name-kebab>
description: "<What end-to-end task this pipeline completes.>"
trigger: "<slash command or condition, e.g. /feature>"
owner: "@<owner>"
last_verified: <YYYY-MM-DD>
---

# <Workflow name>

A multi-step pipeline chaining agents/skills. Encodes the **single-threaded-writes, read/verify-sub-agents** rule from DESIGN §L4.

## Steps
1. **<Plan>** — lead agent drafts a plan (no writes yet).
2. **<Retrieve>** — call `retrieve-context` (read sub-agent).
3. **<Implement>** — lead agent makes the change (SINGLE WRITER).
4. **<Review>** — spawn a CLEAN-CONTEXT reviewer sub-agent on the diff.
5. **<Gate>** — run the eval gate (`evals/`); block if regression.

## Stop conditions
- Any "Ask first" boundary (AGENTS.md) is hit → pause for human.
- Eval gate fails → do not merge; surface the regressed cases.
