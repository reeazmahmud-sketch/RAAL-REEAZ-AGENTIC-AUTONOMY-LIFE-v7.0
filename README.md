# RAAL — Reeaz Agentic Autonomy Life v7.0

RAAL is an early-stage, production-minded foundation for an **agentic autonomy simulation system**.
This repository intentionally starts small with a safe Python scaffold that can be extended over time.

## Current status

This is an **initial scaffold**, not a full autonomy platform. It currently provides:
- typed domain models for goals and plans,
- a deterministic in-memory planner,
- a simulated executor with audit/event logging,
- a safe CLI demo,
- unit tests using the Python standard library.

## Safety boundaries (explicit)

RAAL v7.0 in this repository is simulation-only. The demo and core components:
- do **not** run shell commands,
- do **not** perform destructive system actions,
- do **not** modify files as part of planning/execution,
- do **not** access network services,
- do **not** harvest credentials,
- do **not** trigger unsupervised external side effects.

## Requirements

- Python **3.11+**

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
```

## Run the safe demo

```bash
python -m raal "Plan my weekly learning routine" --context "2 hours per day, focus on fundamentals"
```

Expected behavior: prints a deterministic in-memory plan and simulated audit events.

## Run tests

```bash
python -m unittest discover -s tests -p "test_*.py"
```

## Repository layout

```text
.
├── docs/
│   └── architecture.md
├── src/
│   └── raal/
│       ├── __init__.py
│       ├── __main__.py
│       ├── audit.py
│       ├── config.py
│       ├── executor.py
│       ├── models.py
│       └── planner.py
├── tests/
│   ├── test_executor.py
│   └── test_planner.py
├── .env.example
├── .gitignore
├── LICENSE
└── pyproject.toml
```

## Development notes

See [`docs/architecture.md`](docs/architecture.md) for component boundaries, data flow, extension points, and the safety model.

## License

MIT (see [`LICENSE`](LICENSE)).
