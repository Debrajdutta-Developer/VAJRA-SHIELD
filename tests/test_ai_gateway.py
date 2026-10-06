import json

from core.ai_gateway import analyze


class FakeModel:
    def generate(self, system_prompt: str, user_prompt: str) -> str:
        return json.dumps({
            "summary": "Credential abuse pattern observed.",
            "observations": ["Five failed authentication events were recorded."],
            "inferences": ["The pattern is consistent with automated credential abuse."],
            "confidence": 0.91,
            "automation_likelihood": 0.84,
            "recommended_actions": ["increase_telemetry", "revoke_session"]
        })


def test_local_ai_output_is_structured_and_bounded():
    result = analyze(
        {"event_id": "e1", "kind": "auth", "source": "10.0.0.4", "asset": "srv-1", "attributes": {}},
        [{"rule_id": "AUTH-BURST", "severity": "MEDIUM"}],
        FakeModel(),
        "test-local-model",
    )
    assert result.model == "test-local-model"
    assert 0 <= result.confidence <= 1
    assert 0 <= result.automation_likelihood <= 1
    assert result.observations
