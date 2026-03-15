# Quickstart

## Scaffold a New Project

/// tab | Using uvx (no install needed)
```bash
uvx --with copier-templates-extensions copier copy \
  --trust gh:bassemkaroui/python-template-uv /path/to/my-project
```
///

/// tab | Using installed Copier
```bash
# Install Copier globally (one-time)
uv tool install copier --with copier-templates-extensions

# Generate a project
copier copy --trust gh:bassemkaroui/python-template-uv /path/to/my-project
```
///

!!! note "Why `--trust`?"
    The template runs post-generation tasks (`git init`, `make setup-dev`, etc.) defined in `copier.yaml`, which requires the `--trust` flag.

!!! tip "Additional flags"
    - Add `--prereleases` to include pre-release template versions
    - Add `--vcs-ref=HEAD` to use the latest commit instead of the latest release

## Set Up Your Project

```bash
# Enter your project
cd /path/to/my-project

# Development environment and hooks are set up automatically by copier.
# If you need to re-run setup:
make setup-dev

# (Optional) Install your CLI globally via uv
make setup-cli
```

## Verify Everything Works

```bash
# Run all checks: lint, types, docs build
make check-all
```

## What Happens During Generation

When you run `copier copy`, the template automatically:

1. Runs `git init` to initialize a Git repository
2. Runs `make setup-dev` to install dependencies and set up pre-commit hooks
3. Runs `pre-commit run -a` to format all generated files
4. Prints any required repository secrets for CI/CD
