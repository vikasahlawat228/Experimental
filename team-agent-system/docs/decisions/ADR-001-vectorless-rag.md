# ADR-001 — Vectorless / agentic retrieval as the primary knowledge layer

- **Status:** accepted
- **Date:** 2026-06-03
- **Deciders:** team curators

## Context
We need the agent to find design docs, code, owners, and gotchas, and to stay fresh as the codebase and the team's knowledge grow. Options: (a) embed-everything vector RAG, (b) agentic/structured retrieval over a navigable index + live code search, (c) hybrid.

Evidence (research §3): Anthropic A/B-tested vector RAG vs agentic search in Claude Code and dropped the vector DB ("agentic search outperformed by a lot"; also cited security, privacy, **staleness**, reliability). Amazon (AAAI 2026) reached >90% of RAG quality with no vector store. For code, "similarity ≠ relevance" (RepoGraph; PageIndex). Counter-evidence: embeddings still win for fuzzy conceptual search and survive renames; agentic retrieval costs 3–10× tokens.

## Decision
Primary = **structured + agentic**: a curated pointer index (`knowledge/`) + repo-map/code-graph + agentic grep, reading current files. Keep an **optional embedding index as a fuzzy-search fallback only**. Knowledge entries **point to sources of truth**, never copy them.

## Consequences
**Good:** always-fresh; diff-reviewable; no index pipeline to maintain; quality compounds via a richer pointer/graph structure as we scale.
**Bad / risks:** higher per-query token/latency cost; relies on good code-search tooling; fuzzy conceptual search is weaker without the fallback. We accept these for freshness + simplicity.

## Revisit when
Our repo/corpus grows past the point where agentic search is too slow/expensive per query, or we see frequent "couldn't find it" failures in telemetry → evaluate turning the embedding fallback on by default (move toward hybrid).
