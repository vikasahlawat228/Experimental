# AI-Native Engineering at Google

**A Team Playbook for Storing Context, Building Skills, and Working with Gemini in the Loop**

*For engineering teams using Gemini, Code Assist, NotebookLM, Gems, the Agent Platform, and MCP.*

Version 1.0 · May 2026

---

## Executive Summary

The interesting question in 2026 is no longer whether your engineering team should be using AI day-to-day. Gemini ships ~50% of new code characters into Google's monorepo by character count, the DORA 2025 report shows 90% developer adoption industry-wide, and the production constraint has visibly shifted from typing code to reviewing, integrating, and trusting it. The interesting question is how a single team sets up its context, skills, tools, and human-in-the-loop discipline so that this leverage compounds instead of leaking into friction.

This playbook is the result of an audit across three bodies of practice: what Google has published about how its own engineering teams work with AI (the DIDACT pipeline, Critique's ML-resolved comments, the int32→int64 migration, the OCTO post on review fatigue, the 2025 DORA findings); what the wider ecosystem has converged on in 2025–2026 (AGENTS.md as a cross-tool standard, Anthropic's Skills with progressive disclosure, MCP's near-universal adoption, the Shopify-style internal LLM gateway, Simon Willison's anti-patterns list); and what works specifically inside the Gemini stack a Googler has at hand (Gems, NotebookLM Enterprise, Code Assist with `.gemini/styleguide.md`, the Gemini Enterprise Agent Platform, official remote MCP servers, Gemini CLI).

The recommendation that comes out of all three streams is the same: treat AI enablement as a platform program for the team, not as individual tool choice. Build four layers, in order. First, store team context in a small set of canonical files and grounded knowledge bases. Second, capture reusable procedural knowledge as named, discoverable skills. Third, expose your tools and data through MCP, with allowlists and OAuth. Fourth, write down your human-in-the-loop policy explicitly — which actions are auto-approved, which need PR review, which need a synchronous human — and run an eval harness against it. Most teams overshoot to autonomous agents before any of the four layers is in place; the orgs reporting 2–3× measurable productivity lift are the ones that do these in order.

The rest of this document expands each of those four layers, recommends a concrete four-week rollout, lists the anti-patterns you should publish on the team wiki as norms with teeth, and ends with starter templates you can copy directly.

---

## Part 1 · Why the Bottleneck Has Moved

The single most useful frame for this work comes from Lee Boonstra in Google Cloud's OCTO post from April 2026, and it is worth reading carefully before designing anything else.

> *"AI eliminated the code production bottleneck, and the constraint moved downstream to the humans who have to review, test, and integrate all that output. Better prompts and faster models won't fix that."*
> — Lee Boonstra, Google Cloud Office of the CTO

Google's own published numbers tell the same story from a different angle. According to research.google's *AI in Software Engineering at Google* post and the follow-up ICSE 2026 paper from Tabachnyk, Chandra, and Frömmgen, roughly 50% of new code characters are now AI-generated in the internal IDE, with a 37% suggestion acceptance rate. In Critique, ML-suggested edits now resolve more than 8% of all reviewer comments via a one-click apply, with about 52% of eligible comments receiving a suggestion at a 50% target precision. The int32-to-int64 ID migration across Ads, documented in research.google's July 2024 case study, landed with 80% of code modifications authored by AI, cutting total migration time in half. Pichai's public number on AI-authored code grew from 25% (Oct 2024) to 30%+ (Apr 2025).

And yet the 2025 DORA report, which Google Cloud publishes and which surveys ~39,000 engineers worldwide, found that while 90% of developers now use AI tools daily, only 24% trust them "a lot" or "a great deal," and 30% trust them "a little" or "not at all." DORA calls this the "trust paradox" and concludes that time saved on generation is largely reallocated to review and verification — friction shifts, it does not disappear. The single developer quote pinned in the executive summary of that report is: *"AI tools increase my productivity, they write code faster than I could, but the code is (currently) lower quality than I could write myself."*

If you accept those two facts together — leverage is real, the bottleneck has moved — then the rest of this playbook follows. You are not optimizing for "AI does more"; you are optimizing for review throughput, context portability, calibrated trust, and the discipline that lets a team get to merged code without anyone rubber-stamping a 2,000-line diff at 5:45pm on a Friday. Everything below is in service of that.

### Google's own three-rule playbook

Buried in the research.google post is a remarkably concise statement of Google's internal methodology. It is worth lifting verbatim because it is doing more work than its short length suggests. First, prioritize ideas that are both technically feasible and measurably impactful; offline metrics are at best rough proxies, so validate with online A/B. Second, AI suggestions should blend into the existing workflow — tab to accept, click to apply, no remembering to trigger a feature. Third, the author becomes a reviewer; target acceptance rates that balance the cost of review against the value of the suggestion. The first two are about adoption. The third is the entire HITL problem in one sentence.

---

## Part 2 · Storing Team-Wise Context

Context is the most leveraged thing a team can invest in. A single well-written `GEMINI.md` changes the quality of every interaction every engineer has with the assistant. The mental model to hold is a hierarchy of four layers, each answering a different question at a different lifetime, and each with a corresponding primitive in the Gemini stack.

The personal layer answers *"who am I and how do I like to work"* — your editor preferences, your verbosity tolerance, the team you sit on. It lives in `~/.gemini/GEMINI.md` and travels with you across repos. The repository layer answers *"what is this codebase, how is it built and tested, what is the house style"* and lives at the repo root, ideally checked in as `AGENTS.md` with `GEMINI.md` symlinked to it. The subsystem layer answers *"what is specific about this service or package"* and lives nested in subdirectories. The grounded layer answers *"what do our design docs, RFCs, runbooks, and dashboards say"* and lives in NotebookLM notebooks and Gem knowledge files, where every answer carries a citation back to a source.

### 2.1 · The personal layer

Keep `~/.gemini/GEMINI.md` short. It is loaded on every invocation, so anything you put here is a permanent context tax. Two to three hundred words is plenty: your role and team, the languages you work in most, the level of explanation you want by default, how you like commit messages and PR descriptions formatted, and explicit negative constraints. Negative constraints empirically work better than positive preferences — *"do not use class components"* beats *"prefer hooks"* in every published comparison.

### 2.2 · The repository layer

This is the file that earns its keep. The community has converged in 2025–2026 on `AGENTS.md` as the cross-tool standard, with over 60,000 OSS repos shipping one as of May 2026 and native reading support in every major coding agent. Inside Google, the equivalent expectation is `GEMINI.md` at the repo root. The cleanest pattern is to write `AGENTS.md`, symlink `GEMINI.md` to it, and configure `context.fileName` in `.gemini/settings.json` to pick up whichever name your tooling prefers.

The repo-level file should read like the first day of onboarding a competent new engineer who is going to start typing in five minutes. It tells them how to set up the workspace, the build and test commands they actually need, the directories they should and should not touch, the style guide URL, the test conventions, the PR title format, and the security gotchas. It is not documentation of the codebase, which lives elsewhere; it is the smallest possible map that lets the agent stop asking questions a human teammate would not need to ask.

Keep the always-loaded portion under about 2,000 tokens. Anything richer belongs in a referenced file (`@file` imports work in `GEMINI.md`), as a Skill (Part 3), or as a NotebookLM source (Section 2.4).

### 2.3 · The subsystem layer

For services or packages with their own idioms — a payments service with stricter testing rules, a frontend package with a specific component library, an experimental directory that should not be refactored — add nested `GEMINI.md` files in those directories. They override the repo-level rules locally.

### 2.4 · The grounded layer: NotebookLM and Gem knowledge files

`GEMINI.md` cannot hold design docs, RFC archives, runbooks, or incident postmortems — they are too large and too volatile. The right primitive for that is NotebookLM, which is source-grounded RAG over a fixed corpus and crucially attaches a citation to every answer. NotebookLM Enterprise runs in your Google Cloud project with IAM-bound sharing, VPC-SC, audit logs, and a documented no-training-on-your-data guarantee.

The two patterns that separate teams who get value from NotebookLM from teams who don't are scoping and refresh. On scoping: prefer many small notebooks (*"Payments service runbooks", "Q2 2026 RFCs", "On-call playbook v3"*) over one mega-notebook. On refresh: notebooks are snapshots, not live mirrors, so add a calendar reminder to re-sync sources weekly. The Audio Overview feature is the highest-leverage onboarding tool you will discover; generate one for each domain area and link it from the new-hire doc.

For lighter weight reusable contexts tied to a specific role or workflow, build a Gem. A Gem is a Gemini configuration with up to ten knowledge files and a system prompt, shareable via the Workspace admin console.

### 2.5 · Putting the layers together

If you find yourself re-explaining the same thing to the agent in chat repeatedly, that is a context bug and the fix is to write it down in the appropriate layer, not to re-prompt better.

---

## Part 3 · Creating Skills

A skill is a unit of procedural knowledge. The clearest articulation came from Anthropic's October 2025 launch of Agent Skills and the December 2025 move to make the `SKILL.md` format an open standard. The killer property is **progressive disclosure** — the name and description always sit in context (a few dozen tokens), the body loads only when the model decides the skill is relevant, and any bundled files load only when the body references them. Effectively unbounded context per skill, near-zero idle cost.

For a Google engineering team using Gemini, you build the Skills pattern out of the primitives you already have. A directory in your repo called `skills/`, with one folder per skill, each containing a brief markdown file with a metadata header (name and one-sentence description) and a body describing the procedure.

### 3.1 · What belongs in a skill

A good skill captures something a senior engineer would say out loud while explaining how the team does X. The test for whether something deserves a skill is whether you would type the same paragraph twice. If yes, it is a skill.

Three properties separate skills that compound from skills that rot. They are narrow (one task, one outcome), they cite real artifacts (a link to last quarter's exemplar RFC, the actual postmortem template), and they have a clear failure mode written down (the section heading *"When this skill is the wrong tool"* matters more than people expect).

### 3.2 · Authoring with the agent

Anthropic's recommended workflow for writing Skills is "iterate with the model": do a task end-to-end with the assistant, then ask it to reflect on what worked, what failed, and what context would have made the work faster next time, and capture that into a skill. Within three to six months a team that does this consistently builds a library that is more valuable than any external tool you can buy.

### 3.3 · Skills versus Gems versus Agents

| Primitive | Best for | Lifetime | Autonomy |
|---|---|---|---|
| **Skill (in-repo)** | Procedural knowledge applied per task by the engineer's assistant | Years; checked in | Human is driving |
| **Gem (Workspace)** | Reusable role/workflow for non-code work — RFCs, retros, status updates | Months; shared via Drive | Human is driving |
| **Code Assist style guide** | Repo-wide review standards enforced automatically | Years; checked in | Inline review, human merges |
| **ADK agent (Agent Platform)** | Multi-step, durable, multi-tool, runs hours–days | Long-running service | Agent acts; humans approve |

Most teams will spend their first month building skills and Gems, never touching ADK, and that is correct.

### 3.4 · The hardest skill to write is the smallest one

The right size for a first skill is the smallest amount of text that, if pasted into a fresh chat, would meaningfully change the output for the better. Five hundred words is the upper limit. If a skill is more than a page, it is two skills.

---

## Part 4 · Tools and MCP

Skills tell the assistant *how* to do something with knowledge. Tools let the assistant actually *do* things. The Model Context Protocol has by May 2026 become the lingua franca: ~97 million monthly SDK downloads, 9,400+ public servers, native support across every major client. Google announced first-party remote MCP support for Google services in 2026, with Maps Grounding Lite live and Cloud Run, Cloud Storage, AlloyDB, Cloud SQL, Spanner, Looker, Pub/Sub, and Dataplex rolling out as managed remote MCP endpoints.

### 4.1 · The team-level decision

The two failure modes the community has named in 2026 are **context bloat** (GitHub's MCP server alone consumes ~55,000 tokens before the agent does any work) and **silent-leak** (third-party servers with weak auth can exfiltrate tokens before you notice).

The discipline is straightforward. Enable MCP servers per-project, not globally. Use Google's official remote servers for Google services. For internal-only tools, write a narrow MCP server that exposes only the verbs you need, gate it with OAuth 2.1 + PKCE, and forward the user's OAuth token per request. Filter the exposed tools by scope: a read-only token sees read tools, an admin token sees write tools.

### 4.2 · What to wire up first

Source-control surface → issue tracker → observability (read-only) → deployment system (read-only at first) → design-doc store. Gemini CLI's Plan mode restricts the agent to read-only tools and is the right default for any new server until you have observed it on real tasks.

### 4.3 · The internal LLM gateway pattern

Shopify's centralized LLM proxy is worth importing. A small infrastructure team owns a single internal gateway through which all AI calls flow. Engineers can use whichever client they prefer; the gateway handles authentication, cost attribution per team, model routing, redaction of secrets, and usage analytics. Every prompt, every response, every downstream user signal flows through one pipe, which becomes the substrate for evaluation and improvement.

---

## Part 5 · Human-in-the-Loop

This is the layer where Google's own published practice is the strongest reference. The OCTO post is explicit that the workflow changes inside Google in response to AI-authored code have been: Conditional LGTM, mandatory AI-generated test coverage, AI-generated risk summaries on PRs, and "digital quiet hours" to fight approval fatigue. The lesson the post draws is that human review is not the bottleneck to remove — it is the constraint to engineer around.

### 5.1 · Pick an autonomy taxonomy and write it down

| Level | Name | Example | When to use |
|---|---|---|---|
| **L1** | Assistive | Inline completions, Code Assist autocomplete | Hot keystroke loop, single-file edits |
| **L2** | Conversational | Gemini chat, Code Assist chat, Claude/Cursor | Multi-file changes, human steers |
| **L3** | Autonomous (bounded) | Background coding agents on a ticket | Bounded tickets, parallel runs, PR-as-output |
| **L4** | Autonomous teammate | Flaky-test repair, dep bumps, doc drift bots | Repetitive, scoped, reversible, low blast radius |
| **L5** | Agentic swarm | Planner/Worker/Judge fan-out, parallel agents | Research-grade, isolated repos only |

Higher is not better. L1 with a senior engineer steering is often more productive than L4 with no spec. Write down which work categories sit at which level on your team.

### 5.2 · PR-as-gate is the dominant pattern

The agent opens a PR. A human reviews it. CI runs. An AI reviewer surfaces likely issues. The merge button is the moment of consent. Branch protection should treat agent-authored CLs identically to human-authored ones. Simon Willison's rule: never open a PR with code you have not reviewed yourself.

### 5.3 · Risk-based approval routing

| Action category | Default routing | Rationale |
|---|---|---|
| Lint, formatting, doc regeneration | Auto-merge after CI green | Reversible, no semantic risk |
| Dependency bumps (patch, minor) | Auto-merge after CI green + security scan | Low blast radius, well-tested by CI |
| Refactor in single component | PR review, single reviewer | Semantic but localized |
| Cross-service API change | PR review, owner approval per service | Blast radius proportional to fanout |
| Schema migration, auth, secrets, PII handling | PR review + named senior approval | Irreversible or compliance-relevant |
| Production deploys, on-call config | Synchronous human, two-person rule | Highest blast radius |

### 5.4 · Evaluation and feedback loops

Three eval primitives: a golden dataset of 50–200 input/ideal-output pairs per critical skill, versioned in the repo; an LLM-judge regression run nightly or per-PR; a weekly human sample of 20–30 traces to keep the LLM judge calibrated. Capture explicit feedback but trust implicit signals more (edit distance, accept rate, revert rate, time-to-merge).

### 5.5 · Sandbox by default

For any agent with shell or write access, run it in a sandbox by default. Gemini CLI's Plan mode is the lighter-weight equivalent: read-only tools, no writes, until you have observed the run.

### 5.6 · Things that look like HITL but aren't

A thumbs-up nobody clicks. A reviewer who approves in under thirty seconds. A "confirm?" dialog on every action. Logging without review. An LLM judge without weekly human calibration. Approving a 2,000-line agent diff. None of these are HITL; they are theater. Force smaller units, bundle approvals, and surface metrics that catch the drift.

---

## Part 6 · The Recommended Rollout

**Week 1 · Context.** Write the repo-level `GEMINI.md` (symlinked to `AGENTS.md`). Turn on Gem sharing. Ship four Gems: RFC drafter, PR description writer, incident note-taker, code-review-comment explainer. Add a checked-in `skills/` directory with a README.

**Week 2 · Grounded knowledge.** Stand up two or three NotebookLM notebooks per domain area. Seed with RFCs, runbooks, on-call playbook. Generate Audio Overviews. Share via IAM-bound groups.

**Week 3 · Code Assist Enterprise.** Turn it on. Index the three to five repositories the team owns. Commit `.gemini/styleguide.md` to each. Add internal Markdown docs to the index.

**Week 4 · Gemini CLI + MCP.** Wire up the small set of MCP servers you actually need: source control, issue tracker, observability (read-only). Use Google's official remote servers. Default to Plan mode. Publish the team's HITL policy document.

**Month 2+ · Evaluation and selective autonomy.** Golden datasets per critical skill. Nightly LLM-judge regression. Weekly human review. Only now consider building an ADK agent for a recurring toil that has shown up in three or more retros.

---

## Part 7 · Anti-Patterns to Publish on the Team Wiki

**Context bloat and MCP server sprawl.** Enable per-project, not globally. Prefer Skills for procedural knowledge; reserve MCP for genuine tool access.

**Skill sprawl.** Skill descriptions are always in context; treat them like tool names — budget them, review them on every PR that adds one.

**Rule conflicts.** Keep one source of truth (`AGENTS.md` / `GEMINI.md`); let tool-specific files reference it rather than re-state it.

**Unreviewed PR dumping.** Shipping agent-written PRs you have not read is offloading review work onto teammates. Pin the rule; enforce with branch protection.

**Rubber-stamping and approval fatigue.** Require a one-line justification on approve, rotate approvers, audit the approve-without-comment rate monthly.

**Eval drift.** Version eval datasets next to code; re-baseline on every model swap.

**Auto-generated config files.** Hand-write the repo-level file. Every line earns its place.

---

## Part 8 · Onboarding a New Engineer

**Day 1–5:** read repo `AGENTS.md` + nested files + Audio Overviews; pair on one ticket per category with a teammate driving.

**Week 2–4:** own one ticket end-to-end with the assistant in the driver's seat; ship one skill back into the team library; consume the golden eval set for the skills they've been using.

**Month 2:** own one agent-instrumented workflow end-to-end; contribute one entry to the team's eval golden set.

**Month 3:** contribute to the regression eval suite or build an ADK prototype for a recurring toil. By the end of month three, they should be teaching the next new hire what their first three months taught them.

---

## Appendix A · Starter `GEMINI.md` / `AGENTS.md`

````markdown
# AGENTS.md — [Team name]

## Project
One paragraph: what this codebase is, who owns it, who the users are.
Primary languages: Go, TypeScript. Build system: Bazel.

## Setup
```
make bootstrap
make test
```

## How we work
- Format: `make fmt` before every commit.
- Test: `make test` is the green/red signal.
- Style: Google Go Style + the additions in docs/style.md.
- Comments: only where the *why* is non-obvious.

## Directories
- /api — generated; do not hand-edit
- /services/* — microservices; each has its own AGENTS.md
- /experimental — in-progress; do not refactor without asking

## What to do, what not to do
- Do prefer table-driven tests; httptest for handler tests.
- Do open small PRs (<400 lines).
- Do not introduce new dependencies without listing them in the PR.
- Do not modify /api by hand; regenerate from proto.
- Do not commit credentials, real customer IDs, or PII.

## PR conventions
- Title: `<area>: <imperative summary>` (50 chars max).
- Body: problem, change, test, rollback.

## Security
- Never log Authorization headers, tokens, or full user records.
- New endpoints require an entry in docs/auth-matrix.md.

## Where to look
- Architecture: docs/architecture.md
- Runbooks: NotebookLM "[Team] Runbooks"
- Style deep-dive: @docs/style.md
- Common skills: @skills/README.md
````

---

## Appendix B · Starter Skill

````markdown
# skills/write-rfc/SKILL.md

---
name: write-rfc
description: Draft a new RFC using the team template, voice, and section conventions.
---

# Writing an RFC for [team]

## When to use this skill
The work is a design decision that affects more than one person, will outlive
the current quarter, or changes a contract another team relies on.

## Template
1. **Problem** — what is broken, who feels it, what is the cost of doing nothing.
2. **Goals / non-goals** — each as a one-line bullet.
3. **Proposal** — the change. Cite existing code.
4. **Alternatives considered** — at least two, with the reason rejected.
5. **Risks and mitigations** — reversibility, blast radius, rollout plan.
6. **Open questions** — explicitly unresolved.
7. **References** — prior RFCs, design docs, prior art.

## Voice and length
- 1,500 words is the soft cap.
- Prefer concrete over abstract. Name actual files and APIs.
- One reviewer per stakeholder team.

## Exemplars (do not modify; reference only)
- @rfcs/0042-payments-idempotency.md
- @rfcs/0061-scheduler-rewrite.md

## When this skill is the wrong tool
- One-off ticket-level work: use a CL description.
- Org-wide policy change: needs a directional doc from leadership.
- Postmortem: use the postmortem skill.
````

---

## Appendix C · HITL Policy Skeleton

**Our autonomy levels.** Swarmia's five-level taxonomy. Default to L2 for unfamiliar work and step down or up explicitly per category.

**Default routing by category.** Filled in per the table in Part 5.3. Reviewed quarterly.

**Things we do not skip.** Every CL has a human reviewer. The author reads the agent's output before opening the PR. CI is a required signal, not a substitute. Production access stays two-person. Schema migrations are L1 only.

**Metrics we track.** Approve-without-comment rate (monthly). PR cycle time (weekly). Revert rate of AI-authored PRs (monthly). Eval golden-set scores per critical skill (per release).

**How we change this document.** When an incident, near-miss, or retro reveals a gap, we update the policy in the same CL as the postmortem.

---

## Appendix D · References

### Google internal practice

- [Chandra & Tabachnyk, *AI in Software Engineering at Google: Progress and the path ahead*](https://research.google/blog/ai-in-software-engineering-at-google-progress-and-the-path-ahead/)
- [Frömmgen & Kharatyan, *Resolving Code Review Comments with ML*](https://research.google/blog/resolving-code-review-comments-with-ml/)
- [Nikolov & Taneja, *Accelerating Code Migrations with AI*](https://research.google/blog/accelerating-code-migrations-with-ai/)
- [DIDACT: Large Sequence Models for Software Development Activities](https://blog.research.google/2023/05/large-sequence-models-for-software.html)
- [Tabachnyk et al., *Achieving Productivity Gains with AI-based IDE features* (ICSE LLM4Code 2026)](https://arxiv.org/abs/2601.19964)
- [Lee Boonstra, *When AI writes the code, who reviews it?* (Google Cloud OCTO, April 2026)](https://cloud.google.com/transform/when-ai-writes-the-code-who-reviews-it-cto-google-cloud)
- [DORA 2025 Report on AI-assisted software development](https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf)

### Gemini, Workspace, NotebookLM, Code Assist, Agent Platform

- [Tips for creating custom Gems (Gemini Apps Help)](https://support.google.com/gemini/answer/15235603?hl=en)
- [Sharable Gems announcement (Workspace Blog)](https://workspace.google.com/blog/product-announcements/5-ways-to-boost-your-teams-productivity-with-the-gemini-app-featuring-new-sharable-gems)
- [NotebookLM for enterprise (Google Cloud)](https://cloud.google.com/resources/notebooklm-enterprise)
- [Configure Gemini Code Assist code customization](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization)
- [Code review style guide (Gemini Code Assist)](https://developers.google.com/gemini-code-assist/docs/code-review-style-guide)
- [Introducing Gemini Enterprise Agent Platform](https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform)
- [Announcing official MCP support for Google services](https://cloud.google.com/blog/products/ai-machine-learning/announcing-official-mcp-support-for-google-services)
- [MCP servers with the Gemini CLI](https://google-gemini.github.io/gemini-cli/docs/tools/mcp-server.html)
- [Gemini CLI — GEMINI.md context files](https://google-gemini.github.io/gemini-cli/docs/cli/gemini-md.html)

### Cross-ecosystem patterns

- [agents.md (Agentic AI Foundation)](https://agents.md/)
- [Anthropic, *Equipping agents with Agent Skills*](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- [Simon Willison, *Claude Skills are awesome, maybe a bigger deal than MCP*](https://simonwillison.net/2025/Oct/16/claude-skills/)
- [Model Context Protocol — modelcontextprotocol.io](https://modelcontextprotocol.io/)
- [MCP Adoption Statistics 2026 (Digital Applied)](https://www.digitalapplied.com/blog/mcp-adoption-statistics-2026-model-context-protocol)
- [Inside Shopify's AI-first engineering playbook (BVP Atlas)](https://www.bvp.com/atlas/inside-shopifys-ai-first-engineering-playbook)

### Human-in-the-loop and evaluation

- [Swarmia, *Five levels of AI coding agent autonomy*](https://www.swarmia.com/blog/five-levels-ai-agent-autonomy/)
- [Anthropic, *Demystifying evals for AI agents*](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- [Simon Willison, *Anti-patterns in agentic engineering*](https://simonwillison.net/guides/agentic-engineering-patterns/anti-patterns/)
- [Simon Willison, *A field guide to sandboxes for AI*](https://www.alldevblogs.com/article/simon-willison/a-field-guide-to-sandboxes-for-ai)
- [Braintrust, *AI agent evaluation framework*](https://www.braintrust.dev/articles/ai-agent-evaluation-framework)
- [Vercel, *Eval-driven development*](https://vercel.com/blog/eval-driven-development-build-better-ai-faster)
- [Pragmatic Engineer, *How AI is changing software engineering*](https://newsletter.pragmaticengineer.com/p/how-ai-is-changing-software-engineering)

---

*Where the playbook cites internal Google practice, the cited Google publications are the source of record. Where it cites broader patterns, the references are the strongest public articulations the audit surfaced; adapt to your team's specific constraints.*
