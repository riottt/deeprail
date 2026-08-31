# Execute

**Workflow ID:** `deeprail-execute`

## Purpose
Perform bounded work under the current contract without silently redefining the objective.

## Inputs
- work unit
- specification
- project profile

## Outputs
- artifact/change
- execution notes
- new unknowns

## Required Evidence
- execution artifact exists
- required checks invoked where applicable

## Exit Condition
Produced artifact is ready for independent verification.

## Decision Rights
Escalate new high-risk decisions, contract violations, or scope expansion.

## Failure / Return Path
- decompose
- specify
- discover

## Next
- `verify`

## Runtime Language
Human-facing communication uses the resolved `communication_language`.
Human-readable generated artifacts use the resolved `artifact_output_language`.
Stable IDs, schema keys, code identifiers and machine enum values are not translated.
