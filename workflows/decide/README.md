# Decide / Gate

**Workflow ID:** `deeprail-decide`

## Purpose
Turn evidence into a clear transition decision, exception, or escalation.

## Inputs
- evidence packet
- risk profile
- approval strength

## Outputs
- decision packet
- transition state

## Required Evidence
- decision is traceable to evidence and unresolved unknowns

## Exit Condition
PASS, RETRY, REJECT, DEFER, or ESCALATE is explicit.

## Decision Rights
A / EA / S determine actor and approval strength; they are not collapsed.

## Failure / Return Path
- verify
- specify

## Next
- `reinvest`
- `execute`

## Runtime Language
Human-facing communication uses the resolved `communication_language`.
Human-readable generated artifacts use the resolved `artifact_output_language`.
Stable IDs, schema keys, code identifiers and machine enum values are not translated.
