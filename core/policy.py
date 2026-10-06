from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


Action = Literal[
    "isolate_endpoint",
    "revoke_session",
    "disable_credential",
    "block_indicator",
    "increase_telemetry",
    "activate_decoy",
]


@dataclass(frozen=True)
class PolicyDecision:
    action: Action
    automatic: bool
    reason: str


LOW_RISK_AUTOMATION: set[Action] = {
    "isolate_endpoint",
    "revoke_session",
    "disable_credential",
    "block_indicator",
    "increase_telemetry",
    "activate_decoy",
}


def decide(action: Action, severity: str, verified: bool) -> PolicyDecision:
    if not verified:
        return PolicyDecision(action, False, "Evidence is not verified")

    if severity == "CRITICAL" and action not in LOW_RISK_AUTOMATION:
        return PolicyDecision(action, False, "High-impact action requires human approval")

    return PolicyDecision(action, action in LOW_RISK_AUTOMATION, "Policy permits bounded defensive containment")
