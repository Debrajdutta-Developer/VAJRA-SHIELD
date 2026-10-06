from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


def build_incident_report(incident: dict[str, Any]) -> str:
    """Create a human-readable incident report from structured evidence."""
    lines = [
        "# VAJRA-SHIELD Incident Report",
        "",
        f"Incident: {incident.get('incident_id', 'unknown')}",
        f"Generated: {datetime.now(timezone.utc).isoformat()}",
        f"Severity: {incident.get('severity', 'UNKNOWN')}",
        f"Status: {incident.get('status', 'UNKNOWN')}",
        f"Confidence: {incident.get('confidence', 'unknown')}",
        f"Automation likelihood: {incident.get('automation_likelihood', 'unknown')}",
        "",
        "## Observed Behaviour",
    ]

    for event in incident.get("events", []):
        lines.append(
            f"- {event.get('timestamp', '?')} | {event.get('kind', '?')} | "
            f"{event.get('asset', '?')} | {event.get('summary', '')}"
        )

    lines.extend(["", "## Evidence"])
    for item in incident.get("evidence", []):
        lines.append(
            f"- {item.get('evidence_id', '?')} | {item.get('kind', '?')} | "
            f"SHA-256: {item.get('sha256', '?')}"
        )

    attribution = incident.get("attribution") or {}
    lines.extend([
        "",
        "## Attribution",
        f"- Status: {attribution.get('status', 'UNKNOWN')}",
        f"- Confidence: {attribution.get('confidence', 'unknown')}",
        "- Physical location established: "
        f"{attribution.get('physical_location_established', False)}",
        "",
        "## Defensive Actions",
    ])
    lines.extend(f"- {action}" for action in incident.get("actions", []))
    return "\n".join(lines) + "\n"
