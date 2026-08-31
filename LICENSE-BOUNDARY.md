# License Boundary

DeepRail is distributed as a repository and Python package containing both executable software and documentation/configuration projections. The files below describe the intended license boundary for the v0.16.8 public release.

| Scope | License | Examples |
|---|---|---|
| Executable software and implementation code | MIT | `runtime/deeprail_runtime/**/*.py`, `scripts/**`, executable example code, and tests |
| Book, Standard, Docs, Workflows, Templates, Profiles, Evals, Diagnostics, Maps, and explanatory examples | CC BY 4.0 | `book/**`, `standard/**`, `docs/**`, `workflows/**`, `templates/**`, `profiles/**`, `evals/**`, `diagnostics/**`, `maps/**`, and explanatory example files |
| Packaged resource projections of the documentation/configuration scopes above | CC BY 4.0 | `runtime/deeprail_runtime/resources/**/*.md`, `*.yaml`, and `*.json` that project those scopes |
| Generated metadata and project configuration not covered by the scopes above | MIT | generated resource manifests, package metadata, and repository tooling configuration |

The repository's [LICENSE](LICENSE) applies to MIT-scoped software. [LICENSE-DOCUMENTATION](LICENSE-DOCUMENTATION) applies to documentation and Standard-scoped material. When a directory contains both executable code and documentation/configuration, apply the scope of each file rather than treating the whole directory as one license.

This boundary describes the project's intended terms for its own material. Third-party code, names, logos, and assets retain any separate notices and license obligations. The DeepRail name and logo are governed separately by [TRADEMARK.md](TRADEMARK.md).
