# Promotion checklist

Paste into any PR that changes the shared agent layer (`AGENTS.md`, `knowledge/`, `.agents/`, `evals/`). A curator ticks these before merge (RULES.md §R5).

## For every change
- [ ] **Single source of truth:** no content duplicated from elsewhere; tool files still symlink/import `AGENTS.md` (R2).
- [ ] **Org-sync:** does not add a team-local alternative to an org tool/standard (R3).
- [ ] **Size/bloat:** passes the litmus test — non-inferable + high-signal; `AGENTS.md` still < ~200 lines (R7).
- [ ] **Freshness fields:** new pointers/gotchas/skills have `owner` + `last_verified` (schema.md).

## If it changes behavior (skill / workflow / AGENTS.md)
- [ ] **Eval gate green:** CI capability + regression passed; no metric below baseline beyond tolerance (ci-gate.md).
- [ ] **Transcript read:** reviewer read ≥1 run and confirms the score is real, not a grader artifact (R5).
- [ ] **Clean-context review:** for code-affecting changes, an independent reviewer looked at it.

## If it changes `evals/` (tasks or rubric)
- [ ] **Two human approvers** (never the agent) and a one-line rationale (R4 — anti-drift).
- [ ] Not weakening a check just to make current behavior pass.

## If it came from feedback
- [ ] Promoted on **correctness**, not popularity (R6).
- [ ] Recurring bug also captured as an **eval task** so it can't regress.

Merged changes are versioned; a bad promotion is reverted in one PR.
