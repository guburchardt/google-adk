# ADK Documentation & Examples

Hands-on examples for Google's [Agent Development Kit (ADK)](https://adk.dev) — a
code-first Python toolkit for building, running, and deploying AI agents. The repo
covers single agents, multi-tool agents, and multi-agent workflows (sequential,
loop, parallel, collaborative), using Gemini and (via LiteLLM) NVIDIA NIM models.

Each agent is a self-contained Python package: a folder with `__init__.py`
(exposing `agent`), `agent.py` (defining `root_agent`), a `requirements.txt`, and
a local `.env`.

## Prerequisites

- **Python 3.10+** (a virtual environment is recommended)
- A model provider API key, depending on the example:
  - **Google Gemini** → `GOOGLE_API_KEY` from [Google AI Studio](https://aistudio.google.com/apikey)
  - **NVIDIA NIM** (used by some workflows) → `NVIDIA_NIM_API_KEY` from [build.nvidia.com](https://build.nvidia.com)

## Setup

```bash
# 1. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

# 2. Install dependencies for the example you want to run
pip install -r build-your-agent/multi_tool_agent/requirements.txt
# (base examples need `google-adk`; LiteLLM-based workflows also need `litellm`)
```

## Configure credentials

Every agent package reads a local `.env`. Copy the template and fill in your key:

```bash
cp build-your-agent/multi_tool_agent/.env.example build-your-agent/multi_tool_agent/.env
```

```ini
# .env
GOOGLE_GENAI_USE_VERTEXAI=FALSE    # FALSE = AI Studio API key; TRUE = Vertex AI
GOOGLE_API_KEY=your-gemini-key
NVIDIA_NIM_API_KEY=your-nvidia-key # only for NVIDIA NIM workflows
```

> `.env`, `.adk/`, and `*.session.db` are gitignored — secrets and local session
> state never get committed.

## Run an example

ADK discovers any agent package in the current directory, so run the CLI **from the
folder that contains the agent package(s)**:

```bash
cd multi-agent-workflow/template-workflow

adk web          # browser chat UI — pick the agent from the dropdown
adk run loop     # run a specific agent in the terminal
adk api_server   # expose the agents as a local REST API
```

The same pattern applies under `build-your-agent/` (e.g. `cd build-your-agent && adk web`).

## Models & providers

| Provider | Configured as | Requires |
|----------|---------------|----------|
| Google Gemini | `model="gemini-2.5-flash"` | `GOOGLE_API_KEY` |
| NVIDIA NIM (via LiteLLM) | `model=LiteLlm("nvidia_nim/stepfun-ai/step-3.5-flash")` | `NVIDIA_NIM_API_KEY`, `litellm` |

Notes:
- The built-in `google_search` tool only works with Gemini models (see `paralel/`).
- `_lite_llm_patch.py` is a small shim that makes `LiteLlm` serializable (drops the
  non-serializable `llm_client` field) so it works with ADK's web/API runners.

## References

- ADK Python quickstart: https://adk.dev/get-started/python
- ADK docs: https://adk.dev
- ADK on GitHub: https://github.com/google/adk-python
