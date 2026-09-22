# DR-M20 — Environment / Execution Platform State Management Guide

> Status: **preview v0.16.8**> Creator / Lead Author: **RIO AMADA**

**Layer:** Execution Harness / Operating Context
**Purpose:** Manage in-use execution environments as "resources with state over time," and do not misclassify environment-derived Failures as development Failures.

## M20.1 Targets

Targets include the following.

- Local Development Environment
- Test / Integration Environment
- Ephemeral Environment
- Container / VM / Pod
- Worktree / Port / Lane resource
- Mirror / Cache
- Generated fixture / residual resource

Initial Setup itself is canonically DR-M04, and Production operations are DR-M18.
M20 handles the **in-use environment state** between them.

## M20.2 Environment Lifecycle

```text
Allocate
↓
Initialize
↓
Use
↓
Observe
↓
Contamination Check
↓
Cleanup / Recreate
↓
Release / Return
```

Define an Owner and Evidence at each stage.

## M20.3 Environment State

Use the following as OC-1.

```text
E-0: History Unknown
E-1: Managed / Cleanup Procedure Exists
E-2: Fresh / Disposable Guaranteed
```

At E-0, an Environment Preflight before starting Tests is mandatory.
At E-2, the environment-state Gate can be lightened.

## M20.4 Environment Preflight

Confirm at least the following.

- Version / generation
- residual data / resource
- required service health
- dependency reachability
- cache / mirror freshness
- required credentials presence
- expected configuration
- port / resource collision
- workspace / worktree identity

On Preflight failure, Escalate to the Environment Owner before entering implementation rework.

## M20.5 Environment Provenance

In shared environments, track the following where possible.

```text
environment_id
owner
allocated_at
work_item
generation
last_cleanup
known_residuals
freshness
last_verified_at
```

Do not leave environment state in "human memory."

## M20.6 Lane

Manage parallel-execution Lanes as tuples of:

```text
Human
× Work Item
× Environment
× Resource
```

Even if you only add Agents, Throughput does not rise if Environment / Review / Human Gate supply capacity is insufficient.

## M20.6-A Lane / Lease — Manage Environment as Execution Capacity

When Shared Environments or exclusive Resources exist, manage Environment not by "does it exist" but by "when, who, and for which Work Item it is occupied."

```text
lane_id
├ Human / Agent Session
├ Work Item
├ Environment
├ Worktree / Workspace
├ Port / Exclusive Resource
├ acquired_at
├ lease_expiry
└ release_status
```

Do not leave lease expiry unattended. Visualize expired occupation as Environment Debt, and prevent the next executing agent from "breaking it thinking it was free."

### Supply Lead Time

If environment provisioning requires external approval, closed-network application, account issuance, etc., manage it as an External Dependency before the DoR. Even if AI implementation is fast, if Environment Supply takes days, that becomes the Flow constraint.

## M20.7 Environment Failure

Do not keep routing Environment Failures into Implementation Retry.

```text
Failure
↓ cause routing
Environment State / Availability / Encoding / Network / Shared Resource
↓
Environment / Platform Owner
```

In Solo work, the same person may be the terminal Owner, but do not infinitely Retry as an in-stage Failure.

Do not return Failures judged to be environment-caused to the Code-fix Loop without limit.

```text
Failure
↓
Reproduce on fresh/known environment?
├ Yes → Product / Implementation investigation
└ No  → Environment State Failure
          ↓
       Environment Owner
```

---
