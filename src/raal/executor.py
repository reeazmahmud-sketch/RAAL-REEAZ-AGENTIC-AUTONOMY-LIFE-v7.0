from __future__ import annotations

from dataclasses import dataclass

from .audit import AuditLog
from .models import ExecutionPlan


@dataclass(frozen=True, slots=True)
class ExecutionResult:
    """Result of simulated execution."""

    completed_steps: int
    status: str


class SimulatedExecutor:
    """Executes plan steps in-memory and records audit events."""

    def __init__(self, audit_log: AuditLog | None = None) -> None:
        self._audit_log = audit_log or AuditLog()

    @property
    def audit_log(self) -> AuditLog:
        return self._audit_log

    def run(self, plan: ExecutionPlan) -> ExecutionResult:
        self._audit_log.record(
            "execution.started",
            f"Goal: {plan.goal.title}; steps={len(plan.steps)}",
        )
        for step in plan.steps:
            self._audit_log.record(
                "execution.step.simulated",
                f"step={step.index} summary={step.summary}",
            )
        self._audit_log.record("execution.completed", "Simulation finished successfully")
        return ExecutionResult(completed_steps=len(plan.steps), status="simulated_success")
