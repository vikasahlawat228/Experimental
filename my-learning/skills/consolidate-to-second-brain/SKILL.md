---
name: consolidate-to-second-brain
description: Push durable knowledge from recent learning sessions into the second-brain (../../team-brain/) so it shows up in real work. Triggers at the end of a learning module (mastery ≥ 4 on the module's main concept), when Vikas says "push to second-brain," "consolidate this," "save this to team-brain," or "let's update the second-brain." Decides what's note material vs. what's skill material, drafts both, and waits for confirmation before writing.
---

# Consolidate to second-brain

## When to use this skill

A learning module has reached mastery ≥ 4, or Vikas asks to consolidate. The job is to translate what was learned into shapes the second-brain at `../../team-brain/` will keep using — exocortex notes (the durable facts and mental models) and possibly new skills (the repeatable moves).

The discipline is **propose, don't push**: every consolidation pass shows the proposed files and waits for Vikas's confirmation before writing. The second-brain is too important to write to silently.

## Procedure

### 1. Identify the module's durable content

Read the recent recap(s) in `recaps/` and the module file in `modules/`. Pull from `progress.md`'s insight log and concept graph. Ask:

- What did he **actually learn** — not what we covered, but what he can now reach for?
- What of that is **fact-shaped** (belongs in exocortex notes) vs. **move-shaped** (belongs in a skill)?
- Which of the "Questions I still have" from his notes did this module resolve?

Don't push fluff. Push what he'll reach for in real work.

### 2. Decide the targets in `../../team-brain/`

Route each piece by type:

| Learning produced... | Goes to... |
|---|---|
| Understanding of a specific service / system | `../../team-brain/exocortex/services/<name>.md` — use the eight first-pass questions from the `learn-new-service` skill, but now backed by what he actually learned, not "TODO." |
| A concept, mental model, or process | `../../team-brain/exocortex/concepts/<name>.md` |
| Context about a team's domain | `../../team-brain/exocortex/teams/<name>.md` |
| A new term, acronym, one-line definition | Append to `../../team-brain/exocortex/glossary.md` |
| A repeatable move (e.g., "how I debug a stuck job in this system," "how I read a request trace in this architecture") | Propose a new `SKILL.md` at `../../team-brain/skills/<skill-name>/SKILL.md` |

If the same module produces both a service note and a skill (common), propose both.

### 3. Draft each file

Use the templates in `../../team-brain/`:

- For exocortex notes: the note template at the top of `../../team-brain/exocortex/README.md`. Always include the `> As of YYYY-MM-DD:` line.
- For skills: the format described in `../../team-brain/skills/README.md`. Frontmatter (name, description), 200–500 word body, "When this is the wrong tool" section.

**Pull verbatim quotes** from Vikas's recap entries where they capture his mental model better than your paraphrase would. His phrasing is part of what makes the note feel like his.

### 4. Cross-link

For every new note proposed:

- Add a one-line entry to `../../team-brain/exocortex/INDEX.md` under the right bucket.
- Include a link from the new note **back to the source module** in `my-learning/topics/<slug>/modules/M<NN>-*.md`. Provenance matters; in six months he'll want to know where this understanding came from.
- Where existing exocortex notes are related, propose bidirectional references.

For every new skill proposed:

- Note it in the topic's `skills-index.md` (the pointer back from the learning side).
- Mention it in the new note(s) it pairs with.

### 5. Show, then write

Present the proposed changes in chat:

```
Proposed for the second-brain:

1. exocortex/services/<name>.md     (NEW)    — <one-line summary>
2. exocortex/concepts/<name>.md     (NEW)    — <one-line summary>
3. exocortex/INDEX.md               (APPEND) — adding 2 entries
4. skills/<skill-name>/SKILL.md     (NEW)    — <one-line summary>

Drafts below. Ready to write, or want to edit first?
```

Then paste the actual drafts. Wait for Vikas. If he says "go" → write. If he edits → write his version. If he says "skip <N>" → drop that one.

### 6. Update the source-side memory

After writing, in the topic folder:

- Update `topics/<slug>/skills-index.md` with pointers to any new skills.
- Note the consolidation pass in the relevant recap ("Consolidated to second-brain on YYYY-MM-DD: <files>").
- Resolve anything in `progress.md`'s "Questions I still have"-style queues that the consolidation addressed.

## What good output looks like

One to three proposed files (sometimes a fourth as a skill), each with:

- A clear path under `../../team-brain/`.
- A draft body following the relevant template, with the "As of YYYY-MM-DD" line.
- A one-line **rationale** for the routing decision ("Belongs in `concepts/` because it's a mental model I'll reach for outside this learning context, not a service writeup.").
- Cross-links proposed.

Then approval-then-write. Never silent.

## When this is the wrong tool

- The module hasn't solidified — mastery still 2 or 3 → don't push. The second-brain is for what's owned, not what's being acquired.
- The content is purely about the **learning process** ("I learned that I stall on data models") — that belongs in `learner-profile-overlay.md` and possibly the global `learner-profile.md`, not the second-brain.
- The content is **sensitive** (real customer data, secrets, PII, sensitive bug numbers) — don't write it anywhere in either system. Use placeholders, or tell Vikas to put it in the proper internal store.
- Vikas wants to **share** this with his team → the second-brain is personal. The team wiki is the right surface for shared writeups; consolidation here doesn't produce team-wiki content.
- The proposed note would just **duplicate** something already in the second-brain → propose an append/merge, not a new file. Show the diff.
