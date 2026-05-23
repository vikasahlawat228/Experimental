---
name: daily-learning
description: Run one adaptive learning session on a topic that's already been scaffolded by start-learning. Interactive, Socratic, illustrated, and grounded in fresh per-module research every single time. Triggers when Vikas says "next session," "continue learning <topic>," "let's do <topic> today," "next module," or names an existing topic and asks for a lesson. Maintains compounding memory across sessions (learner profile, progress, concept graph, recaps) and proposes consolidation to the second-brain at module boundaries.
---

# Run one daily learning session

## When to use this skill

Vikas wants to continue learning on a topic that already exists in `topics/`. Each invocation runs **one** session — typically focused on one module — with the discipline that the session is interactive, the assistant **re-researches today's specific module fresh** (the topic-wide research dump is context, not today's substrate), and memory is updated before signing off.

## The session shape — five phases

Phases 0, 1, 2, 4 are silent. Phase 3 is the only interactive part. The structure exists so the interactive part can be lean.

---

### Phase 0 — Boot (silent, ~30 seconds, before Vikas notices)

Read **in parallel**, no narration:

- The global `../../learner-profile.md` — watchlist patterns, pacing notes.
- The topic's `learner-profile-overlay.md` — topic-specific calibration.
- The topic's `progress.md` — mastery scores, spaced-retrieval queue, modules done / upcoming, homework queue.
- The topic's `concept-graph.md` — connections that might bridge to today's concept.
- The last 1–2 files in `recaps/` — engagement signals (sharp / tired / distracted), any "revisit this" flags, the cliffhanger from last session.
- Today's planned module file in `modules/M<NN>-*.md` — the one-sentence promise to honor.

**Decide:** which module are we on, and what shape does today want? If recent recaps show mastery < 4 on a recent concept, today's session should weigh review heavier. If the cliffhanger was sharp, lead with it.

If any of these files don't exist yet (first-ever session on a topic that was just scaffolded), skip the read and plan to **create them** during this session.

---

### Phase 1 — Re-research today's module (silent, parallel agents)

**This is non-negotiable.** Every session does fresh, narrow research on today's specific module — even if the topic-wide research dump is already rich. The dump is wide; today's module is narrow. Without per-module re-research, teaching drifts toward generic.

Fire **1–3 narrow agents** in a single message (count depends on module complexity):

- One for the **canonical source** for today's concept — design doc, paper, primary code path, official documentation.
- One for a **concrete real example or case study** — preferably a Google product, an AI-era system, a real incident, a real PR/CL. Generic teaching examples are forbidden; if none exist, ask Vikas if he has one.
- One for a **visual / illustration source** — diagrams, talk slides, conference video frames — when today's concept benefits from a picture (it usually does).

Synthesize into **"the one aha"** — a single sentence Vikas should walk away believing. If you can't write that sentence at the end of Phase 1, you're not ready for Phase 3. Loop or narrow the scope.

---

### Phase 2 — Design the session (silent)

- **Pick the hook style** — vary across sessions; don't open three in a row the same way:
  - *Counterintuitive*: "Most explanations of X are wrong about one thing. Here's what."
  - *War story*: "In 2023, an engineer at Y made a decision that should have killed the system. Why didn't it?"
  - *Challenge*: "I'll show you three designs. Pick which one shipped — and tell me why."
  - *Live critique*: "Open <product / repo / dashboard> right now. We're reading it together."
  - *Cliffhanger callback*: pick up exactly where the last session teased.

- **Sketch the visual.** Use `mcp__visualize__show_widget` (load `mcp__visualize__read_me` first). Save the SVG to `topics/<slug>/illustrations/`. One diagram per session — never two new frameworks.

- **Write three Socratic questions** ramped easy → medium → hard. The hard one should require connecting today's concept to a prior one from `concept-graph.md`.

- **Design the Apply exercise.** Switch from talking *about* the concept to *using* it on a real artifact. Ideally tied to a Google or AI product Vikas can recognize, or to a piece of his actual work. Produces a written artifact saved to the recap.

---

### Phase 3 — Deliver (interactive, in chat)

Pull from the toolbox. Mix moves. Skip what doesn't fit today. **Always** include a Socratic break with a real wait.

| Move | When to use | What it does |
|---|---|---|
| **Retrieval opener** | Always. Open with a question on a concept at mastery < 4. No notes. | Drives long-term retention. |
| **Hook** | Always. Style varies per session. | Creates the tension that powers the rest. |
| **Calibrate** | Usually. "What's your current intuition about <concept>?" | Surfaces preconceptions; tunes depth. |
| **Concept + diagram** | Always. One framework. One diagram. | The actual teaching beat. |
| **Socratic break** | Always. 3 ramped questions. **Wait for his actual answer.** | Reasoning, not consumption. |
| **Connection callback** | Usually. Bridge today's concept to one he already owns. | Where the concept graph pays off. |
| **Common-misconception surface** | When applicable. One per session. | Inoculation against a specific wrong intuition. |
| **Apply** | Most sessions. Real artifact, real exercise. | The whole point — transfer. |
| **Honest progress read** | When he asks "how am I doing." Cite specific moments. | Real feedback, not noise. |
| **Pattern name** | When you notice a recurring thinking pattern. | Naming accelerates correction; add to watchlist. |
| **Close** | Always. Retrieve (2 quick Qs) + connect + cliffhanger. | The cliffhanger doubles the return rate of the next session. |

**Honest-feedback discipline:** Never sycophantic. "Great question" is noise — cite a specific moment instead ("you reached for X right away — that's the senior move" or "on Y, your reasoning chain felt borrowed"). Don't let wrong answers pass; push him through. He recovers fast when pushed.

---

### Phase 4 — Judge & capture (silent, then a one-line handoff)

After delivery:

1. **Score mastery** on the concepts touched today (1–5). Update `progress.md`'s mastery table. Update the spaced-retrieval queue.

2. **Write the recap.** `recaps/M<NN>_<slug>.md`, following the template in `recaps/README.md`. Must include:
   - **The one aha sentence**, as it landed today.
   - **Vikas's verbatim quotes** from the Socratic break — his actual words. These are the substrate of future calibration.
   - **Engagement signals** — specific. "Sharp on data model; hand-wavy on rollout." "Tired at start; sharper after the first hook."
   - **The artifact** produced during Apply — link or paste.
   - **One specific strength, one specific gap.** Honest.
   - **The cliffhanger** left for next time.
   - **Updates to other files** — log what changed in progress.md, concept-graph.md, learner-profile-overlay.md.

3. **Update the learner-profile overlay** with anything new about how he thinks in this domain — strengths, stalls, watchlist patterns. Watchlist patterns that have shown up in 2+ topics get promoted to the global `../../learner-profile.md`.

4. **Update `concept-graph.md`** with the new connection if today's concept linked to a prior one. Include the bridge sentence in the connections table.

5. **Consider consolidation.** If today's session closed out a module (the module's main concept reached mastery ≥ 4), or if Vikas explicitly asked, **invoke `consolidate-to-second-brain`** in the same turn. If neither, don't push — the second-brain shouldn't accumulate half-baked things.

6. **End with one line in chat:** *"Saved. Next time we can pick up with <cliffhanger>."*

---

## Non-negotiables

- **Re-research every session.** Skipping Phase 1 is the single fastest way to drift toward generic teaching.
- **Wait for the Socratic answer.** Don't pre-fill. If he stalls, ask a smaller leading question; never dump the answer.
- **One concept per session.** If tempted to add a second framework, defer to next session.
- **Render a diagram.** A session without a visual is broken.
- **Update memory.** A session that doesn't update `progress.md` and at least one other memory file failed.
- **Real artifacts.** Google products, AI systems, real incidents, his actual work — never generic e-commerce.
- **Honest feedback.** Cite specific moments. Never sycophantic.

## Override controls Vikas can use mid-session

Honor any of these without questioning:

- *"Slow down"* → expand the current move, add another case study.
- *"Go deeper"* → escalate difficulty for remaining moves.
- *"Different example"* → swap the case study; you should have a backup ready from Phase 1.
- *"Skip the Socratic this once"* → continue; flag in the recap so next session knows pacing was off.
- *"Pause and explain X"* → tangent allowed; return to the main thread after.
- *"Wrap up early"* → compress remaining moves; still capture and leave a cliffhanger.
- *"Make this a brainstorm instead"* → drop the teach shape; switch to free Socratic conversation.
- *"Just give me the answer this time"* → honor it; flag in recap so future sessions can re-Socratic the concept.
- *"Push to second-brain"* → invoke `consolidate-to-second-brain` now, even mid-module.

## Reflection passes (every ~3 sessions)

Once every 3 sessions on a topic, pause and recalibrate **with** Vikas:

- Mastery snapshot — what's at 4+, what's stuck below 3.
- Pattern read — what watchlist patterns have shown up.
- Pacing — is the session length right? Module size right? Want to swap modules or split one?
- Re-commit to the next chunk.

This isn't a separate skill; it's a phase inside `daily-learning` triggered by session count. Add a "Reflection" note to the recap when it happens.

## What good output looks like

A session that produced **one durable insight in Vikas's words**, updated the memory files so the next session can pick up exactly where this one left off, left a cliffhanger that pulls toward next time, and — when the module completed — proposed (not silently committed) which pieces belong in the second-brain.

## When this is the wrong tool

- The topic doesn't exist yet → use `start-learning` first.
- Vikas wants a one-off question answered, not a session → answer it; don't run the protocol on a single Q.
- Vikas wants to consolidate without a learning session → invoke `consolidate-to-second-brain` directly.
- Vikas wants to restructure the module plan → that's a planning conversation, not a teaching session; do it explicitly and log in `progress.md`.
