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
