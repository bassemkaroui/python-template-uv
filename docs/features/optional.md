# Optional Features

These features can be toggled during project generation via template variables.

## Typer CLI (`with_typer_cli`)

Scaffolds a [Typer](https://typer.tiangolo.com/) CLI application with:

- Entry point configured in `pyproject.toml`
- CLI module with a sample command
- Customizable CLI name via the `cli_name` variable

/// tab | make

```bash
# Install CLI globally after generation
make setup-cli
```

///

/// tab | mise

```bash
# Install CLI globally after generation
mise run setup:cli
```

///

## Strict Typing (`with_strict_typing`)

Enables strict type checking and adds a `py.typed` marker file for [PEP 561](https://peps.python.org/pep-0561/) compliance. This signals to downstream consumers that your package ships inline type information.

## Pydantic Settings (`with_settings`)

Adds [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) for typed configuration management. Settings are loaded from environment variables with type validation and can be nested.

Enabled by default (`with_settings: true`).

## Doppler Integration (`with_doppler`)

Adds [Doppler](https://www.doppler.com/) integration for secure secret management. Doppler injects environment variables at runtime, which Pydantic Settings then validates and parses.

Requires `with_settings: true` and a Doppler project name (`doppler_project`).

## Parallel Testing (`pytest_xdist`)

Adds [pytest-xdist](https://github.com/pytest-dev/pytest-xdist) for parallel test execution, which can significantly speed up large test suites.

## Conventional Commits (`with_conventional_commits`)

Enforces the [Conventional Commits](https://www.conventionalcommits.org/) standard using [Commitizen](https://github.com/commitizen-tools/commitizen). Optionally includes [gitmoji](https://github.com/ljnsn/cz-conventional-gitmoji) for emoji-enhanced commit messages (`cz_gitmoji`).

Enables automated changelog generation and semantic version bumping via `make release`.
