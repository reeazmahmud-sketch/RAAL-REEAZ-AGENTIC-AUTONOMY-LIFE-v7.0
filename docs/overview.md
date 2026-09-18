# Project overview

## What RAAL is
RAAL (Reeaz Agentic Autonomy Life) is a production-minded Python foundation for modeling goal-oriented planning and execution as a **safe simulation**.

## What RAAL currently includes
- typed domain model for goals and plans,
- deterministic in-memory planner,
- simulation-only executor,
- in-memory audit/event logging,
- minimal CLI demo (`python -m raal`),
- standard-library `unittest` coverage for planner and executor behavior.

## What RAAL is not (yet)
- not an autonomous runtime,
- not an orchestration engine for real-world actions,
- not integrated with cloud APIs, shell tools, external services, or credentials.

## Current priority
Stabilize a reliable, well-documented core so future extensions can be built with explicit guardrails and test coverage.
