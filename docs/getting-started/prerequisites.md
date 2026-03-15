# Prerequisites

Before using this template, make sure you have the following tools installed:

## Required

| Tool | Minimum Version | Install Guide |
|------|----------------|---------------|
| [Python](https://www.python.org/) | 3.10+ | [python.org/downloads](https://www.python.org/downloads/) |
| [Copier](https://copier.readthedocs.io/) | 9.14.0+ | `uv tool install copier --with copier-templates-extensions` |
| [copier-templates-extensions](https://github.com/copier-org/copier-templates-extensions) | 0.3.2+ | Installed alongside Copier (see above) |
| [uv](https://docs.astral.sh/uv/) | latest | [uv installation guide](https://docs.astral.sh/uv/getting-started/installation/) |
| [mise](https://mise.jdx.dev/) | latest | [mise installation guide](https://mise.jdx.dev/getting-started.html) |
| [pre-commit](https://pre-commit.com/) | latest | [pre-commit installation guide](https://pre-commit.com/index.html#install) |

## Quick Install

/// tab | :fontawesome-brands-apple: macOS (Homebrew)
```bash
brew install python uv mise pre-commit
uv tool install copier --with copier-templates-extensions
```
///

/// tab | :fontawesome-brands-linux: Linux
```bash
# uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# mise
curl https://mise.jdx.dev/install.sh | sh

# pre-commit
uv tool install pre-commit

# copier
uv tool install copier --with copier-templates-extensions
```
///

/// tab | :fontawesome-brands-windows: Windows
```powershell
# uv
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# mise
# See https://mise.jdx.dev/getting-started.html#windows

# pre-commit
uv tool install pre-commit

# copier
uv tool install copier --with copier-templates-extensions
```
///
