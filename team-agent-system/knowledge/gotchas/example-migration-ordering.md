---
id: migration-ordering
type: gotcha
severity: high
area: "Data model / migrations"
owner: "@bob"
trigger: "editing a DB migration or a Temporal workflow definition"
last_verified: 2026-06-03
eval_task: evals/tasks/_template.yaml
---

# Migrations must not rename columns Temporal workflows replay

**The trap:** renaming/dropping a column in a migration breaks **in-flight Temporal workflow replay** (it deserializes old history against the new schema) — tests pass, prod breaks on replay hours later.

**The rule:** additive migrations only while workflows are in flight; do expand→migrate→contract across two deploys. Never collapse the steps to "save a PR."

*(Example gotcha — non-inferable from the code, high-severity, and pinned by an eval task. Replace with your real ones, captured the moment the team hits them.)*
