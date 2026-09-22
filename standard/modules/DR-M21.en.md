# DR-M21 — Enforcement and Standard Observation Guide

> Status: **preview v0.16.8**> Creator / Lead Author: **RIO AMADA**

**Layer:** Execution Harness / Governance
**Purpose:** Make it auditable how far declared Rules / Policies / Gates are actually enforced, and whether the enforcement mechanism itself is operating normally.

> **Rule exists ≠ Rule enforced ≠ Enforcement healthy ≠ Control effective.**

## M21.1 Enforcement Lifecycle

Manage the life of a Rule / Policy in the following Loop.

```text
Declare
↓
Register
↓
Enforce
↓
Verify the Enforcer
↓
Audit
↓
Improve / Retire
```

When a new Rule is born from an incident, Decision, or external borrowing, do not add only the Rule text; register it in the Enforcement Ledger in the same change.

## M21.2 Enforcement Ledger

```yaml
- rule_id:
  statement:
  canonical_source:
  source_or_provenance:
  layer: ExH | OpM | EngStd | Org
  status: draft | provisional | effective | retired
  enforcement:
    level: declared_only | nudge | block | measured | human_review
    checker:
    checker_due:
    fixtures: []
  coverage:
    paths: {}
  escape_hatch:
    mode: none | opt_in | temporary | emergency
    expiry:
  owner:
  evidence:
  exception_policy:
```

`declared_only` is not forbidden. However, display it not as "being observed" but as a state where **whether it is observed cannot be judged by the mechanism**.

Some Org Layer Policies may be impossible to enforce mechanically. In that case, mark `not_machine_enforceable` explicitly to distinguish it from mere non-implementation.

## M21.3 Enforcement Coverage

```text
Coverage
= block / measured / explicitly human-reviewed rules
  / rules that are enforceable in the declared layer
```

Do not make Coverage a KPI target. Its use is discovering long-term `declared_only` stagnation, expired deadlines, and Coverage Gaps.

## M21.4 Gate Coverage Map — Declare "How Far a Gate Reaches"

Each Gate holds at least six items.

| Viewpoint | Question |
|---|---|
| Match Set | What is matched as the full set of allowed / forbidden |
| Path Coverage | Which of AI Tool / Human CLI / CI / External Tool it passes through |
| Enforcement Mode | Which of block / nudge / after-the-fact review / static deny |
| Fail Direction | Which of fail-closed / fail-open / fail-silent, and why |
| Blocked-Actor Behavior | On block, after how many attempts does the Agent stop, and where does it Escalate |
| Limitation | What this Gate cannot prevent |

Furthermore, associate Operation with Environment.

```text
Operation: Read / Write / Execute / External Send / Production / Secret / Approval
Environment: Windows / macOS / Linux / Container / Cloud / Shared Legacy
```

Do not leave implicit states like "the AI path is Guarded but the Human CLI passes straight through" or "the Hook only warns but is believed to Block."

## M21.5 Guard the Guards

Do not treat changes to Control Mechanisms more lightly than normal code.

### Class 1 — Regression Fixture

A Gate / Checker change has at least the following pair.

```text
should_pass fixture
should_block fixture
```

### Class 2 — Doctor

Have a Harness Health Check that can be run daily — idempotent, routine, short. Move checks that have grown long to Audit.

### Class 3 — Generator + Check

For mechanisms that produce generated artifacts, pair the following where possible.

```text
generator
+
generator --check
```

### Class 4 — PROVENANCE

For externally sourced Skills / Rules / Scripts / Templates, record the borrowing source, acquisition time, whether modified, and update policy.

### Class 5 — Quarantine

Do not place externally sourced executable Assets on the production search Path immediately after acquisition. Separate inspection from promotion.

### Class 6 — Audit / Triangulation

Cross-check three points: declaration, substance, and usage traces.

```text
Declared
vs
Exists
vs
Actually used
```

## M21.6 Meta-Health

Detect failures of the observation / Learning / Audit Pipeline itself from a separate system.

Minimum candidates:

- Liveness
- parse error rate
- output/event count deviation
- dropped event
- redaction status
- schema drift
- latency
- Production telemetry / Eval telemetry separation
- cross-platform matrix where relevant

> **Distinguish "no problem has been observed" from "the observation device is dead."**

For systems that tolerate fail-silent, place a separate-system Liveness / Quality Check.

### M21.6-A Harness Assumption Register — Control Assumptions Have a Lifespan Too

A Harness / Guard / Workaround holds some Assumption about the Model Capability, Runtime, and Tool constraints at the time it was made. When that premise changes, a once-necessary Control can become excessive or, conversely, miss new Failures.

At minimum, keep the following for important Controls.

```text
Assumption
What this Control cannot do / on what fragile premise it exists

Capability / Environment Dependency
Which Model / Tool / Runtime / Work Class it depends on

Control Justified
What it Blocks / Guides / Verifies by that premise

Evidence
Grounds for judging the premise still holds

Review Trigger
Model update / Tool update / False Reject increase / Incident / Eval improvement

Expiry / Review Date
Deadline for re-evaluation

Status
active / simplify-candidate / remove-candidate / superseded
```

Guard the Guards asks not only "is the Guard unbroken." **It also asks whether the premise that required the Guard is still alive.**

> **Do not grow a Harness by addition alone. When capability rises, removing old training wheels is also Reinvestment.**

## M21.7 Environment Matrix for Controls

Test Gates / Checkers / Observers under the following in the required Operating Contexts.

```text
CRLF / LF
UTF-8 / BOM / legacy encoding
non-ASCII path
space-containing path
long path
proxy / network path where relevant
```

Do not make "it worked on my Mac" alone the completion condition of a Control.

## M21.8 Audit Evidence Contract

Decompose "keep logs" into five dimensions.

```text
Structure  : decide the schema first
Protection : redaction / append-only / writer ownership
Failure    : record evidence-capture failure itself
Quality    : path / evidence grade / null semantics
Retention  : retention / deletion / access policy
```

If evidence capture fails, turn that failure itself into evidence.

## M21.9 Enforcement Backlog

Put unbuilt Enforcement into the Harness Backlog.

```text
declared_only aging
checker_due expired
fixture missing
path coverage gap
meta-health missing
stale provenance
human-only control with excessive load
```

However, do not make raising the Coverage ratio itself the goal; prioritize from current Failure / Risk / Human Bottleneck.

---
