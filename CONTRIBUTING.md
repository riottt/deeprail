# Contributing

Keep Book, Docs, Standard, Workflows, Runtime and Harness responsibilities distinct.

## Development setup

Python 3.10 or newer is required.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Before proposing changes

```bash
./scripts/generate
./scripts/check
python3 -m unittest discover -s tests
python3 -m build
```

`./scripts/generate` regenerates `.deeprail/generated/` — never edit generated files directly. `./scripts/check` enforces publication purity, attribution consistency, workflow schemas, and distribution cleanliness.

## Rules

1. Identify which layer the change belongs to: Book / Docs / Standard / Workflow / Runtime / Harness.
2. Do not change Stable IDs (DR-M01〜DR-M25).
3. Separate Standard semantic changes from wording improvements.
4. Workflow changes must preserve Evidence / Exit / Failure paths.
5. Do not fork workflows by language; use the presentation projections inside the same definition.

## Pull requests

- Open a PR against `main`. The required checks (CI test matrix on Python 3.10–3.13, docs build) must pass.
- Describe which layer changed, the evidence, and whether canonical content is touched.

Public releases, canonical promotions, stable module changes, and license or trademark changes remain explicit human decisions owned by riottt (see [GOVERNANCE.md](GOVERNANCE.md)).
