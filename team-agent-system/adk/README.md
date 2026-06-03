# adk/ — Google-stack bindings (skeletons)

These are **documented skeletons**, not a deployable package — they show the *shape* of how the portable layers bind to Google ADK. Verify exact signatures against the live [ADK docs](https://google.github.io/adk-docs/) before running (the API moves; see research §9.3).

## What's here
| File | Layer | Portable analog | Purpose |
|---|---|---|---|
| `plugins/guardrail_plugin.py` | L5 | hooks / permission rules | Global, deterministic guardrail registered on the Runner — blocks dangerous tools, scans for secrets. Precedes per-agent callbacks. |
| `plugins/telemetry_plugin.py` | L6 | OTel exporter | Emits OpenTelemetry GenAI spans/metrics for every model & tool call (vendor-neutral). |
| `callbacks/context_freshness_callback.py` | L1/L5 | freshness job + JIT retrieval | Before the agent runs, injects the freshest pointers and warns on stale knowledge. |
| `memory/memory_bank_config.md` | L1 | `knowledge/` + memory files | How State scopes + Vertex Memory Bank map to our durable knowledge. |

## Why Plugins for enforcement
ADK **Plugins** register once on the `Runner` and apply to **all** agents/models/tools, and their hooks **precede and can short-circuit** per-agent callbacks. That's the right seam for org/team-wide hard rules (RULES.md §R9). Per-agent `callbacks` remain for agent-specific behavior.

Key short-circuit semantics (confirmed in ADK docs):
- `before_model_callback` returning an `LlmResponse` → **skips the model call** (guardrail/cache).
- `before_tool_callback` returning a `dict` → **skips the tool** (block/deny).
- `before_agent_callback` returning `Content` → **skips the agent**.

## Wiring
```python
runner = Runner(
    agent=lead_agent,
    plugins=[GuardrailPlugin(), GenAITelemetryPlugin()],   # global L5 + L6
)
```
Model-agnostic: swap `model=` between Gemini, Claude (`LiteLlm`), or a Vertex model without touching these plugins.
