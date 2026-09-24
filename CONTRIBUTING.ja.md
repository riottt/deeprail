# DeepRailへのContribution

Book / Docs / Standard / Workflow / Runtime / Harnessの責務を分けたままにしてください。

## 開発環境

Python 3.10以上が必要です。

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## 変更を提案する前に

```bash
./scripts/generate
./scripts/check
python3 -m unittest discover -s tests
```

`./scripts/generate` は `.deeprail/generated/` を再生成します。生成物を直接編集しないでください。`./scripts/check` は公開純度・帰属の一致・Workflowスキーマ・配布の清浄性を検査します。

## Rule

1. 変更対象がBook / Docs / Standard / Workflow / Runtime / Harnessのどこかを明確にする
2. Stable ID（DR-M01〜DR-M25）を勝手に変えない
3. Standard semantic changeと文章改善を分ける
4. Workflow変更はEvidence / Exit / Failure pathを維持する
5. Workflowを言語で分岐させず、同じ定義内のpresentation projectionを使う

## Pull Request

- `main` へのPRを開きます。必須チェック（Python 3.10–3.13のCIマトリクス、docs build）が通る必要があります。
- どの層を変えたか、Evidence、Canonical内容への影響を書いてください。

Public ReleaseやCanonical Promotion、Stable Module変更、License / Trademark変更はriotttの明示的な人間判断です（[GOVERNANCE.md](GOVERNANCE.md)）。
