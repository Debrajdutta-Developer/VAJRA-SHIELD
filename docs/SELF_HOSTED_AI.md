# Self-hosted AI boundary

VAJRA-SHIELD treats model inference as an internal security service.

## Required properties

- model weights stored locally
- inference process isolated from public internet
- signed/checksummed model artifacts
- no telemetry sent to hosted AI providers
- explicit model version recorded in every AI-derived finding
- AI output stored as an untrusted analytical result until evidence verification
- no unrestricted shell or network tool exposed to the model

## Model selection

The platform intentionally does not hard-code a single vendor or model. A local adapter can connect to a self-hosted inference runtime appropriate for the deployment hardware.

This allows the operator to replace a model without changing detection, evidence, policy or reporting layers.

## AI-assisted attack assessment

The system may estimate whether activity is automated or AI-assisted, but this is an evidence-based confidence assessment, not proof of the attacker's identity or nationality.

Example:

- automation likelihood: 0.87
- evidence: high-rate adaptive requests, repeated tool-like sequences, correlated infrastructure
- conclusion: likely automated activity
- physical attacker location: not established

## Failure mode

If the AI service is offline, VAJRA-SHIELD must continue deterministic detection, containment policy, evidence preservation and alert generation.
