# Template Variables

When running `copier copy`, you'll be prompted for the following variables. They control what gets generated in your project.

## Project Information

| Variable | Description | Default |
|----------|-------------|---------|
| `project_name` | Project name (lowercase, letters/digits/dashes) | Current folder name |
| `project_description` | Short summary of what your project does | -- |
| `project_keywords` | Comma-separated keywords for the package | `python,<project_name>` |
| `author_fullname` | Your full name | From `git config` |
| `author_email` | Your email address | From `git config` |

## Repository

| Variable | Description | Default |
|----------|-------------|---------|
| `repository_provider` | Where you host your repo (`github` or `other`) | `github` |
| `author_github_handle` | Your GitHub username | Derived from `author_fullname` |
| `homepage` | Project homepage URL | `https://<user>.github.io/<project>` |
| `repository` | Repository URL | `https://github.com/<user>/<project>` |
| `documentation` | Documentation URL | Same as `homepage` |

## Python

| Variable | Description | Default |
|----------|-------------|---------|
| `python_version` | Default Python version for development | `3.12` |
| `min_python_version` | Minimum supported Python version | `3.10` |

## Features

| Variable | Description | Default |
|----------|-------------|---------|
| `with_typer_cli` | Include a [Typer](https://typer.tiangolo.com/) CLI scaffold | `false` |
| `cli_name` | CLI command name (if Typer enabled) | `<project_name>` |
| `with_strict_typing` | Enable strict typing with `py.typed` marker | `false` |
| `with_settings` | Include [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) | `true` |
| `with_doppler` | Add [Doppler](https://www.doppler.com/) secrets integration | `false` |
| `doppler_project` | Doppler project name (if Doppler enabled) | `<project_name>` |

## Testing

| Variable | Description | Default |
|----------|-------------|---------|
| `tox` | Include Tox configuration for multi-version testing | `true` |
| `pytest_xdist` | Enable parallel test execution with pytest-xdist | `false` |
| `coverage_threshold` | Minimum test coverage percentage (0-100) | `100` |

## Commits & Releases

| Variable | Description | Default |
|----------|-------------|---------|
| `with_conventional_commits` | Enforce [Conventional Commits](https://www.conventionalcommits.org/) | `true` |
| `cz_gitmoji` | Include emojis in commit messages | `true` |
| `publish_to_pypi` | Publish releases to PyPI | `false` |

## Docker

| Variable | Description | Default |
|----------|-------------|---------|
| `dockerfile` | Generate Dockerfile and Compose files | `true` |
| `privileged_container` | Run container as root | `false` |
| `gpus` | Enable GPU support in Docker | `false` |

## Dependencies

| Variable | Description | Default |
|----------|-------------|---------|
| `dependency_updater` | Dependency update tool (`none`, `dependabot`, `renovate`) | `renovate` |
| `renovate_auth_method` | Renovate auth method (`pat` or `github_app`) | `pat` |

## License

| Variable | Description | Default |
|----------|-------------|---------|
| `copyright_license` | Project license | `MIT License` |
| `copyright_holder` | Copyright holder name | `<author_fullname>` |

!!! tip
    See the full variable definitions with validators in [`copier.yaml`](https://github.com/bassemkaroui/python-template-uv/blob/main/copier.yaml).
