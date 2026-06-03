# Team Agent System — a self-improving, team-level agent harness

A reference design + starter scaffold for a **team-level agent system that gets better with time instead of rotting** as the team uses and refines it. Built for a **coding/software-engineering team (~10–12 people inside a ~100-person org)**, designed to plug into org-level standards as cross-team overlap grows.

It is **portable by default** (works with any multi-agent IDE/agent — Claude Code, Cursor, Gemini CLI, Antigravity) with a **Google-stack instantiation** (Gemini + ADK + Antigravity + Vertex Memory Bank + A2A).

> This scaffold is grounded in the research report at `../team-agent-system-research-report.md`. Every design choice traces to a finding there; the contrarian evidence (e.g., that careless context files *measurably hurt*) is baked into the guardrails.

## The one idea

Bias every layer toward **curation, not accumulation**, and make **evals + human-owned promotion gates** the only way anything reaches the shared layer. The system improves because *good* changes are the only ones that survive — not because it blindly accretes context.

## Repository map

```
team-agent-system/
├── README.md                  ← you are here
├── DESIGN.md                  ← the layered design (levels & aspects, target state + phased path)
├── AGENTS.md                  ← THE single source of truth for agents (portable, <200 lines)
├── docs/
│   ├── google-stack-mapping.md    portable concept → ADK/Gemini/Antigravity
│   └── decisions/                 Architecture Decision Records (ADRs)
├── knowledge/                 ← the vectorless RAG: pointers + gotchas (no embeddings)
│   ├── index.md                   navigable root the agent reasons over
│   ├── schema.md                  pointer/gotcha schema + freshness rules
│   ├── pointers/                  one file per subsystem/design-doc/code area
│   └── gotchas/                   hard-won, non-inferable warnings
├── .agents/                   ← portable + Antigravity-native agent config
│   ├── rules/                     thin pointers to the single source of truth
│   ├── skills/                    on-demand, self-contained skills (template + example)
│   └── workflows/                 multi-step agent pipelines (template + example)
├── evals/                     ← the anti-degradation engine
│   ├── README.md                  the eval-gate spec
│   ├── rubric.md                  binary judging rubric
│   ├── ci-gate.md                 CI gating flow + tolerance
│   └── tasks/                     golden eval tasks (template + example)
├── adk/                       ← Google-stack skeletons (model-agnostic)
│   ├── plugins/                   deterministic guardrail + OTel telemetry
│   ├── callbacks/                 context-freshness injection
│   └── memory/                    Vertex Memory Bank + State-scope config
└── governance/                ← the human layer
    ├── RULES.md                   the constitution (how the system is allowed to change)
    ├── promotion-checklist.md     PR-style gate for shared-layer changes
    └── CODEOWNERS                 curation roles
```

## How to use it

1. **Read `DESIGN.md`** for the full architecture and the crawl-walk-run rollout.
2. **Start at Phase 0** (see DESIGN §7): fill in `AGENTS.md`, seed `knowledge/index.md`, write 10 eval tasks. That alone is a working, non-rotting system.
3. **Adopt `governance/RULES.md`** as the team agreement before more than one person edits the shared layer.
4. **Grow only behind evals.** Each later phase has explicit exit criteria — don't add machinery until the metrics justify it.

## What this is NOT

Not a framework to install, and not production code — it's a **design + editable templates**. The `.py` files in `adk/` are documented skeletons showing the integration shape, not a deployable package.
