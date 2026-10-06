from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from typing import Any


def canonical_json(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def evidence_sha256(value: Any) -> str:
    return hashlib.sha256(canonical_json(value)).hexdigest()


def ledger_entry(event: dict[str, Any]) -> dict[str, Any]:
    created = datetime.now(timezone.utc).isoformat()
    digest = evidence_sha256(event)
    return {
        "created_at": created,
        "event_sha256": digest,
        "event": event,
    }
