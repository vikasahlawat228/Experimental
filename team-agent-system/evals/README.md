# Evals — the anti-degradation engine (L6)

Evals are **the unit of progress**. They are why the system can improve without rotting: a change reaches the shared layer only by **beating the baseline** (RULES.md §R5). Without this gate, every other layer slowly decays.

## Two suites
- **Capability** — hard tasks the agent doesn't yet ace. Start low; they give a hill to climb. Track the trend.
- **Regression** — tasks the agent *should* always pass (~100%). These **block** backsliding in CI. A capability task **graduates** into the regression suite once it's reliably passing.

## Where tasks come from
- Real bugs, incidents, and review comments — the failures you actually hit.
- Every recurring agent mistake → a task (so the whole team stops hitting it).
- **Start with ~10–20 tasks.** Small sets suffice early because changes have large effects. Grow toward ~25–50 as the agent matures (research §7.1).

## How tasks are scored
- **Binary pass/fail** per check (not 1–5 scales — they're subjective and gameable). Decompose a task into several binary sub-checks to track partial progress (`rubric.md`).
- Checks are **programmatic where possible** (tests pass, file changed, command exits 0); **LLM-as-judge** only for fuzzy criteria, and then **calibrated against a human** and run with a *different* model than the generator (research §7.3).
- Each task has a known-good reference solution to prove it's solvable and the grader works.

## The non-negotiables
- **Read transcripts.** A green score nobody inspected doesn't count — graders have bugs (a real case went 42%→95% after fixing the grader, not the model).
- **Tasks & rubric are human-owned and agent-immutable** (R4). The agent may add tasks via PR, but weakening a check needs two human approvers.

## Files
- `rubric.md` — the binary judging rubric + LLM-judge prompt guidance.
- `ci-gate.md` — how the gate runs in CI and the tolerance rule.
- `tasks/` — one YAML per task (`_template.yaml` to start).

## Run (conceptually)
```
# pseudo — wire to your harness (pytest, promptfoo, ADK eval, etc.)
run-evals --suite regression --baseline main --tolerance 0      # blocks on ANY regression
run-evals --suite capability --report                            # trend only, non-blocking
```
