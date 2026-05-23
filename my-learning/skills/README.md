# skills

The three skills that drive `my-learning`. Each one move, each one purpose.

| Skill | Job | When to invoke |
|---|---|---|
| **`start-learning/`** | Kick off a brand-new topic. Deep parallel research, curated dump, planned module sequence. | "Let's start learning X" / "I want to go deep on Y" / "Teach me everything about Z" |
| **`daily-learning/`** | Run one adaptive session on an existing topic. Interactive, Socratic, illustrated; maintains memory; re-researches the specific module each time. | "Next session" / "Let's do <topic> today" / "Next module" / "Continue <topic>" |
| **`consolidate-to-second-brain/`** | Push solidified learning into `../../team-brain/` (notes + skills) so it shows up in real work. | "Push to second-brain" / "Consolidate this" / Or auto-invoked by daily-learning at end of a module |

## Anatomy

Each skill has a `SKILL.md` with YAML frontmatter (`name`, `description`) plus a body. Same format as `../../team-brain/skills/`. Use `_template/SKILL.md` as the starter if you ever add a new learning-loop skill.

## Where new skills go

**Most application skills you produce while learning belong in `../../team-brain/skills/`**, not here. The skills in this directory are for the *learning loop itself*; the skills they help you capture (taste-teardown, debug-this-system, postmortem-writeup, whatever) go to the second-brain so they're invocable in real work.

The `consolidate-to-second-brain` skill is the one that decides when a learning module has produced a capture-worthy procedure and proposes it to the second-brain side.

## Override controls for `daily-learning`

Mid-session, any of these will be honored:

- *"Slow down"* — expand the current move, add a case study.
- *"Go deeper"* — escalate difficulty.
- *"Different example"* — swap the case study; a backup is ready from Phase 1.
- *"Skip the Socratic this once"* — continue; flagged in the recap.
- *"Pause and explain X"* — tangent allowed; return after.
- *"Wrap up early"* — compress remaining moves; still capture + leave a cliffhanger.
- *"Make this a brainstorm instead"* — drop the teach shape; free Socratic conversation.
- *"Push to second-brain"* — invoke `consolidate-to-second-brain` mid-module.
