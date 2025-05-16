<div align="center">

# python-template-uv

A modern, batteries‑included [Copier](https://github.com/copier-org/copier) template for bootstrapping Python packages and applications managed with [uv](https://github.com/Astral-Projects/uv)

[![Copier Template](https://img.shields.io/badge/copier-9.6.0-blue.svg)](https://copier.readthedocs.io/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Python 3.10–3.13](https://img.shields.io/badge/python-3.10%20|%203.11%20|%203.12%20|%203.13-blue.svg)]()

[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white)](https://conventionalcommits.org)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![GitHub](https://img.shields.io/github/license/bassemkaroui/python-template-uv)](https://github.com/bassemkaroui/python-template-uv/blob/main/LICENSE)

</div>

## 🚀 Features

- **Copier-powered scaffolding**:
  Effortlessly generate or update projects with one command.

- **Task runner integration**:
  Project tasks are organized using [duty](https://github.com/pawamoy/duty) and exposed via a [Makefile](https://github.com/bassemkaroui/python-template-uv/blob/main/template/Makefile.jinja) for easy command-line usage.
  Simply run tasks with `make <task>` (e.g. `make check`, `make docs`).

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
  - Live server: `make docs` (serves on localhost:8080)
  - Deploy to GitHub Pages: `make docs-deploy`

- **Release & changelog**

  - [Conventional Commits](https://www.conventionalcommits.org/) + [Commitizen](https://github.com/commitizen-tools/commitizen) + [gitmoji](https://github.com/ljnsn/cz-conventional-gitmoji)
  - Automated `CHANGELOG.md` updates
  - Release new versions ➜ `make release`

- **Docker & Docker Compose**

  - Generate `Dockerfile` + `compose.yml` for local development and deployment (GPU support)
  - Docker targets: `make docker-build`, `make docker-start`, `make docker-stop`

- **Optional tooling**

  - Typer CLI scaffold
  - Strict typing
  - Run tests with parallel execution via pytest-xdist
  - Preconfigured dependency categories (ML, data, web, etc.)

- **CI/CD Workflows**

  This template includes GitHub Actions workflows for continuous integration, testing, and release automation:

  - **PR Commenting** (`pr-thank-you.yaml`): Posts a fun GIPHY comment on new pull requests using [`docker-action-pr-giphy-comment`](https://github.com/bassemkaroui/docker-action-pr-giphy-comment)

  - **CI/CD Pipeline** (`main.yaml.jinja`):
    - **Checks**: Linting (Ruff), type checking (Mypy), documentation build.
    - **Tests**: Runs `pytest` across supported Python versions using a matrix strategy.
    - **Releases**: Automatically publishes releases when a Git tag is pushed.
    - **Docs Deployment**: Deploys MkDocs documentation to GitHub Pages.
    - **Package Publishing** (optional): Publishes the package to PyPI if `publish_to_pypi` is enabled and `PYPI_TOKEN` is set.

  These workflows are generated into `.github/workflows/` in the scaffolded project. You can customize them further as needed.

## 🛠 Prerequisites

- **Python** ≥ 3.10
- **Copier** ≥ 9.7.1
- **copier-templates-extensions** ≥ 0.3.1
- **uv** (if not installed check [uv installation guide](https://docs.astral.sh/uv/getting-started/installation/))

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
make check   # runs all checks: lint, types, docs build, API, etc.
```

**Stay up to date**

```bash
cd /path/to/my-project

uvx copier update --trust --exclude src/ --exclude tests/ .
```

> [!WARNING]
> To be able to [update your project](https://copier.readthedocs.io/en/stable/updating/), do not delete or manually modify the generated `.copier-answers.yml` file.

## 📋 Available Duties

All tasks are defined in `duties.py` and exposed through `make`. Common duties include:

```
build                      Build source and wheel distributions.
check                      Check it all!
check-api                  Check for API breaking changes.
check-docs                 Check if the documentation builds correctly.
check-quality              Run linters and format checks.
check-types                Run static type checks.
clean                      Delete build artifacts.
clean-cache                Remove cache files.
coverage                   Generate coverage reports (text, HTML, XML).
docker-build               Build Docker images.
docker-exec-*              Dockerized executions of checks, tests, docs, coverage.
docker-start               Start Docker Compose services.
docker-stop                Stop and remove Docker Compose services.
docs                       Serve the documentation (localhost:8080).
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

For the full list and details, see [duties.py](https://github.com/bassemkaroui/python-template-uv/blob/main/template/duties.py.jinja).

## 🔧 Template Variables

When running `copier`, you’ll be prompted for:

| Variable                    | Description                                                | Default                           |
| --------------------------- | ---------------------------------------------------------- | --------------------------------- |
| `project_name`              | Your project’s **name** (lowercase, letters/digits/dashes) | _—_                               |
| `project_description`       | A short summary of what your project does                  | _—_                               |
| `author_fullname`           | Your full name                                             | from `git`                        |
| `author_email`              | Your email address                                         | from `git`                        |
| `repository_provider`       | Where you host your repo (`github` or `other`)             | `github`                          |
| `homepage`                  | Project homepage URL                                       | `https://<user>.github.io/<proj>` |
| `python_version`            | Default Python interpreter for development                 | `3.12`                            |
| `min_python_version`        | Minimum supported Python version                           | `3.10`                            |
| `with_typer_cli`            | Include a Typer CLI scaffold?                              | `false`                           |
| `with_strict_typing`        | Enable strict typing enforcement?                          | `false`                           |
| `tox`                       | Include Tox configuration?                                 | `true`                            |
| `coverage_threshold`        | Minimum test coverage %                                    | `100`                             |
| `with_conventional_commits` | Enforce Conventional Commits?                              | `true`                            |
| `cz_gitmoji`                | Include emojis in commit messages?                         | `true`                            |
| `dockerfile`                | Generate Dockerfile and Compose file?                      | `true`                            |
| `gpus`                      | Enable GPU support in Docker builds?                       | `false`                           |

> See the full list in [copier.yaml](https://github.com/bassemkaroui/python-template-uv/blob/main/copier.yaml).

## 📄 License

This project is released under the **MIT License**. See [LICENSE](https://github.com/bassemkaroui/python-template-uv/blob/main/LICENSE) for details.
