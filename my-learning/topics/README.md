# topics/

One folder per learning topic. Each topic is something I'm deliberately learning — a service, an architecture, a domain, a concept — that will take multiple sessions and is worth keeping memory for.

## Naming

kebab-case slug from the topic name. Examples: `g1-partnership-services`, `spanner-internals`, `ranking-architecture`, `vertex-agent-builder`.

## What's inside a topic folder

The `_template/` directory shows the layout. Every topic folder created by `start-learning` looks like this:

```
<topic-slug>/
├── topic.md                       ← topic overview, scope, goal, status
├── research-dump/                 ← curated research from start-learning
│   ├── README.md
│   ├── INDEX.md                   ← what's here + rejection list + open questions
│   └── <named source files>
├── modules/                       ← sequenced module files
│   ├── README.md
│   └── M01-<slug>.md, M02-<slug>.md, ...
├── recaps/                        ← one file per completed session
│   └── M01_<slug>.md, ...
├── illustrations/                 ← saved SVGs from the visualize widget
├── progress.md                    ← mastery × concept; queue; logs
├── concept-graph.md               ← how concepts in this topic connect
├── learner-profile-overlay.md     ← topic-specific calibration
└── skills-index.md                ← application skills captured (pointers to ../../team-brain/skills/)
```

## Lifecycle

- **Created** by `start-learning` when I begin a topic.
- **Grown** by `daily-learning` over many sessions.
- **Periodically drained** to `../team-brain/` by `consolidate-to-second-brain` as modules solidify.
- **Archived** (moved to `topics/_archive/` or deleted) once I've internalized the topic and the durable bits live in the second-brain. Recaps stay as a learning history.
