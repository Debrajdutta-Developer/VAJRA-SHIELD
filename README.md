# VAJRA-SHIELD

**Self-hosted Cyber Defence, Detection, Analysis & Forensic Assurance Platform**

VAJRA-SHIELD is an independent defensive cybersecurity research platform designed around four primary functions:

1. Real-time detection
2. Evidence-driven attack analysis
3. Controlled automatic containment
4. Immediate alerting and forensic reporting

## Design principles

- **Self-hosted by default:** core inference, telemetry, evidence and databases stay inside the protected environment.
- **No mandatory external AI provider:** OpenAI, Gemini, Anthropic and other hosted inference APIs are not required.
- **Evidence before attribution:** the system never treats an IP address as proof of an attacker's physical location.
- **Unknown attacks matter:** detection combines signatures, behavioural anomalies and correlation rather than relying only on known signatures.
- **AI is advisory and policy-constrained:** AI output cannot directly perform unrestricted infrastructure changes.
- **Non-destructive active defence:** containment, isolation, credential/session revocation, IOC blocking and deception are preferred over retaliation.
- **Forensic completeness:** every important decision is timestamped, correlated and recorded.

## High-level pipeline

```
Telemetry
  -> Normalization
  -> Detection
  -> Correlation
  -> Local AI analysis
  -> Evidence verification
  -> Policy engine
  -> Containment
  -> SOC alert
  -> Forensic report
```

## Repository layout

- `apps/` service entrypoints
- `core/` detection, correlation and policy logic
- `schemas/` canonical event/incident schemas
- `docs/` architecture, threat model and operational guidance
- `tests/` deterministic safety and detection tests
- `deploy/` self-hosted deployment material

## Status

This repository starts as a defensive research foundation. It intentionally does **not** contain destructive payloads, retaliatory malware, exploit delivery, or disk-destruction functionality.
