# DeepRail Operational Workflows

DeepRailのStandardを、AIとHumanが実際の仕事で使えるActor-neutralなWorkflow Unitへ投影したものです。

```text
start
→ discover
→ shape / align
→ specify
→ decompose
→ execute
→ verify
→ decide
→ reinvest
```

固定N工程ではありません。Workの規模・Risk・Evidence・Autonomyに応じて圧縮・分離・反復します。

## Workflow Contract

各Workflowは最低限:

- Purpose
- Inputs
- Outputs
- Required Evidence
- Exit Condition
- Decision Rights
- Failure / Return Path
- Next

を持ちます。

## Runtime

```bash
./scripts/deeprail workflow start --project /path/to/project
```

言語別Workflowは作りません。Runtime Language Resolverが同じWorkflowを日本語 / 英語へ投影します。
