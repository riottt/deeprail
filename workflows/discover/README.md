# Discover

**Workflow ID:** `deeprail-discover`

## Purpose
Reduce unknowns by inspecting domain, codebase, constraints, current behavior, and decision boundaries.

## Inputs
- work intent
- repository/domain context

## Outputs
- facts
- unknowns
- constraints
- decision candidates

## Required Evidence
- source inspection
- observed current behavior when relevant

## Exit Condition
The next responsibility can start without relying on avoidable guesses.

## Decision Rights
AI may research and propose; semantic conflict or objective change escalates.

## Failure / Return Path
- start
- discover

## Next
- `shape`
- `align`
- `specify`

## Runtime Language
Human-facing communication uses the resolved `communication_language`.
Human-readable generated artifacts use the resolved `artifact_output_language`.
Stable IDs, schema keys, code identifiers and machine enum values are not translated.
