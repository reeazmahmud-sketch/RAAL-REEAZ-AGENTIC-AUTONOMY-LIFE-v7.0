from __future__ import annotations

import argparse

from .executor import SimulatedExecutor
from .models import Goal
from .planner import DeterministicPlanner
from .config import load_config


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="raal",
        description="RAAL v7.0 safe simulation demo",
    )
    parser.add_argument("goal", help="Goal title to simulate")
    parser.add_argument("--context", default="", help="Optional planning context")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    config = load_config()
    planner = DeterministicPlanner(max_steps=config.max_steps)
    goal = Goal(title=args.goal, context=args.context)
    plan = planner.plan(goal)

    executor = SimulatedExecutor()
    result = executor.run(plan)

    print(f"agent: {config.agent_name}")
    print(f"status: {result.status}")
    print("plan:")
    for step in plan.steps:
        print(f"  {step.index}. {step.summary} - {step.rationale}")

    print("events:")
    for event in executor.audit_log.events:
        print(f"  [{event.timestamp}] {event.kind}: {event.detail}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
