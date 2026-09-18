# Safety model

RAAL v7.0 currently enforces a simulation-only operating model.

## Hard boundaries
- No shell command execution.
- No filesystem mutation by planner/executor runtime paths.
- No network access from planner/executor runtime paths.
- No credential harvesting or secret collection behavior.
- No unsupervised external side effects.

## Why these boundaries exist
The project is intentionally maturing from a minimal deterministic core. Safety boundaries prevent accidental expansion into high-risk behavior before policy controls, approvals, and security review are implemented.

## Contribution rule
Any proposed change that introduces external side effects must first include:
- explicit design documentation,
- threat/risk review,
- policy enforcement points,
- test coverage for failure modes and guardrails.
