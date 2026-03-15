# CI/CD

The template generates GitHub Actions workflows for continuous integration, testing, and release automation.

## Main Pipeline (`main.yaml`)

The primary CI/CD workflow runs on pushes to `main` and pull requests:

- **Checks** -- Linting (Ruff), type checking (Mypy), documentation build
- **Tests** -- Runs pytest across supported Python versions using a matrix strategy
- **Releases** -- Automatically publishes releases when a Git tag is pushed
- **Docs Deployment** -- Deploys MkDocs documentation to GitHub Pages
- **Package Publishing** (optional) -- Publishes to PyPI if `publish_to_pypi` is enabled

## PR Thank You (`pr-thank-you.yaml`)

Posts a fun GIPHY comment on new pull requests using [`docker-action-pr-giphy-comment`](https://github.com/bassemkaroui/docker-action-pr-giphy-comment).

**Required secret:** `GIPHY_API_KEY`

To obtain one, sign up at [GIPHY Developers](https://developers.giphy.com/), create an app, and copy the API key.

## Dependency Updates

Choose your preferred dependency update tool via the `dependency_updater` variable:

### Renovate (`dependency_updater: renovate`)

Self-hosted via GitHub Actions. Updates all dependencies with smart grouping and automerge:

- Python packages and lock files
- Pre-commit hooks
- GitHub Actions
- Docker base images

Supports PAT or GitHub App authentication via the `renovate_auth_method` variable. See the [Renovate setup guide](https://github.com/bassemkaroui/python-template-uv/blob/main/renovate-setup.md) for detailed instructions.

### Dependabot (`dependency_updater: dependabot`)

GitHub-native solution. Opens weekly PRs to keep GitHub Actions dependencies up to date.

## Required Secrets

| Secret | Required For | How to Set |
|--------|-------------|------------|
| `GIPHY_API_KEY` | PR thank-you comments | `gh secret set GIPHY_API_KEY` |
| `PYPI_TOKEN` | PyPI publishing (if enabled) | `gh secret set PYPI_TOKEN` |
| `RENOVATE_TOKEN` | Renovate with PAT auth | `gh secret set RENOVATE_TOKEN` |
| `RENOVATE_APP_ID` | Renovate with GitHub App auth | `gh secret set RENOVATE_APP_ID` |
| `RENOVATE_APP_PRIVATE_KEY` | Renovate with GitHub App auth | `gh secret set RENOVATE_APP_PRIVATE_KEY` |
