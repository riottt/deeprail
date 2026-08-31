# Reinvest / Learn

**Workflow ID:** `deeprail-reinvest`

## Purpose
Return reusable learning to the project so the next execution changes.

## Inputs
- decision
- human interventions
- failures
- unknowns
- successful controls

## Outputs
- reinvestment candidates
- rule/eval/workflow updates
- deletions/simplifications

## Required Evidence
- candidate linked to observed friction or outcome

## Exit Condition
Learning is either reinvested, intentionally deferred, or rejected with rationale.

## Decision Rights
Changes to stable rules / schemas / governance follow their own change contract.

## Failure / Return Path
- reinvest

## Next
- `start`

## Runtime Language
Human-facing communication uses the resolved `communication_language`.
Human-readable generated artifacts use the resolved `artifact_output_language`.
Stable IDs, schema keys, code identifiers and machine enum values are not translated.
