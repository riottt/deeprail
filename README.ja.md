# DeepRail

**AIネイティブな仕事・開発・組織を設計するオープン標準。**

> **v0.16.8 Public Release Candidate Final / unreleased** — 公開用の文章・Runtime・Validationを統合した最終候補です。Stable Canonical Promotionは別途Governance Decisionとして扱います。

## 5つの入口

- 📖 **深く理解する** → [45章 + 終章](book/ja/chapters/README.md)
- 🚀 **10分で使う** → [Quickstart](docs/ja/quickstart.md)
- 🩺 **自分の詰まりを診断する** → [Diagnostic](docs/ja/diagnostic.md)
- ⚙️ **AIと仕事を進める** → [Workflows](workflows/README.md)
- 📐 **正式Ruleを参照する** → [Standard](standard/README.md)

## DeepRailが今回つながった範囲

```text
BOOK
Why / Friction / Case / Thought
  ↓
DIAGNOSTIC + DOCS
Problem → Navigation
  ↓
STANDARD
Stable Rules / Decision Rights
  ↓
RUNTIME
Work State → Task Packet → Artifact / Evidence → Gate → Decision → Transition
  ↓
ADAPTER
Claude / Generic Agent project integration
  ↓
REINVESTMENT
Repeated friction → Rule / Eval / Workflow / Harness
```

## 10分で動かす

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .

deeprail init --target /path/to/project --profile lightweight --communication ja --artifacts ja --adapter claude
deeprail doctor --project /path/to/project
deeprail work-start --project /path/to/project --title "Feature" --intent "実現したいOutcome"
deeprail task --project /path/to/project --work-id DRW-... --write
```

## Evidence-gated Runtime

Transition前にWorkflowごとの `evidence_policy` を評価します。Verifyでは、Machine Check + 追加Evidence + verified + independent evaluationを要求します。

```bash
deeprail gate --project /path/to/project --work-id DRW-...
deeprail audit-verify --project /path/to/project --work-id DRW-...
```

## Runtime Language

Standard TranslationとRuntime Languageは独立。

- communication: `ja | en`
- artifacts: `ja | en`
- Workflow Definitionは言語別Forkしない

## Repository Layers

```text
book/         Long-form knowledge
 docs/        Quickstart / Diagnostic / Use cases
standard/     DR-M01..DR-M25
workflows/    Actor-neutral execution contracts
profiles/     A / EA / S operating profiles
evals/        Evaluation contracts
runtime/      State / Task / Evidence Gate / Policy / Audit
adapters/     Runtime integration
diagnostics/  Problem assessment
maps/         Book → Standard → Workflow traceability
examples/     Runnable / policy / organization golden paths
.deeprail/    Repository harness / manifests / generated state
```

## Validation

```bash
./scripts/generate
./scripts/check
python3 -m unittest discover -s tests -v
python3 -m build
./scripts/build-dist
```

CI / Docs Build / Release Build workflows are included under `.github/workflows/`.

## Release Status

- Candidate corpus: v0.16.8
- Runtime/packaging version: `0.16.8rc3`
- Stable Module IDs: DR-M01〜DR-M25
- Japanese Standard projection: present
- English Standard projection: first-class but incomplete
- Public release: **not yet declared**
- Canonical promotion: **not yet declared**

This final release candidate is self-contained for publication and use. Stable canonical promotion remains a governance decision.


## Authorship

著作者情報と公開境界は [`AUTHORSHIP.md`](AUTHORSHIP.md) を参照してください。
