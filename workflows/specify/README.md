# Specify / Contract

**Workflow ID:** `deeprail-specify`

## Purpose
Convert agreed meaning into an executable contract with acceptance and evidence requirements.

## Inputs
- aligned scope
- decisions
- constraints

## Outputs
- specification
- acceptance criteria
- evidence requirements
- non-goals

## Required Evidence
- traceability from intent to acceptance

## Exit Condition
Execution can proceed without inventing missing requirements.

## Decision Rights
AI may draft; unresolved normative/architecture decisions escalate.

## Failure / Return Path
- align
- discover

## Next
- `decompose`
- `execute`

## Runtime Language
Human-facing communication uses the resolved `communication_language`.
Human-readable generated artifacts use the resolved `artifact_output_language`.
Stable IDs, schema keys, code identifiers and machine enum values are not translated.
