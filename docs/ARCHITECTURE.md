# VAJRA-SHIELD Architecture

## 1. Trust boundaries

```
                 UNTRUSTED INPUTS
                       |
                 [Telemetry Edge]
                       |
              +--------v---------+
              | Normalizer      |
              +--------+---------+
                       |
              +--------v---------+
              | Detection       |
              | Signature        |
              | Behaviour        |
              | Anomaly          |
              +--------+---------+
                       |
              +--------v---------+
              | Correlation      |
              | Timeline         |
              | TTP/IOC mapping  |
              +--------+---------+
                       |
              +--------v---------+
              | LOCAL AI GATEWAY |
              | No required WAN  |
              +--------+---------+
                       |
              +--------v---------+
              | Evidence /       |
              | Confidence       |
              +--------+---------+
                       |
              +--------v---------+
              | Policy Engine    |
              +---+----------+---+
                  |          |
            low-risk       high-impact
             actions       actions
                  |          |
            containment   human approval
                  |          |
                  +----+-----+
                       |
                 Alert + Report
```

## 2. Local AI boundary

The AI gateway accepts only normalized, access-controlled evidence. It must not have unrestricted network egress or arbitrary command execution.

The gateway exposes analysis functions such as:

- classify incident
- summarize behaviour
- correlate evidence
- assess automation likelihood
- map observed behaviour to defensive TTP categories
- produce analyst report
- identify missing evidence

The gateway does **not** expose a generic unrestricted shell tool.

## 3. Detection model

Detection is deliberately multi-layered:

- deterministic signatures
- statistical/anomaly detection
- sequence/behaviour detection
- IOC correlation
- historical incident similarity
- local AI reasoning

An AI conclusion without supporting evidence is never promoted to a confirmed incident by itself.

## 4. Automated defence

Allowed automated actions are scoped by policy and asset:

- isolate a compromised endpoint
- revoke a suspicious session
- disable a compromised credential
- block a verified malicious indicator
- increase telemetry collection
- activate a controlled decoy

High-impact actions require human approval.

## 5. Attribution

Attribution is an evidence-management problem, not an IP lookup.

The platform records source infrastructure, network observations, historical indicators and confidence. It explicitly distinguishes:

- observed source
- probable infrastructure
- suspected operator
- physical location: unestablished unless independently evidenced

## 6. Forensic integrity

Each evidence item receives a content hash. Incident records reference evidence hashes and immutable timestamps. The ledger is designed to make post-incident tampering detectable.

## 7. Availability

The core defensive pipeline must continue operating if the external internet or any hosted AI provider becomes unavailable.
