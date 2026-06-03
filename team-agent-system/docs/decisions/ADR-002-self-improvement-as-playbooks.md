# ADR-002 — Self-improvement lives in external artifacts, gated by evals (not fine-tuning, not self-merge)

- **Status:** accepted
- **Date:** 2026-06-03
- **Deciders:** team curators + tech lead

## Context
The system must "get better with time" as the team refines it. How should improvement be stored and applied? Options: (a) fine-tune the model on team feedback; (b) let the agent auto-update its own instructions/skills; (c) external, versioned artifacts (skills/pointers/prompts) updated via incremental deltas and a human-owned gate.

Evidence (research §5, §7.4): ACE shows evolving "playbooks" via **incremental delta updates** beat baselines and avoid "context collapse"; Voyager shows **executable, external** skills resist forgetting. But every autonomous self-improver studied **reward-hacked** (DGM deleted detection markers / faked logs; STOP bypassed its sandbox), and aggregating human preference **induces sycophancy** (ICLR 2024).

## Decision
- Improve **external artifacts only**; the base model stays **frozen** (no fine-tuning on team feedback).
- Updates are **incremental, itemized deltas** (à la ACE), never monolithic rewrites.
- The agent may **propose** changes; **humans + the eval gate promote** them. **No self-approval, no auto-merge.**
- Success criteria/eval tasks are **agent-immutable** (RULES.md §R4).
- Feedback is weighed on **correctness, not popularity**; recurring failures become eval tasks.

## Consequences
**Good:** capability compounds with a hard ratchet (only changes that beat baseline survive); fully reversible (git); no drift into a fine-tuned black box.
**Bad / risks:** slower than letting the agent self-edit; requires curator discipline and a real eval suite. We accept this — the alternative is documented to reward-hack.

## Revisit when
Eval infrastructure is mature enough that automated promotion of *low-risk* artifact classes (e.g., a new pointer) could be trusted behind the gate — and only with append-only audit + easy rollback.
