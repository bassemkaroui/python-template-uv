# Features Overview

python-template-uv generates a fully configured Python project with modern tooling. Here's what you get out of the box:

## Project Management

- **[Task Runner](task-runner.md)** -- All project tasks defined in `mise.toml` with a `Makefile` wrapper for convenience
- **[uv](https://docs.astral.sh/uv/)** -- Fast Python package and project manager for dependency resolution and virtual environments

## Code Quality

- **[Quality Tools](quality-tools.md)** -- Ruff for formatting and linting, Mypy for type checking, pre-commit hooks for automated checks
- **[Testing](testing.md)** -- pytest with coverage, optional parallel execution, and multi-version testing with Tox

## Infrastructure

- **[Documentation](documentation.md)** -- MkDocs with Material theme, auto-generated API docs, GitHub Pages deployment
- **[Docker](docker.md)** -- Production Dockerfile, compose files, development overrides, optional GPU support
- **[CI/CD](ci-cd.md)** -- GitHub Actions workflows for testing, releasing, docs, and dependency updates

## Customization

- **[Optional Features](optional.md)** -- Typer CLI, strict typing, Pydantic Settings, Doppler integration
- **[Template Variables](../configuration/variables.md)** -- Full control over what gets generated
