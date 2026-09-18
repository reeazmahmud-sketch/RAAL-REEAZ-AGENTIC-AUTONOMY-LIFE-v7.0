# Getting started

## Requirements
- Python 3.11+

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
```

## Run the demo
```bash
python -m raal "Plan my weekly learning routine" --context "2 hours per day"
```

The command prints:
- the selected runtime agent name,
- a deterministic in-memory plan,
- a simulated execution event timeline.

## Run tests
```bash
python -m unittest discover -s tests -p "test_*.py"
```

## Optional environment configuration
Copy `.env.example` values into your environment:
- `RAAL_AGENT_NAME` (default: `raal-sim-agent`)
- `RAAL_MAX_STEPS` (default: `6`, bounded in code)
- `RAAL_LOG_LEVEL` (default: `INFO`)
