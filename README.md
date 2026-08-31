# DeepRail

**The open standard for designing AI-native work, software, and organizations.**

**Creator / Lead Author: RIO AMADA**

> **v0.16.8 Public Release Candidate Final / unreleased.** Public release and canonical promotion are intentionally not declared.

DeepRail now connects the long-form Book to problem diagnostics, stable Standard modules, actor-neutral workflows, a stateful evidence-gated runtime, thin agent adapters, audit history, and reinvestment.

## Start

- [Japanese Book — 45 chapters + ending](book/ja/chapters/README.md)
- [Japanese 10-minute Quickstart](docs/ja/quickstart.md)
- [Diagnostic](docs/ja/diagnostic.md)
- [English Quickstart](docs/en/quickstart.md)
- [Standard](standard/README.md)
- [Workflows](workflows/README.md)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
deeprail init --target /path/to/project --profile lightweight --communication en --artifacts en --adapter generic
```

## Validate

```bash
./scripts/generate
./scripts/check
python3 -m unittest discover -s tests -v
python3 -m build
./scripts/build-dist
```


## Authorship

DeepRail Creator / Lead Author: **RIO AMADA**. See [`AUTHORSHIP.md`](AUTHORSHIP.md) for the public-content boundary.
