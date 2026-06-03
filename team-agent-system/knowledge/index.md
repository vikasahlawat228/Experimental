# Knowledge Index — the navigable root (vectorless RAG)

This is the **table of contents the agent reasons over** to find design docs, code areas, owners, and gotchas. It is plain Markdown on purpose: no embeddings, always fresh, diff-reviewable. The agent reads this, picks the relevant pointer, then fetches detail on demand.

> **How retrieval works here:** navigate this index → open the matching `pointers/<name>.md` → follow its `source_of_truth` link or grep the code path it names. Check `gotchas/` for any ⚠ area before editing. See `schema.md` for the entry format and freshness rules.

## Subsystems / areas
*(one row per area; link to the pointer file; ⚠ = read the gotcha first)*

| Area | Pointer | Owner | Source of truth | ⚠ |
|---|---|---|---|---|
| Auth & sessions | [auth-service](pointers/example-auth-service.md) | @alice | `services/auth/` + Design Doc | ⚠ |
| <Billing> | <pointers/billing.md> | <@owner> | <link> | |
| <Data model / migrations> | <pointers/migrations.md> | <@owner> | <runbook link> | ⚠ |
| <Public API> | <pointers/api.md> | <@owner> | <OpenAPI spec> | |

## Design docs (pointers, not copies)
| Doc | Pointer | Status | Last verified |
|---|---|---|---|
| <Architecture overview> | <pointers/architecture.md> | <current> | <YYYY-MM-DD> |

## Cross-team dependencies (the org seam)
*(point to the OTHER team's source of truth; never copy it — keeps it fresh)*

| What we depend on | Their source of truth | Their contact | Last verified |
|---|---|---|---|
| <Identity platform> | <link to their docs/repo> | <@team-contact> | <YYYY-MM-DD> |

## Gotchas quick list
*(full entries in `gotchas/`; surfaced here for discoverability)*
- ⚠ [Migration ordering vs. Temporal replay](gotchas/example-migration-ordering.md) — @bob

---
*Maintained under `governance/RULES.md`. Add a row when you add a pointer. The freshness job (L6) flags rows whose `last_verified` is stale or whose source file changed.*
