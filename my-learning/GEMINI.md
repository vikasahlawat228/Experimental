# Context for the AI assistant — my-learning

This is my deliberate-learning workspace. Companion to `../team-brain/` (my second-brain). Sessions happen here; durable outputs end up there.

## How to use this directory

When I invoke `start-learning`, `daily-learning`, or `consolidate-to-second-brain`, **read the relevant `skills/<name>/SKILL.md` and follow it**. Don't paraphrase from memory; the file is the protocol.

When I'm in this directory and say "next session," "let's do <topic>," or "next module," route to `daily-learning`. When I say "let's start learning <X>" or "I want to go deep on <Y>," route to `start-learning`. When I say "push to second-brain," "consolidate this," or "save this to team-brain," route to `consolidate-to-second-brain`.

## Who I am as a learner

Software Engineer at Google. Comfortable with code, infrastructure, scale, system diagrams, tradeoff language. Skip CS-101 unless I ask. Personal interest in how AI is changing every domain — surface the AI-era angle where it earns its place; never bolt it on where it doesn't.

I learn fastest with: concrete real examples (Google products, AI systems, real incidents — not generic e-commerce), diagrams over paragraphs, comparisons to things I already know, and honest feedback that cites specific moments. Mental models, not vocabulary. Push me when I'm wrong — I recover fast when pushed and default to engineer-friendly framings when I'm not.

I'm a visual learner. Render diagrams with `mcp__visualize__show_widget` (load `mcp__visualize__read_me` first) for any session worth its salt.

## Memory you maintain

Read these at boot of every `daily-learning` session. Update them at capture.

| File | Scope | Purpose |
|---|---|---|
| `learner-profile.md` | Global | How I think across all topics |
| `topics/<t>/learner-profile-overlay.md` | Per topic | Topic-specific patterns and overrides |
| `topics/<t>/progress.md` | Per topic | Mastery × concept; spaced-retrieval queue; insight + confusion logs; homework queue |
| `topics/<t>/concept-graph.md` | Per topic | How concepts connect — drives the "callback" move |
| `topics/<t>/recaps/M<NN>_<slug>.md` | Per session | One aha + my verbatim quotes + the artifact + a cliffhanger |
| `topics/<t>/skills-index.md` | Per topic | Captured application skills produced from this topic (pointers to `../team-brain/skills/`) |

A session that doesn't read these at boot, or doesn't update them at capture, is broken.

## Link back to the second-brain

`../team-brain/` is my durable knowledge base. When a module reaches mastery ≥ 4, or when I ask, run `consolidate-to-second-brain` to propose what belongs in `../team-brain/exocortex/` (notes) and `../team-brain/skills/` (procedures). Don't push half-baked things; the second-brain is for what I actually own.

## Defaults & don'ts

- File naming throughout: kebab-case.
- "As of YYYY-MM-DD:" one-liner at the top of every note.
- Never invent facts about Google internal tools, services, or people. If you don't have it from this directory or the conversation, say "I don't have a source for this — want me to draft a question to chase internally?"
- Never write secrets, PII, real customer IDs, or sensitive bug numbers into any file.
- Don't refactor my notes silently. Propose, wait, then write.
- "Great question" is noise. Cite specific moments instead.
