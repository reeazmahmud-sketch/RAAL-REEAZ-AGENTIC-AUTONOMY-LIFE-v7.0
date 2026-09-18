# RAAL v7.0 architecture (initial scaffold)

## Purpose
RAAL currently provides a **safe simulation scaffold** for planning and execution flows.
It does not perform autonomous real-world actions.

## Components
- `raal.config`: Loads runtime settings from environment variables with safe defaults.
- `raal.models`: Typed dataclasses for `Goal`, `PlanStep`, and `ExecutionPlan`.
- `raal.planner`: Deterministic planner that builds bounded in-memory plans.
- `raal.audit`: In-memory audit/event log abstraction.
- `raal.executor`: Simulated executor that records events only.
- `raal.__main__`: CLI demo entrypoint (`python -m raal`).

## Data flow
1. CLI parses goal input.
2. Config loads from environment (`RAAL_*` values).
3. Planner converts goal -> deterministic `ExecutionPlan`.
4. Executor simulates each step and appends audit events.
5. CLI prints plan and event timeline.

## Extension points
- Replace/extend planner templates while preserving deterministic behavior.
- Add alternate in-memory event sinks (e.g., ring buffers).
- Add policy validation on plan steps before simulation.

## Safety model
- No shell execution.
- No filesystem mutation by planner/executor.
- No network access.
- No credential collection or secret handling.
- No unsupervised external side effects.
