# Google-stack mapping (portable concept → ADK / Gemini / Antigravity)

The portable artifacts in this repo are the **source of truth**. The Google primitives below are *bindings* to them — not separate copies. This keeps a Gemini/Antigravity teammate and a Claude Code/Cursor teammate on identical behavior.

| Layer / concept | Portable artifact | Google equivalent | Notes & source |
|---|---|---|---|
| **L0 models** | model-profile config | ADK is model-agnostic: `LlmAgent(model=...)`, `LiteLlm(...)`, Vertex, documented Claude support | Don't hard-code Gemini; route cheap vs long-context models. [ADK models](https://google.github.io/adk-docs/agents/models/) |
| **L0 tools** | MCP tool defs | ADK `McpToolset` (stdio/SSE) consumes MCP natively | Same MCP servers across IDEs. [MCP tools](https://google.github.io/adk-docs/tools-custom/mcp-tools/) |
| **L0 cross-org agents** | — | **A2A** `A2AServer` / `RemoteA2aAgent`; complementary to MCP (A2A = agent↔agent, MCP = agent↔tool) | Use for the future org seam. [A2A](https://a2a-protocol.org/latest/) |
| **L1 pointer index** | `knowledge/index.md` + `pointers/` | An ADK **tool** that reads the index and returns matching pointers; fetch detail on demand | Stays vectorless; always fresh. |
| **L1 durable gotchas/prefs** | `knowledge/gotchas/` | **Vertex AI Memory Bank** (Gemini-extracted, self-curating, scoped similarity search) | Managed memory at P3; flat files fine earlier. [Memory Bank](https://cloud.google.com/agent-builder/agent-engine/memory-bank/overview) |
| **L1 big stable context** | (the shared overview) | **Gemini context caching** (implicit on 2.5; explicit `CachedContent`) | Cache the stable team overview once, reuse cheaply. [Caching](https://ai.google.dev/gemini-api/docs/caching) |
| **L2 instructions** | `AGENTS.md` | Antigravity reads `.agents/agents.md` + cross-tool `AGENTS.md`; Gemini CLI `context.fileName` → `AGENTS.md` | One file, every tool. [Antigravity codelab](https://codelabs.developers.google.com/autonomous-ai-developer-pipelines-antigravity) |
| **L3 skills** | `.agents/skills/*.md` | Antigravity `skills/` (on-demand); ADK sub-agents preloaded with skill content | Self-contained; routed by `description`. |
| **L3 workflows** | `.agents/workflows/*.md` | Antigravity `workflows/` slash commands; ADK Sequential/Loop agents | Chain plan→retrieve→implement→review→gate. |
| **L4 orchestration** | harness/sub-agent defs | ADK Workflow agents (Sequential/**Parallel**/Loop) + LLM delegation; Antigravity **Agent Manager** | Parallel only for reads. [Agents](https://google.github.io/adk-docs/agents/) |
| **L5 hooks (per-agent)** | hook scripts | **ADK callbacks**: before/after agent·model·tool; `before_model_callback`→`LlmResponse` skips the call | Guardrails/caching. [Callbacks](https://google.github.io/adk-docs/callbacks/types-of-callbacks/) |
| **L5 hooks (global)** | global hook config | **ADK Plugins** on the `Runner` — apply to all agents/tools/models, precede & can skip local callbacks | The real enforcement seam. [Plugins](https://google.github.io/adk-docs/plugins/) |
| **L1/L2 memory scopes** | file locations | **ADK State scopes**: none=session, `user:`, `app:`, `temp:`(discarded) | Finer-grained than files. [State](https://google.github.io/adk-docs/sessions/state/) |
| **L6 telemetry** | OTel GenAI export | ADK tracing → OTel GenAI semantic conventions; export to Datadog/Langfuse/Phoenix | Vendor-neutral. [OTel GenAI](https://opentelemetry.io/docs/specs/semconv/gen-ai/) |
| **L6 evals** | `evals/tasks/` | ADK eval runner; same task definitions | Run in CI. |
| **L7 governance** | `governance/` | identical — process, not product | Vendor-independent. |

## Minimal ADK wiring sketch

```python
from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.runners import Runner
from adk.plugins.guardrail_plugin import GuardrailPlugin       # L5 global
from adk.plugins.telemetry_plugin import GenAITelemetryPlugin  # L6

lead = LlmAgent(name="lead", model="gemini-2.5-pro", tools=[pointer_index_tool, code_search_tool])
reviewer = LlmAgent(name="reviewer", model="gemini-2.5-pro")   # spawned with CLEAN context (L4)

runner = Runner(
    agent=lead,
    plugins=[GuardrailPlugin(), GenAITelemetryPlugin()],       # global enforcement + telemetry
)
```

## Confirmed vs. verify-before-building
- **Confirmed (Google primary sources):** ADK callbacks/Plugins semantics, State scopes, MemoryService→Memory Bank, MCP via `McpToolset`, A2A, Gemini caching, Antigravity `.agents/`/`skills/`/`workflows/` + cross-tool `AGENTS.md`.
- **Verify against `antigravity.google/docs` before relying:** exact `GEMINI.md`↔`AGENTS.md` precedence ordering, any parallel-agent cap, live caching prices, and the Gemini CLI→Antigravity CLI transition. *(research §9.3)*
