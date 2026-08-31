# Verify / Accept

**Workflow ID:** `deeprail-verify`

## Purpose
Evaluate the outcome using approved evidence rather than executor self-report.

## Inputs
- artifact/change
- acceptance criteria
- evidence contract

## Outputs
- evidence packet
- evaluation result
- unknowns

## Required Evidence
- machine checks when relevant
- observed behavior when relevant
- independent evaluation appropriate to risk

## Exit Condition
Evidence is sufficient to pass, retry, reject, or escalate.

## Decision Rights
EA level controls whether AI may only evaluate, recommend, or issue GO within policy.

## Failure / Return Path
- execute
- specify
- discover

## Next
- `decide`
- `execute`

## Runtime Language
Human-facing communication uses the resolved `communication_language`.
Human-readable generated artifacts use the resolved `artifact_output_language`.
Stable IDs, schema keys, code identifiers and machine enum values are not translated.
