# Updating Your Project

Keep your project in sync with the latest template changes using Copier's update mechanism.

## Update Command

```bash
cd /path/to/my-project

uvx copier update --trust --exclude src/ --exclude tests/ .
```

The `--exclude` flags prevent Copier from overwriting your source code and tests during the update. Only template infrastructure files (configs, CI workflows, Makefile, etc.) are updated.

## How It Works

Copier uses the `.copier-answers.yml` file in your project root to track which template version and answers were used. During an update, it computes a three-way diff between:

1. The previous template version (your current answers)
2. The new template version
3. Your local modifications

This allows it to merge template updates with your customizations.

!!! warning "Do not modify `.copier-answers.yml`"
    Do not delete or manually edit the `.copier-answers.yml` file. Copier relies on it to perform updates correctly. If this file is missing or corrupted, Copier cannot determine what has changed and the update will fail.

## Reviewing Changes

After running the update:

```bash
# Review what changed
git diff

# If everything looks good, commit
git add -A && git commit -m "chore: update template to latest version"
```
