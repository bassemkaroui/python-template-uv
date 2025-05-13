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
