"""
GenAITelemetryPlugin — L6 observability (Google ADK binding).

SKELETON. Emits OpenTelemetry GenAI semantic-convention spans/metrics for model and tool
calls so the feedback loop has data and we avoid vendor lock-in (export to Datadog,
Langfuse, Phoenix, etc.). Maps the portable "instrument everything with OTel GenAI" tenet.

Refs: https://opentelemetry.io/docs/specs/semconv/gen-ai/
Verify ADK Plugin hook names against https://google.github.io/adk-docs/plugins/.
"""

from __future__ import annotations
import time
from typing import Any, Optional

# from opentelemetry import trace, metrics
# tracer = trace.get_tracer("team-agent-system")
# meter = metrics.get_meter("team-agent-system")
# token_usage = meter.create_histogram("gen_ai.client.token.usage")
# op_duration = meter.create_histogram("gen_ai.client.operation.duration")


class GenAITelemetryPlugin:  # (BasePlugin)
    """Records the signals that drive evals & curation: tokens, cost, latency, tool errors."""

    def __init__(self) -> None:
        self._t0: dict[str, float] = {}

    async def before_model_callback(self, *, llm_request: "Any") -> Optional[Any]:
        self._t0["model"] = time.perf_counter()
        return None  # observe only

    async def after_model_callback(self, *, llm_response: "Any") -> Optional[Any]:
        dur = time.perf_counter() - self._t0.get("model", time.perf_counter())
        usage = getattr(llm_response, "usage_metadata", None)
        # Emit per the GenAI conventions. Span name SHOULD be "{operation} {model}".
        # with tracer.start_as_current_span("chat <model>") as span:
        #     span.set_attribute("gen_ai.operation.name", "chat")
        #     span.set_attribute("gen_ai.usage.input_tokens",  getattr(usage, "prompt_token_count", 0))
        #     span.set_attribute("gen_ai.usage.output_tokens", getattr(usage, "candidates_token_count", 0))
        # op_duration.record(dur, {"gen_ai.operation.name": "chat"})
        _log("model_call", duration_s=round(dur, 3),
             input_tokens=getattr(usage, "prompt_token_count", None),
             output_tokens=getattr(usage, "candidates_token_count", None))
        return None

    async def before_tool_callback(self, *, tool: "Any", tool_args: dict, tool_context: "Any") -> Optional[dict]:
        self._t0[f"tool:{getattr(tool,'name','?')}"] = time.perf_counter()
        return None

    async def after_tool_callback(self, *, tool: "Any", result: Any, tool_context: "Any") -> Optional[Any]:
        name = getattr(tool, "name", "?")
        dur = time.perf_counter() - self._t0.get(f"tool:{name}", time.perf_counter())
        _log("tool_call", tool=name, duration_s=round(dur, 3),
             error=isinstance(result, dict) and result.get("status") == "error")
        return None

    async def on_tool_error_callback(self, *, tool: "Any", error: Exception, tool_context: "Any") -> Optional[Any]:
        _log("tool_error", tool=getattr(tool, "name", "?"), error=str(error))
        return None


def _log(event: str, **fields: Any) -> None:
    # Replace with your real OTel exporter. Privacy: do NOT log prompt/response CONTENT
    # by default (OTel GenAI warns on this) — log metadata only.
    print({"event": event, **{k: v for k, v in fields.items() if v is not None}})
