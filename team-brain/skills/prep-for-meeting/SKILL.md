---
name: prep-for-meeting
description: Get me ready for a cross-team meeting in 10 minutes by pulling the relevant exocortex notes, surfacing my open questions, and producing a one-page brief. Use when I say "prep me for X meeting," "help me get ready for the Y sync," or share a meeting topic and ask for a brief.
---

# Prep for a meeting

## When to use this skill

I have a meeting coming up — design review, cross-team sync, 1:1 with someone from a related team, decision meeting — and I want to walk in ready. The goal is a 5–10 minute prep that produces a one-page brief I can read on the way.

## Procedure

1. **Ask me for the inputs** if I haven't given them:
   - Meeting topic, in one sentence.
   - Attendees, especially anyone I might have a note on in `exocortex/people/`.
   - Any pre-read doc URL or title.

2. **Pull from my exocortex.** Grep and read:
   - Notes on the services / systems the topic touches (`exocortex/services/`).
   - Notes on the teams of any attendees (`exocortex/teams/`).
   - Notes on the people themselves (`exocortex/people/`).
   - Any open questions I had in related notes that might come up.

3. **Produce the brief** with these sections:

   - **TL;DR** — what this meeting is about, in one sentence.
   - **What I bring** — my position, decisions I'm carrying, things I want to be clear on.
   - **What I want out of it** — the outcome I would take.
   - **Open questions to raise** — pulled from my exocortex, tied to whichever attendee or system they relate to.
   - **What I don't know yet** — explicit gaps I should flag in the meeting rather than hide.
   - **People to listen for** — anything notable from `exocortex/people/` about how attendees work or what they care about.

4. **Don't invent.** If my exocortex has no notes on a relevant person or service, say so — don't fabricate context. A blank section labeled "I have no notes on this — TODO" is more useful than a plausible-looking fiction.

## What good output looks like

One page of prose, scannable in 5 minutes. Confident about what's in my notes, explicit about what isn't. Specific — "Ask Y about whether decision Z was made" beats "raise questions about Z."

## When this is the wrong tool

- The meeting is purely tactical (standup, status sync) — overkill, skip.
- I have no relevant notes at all → a better use of the 10 minutes is to skim the pre-read; tell me that.
- I'm asking to *write* meeting notes after the meeting → that's a different skill (write one if you find yourself doing it twice).
