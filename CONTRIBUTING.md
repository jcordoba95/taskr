# Contributing to taskr

Thanks for contributing! This document explains how the project is structured, how to set up your development environment, and the workflow for getting changes merged.

## Project overview

taskr is a command-line task manager built in Python 3.13. It is developed in four phases:

| Phase | Scope |
|-------|-------|
| 1 — CLI | Command-line interface with JSON persistence |
| 2 — Persistence | SQLite database + FastAPI scaffold |
| 3 — API | Full REST API with validation and tests |
| 4 — Web UI | Browser frontend in plain HTML/CSS/JS |

Each phase has its own GitHub Project board. Work on issues in order — later issues build on earlier ones.

## Prerequisites

- Python 3.13+
- git

## Local setup

```bash
git clone https://github.com/jcordoba95/taskr.git
cd taskr
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements-dev.txt
```

## Branching

All work happens on feature branches. Never commit directly to `main`.

Branch naming convention:

```
feature/<short-description>
```

Examples:
- `feature/add-task`
- `feature/sqlite-storage`
- `feature/get-tasks-endpoint`

```bash
git checkout main
git pull
git checkout -b feature/your-branch-name
```

## Making changes

1. Pick an open issue from the current phase project board
2. Move the issue card to **In Progress**
3. Create a branch (see above)
4. Work through the checklist in the issue
5. Commit your changes with a clear message
6. Push and open a pull request

## Commit messages

Keep them short and descriptive. Use the imperative form:

```
add task command to CLI          ✅
added task command               ❌
adding task command              ❌
```

## Opening a pull request

- Base branch: `main`
- Title: mirrors the issue title or describes the change clearly
- Body: briefly describe what you did and how to test it
- Link the issue by including `Closes #<issue-number>` in the body

Once the PR is open, move the issue card to **In Review**.

## CI checks

Every pull request runs two checks automatically:

| Check | Tool | What it verifies |
|-------|------|-----------------|
| Lint | ruff | Code style and common errors |
| Tests | pytest | All tests pass (Phase 3+) |

Both must pass before a PR can be merged. To run them locally:

```bash
ruff check .
pytest --tb=short
```

Fix any issues, commit, and push — the PR updates automatically.

## Code review

All pull requests require one approving review before merging. A reviewer may:

- **Approve** — the PR is ready to merge
- **Request changes** — address the comments, push new commits, and re-request review

Reply to review comments directly on GitHub so the conversation stays attached to the code.

## Code style

This project uses [ruff](https://docs.astral.sh/ruff/) for linting. Configuration is in `pyproject.toml`. The rules are intentionally minimal:

- Max line length: 88 characters
- Rule sets: E (pycodestyle errors), F (pyflakes), W (pycodestyle warnings)

Run `ruff check .` before pushing to catch issues early.

## Project structure

```
taskr/
├── main.py            # CLI entry point
├── storage.py         # JSON persistence (Phase 1)
├── database.py        # SQLite layer (Phase 2+)
├── api/
│   ├── __init__.py
│   ├── main.py        # FastAPI app
│   └── schemas.py     # Pydantic models
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
├── tests/
│   └── test_api.py
├── pyproject.toml
├── requirements.txt
└── .gitignore
```

Note: not all files exist yet — they are created as issues are completed.

## Issue labels

| Label | Meaning |
|-------|---------|
| `phase-1` / `phase-2` / `phase-3` / `phase-4` | Which phase this issue belongs to |
| `feature` | New functionality |
| `setup` | Project scaffolding or configuration |
| `docs` | Documentation only |
| `tests` | Tests only |
