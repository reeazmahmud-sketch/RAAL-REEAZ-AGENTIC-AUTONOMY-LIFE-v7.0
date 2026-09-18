from __future__ import annotations

from .models import ExecutionPlan, Goal, PlanStep


class DeterministicPlanner:
    """Transforms goals into deterministic simulation plans."""

    def __init__(self, max_steps: int = 6) -> None:
        if max_steps < 3:
            raise ValueError("max_steps must be at least 3")
        self._max_steps = max_steps

    def plan(self, goal: Goal) -> ExecutionPlan:
        clean_title = " ".join(goal.title.strip().split()) or "Untitled goal"
        clean_context = " ".join(goal.context.strip().split())

        templates = [
            (
                "Clarify objective",
                f"Summarize the goal as: {clean_title}",
            ),
            (
                "Identify constraints",
                "List boundaries, dependencies, and non-goals for safe simulation.",
            ),
            (
                "Create simulation actions",
                "Define purely in-memory actions with no external side effects.",
            ),
            (
                "Evaluate outcome",
                "Assess if simulated actions satisfy the goal and propose next steps.",
            ),
        ]

        if clean_context:
            templates.insert(
                1,
                (
                    "Capture context",
                    f"Incorporate user context: {clean_context}",
                ),
            )

        capped_templates = templates[: self._max_steps]
        steps = tuple(
            PlanStep(index=index + 1, summary=summary, rationale=rationale)
            for index, (summary, rationale) in enumerate(capped_templates)
        )

        return ExecutionPlan(goal=Goal(title=clean_title, context=clean_context), steps=steps)
