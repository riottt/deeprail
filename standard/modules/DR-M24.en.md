# DR-M24 — Demand Supply and Acceptance Operations Guide

> Status: **preview v0.16.8**> Creator / Lead Author: **RIO AMADA**

**Layer:** Organization ↔ Operating Model ↔ Engineering
**Main readers:** Product / Business / PM / PO / Engineering Lead / Architect
**Purpose:** Standardize the Interface from converting Business Intent into Demand that Engineering can execute and verify with AI, through to accepting the deliverable.

M24 is not merely "how to write requirements definition."
It handles the **Demand / Acceptance Contract** between Organization and Engineering.

## M24.1 Demand Flow

```text
Business Intent
↓
Outcome
↓
Demand
↓
Requirement / Constraint
↓
Acceptance Criteria
↓
Unknown / Assumption
↓
Alignment
↓
Engineering
↓
Acceptance
↓
Feedback
```

## M24.2 Demand Contract

Holds at least the following.

```yaml
demand:
  intent:
  expected_outcome:
  scope:
  non_goals:
  constraints:
  acceptance_criteria:
  unknowns:
  assumptions:
  risk:
  primary_consumer:
  failure_detectability:
  decision_owner:
  acceptance_owner:
  change_path:
```

Do not fill undecided items with guesses.

## M24.3 Acceptance Criteria

Acceptance Criteria describe not "how to implement" but the expected observable result.

Bad example:

```text
Build a dialog in React
```

Good example:

```text
When the user performs operation X,
state Z can be confirmed on screen under condition Y
```

## M24.4 Unwritten Expectation

Do not assume every expectation can be fully documented.

Explicitly choose how to handle implicit specifications.

```text
1. Explicit
   → Document it

2. Visualize
   → Fix it first via Mock / Prototype / Example

3. Human Catch
   → Place a Human Acceptance Test as a formal detection stage

4. Standardize
   → Promote to UI / Domain / Architecture Standard
```

Distinguish leaving implicit specifications unattended from intentionally entrusting them to Human Catch.

## M24.5 Pre-implementation Alignment

Before implementation, confirm:

- Undecided Decisions
- Domain terminology
- Acceptance Criteria
- Visual expectation
- Constraint
- Non-goal
- Risk
- Testability

Question Skills and Interview Tools are one implementation means; DeepRail Core does not depend on them.

## M24.6 Business / Product Gate

Upstream Human Gates include not only Engineering but also the Demand Owner.

Engineering does not guess and finalize Business Intent.

## M24.7 Requirement Change

Do not slip changes in through conversation alone.

```text
Change Request
↓
Impact
↓
Affected Requirement / Decision / Test
↓
Re-approval
↓
Work Item update
```

Connect the change history to Traceability.

## M24.8 Acceptance

Acceptance does not end at "tests are green."

As needed, combine:

```text
Machine Check
+
Observed Behavior
+
Human Acceptance
```

## M24.9 Requirement Quality Metrics

Examples:

- Acceptance Criteria completeness
- Unknowns resolved before Build
- Requirement change rate
- implicit-expectation rework rate
- acceptance rejection rate
- requirement surprise found during Review
- business-side waiting time
- engineering clarification loops

Do not tie these directly to "personnel evaluation of the requirements owner."
The purpose is System Improvement.

## M24.10 Learning Back

Implicit expectations, judgments, and constraints discovered at Acceptance are split into:

```text
Current Work Fix
+
Future Prevention
```

If recurring, return them to Requirement Template / Domain Rule / Design Standard / Test / Living Document.

---
