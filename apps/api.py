from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel, Field

from core.detection import detect_event
from core.ledger import ledger_entry
from core.policy import decide

app = FastAPI(
    title="VAJRA-SHIELD",
    version="0.1.0",
    description="Self-hosted defensive cyber detection and incident assurance API",
)


class Event(BaseModel):
    event_id: str
    kind: str
    source: str
    asset: str | None = None
    attributes: dict[str, object] = Field(default_factory=dict)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "mode": "self-hosted"}


@app.post("/v1/analyze")
def analyze(event: Event) -> dict[str, object]:
    payload = event.model_dump()
    detections = detect_event(payload)
    return {
        "event": payload,
        "detections": [d.__dict__ for d in detections],
        "evidence": ledger_entry(payload),
    }


@app.post("/v1/policy/preview")
def policy_preview(action: str, severity: str = "HIGH", verified: bool = True):
    allowed = {
        "isolate_endpoint", "revoke_session", "disable_credential",
        "block_indicator", "increase_telemetry", "activate_decoy"
    }
    if action not in allowed:
        return {"allowed": False, "reason": "Unknown action"}
    return decide(action, severity, verified).__dict__
