---
id: auth-service
type: pointer
area: "Auth & sessions"
owner: "@alice"
source_of_truth:
  - "services/auth/"
  - "https://docs.internal/design/auth-v2"
last_verified: 2026-06-03
related: [migrations, api]
---

# Auth & sessions — orientation

**What lives here:** session issuance/validation, OAuth callback handling, and the token-refresh path. Backed by Postgres (`auth.sessions`) + Redis (hot session cache).

**Entry points:** `services/auth/handler.go` (HTTP), `services/auth/session.go` (issuance/validation), `services/auth/oauth/` (providers).

**Watch out for:** token refresh is **not** idempotent across regions — see ⚠ `../gotchas/example-migration-ordering.md` for the related replay caveat, and the Design Doc §"Refresh races" for the canonical rule.

*(Example entry — replace with your real subsystems. Note it links to source of truth and a gotcha rather than restating either.)*
