from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Goal:
    """User-supplied objective for planning."""

    title: str
    context: str = ""


@dataclass(frozen=True, slots=True)
class PlanStep:
    """A single deterministic execution step."""

    index: int
    summary: str
    rationale: str


@dataclass(frozen=True, slots=True)
class ExecutionPlan:
    """A bounded, deterministic, in-memory plan."""

    goal: Goal
    steps: tuple[PlanStep, ...]
