"""
GuardrailPlugin — L5 deterministic enforcement (Google ADK binding).

SKELETON. Maps the portable "hard rules are hooks, not prose" principle (RULES.md §R9)
onto an ADK Runner-level Plugin. A Plugin registers once on the Runner and applies to
EVERY agent/model/tool, with precedence over per-agent callbacks — the right place for
team/org-wide non-negotiables.

Verify signatures against https://google.github.io/adk-docs/plugins/ before running.
"""

from __future__ import annotations
from typing import Any, Optional

# from google.adk.plugins import BasePlugin          # real import
# from google.adk.tools import BaseTool, ToolContext
# from google.adk.models import LlmRequest, LlmResponse


# --- policy config (keep declarative; ideally load from a shared org policy file) ---
DENIED_TOOLS = {"shell_rm_rf", "prod_db_write", "force_push"}
SECRET_PATTERNS = (
    r"AKIA[0-9A-Z]{16}",          # AWS key
    r"-----BEGIN .*PRIVATE KEY-----",
    r"(?i)bearer\s+[a-z0-9._-]{20,}",
)


class GuardrailPlugin:  # (BasePlugin)
    """Blocks dangerous tools and refuses to send secrets to the model/tools."""

    # Returning a value SHORT-CIRCUITS the call. Returning None lets it proceed.

    async def before_tool_callback(
        self, *, tool: "BaseTool", tool_args: dict, tool_context: "ToolContext"
    ) -> Optional[dict]:
        # 1) Deny-list enforcement (deterministic — never left to the model).
        if tool.name in DENIED_TOOLS:
            return {  # non-None dict => tool is skipped, this is returned instead
                "status": "blocked",
                "reason": f"Tool '{tool.name}' is denied by GuardrailPlugin (RULES.md §R9).",
            }
        # 2) Secret-scan tool arguments before anything leaves the boundary.
        if _contains_secret(str(tool_args)):
            return {"status": "blocked", "reason": "Potential secret in tool args; call refused."}
        return None  # allow

    async def before_model_callback(
        self, *, llm_request: "LlmRequest"
    ) -> Optional["LlmResponse"]:
        # Redact/refuse if a secret is about to be sent to the model.
        if _contains_secret(_request_text(llm_request)):
            # Returning an LlmResponse here SKIPS the model call entirely.
            # from google.adk.models import LlmResponse
            # return LlmResponse(content=_refusal("secret in prompt"))
            raise RuntimeError("Secret detected in prompt; blocked before model call.")
        return None

    async def on_tool_error_callback(
        self, *, tool: "BaseTool", error: Exception, tool_context: "ToolContext"
    ) -> Optional[dict]:
        # Graceful fallback instead of crashing the run; telemetry plugin records it.
        return {"status": "error", "tool": getattr(tool, "name", "?"), "error": str(error)}


def _contains_secret(text: str) -> bool:
    import re
    return any(re.search(p, text or "") for p in SECRET_PATTERNS)


def _request_text(llm_request: Any) -> str:
    # Extract concatenated prompt text from the request in whatever shape ADK provides.
    return str(getattr(llm_request, "contents", llm_request) or "")
