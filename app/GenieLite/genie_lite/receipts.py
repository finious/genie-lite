"""Receipts make the human-to-Echo-to-CREATE chain inspectable."""

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from uuid import uuid4


@dataclass(frozen=True)
class WorkReceipt:
    human_request: str
    echo_interpretation: str
    route: str
    specialist: str
    specialist_return: str
    authority_state: str
    correction_applied: str | None = None
    action_state: str = "PROPOSED_ONLY"
    verification_state: str = "NOT_VERIFIED"
    unproven_claims: list[str] = field(default_factory=list)
    receipt_id: str = field(default_factory=lambda: str(uuid4()))
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def to_dict(self) -> dict:
        return asdict(self)
