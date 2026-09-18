# Contributing to RAAL

Thanks for helping improve RAAL.

## Development workflow
1. Create a focused branch.
2. Keep changes small and scoped.
3. Update docs when behavior changes.
4. Add or update tests for logic changes.
5. Run local checks before opening/reviewing a PR.

## Local checks
```bash
python -m unittest discover -s tests -p "test_*.py"
python -m compileall src tests
```

## Documentation-first rule
Before major feature work, document:
- the problem statement,
- component boundaries,
- safety implications,
- test strategy.

## Safety and scope
Contributions must preserve current RAAL safety boundaries unless a deliberately reviewed design change is approved. See [docs/safety.md](docs/safety.md).

## Coding expectations
- Python 3.11+
- Keep dependencies minimal and standard-library-first.
- Prefer explicit, typed, deterministic behavior in core components.
