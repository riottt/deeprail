# Source of Truth

- Stable module registry: `.deeprail/manifests/content.json`
- Repository state: `.deeprail/manifests/repository.json`
- Standard projection languages: `.deeprail/manifests/languages.json`
- Runtime languages: `.deeprail/manifests/runtime-languages.json`
- Workflows: `workflows/*/workflow.yaml`
- Project profile schema: `schemas/project-profile.schema.json`

Book is a first-class reading projection, not the normative source of stable module identity.
Runtime adapters must remain thin projections.
