---
name: learn-new-service
description: First encounter with a service, system, or library I haven't worked with before. Helps me capture the right initial questions and produce a useful first-pass note. Use when I say "I'm looking at service X for the first time," "help me ramp on Y," or "I just got pointed at this system."
---

# Learn a new service

## When to use this skill

I am about to work with — or have just been pointed at — a service, system, or library that I haven't used before. Goal: come out of the first session with a usable mental model and a note I can return to.

## Procedure

1. **Create the file.** `exocortex/services/<service-name>.md`. Use the note template from `exocortex/README.md`. The filename should be the service's actual short name in kebab-case.

2. **Answer the eight first-pass questions.** Even if some answers are "TODO" or "I don't know yet," capture the question itself — it's the prompt for the next conversation:

   - **What does this service do, in one sentence?**
   - **Who owns it?** (team, tech lead, on-call rotation, owners file path)
   - **Where's the code?** (path / repo)
   - **Where's the design doc?**
   - **What does it depend on, and what depends on it?**
   - **What's the data model?** (what is the *thing* this service is about — the entity, the lifecycle)
   - **How do I observe it?** (dashboards, logs, what the on-call sees)
   - **What's known to be sharp?** (footguns, gotchas, "don't ever X")

3. **Capture my open questions** in a "Questions I still have" section. These become the things I ask next time I'm with someone who knows.

4. **Cross-link.** Add a one-line entry under "Services I've written up" in `INDEX.md`. If this service is owned by a team I already have a note on, add a reference from each side.

5. **Surface what to read next.** Suggest one specific artifact (a design doc, a code file, a runbook) I should look at to deepen the note. Don't suggest five — one I will actually open beats five I won't.

## What good output looks like

A 200–500 word note covering as many of the eight questions as I have answers to, with explicit TODOs for the rest, dated, with at least two links to real artifacts (code path, design doc, dashboard) and three or more entries in "Questions I still have." Honest about what I don't yet know.

## When this is the wrong tool

- It's a service I already have a file for → use `capture-new-knowledge` to append rather than overwrite.
- It's just a one-off lookup I won't return to → don't create a service file; the cost isn't worth it.
- It's a public/well-documented external service (e.g., Spanner SQL semantics, gRPC mechanics) → link to the canonical doc rather than restating it. Only capture *my team's* specific usage and gotchas in the note.
