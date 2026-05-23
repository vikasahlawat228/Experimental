# Context for the AI assistant

This is my team-brain: a personal knowledge system about my team and Google. Treat `exocortex/` as my notes and `skills/` as procedures I want you to apply.

## Who I am

Software engineer at Google. I learn fastest with concrete examples, named real-world artifacts, and comparisons to things I already know. I prefer terse, direct answers — skip the framing sentences and "I'd be happy to help."

## How to use this directory

When I ask about a service or concept, **check `exocortex/` first** before generalizing from training data. If a relevant file exists, prefer what's there over your general knowledge — my notes reflect my team's actual usage.

When I invoke a skill ("use the learn-new-service skill" or "apply prep-for-meeting"), read `skills/<name>/SKILL.md` and follow it. Don't paraphrase the skill from memory; read it.

When I learn something new, help me capture it. Propose where it goes in the exocortex (or whether a new note is even needed), draft the note using the template at the top of `exocortex/README.md`, and tell me the path you used.

## Defaults I prefer

- **File naming** in `exocortex/`: kebab-case, no dates in filename. Dates live inside the file as the "As of YYYY-MM-DD" line.
- **Note shape**: every new note opens with a one-sentence "As of YYYY-MM-DD" summary. That line is what I will skim later, so make it earn its keep.
- **Linking**: liberal. A note that doesn't link to other notes or to real artifacts (go/, code paths, design docs) is a dead end.
- **Length**: notes 50–500 words. Skills 200–500 words. If something is longer, split it.

## What not to do

- **Don't invent facts** about Google internal tools, services, or people. If I haven't told you in this directory or in the conversation, say "I don't have notes on this — want me to draft questions to ask the team?"
- **Don't refactor my notes silently.** If you would reorganize, propose the move and wait.
- **Never write secrets, PII, real customer IDs, or sensitive bug numbers** into files here. Use placeholders.
- **Don't manufacture work** during weekly consolidation. If I didn't touch anything, say so.

## Skills available in this directory

- `capture-new-knowledge/` — when I learn something, where the note goes and how to draft it.
- `learn-new-service/` — first encounter with a service or system.
- `prep-for-meeting/` — get me ready for a cross-team meeting in 10 minutes.
- `weekly-consolidation/` — the Friday review ritual.

New skills get added under `skills/<kebab-case-name>/SKILL.md`. The format is described in `skills/README.md` and a starter copy lives in `skills/_template/SKILL.md`.

## Source of truth

The team wiki, design docs, and code are authoritative. This directory is my interpretation. If you have access to the source and a note here contradicts it, flag the contradiction — don't silently align to either side.
