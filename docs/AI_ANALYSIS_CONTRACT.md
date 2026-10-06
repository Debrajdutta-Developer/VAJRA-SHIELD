# Local AI Analysis Contract

VAJRA-SHIELD treats the model as an **untrusted analytical component**, not an authority.

## Flow

Telemetry -> deterministic detection -> evidence hash -> local model -> schema validation -> confidence/review policy -> analyst report.

## Guarantees

- No mandatory cloud model.
- No model-generated shell commands are executed.
- Hostile telemetry is data, never instructions.
- Physical attribution is never inferred from an IP address alone.
- AI-assisted/automated behaviour is represented as likelihood plus evidence.
- High-impact response remains policy-controlled and can require human approval.
- Deterministic detection and evidence collection continue if the local model is unavailable.

## Adapter boundary

The `LocalInference` protocol allows an adapter for Ollama, llama.cpp, vLLM, SGLang, or another locally hosted inference runtime without changing detection or policy logic.

A future adapter must enforce:
1. local-only endpoint by default;
2. explicit model identifier/version;
3. bounded input/output size;
4. request timeout;
5. structured JSON output;
6. no arbitrary tool execution;
7. model artifact integrity verification.
