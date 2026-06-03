"""
context_freshness_callback — L1/L5 just-in-time, fresh context injection (ADK binding).

SKELETON (per-agent callback, not a global Plugin — it's agent-specific behavior).
Before the agent runs, it injects the FRESHEST high-signal pointers and warns if any
knowledge entry is stale. Embodies two tenets: "point to source / retrieve live" and
"curate, don't accumulate" — we inject a tiny, current pointer set, not the whole KB.

Verify against https://google.github.io/adk-docs/callbacks/types-of-callbacks/.
"""

from __future__ import annotations
import datetime as dt
from pathlib import Path
from typing import Any, Optional

KNOWLEDGE_DIR = Path(__file__).resolve().parents[1].parent / "knowledge"
STALE_AFTER_DAYS = 90


def before_agent_callback(*, callback_context: "Any") -> Optional["Any"]:
    """Inject the index + flag stale entries. Returning None = proceed normally."""
    index = (KNOWLEDGE_DIR / "index.md")
    stale = _stale_entries()

    # Keep it SMALL: inject the navigable index (pointers), not the documents themselves.
    # The agent follows pointers and fetches detail on demand (JIT) — avoids context rot.
    preamble = "## Knowledge index (navigate; fetch detail on demand)\n"
    preamble += index.read_text()[:4000] if index.exists() else "(index missing)\n"
    if stale:
        preamble += "\n⚠ STALE knowledge (re-verify before trusting): " + ", ".join(stale) + "\n"

    # Append to the agent's working context via whatever ADK state mechanism you use, e.g.:
    # callback_context.state["temp:knowledge_preamble"] = preamble   # temp: = discarded after turn
    _ = preamble
    return None


def _stale_entries() -> list[str]:
    """Flag pointers/gotchas whose last_verified is older than STALE_AFTER_DAYS."""
    out: list[str] = []
    today = dt.date.today()
    for md in list(KNOWLEDGE_DIR.glob("pointers/*.md")) + list(KNOWLEDGE_DIR.glob("gotchas/*.md")):
        if md.name.startswith("_"):
            continue
        lv = _front_matter_date(md, "last_verified")
        if lv and (today - lv).days > STALE_AFTER_DAYS:
            out.append(md.stem)
    return out


def _front_matter_date(path: Path, key: str) -> Optional[dt.date]:
    try:
        for line in path.read_text().splitlines():
            if line.strip().startswith(f"{key}:"):
                raw = line.split(":", 1)[1].strip()
                return dt.date.fromisoformat(raw)
    except Exception:
        return None
    return None


# A scheduled version of _stale_entries() is the L6 "freshness job" that opens prune PRs
# (RULES.md §R7). Same logic, run on a cron instead of per-agent-turn.
