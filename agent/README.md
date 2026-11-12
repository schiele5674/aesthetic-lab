# Research Agent — future module

Planned responsibilities:
1. Load a versioned benchmark prompt.
2. Submit it to approved model endpoints.
3. Save raw outputs and run metadata.
4. Prepare anonymized evaluation packets.
5. Aggregate human scores and summarize failure cases.

Safety requirements:
- Never execute arbitrary generated code as part of the initial evaluator.
- Keep API keys in environment variables or a local `.env` file excluded by `.gitignore`.
- Require human review before publishing results.
- Log model versions, prompt versions, errors, and tool calls.
- Do not let an LLM judge its own output without a separately designed validation protocol.
