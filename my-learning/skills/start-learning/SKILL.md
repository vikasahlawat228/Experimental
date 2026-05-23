---
name: start-learning
description: Kick off learning a brand-new topic — typically a Google service, an architecture I want to internalize, my team's domain (e.g., G1 Partnership), an adjacent team's system, or a Google-specific concept. Triggers when Vikas says "let's start learning X," "I want to learn the architecture of Y," "kick off a learning topic on Z," "teach me everything about <service/team>," or "let's go deep on <topic>." Does deep parallel research, scaffolds the topic folder, curates a research dump, plans a sequenced module curriculum, and hands off to daily-learning for the actual sessions.
---

# Start a new learning topic

## When to use this skill

Vikas wants to learn something substantial — a service his team owns, the architecture of a related team's system, a domain like "G1 Partnership," a class of internal tooling, a Google-specific concept. The kind of thing that will take multiple sessions and would otherwise be a sprawling pile of links and half-thoughts.

If a folder already exists under `topics/` for this topic, this is the wrong skill — use `daily-learning` instead.

## The procedure (seven steps)

### 1. Confirm topic and scope (in chat, ~2 minutes)

Ask in one short message — don't run a wizard:

- **What's the topic, in 5–15 words?** "G1 Partnership services and how they hang together," not "G1 stuff."
- **Your current relationship to it.** First encounter, refresher, going deeper for a specific reason?
- **The goal.** *What do you want to be able to do at the end?* "Debug an incident on it without paging the owners." "Lead a design review." "Onboard a teammate in an hour." "Have a strategic conversation about where it's going." Vague goals produce vague modules; push back if the goal is "understand it generally."
- **Rough time budget.** "Maybe 8 sessions of 30 minutes over two weeks." Doesn't have to be precise.
- **Starting pointers.** Code paths, design docs, go/ links, people whose brains to mine, prior teammates' writeups. Even one good pointer makes the research 10× sharper.

Read what he says, infer where you can, and proceed. One clarifying round is fine; two is over-asking.

### 2. Scaffold the topic folder (silent)

Copy `topics/_template/` to `topics/<topic-slug>/`. Slug is kebab-case derived from the topic name.

Populate `topic.md` from step 1: name, scope, goal, time budget, pointers, status. Set the "As of YYYY-MM-DD" line.

### 3. Deep research (silent, parallel agents)

Spawn **2–4 research agents in a single message**, each with a clear, narrow brief. Typical splits:

- **Architecture & data model** — what the system is, what it does, where the code lives, what the data flow looks like, what the entities are.
- **Rationale & history** — *why this design*. What was rejected and why. What constraints drove it. The "why" is the most-missing thing in public writeups; ask for it explicitly.
- **Operational reality** — how it's run day to day. Dashboards, common failure modes, the on-call experience, runbooks.
- **Adjacent context** — what teams depend on it, what it depends on, where the seams are, where ownership transitions happen.

For internal-only systems where the open web is limited, give every agent the same caveat: *"Surface what's available externally; explicitly list what would need to be filled in from internal sources, and produce that as a 'questions to chase' list."*

### 4. Curate into `research-dump/` (silent)

Don't dump raw agent output. Curate.

- Save the **6–10 strongest sources as named files** in `research-dump/`. `architecture-overview.md`, `design-rationale-from-2022-doc.md`, `recent-postmortem-summary.md`. One file per source, not a giant blob.
- Write `research-dump/INDEX.md` with:
  - **Sources kept** — file + one-line rationale for why each earned its place.
  - **Rejected and why** — what you looked at and discarded. This list teaches taste over time.
  - **Open questions to chase internally** — what the public web couldn't answer.

### 5. Plan the modules (silent, then checkpoint)

Draft 5–10 modules ordered by dependency. Each module gets a stub file in `modules/`:

```
modules/
├── M01-foundations.md         ← What this thing is, why it exists
├── M02-data-model.md          ← The core entities, the lifecycle
├── M03-request-flow.md        ← How requests move through the system
├── M04-failure-and-obs.md     ← Failure modes, dashboards, on-call view
├── M05-deploy-and-rollout.md  ← How it changes
└── M06-strategic-context.md   ← Where it fits in the bigger picture
```

Each stub contains: the module's **one-sentence promise**, the source(s) from the dump it draws on, the prior module(s) it depends on, and a placeholder for "what good output looks like" (filled in over time).

Then **show Vikas the plan in chat** — short list, one line per module — and ask: *"Does this shape work, or do you want to redirect?"* Honor any reshuffle he requests. Log the changes in `progress.md` under "reordered / merged / dropped."

### 6. Seed the learner-profile overlay (silent)

Create `learner-profile-overlay.md` and populate from step 1:

- **Entry point** — what he said he knew, **verbatim**.
- **Stated goal** — verbatim.
- The other sections (strengths, gaps, watchlist patterns, interests, pacing notes, overrides) stay empty for now — `daily-learning` fills them in over time.

### 7. Hand off (in chat, one line)

End with: *"Topic scaffolded. Next time you say 'next session' or 'let's do <topic-slug>,' I'll start with Module 01: <name>."*

## What good output looks like

A populated `topics/<slug>/` containing:

- `topic.md` with goal, scope, time budget, pointers.
- `research-dump/` with 6–10 named source files and an INDEX.md that includes the rejection list and open questions to chase internally.
- `modules/` with 5–10 sequenced stub files, each with a one-sentence promise.
- `learner-profile-overlay.md` with Vikas's verbatim entry-point and stated goal.
- `progress.md` initialized with the module list and an empty mastery table.
- A one-line handoff in chat to `daily-learning`.

The plan is reviewed and adjusted with Vikas before being treated as final. Silent re-planning is forbidden at every stage of this skill.

## When this is the wrong tool

- A folder for the topic already exists → use `daily-learning` to continue from where you left off.
- Vikas wants a one-off question answered ("what is X?") → answer the question; don't scaffold a topic just to look something up.
- The topic is genuinely tiny (one concept, one session) → still create a minimal folder for memory, but skip the module plan and jump straight to a single `daily-learning` session.
- The "topic" is actually a learning-loop change (e.g., "I want my sessions to be shorter") → that's a `learner-profile.md` update, not a new topic.
