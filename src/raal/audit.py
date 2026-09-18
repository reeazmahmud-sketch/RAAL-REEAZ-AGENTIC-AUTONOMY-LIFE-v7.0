from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(frozen=True, slots=True)
class AuditEvent:
    """Immutable runtime event."""

    timestamp: str
    kind: str
    detail: str


class AuditLog:
    """In-memory event sink for simulated execution."""

    def __init__(self) -> None:
        self._events: list[AuditEvent] = []

    def record(self, kind: str, detail: str) -> AuditEvent:
        event = AuditEvent(
            timestamp=datetime.now(timezone.utc).isoformat(),
            kind=kind,
            detail=detail,
        )
        self._events.append(event)
        return event

    @property
    def events(self) -> tuple[AuditEvent, ...]:
        return tuple(self._events)
