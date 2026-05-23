---
name: consolidate-to-second-brain
description: Push durable knowledge from a completed learning module into the second-brain (../../team-brain/) so it shows up in real work. Triggers in two cases — when a module wraps (main concept ≥ 4 and promise delivered), or when Vikas explicitly says "push to second-brain," "consolidate this," or "save this to team-brain." Decides what's note material vs. what's skill material, may propose restructuring the second-brain when it has grown unwieldy, drafts everything, and waits for confirmation before writing.
---

# Consolidate to second-brain

## When to use this skill

Invoked by `daily-learning` when a module wraps, or directly by Vikas at any time. The job is to translate what was learned into shapes the second-brain at `../../team-brain/` will keep using — exocortex notes (durable facts and mental models) and possibly new skills (repeatable moves).

The discipline is **propose, don't push**: every consolidation pass shows the proposed files and waits for Vikas's confirmation before writing. The second-brain is too important to write to silently.

## The two triggers

| Trigger | What it means |
|---|---|
| **Module wrap** | The module's main concept hit mastery ≥ 4 *and* the module's "one-sentence promise" has been delivered. Invoked by `daily-learning` Phase 4. |
| **On demand** | Vikas asked. Honor immediately. |

Session-end without a module wrap is **not** a trigger. The recap captures the session; the second-brain waits.

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

### 7. (When the second-brain has grown) Propose restructuring

The second-brain is a living artifact. After a topic has dropped 5+ modules' worth of content, or a directory has 8+ files, or two notes start overlapping, the cleanest consolidation is often a **restructure**, not another append. This skill is allowed — and expected — to propose restructuring when it sees the need.

**Triggers that should make you propose restructuring (any one is enough):**

- A directory in `../../team-brain/exocortex/<bucket>/` has more than ~8 files and they fall into clear sub-themes.
- Two existing notes have grown overlapping content and would be clearer as one merged note or as a split along a different axis.
- The new content you're about to propose would create a clearer abstraction than the current shape (e.g., a new "subsystem-X-overview.md" that lifts repeated content out of three service files).
- The file you're proposing belongs equally in two buckets (concepts and services, say) — that's a signal the bucketing might want to change.
- You'd otherwise be appending to a file that's now > ~600 words and getting hard to skim.

**Restructuring moves you may propose:**

- **Split** a file into two or more along a clearer axis (architecture vs. operations, current vs. historical, etc.).
- **Merge** two overlapping files into one, with a one-line "see also" left at the old paths if they were linked from elsewhere.
- **Promote** a section that's grown into its own note (e.g., a "Data model" section inside a service file becomes `data-model-<service>.md`).
- **Add a sub-directory** when a flat bucket has gotten unwieldy (e.g., `exocortex/services/` → `exocortex/services/payments/`, `exocortex/services/auth/`, …). Move the existing files. Update `INDEX.md`.
- **Lift** a recurring mental model that shows up in several service notes into a `concepts/` note that the service notes then link to.

**Rules for restructuring:**

- **Always propose, never silently restructure.** Show Vikas a diff-style summary: "Move these N files into a new subdir; merge X and Y into Z; lift this section into a new concepts note." Wait for his call.
- **Preserve provenance.** When you move or merge, preserve the "As of YYYY-MM-DD" lines and the link back to the source `my-learning` module that produced the content. Don't rewrite history.
- **Update `INDEX.md` in the same pass.** A restructure that doesn't update the index is half-done.
- **Don't restructure for the sake of it.** The bar is "the new shape will be materially clearer to read in six months." If you can't articulate that benefit in one line, leave the structure alone.

If no restructuring is warranted, skip step 7. Most consolidation passes will skip it; that's fine.

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
