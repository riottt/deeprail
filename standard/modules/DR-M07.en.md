# DR-M07 — Scale Assessment and Work Item Decomposition Rules

> Status: **preview v0.16.8**> Creator / Lead Author: **riottt**

This chapter is not a manual for humans to fully decompose Epic / Feature / Issue / Task by hand.

If AI capability and Autonomy are sufficient, **AI may generate and re-decompose the Work Breakdown itself**.

Human responsibility shifts to clarifying

```text
Objective
Constraint
Risk
Non-goal
Acceptance
Decision Boundary
```

and to evaluating and approving, at the necessary granularity, the Work Structure that AI generates.

This chapter divides work by the following criteria.

> **It is a design viewpoint for humans and, at the same time, an Evaluation Rubric for AI to autonomously decompose and reconstruct Work.**

---

## 11.1 Scale Assessment

### Small

- Within a single feature
- No API Contract change
- No DB Schema change
- No impact on other teams
- Easy Rollback
- Clear scope of impact

### Medium

- Multiple components
- Limited API or DB changes
- Multiple files / multiple Layers
- Requires some design consideration
- Manageable per Issue

### Large

- Multiple Repositories
- Architecture change
- DB Migration
- External interface change
- Multi-team impact
- Security impact
- Long duration / multiple Issues
- Requires a Release plan

---

## 11.2 Scale × Development Lifecycle

| Item | Small | Medium | Large |
|---|---|---|---|
| Lifecycle Responsibility | Lightweight | Standard | Full |
| Requirements document | Can be replaced by an Issue | Diff-focused | Formal deliverable |
| Design | Local diff | Design Delta | Formal Design |
| Human Gate | Few | Standard | Many |
| Test | Local | Feature | Including integration |
| Reinvest / Learn | Affected areas only | Related canonical sources | Full canonical set |
| Work Item | Issue | Issue + Task | Epic + Issue |

Being small does not mean eliminating the Reinvest / Learn responsibility.

"Confirmed there is nothing to update or reinvest in, then finished" is also a valid Reinvest / Learn result.

---

## 11.3 DeepRail Work Model

Work Items are handled with the following logical model.

```text
Business Objective / Outcome
        ↓
Initiative / Epic
        ↓
Feature / Capability
        ↓
Issue / Work Item
        ↓
Execution Task
        ↓
Agent Task
```

This does not enforce a product-specific hierarchy such as a particular Work Management tool.

Names and hierarchies may differ per Tool.
What we want to align is **meaning and responsibility boundaries**, not names.

| Level | Meaning | Main Owner | Completion Judgment |
|---|---|---|---|
| Objective / Outcome | What to achieve | Business / Product | Outcome is observable |
| Epic | Large change / investment unit | Epic Owner | Satisfies Epic Outcome |
| Feature | Usable capability / value | Feature Owner | Feature Acceptance |
| Issue | A change that can be completion-judged independently | Issue Owner | Evidence + Gate |
| Task | Work inside an Issue | Human / AI | Task Output |
| Agent Task | Execution contract handed to AI | AI Runtime | Output Contract |

PR / MR is not part of the Work Item hierarchy; it is the integration unit of Source changes.

---

## 11.4 The Basic Idea of Work Decomposition

Conventional:

```text
Human
↓
Split Epics
↓
Split Features
↓
Split Issues
↓
Split Tasks
↓
Distribute to Developers
```

AI Native:

```text
Human
├ Objective
├ Constraint
├ Risk
├ Non-goal
├ Acceptance
└ Decision Boundary
        ↓
AI
├ Epic candidates
├ Feature candidates
├ Issue candidates
├ Dependency
├ Parallelization Plan
└ Agent Task
        ↓
Machine / AI Evaluation
        ↓
Human Decision only where needed
        ↓
Execution
```

DeepRail does not assume that humans complete the Work Breakdown Structure from the start.

---

## 11.5 Epic Extraction Rubric

An Epic is not "a box that holds many Issues."

It is **a large unit of change with independent Outcome, investment, responsibility, and Risk**.

When AI generates Epic candidates, it evaluates at least the following viewpoints.

| Viewpoint | Question to Judge |
|---|---|
| Outcome | Does it have an independent Business / User Outcome |
| Boundary | Are responsibility and purpose boundaries with other Epics clear |
| Acceptance | Can completion be judged at the Epic level alone |
| Ownership | Can a decision Owner be identified |
| Dependency | Is dependency on other Epics not excessive |
| Architecture | Does it not unnaturally cross multiple Architecture boundaries |
| Risk | Can high-Risk changes be controlled independently |
| Reversibility | Can it be independently stopped, degraded, or rolled back |
| Context | Can lower-level Work be decomposed into Context that AI can handle |
| Parallelism | Can it be safely parallelized with other Epics / Features as independent Execution / Evidence / Retry / Rollback units |
| Source of Truth | Are the canonical sources and responsibility scope it updates clear |
| Human Gate | Can important human judgment boundaries be identified |
| Evidence | Can the Outcome be proven with independent Evidence |

### 11.5.1 Verifiable Parallelism

"Being able to launch multiple Agents" alone does not satisfy the conditions for Parallelism.
The more Work satisfies the following, the easier it is to move to Parallel Execution.

```text
Outcome Independence
Acceptance Independence
Context Sufficiency
State / Workspace Isolation
Independent Evidence
Failure Localization
Retry Independence
Rollback / Reversibility
Integration Boundary
```

In particular, when each piece of Work contends for the same Source / Environment / Mutable State and one side's Failure breaks the other's Evidence, adding more Agents is not treated as safe Parallelism.

```text
Adding Agents
≠
Parallelism goes up

Work can be independently executed, proven, and recovered
→
Parallelism can be raised safely
```

When parallelization is impossible, consider Work re-decomposition, Workspace separation, State separation, Acceptance redefinition, or adding an Integration Gate first.

### 11.5.1-A Parallel Fit — Separating "Can Parallelize" from "Worth Parallelizing"

Even when the Verifiable Parallelism conditions are met, we do not always move to Parallel Execution. The parallelization decision also looks at the following.

```text
Value of Earlier Completion
Work Independence
Coordination Cost
Evaluation Cost
Compute / Token Cost
Integration Cost
Failure Localization Cost
Human Attention Cost
```

```text
Parallelizable = can be independently executed, proven, and recovered
Worth Parallelizing = the value of finishing earlier outweighs the Cost of creating that independence
```

Work with dense dependencies requiring frequent synchronization, Work that must constantly share the same Context, and Work whose evaluation Cost exceeds its implementation Cost may be better as Sequential / Staged Execution even when Agents can be added.

> **Parallelization is not only a capability; it is also an investment decision. Do not confuse low startup Cost with low Coordination Cost.**

### 11.5.1.1 Why — Why Parallelism Is Determined by Verifiability, Not Agent Count

Launch ten Agents and work advances tenfold.

There are moments when it looks that way. Ten executions line up on the screen and Code grows simultaneously. Clearly faster than one human working in order.

But the true cost of parallelization appears at the end.

Suppose in FlowDesk, Frontend, Backend, DB Migration, audit Log, and Test were each handed to different Agents. Five advanced simultaneously. But the Backend Agent changed the proxy-approval State, and the DB Agent changed the same Schema. The Frontend was implemented assuming the old Response Shape, and the Test Agent produced Green looking at only one Branch.

Five Agents are working. The work is not moving forward.

Rather, the human who integrates at the end is carrying the job of untangling five changes.

What clogged this scene is not Agent performance but how the work was cut. **The parallelized pieces of work were not units that could independently prove completion.**

```text
Execution independence
One side advancing does not break the other's State

Judgment independence
Each Acceptance can be confirmed separately

Failure independence
When one side fails, cause and impact can be localized

Recovery independence
Only one side can be Retried / Rolled back
```

Agent count is not the first number to decide. First cut the Work. Separate Sources and Workspaces. Do not over-share Mutable State. Make Acceptance clear. Establish Evidence per Work. Decide the Integration Boundary. Only then can you say "these may run at the same time."

Conversely, forcibly parallelizing work that does not meet these conditions raises Local Throughput while lowering System Throughput. Because it looks fast when counting only generated Artifacts, discovery comes late.

With AI, the Cost of adding an Agent is low, making this problem even harder to see. Low startup Cost and low integration Cost are different things.

If you truly want to parallelize FlowDesk's five pieces of Work, you need preparation such as "fix the Audit Log contract first," "put the API Contract in the Source of Truth," "make DB Migration an independent Release / Rollback unit," and "verify Frontend with Contract Tests."

Once that is done, each piece holds its own Evidence, and only the boundaries need checking at Integration.

> **Parallelism is not how many can run at once. It is determined by whether, while running at once, correctness and failure can still be handled separately.**

Before adding Agents, divide the work. To never forget this order, we give it the name Verifiable Parallelism.

### Conditions for Splitting into Separate Epics

When any of the following is strong, AI proposes Epic separation.

```text
Multiple Outcomes exist
Owners differ
Risk Classes differ greatly
Architecture boundaries are independent
Release / Rollback units differ
Business Decisions are independent
Can be executed at different times without dependency
Evidence holds separately
```

### Conditions for Not Over-Splitting Epics

Avoid separate Epics in the following cases.

```text
Mere Frontend / Backend separation
Mere owning-Team separation
Splitting the same Outcome only by technical Layer
Always requires simultaneous Release
Acceptance is one piece
Splitting only increases Coordination Cost
```

Do not map technical structure directly onto the Business Work Structure.

---

## 11.6 Epic Contract

An Epic has at least the following.

```yaml
epic:
  objective:
  expected_outcome:
  owner:
  scope:
  non_goals:
  business_context:
  affected_capabilities:
  affected_systems:
  constraints:
  risk:
  success_metrics:
  dependencies:
  decision_points:
  target_operating_context:
  completion_evidence:
```

AI does not fix unknown items by guessing; it leaves them as Unknown / Question.

---

## 11.7 Feature Extraction Rubric

A Feature is cut not as an "implementation Component" but, in principle, as **a usable Capability / Behavior**.

Good example:

```text
Epic: Bring contract procedures online

Feature A: Can submit a contract application
Feature B: Can approve
Feature C: Can check progress
```

Example to avoid:

```text
Feature A: Frontend
Feature B: Backend
Feature C: Database
```

However, when the technical Capability itself is the Outcome, such as an Architecture migration, a technically-axed Feature is allowed.

Feature judgment viewpoints:

- Can be explained as a usable capability
- Acceptance can be defined independently
- Can be split into lower-level Issues
- Has Traceability to the Outcome
- Dependencies on other Features are explainable
- Can be independently verified via Release / Feature Flag etc.

---

## 11.8 Issue Extraction Rubric

An Issue is the central unit of AI-driven execution.

A good Issue roughly satisfies the following.

```text
Independent Acceptance
× Testability
× Reviewability
× Context Fit
× Low Conflict
× Clear Source of Truth
× Evidenceability
```

Judgment viewpoints:

- Does it have an independent completion condition
- Is it testable
- Is it reviewable
- Is the Context volume not excessive
- Is conflict with other Issues not too strong
- Can the Source of Truth be identified
- Can Required Evidence be defined
- Does it make a reasonable diff as a PR / Patch
- Is the return destination on Failure known

In AI-driven work, do not fix "1 Issue = 1 Agent Session."

An Issue is a unit in Product / Project management and,
on the AI Runtime, can be re-decomposed into multiple Agent Tasks as needed.

---

## 11.9 Agent Task Extraction Rubric

An Agent Task is the **minimum execution contract** handed to AI.

```text
Agent Task
=
One Clear Objective
+
Bounded Context
+
Bounded Permission
+
Explicit Output Contract
+
Verification
+
Stop / Escalation Condition
```

Recommended conditions:

- One clear objective
- Required Context can be enumerated
- In principle, a range handleable in 1 fresh context
- Clear Tool / Permission scope
- Clear output format
- A way to confirm completion
- A stop condition when unclear
- Write conflicts with other Agent Tasks are manageable

An Agent Task does not always need to be registered in Work Management etc.
It may be a temporary Execution Unit inside the Runtime.

---

## 11.10 Autonomous Decomposition Flow by AI

```text
Objective / Epic
      ↓
AI Decomposition
      ↓
Feature candidates
      ↓
Rubric Evaluation
      ↓
Issue candidates
      ↓
Dependency / Risk / Context Analysis
      ↓
Agent Task candidates
      ↓
Execution
      ↓
Context Overflow / New Finding / Failure
      ↓
Re-decomposition
      ↺
```

AI may reconstruct the Work Structure mid-execution.

Make Work Breakdown not a static plan but
**a Living Structure updated many times by Evidence and new Context**.

---

## 11.11 Re-decomposition Triggers

In the following cases, AI considers re-decomposing the Work Item.

- Context exceeds the fresh window
- Acceptance Criteria split into multiple independent results
- An unexpected Architecture boundary is found
- An area with higher-than-expected Risk is discovered
- Write conflicts between Agents increase
- Too large as a Test / Review unit
- A Decision by another Owner becomes necessary
- Independent waiting occurs due to Environment / External Dependency
- The change scope exceeds the declared Scope

If re-decomposition changes the Objective or Acceptance,
do not treat it as merely reassigning Tasks. Record it as a Requirement Change.

---

## 11.12 Dependency Model

Do not let Dependency end as a mere "blocks" link.

Make it possible to distinguish at least the following.

```text
Data Dependency
Architecture Dependency
Decision Dependency
Environment Dependency
External Dependency
Human Approval Dependency
Release Dependency
Source-of-Truth Dependency
```

AI uses the Dependency Graph to judge:

- Execution order
- Parallelization possibility
- Human Gate
- Environment preparation
- Escalation destination

---

## 11.13 Work Decomposition and Autonomy

Connect the autonomy of work decomposition to A0–A5.

| Autonomy | Work Decomposition |
|---|---|
| A0 | AI only proposes a decomposition plan |
| A1 | Human confirms Issue / Task decomposition |
| A2 | AI autonomously decomposes inside an Issue into Tasks / Agent Tasks |
| A3 | AI generates and re-decomposes Issues from a Feature |
| A4 | AI generates Feature / Issue structure from an Epic. Human focuses on Epic Outcome / Risk / Exception |
| A5 | AI generates up to Epic candidates from Portfolio / Initiative. Human focuses on Strategy / Investment / Exception |

As Autonomy rises, the granularity humans watch moves upward.

```text
A0-A1
Human → Issue / Task

A2-A3
Human → Feature / Boundary

A4
Human → Epic Outcome / Risk

A5
Human → Strategy / Portfolio / Investment
```

The smarter AI gets, the less human value should be fixed to "the ability to decompose finely."

---

## 11.14 Decomposition Gate

For high-Risk / high-impact Work, do not adopt AI decomposition unconditionally.

Main points a Human confirms:

```text
Outcome
Scope Boundary
Non-goal
Architecture
Security / Compliance
Irreversible Decision
Cross-team Dependency
Investment
Acceptance
```

On the other hand, low-Risk and evaluatable lower-level decomposition can be delegated to AI.

---

## 11.15 Mapping to Tools

The DeepRail Work Model does not depend on a specific product.

Example:

```text
DeepRail      Work Management / SCM Platform etc.
Epic       → Epic / Initiative / Parent
Feature    → Feature / Story / Parent Issue
Issue      → Issue / Work Item / Story
Task       → Task / Subtask
Agent Task → Runtime-internal Execution Unit
```

Map according to the Tool's hierarchy constraints.

However, maintain the logical Traceability:

```text
Objective
→ Epic
→ Feature
→ Issue
→ Evidence
→ Outcome
```

---
