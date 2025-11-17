# 🐍 Next Steps: Getting Started with StudyFrog

## Structure
.
├── src/studyfrog/
├── tests/
├── docs/
├── .github/workflows/
├── Makefile, Dockerfile, pyproject.toml, setup.cfg, setup.py
└── requirements.txt

## Common Commands
- Create venv: python -m venv .venv
- Activate: source .venv/bin/activate
- Install: pip install -r requirements.txt
- Test: pytest -q
- Format: black src tests
- Lint: ruff check src tests

## CI
GitHub Actions config at .github/workflows/ci.yml runs tests on 3.10–3.12.
