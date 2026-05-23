---
name: capture-new-knowledge
description: When I have just learned something about my team or Google that I want to keep, decide where it goes and draft the note. Use whenever I say "save this," "write this down," "note that...," or finish a learning session and want to record the takeaways.
---

# Capture new knowledge

## When to use this skill

I have just learned something useful — from a conversation, a doc, a code walk, an incident, a meeting. It might be a fact, a mental model, a piece of jargon, a person's role, or a sharp edge of a system. I want to keep it before I lose it.

## Procedure

1. **Decide the type.** Route by what kind of thing this is:
   - A specific service / system / library → `exocortex/services/<name>.md`
   - A concept, process, or mental model → `exocortex/concepts/<name>.md`
   - A team I work with → `exocortex/teams/<name>.md`
   - A person → `exocortex/people/<name>.md`
   - A one-line acronym or term → append to `exocortex/glossary.md`
   - Genuinely unclear → default to `concepts/` and ask me.

2. **Check for existing notes first.** Grep across `exocortex/` for the key term. If a file already exists, add to it rather than creating a duplicate. Show me what you found before deciding.

3. **Draft the note** using the template at the top of `exocortex/README.md`. Always include the `> As of YYYY-MM-DD:` one-liner — that's the part future-me will skim.

4. **Propose links.** Suggest links to other notes I already have (look for related concepts, services, people, teams) and to any external artifacts I mentioned (go/ links, code paths, design doc URLs).

5. **Tell me the path.** Show me where you saved it. If you created a new subdirectory, mention it explicitly.

## What good output looks like

A short note (50–300 words) with a one-sentence summary at the top, the content I actually cared about, at least one "Questions I still have" entry if any popped up during the conversation, and a couple of links. Honest about what I don't yet know — TODOs are fine, fabrications are not.

## When this is the wrong tool

- I'm asking you to *find* something I already know — use grep/read on the existing notes; don't write a new one.
- The information is sensitive (secrets, real customer IDs, PII, sensitive bug numbers) — don't write it here. Use placeholders or tell me to put it in the proper internal system.
- It would just duplicate something authoritative I already have a link to — add the link to `INDEX.md` instead of restating the content.
- It's a one-time lookup I will never need again — don't bother.
