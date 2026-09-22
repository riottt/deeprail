# Evidence Gates

Each workflow has an `evidence_policy`.

For Verify in particular, this RC requires at minimum:

- 2 or more usable evidence items
- `machine_check`
- one of `observed_behavior | independent_evaluation | human_decision`
- verified evidence
- independent evidence
- no unresolved `fail`

This ends the state where "a single piece of evidence is enough to proceed."
