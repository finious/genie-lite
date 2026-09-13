"""Explicit, expiring human authority for Genie Lite."""

from dataclasses import asdict, dataclass
from enum import Enum


class AuthorityState(str, Enum):
    UNAUTHORIZED = "UNAUTHORIZED"
    AUTHORIZED_CURRENT = "AUTHORIZED_CURRENT"
    AUTHORIZED_RECORDED_EXPIRED = "AUTHORIZED_RECORDED_EXPIRED"


@dataclass
class AuthorityRecord:
    state: AuthorityState = AuthorityState.UNAUTHORIZED
    scope: str | None = None
    granted_by: str | None = None

    def authorize(self, scope: str, granted_by: str = "Jimmy") -> None:
        if not scope.strip():
            raise ValueError("authority scope must not be empty")
        self.state = AuthorityState.AUTHORIZED_CURRENT
        self.scope = scope.strip()
        self.granted_by = granted_by

    def expire_on_recovery(self) -> None:
        if self.state is AuthorityState.AUTHORIZED_CURRENT:
            self.state = AuthorityState.AUTHORIZED_RECORDED_EXPIRED

    def permits(self, scope: str) -> bool:
        return self.state is AuthorityState.AUTHORIZED_CURRENT and self.scope == scope

    def to_dict(self) -> dict:
        data = asdict(self)
        data["state"] = self.state.value
        return data
