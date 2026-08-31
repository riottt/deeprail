# Evidence Gate

各Workflowは `evidence_policy` を持ちます。

特にVerifyでは、このRCは最低限次を要求します。

- 2件以上のusable Evidence
- `machine_check`
- `observed_behavior | independent_evaluation | human_decision` のいずれか
- verified Evidence
- independent Evidence
- unresolved `fail` が存在しない

これにより「Evidenceが1件あれば進める」状態をやめます。
