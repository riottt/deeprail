# DR-M09 — Team and Role Operations Guide

> Status: **preview v0.16.8**> Creator / Lead Author: **riottt**

This chapter does not create "new job titles for AI."
It defines **AI-Native Team Leadership Functions** that can be assigned to existing Roles such as Scrum Master, Development Lead, Tech Lead, Engineering Lead, and Sub Lead.

> **What is standardized is not Role names, but the responsibilities and decision-making that make a Team work.**

---

## 13.1 AI-Native Team Leadership Function

Core responsibilities a Team Lead-equivalent human should hold:

```text
Understand Outcome / Priority
↓
Generate and evaluate Work Structure with AI
↓
Assign Execution to Human / AI
↓
Prepare Context / Tool / Environment / Permission
↓
Observe state from Evidence
↓
Handle Decision / Blocker / Exception
↓
Re-decompose Work if needed
↓
Evaluate and accept outcomes
↓
Return Failure / Human Intervention to System Improvement
```

A Team Lead is not the person who writes every Issue, prompts every Agent one by one, and reads every Diff from the top.
The role shifts to **the person who designs the team's Flow, Decisions, and Control Points**.

---

## 13.2 Responsibility Boundary Between Planning / Execution

In DeepRail, Planning and Execution are not treated as the same responsibility. Planning handles "what to make hold together, which Approach to take, and what counts as done"; Execution handles "which Artifact to change, which operations to perform, and which Checks to run."

However, do not fix Planning as Human-only forever. Depending on Work Class, Risk, Evidence Reliability, Failure Detectability, Reversibility, Permission, and Accountability, responsibilities on the Planning side can also be delegated in stages.

In the initial design of Team Leadership, start from the following separation.

```text
Human-centric
├ Outcome
├ Priority
├ Risk Appetite
├ Acceptance
├ Decision Boundary
└ Exception

Easily delegated to AI
├ Exploration
├ Detailed Plan
├ Work Decomposition candidates
├ Implementation
├ Tool Operation
├ Test
├ Status Aggregation
└ Documentation / Improvement Proposal
```

As Autonomy rises, AI expands toward the Planning side, but Objective changes, Risk acceptance, and significant exceptions follow Decision Rights.

---

## 13.3 Delegation Contract

For both Human→AI and AI→AI, make a common Work Contract usable.

```text
Purpose
Objective
Input / Context
Scope
Non-goal
Source of Truth
Allowed Tools
Permission
Expected Output
Acceptance Criteria
Required Evidence
Stop Condition
Escalation Condition
```

Rather than vague "look into it" or "implement it," contract **what to make hold together, how far to delegate, and what to return**.

---

## 13.4 Example Human Roles

| Role | Responsibility |
|---|---|
| Team Lead / Development Lead | Flow, Priority, Decision, Blocker, Risk, Team Operating Model |
| Product / Feature Owner | Outcome, requirements, Acceptance responsibility |
| Developer | Execution using the Harness / Domain judgment |
| Reviewer / Evaluator | Evaluation of design, deliverables, Evidence |
| Quality Owner | Gate, Test, Eval management |
| Environment / Platform Owner | Environment / CI/CD / Runtime state management |
| Harness Maintainer | Agent/Skill/Rule/Harness management |
| Security Approver | Approval of high-risk operations and Data / Production boundaries |

Role names may be adapted to the organization.
In a small Team, one person may hold multiple Functions.

---

## 13.5 AI Agent Responsibility Design

Do not multiply Agents as personality copies of a human org chart.
Separate responsibilities by Work Contract / Context Boundary / Tool Boundary.

Agent Roles are not created from stage names; they are derived from the following **Viewpoint Contract**.

```text
What to observe      What to watch / which canonical sources to reference
How to interpret     How to read / which evaluation axes to hold
What to output       What to return / Output Contract
Authority            What it may execute
Cost / Model profile In which Model tier it works
```

> **Defining a Role and placing one Agent are different things.**

Responsibilities that can be processed deterministically go to Rule / Script / Tool / CI. Make something an Agent only when it needs an independent Context, viewpoint, authority, or deliverable contract. Do not add an Agent for every stage.

Representative examples:

| Function | Responsibility |
|---|---|
| Orchestrator / Lead | Planning, decomposition, assignment, integration, re-planning |
| Research | Specification, code, and impact-range investigation |
| Architecture | Design candidates, Trade-off organization |
| Implementation | Implementation of agreed Contracts |
| Test / Evaluator | Test, Observed Behavior, Acceptance confirmation |
| Independent Review | Review from a separate Context |
| Documentation / Learning | Current Truth updates, improvement-candidate extraction |
| Release / Operations | Release preparation, Production verification |

---

## 13.6 Team Capacity — Do Not Treat Agent Count as Throughput

See a Team's effective capacity with at least the following.

```text
Execution Capacity
Review Capacity
Approval Capacity
Environment Capacity
Decision Capacity
Product / Domain Capacity
```

If you add AI Agents and raise only Execution Capacity, the Bottleneck moves to the Review Queue, Approval Queue, Environment contention, and Decision waiting.

When approval clogs, it does not end with mere delay. Once volume exceeds human Attention, the Gate remains institutionally while substantive checking drains away. This is **Approval Hollowing / Rubber-stamp Risk**.

Team Capacity should include how much can be Reviewed, Decided, and Approved per week. Do not detach the WIP limit of AI Execution from that bandwidth either.

Set the WIP Limit considering not only headcount but also:
- Human Reviewable volume
- CI / Test Environment slots
- Shared Environment
- Risk Class
- Dependency
- Decision waiting

---

## 13.7 Turn Team Meetings from "Status Readout" into a Decision System

Do not read out, one by one in a synchronous human meeting, Status that AI can collect.
Concentrate meetings on **alignment, Decision, Exception, and Learning**.

The standard Meeting Functions are the following nine.
They do not all need to be held as separate meetings. Merge them according to scale, Method, and Risk.

### Meeting 1: Outcome / Intake Sync

**Purpose:** Align on what the work is meant to make hold together.
**Held:** At Epic / Initiative start and on significant requirement changes.
**Main participants:** Product/Customer owner, Team Lead, necessary Domain Experts, AI.

Decide:
- Objective / Expected Outcome
- Scope / Non-goal
- Priority / Deadline
- Initial Risk / Constraint
- Success Metric
- Decision Owner

AI prepares in advance:
- Existing Context summary
- Unknown / Open Question
- Conflict / Assumption

**Output:** Outcome Contract / Intake Decision.

### Meeting 2: Discovery / Alignment Session

**Purpose:** Prevent "using the same words while imagining different things."
**Held:** Upstream, on important changes, when there is a perception gap with the customer.

What AI can prepare:
- Mock / Wireframe / Prototype
- User / Business Flow
- API / Data Example
- Before / After
- Plan / Price / Scope comparison
- Architecture / Migration scenario

Decide:
- Domain Interpretation
- User Behavior
- Boundary
- Acceptance Image
- High-cost Decision
- Open Question

**Output:** Shared Reality / Alignment Record.

### Meeting 3: AI Refinement / Work Design

**Purpose:** Evaluate whether the Work Structure can be executed safely.
**Held:** Before Epic / Feature start, and on re-decomposition Triggers.

AI generates:
- Epic / Feature / Issue / Agent Task candidates
- Dependency Graph
- Risk / Context / Parallelism analysis

Humans mainly confirm:
- Outcome independence
- Acceptance separation
- Risk
- Dependency
- Human Gate
- Source of Truth
- Parallel Conflict

**Output:** Execution-ready Work Graph.

### Meeting 4: Execution Planning

**Purpose:** Decide "how to execute safely" rather than "who to assign."

Decide:
- Human / AI assignment
- Agent / Runtime
- Required Context
- Allowed Tool
- Environment
- Permission Boundary
- Required Evidence
- Human Gate
- Stop / Escalation Condition

**Output:** Work Contract / Execution Plan.

### Meeting 5: Decision & Blocker Sync

A replacement for and extension of the conventional Daily.

AI aggregates before the meeting:

```text
Completed
In Progress
Blocked
Failed
Waiting Approval
Risk Changed
Acceptance Changed
Environment Failure
Unknown
Decision Required
```

Handled in the meeting:
- Decision Required
- Blocker-removal Owner
- Re-decomposition necessity
- Priority change
- Agent stop / resume
- Permission change
- Environment Owner escalation

If it is only Status, do not bring it to a synchronous meeting.

**Output:** Decision / Escalation / Updated Work Graph.

### Meeting 6: Technical / Architecture Decision Sync

**Purpose:** Humans judge the design boundaries AI must not cross.
**Held:** Event-driven. Not held daily.

AI generates a Decision Packet in advance.

```text
Decision Required
Context
Option A / B / ...
Trade-off
Recommendation
Evidence
Risk
Unknown
Reversibility
```

**Output:** ADR / Decision Record / updated Contract.

### Meeting 7: Review / Acceptance

**Purpose:** Judge deliverables from Outcome / Evidence, not by reading every Raw Artifact.

Order of viewing:

```text
Decision / Acceptance
↓
Summary
↓
Evidence
↓
High-risk Change
↓
Raw Artifact (only when needed)
```

Confirm:
- Intent
- Acceptance Criteria
- Observed Result
- Test / Eval
- Risk / Deviation
- Unknown / Untested

**Output:** Accept / Reject / Request Change / Escalate.

### Meeting 8: Release Readiness

**Purpose:** Judge "development complete" and "shippable to production" separately.

Confirm:
- Acceptance complete
- CI status
- Security / Compliance checks
- Migration
- Residual Risk
- Rollback
- Monitoring
- Human Approval
- Living Document / Runbook readiness

**Output:** Release Decision Packet / Go-NoGo.

### Meeting 9: Learning / Harness Retro

Do not end it as a conventional "human retrospective."

Central question:

> **Can the places where humans intervened or AI hesitated this time be reduced by mechanisms next time?**

| Finding | Main reinvestment destination |
|---|---|
| Requirements ambiguous every time | Intake / Requirement Template |
| Agent repeats the same mistake | Rule |
| Same procedure explained every time | Skill |
| Test gaps | Eval / Gate |
| Tool shortage | Tool / MCP |
| Environment incident | Environment Gate / Provenance |
| Same approval repeated | Delegation Policy |
| Huge Diff Review | Review Packet improvement |
| Poor Work decomposition | Decomposition Rubric |
| Waiting on organizational judgment | Decision Rights / Operating Model |

**Output:** Harness Backlog / Standard Backlog / Training Backlog.

---

## 13.8 Bundle Meetings According to the Method

### Scrum Example

```text
Sprint Planning
= Outcome / Work Design / Execution Planning

Daily
= Decision & Blocker Sync

Refinement
= Discovery / Alignment + AI Refinement

Sprint Review
= Review / Acceptance

Retro
= Learning / Harness Retro
```

Changing Scrum Event names itself is not a DeepRail requirement.
**Change what is Decided in the Event, what AI prepares, and what is kept as Evidence.**

### Waterfall / Enterprise Example

```text
Requirements coordination meeting
→ Discovery / Alignment

Design review
→ Decision Packet / Architecture Decision

Progress meeting
→ Decision & Blocker Sync

Test judgment
→ Evidence / Acceptance

Release judgment
→ Release Readiness

Retrospective / improvement meeting
→ Harness / Standard Learning
```

---

## 13.9 Team Lead's Standard Dashboard

What a Team Lead should see daily is centered on pending decisions, not a Status list.

```text
Outcome Health
Decision Required
Blocker
Risk Change
Approval Queue
Review Queue
Environment Health
WIP / Dependency
Acceptance Progress
Human Intervention Hotspot
Harness / Standard Improvement Candidate
```

**Human Attention has a limit. Do not design as if it were infinite.**

# Part C. Repository / Tool / AI Runtime

## 13.4 Team Management Review

In a Human + AI Team, do not read out in human meetings the state information AI can report.

Concentrate synchronous human time on Decisions.

```text
Planning
→ Priority / Objective / Boundary

Refinement
→ Confirm Outcome / Risk / Dependency of AI decomposition proposals

Daily / Async
→ AI aggregates Status / Blocker / Evidence
→ Human handles only Decision / Escalation

Review
→ Decision Packet / Evidence / Risk centered

Retro
→ Return Failures to Rule / Skill / Eval / Process
```

Important metrics in Team operations:

```text
Execution Capacity
Review Capacity
Approval Capacity
Environment Capacity
Decision Capacity
```

Do not treat Agent count itself as Throughput.

---
