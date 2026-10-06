from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass(frozen=True)
class Detection:
    rule_id: str
    severity: str
    confidence: float
    reason: str
    evidence: list[str] = field(default_factory=list)


def _now() -> datetime:
    return datetime.now(timezone.utc)


def detect_event(event: dict[str, Any]) -> list[Detection]:
    """Deterministic first-pass detection.

    This layer deliberately does not execute commands or contact external systems.
    Production deployments should add independently tested detectors here.
    """
    detections: list[Detection] = []
    kind = str(event.get("kind", "")).lower()
    attrs = event.get("attributes") or {}

    if kind in {"credential_abuse", "privilege_escalation", "lateral_movement"}:
        detections.append(
            Detection(
                rule_id=f"VS-{kind.upper()}",
                severity="HIGH",
                confidence=0.85,
                reason=f"Sensitive security behaviour observed: {kind}",
                evidence=[f"event:{event.get('event_id', 'unknown')}"],
            )
        )

    failed = attrs.get("failed_auth_count")
    if isinstance(failed, int) and failed >= 5:
        detections.append(
            Detection(
                rule_id="VS-AUTH-BURST",
                severity="MEDIUM",
                confidence=0.90,
                reason="Repeated authentication failures exceeded policy threshold",
                evidence=[f"failed_auth_count:{failed}"],
            )
        )

    return detections
