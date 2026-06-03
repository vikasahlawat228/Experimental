# AGENTS.md — single source of truth for agents

<!--
  RULES FOR THIS FILE (enforced by governance/RULES.md):
  • Keep under ~200 lines / ~350 words of real content. Longer files get ignored.
  • Per-line litmus test: "Would removing this cause the agent to make a mistake?" If no, cut it.
  • Only NON-INFERABLE, high-signal content. Nothing the agent can read from code/config.
  • Sometimes-relevant knowledge → a skill in .agents/skills/. Detail → a pointer in knowledge/.
  • This is the ONE source of truth. CLAUDE.md / GEMINI.md / .cursor must symlink or @import this file — never fork it.
  • The org layer (when it exists) is non-overridable. Do NOT restate or contradict org standards here.
  REPLACE every <PLACEHOLDER> below with your project's real values, then delete this comment.
-->

## Project snapshot
- **What this is:** <one line — e.g., "Payments service: Go API + Postgres + Temporal workflows.">
- **Owner / curators:** see `governance/CODEOWNERS`.
- **Sources of truth:** code in this repo; design docs & gotchas indexed in `knowledge/index.md`.

## Commands (non-guessable only)
- Build: `<cmd>`  ·  Test: `<cmd>`  ·  Lint: `<cmd>`  ·  Run one test: `<cmd>`
- Local env: `<cmd / notable quirk>`

## Conventions (only where we differ from the language/default)
- <e.g., "Errors: wrap with `fmt.Errorf("%w")`, never `errors.New` in handlers.">
- <e.g., "No new dependencies without a curator-approved ADR.">

## How to find things (the knowledge layer)
- Navigate `knowledge/index.md` to locate subsystems, design docs, owners.
- For code, use agentic search (grep/glob) + the repo map; do **not** assume a stale index.
- Check `knowledge/gotchas/` before touching auth, migrations, billing, or anything marked ⚠ in the index.

## Boundaries

### Always
- Run lint + tests before proposing a diff is "done".
- Cite the file/pointer you relied on when you make a non-obvious change.
- Prefer the org-provided tool/model/library over a custom alternative.

### Ask first
- Adding a dependency, changing a public API, editing a migration, or touching `infra/`.
- Anything that would change behavior for another team (check `knowledge/index.md` ownership).

### Never
- Edit eval tasks, rubrics, or success criteria to make a check pass (see governance/RULES.md §Anti-drift).
- Commit secrets, disable a security hook, or bypass the review step.
- Re-implement something the org already provides as a shared tool/service.

## Working with sub-agents
- **Writes are single-threaded** through the lead agent. Sub-agents are for **read/search/review** only.
- When delegating, restate the needed context — sub-agents do not see this conversation.
- Sub-agents return a **compressed summary** (~1–2k tokens), not raw dumps.
- For review, spawn a **clean-context reviewer** (no prior context) — it catches more.

## Skills & workflows
- On-demand capabilities live in `.agents/skills/`; multi-step pipelines in `.agents/workflows/`.
- Don't inline a procedure here — point to the skill.

## Hard rules are hooks, not prose
- Secret-scanning, lint/format, and dangerous-tool blocks are enforced by hooks/ADK Plugins (`adk/plugins/`), not by this file. If something *must* happen every time, it belongs there.
