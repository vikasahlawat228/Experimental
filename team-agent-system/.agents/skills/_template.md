---
name: <skill-name-kebab>
description: >
  <One sharp sentence. Routing depends on this — say exactly WHEN to use the skill
  and WHEN NOT to. Bad: "helps with code." Good: "Locate where a feature is implemented
  across the repo when the user names a behavior but not a file.">
inputs: "<what the caller must provide>"
outputs: "<what this returns — usually a COMPRESSED summary, not raw dumps>"
tools: [<only the tools this skill needs>]
owner: "@<owner>"
last_verified: <YYYY-MM-DD>
eval_task: <evals/tasks/<id>.yaml or "none">
---

# <Skill name>

## When to use
<Bullet the trigger conditions. Be specific; over-broad skills get mis-routed.>

## Steps
1. <Self-contained steps. Assume NO access to the parent conversation — restate any needed context.>
2. ...

## Return format
<Exactly what to hand back. Prefer a tight summary (~1–2k tokens) over raw output.>

## Guardrails
- Read-only unless explicitly a write skill.
- Stop and ask if <ambiguity condition>.

> A skill is a **candidate** until it passes its eval task + curator review (governance/RULES.md). Keep it small and single-purpose; split if it grows two jobs.
