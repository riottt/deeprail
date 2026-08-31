# DeepRail Runtime

DeepRail RuntimeはLLMそのものではありません。Vendor-neutralなControl Planeとして、Project Profile / Workflow / Evidence Gate / Decision Rights / State / Auditを管理し、Adapterを通してAgent Runtimeへ実行Contractを渡します。

## 実行単位

```text
Work State
  ↓
Task Packet
  ↓
Agent executes bounded responsibility
  ↓
Artifacts + Evidence
  ↓
Evidence Gate
  ↓
A / EA / S Policy
  ↓
Transition / Retry / Escalate
```

`deeprail task` が現在のWorkflow Contractを実行Packetに変換します。

## Runtime Localization

WorkflowのSemantic Definitionは1つのまま、同じ`workflow.yaml`内のpresentation projectionをLanguage Resolverが選びます。Human-readable Artifact Templateは`artifact_output_language`で選択します。

```bash
deeprail template --project /path/to/project --kind specification --output spec.md
```
