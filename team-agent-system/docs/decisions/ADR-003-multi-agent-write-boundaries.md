# ADR-003 — Single-threaded writes; sub-agents for read & verify only

- **Status:** accepted
- **Date:** 2026-06-03
- **Deciders:** team curators

## Context
We're a coding team, so most work is **write-heavy and interdependent** — exactly the regime where multi-agent systems are documented to struggle. How should we use sub-agents?

Evidence (research §8): Anthropic's multi-agent research system beat single-agent by 90.2% but for **read-heavy, breadth-first** work, at ~15× token cost, and explicitly calls multi-agent a **bad fit for shared-context/interdependent tasks — naming most coding**. Cognition: parallel **writers** make conflicting implicit decisions. Both agree the safe use is **read-only sub-agents**. Cognition also found a **clean-context reviewer** (no shared history) catches ~2 bugs/PR.

## Decision
- The **lead agent is the sole writer** (single-threaded writes).
- Spawn sub-agents freely for **read/search** (parallel, isolated context, compressed summaries) and for **review** (a clean-context critic on the diff).
- Reserve broader multi-agent parallelism for high-value, parallelizable *read* tasks; budget the ~15× token cost.

## Consequences
**Good:** avoids conflicting-write failures; gains context isolation + an independent reviewer; controls cost.
**Bad / risks:** less parallelism on the write path; reviewer/readers add token cost (intended). Single-file trivial changes skip the readers.

## Revisit when
Models materially improve at real-time write coordination, or our tasks shift toward parallelizable/read-heavy work (e.g., large-scale codemods) where parallel writers with strong contracts could pay off.
