# Task Runner

Project tasks are defined in a [`mise.toml`](https://mise.jdx.dev/) file. A `Makefile` is included as a simple wrapper that proxies commands to `mise run` for convenience.

Run any task with:

```bash
make <task>
# or directly:
mise run <task>
```

## Available Tasks

| Task | Description |
|------|-------------|
| `build` | Build source and wheel distributions |
| `check` | Run all checks (lint, types, docs) |
| `check-quality` | Run linters and format checks |
| `check-types` | Run static type checks |
| `clean-all` | Delete build artifacts |
| `clean-cache` | Remove cache files |
| `coverage` | Generate coverage reports (text, HTML, XML) |
| `docker-build` | Build Docker images |
| `docker-start` | Start Docker Compose services |
| `docker-stop` | Stop and remove Docker Compose services |
| `docs-serve` | Serve the documentation (localhost:8080) |
| `docs-deploy` | Publish docs to GitHub Pages |
| `docs-check` | Check if the documentation builds correctly |
| `format` | Auto-format code (Ruff) |
| `publish` | Upload distributions to PyPI |
| `release` | Automate version bump, changelog, and publish |
| `setup` | Bootstrap prod environment |
| `setup-cli` | Install the project's CLI globally via uv |
| `setup-dev` | Bootstrap dev environment and install pre-commit hooks |
| `test` | Run tests with pytest |
| `tox` | Run tests across multiple Python versions |

For the full list and task definitions, see [`mise.toml`](https://github.com/bassemkaroui/python-template-uv/blob/main/template/mise.toml.jinja).
