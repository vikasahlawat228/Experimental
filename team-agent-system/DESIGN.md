# DESIGN — Self-Improving Team Agent System

*Companion to the research report (`../team-agent-system-research-report.md`). This document turns the evidence into a concrete, layered design for a coding team of ~10–12 inside a ~100-person org, with a portable core and a Google-stack instantiation, framed as a target state plus a phased path to reach it.*

---

## 1. TL;DR

The system is **eight layers** wrapped by **one feedback loop** and **one rule book**:

```
        ┌──────────────────────  GOVERNANCE (humans + RULES.md)  ──────────────────────┐
        │   proposes ▸ evaluates ▸ promotes ▸ prunes      (nothing self-merges)          │
        │                                                                                │
   L7 Governance ── L6 Feedback/Evals ── L5 Enforcement(hooks) ── L4 Orchestration ──┐  │
        │                                                                            │  │
   L3 Skills/Playbooks ── L2 Instructions(AGENTS.md) ── L1 Knowledge(vectorless RAG) │  │
        │                                                                            │  │
   L0 Substrate (org LLMs + tools via MCP, model-agnostic) ◂─────────────────────────┘  │
        └────────────────────────────────────────────────────────────────────────────┘
```

The **directed bet** for a coding team: model the codebase as a *navigable structure* (not embedded chunks), keep the instruction layer ruthlessly small, store improvements as *external skills/playbooks* (never fine-tuned weights), keep **writes single-threaded** while spawning **read/verify sub-agents** freely, enforce hard rules with **deterministic hooks**, and let **evals + human promotion** be the only path to the shared layer. That combination is what makes it compound instead of rot.

---

## 2. How the research is "directed" to our context

| Our context | Directed design consequence |
|---|---|
| **Coding/software-eng work** | Retrieval = code-graph + repo-map + pointer index (not doc Q&A vector RAG). Writes single-threaded through a lead agent; sub-agents do read/search/**clean-context review**. |
| **~10–12 person team** | Lightweight governance: 1–2 rotating *curators*, PR-review promotion, a ~20–30 task eval set. No central platform team yet. |
| **Inside a ~100-person org, growing overlap** | Build the **layering seams now** (global→team→project precedence) even though only the team layer is populated today, so org standards can drop in without a rewrite. Never fork an org standard locally. |
| **Will gain org-level context over time** | Knowledge layer points to *sources of truth* (other teams' docs/repos) rather than copying them — so cross-team facts stay fresh automatically. |
| **Google stack (Gemini/ADK/Antigravity) + portability** | Portable artifacts (AGENTS.md, skills, eval tasks, pointer index) are the source of truth; ADK Plugins/callbacks and Antigravity `.agents/` are *bindings* to them, not separate copies. |

**The five decay forces we are explicitly engineering against** (from research §2): context rot, instruction bloat, self-improvement drift/reward-hacking, sycophantic feedback loops, knowledge staleness. Each layer below names which force it counters.

---

## 3. Design principles (the condensed tenets)

1. **Curate, don't accumulate** — smallest high-signal context, retrieved just-in-time. *(context rot)*
2. **Point to source; retrieve live** — store pointers, navigate on demand. *(staleness)*
3. **Structure over similarity** — code-graph/repo-map/pointer-tree, embeddings only as fuzzy fallback. *(retrieval quality at scale)*
4. **Improve artifacts, not weights** — skills/playbooks/memory via incremental delta updates. *(drift, forgetting)*
5. **Success criteria are human-owned and agent-immutable.** *(reward-hacking)*
6. **One source of truth, layered precedence** — adopt AGENTS.md; org layer non-overridable. *(forks, org-sync)*
7. **Small, pruned instructions** — <200 lines; move "sometimes" knowledge to on-demand skills. *(instruction bloat)*
8. **Hard rules via hooks, not prose.** *(non-compliance)*
9. **Evals are the unit of progress; gate every change in CI.** *(the core engine)*
10. **Feedback informs candidates, never auto-merges; correctness over popularity.** *(sycophancy / commons-degradation)*
11. **Federated contribution, central stewardship.** *(safe team-wide refinement)*
12. **Multi-agent for read/verify; single-threaded writes.** *(coordination failure, cost)*
13. **Vendor-neutral telemetry (OTel GenAI).** *(observability without lock-in)*

---

## 4. The eight layers (target state)

Each layer is independently ownable, independently testable, and bound to a repo location.

### L0 — Substrate: models & tools (reuse the org's, stay model-agnostic)
- **What:** the LLMs and tools the agent can call. Reuse org-provided models and tools rather than standing up your own.
- **Design:** expose every tool through **MCP** so the same tool works across IDEs; never hard-code a single model. Keep a thin "model profile" config (long-context model for synthesis, cheap model for routing/judging).
- **Counters:** lock-in. **Repo:** `adk/` bindings; tool list referenced from `AGENTS.md`.
- **Rule:** if the org provides a tool/model, **use it** — do not build a divergent local alternative (RULES.md §Org-sync).

### L1 — Knowledge: vectorless / agentic RAG (pointers + gotchas)
- **What:** a **navigable structure** the agent reasons over to find design docs, code, owners, and gotchas — *not* an embedding store.
- **Design:** three sub-parts —
  1. **Live code retrieval** — agentic grep/glob + a **repo-map** (tree-sitter ranked symbols) and/or **code-graph**. Always fresh because it reads current files.
  2. **Pointer index** (`knowledge/index.md` + `knowledge/pointers/`) — a curated table-of-contents the agent navigates: "auth lives here, design doc X is the source of truth, owner is Y." Each entry points to a source of truth, with a `last_verified` date.
  3. **Gotchas** (`knowledge/gotchas/`) — hard-won, *non-inferable* warnings. This is the highest-value, highest-risk content (see anti-pattern in §8).
- **Counters:** staleness (point-to-source), context rot (load pointers, fetch detail on demand).
- **Freshness mechanism:** every pointer/gotcha has `owner` + `last_verified` + `source_of_truth` link; a scheduled job flags entries older than N days or whose source file changed (see L6).
- **Fallback:** keep an optional embedding index for *fuzzy conceptual* search only; the structured layer is primary. *(research §3.2 — hybrid is the realistic endgame.)*

### L2 — Instructions: AGENTS.md as single source of truth
- **What:** the always-loaded behavioral context.
- **Design:** one `AGENTS.md` at root (<200 lines / ~350 words of real content), with the **Always / Ask-first / Never** boundary block, build/test commands, non-default conventions, and **pointers** into L1/L3 rather than inlined detail. Tool-specific files (`CLAUDE.md`, `GEMINI.md`) **symlink or import** it — never fork it.
- **Layered precedence:** `org (managed, non-overridable) → team (this repo) → project/subdir`. Today only team+project are populated; the org seam exists and is reserved.
- **Counters:** instruction bloat, forks, org-sync.
- **Rule:** the team layer may only *add* non-conflicting, non-inferable specifics; it may **never** restate or override an org standard.

### L3 — Skills & playbooks: where self-improvement lives
- **What:** on-demand, self-contained capabilities (`.agents/skills/`) and evolving "playbooks" of strategies.
- **Design:** each skill is a small Markdown file with a sharp `description` (routing depends on it), explicit inputs/outputs, and self-contained instructions (a sub-agent sees none of the parent's history). Improvements are applied as **incremental, itemized delta updates** (à la ACE), never monolithic rewrites — this is what prevents "context collapse."
- **Counters:** drift, forgetting, context rot (knowledge that's only *sometimes* relevant lives here, not in L2).
- **Rule:** a new/edited skill is a **candidate** until it passes the eval gate (L6) + curator review (L7). Then it's promoted. Store every version (git) for rollback.

### L4 — Orchestration: the harness (lead + sub-agents)
- **What:** how work is decomposed across agents.
- **Design (coding-directed):**
  - **Lead agent** owns the task and is the **only writer** (single-threaded writes).
  - **Read/search sub-agents** (parallel, isolated context) gather code/context and return *compressed summaries* (~1–2k tokens).
  - **Clean-context reviewer** sub-agent — a critic with **no prior context** — reviews diffs (catches what the author missed; research §8.2).
  - Patterns used: orchestrator-workers (research), routing (pick skill), evaluator-optimizer (the review loop).
- **Counters:** coordination failure, cost (sub-agents only for read/verify), context rot (isolation + compression).
- **Rule:** never parallelize interdependent writes; budget the ~15× token cost — reserve multi-agent for high-value tasks.

### L5 — Enforcement: deterministic hooks / guardrails
- **What:** the things that must happen *every time*, not left to the model's goodwill.
- **Design:** pre/post tool & model hooks (Claude Code hooks / **ADK Plugins & callbacks**) that block dangerous tools, scan for secrets, run linters/formatters, inject the freshest pointers, and redact sensitive data. Global enforcement (ADK Plugin on the Runner) sits above per-agent config and can short-circuit.
- **Counters:** non-compliance, security/privacy leakage.
- **Rule:** if a requirement is "always/never," it is a hook or a permission rule — **not** a line in AGENTS.md.

### L6 — Feedback & evals: the anti-degradation engine
- **What:** how the system knows a change is an improvement.
- **Design:** two suites — **capability** (start low, a hill to climb) and **regression** (~100% pass, blocks backsliding). 20–30 tasks seeded from real bugs/incidents; **binary** pass/fail rubric; LLM-judge **calibrated against a human** and using a *different* model than the generator; run in **CI on every change** with a tolerance gate. Plus production telemetry (OTel GenAI): traces, token/cost, tool errors, explicit feedback.
- **Counters:** all five forces — this is the gate everything passes through.
- **Rule:** read transcripts before trusting a score; capability tasks "graduate" into the regression suite when saturated.

### L7 — Governance: the human layer
- **What:** who can change what, and how.
- **Design:** **federated contribution, central stewardship** — anyone proposes skills/gotchas/eval-tasks via PR; **1–2 rotating curators** approve promotion to the shared layer; a quarterly (or trigger-based) **prune** removes stale/contradicted/low-value entries. Feedback (thumbs/bug reports) creates *candidates*, never auto-merges (anti-sycophancy).
- **Counters:** commons-degradation, sycophancy, drift.
- **Repo:** `governance/RULES.md`, `promotion-checklist.md`, `CODEOWNERS`.

---

## 5. Cross-cutting aspects (apply at every layer)

- **Freshness** — every durable artifact (pointer, gotcha, skill) carries `owner` + `last_verified`; staleness is detected, not hoped away (L1/L6).
- **Anti-drift** — success criteria and eval sets are human-owned; agents may propose but never self-approve (L5/L7).
- **Portability** — portable artifacts are the source of truth; vendor bindings (ADK/Antigravity) are generated/linked from them (L0/L2).
- **Token & cost budget** — context is an "attention budget"; sub-agents and caching keep it small. Track cost-per-task in telemetry (L4/L6).
- **Security & privacy** — secrets-scanning and data redaction live in hooks; sensitive data stays out of context via code-execution patterns (L5).
- **Observability** — OTel GenAI conventions everywhere, so the loop has data and you avoid lock-in (L6).

## 6. The self-improvement loop (why it gets better, not worse)

This is the closed loop that turns daily use into compounding quality:

```
 1. USE        Agent does real work (lead + sub-agents), emitting telemetry.
 2. OBSERVE    Telemetry + thumbs/bug reports surface failures & friction.
 3. DIAGNOSE   A failure → a candidate change: a new gotcha, a sharper skill,
               a fixed pointer, a tuned prompt, or a new eval task.
 4. PROPOSE    Candidate enters as a PR (never auto-applied).
 5. EVALUATE   CI runs the eval gate: capability + regression. Transcripts read.
 6. PROMOTE    Curator approves → merged into the shared layer (versioned).
 7. PRUNE      On cadence: stale/contradicted/low-value artifacts retired.
        └────────────────────────────► back to USE (now measurably better)
```

**The guarantee:** quality is monotonic *because step 5 is a gate*. A change that doesn't beat the baseline doesn't merge. The system can only ratchet upward — and pruning keeps it from bloating. Each failure the team hits once becomes an eval task that prevents the whole team from hitting it again. *This is the mechanism that answers "get better with time, don't rot."*

> **Anti-sycophancy detail:** step 3 weighs *correctness* (did it pass evals / fix the bug), not *popularity* (how many thumbs-up). A loud contributor cannot skew the commons because votes don't merge — passing evals + curator review do.

## 7. Instantiations

### 7a. Generic / portable (any multi-agent IDE)
- **L0:** tools via MCP; model profile in a config file. **L1:** `knowledge/` pointer index + `rg`/repo-map. **L2:** `AGENTS.md` (symlinked to `CLAUDE.md`/`.cursor/rules`). **L3:** `.agents/skills/`. **L4:** the IDE's sub-agent feature (Claude Code subagents, Cursor, etc.). **L5:** Claude Code hooks / git pre-commit. **L6:** `evals/` run via any harness in CI. **L7:** `governance/` + CODEOWNERS.
- Nothing here is Google-specific; a teammate on Claude Code or Cursor uses the identical artifacts.

### 7b. Google stack (Gemini + ADK + Antigravity)
See `docs/google-stack-mapping.md` for the full table. Highlights:
- **L0:** ADK is model-agnostic (`LiteLlm`/Vertex/Claude); tools via ADK `McpToolset`; cross-org agents via **A2A** (`RemoteA2aAgent`).
- **L1:** pointer index as an ADK tool; durable prefs/gotchas in **Vertex AI Memory Bank** (self-curating, scoped); large stable context cached via **Gemini context caching**.
- **L2:** `AGENTS.md` read natively by Antigravity (`.agents/`) and Gemini CLI (`context.fileName`).
- **L3:** Antigravity `skills/` + `workflows/` slash commands; ADK sub-agents.
- **L4:** ADK Workflow agents (Sequential/Parallel/Loop) + delegation; Antigravity Agent Manager.
- **L5:** **ADK Plugins** (Runner-level, global, precedence) + **callbacks** = deterministic guardrails. `adk/plugins/` has skeletons.
- **L6:** OTel GenAI export; eval tasks runnable via ADK eval.
- **L7:** identical (governance is human/process, vendor-independent).

### 7c. The seam to the org (future, ~100-person org)
- Reserve the **`org` precedence tier** above the team layer (managed/non-overridable). When org standards arrive, they drop into that tier; the team layer is already forbidden from conflicting with it (RULES.md).
- Cross-team facts are **pointers to the other team's source of truth**, kept fresh by `last_verified` checks — never copied.
- When multiple teams adopt this, the per-team `governance/` federates under a light central stewardship (the "department" model in the research) — no rewrite required.

## 8. Phased rollout (crawl → walk → run) with exit criteria

Grow the machinery **only when evals justify it** — the research is explicit that these systems should grow through iteration, not big up-front design.

| Phase | You build | Exit criteria (don't advance until met) |
|---|---|---|
| **P0 — Crawl (week 1)** | `AGENTS.md` filled in; `knowledge/index.md` seeded with top 10 pointers; 10 eval tasks from recent bugs; `RULES.md` adopted. | Agent passes all 10 tasks; team agrees on RULES; one real task done end-to-end. |
| **P1 — Walk (weeks 2–4)** | CI eval gate wired up; gotchas captured as they're hit; 2–3 core skills; secrets/lint hooks; clean-context reviewer sub-agent. | Eval gate blocks a real regression in CI; ≥25 tasks; reviewer catches ≥1 bug; curator rotation running. |
| **P2 — Run (months 2–3)** | Repo-map/code-graph retrieval; parallel read sub-agents; telemetry dashboard (OTel); freshness job flags stale pointers; prompt optimization (GEPA/DSPy) against the eval set. | Cost-per-task tracked & stable; staleness flags actioned; a skill measurably improved via optimization (eval delta). |
| **P3 — Compound (ongoing)** | Playbook delta-update loop; Vertex Memory Bank (Google) / persistent memory; org-tier seam populated as overlap grows; federated governance if other teams join. | Quarterly prune executed; ≥1 cross-team pointer live; eval suite still discriminating (not saturated). |

**Rollback is always available:** every shared-layer artifact is versioned in git; a bad promotion is reverted in one PR.

## 9. Anti-patterns to avoid (straight from the evidence)

- **The bloated AGENTS.md.** A controlled study found careless context files *reduce* success and add 20%+ cost. Keep it small; prune ruthlessly; only non-inferable, high-signal content. *(research §6.4)*
- **Letting the agent edit its own success criteria.** Self-improving systems reward-hack (deleted detection markers, faked logs). Criteria are human-only. *(§5.2)*
- **Thumbs-up-driven auto-updates.** Aggregating preference breeds sycophancy. Feedback → candidate → eval gate, never auto-merge. *(§7.4)*
- **Embedding-everything RAG for code.** Similarity ≠ relevance for code symbols; prefer structure + agentic retrieval, keep embeddings as fuzzy fallback. *(§3)*
- **Multi-agent for interdependent writes.** Parallel writers make conflicting decisions. Single-threaded writes; sub-agents for read/verify. *(§8)*
- **Forking org standards locally.** One source of truth, layered precedence, org tier non-overridable. *(§6.2)*
- **Trusting eval scores you haven't transcript-read.** Scores lie until someone reads the runs. *(§7.1)*

## 10. Decisions & open questions

Key decisions are recorded as ADRs in `docs/decisions/` (vectorless RAG, self-improvement-as-playbooks, multi-agent boundaries). Revisit when the triggering assumption changes — this is part of anti-staleness. Live open questions: vectorless-vs-hybrid threshold for *our* repo size; whether Memory Bank or a flat file store fits our scale at P3; when team→department governance federation is worth it.

