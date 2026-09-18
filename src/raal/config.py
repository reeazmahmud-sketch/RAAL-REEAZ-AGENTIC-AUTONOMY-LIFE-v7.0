from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RuntimeConfig:
    """Safe runtime configuration loaded from environment variables."""

    agent_name: str
    max_steps: int


def _read_int(name: str, default: int, minimum: int, maximum: int) -> int:
    raw = os.getenv(name)
    if raw is None:
        return default
    try:
        value = int(raw)
    except ValueError:
        return default
    return max(minimum, min(value, maximum))


def load_config() -> RuntimeConfig:
    agent_name = (os.getenv("RAAL_AGENT_NAME") or "raal-sim-agent").strip() or "raal-sim-agent"
    max_steps = _read_int("RAAL_MAX_STEPS", default=6, minimum=3, maximum=20)
    return RuntimeConfig(agent_name=agent_name, max_steps=max_steps)
