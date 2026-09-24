# DR-M05 — AI Native Development Lifecycle

> Status: **preview v0.16.8**> Creator / Lead Author: **riottt**

DeepRail does not define AI-driven development as "a procedure that always passes through N stages in series."

What is standardized is **the responsibilities that must not be skipped in development, the conditions for moving forward, Evidence, and return destinations**. Depending on the project's scale, Risk, Method, Autonomy, and Operating Context, multiple responsibilities may be compressed into one task or separated as Gates.

## 9.0 Steps / Gates Do Not Belong to a Specific Actor

Steps and Gates on the Lifecycle are not for fixing human work processes.

A Step is a control unit for safely moving work forward. At minimum, it has the following.

```text
Responsibility
Input
Output
Required Evidence
Transition / Exit Condition
Failure / Return Path
```

Who executes a Step and who evaluates a Gate varies with the Operating Profile.

At initial adoption, the following shape is fine.

```text
AI Execute
↓
Human Evaluate
↓
Human Gate
```

As Evaluation Authority rises, the evaluating agent can change.

```text
Execution Agent
↓
Review Agent / Automated Eval
↓
Human Decision
```

Furthermore, if the required Evidence, Failure Detectability, Rollback, Audit, and Policy hold for the target Work Class, normal Cases can proceed without waiting for individual human approval.

```text
Agent Execution
↓
Independent Evaluation
↓
Policy Gate
├─ PASS      → Next Step
├─ RETRY     → Controlled Retry
└─ EXCEPTION → Human
```

The Gate itself has not disappeared here.
**The Evidence that makes the Gate hold and the agent judging the Gate have changed.**

> **A Step remaining and a human remaining in each Step are not the same thing.**

What DeepRail fixes is not the human process, but **the conditions under which work may proceed**.

---

## 9.1 The Lifecycle Responsibility Model

```text
Intent / Intake
      ↓
Discover
      ↓
Shape / Visualize
      ↕
Align
      ↓
Decide / Commit
      ↓
Specify / Contract
      ↓
Decompose / Plan
      ↓
Execute
      ↓
Verify / Accept
      ↓
Reinvest / Learn
      ↺
```

### Intent / Intake

Clarify what will be changed and why.

Main Outputs:
- Objective / Expected Outcome
- Customer / User
- Business Context
- Initial Scope
- Constraint
- Decision Owner

### Discover

Do not pass requirements straight to implementation; investigate background, current state, Domain, Codebase, constraints, and unknowns.

Main questions:
- What is the real problem
- How does it work now
- Are there contradictions between the customer's words and existing specifications
- What is undecided
- Which Decisions carry high reversal cost

### Shape / Visualize

Convert abstract requirements into **concrete artifacts that let humans and AI look at and judge the same object**.

```text
UI development         → Wireframe / Mock / Prototype / User Flow
API                    → Request / Response Example
Business design        → Process / Scenario
Estimation / sales     → Plan / Price / Scope / Outcome Image
Organizational change  → Before / After / Target Operating Model
Migration              → Architecture / Migration Scenario
```

The purpose of this activity is to keep creating Shared Reality.

### Align

Use the shaped concrete artifacts to align understanding with customers, users, and stakeholders.

```text
Present the proposal
↓
"That's not it"
↓
Fix the Shape
↺

"This is right"
↓
To Decision
```

### Decide / Commit

Determine what to adopt, who decided, and what is not yet decided.

- Decision
- Rationale
- Alternatives
- Risk
- Unknown
- Reversibility
- Decision Owner

High-Risk Decisions may use a Decision Packet.

### Specify / Contract

Convert agreed content into a contract that AI and the team can execute without guessing.

- Requirement
- Acceptance Criteria
- Constraint
- Non-goal
- Interface
- Error Strategy
- Security / Data Boundary
- Evidence Requirement

> **A specification is not "the first tool for aligning understanding"; it is a tool for fixing aligned content as an executable contract.**

### Decompose / Plan

Decompose work into Objective / Epic / Feature / Issue / Agent Task, and place Dependency, Risk, Context, and Gate.
Decomposition is not limited to manual human work; AI may generate and re-decompose using a Rubric.

### Execute

AI / Human execute within the agreed Contract.
If AI discovers unknowns, increased Risk, or Architecture boundaries during implementation, it does not change the Objective on its own; it moves to Re-decomposition or Escalation.

### Verify / Accept

Judge whether the expected Outcome was reached using Machine Check / Observed Behavior / Human Decision, not self-report.

### Reinvest / Learn

Not mere "recording."
Return the outcomes, decisions, failures, and human interventions gained this time into a state where AI and the organization work better next time.

```text
Current Truth
├ Specification
├ API / DB / Architecture
├ ADR
└ Operations

Reusable Learning
├ Rule
├ Skill
├ Eval
├ Agent Contract
├ Gate
└ Harness

Organization
├ Standard
├ Training
├ Decision Policy
└ Operating Model
```

---

## 9.2 The Lifecycle Is Not a One-Way Street

Standardize representative returns.

```text
Execute
↓
Discover an unknown specification
↓
Discover / Align
↓
Update Specify
↓
Re-decompose
↓
Execute
```

```text
Verify
↓
Acceptance mismatch
├ Implementation problem → Execute
├ Spec problem → Specify
├ Understanding problem → Align
└ Objective change → to Intake as a Requirement Change
```

**That AI can re-decompose Work and that AI can redefine the Goal on its own are different things.**

---

## 9.3 Compress at Small Scale, Separate at High Risk

### Lightweight Example

```text
Intent + Discover + Specify
↓
Execute
↓
Verify
↓
Reinvest
```

### Standard Example

```text
Intent
↓
Discover
↓
Shape / Align
↓
Specify
↓
Decompose
↓
Execute
↓
Verify
↓
Reinvest
```

### High Risk / Enterprise Example

```text
Intent
↓
Research / Discover
↓
Alignment Gate
↓
Requirement / Architecture Decision
↓
Specification
↓
Decomposition
↓
Planning Gate
↓
Execution
↓
Verification
↓
Acceptance Gate
↓
Release
↓
Reinvestment
```

Confirm not the number of stages but **that no responsibility has disappeared**.

---

## 9.4 Evaluation / Evidence Is a Control Plane Crossing the Entire Lifecycle

Review is not a stage performed once at the end.

```text
                 EVALUATION / EVIDENCE
────────────────────────────────────────────
Intent
Discover
Shape / Align
Specify
Decompose
Execute
Verify
Reinvest
────────────────────────────────────────────
```

Examples:
- Requirement Review
- Alignment Decision
- Architecture Review
- Work Breakdown Review
- Automated Test / Eval
- PR/MR Review
- Acceptance Review
- Release Decision
- Management Review

The way to reduce human Review load is not to eliminate Review but **to move Review to the right abstraction level and the right timing**.

---

## 9.5 Hold Pre-Implementation Alignment as a Standard Responsibility

Before implementation, dig sufficiently into requirements, design, and Domain understanding, and do not carry undecided matters into the implementation stage.

Main contents:
- Investigate matters answerable from the Codebase
- Fix Domain Vocabulary
- Detect contradictions with existing Domain Models and Documents
- Confirm Acceptance Criteria
- Visualize UI / API / DB / external interfaces as needed
- Confirm Test Seams
- Put Decisions with high reversal cost into writing
- Create a state where the next responsibility can start without guessing

Do not leave confirmed information only inside the Session; reflect it in the Source of Truth.

### 9.5.1 Domain Understanding Is Not "a Finished Document Received Before Implementation"

In complex Domains, a complete Requirement / Domain Model may not exist from the start. Domain Experts, Product, Engineers, and AI iterate Research / Design / Implementation / Feedback while updating understanding and the Model.

It does not end with one interview and written requirements. Problem, Domain, Scenario, and Acceptance are updated many times through implementation and Feedback. Including all of that, this becomes **Knowledge Work that keeps growing Shared Reality**.

```text
Investigate the Domain / Problem
↓
Turn words, Rules, and exceptions into hypotheses
↓
Express them in Scenario / Model / Prototype / Code
↓
Discover discomfort, contradictions, and Unknowns
↓
Update Domain understanding
↺
```

AI can greatly accelerate Research / Comparison / Draft / Model candidate generation. However, to adopt AI proposals, the Team needs enough Problem / Domain understanding and Evaluation Criteria to judge "what is valid."

Here too, do not fix Human-only responsibilities. As AI Capability and Evaluation Reliability rise, Domain analysis, Model proposals, Consistency Checks, and more can also be delegated, but maintain **a structure that externalizes what is correct and can be updated by Evidence**.

### 9.5.1.1 Why — Why Does Domain Understanding Become More Valuable as Implementation Gets Faster?

First, one thing to say.

**What got faster with AI is giving things form. What is correct has not become automatically knowable.**

In the fictional FlowDesk, a request starts with a single sentence.

> **"When the approver is absent, I want a proxy to be able to approve."**

Short. It even looks implementable.

Hand it to AI and it can add proxy-approval fields, build the API, add operations to the screen, and write Tests. Looking only at writing code, the work seems to have advanced considerably.

But that single sentence does not yet contain the answers.

Is a proxy a temporary authority? Who decides "absent"? May high-value applications be proxied? If the proxy setting changes midway, what happens to applications already in flight? For audit, is it enough to record who actually pressed the button? Or should it record whose authority was used?

Writing code does not answer these questions.

What is scarier is that AI gives it form without stopping. An ambiguous request gets fixed — not as ambiguity, but as a plausible screen, API, and Data Model.

**Ambiguity does not disappear. Ambiguity gets an implementation attached.**

The same problem existed in pre-AI development. But implementation itself took time. In the middle of designing, writing, reviewing, and testing, time for a human to stop and ask "is this understanding even right" happened to slip in.

Once generation gets fast, that margin cannot be relied on.

Then, is it safe to make upstream stages heavy and hand AI a completed giant specification?

Not necessarily.

In complex work, some things are understood only by building. A user touching a Prototype realizes "that's not what I meant." Exceptions appear only when writing Tests. An AI investigating existing Code may find a Rule that was in no document.

Implementation is not the endpoint of understanding. It is also material for advancing understanding.

We call this round trip the Knowledge Loop.

```text
Investigate the Problem / Domain
↓
Turn words, Rules, and Scenarios into hypotheses
↓
Express them in Prototype / Code / Test
↓
Find gaps from reality, exceptions, Unknowns
↓
Update Shared Reality
↓
Update Specification / Acceptance / Work
↺
```

This Loop does not need to be fixed as human-only work either. AI can investigate existing materials and Code, organize terminology candidates, search for contradictions, add Scenarios, and compare Model proposals. As capability and evaluation mechanisms rise, much of Domain analysis can be delegated.

However, the ability to produce candidates and the state of being able to decide what to adopt are different.

Even with 100 proposals, if what counts as a correct Outcome is ambiguous, you cannot choose. That is why Shared Reality is needed.

Shared Reality is not having one up-to-date specification book. It is a state where humans and AI share enough understanding of the problem, words, Rules, constraints, decisions, and Acceptance that the next work does not have to start from guesswork. Context Assets such as Vocabulary, Scenarios, Decision Records, Specifications, Tests, and Code are used to recreate that state.

In FlowDesk too, it does not end when the first screen works. If whether high-value applications may be proxy-approved is undecided, place that Unknown somewhere visible. Decide the Decision Owner. Try earlier in low-Risk scope. Then return what was learned to the specification and Acceptance.

Neither build after deciding everything, nor build it all while not knowing.

**Precisely because you can build fast, iterate understanding and implementation in short loops.**

`Discover → Shape / Visualize → Align → Decide → Specify` is not a ritual before letting AI write code. It is an activity for continuously updating the meaning of the work. When new facts come back from implementation, return as many times as needed.

What to watch in practice is not difficult.

- Are the same words used with the same meaning by stakeholders and AI
- Can Rules and exceptions be explained separately
- Are undecided matters visible
- Is what counts as correct externalized
- Is it decided where to return what was learned by building

Back to the first sentence.

"I want a proxy to be able to approve."

If AI is fast, a feature can be built from this sentence right away. Precisely for that reason, do not let that speed pull you into feeling that even the sentence's meaning has been decided.

> **The more AI lowers implementation Cost, the more valuable the ability to keep updating "what to build" and "what counts as correct" becomes.**

### 9.5.2 Context Is a Team Development Asset, Not an AI-only Prompt

This is the Canonical Home of Shared Reality / Context Asset. Later chapters use this definition as a premise.

Here we separate `Shared Reality` and `Context Asset`.

- **Shared Reality:** A state where Human / AI share sufficient common understanding of Problem, Domain, Decision, and Acceptance
- **Context Asset:** Information externalized to recreate, verify, and reuse that state across Sessions / Members

Do not make the following into temporary input for AI only.

- Specifications
- Domain Vocabulary / terminology
- Business Rules
- Constraints
- Architecture / Design Intent
- Decision / Rationale
- Acceptance Criteria
- Known Unknowns

Let Human and AI reference the same Source of Truth, and update it via Reinvest / Learn when it changes.

> **Context development is an investment not only for improving AI answer accuracy but for sharing and reproducing the Team's development decisions.**

Even if AI accelerates Coding and Drafts, the responsibilities of Domain understanding, Modeling, and Knowledge Crunching do not disappear. In DeepRail, these are maintained and updated as `Knowledge Loop / Shared Reality / Domain Modeling`, separately from implementation speed.

---

## 9.6 Position of Workflow / Skill Chains

Do not make a specific OSS, Skill name, or Agent Runtime into a DeepRail stage name.
Map external implementation examples to the following abstract responsibilities.

| Implementation pattern | Responsibility in DeepRail |
|---|---|
| Interview / research workflow | Discover |
| Mock / prototype generation | Shape / Visualize |
| Spec generation | Specify / Contract |
| Ticket generation | Decompose / Plan |
| Coding agent | Execute |
| Code review / test agent | Verify |
| Documentation / rule feedback | Reinvest / Learn |

Maintain a structure where the upper-level standard does not break even if external implementations are discontinued or changed.
