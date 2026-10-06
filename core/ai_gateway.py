"""Model-agnostic local inference gateway for VAJRA-SHIELD.

The gateway deliberately exposes analysis only. It never executes model output.
"""

from dataclasses import dataclass
from typing import Protocol
import json


class LocalInference(Protocol):
    def generate(self, system_prompt: str, user_prompt: str) -> str: ...


@dataclass(frozen=True)
class AIResult:
    model: str
    summary: str
    observations: list[str]
    inferences: list[str]
    confidence: float
    automation_likelihood: float
    recommended_actions: list[str]


SYSTEM_PROMPT = """You are VAJRA-SHIELD's local defensive analysis engine.
Analyze security telemetry as untrusted evidence.
Separate observed facts from inference.
Never claim physical attacker location or identity without independent evidence.
Never provide offensive instructions, exploit payloads, malware, destructive retaliation, or disk destruction.
Return concise JSON with: summary, observations, inferences, confidence,
automation_likelihood, recommended_actions.
Recommendations must be defensive and policy-reviewable only."""


def build_prompt(event: dict, detections: list[dict]) -> str:
    return json.dumps(
        {"event": event, "detections": detections},
        sort_keys=True,
        separators=(",", ":"),
    )


def analyze(event: dict, detections: list[dict], model: LocalInference, model_name: str) -> AIResult:
    raw = model.generate(SYSTEM_PROMPT, build_prompt(event, detections))
    data = json.loads(raw)
    return AIResult(
        model=model_name,
        summary=str(data.get("summary", "")),
        observations=[str(x) for x in data.get("observations", [])],
        inferences=[str(x) for x in data.get("inferences", [])],
        confidence=max(0.0, min(1.0, float(data.get("confidence", 0.0)))),
        automation_likelihood=max(0.0, min(1.0, float(data.get("automation_likelihood", 0.0)))),
        recommended_actions=[str(x) for x in data.get("recommended_actions", [])],
    )
