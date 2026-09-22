# DR-M10 — SCM / Repository Operations Guide

> Status: **preview v0.16.8**> Creator / Lead Author: **RIO AMADA**

## 14.1 Common Standard for SCM / Collaboration Adapters

Define from Git operations, not product names.

- Branch naming
- Worktree usage
- Commit granularity
- PR/MR granularity
- Reviewer
- Approval
- CI
- Merge method
- Conflict
- Release Branch
- Protected Branch
- Issue links
- Auto Merge conditions

---

## 14.2 SCM Adapter

Example:

```text
Work Item → Issue / Work Item
Review → Pull Request
Automation → CI/CD Automation
Protection → Branch Protection / Rulesets
```

---

## 14.3 Collaboration Adapter

Example:

```text
Work Item → Issue / Work Item
Review → Merge Request
Automation → CI/CD Automation
Protection → Protected Branch
```

---

## 14.4 Branch / Worktree

In AI parallel development, actively consider Worktrees.

```text
Developer A
└ Issue A
  └ Worktree A
    └ Agent A

Developer B
└ Issue B
  └ Worktree B
    └ Agent B
```

When multiple Agents edit shared files simultaneously, decide ownership ranges or integration order.

---

## 14.5 Standard PR/MR Flow

```text
Issue
↓
Branch / Worktree
↓
Implementation
↓
Self Review
↓
Test
↓
Living Document Check
↓
PR / MR
↓
CI
↓
Independent Review
↓
Approval
↓
Merge
```

---

## 14.6 Common Items in a PR/MR Body

```markdown
## Why
Why this change is made

## What
What was changed

## Impact
Scope of impact

## Verification
What was verified

## Documents
Canonical sources updated

## Risks
Residual risks / known constraints

## Work Item
Related Epic / Feature / Issue
```

Even when AI generates the PR/MR body, the Harness enforces this structure.

---

## 14.7 Split AI-Era PR/MR Review into Four Layers

Do not make it standard for humans to uniformly review the full volume of AI output.

### Layer 1: Deterministic Check

- Build
- Type Check
- Lint
- Unit Test
- Integration Test
- Security Scan
- Policy Check

Push what can be judged mechanically to CI/Hooks.

### Layer 2: AI Standards Review

Check targets:

- Repository conventions
- Coding Standards
- Architecture Rules
- Known Code Smells
- Unnecessary Scope expansion

### Layer 3: AI Spec Review

Check targets:

- Whether it satisfies the Issue/Spec
- Acceptance Criteria gaps
- Scope Creep
- Differences from the specification
- Whether Tests prove the specification

Judge Standards and Spec on separate axes; do not mix them.

### Layer 4: Human Decision Review

Humans mainly look at:

- Intent
- Business Decisions
- Significant Architecture judgments
- Risk
- Security
- Exceptions
- Properties that Tests cannot prove
- Issues AI escalated

After the Harness matures, expand the areas where human Review can shift from "word-by-word checking of every Diff" to "confirming important Decisions and Evidence."

However, maintain Human Review under a separate Policy for high-Risk changes, Production impact, Security, Data Migration, etc.

### 14.7.1 Return Code Review from Purpose to Means

DeepRail does not treat "not doing Code Review" as evidence of maturity. Whether a Human looked at the Code is not a KPI either.

The first question is what conventional Code Review was trying to detect.

| What to detect | Primary Control candidates |
|---|---|
| Requirement / Acceptance mismatch | Spec Eval / Acceptance Test / Traceability |
| Regression | Unit / Integration / E2E / Differential Test |
| Coding Rule violation | Lint / Static Analysis / Policy Check |
| Security Risk | SAST / DAST / Security Eval / Human Security Decision |
| Architecture deviation | Architecture Rule / Independent AI Review / Human Decision |
| Maintainability Risk | Metrics / Smell Detection / Sampling Review |
| Unknown / Low-detectability Risk | Human Deep Review / Experiment / Escalation |

After this decomposition, look at Code in Work Classes where Human Code Review is the best Control. In other Work Classes, make Machine / AI Evaluation primary and move Humans to Decision / Exception.

The Review Interface is viewed first in the following order.

```text
Decision / Outcome
↓
Evidence / Risk / Unknowns
↓
High-risk Diff
↓
Raw Diff / Code / Log
```

Raw Artifacts are not hidden. However, **they are not made the Interface read first**.

> **The point is not to eliminate Code Review. It is to redesign the quality that Code Review used to guarantee into a more verifiable Evidence System.**

---

## 14.8 Review Packet

Attach a Review Packet to the PR/MR so humans do not have to excavate design intent from a huge Diff.

```markdown
## Intent
What this change makes hold together

## Decisions
Major judgments fixed before implementation

## Spec Evidence
Which change/Test satisfies which Acceptance Criteria

## High-risk Diff
Places you especially want humans to see

## Automated Evidence
Build / Test / CI / Security results

## Deviations
What changed from the initial plan

## Open Questions
Unresolved matters
```

The Review Packet itself can also be AI-generated, but its content must be traceable from the Issue, Spec, Test, and Diff.

### Review Packet v2 — Do Not Hide "Unverified" and "Unplanned Decisions"

A Review Packet does not summarize only successful content. At minimum, it has the following keys.

```text
Intent
Decisions
Spec Evidence
High-risk Diff
Automated Evidence
what_untested
Agent-initiated Decisions
Deviations / Rulings
Open Questions
```

Keep the `what_untested` key even when empty. Distinguish a missing key from "nothing unverified."

If the Agent changed Scope or Implementation Strategy on its own judgment after Design / Contract finalization, record it in `Agent-initiated Decisions` and Escalate to Independent Evaluation / Human Decision according to Risk.

### A Send-Back Is Not a "Rejection Notice" but the Next Work Contract

```text
Rework Package
├ Failed condition + Evidence
├ Remaining work — what to add to reach a pass
├ causeClass — Failure Routing
└ Re-evaluation scope — previous failure + new diff
```

Do not return just "it failed" to the Executor. Decide the return destination by Failure Routing and limit the re-evaluation scope.

### Relationship Between Review Packet and Decision Packet

The Review Packet is the Engineering / PR-facing Profile of the Decision Packet.

```text
Decision Packet
├ Epic Decision Packet
├ Feature Acceptance Packet
├ Issue Gate Packet
├ PR / MR Review Packet
├ Release Decision Packet
├ Security Decision Packet
└ Transformation Decision Packet
```

The canonical Human Evaluation Interface principles are placed in DR-M17.

---

## 14.X Centralized VCS / Legacy SCM Adapter

An SCM / Collaboration Platform is not a required element of DeepRail Core.

In environments where a centralized VCS is the canonical source, choose in the following order.

```text
1. Can the Control Objective be satisfied with a Native profile?
2. Only if insufficient, place a Git Bridge
3. If the Bridge's dual-source-of-truth Risk is high, degrade to Reduced Parallelism
```

The centralized VCS Adapter is currently unverified;
do not describe it as "supported."

Validation targets:

- sync drift
- revision ↔ evidence traceability
- reviewability
- parallelism benefit
- bridge operational cost
- rollback
- auditability

Until viability is confirmed, mark it `experimental / unverified`.
