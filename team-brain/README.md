# team-brain

Personal knowledge system for everything I learn about my team, the services we touch, the people I work with, and the way Google does things. Designed to compound over time and to be queryable by my AI assistants.

## Two halves

**`exocortex/`** — free-form notes. What I currently know about specific things: services, concepts, teams, people, acronyms, internal tools. Grows continuously. Updated whenever I learn something or notice I'm wrong.

**`skills/`** — procedural knowledge. The repeatable moves I want my AI assistant to apply: "how I learn a new service," "how I prep for a cross-team meeting," "how I consolidate this directory on Fridays." Stays small and curated.

## The discipline that makes this work

1. **Write it down immediately.** If I learn something useful and don't capture it within an hour, I will lose it. A rough note beats no note.
2. **Be wrong on purpose.** Capture what I currently believe, dated. Correct it when I learn better. The audit trail is part of the value.
3. **Link liberally.** Notes that reference other notes compound. The `INDEX.md` is the map; concept and service notes are the territory.
4. **Consolidate weekly.** Friday 30 minutes: read what I added, move things, kill duplicates, strengthen links. See `skills/weekly-consolidation/`.

## How the AI assistant uses this

`GEMINI.md` at the root is the entry point Gemini CLI reads when invoked here. It tells the assistant who I am, points it at the skills, and sets the ground rules. When working from inside this directory I can say "use the `learn-new-service` skill" or "check exocortex for what I know about service X" and the assistant will read the relevant files.

For Gemini app / Gem usage: I can attach individual exocortex files as knowledge files to a Gem, or copy a `SKILL.md` body into a Gem's instructions to make it always-on for that Gem.

## Adding to this

| If I have... | It goes in... |
|---|---|
| Something I just learned about a service, concept, person, team | `exocortex/` (see `exocortex/README.md`) |
| A repeatable move I want my assistant to do consistently | `skills/` (see `skills/README.md`) |
| Don't know which | Default to exocortex. Promote to a skill if I find myself writing the same instructions to the assistant twice. |

## Worth saying out loud

This system is mine; it is not the team wiki. It is allowed to be opinionated, half-finished, and full of "I think" and "TODO verify." That is the point — the team wiki is the authoritative artifact, and this is my interpretation of it. The two are different jobs.

No secrets, no real customer data, no PII, no sensitive bug IDs in here. Use placeholders or put them in the proper internal system.
