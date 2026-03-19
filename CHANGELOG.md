## 1.0.0 (2026-03-19)

### ✨ Features

- add mkdocs for the template
- add support for self hosted Renovate using a GitHub App
- add support for self hosted Renovate using a GitHub App
- add support for self-hosted Renovate in the template
- add support for self-hosted Renovate in the template

### 🐛🚑️ Fixes

- fix an issue with Makefile when commands have more than one hyphen
- remove font size which made the deployed docs smaller than the locally served
- remove commitizen-branch since it generates an error when creating docs
- wrap GitHub Actions expressions in {% raw %} blocks in renovate.yaml.jinja
- add '.jinja' to renovate github action workflow
- make 'pre-commit' more robust in _tasks
- **config**: attempt to correct renovate config to handle template's precommit config

### ♻️ Refactorings

- **ci**: make dependabot optional

### build

- **deps**: update dependency astral-sh/ruff-pre-commit to v0.15.7
- **deps**: update dependency astral-sh/ruff-pre-commit to v0.15.7
- **deps**: update ghcr.io/renovatebot/renovate docker tag to v43.83.0
- **deps**: update ghcr.io/renovatebot/renovate docker tag to v43.83.0
- **deps**: update dependency astral-sh/uv-pre-commit to v0.10.11 (#62)
- **deps**: update ghcr.io/renovatebot/renovate docker tag to v43.76.4
- **deps**: update ghcr.io/renovatebot/renovate docker tag to v43.76.4
- **deps**: update astral-sh/setup-uv digest to 37802ad
- **deps**: update astral-sh/setup-uv digest to 37802ad
- **deps**: update github actions (#56)
- **deps**: update ghcr.io/renovatebot/renovate docker tag to v43.76.3
- **deps**: update ghcr.io/renovatebot/renovate docker tag to v43.76.3
- **deps**: update github actions (major)
- **deps**: update github actions
- **deps**: update ghcr.io/renovatebot/renovate docker tag to v43.76.2 (#58)
- **deps**: update ghcr.io/renovatebot/renovate docker tag to v43.76.1 (#55)
- **deps**: update softprops/action-gh-release digest to b25b93d (#52)
- **deps**: update dependency commitizen-tools/commitizen to v4.13.9
- **deps**: update dependency commitizen-tools/commitizen to v4.13.9
- **deps**: update dependency astral-sh/uv-pre-commit to v0.10.10
- **deps**: update dependency astral-sh/uv-pre-commit to v0.10.10
- **deps**: update dependency astral-sh/ruff-pre-commit to v0.15.6
- **deps**: update dependency astral-sh/ruff-pre-commit to v0.15.6
- **deps**: update actions/checkout action to v6
- **deps**: update actions/checkout action to v6
- **deps**: update pre-commit hook commitizen-tools/commitizen to v4.13.9
- **deps**: update pre-commit hook commitizen-tools/commitizen to v4.13.9
- **deps**: update astral-sh/setup-uv digest to e06108d
- **deps**: update astral-sh/setup-uv digest to e06108d
- **deps**: update softprops/action-gh-release digest to a06a81a
- **deps**: update softprops/action-gh-release digest to a06a81a
- **deps**: update dependency copier to v9.14.0
- **deps**: update dependency copier to v9.14.0
- **deps**: lock file maintenance
- **deps**: lock file maintenance
- **deps**: update actions/checkout digest to 93cb6ef
- **deps**: update actions/checkout digest to 93cb6ef
- **deps**: update actions/setup-python digest to a309ff8
- **deps**: update actions/setup-python digest to a309ff8
- **deps**: update jdx/mise-action action to v4
- **deps**: update jdx/mise-action action to v4
- **deps**: update actions/upload-artifact action to v7
- **deps**: update actions/upload-artifact action to v7

### 💚👷 CI & Build

- exclude python-version in docs workflow from being updated by Renovate
- update Renovate config to detect versions in workflow templates

### 📝💡 Documentation

- remove any mention of API from the docs
- correct some mistakes in the docs
- rewrite the template README and changed the contributor docs to include more info
- add some emojis and fix some rendering issues
- **mkdocs**: add mise equivalent commands along with make
- add docs badge to link to the docs website
- add mkdocs

### 🔧🔨📦️ Configuration, Scripts, Packages

- add prerequisites to mise tools
- fix some dependencies for docs and add mise tasks for docs

### 🧹 chore

- **pyproject.toml**: set major_version_zero to false in preparation for the first major stable release

## 0.3.0 (2026-03-14)

### ✨ Features

- replace duties.py with mise and add settings/config support
- use 'uv_build' as a build backend instead of hatchling
- modify `Dockerfile` and split `compose.yaml` into `compose.yaml` and `compose.override.yaml`
- add support for GitHub Actions

### 🐛🚑️ Fixes

- **ci**: harden GitHub Actions workflows for production readiness
- substitute '-' in tasks names to ':' so that mise understand them
- add mise trust in 'copier.yaml' _tasks
- add torch as a dep when choosing newer version of CUDA

### build

- **deps**: update pre-commit hook pre-commit/pre-commit-hooks to v6
- **deps**: update pre-commit hook pre-commit/pre-commit-hooks to v6
- **deps**: update actions/checkout action to v5
- **deps**: update actions/checkout action to v5
- **deps**: update dependency copier to v9.10.2
- **deps**: update dependency copier to v9.10.2
- **deps**: update actions/setup-python action to v6
- **deps**: update actions/setup-python action to v6
- **deps**: update pre-commit hook commitizen-tools/commitizen to v4.9.1
- **deps**: update pre-commit hook commitizen-tools/commitizen to v4.9.1
- **deps**: update softprops/action-gh-release digest to aec2ec5
- **deps**: update softprops/action-gh-release digest to aec2ec5
- **deps**: lock file maintenance
- **deps**: lock file maintenance
- **deps**: update astral-sh/setup-uv action to v7
- **deps**: update astral-sh/setup-uv action to v7
- **deps**: update dependency copier-templates-extensions to v0.3.2
- **deps**: update dependency copier-templates-extensions to v0.3.2
- **deps**: update astral-sh/setup-uv digest to e92bafb
- **deps**: update astral-sh/setup-uv digest to e92bafb
- **deps**: update dependency copier to v9.9.0
- **deps**: update dependency copier to v9.9.0
- **deps**: lock file maintenance
- **deps**: lock file maintenance
- **deps**: update pre-commit hook commitizen-tools/commitizen to v4.8.3
- **deps**: update pre-commit hook commitizen-tools/commitizen to v4.8.3
- **deps**: update softprops/action-gh-release digest to 72f2c25
- **deps**: update softprops/action-gh-release digest to 72f2c25
- **deps**: update astral-sh/setup-uv digest to bd01e18
- **deps**: update astral-sh/setup-uv digest to bd01e18
- **deps**: lock file maintenance
- **deps**: lock file maintenance
- **deps**: update pre-commit hook commitizen-tools/commitizen to v4.8.2
- **deps**: update pre-commit hook commitizen-tools/commitizen to v4.8.2
- **deps**: update astral-sh/setup-uv digest to f0ec1fc
- **deps**: update astral-sh/setup-uv digest to f0ec1fc
- **deps**: update pre-commit hook commitizen-tools/commitizen to v4.8.0
- **deps**: update pre-commit hook commitizen-tools/commitizen to v4.8.0
- **deps**: update peaceiris/actions-gh-pages digest to 4f9cc66
- **deps**: update peaceiris/actions-gh-pages digest to 4f9cc66
- **deps**: pin bassemkaroui/docker-action-pr-giphy-comment action to f4e007d
- **deps**: pin bassemkaroui/docker-action-pr-giphy-comment action to f4e007d
- **deps**: update pre-commit hook commitizen-tools/commitizen to v4.7.1
- **deps**: update pre-commit hook commitizen-tools/commitizen to v4.7.1

### 📌➕⬇️➖⬆️ Dependencies

- **template**: add support for newer version of CUDA
- **template**: add some dependencies to the template
- **template**: add support for `pytest-benchmark`
- add some backend dependencies for the template

### 🔧🔨📦️ Configuration, Scripts, Packages

- **pre-commit**: add 'uv-export' pre-commit to the template and bump all pre-commit versions
- **template**: add support for `.editorconfig` and format files accordingly
- **Renovate**: add support for dependencies in the `template` directory
- **copier.yaml**: add some initialization tasks after creating a new project
- **pyproject.toml**: add some linting rules to ruff and configure pyright as an LSP

### 🩹 fix-simple

- **Renovate**: add a custom regex manager for pre-commit hooks in Jinja template
- **Renovate**: add a custom regex manager for pre-commit hooks in Jinja template
- fix the CI badge in the `README.md.jinja`

## 0.2.0 (2025-05-13)

### ✨ Features

- add `README.md.jinja` for the template
- **copier.yaml**: set the project name by default to the project root directory

### 🐛🚑️ Fixes

- change how Python versions show in the template `README.md.jinja` and in copier.yaml
- fix some bugs

### ♻️ Refactorings

- include waiting for containers' startup in `docker_start`

### build

- **deps**: update pre-commit hook commitizen-tools/commitizen to v4.7.0
- **deps**: update pre-commit hook commitizen-tools/commitizen to v4.7.0
- **deps**: lock file maintenance
- **deps**: lock file maintenance
- **deps**: update astral-sh/setup-uv digest to 6b9c606
- **deps**: update astral-sh/setup-uv digest to 6b9c606
- **deps**: lock file maintenance
- **deps**: lock file maintenance
- **deps**: update astral-sh/setup-uv action to v6
- **deps**: update astral-sh/setup-uv action to v6
- **deps**: update pre-commit hook commitizen-tools/commitizen to v4.6.0
- **deps**: update pre-commit hook commitizen-tools/commitizen to v4.6.0
- **deps**: update dependency copier to v9.7.1
- **deps**: update dependency copier to v9.7.1
- **deps**: pin dependencies
- **deps**: pin dependencies

### chore

- **config**: migrate renovate config
- **config**: migrate config .renovaterc.json

### 📌➕⬇️➖⬆️ Dependencies

- add `mkdocs-minify-plugin` as dependency

### 📝💡 Documentation

- **template/docs/index.md.jinja**: remove a non-existing path
- **README.md.jinja**: change `info` to `note` for better rendering on GitHub

### 🔐🚧📈✏️💩👽️🍻💬🥚🌱🚩🥅🩺 Others

- **copier-templates-extensions**: fix dependency name in `README.md` and in `.renovaterc.json`
- correct file name from `pytorch_indixes.jinja` to `pytorch_indexes.jinja`

### 🔧🔨📦️ Configuration, Scripts, Packages

- **.gitignore**: add `**/*.posting.yaml` to `.gitignore` to ignore Posting requests
- **.renovaterc.json**: disable Renovate `pyenv` manager to avoid updating `.python-version`
- **Renovate**: add the first version of `.renovaterc.json`
- **pre-commit**: don't sort keys in `pretty-format-json` hook
- **pre-commit**: modify `.pre-commit-config.yaml` files for the project and the template to be compatible with Renovate

### 🩹 fix-simple

- **duties.py.jinja**: watch all services in dev profile
- **Dockerfile.jinja**: use the project slug in the CMD for FastAPI

## 0.1.0 (2025-04-26)

### 💚👷 CI & Build

- add a `release.yaml` workflow to automate new releases

### 📝💡 Documentation

- add README.md
- modify the template `README.md`

## 0.1.0rc2 (2025-04-25)

### ✨ Features

- **duties.py**: add a duty to setup the CLI globally
- add support forfoptional dependency pre-configuration in template

### 🐛🚑️ Fixes

- **copier.yaml**: remove default dependencies
- **duties.py**: made the `release` duty more robust to errors

### ✅🤡🧪 Tests

- group tests for `version` functionality in a class
- exclude src/<project>/__main__.py from test coverage since it's an entry point

### 🎨🏗️ Style & Architecture

- **duties.py**: change jinja2 templating in `duties.py`

### 📄 License

- add support for `No License`

### 📝💡 Documentation

- **mkdocs**: add some cool examples to `docs/index.md`

### 🔧🔨📦️ Configuration, Scripts, Packages

- **mkdocs**: change the font size and add minify plugin
- change `mypy` config to ignore missing imports
- **mkdocs.yaml**: enable `callouts` and `PyMdown Tab Extension`

### 🩹 fix-simple

- **duties.py**: add `action` parameter to `_pick_env` to distinguish between `build`, `start` and `stop` when dealing with Docker containers
- **duties.py**: wait for dev containers to fully start after building them in `_setup_container`

## 0.1.0rc1 (2025-04-22)

### 🐛🚑️ Fixes

- **duties.py**: rename `duties.py` -> `duties.py.jinja`

## 0.1.0rc0 (2025-04-22)

### ✨ Features

- **duty**: add support for `duty`
- **tox**: add support for `pytest-xdist` in Tox

### 🐛🚑️ Fixes

- **copier.yaml**: add `pytest-xdist` to `copier.yaml`

### ✅🤡🧪 Tests

- **typer-CLI**: add some tests for typer CLI

### 🩹 fix-simple

- **Dockerfile**: fix a minor issue with Docker images

## 0.1.0b3 (2025-04-18)

### ✨ Features

- add support for a Typer CLI and strict typing

### 🐛🚑️ Fixes

- fix some issues with Typer config and code
- add `.jinja` suffix to some files

### 🎨🏗️ Style & Architecture

- change the order of packages imports

### 🔧🔨📦️ Configuration, Scripts, Packages

- move `__version__` to `__init__.py`

### 🩹 fix-simple

- avoid asking for the CLI's name when the user doesn't want one

## 0.1.0b2 (2025-04-17)

### ✨ Features

- add support for Docker containers

### 🐛🚑️ Fixes

- **Dockerfile**: fix some issues with Dockerfile
- **tox**: prevent uv from removing project `.venv` by using `--active` flag in `tox.ini`
- **commitizen**: avoid running `prepare-commit-msg.py` in certain cases so that `copier update` works

### 🔥⚰️ Clean up

- **commitizen**: remove `prepare-commit-msg` and `post-commit` git hooks

### 🔧🔨📦️ Configuration, Scripts, Packages

- **coverage**: set a default coverage of 100 for the template

### 🩹 fix-simple

- **compose.yaml**: change the version in the Docker images tags automatically with commitizen
- fix `install` and `install-dev` targets in Makefile and minor change in Dockerfile

## 0.1.0b1 (2025-04-15)

### 🐛🚑️ Fixes

- **commitizen**: make the `post-commit` and `prepare-commit-msg` available only when using commitizen

### 📌➕⬇️➖⬆️ Dependencies

- add `copier-templates-extensions` and `ruff` to the dependencies

### 🔧🔨📦️ Configuration, Scripts, Packages

- **pre-commit**: Run certain hooks only in `pre-commit` if `pre-push` is in `default_install_hook_types`
- **pre-commit**: set the default stage to `pre-commit`

## 0.1.0b0 (2025-04-15)

### ✨ Features

- scaffold initial beta version of the Python template
- **copier**: initialize copier config and template

### 🐛🚑️ Fixes

- **commitizen-hooks**: fix how `prepare-commit-msg` and `post-commit` work
- **pre-commit**: force `mypy` to scan just the `src` directory and exclude `mkdocs.yml` from check-yaml

### ♻️ Refactorings

- **post-commit.py**: replace `exit` with `sys.exit`

### 🎨🏗️ Style & Architecture

- remove some newlines

### 🔐🚧📈✏️💩👽️🍻💬🥚🌱🚩🥅🩺 Others

- remove a typo from .pre-commit-config.yaml.jinja

### 🔧🔨📦️ Configuration, Scripts, Packages

- **pre-commit**: remove commitizen-branch hook
- **copier**: initialize copier config

## 0.0.1 (2025-04-12)
