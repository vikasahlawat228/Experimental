# Rule 00 — single source of truth

This `.agents/rules/` directory (read natively by Antigravity, and mirrored by other IDEs) must stay **thin**. It exists only to point agents at the real source of truth.

- **Behavioral instructions:** see the root [`AGENTS.md`](../../AGENTS.md). Do not duplicate it here.
- **Where things are / gotchas:** navigate [`knowledge/index.md`](../../knowledge/index.md).
- **How the system is allowed to change:** [`governance/RULES.md`](../../governance/RULES.md).

> Why so thin: duplicated rules across files **drift apart** and silently fork behavior. One source of truth (`AGENTS.md`), pointed to from everywhere. Tool-specific files (`CLAUDE.md`, `GEMINI.md`) should `@import` or symlink `AGENTS.md`, never copy it.

**Org precedence reminder:** when the org layer exists, it sits *above* this team layer and is non-overridable. Nothing in `.agents/` may contradict an org standard.
