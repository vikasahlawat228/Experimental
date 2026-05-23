# exocortex

Free-form notes about things I am learning. Organized loosely by type. This will get messy — that is fine. The `weekly-consolidation` skill is the forcing function that keeps it usable.

## What goes where

| Bucket | Holds |
|---|---|
| `concepts/` | Google-specific concepts, processes, mental models. "What is a TI?" "How does the launch process work?" "How does our auth model differ from the public one?" |
| `services/` | Services, systems, libraries. One file per service. Architecture, ownership, on-call, data model, sharp edges. |
| `teams/` | Other teams I work with or depend on. What they own, their priorities, how we relate to them. |
| `people/` | Folks I work with regularly. Their role, what they own, what they care about. Light-touch, for me, not a CRM. No sensitive personal info. |
| `glossary.md` | Quick-lookup acronyms and terms, one line each. If a term needs more than a sentence, promote it to `concepts/`. |
| `INDEX.md` | Human-readable map of what is in here. Updated during weekly consolidation. |

## File naming

- kebab-case: `spanner-y-replication.md`, not `Spanner_Y_Replication.md`.
- No dates in filenames; dates live inside the file.
- If a service has multiple aspects (architecture vs. ops vs. data model), one file with sections beats four files.

## Template for a new note

Every note opens like this:

```markdown
# <Title>

> As of YYYY-MM-DD: <one sentence I would tell a teammate>.

## What I currently believe
<the actual content>

## Questions I still have
- ...

## Links
- Internal: go/...
- Code: //...
- Doc: ...
```

The "As of" line is what makes notes safe to write half-baked. I am allowed to be wrong; I am required to date it.

## When NOT to write a note

- It's a one-time lookup I will never need again.
- It's already authoritatively documented elsewhere and I have a link to it — add the link to `INDEX.md` rather than restating it.
- It would contain anything sensitive (secrets, PII, real customer data, sensitive bug IDs). Use placeholders or put it in the proper internal system.

## Growth rule

Don't pre-organize. Let structure emerge. If a subdirectory starts to dominate with 20+ files of one kind, split it then. Premature organization is harder to undo than late organization.
