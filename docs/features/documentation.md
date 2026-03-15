# Documentation

Generated projects include a fully configured [MkDocs](https://github.com/mkdocs/mkdocs) setup with the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme.

## What's Included

- **MkDocs Material** theme with dark/light mode, search, and navigation features
- **mkdocstrings** for auto-generated API documentation from docstrings
- **Code highlighting** with copy buttons and annotations
- **Admonitions**, tabbed content, and other Material extensions

## Local Development

```bash
# Serve docs with live reload (localhost:8080)
make docs-serve

# Check that docs build without errors
make docs-check
```

## Deployment

```bash
# Deploy to GitHub Pages
make docs-deploy
```

The CI/CD pipeline also deploys docs automatically on pushes to `main`.

## Structure

```
docs/
  index.md          # Landing page
  modules.md        # Auto-generated API reference
  css/
    overrides.css   # Custom styling
mkdocs.yml          # MkDocs configuration
```

## API Documentation

The template uses [mkdocstrings](https://mkdocstrings.github.io/) with the Python handler to generate API docs from your source code docstrings. Simply document your modules and classes with docstrings, and they appear in the docs automatically.
