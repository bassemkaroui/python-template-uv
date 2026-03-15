# Task Runner

Project tasks are defined in a [`mise.toml`](https://mise.jdx.dev/) file. A `Makefile` is included as a simple wrapper that proxies commands to `mise run` for convenience.

Run any task with:

```bash
make <task>
# or directly:
mise run <task>
```

> [!TIP]
> Prefer `mise run` over `make` when running tasks directly:
>
> - **Auto-completion**: Run `make mise-setup-completions` to install shell completions for mise, giving you tab-completion for all tasks.
> - **Flags & arguments**: mise tasks can accept flags and positional arguments (e.g. `mise run docker-build --dev`, `mise run test -- -k test_foo`), which is not possible through `make`.

## Available Tasks

| Task                     | Description                                            |
| ------------------------ | ------------------------------------------------------ |
| `audit`                  | Check dependencies for known vulnerabilities           |
| `build`                  | Build source and wheel distributions                   |
| `check-all`              | Run all quality checks                                 |
| `check-quality`          | Run linters and format checks                          |
| `check-security`         | Run security analysis with Bandit                      |
| `check-types`            | Run static type checks                                 |
| `clean-all`              | Delete build artifacts and cache files                 |
| `clean-cache`            | Remove cache files                                     |
| `coverage`               | Generate coverage reports (text, HTML, XML)            |
| `dc`                     | Run docker compose with Doppler-mounted .env           |
| `docker-build`           | Build Docker images                                    |
| `docker-shell`           | Open a shell in a service container                    |
| `docker-start`           | Start Docker Compose services                          |
| `docker-stop`            | Stop and remove Docker Compose services                |
| `docs-check`             | Check if the documentation builds correctly            |
| `docs-deploy`            | Publish docs to GitHub Pages                           |
| `docs-serve`             | Serve the documentation (localhost:8080)               |
| `doppler-create-config`  | Create a new Doppler branch config                     |
| `doppler-create-token`   | Create a Doppler service token for this directory      |
| `doppler-delete-config`  | Delete a Doppler branch config                         |
| `doppler-set-token`      | Configure a preexisting Doppler service token          |
| `doppler-upload-secrets` | Upload a local .env file to Doppler                    |
| `format`                 | Auto-format code (Ruff)                                |
| `mise-setup-completions` | Install mise shell completions for the current shell   |
| `pre-commit`             | Run all pre-commit hooks on all files                  |
| `publish`                | Upload distributions to PyPI                           |
| `release`                | Automate version bump, changelog, and publish          |
| `setup-cli`              | Install the project's CLI globally via uv              |
| `setup-dev`              | Bootstrap dev environment and install pre-commit hooks |
| `setup-prod`             | Set up the project environment                         |
| `test`                   | Run tests with pytest                                  |
| `tox`                    | Run tests across multiple Python versions              |
| `upgrade`                | Upgrade all dependencies to latest compatible versions |

For the full list and task definitions, see [`mise.toml`](https://github.com/bassemkaroui/python-template-uv/blob/main/template/mise.toml.jinja).
