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
