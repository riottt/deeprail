# Start / Intake

**Workflow ID:** `deeprail-start`

## Purpose
Establish the work intent, operating profile, and the next responsibility without assuming a fixed human-owned process.

## Inputs
- request
- project profile
- current repository state

## Outputs
- work intent
- initial unknowns
- selected next workflow

## Required Evidence
- request captured
- project profile resolved

## Exit Condition
Intent and bounded scope are clear enough to choose the next responsibility.

## Decision Rights
Escalate objective changes or unbounded scope to the accountable human owner.

## Failure / Return Path
- ask for missing intent
- discover

## Next
- `discover`
- `shape`
- `specify`

## Runtime Language
Human-facing communication uses the resolved `communication_language`.
Human-readable generated artifacts use the resolved `artifact_output_language`.
Stable IDs, schema keys, code identifiers and machine enum values are not translated.
