# Memory mapping — State scopes & Vertex AI Memory Bank (L1)

How our durable knowledge maps onto ADK memory primitives. Start with files (`knowledge/`); adopt Memory Bank at Phase 3 when scale justifies managed, self-curating memory.

## ADK State scopes → our usage
| Scope (prefix) | Lifetime | We use it for |
|---|---|---|
| *(none)* | current session | the task's working notes (compaction target) |
| `user:` | across a user's sessions | a teammate's stable preferences (e.g., review style) |
| `app:` | all users of the app | team-wide toggles / config |
| `temp:` | current turn only (discarded) | injected pointer preamble (freshness callback) — never persisted |

> Mapping rule: anything that should be **team-durable and reviewable** belongs in the git-tracked `knowledge/` layer (diffable, gated by RULES.md), **not** in opaque memory state. Use State/Memory Bank for *runtime* recall, not as the source of truth.

## Vertex AI Memory Bank (Phase 3)
- Managed, Gemini-extracted, **self-curating** (add/update/remove), scoped similarity search.
- Wire via `VertexAiMemoryBankService` behind the ADK `MemoryService` interface
  (`add_session_to_memory`, `search_memory`).
- Managed topics include `EXPLICIT_INSTRUCTIONS`, `USER_PREFERENCES`, `KEY_CONVERSATION_DETAILS`.

### Guardrail (anti-drift)
Memory Bank self-curates, which is convenient but is also an **unsupervised mutation** of context. Keep the **authoritative** gotchas/standards in the git-tracked, eval-gated `knowledge/` layer; let Memory Bank hold *convenience recall* only. If a memory contradicts a `knowledge/` entry, the git entry wins (RULES.md §R2 — one source of truth).

## Big stable context → Gemini caching
Cache the stable team overview (architecture summary, canonical pointers) with Gemini **context caching** (implicit on 2.5; explicit `CachedContent` for guaranteed savings) so every agent reuses it cheaply instead of re-sending it. Re-confirm pricing on the live Gemini pricing page (research §9.3).
