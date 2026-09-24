# DeepRail Runtime

DeepRail Runtime is not an LLM itself. As a vendor-neutral control plane, it manages Project Profile / Workflow / Evidence Gate / Decision Rights / State / Audit, and hands an execution contract to the agent runtime through adapters.

## Execution unit

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

`deeprail task` converts the current workflow contract into an execution packet.

## Runtime Localization

The workflow's semantic definition stays single; the Language Resolver selects the presentation projection inside the same `workflow.yaml`. Human-readable artifact templates are selected by `artifact_output_language`.

```bash
deeprail template --project /path/to/project --kind specification --output spec.md
```
