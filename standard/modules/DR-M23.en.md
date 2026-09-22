# DR-M23 — Management, AI Adoption, and Maturity Operations Guide

> Status: **preview v0.16.8**> Creator / Lead Author: **riottt**

**Layer:** Organization / Management
**Main readers:** CEO / Founder / CTO / CIO / VPoE / AI & DX promotion leads / PMO
**Purpose:** Judge AI adoption not as Tool adoption but as investment in the Operating Model and Organization Capability.

## M23.1 Why Adopt

Fix the purpose of AI adoption first.

Candidates:

- Lead Time
- Quality
- Capacity
- Cost
- Innovation
- Knowledge leverage
- Business responsiveness

Do not make "using AI" itself the purpose.

## M23.2 Where to Start

Choose Pilot candidates by:

```text
Business value
× Repeatability
× Observability
× Reversibility
× Risk
× Available context
```

Do not expand to the most Critical area from the start.

## M23.3 Pilot Contract

Define before the Pilot starts.

```text
Objective
Scope
Baseline
Evaluation function
Owner
Allowed autonomy
Required gates
Kill criteria
Duration
Expected learning
```

A stage where the Pilot's purpose is not "productivity improvement" but "discovering Failures" is also allowed.

## M23.4 Investment Model

Include in TCO.

- Model / API
- Tool license
- Platform
- Harness development
- Eval / Test
- Security / Governance
- Training
- Review capacity
- Migration
- Maintenance
- Incident / rollback
- Change management

Do not compare only AI cost against personnel cost.

## M23.5 KPI / ROI

Do not judge by local Coding Speed alone.

```text
End-to-end Lead Time
Human Touch Time
Review Time
Queue Time
Rework
Defect
Release Frequency
Incident
Human Intervention
Adoption
Model / Tool Cost
Business Outcome
```

Change the main evaluation function by maturity.

### M23.5-A Local-to-System Translation Check

After AI adoption, do not make investment decisions on Signals alone like "Coding got faster," "PRs increased," or "the person feels faster." Translate whether local improvement reached System Outcome.

```text
Local Signal
Coding Time / Generated Changes / Agent Runs
↓
Flow Translation
Batch Size / Queue Time / Review Time / Integration Cost
↓
Quality Translation
Rework / Escaped Defect / Instability / Rollback
↓
Delivery Outcome
Lead Time / Release Frequency / Recovery
↓
Business Outcome
User Value / Revenue / Cost / Risk / Learning Speed
```

Confirm at least the following.

- Has increased generation volume enlarged the Change Batch
- Has Human Touch Time moved into Review / Verification
- Are Queue / Integration waits increasing
- Did Lead Time improve even including Rework / Incident / Rollback
- Do developers' subjective Speedup and observed values match
- Is the Baseline updated after Tool generation or Work Class changes

> **Getting locally faster is not evidence the System got faster. Judge AI's effect after it passes through the Value Stream.**

## M23.6 Governance

Do not make Governance a set of prohibitions.

Hold at least:

```text
Allowed use
Disallowed use
Permission
Approval
Evidence
Audit
Exception
Escalation
Rollback
```

## M23.7 Ownership

Do not end at merely appointing an "AI promotion lead."

Explicitly assign Owners for Standard / Harness / Eval / Risk / Environment / Adoption, and confirm staffing and Bus Factor.

## M23.8 Maturity

```text
M0 Exploration
M1 Controlled Adoption
M2 Standardization
M3 Scaled Adoption
M4 Continuous Optimization
```

Promote by Evidence, not enthusiasm.

## M23.8-A Do Not Look at Maturity as a Single Number

An organization does not mature evenly. Evaluate at least the following four axes independently.

```text
Governance
Measurement
Reinvestment
Reproducibility
```

Example:

```text
Overall M1
Governance       M2
Measurement      M0
Reinvestment     M1
Reproducibility  M0
```

From this asymmetry, decide what to invest in next.

### Promotion Evidence Catalog

Judge promotion not by "using AI a lot" but by Evidence.

M1 candidate Evidence examples:

- Another member / another environment could complete the same Golden / Standard Flow
- Fixtures actually work when a Gate changes
- There are records of Failure → Rule / Skill / Eval reinvestment
- Approval / Decision records can be traced later
- Someone other than the Harness Owner could take over operations
- A Delegation Contract exists when using S1/S2

M2 candidate Evidence examples:

- An Enforcement baseline exists
- Important Metrics that were `null` got a proper Writer implemented
- Knowledge Reinvestment actually reached canonical sources, not just proposals
- Areas needing independence such as Eval Owner / Approval Owner are established

Do not make the catalog a universal Checklist. For Evidence unobtainable in the Operating Context, declare the reason and substitute Evidence.

### Kill Criteria

When entering each Pilot / Maturity Stage, place `continue / change course / stop` conditions in advance.

Do not make "no results in Exploration" itself an immediate withdrawal condition. At M0, candidate stop conditions are **learning has stopped, significant Risk is uncontrollable, or the work is unobservable**.

## M23.9 Scale-out

Horizontal rollout transplants not a copy of the completed Harness but:

> **parts + how to measure + the assembly process**

If the Operating Context differs, do not distribute the same Harness as-is.

## M23.10 Stop / Rollback

Define stop conditions before the Pilot starts.

Examples:

- Quality degradation
- Risk incident
- Review capacity collapse
- Cost ceiling exceed
- insufficient observability
- unacceptable human intervention
- business outcome absent

## M23.11 Executive Dashboard

At M0-M1, do not fabricate Flow Metrics that do not exist.

From M2 onward, gradually add:

```text
Flow
Quality
Cost
Risk
Adoption
Enforcement
Business Outcome
```

---

## 23.8 Conditions for AI Adoption to Become Management Strategy

AI adoption is not always management strategy.
While it stays closed as a simple personal-assistance Tool, it can be treated as a local productivity improvement.

But the more AI enters the following responsibilities, the more it becomes a management issue.

```text
Execution
↓
Planning
↓
Work Decomposition
↓
Evaluation
↓
Coordination
↓
Priority Proposal
↓
Resource Allocation
↓
Organization Design
↓
Strategy Option Design
```

At this stage, the questions management must judge change.

- Which Human Roles to reduce, change, or reassign
- Which Decision Rights to delegate to AI
- How to redesign the Management Layer with AI
- Which Decisions to concentrate Human Attention on
- How to convert AI Capability into competitive advantage
- How to separate capabilities AI can easily imitate from organization-specific advantage
- How to convey Purpose / Risk Appetite / Business Priority into AI execution
- How to reflect new Operating Models made possible by AI into business strategy

> **AI not only makes operations efficient; it changes "who does the work," "who decides," and "what becomes the competitive advantage," so from a certain maturity point it becomes management strategy itself.**

Track this change in stages via `Transformation Profile / Maturity / Autonomy / Decision Rights / Evidence`.
