from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


Severity = Literal["INFO", "LOW", "MEDIUM", "HIGH", "CRITICAL"]


@dataclass(frozen=True)
class Alert:
    incident_id: str
    severity: Severity
    title: str
    summary: str
    requires_human_review: bool


def create_alert(incident_id: str, severity: Severity, summary: str) -> Alert:
    return Alert(
        incident_id=incident_id,
        severity=severity,
        title=f"VAJRA-SHIELD {severity} incident",
        summary=summary,
        requires_human_review=severity in {"HIGH", "CRITICAL"},
    )
