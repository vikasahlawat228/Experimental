# skills

Procedural knowledge I want my AI assistant to apply consistently. Each skill is a small folder containing a `SKILL.md` that describes one specific move.

## Anatomy of a skill

Frontmatter (always, at the top of the file):

```yaml
---
name: skill-name-in-kebab-case
description: One sentence the assistant reads to decide when to invoke this skill. Be specific.
---
```

The `description` is doing real work — it is the only part of the skill the assistant sees before deciding whether to invoke. Write it for clarity, not for flourish. "Use when starting a new RFC about a system that touches more than one team" is better than "for writing design docs."

Body (200–500 words is the sweet spot):

1. **When to use this skill.** The trigger condition. Specific.
2. **The procedure.** Numbered steps or prose, whichever fits the move.
3. **What good output looks like.** A short example or a pointer to one.
4. **When this is the wrong tool.** Explicit. The most useful section.

## Rules of thumb

- **One skill, one move.** If you have two moves, you have two skills.
- **Cite real artifacts.** "Use our RFC template" → link to the actual template or paste the headings. Generic instructions produce generic output.
- **Negative constraints work.** "Don't include a TL;DR" beats "be concise."
- **500 words is the cap.** If a skill is longer, it is two skills.

## How to create a new skill

1. Copy `_template/` to `<your-skill-name>/`.
2. Edit the new `SKILL.md`: name, description, body.
3. After your next non-trivial task, ask the assistant: "what context or skill would have made this faster next time?" Capture the answer back into a skill.
4. Iterate. Skills get materially better the second and third time you use them — the first version is rarely the right one.

## Invoking a skill

When chatting with Gemini in this directory, say "use the `<skill-name>` skill" or "apply the prep-for-meeting skill." The assistant will read the `SKILL.md` and follow it.

For Gemini-app / Gem usage outside the CLI: copy a `SKILL.md` body into a Gem's instructions to make it always-on for that Gem. Attach relevant exocortex files as the Gem's knowledge files.

## Existing skills

- **`capture-new-knowledge/`** — when I learn something, where the note goes and how to draft it.
- **`learn-new-service/`** — first encounter with a service or system.
- **`prep-for-meeting/`** — get me ready for a cross-team meeting in 10 minutes.
- **`weekly-consolidation/`** — Friday review of the exocortex.

## When to write a new skill versus a new exocortex note

If it's a *fact* about my world → exocortex. If it's a *move* I want to repeat → skill. If it's both → exocortex for the fact, optional small skill that references the fact. If you're not sure, default to exocortex; promote to a skill once you've written the same instructions to the assistant twice.
