# Quality Tools

The template sets up a comprehensive code quality pipeline that runs automatically via pre-commit hooks and can be invoked manually.

## Ruff

[Ruff](https://github.com/astral-sh/ruff) handles both **formatting** and **linting** in a single, fast tool.

```bash
# Auto-format code
make format

# Check formatting and lint rules
make check-quality
```

Ruff is configured in `pyproject.toml` with sensible defaults. It replaces Black, isort, flake8, and many other tools.

## Mypy

[Mypy](https://github.com/python/mypy) performs static type checking.

```bash
make check-types
```

Configuration lives in `pyproject.toml`. If you enable the `with_strict_typing` option during generation, a `py.typed` marker file is included for PEP 561 compliance.

## Pre-commit Hooks

[pre-commit](https://pre-commit.com/) runs checks automatically before each commit. Hooks are configured in `.pre-commit-config.yaml` and include:

- Ruff formatting and linting
- Trailing whitespace removal
- YAML/TOML validation
- Merge conflict detection
- Conventional commit message validation (if enabled)

```bash
# Run all hooks on all files manually
pre-commit run -a

# Install hooks (done automatically by make setup-dev)
pre-commit install
```

## Running All Checks

```bash
# Run everything: lint, types, docs build
make check
```
