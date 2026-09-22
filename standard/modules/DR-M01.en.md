# DR-M01 — AI-Driven Development Basic Policy

> Status: **preview v0.16.8**> Creator / Lead Author: **RIO AMADA**

## 5.1 Do Not Fix the Responsibility Boundary Between Human and AI

DeepRail is designed to include AI as an agent that actually advances work.
However, `AI = Execution / Human = Decision` is not fixed as a permanent boundary.

### Baseline Profile at This Stage

For most engagements, the following division of labor is safe at initial adoption.

```text
Human
├ Objective / Outcome
├ Business Priority
├ Risk Appetite
├ High-cost / Irreversible Decision
├ Exception Judgment
└ Accountability

AI
├ Research
├ Planning Draft
├ Work Breakdown Draft
├ Implementation
├ Test / Verification
├ Documentation
├ Review Assistance
└ Repetitive Coordination
```

This is a **starting Profile**, not a permanent list of Human-only areas.

### Dynamic Responsibility Boundary

As AI Capability, Risk, Evidence Reliability, Failure Detectability, Reversibility, Permission, and organizational Accountability change, the placement of responsibilities may change as well.

```text
Traditionally Human-centric
Planning
Work Decomposition
Review
Evaluation
Coordination
Priority Proposal
Resource Allocation Proposal
Strategy Option Design

        ↓ As Capability / Evidence / Control mature

Can be progressively delegated to AI
```

What DeepRail protects is not the Human domain, but the **safety conditions for moving responsibilities**.

### Delegation Decisions

```text
Delegability = f(
  Capability,
  Risk,
  Evidence Reliability,
  Failure Detectability,
  Reversibility,
  Permission Boundary,
  Accountability
)
```

We do not delegate because AI can do it.
**We delegate because failures can be observed, stopped, rolled back, and evaluated from Evidence.**

### The Current Operating Profile Is Not the Destination

Holding a thick Human Gate at initial adoption is not the same as Humans owning that Gate forever.

The current division of labor is a starting Profile matched to today's AI Capability, Evidence Reliability, Failure Detectability, Reversibility, Permission, Risk, and Accountability.

For example, at first AI executes and humans evaluate and approve. Once the evaluation system is sufficiently calibrated, AI takes first-pass evaluation and humans concentrate on Decision and Evidence. Furthermore, in bounded Work Classes where False Accepts and Escaped Defects are continuously observed and Rollback and Audit hold, normal GO decisions can be delegated to AI while humans move to Sampling / Exception.

Beyond that, once Policy and Risk Appetite are stable, AI can perform evaluation, GO, and Retry within the defined scope.

```text
Human-led
↓
AI-assisted
↓
Delegated Execution
↓
Delegated Evaluation
↓
Audited Autonomy
↓
Policy-Governed Autonomy
```

This is not a one-way maturity race. Proceed per Work Class based on Evidence, and revert when conditions break.

**What DeepRail fixes is not the current Human / AI division of labor, but the conditions under which responsibilities may move.**

### What It Means for AI to Enter "Human Territory"

AI does not merely replace human tasks one by one.
It continuously rewrites the very boundary once thought of as "beyond this point, humans only."

As a result, AI adoption propagates into:

```text
Task Automation
↓
Team Design
↓
Management
↓
Role / Headcount / Decision Rights
↓
Organization Structure
↓
Business Strategy / Competitive Advantage
```

The more AI enters Planning, Evaluation, Coordination, and Priority, the more the conversation expands beyond tool selection. Eventually, staffing, authority, organization structure, and business strategy become design targets.

## 5.2 Core Principles

1. Do not treat AI output unconditionally as a finished product.
2. Have AI investigate existing specifications, code, and constraints before implementation.
3. Do not finalize unclear requirements from AI guesses alone.
4. Do not separate code changes from documentation changes.
5. Do not load all information into Context at all times.
6. Define the canonical source and the order in which AI should consult references.
7. Promote repeated procedures into Skills or equivalent mechanisms.
8. For constraints you want to enforce, consider mechanical Gates, not only natural language.
9. Limit AI permissions to the scope required by the task.
10. Judge Harness maturity by evaluation results, not by feel.

11. Do not mix guesses into confirmed information; isolate them as Unknown / Assumption / Confirmation Required.
12. Do not fill unimplemented, unmeasured, or unverified items with values. Use `null` for nonexistent values, and mark unverified claims with their Evidence state.

### Trust Architecture — Three Layers That Make Evidence Trustworthy

```text
Philosophy
→ Do not treat self-reporting as Evidence

Design
→ Evidence Level / Independent Evaluation / Evaluation Authority / Human Gate

Execution
→ CI / Hook / Checker / Permission / Enforcement Ledger

Health
→ Guard the Guards / Meta-Health
```

Do not consider Trust established just because "a strong Rule was written" or "a Hook was placed."

---

## 5.3 After AI Adoption, the Bottleneck Moves from "Build" to Other Stages

Do not evaluate the effect of AI Agent adoption by "code generation speed" alone.

In conventional software development, the implementation / Build stage often occupied most of the time.
When AI Agents rapidly shorten this stage, the constraint on development as a whole moves to the stages before and after it.

```text
Before

Requirements
    ↓
Design
    ↓
████████████████
     Build
████████████████
    ↓
Test
    ↓
Release
    ↓
Maintain

Primary constraint = Build
```

```text
After AI Agents

Requirements ━━━━━━━
       ↓
Design       ━━━━━━━
       ↓
Build        ━
       ↓
Review       ━━━━━━━
       ↓
Test         ━━━━━━━
       ↓
Release      ━━━━━━━
       ↓
Maintain     ━━━━━━━
```

When looking at AI-driven development, do not isolate Coding alone. When Build gets faster, the next place where work stalls changes. The object of observation becomes **the Flow of the entire SDLC**.

The Harness covers more than Build.

```text
Requirements
├ Requirements collection
├ Requirements organization
├ Work Item conversion
└ Ambiguity / contradiction detection

Design
├ Impact Analysis
├ Architecture
├ Interface Design
└ Design Review

Build
├ Implementation
├ Refactoring
├ Local Build
└ Local Test

Review
├ AI Self Review
├ Independent AI Review
├ Human Review
└ Security Review

Test
├ Unit
├ Integration
├ E2E
└ Acceptance

Release
├ CI/CD
├ Release Gate
├ Migration
└ Rollback

Maintain
├ Monitoring
├ Incident
├ Bug Analysis
├ Operations
└ Living Documents
```

When AI accelerates a stage, observe where wait time, WIP, and human judgment concentrate next, and change the Harness improvement target accordingly.

---

## 5.4 Move Review in the AI Era from "Reading Every Finished Artifact" to "Reviewing Assumptions and Decisions First"

AI Agents can generate large volumes of code, design options, and documents in less time than humans.
After AI produces everything, a human reviews the artifacts from beginning to end. Unless that order changes, the Review stage itself becomes the next Bottleneck.

```text
Conventional
Humans build
↓
Humans review
↓
Merge
```

```text
Failure pattern after AI adoption
AI generates at scale
↓
Huge diffs / large volumes of documents
↓
Humans review after the fact
↓
Cognitive load grows
↓
Review Queue
↓
Cannot absorb AI's speed
```

Do not place review only at the final stage.

```text
Intent
↓
Agree on assumptions
↓
Fix terminology, constraints, and design decisions
↓
Specification
↓
Implementation
↓
Mechanical verification / AI Review
↓
Humans check decision points, Risks, and exceptions
```

What humans confirm especially early:

- What to build
- What not to build
- Domain terminology
- Acceptance Criteria
- Contradictions with existing specifications
- Interface / Test Seam
- External dependencies
- Error Strategy
- Security / Data Boundary
- Design decisions with high reversal cost

The way to reduce review load is not "skipping Review." It is **moving the decisions that need review ahead of implementation, and avoiding a state where humans first discover design intent after implementation**.

This module stops at why the Review Queue clogs and the principle of moving decisions earlier. The main discussion of how to pass Evidence to humans and what to look at to issue a GO is consolidated in `21.X Human Evaluation Interface`.

---
