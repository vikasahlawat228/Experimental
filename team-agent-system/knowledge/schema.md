# Knowledge schema — pointers & gotchas

Defines the format and the **freshness rules** that keep the vectorless RAG from rotting. Two entry types: **pointers** (where things are) and **gotchas** (non-inferable warnings). Both are small Markdown files with YAML front-matter so a script (and the agent) can parse them.

## Why pointers, not embedded content
We **point to the source of truth** and retrieve live, instead of copying content into an index. Copied content goes stale silently; a pointer + `last_verified` makes staleness *visible and actionable*. (Research §3.3.)

## Pointer entry — required fields
```yaml
---
id: auth-service              # kebab-case, unique
type: pointer
area: "Auth & sessions"
owner: "@alice"               # who keeps this true
source_of_truth:              # links/paths — NOT copied content
  - "services/auth/"
  - "https://docs.internal/design/auth"
last_verified: 2026-06-03     # date a human confirmed this is still accurate
related: [migrations, api]    # other pointer ids
---
```
Body = a *short* orientation (3–10 lines): what lives here, the entry points, what to be careful of, and a link to the relevant gotcha. **No copied design-doc prose** — link to it.

## Gotcha entry — required fields
```yaml
---
id: migration-ordering
type: gotcha
severity: high                # low | medium | high
area: "Data model / migrations"
owner: "@bob"
trigger: "editing a migration or a Temporal workflow"
last_verified: 2026-06-03
eval_task: evals/tasks/migration-ordering.yaml   # the test that locks this in (optional but encouraged)
---
```
Body = the trap + the rule, in ≤8 lines. A gotcha is only worth keeping if it's **non-inferable** (the agent can't deduce it from the code) and **high-signal**.

## Freshness rules (enforced by the L6 job + L7 prune)
1. Every entry MUST have `owner` and `last_verified`.
2. The freshness job flags entries where `last_verified` is older than **90 days** OR a listed `source_of_truth` file changed since then.
3. Flagged entries are re-verified or retired at the next prune (quarterly or trigger-based).
4. A gotcha that has a passing `eval_task` may extend its review interval — the eval now guards it.
5. Contradictory entries are a governance bug: resolve to one, delete the other (no silent forks).

## Quality bar (the litmus test)
Before adding an entry, ask: *"Would the agent make a mistake without this, and can it not figure it out from the code?"* If either answer is no, **don't add it** — every entry competes for attention and adds retrieval cost. (Research §6: instruction/context bloat measurably hurts.)
