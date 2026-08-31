# Distribution Contract

A distributable ZIP MUST:

- exclude `.artifacts/`, `__pycache__/`, `*.pyc`, local authoring sources and raw imports
- include Book / Docs / Standard / Workflows / Runtime / Harness entrypoints
- pass `./scripts/check`
- pass runtime and Golden Path tests
- state released version and language scope accurately
- include a reproducible versioned archive and checksum
- keep published release tags immutable
