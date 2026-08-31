# Decompose / Plan

**Workflow ID:** `deeprail-decompose`

## Purpose
Split work into bounded units while preserving dependencies, evidence, and return paths.

## Inputs
- specification
- risk profile
- repository topology

## Outputs
- work units
- dependencies
- parallelization plan
- gates

## Required Evidence
- every work unit has acceptance/evidence or a parent contract

## Exit Condition
Units are independently executable enough for the chosen autonomy profile.

## Decision Rights
AI may re-decompose within objective boundaries; objective changes escalate.

## Failure / Return Path
- specify
- discover

## Next
- `execute`
- `decide`

## Runtime Language
Human-facing communication uses the resolved `communication_language`.
Human-readable generated artifacts use the resolved `artifact_output_language`.
Stable IDs, schema keys, code identifiers and machine enum values are not translated.
