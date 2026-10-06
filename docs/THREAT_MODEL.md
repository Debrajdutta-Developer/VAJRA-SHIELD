# VAJRA-SHIELD Threat Model

## Assets

- telemetry
- authentication events
- endpoint observations
- incident evidence
- threat intelligence
- model weights
- model configuration
- policy configuration
- forensic ledger
- alerting credentials

## Adversaries

1. External opportunistic attacker
2. Automated scanner
3. Credential attacker
4. Malware operator
5. Insider with limited privileges
6. Attacker attempting to poison telemetry or AI context
7. Attacker attempting to manipulate attribution

## Security objectives

### Confidentiality
Sensitive telemetry and evidence remain inside the protected security boundary.

### Integrity
Attackers must not be able to alter evidence, policy or model artifacts without detection.

### Availability
Detection and alerting continue during external service outages.

### Correctness
The system must distinguish observations from inference.

### Safe automation
An incorrect model decision must have bounded impact.

## AI-specific threats

- prompt injection through hostile logs
- poisoned threat intelligence
- malicious content embedded in files
- model hallucination
- model drift
- compromised model artifact
- excessive tool privileges
- data exfiltration through model output

## Required controls

- signed model artifacts
- checksum verification
- network egress deny-by-default for inference
- schema validation
- untrusted-data labels
- output validation
- least-privilege service accounts
- policy-controlled actions
- immutable/auditable evidence
- human approval for high-impact actions
- deterministic tests for containment logic

## Explicit non-goals

VAJRA-SHIELD does not implement:

- destructive retaliation
- disk/SSD destruction
- malware delivery to an attacker
- unauthorized exploitation of external systems
- unrestricted autonomous offensive operations
