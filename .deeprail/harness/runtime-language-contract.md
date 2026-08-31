# Runtime Language Contract

Runtime localization has two independent fields:

- `communication_language`: human-facing interaction
- `artifact_output_language`: human-readable generated artifacts

All workflows consume one resolved language context. Workflows are not forked by language.

Stable IDs, schema keys, code identifiers, protocol constants, command names, and machine enum values are not translated.
