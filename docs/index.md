---
template: main.html
title: python-template-uv
hide:
  - navigation
  - toc
---

<style>
  .md-typeset h1 { display: none; }
</style>

<div class="hero" markdown>

<div class="hero-content" markdown>

# A modern Python project template :material-language-python:{ .hero-icon }

Scaffold production-ready Python packages and applications in seconds with [Copier](https://copier.readthedocs.io/) and [uv](https://docs.astral.sh/uv/).

[![Copier Template](https://img.shields.io/badge/copier-9.6.0-blue.svg)](https://copier.readthedocs.io/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Python 3.10-3.13](https://img.shields.io/badge/python-3.10%20|%203.11%20|%203.12%20|%203.13-blue.svg)]()
[![License](https://img.shields.io/github/license/bassemkaroui/python-template-uv)](https://github.com/bassemkaroui/python-template-uv/blob/main/LICENSE)

[Get Started](getting-started/quickstart.md){ .md-button .md-button--primary }
[View on GitHub](https://github.com/bassemkaroui/python-template-uv){ .md-button }

</div>

</div>

<div class="grid cards" markdown>

-   :material-rocket-launch:{ .lg .middle } **Quick Setup**

    ---

    Generate a fully configured project with a single command. Copier handles scaffolding, git init, and dependency installation automatically.

    [:octicons-arrow-right-24: Get started](getting-started/quickstart.md)

-   :material-tools:{ .lg .middle } **Task Runner**

    ---

    All project tasks defined in `mise.toml` with a `Makefile` wrapper. Run linting, testing, builds, and deploys with simple commands.

    [:octicons-arrow-right-24: Task runner](features/task-runner.md)

-   :material-check-decagram:{ .lg .middle } **Quality & Standards**

    ---

    Ruff for formatting and linting, Mypy for type checking, and pre-commit hooks to enforce standards on every commit.

    [:octicons-arrow-right-24: Quality tools](features/quality-tools.md)

-   :material-test-tube:{ .lg .middle } **Testing & Coverage**

    ---

    pytest with coverage reporting, optional parallel execution via pytest-xdist, and multi-version testing with Tox.

    [:octicons-arrow-right-24: Testing](features/testing.md)

-   :material-docker:{ .lg .middle } **Docker Ready**

    ---

    Production Dockerfile with compose files, development overrides, and optional GPU support out of the box.

    [:octicons-arrow-right-24: Docker](features/docker.md)

-   :material-github:{ .lg .middle } **CI/CD Workflows**

    ---

    GitHub Actions for linting, testing, releasing, docs deployment, and optional PyPI publishing. Dependency updates via Renovate or Dependabot.

    [:octicons-arrow-right-24: CI/CD](features/ci-cd.md)

-   :material-file-document:{ .lg .middle } **Documentation**

    ---

    MkDocs with Material theme pre-configured. Auto-generated docs with mkdocstrings. Deploy to GitHub Pages with one command.

    [:octicons-arrow-right-24: Documentation](features/documentation.md)

-   :material-puzzle:{ .lg .middle } **Optional Features**

    ---

    Typer CLI scaffold, strict typing, Pydantic Settings, Doppler secrets management -- enable only what you need.

    [:octicons-arrow-right-24: Optional features](features/optional.md)

</div>
