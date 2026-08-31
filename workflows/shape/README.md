# Shape / Visualize

**Workflow ID:** `deeprail-shape`

## Purpose
Turn an abstract request into something humans and AI can inspect together.

## Inputs
- discovery output

## Outputs
- scenario
- prototype/wireframe/example/interface sketch

## Required Evidence
- shape artifact linked to the stated intent

## Exit Condition
Stakeholders can judge the same concrete representation.

## Decision Rights
AI may generate options; commitment requires the configured decision owner.

## Failure / Return Path
- discover
- shape

## Next
- `align`
- `specify`

## Runtime Language
Human-facing communication uses the resolved `communication_language`.
Human-readable generated artifacts use the resolved `artifact_output_language`.
Stable IDs, schema keys, code identifiers and machine enum values are not translated.
