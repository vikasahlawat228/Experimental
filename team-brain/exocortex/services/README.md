# services/

One file per service, system, or library I'm learning about. Architecture, data model, ownership, on-call, dashboards, known sharp edges, my open questions.

File naming: kebab-case, the service's actual name. `auth-frontend.md`, `spanner-y-replication.md`.

For first-pass notes on a brand-new service, use the `learn-new-service` skill — it walks you through the eight first-pass questions worth answering.

Suggested sections (adapt as needed):

```
# <service-name>

> As of YYYY-MM-DD: <One sentence — what this service does and why I care>.

## What it does
## Who owns it
## Where the code lives
## Design doc
## Data model
## Dependencies (what it uses, what uses it)
## How to observe it (dashboards, logs)
## Known sharp edges
## Questions I still have
## Links
```
