# DeepRail

**The open standard for designing AI-native work, software, and organizations.**

> **v0.16.8 — Public Release.** The Japanese Standard projection is canonical; English normative modules are published as Preview.

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

## Release Status

- Public release: **v0.16.8**
- Canonical Standard projection: Japanese (`ja`), DR-M01〜DR-M25
- English Standard projection: Preview; normative module translation is planned for a later release
- Runtime communication and artifact output: Japanese and English
- Software license: [MIT](LICENSE)
- Documentation license: [CC BY 4.0](LICENSE-DOCUMENTATION)
- Release history: [CHANGELOG.md](CHANGELOG.md)


## Authorship

Authorship and the public-content boundary are documented in [`AUTHORSHIP.md`](AUTHORSHIP.md).
