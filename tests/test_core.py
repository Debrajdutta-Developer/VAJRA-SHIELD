from core.detection import detect_event
from core.ledger import evidence_sha256
from core.policy import decide


def test_failed_auth_detection():
    result = detect_event({
        "event_id": "e1",
        "kind": "authentication",
        "source": "sensor-1",
        "attributes": {"failed_auth_count": 7},
    })
    assert any(d.rule_id == "VS-AUTH-BURST" for d in result)


def test_evidence_hash_is_deterministic():
    value = {"b": 2, "a": 1}
    assert evidence_sha256(value) == evidence_sha256({"a": 1, "b": 2})


def test_unverified_action_never_automates():
    decision = decide("isolate_endpoint", "HIGH", False)
    assert decision.automatic is False
