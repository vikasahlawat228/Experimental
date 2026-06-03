---
id: <kebab-case-unique-id>
type: gotcha
severity: <low | medium | high>
area: "<area matching index.md>"
owner: "@<owner>"
trigger: "<when the agent is about to do X>"
last_verified: <YYYY-MM-DD>
eval_task: <evals/tasks/<id>.yaml or "none">
---

# <Short title of the trap>

**The trap:** <what goes wrong, in 1–3 lines.>

**The rule:** <what to do instead, in 1–2 lines.>

> Keep ≤8 lines total. A gotcha is only worth keeping if it is NON-INFERABLE from the code and HIGH-SIGNAL. If you can, add an `eval_task` that locks it in — then the test guards it and this note can age more slowly.
