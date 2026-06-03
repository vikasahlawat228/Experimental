---
name: feature-change
description: "Implement a scoped feature or bugfix safely, end to end."
trigger: "/feature"
owner: "@alice"
last_verified: 2026-06-03
---

# feature-change

The default pipeline for a coding task. Demonstrates the harness shape: one writer, isolated readers, an independent reviewer, and a hard eval gate.

## Steps
1. **Plan** — lead agent restates the goal + acceptance criteria; lists files it expects to touch. No writes.
2. **Retrieve** — run the `retrieve-context` skill (parallel read sub-agents if multiple areas). Returns compressed briefs + any ⚠ gotchas.
3. **Implement** — **lead agent only** writes the change. Sub-agents never write here (avoids conflicting decisions; DESIGN §9).
4. **Review** — spawn a **clean-context reviewer** sub-agent: give it ONLY the diff + acceptance criteria, no history. It reasons backward from the implementation and reports bugs/edge-cases.
5. **Gate** — run `evals/` (capability + regression). On any regression below tolerance: stop, surface the failed cases, do not open the PR.
6. **Promote** — if a new gotcha/skill emerged, file it as a candidate per `governance/promotion-checklist.md`.

## Stop conditions
- "Ask first" boundary hit (new dep, public API, migration, infra) → pause for a human.
- Eval gate fails → block. Hooks (lint/secrets) failing → block (enforced in `adk/plugins/`).

## Token budget
- Reviewer + readers add cost; that's intended. Skip parallel readers for single-file changes.

*(Example workflow — replace specifics with your stack. The structure is the point.)*
