---
name: weekly-consolidation
description: The Friday ritual. Skim what I added this week, kill duplicates, strengthen links, update INDEX, surface stale open questions, propose new skills. Use when I say "let's consolidate," "Friday review," "weekly cleanup," or at the end of the week.
---

# Weekly consolidation

## When to use this skill

End of the week. 30 minutes. The forcing function that keeps the exocortex usable instead of letting it rot into a pile of half-thoughts.

## Procedure

1. **List what I touched this week.** Use filesystem mtime under `exocortex/` (or `git log --since="7 days ago"` if it's a repo). Group by directory.

2. **For each new or modified note, ask:**
   - Is the `> As of YYYY-MM-DD:` line still current? Update it where I've learned more.
   - Are there obvious links to other notes I should add? Bidirectional where possible.
   - Anything in here that's now wrong? Mark it explicitly (don't silently rewrite — show me).

3. **Check for duplicates.** If two notes cover overlapping ground, propose a merge. Don't merge silently; show me both and let me decide.

4. **Update `INDEX.md`:**
   - Add one-line entries for new notes.
   - Refresh "active question threads" by scanning the "Questions I still have" sections across notes.
   - Update "recently changed."

5. **Surface stale open questions.** If a question has been on a note for more than two weeks with no movement, flag it. Either it's still important and I should ask someone, or it's no longer relevant and I should resolve it.

6. **Propose new skills.** If I've been writing similar instructions to the assistant three or more times this week (you'll see it in conversation patterns I share, or I'll mention it), suggest a new skill that would capture the move.

## What good output looks like

A short report (around 150 words) covering: files touched this week, suggested merges with paths, stale questions worth chasing, suggested new skills. I make the calls; you propose. No silent edits.

## When this is the wrong tool

- I haven't added anything this week → no-op. Tell me so explicitly. Don't manufacture work to look productive.
- It's not end-of-week and I'm just curious what's in here → use grep/read, not this skill.
- I want to do a deeper restructure (renaming buckets, moving large numbers of files) → that's a separate session; this skill is the lightweight weekly pass.
