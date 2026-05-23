# my-learning

The companion to `../team-brain/`. Where I do active, deliberate learning — typically about my team's services, the architecture of adjacent teams, Google-specific concepts I want to internalize, or domains I want to think clearer about.

The team-brain is the *result*; my-learning is the *factory*. Sessions happen here. When a module solidifies, the durable bits get pushed to the team-brain so they show up in real work.

## Two halves

**`topics/`** — one folder per learning topic. Inside each: the research dump from the initial deep-research pass, a planned module sequence, per-session recaps, a progress tracker, a concept graph, and a learner-profile overlay specific to that topic. The shape is captured in `topics/_template/`.

**`skills/`** — the procedural moves that drive sessions:

- **`start-learning/`** — kicks off a brand new topic. Deep parallel research, curated dump folder, planned module sequence.
- **`daily-learning/`** — runs one adaptive session on an existing topic. Interactive, Socratic, illustrated, with fresh per-module research every time. Maintains compounding memory across sessions.
- **`consolidate-to-second-brain/`** — at module boundaries (or on demand), pushes durable knowledge into `../team-brain/` so it shows up in real work, not just in recap files.

## How a session goes (the loop)

```
   Say: "Let's start learning <X>"
            │
            ▼
   start-learning → research-dump/, modules/, learner-profile-overlay
            │
            ▼
   Say: "Next session" or "Let's do <topic> today"
            │
            ▼
   daily-learning → Re-research today's module → Interactive teach →
                    Update progress + recap → (maybe) consolidate
            │
            ▼
   Module completes → consolidate-to-second-brain → team-brain grows
            │
            ▼
   Repeat with next module, or next topic
```

## What's in `learner-profile.md`

The global learner profile — who I am as a learner, across all topics. Read by `daily-learning` at session boot. Updated when the assistant notices something durable about how I think (a recurring pattern, an interest, a stalling pattern). Each topic also has its own overlay at `topics/<slug>/learner-profile-overlay.md` for topic-specific calibration that doesn't pollute the global picture.

## The non-negotiables

These aren't preferences; they're how sessions are kept honest.

1. **One concept per session.** No piling. If tempted to add a second framework, defer to the next session.
2. **Always Socratic.** Reach before reveal. Don't pre-fill the answer when I stall — ask a smaller leading question.
3. **Always illustrated.** A session without a diagram is broken. Render with the visualize widget.
4. **Always captured.** A session that doesn't update progress.md + at least one other memory file failed.
5. **Always re-research the module.** Even when the topic dump exists, today's module gets fresh narrow research. This is what keeps teaching from drifting toward generic.
6. **Real artifacts.** Examples come from Google products, AI systems, real incidents, my actual work — not generic e-commerce.
7. **Honest feedback.** Never sycophantic. Cite specific moments — "you reached for X right away" or "your reasoning on Y felt borrowed" — never "great question."

## Relationship to `../team-brain/`

| | my-learning | team-brain |
|---|---|---|
| Purpose | Active learning sessions | Durable knowledge I reach for |
| Lifetime | Sessions span days–weeks; topic folders archive when done | Years; the substrate of my work |
| Updated by | The two learning skills | `capture-new-knowledge`, `learn-new-service`, and `consolidate-to-second-brain` from this side |
| AI behavior | Interactive, Socratic, illustrated | Reference lookup, drafting, answering |

Things flow one direction: my-learning → team-brain. Never the other way; the team-brain is the source of truth, not a scratchpad.
