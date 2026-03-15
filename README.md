<div align="center">

# python-template-uv

A modern, batteries‑included [Copier](https://github.com/copier-org/copier) template for bootstrapping Python packages and applications managed with [uv](https://github.com/Astral-Projects/uv)

[![Copier Template](https://img.shields.io/badge/copier-9.6.0-blue.svg)](https://copier.readthedocs.io/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Python 3.10–3.13](https://img.shields.io/badge/python-3.10%20|%203.11%20|%203.12%20|%203.13-blue.svg)]()

[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-blue?logo=materialformkdocs&logoColor=white)](https://bassemkaroui.github.io/python-template-uv)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white)](https://conventionalcommits.org)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![GitHub](https://img.shields.io/github/license/bassemkaroui/python-template-uv)](https://github.com/bassemkaroui/python-template-uv/blob/main/LICENSE)

</div>

## 🚀 Features

- **Copier-powered scaffolding**:
  Effortlessly generate or update projects with one command.

- **Task runner integration**:
  Project tasks are defined in a [mise.toml](https://mise.jdx.dev/) file.
  The [Makefile](https://github.com/bassemkaroui/python-template-uv/blob/main/template/Makefile.jinja) is a simple wrapper that proxies commands to `mise run` for convenience.
  Run tasks with `make <task>` (e.g. `make check-all`, `make docs-serve`) or directly with `mise run <task>`.

- **Quality & standards**
    - **Formatting** and **Linting**: [Ruff](https://github.com/astral-sh/ruff) ➜ `make format` & `make check-quality`
    - **Type checking**: [Mypy](https://github.com/python/mypy) ➜ `make check-types`
    - **Pre-commit hooks**: [pre-commit](https://pre-commit.com/)

- **Testing & coverage**
    - [**pytest**](https://github.com/pytest-dev/pytest) ➜ `make test`
    - [**Coverage**](https://github.com/nedbat/coveragepy) (text, HTML, XML) ➜ `make coverage`
    - Compatibility testing for multiple versions of Python with [**Tox**](https://github.com/tox-dev/tox) and its plugin [tox-uv](https://github.com/tox-dev/tox-uv) ➜ `make tox`

- **Documentation**
    - [**MkDocs**](https://github.com/mkdocs/mkdocs) with [mkdocs-material](https://github.com/squidfunk/mkdocs-material) theme
    - Live server: `make docs-serve` (serves on localhost:8080)
    - Deploy to GitHub Pages: `make docs-deploy`

- **Release & changelog**
    - [Conventional Commits](https://www.conventionalcommits.org/) + [Commitizen](https://github.com/commitizen-tools/commitizen) + [gitmoji](https://github.com/ljnsn/cz-conventional-gitmoji)
    - Automated `CHANGELOG.md` updates
    - Release new versions ➜ `make release`

- **Docker & Docker Compose**
    - Generate `Dockerfile` + `compose.yaml` for deployment and `compose.override.yaml` for development overrides (hot-reload, exposed ports, GPU support)
    - Docker targets: `make docker-build`, `make docker-start`, `make docker-stop`

- **Optional features**
    - Typer CLI scaffold
    - Strict typing (py.typed marker for type checking)
    - Run tests with parallel execution via pytest-xdist
    - Settings & configuration with [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) + [Doppler](https://www.doppler.com/) integration for secure secret management

- **CI/CD Workflows**

    This template includes GitHub Actions workflows for continuous integration, testing, and release automation:
    - **PR Commenting** (`pr-thank-you.yaml`): Posts a fun GIPHY comment on new pull requests using [`docker-action-pr-giphy-comment`](https://github.com/bassemkaroui/docker-action-pr-giphy-comment).
      Requires a `GIPHY_API_KEY` repository secret. To obtain one, sign up at [GIPHY Developers](https://developers.giphy.com/), create an app, and copy the API key. Then add it to your repository:
        - **CLI**: `gh secret set GIPHY_API_KEY` and paste the key when prompted
        - **Web UI**: Go to repo **Settings → Secrets and variables → Actions → New repository secret**, name it `GIPHY_API_KEY`, and paste the key

    - **CI/CD Pipeline** (`main.yaml.jinja`):
        - **Checks**: Linting (Ruff), type checking (Mypy), documentation build.
        - **Tests**: Runs `pytest` across supported Python versions using a matrix strategy.
        - **Releases**: Automatically publishes releases when a Git tag is pushed.
        - **Docs Deployment**: Deploys MkDocs documentation to GitHub Pages.
        - **Package Publishing** (optional): Publishes the package to PyPI if `publish_to_pypi` is enabled and `PYPI_TOKEN` is set.

    - **Dependency Updates** (optional): Choose between Dependabot or self-hosted Renovate via the `dependency_updater` template variable.
        - **Dependabot** (`dependabot.yml`): Opens weekly PRs to keep GitHub Actions dependencies up to date.
        - **Renovate** (`renovate.yaml` + `renovate.json5`): Self-hosted via GitHub Actions. Updates all dependencies (Python packages, pre-commit hooks, GitHub Actions, lock files) with smart grouping and automerge.
          Supports PAT or GitHub App authentication via the `renovate_auth_method` variable. See the [Renovate setup guide](renovate-setup.md) for detailed instructions.

    These workflows are generated into `.github/workflows/` in the scaffolded project. You can customize them further as needed.

## 🛠 Prerequisites

- **Python** ≥ 3.10
- **Copier** ≥ 9.14.0
- **copier-templates-extensions** ≥ 0.3.2
- **pre-commit** (if not installed check [pre-commit installation guide](https://pre-commit.com/index.html#install))
- **uv** (if not installed check [uv installation guide](https://docs.astral.sh/uv/getting-started/installation/))
- **mise** (if not installed check [mise installation guide](https://mise.jdx.dev/getting-started.html))

## 🎉 Quickstart

```bash
# 1. Scaffold a new project

# Option 1: Use uvx to run Copier with extensions
uvx --with copier-templates-extensions copier copy --trust gh:bassemkaroui/python-template-uv /path/to/my-project

# Option 2: Install Copier globally
uv tool install copier --with copier-templates-extensions

# Then run
copier copy --trust gh:bassemkaroui/python-template-uv /path/to/my-project

# Notes:
# • copier.yaml automatically runs `git init`, so `--trust` is required
# • Add `--prereleases` to include pre-release versions
# • Add `--vcs-ref=HEAD` to use the latest commit

# 2. Enter your project
cd /path/to/my-project

# 3. Set up development environment and hooks
make setup-dev

# 4. (Optional) Install your CLI globally via uv
make setup-cli

# 5. Run quality & tests
make check-all   # runs all checks: lint, types, docs build, API, etc.
```

**Stay up to date**

```bash
cd /path/to/my-project

uvx copier update --trust --exclude src/ --exclude tests/ .
```

> [!WARNING]
> To be able to [update your project](https://copier.readthedocs.io/en/stable/updating/), do not delete or manually modify the generated `.copier-answers.yml` file.

## 📋 Available Tasks

All tasks are defined in `mise.toml` and exposed through `make`. Common tasks include:

```
build                      Build source and wheel distributions.
check                      Check it all!
docs-check                 Check if the documentation builds correctly.
check-quality              Run linters and format checks.
check-types                Run static type checks.
clean-all                  Delete build artifacts.
clean-cache                Remove cache files.
coverage                   Generate coverage reports (text, HTML, XML).
docker-build               Build Docker images.
docker-start               Start Docker Compose services.
docker-stop                Stop and remove Docker Compose services.
docs-serve                 Serve the documentation (localhost:8080).
docs-deploy                Publish docs to GitHub Pages.
format                     Auto-format code (Ruff).
publish                    Upload distributions to PyPI.
release                    Automate version bump, changelog, and publish.
setup                      Bootstrap prod environment.
setup-cli                  Install the project's CLI globally via uv.
setup-dev                  Bootstrap dev environment & install pre-commit hooks.
test                       Run tests with pytest.
tox                        Run tests across multiple Python versions.
```

For the full list and details, see [mise.toml](https://github.com/bassemkaroui/python-template-uv/blob/main/template/mise.toml.jinja).

## 🔧 Template Variables

When running `copier`, you’ll be prompted for:

| Variable                    | Description                                                  | Default                           |
| --------------------------- | ------------------------------------------------------------ | --------------------------------- |
| `project_name`              | Your project’s **name** (lowercase, letters/digits/dashes)   | _—_                               |
| `project_description`       | A short summary of what your project does                    | _—_                               |
| `author_fullname`           | Your full name                                               | from `git`                        |
| `author_email`              | Your email address                                           | from `git`                        |
| `repository_provider`       | Where you host your repo (`github` or `other`)               | `github`                          |
| `homepage`                  | Project homepage URL                                         | `https://<user>.github.io/<proj>` |
| `python_version`            | Default Python interpreter for development                   | `3.12`                            |
| `min_python_version`        | Minimum supported Python version                             | `3.10`                            |
| `with_typer_cli`            | Include a Typer CLI scaffold?                                | `false`                           |
| `with_strict_typing`        | Enable strict typing (py.typed marker)?                      | `false`                           |
| `with_settings`             | Include Pydantic Settings for configuration?                 | `true`                            |
| `with_doppler`              | Add Doppler integration for secrets management?              | `false`                           |
| `tox`                       | Include Tox configuration?                                   | `true`                            |
| `coverage_threshold`        | Minimum test coverage %                                      | `100`                             |
| `with_conventional_commits` | Enforce Conventional Commits?                                | `true`                            |
| `cz_gitmoji`                | Include emojis in commit messages?                           | `true`                            |
| `dockerfile`                | Generate Dockerfile and Compose file?                        | `true`                            |
| `dependency_updater`        | Dependency update tool (`none`, `dependabot`, or `renovate`) | `renovate`                        |
| `renovate_auth_method`      | Renovate auth method (`pat` or `github_app`)                 | `pat`                             |
| `gpus`                      | Enable GPU support in Docker builds?                         | `false`                           |

> See the full list in [copier.yaml](https://github.com/bassemkaroui/python-template-uv/blob/main/copier.yaml).

## 📄 License

This project is released under the **MIT License**. See [LICENSE](https://github.com/bassemkaroui/python-template-uv/blob/main/LICENSE) for details.
