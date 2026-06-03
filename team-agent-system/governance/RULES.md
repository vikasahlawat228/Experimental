# RULES.md — the constitution

How this agent system is **allowed to change**. The whole point is that the team can refine it without it degrading. These rules are what make that true. They are deliberately short and human-owned.

> Precedence: **org standards (when present) > these rules > AGENTS.md > skills/pointers**. Nothing in a lower layer may override a higher one.

---

## R1 — What may change, and by whom

| Asset | Who can propose | Who approves (promotes) | How |
|---|---|---|---|
| `knowledge/` pointers & gotchas | anyone (incl. the agent) | a curator | PR + checklist |
| `.agents/skills/` & `workflows/` | anyone | a curator | PR + eval gate |
| `AGENTS.md` | anyone | a curator | PR (watch the size budget) |
| `evals/` tasks & **rubric** | anyone | **2 humans** (never the agent) | PR; see R4 |
| `governance/` (this file, RULES) | anyone | team consensus | PR + discussion |

The **agent may propose** any candidate (a gotcha it learned, a sharper skill, a fixed pointer). It **may not self-approve or self-merge** anything. (Counters self-improvement drift.)

## R2 — Single source of truth, no forks
- `AGENTS.md` is the one behavioral file. `CLAUDE.md` / `GEMINI.md` / `.cursor/rules` **symlink or `@import`** it. Copying is a violation.
- A fact lives in exactly one place. Duplicated guidance that drifts is a governance bug — resolve to one, delete the rest.

## R3 — Org-sync (no custom alternatives to global tools)
- If the org provides a tool, model, library, or standard, **use it**. Do not build or document a team-local alternative.
- The team layer may only **add** non-conflicting, non-inferable specifics. It may never restate or contradict an org standard. When the org tier is populated, conflicting team entries are deleted, not negotiated.

## R4 — Anti-drift (success criteria are sacred)
- The **eval tasks, rubric, and acceptance criteria are human-owned and agent-immutable.** The agent must never edit them to make a check pass — doing so is the #1 documented failure of self-improving systems (deleting detectors, faking logs).
- Changes to `evals/rubric.md` or any task's expected outcome require **two human approvers**, and a one-line rationale.
- The base model is **frozen**: we improve external artifacts (skills/pointers/prompts), never fine-tune on team feedback.

## R5 — The promotion gate (how a candidate becomes shared)
Nothing reaches the shared layer without passing, in order:
1. **Eval gate** — CI runs capability + regression suites; no metric may fall below baseline beyond tolerance (`evals/ci-gate.md`).
2. **Transcript check** — the reviewer reads at least one run; a green score nobody looked at doesn't count.
3. **Curator approval** — a curator signs off using `promotion-checklist.md`.
Versioned in git → **rollback is one revert**.

## R6 — Feedback handling (anti-sycophancy)
- Thumbs/bug reports create **candidates**, never auto-applied changes.
- Promotion weighs **correctness** (passes evals / fixes the bug), not **popularity** (vote count). A loud minority cannot skew the shared layer.
- A recurring failure should become an **eval task** (so it can never regress) before or alongside any prompt/skill fix.

## R7 — Anti-bloat & freshness (prune or it rots)
- `AGENTS.md` stays under ~200 lines; pointers/gotchas/skills stay minimal and single-purpose.
- Litmus test for any addition: *"Would the agent err without this, and can it not infer it from code?"* If not — reject.
- **Prune cadence:** quarterly, or whenever the freshness job flags >10 stale entries. Retire stale/contradicted/low-value artifacts. Pruning is a celebrated contribution, not a chore.

## R8 — Multi-agent boundaries
- **Writes are single-threaded** (one lead writer). Sub-agents are read/search/review only.
- Always include an **independent (clean-context) reviewer** for non-trivial diffs.
- Reserve parallel/multi-agent for high-value, parallelizable read work (it costs ~15× tokens).

## R9 — Hard rules are hooks, not prose
- Anything that must happen every time (secret-scan, lint/format, blocking a dangerous tool) is enforced in `adk/plugins/` (or IDE hooks), not written as an instruction. Instructions are advisory; hooks are deterministic.

## R10 — Roles (kept light for a ~10–12 person team)
- **Curators (1–2, rotating monthly):** approve promotions, run the prune, own `evals/` health. Listed in `CODEOWNERS`.
- **Everyone:** proposes candidates, files gotchas the moment they're hit, adds eval tasks for bugs they fix.
- As the org overlap grows, curator roles federate under light central stewardship (department model) — no rewrite needed.

---
*Amend this file by PR + team discussion. Keep it this short — a constitution nobody reads is worse than none.*
