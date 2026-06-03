# CI eval gate

Treat prompts/skills/instructions like code: every change to the shared agent layer runs the eval gate in CI, and **regressions block the merge**.

## Trigger
- On PRs touching `AGENTS.md`, `knowledge/`, `.agents/`, `adk/`, or `evals/`.
- On model/version bumps (a new model is a change too).

## Flow
```
1. Check out the PR.
2. Run REGRESSION suite at tolerance 0  → any task below baseline = FAIL the check.
3. Run CAPABILITY suite (report only)   → post the trend, do not block.
4. Post to the PR: pass/fail, score deltas vs. main, and any regressed task names.
5. A human reads ≥1 transcript before approving (RULES.md §R5).
```

## Tolerance rule
- **Regression suite: tolerance = 0.** No required check may drop below the `main` baseline. (These are things the agent must always get right.)
- **Capability suite: non-blocking.** Track the trend; celebrate gains; never let a capability dip *alone* block a PR (it's expected to be noisy).

## Baseline & flakiness
- Baseline = scores on `main`. Re-baseline only via PR when the suite itself changes.
- Run stochastic tasks N times; require the pass *rate* to hold, not a single lucky run.
- A task that's 0% across many runs is usually a **broken task**, not an incapable agent — fix the task.

## Pair with production sampling
The golden gate catches *known* regressions deterministically. Separately, sample real production runs weekly to **discover new** failure modes → file them as new tasks. Gate = safety net; sampling = discovery (research §7.2).

## Wiring options
Harness-agnostic. Implement with `pytest`, `promptfoo`, `Braintrust`, or **ADK eval**; export traces via OTel GenAI to LangSmith/Langfuse/Phoenix. Keep task definitions (`tasks/*.yaml`) portable across whichever runner you pick.
