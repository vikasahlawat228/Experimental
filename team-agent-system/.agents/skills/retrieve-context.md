---
name: retrieve-context
description: >
  Locate where something lives and gather just-enough context before a change, when the
  user names a behavior/area but not exact files. Use at the START of any non-trivial task.
  Do NOT use for tasks where the file is already known.
inputs: "A feature/area/behavior description."
outputs: "A compressed brief: relevant files, the owning pointer, any ⚠ gotcha, and open questions."
tools: [read, grep, glob]
owner: "@alice"
last_verified: 2026-06-03
eval_task: none
---

# retrieve-context

## When to use
- Start of a feature/bugfix where the exact code location is unclear.
- Before editing an area flagged ⚠ in `knowledge/index.md`.

## Steps
1. Open `knowledge/index.md`; find the area row(s) matching the request.
2. Open the matching `knowledge/pointers/<id>.md`; note entry points + `source_of_truth`.
3. Check `knowledge/gotchas/` for any entry whose `trigger` matches this task.
4. Agentic-search the code (grep/glob) from the pointer's entry points to confirm current reality (don't trust a stale index).
5. Compress findings into the return brief.

## Return format
```
AREA: <name> (owner @x)
FILES: <3–6 paths that matter>
SOURCE OF TRUTH: <link>
GOTCHAS: <⚠ ids that apply, or "none">
OPEN QUESTIONS: <anything needing a human decision>
```
Keep under ~1.5k tokens. This brief is what the lead agent uses to plan — it must be tight.

## Guardrails
- Read-only. Never edit.
- If the index has no matching pointer, say so and propose adding one (don't guess silently).

*(Example skill — self-contained, single-purpose, summary-returning, sub-agent-friendly per DESIGN §L3/L4.)*
