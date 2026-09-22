# DR-M15 — Talent Development, Proficiency, and Practice Guide for the AI Era

> Status: **preview v0.16.8**> Creator / Lead Author: **RIO AMADA**

## 19.1 The Purpose of Talent Development

Teaching only how to operate AI Tools is not called talent development.

What we want to grow is, beyond tool operation speed, the following abilities.

```text
Can use AI
↓
Can delegate work to AI
↓
Can evaluate AI output from Evidence
↓
Can structure work into AI-executable Work
↓
Can operate a Human + AI Team
↓
Can improve Harness / Eval / Process
↓
Can design AI-Native organizational capability
```

---

## 19.2 Human AI Proficiency / Leadership Maturity

| Level | Profile | Main abilities |
|---|---|---|
| HC0 | Not proficient with AI | Uses AI in a limited way |
| HC1 | AI User | Can make requests including purpose and constraints |
| HC2 | AI Operator | Completes work using Context / Tool / Harness |
| HC3 | AI Evaluator | Evaluates output from Evidence / Acceptance / Risk |
| HC4 | AI Orchestrator | Designs Work decomposition, Delegation, multiple AIs, Human Gates |
| HC5 | AI System Designer | Designs Harness / Eval / CI/CD connection / Failure improvement |
| HC6 | AI Native Leader | Operates Team / Operating Model / Transformation |

Do not use HC0–HC6 as ranking for personnel evaluation. What we look at is **which responsibilities can be safely carried**.

For talent development stages, use `HC0–HC6` (Human Capability). Harness maturity is `H0–H6`, and delegation qualifications on the Operating Context are `H-1–H-3`; keep the symbols' responsibilities separate.

---

## 19.2-A Experience Curve Recomposition — The Value of Experience Does Not Disappear. It Is Rearranged

An Engineer eight months in finishes a Feature before an Engineer with eight years of experience.

In the AI era, such scenes are entirely possible.

Even so, you cannot say "the newcomer is more capable than the veteran." What is changing is not human value but **the path by which experience turns into outcomes**.

For example, assign a small, clearly bounded Feature to two people. The eight-year Engineer asks AI to implement, then reads the entire Diff at the end and reconstructs the specification and impact in their head. The eight-month Engineer places Acceptance first, hands a Task Contract to AI, has it run Tests and the Verification Procedure, and escalates only the Unknowns in the Evidence Packet to a Senior.

Looking only at this Work Class, the latter may reach the Outcome first.

But suppose midway a Decision appears: change an old API contract that only existing customers use. The newcomer could not see it. The eight-year Engineer knew about an incident from three years ago and a Compatibility quirk recorded in no Document. They stop the implementation there.

Watching this scene, you see the two cannot be compared on a single scale.

**Neither the newcomer nor the veteran won. The kinds of strength the two held were different.**

AI does not move every experience gap in the same direction.

### Experience Gaps That Compress Easily

To the extent AI can carry search, generation, comparison, and iteration, the following gaps can close in less time than before.

- Syntax / Boilerplate
- Library / API exploration
- Initial implementation of typical Patterns
- Test Draft / Data Draft
- Extracting Rule candidates from Documents and existing Code
- First drafts of option enumeration and comparison

These do not mean "experience is no longer needed." It is closer to say that parts that used to depend heavily on human memory volume and manual dexterity can now be externalized to AI.

### Experience That Can Rather Be Amplified

On the other hand, the following kinds of experience may gain value by using AI.

- The meaning behind Domain Vocabulary
- Constraints not written into Documents
- Trade-offs in Architecture Decisions
- Failure Patterns learned from past Incidents
- Interests and responsibility boundaries among Stakeholders
- The Risk sense that notices "this change is somehow suspicious"
- Decision experience accompanied by Accountability

Even if AI accelerates investigation and implementation, what to doubt, which Unknowns to leave, and what to have proven by Evidence grow stronger from such experience.

It is better not to assume that AI uniformly lowers the Experience Premium.

> **AI does not make experience worthless. It compresses low-value experience gaps and can amplify high-value experience.**

However, which occurs depends on Work Class, Domain Familiarity, Task ambiguity, Harness, and Model Capability.

### Treat the Experience Effect as Condition-Dependent

DeepRail does not make simple orderings like `Junior > Senior` or `Senior > Junior` a premise of the AI era.

**The Experience Effect itself changes with the kind of work and how AI is used.**

In Work where AI compresses Syntax, exploration, Drafts, and iteration, experience gaps may shrink. Meanwhile, experience in Domain, Architecture, Risk, Stakeholders, and Incident Memory can be amplified by giving AI appropriate Context, Constraints, and Evaluation.

When looking at AI effects by experience, look at least at the following conditions together.

```text
Experience Level
×
Work Class / Task Mix
×
Domain Familiarity
×
AI-Native Capability
×
Harness / Evidence Quality
×
Tool Generation
→
Observed Outcome
```

> **Do not use years as a proxy for capability. At the same time, do not use AI utilization as a proxy for capability either. Look at Outcome and Evidence.**

### Treat AI Native Entry Advantage as a "Hypothesis"

New graduates and juniors who learn work assuming AI from the start may have a smaller Cost of unlearning the conventional Operating Model. Here we call this hypothesis **AI Native Entry Advantage**. However, it is not a Maturity Level, a talent ranking, or an established Empirical Law.

Newcomers have the clear weakness of little experience. At the same time, they also have the characteristic of not being optimized for the old learning order:

```text
Humans write everything
→ Humans memorize everything
→ Humans read everything
→ After some years, become the side that delegates work
```

So from the start, there is room to raise them in this order:

```text
Define the Outcome
↓
Hold your own hypothesis
↓
Delegate the work to AI
↓
Verify with Evidence
↓
Escalate what you do not know
↓
Return failures to Rule / Test / Harness
↓
Take on a larger Outcome
```

However, this must not become a claim that basic understanding can be skipped if AI does the thinking.

> **Do not count a result you do not understand as "understood" merely because AI produced it.**

In AI Native newcomer education, do not make "can you reproduce the implementation unaided" the only test. Instead, have them explain why that Design was adopted, which Evidence could refute it, what is Unknown, and where to return to a Senior.

### Experience × AI-Native Capability Matrix

Do not place years of experience and AI Native Capability on the same axis.

| | AI Native Capability low | AI Native Capability high |
|---|---|---|
| **Domain / Technical Experience low** | Start with basic learning and small Work. Manage the Risk of swallowing AI Output whole | **Fast-ramp candidate**. Give early Outcomes through Bounded / Verifiable Work. However, connect Domain / Risk Decisions to a Mentor |
| **Domain / Technical Experience high** | Has deep knowledge, but sequential execution and sequential Review can become a Capacity Bottleneck | **Compounding Leverage**. Can externalize experience into Context / Rule / Eval / Harness and amplify it across the Team |

Do not use this Matrix for personnel Rating. Use it as a Profile for thinking about Work Allocation / Training / Mentoring.

In hiring, placement, and development too, `3+ years of experience` alone no longer reveals a person's strength.

What to look at is at least the following.

```text
Domain / Technical Experience
×
AI Delegation Capability
×
Evaluation / Evidence Capability
×
Work Class Fit
×
Context / Harness utilization ability
×
Accountability / Escalation Judgment
```

Even with the same eight years of experience, the Outcome that can be completed as a Human + AI System differs. Even with the same new graduate, the Work Class that can be delegated differs.

> **Talent evaluation in the AI era expands from "what can they do alone" to "what can they safely complete as a Human + AI System."**

### AI Native Onboarding Rule

When raising newcomers to be AI Native, do not leave them completely free from the start.

1. Give small Work with clear Acceptance that is Rollback-able.
2. AI use may be assumed, but decide Required Evidence first.
3. Have them explain `why they did it / what is unverified / what could break`.
4. Escalate High-risk Decisions such as Domain / Architecture / Security to an Experienced Mentor.
5. The Mentor not only supplies answers but externalizes tacit knowledge into Vocabulary / Rule / Decision Record / Test.
6. Widen the Delegation Envelope starting from Work Classes where Outcomes are stable.

In addition, place the following four as Guardrails in AI Native Onboarding.

```text
Explain-back
The person can explain "why that design"

Evidence Review
Verify by Test / Runtime / Artifact, not AI self-report

Escalation Judgment
Can choose where to stop and whom to return to when unsure

Agency Check
Confirm they have not handed off even their own judgment responsibility to AI
```

Do not judge someone as proficient merely because they use AI a lot. Judge by **whether they can safely be entrusted with larger Outcomes while keeping their understanding**.

The goal is not to increase people who have AI write code. It is to increase **people who can make work hold together with AI**.

And the experienced side needs the same learning.

A Senior's value is not in continuing to hold what only they know. When that experience is converted into a form the next Human and AI can use, individual experience becomes Organization Capability.

This theme starts from the recognition that "years of experience alone cannot explain Skill," and connects to AI Native Onboarding, hiring / placement / evaluation, and organizational Capability.

---

## 19.3 Learning Path by Level

```text
HC1
→ Basic operation / Data & Security / good Objectives

HC2
→ Existing System investigation / Work Contract / Tool / Test / Source of Truth

HC3
→ Acceptance / Evidence / Review Packet / Decision Packet

HC4
→ Epic decomposition / Dependency / Agent Coordination / Re-decomposition / Meeting Facilitation

HC5
→ Harness / CI/CD / Eval / Environment / Observability / Enforcement

HC6
→ Transformation / Decision Rights / Capacity / Governance / Organizational Learning
```

---

## 19.4 In Team Lead Development, Make "Being Able to Run Meetings" the Practical Skill

For team-leader proficiency, evaluate not an AI Tool demo but the following as practical skills.

- Can organize ambiguous requests in an Outcome / Intake Sync
- Can design Alignment using Mock / Prototype / Scenario
- Can evaluate AI's Work Breakdown with a Rubric
- Can decide Context / Permission / Evidence in Execution Planning
- Can turn a Daily from a status meeting into a Decision & Blocker Sync
- Can judge Architecture / Risk from a Decision Packet
- Can run Review / Acceptance centered on Evidence
- Can confirm CI/CD, Rollback, and Monitoring in Release Readiness
- Can return Human Intervention to Rule / Skill / Eval / Process in a Retro

---

## 19.5 Training Principle — Replay the History of the Harness as the Learning Order

The explanation of Harness Engineering itself is left to Ch39. What we consider here is **how to teach so that learners discover the necessity themselves**.

Having learners memorize a list of Rules, Context, Gates, and Evals from the start does not easily instill the reasons to use them. Hand them a small End-to-End assignment, and they start hitting trouble in a different order.

"I'm explaining the same thing again." "Every time the AI says it's done, I verify everything myself." "I don't want it doing this operation on its own." When that discomfort appears, introduce Rules, Evidence, and Permission.

What education should reproduce is not the Harness parts list but **the order of thinking by which you add the mechanisms you need yourself**.

> **Friction is Curriculum. — Make the friction itself the teaching material.**

There is no need to hide the answers. Create an order in which learners can connect "why this is needed now" to their own experience of being stuck.

---

## 19.6 AI Delegation Literacy — The Ability to Develop After Tool Usage

Split AI Literacy into at least two layers.

| Layer | Core ability | Typical question |
|---|---|---|
| AI Usage Literacy | Get results from AI using Prompt / Context / Tool | How should I ask |
| AI Delegation Literacy | Design Objective / Responsibility / Permission / Evidence / Evaluation / Escalation and delegate work | How far may I delegate |

The latter is closer to a Management Skill than a mere Tool Skill.

What learners should finally be able to explain is, more than Prompt technique, the following.

```text
What Humans decide
What is delegated to AI
How far AI may self-evaluate
What counts as Evidence
Where automatic GO is possible
Where to return to a Human
How to detect and recover from failure
```

---

## 19.7 Recommended Learning Format — First-Person End-to-End AI Development Lab

For AI-inexperienced to beginner learners, rather than local assignments covering only Frontend or only Backend, we recommend **small-scale business-system development that one person crosses through Frontend + Backend + DB + Test + CI**.

The aim is not to make Full-stack Engineers.
By having one Human hold multiple specialized responsibilities, sequential instruction and sequential checking quickly reach their limit, creating a state where delegation to AI and mechanization become necessary.

Example:

```text
Task / Project Management App

Frontend
- React / Next.js etc.

Backend
- Node / FastAPI etc.

DB
- PostgreSQL etc.

Delivery
- lint
- unit test
- integration test
- build
- staging equivalent

Functions
- Login / Role
- CRUD
- Status / Assignee
- Comment
- Search / Filter
```

Runtime / Model / Framework are not fixed.
What DeepRail wants to teach is not Vendor operation but Delegation Design.

---

## 19.8 Seven Questions to Have Them Write Before Starting

Before development starts, participants record at least the following.

| Viewpoint | Question |
|---|---|
| Outcome | What must finally work for this to succeed |
| Human Decision | What do you think you must judge yourself |
| Delegation Candidate | What could be delegated wholesale to AI |
| Acceptance | By what do you judge "done" |
| Evidence | What do you look at besides AI self-report |
| Risk | What do you not want AI doing on its own |
| Escalation | Under which conditions do you return to a Human |

Also draw the **Human Decision Surface** at the start.

```text
Architecture      → Human
Implementation    → AI
Review            → Human
Test Confirmation → Human
DB Change         → Human
Release           → Human
```

This becomes the Baseline for measuring change after completion.

---

## 19.9 Build Assignment Difficulty from "Operational Complexity," Not "Obscurity"

To let a Harness emerge spontaneously, do not set only difficult Algorithm problems.
That can become a contest of one-shot prompting a strong Model.

Give assignments **a structure that is hard to complete without keeping AI working continuously**.

| Assignment characteristic | Design that becomes naturally necessary |
|---|---|
| Multiple Features | Work Decomposition / Dependency |
| Front / API / DB crossing | Context / Boundary / Contract |
| Multiple Business Rules | Rule / Source of Truth |
| Ambiguous requirements | Discover / Align / Human Decision |
| Repetition of similar work | Skill / Reusable Instruction |
| Regression Risk | Test / Eval / Evidence |
| Dangerous operations | Permission / Gate |
| Environment differences | Provenance / Preflight |
| Long duration / multiple Turns | Context Management / Living Document |
| Mid-course requirement changes | Re-plan / Re-decomposition / Reinvestment |
| Failure injection | Retry / Recovery / Escalation |

> **Before instructing "build a Harness," let them experience work that is painful without one.**

However, do not let them lose time to Infrastructure malfunctions unrelated to the learning objective.
Operators run the Golden Path in advance and separate material-side Failures from learner-side Failures.

---

## 19.10 Staged Learning — Use → Delegate → Evaluate → Remove One Gate → Harness

Proceed with learning in the following order.

### Phase 0 — Baseline

Before delegating to AI, record the Human Decision Surface, Risk, Acceptance, and Evidence candidates.

### Phase 1 — Use AI

Start with small requests and experience normal AI Coding.

```text
Human Instruction
↓
AI Output
↓
Human Full Check
```

### Phase 2 — Delegate Work to AI

Per Feature, hand over Objective / Constraint / Acceptance and delegate through Plan / Implement / Test / Fix.

### Phase 3 — Have AI Evaluate Itself

Not only have AI self-report Completion; have it generate Evaluation and Evidence against Acceptance.
Compare with Human evaluation and observe False Accept / False Reject / Unknown.

### Phase 4 — Remove Just One Human Gate

Pick a low-Risk, machine-verifiable, reversible Work Class, and let it proceed without Human confirmation only when Evidence holds.

Whether they can once feel "it held even when delegated" in this Phase greatly affects subsequent learning speed.

> **Experience that "even without watching everything yourself, results hold if you design the conditions."**

### Phase 5 — Turn Friction into a Harness

Classify the Human Interventions that recurred, and return them to Rule / Context / Skill / Permission / Hook / Eval / Gate / Tool.

### Phase 6 — Inject Change / Failure Events

Inject the events described later, and see whether the Harnessed mechanisms still function under change.

---

## 19.11 Event-driven Challenge — Change the Work Midway

Do not hand over all completion requirements from the start.
Inject customer, Security, Environment, and Production-equivalent events mid-exercise.

Example:

```text
Event 1
"Please separate permissions for admins and general Users"

Event 2
"Please change the assignee from one person to multiple"

Event 3
"Only specific data returns 500 Errors on Staging"

Event 4
"Please add a search condition without breaking existing Features"

Event 5
"If you cannot explain the Migration Rollback means, Release is not allowed"
```

The purpose of events is not Surprise.

```text
Requirement Change
→ Is the Source of Truth updated

Regression
→ Do Test / Eval detect it

Environment Failure
→ Can it be separated from a Code Failure

Permission Boundary
→ Can the Agent stop / Escalate

New Feature
→ Can the Work be re-decomposed
```

That is what we observe.

---

## 19.12 Scoring — Measure "Safe Delegation" over Product Completeness

Recommended scoring example:

| Evaluation axis | Points | Main observation target |
|---|---:|---|
| Outcome / Product Quality | 25 | Satisfies requirements and actually works |
| Evidence / Quality | 20 | Can prove completion via Test / Eval / CI |
| Delegation Design | 20 | Appropriately delegates responsibility, Decision Rights, Escalation |
| Harness Design | 20 | Turns friction into mechanisms: Rule / Context / Skill / Gate etc. |
| Change / Recovery | 10 | Can re-plan and recover from requirement changes / Failures |
| Learning / Reflection | 5 | Can explain changes in Human Intervention |

Do not make the following reasons for extra points.

- Many Agents
- Few Prompts
- Heavy use of a specific Vendor's advanced features
- Only a high count of completed Features

The central evaluation is:

> **While maintaining quality and Risk, how far could they expand, with grounds, the area where Humans do not have to intervene step by step.**

---

## 19.13 Compare the Human Decision Surface Before / After

At the end, recreate the same Decision Map as at the start.

Example:

```text
Before
Architecture      → Human
Implementation    → AI
Review            → Human
Test Confirmation → Human
DB Change         → Human
Release           → Human

After
Architecture      → AI Proposal + High-Risk Human Decision
Implementation    → AI
Review            → AI Eval + Exception Review
Test Confirmation → Machine Evidence
DB Change         → AI + Migration Gate
Release           → Human
```

Simply reducing Human items is not the goal.
For every place where a Gate was removed, participants must explain the following.

```text
What was delegated
↓
Why it can be delegated
↓
What the Evidence is
↓
Can Failure be detected
↓
Can it be reverted
↓
What the Escalation condition is
```

This teaches Human Gate reduction not as intuitive AI trust but as **the design of Decision Rights**.

---

## 19.14 Final Presentation / Retro — Do Not End with "What Was Built"

The final presentation covers at least the following.

1. What was built
2. What Humans judged at first
3. Where AI usage became difficult
4. Which Harness element was born from which Friction
5. What was additionally delegated to AI
6. Which Human Gate was removed, and with what Evidence
7. What was still left to Humans, and why
8. What would be further mechanized / delegated next time

Central retrospective question:

> **By which conditions, mechanisms, and Evidence can the places Humans intervened this time be reduced next time.**

This question is the same as the Harness Retro, and connects individual learning directly to Team / Organization Learning.

---

## 19.15 Operator Responsibilities — Design the "Discovery"

Operators behave less as lecturers than as Learning Environment Designers.

- Run the Golden Path End-to-End in advance
- Promptly remove Environment failures unrelated to the learning objective
- For learning-purpose Friction, do not teach the answer immediately; let them observe
- Have them record Human Intervention counts and reasons
- Inject midway events as a consistent Scenario
- When a Gate is reduced, confirm Evidence / Risk / Reversibility
- Have them record AI / Human evaluation differences
- Have them verbalize reusable principles, not Tool-specific tricks

The success condition of the education is not that everyone builds the same Harness.

> **That participants themselves can explain "why the mechanism became necessary" and succeed at safe Delegation once.**

---

## 19.16 Returning to Organizational Capability

Do not close education at individual participant proficiency.

```text
Training / Delegation Lab
↓
Observed Friction / Human Intervention
↓
Root Cause
├ Individual Skill
├ Team Operating Model
├ Harness
├ CI / Eval
├ Standard
└ Organization Constraint
↓
Improvement Backlog
↓
Re-inject into next Training / Project
```

Education is part of DeepRail's Organizational Learning Loop.

### 19.16.1 Why — Why Are Individual AI Use and Organization Capability Different Things?

There is one person who can use AI incredibly well.

That person investigates fast. Implements fast. Has personal Prompts and Scripts, and is good at delegating to Agents. When a hard Task arrives, everyone relies on them.

At a glance, AI-Native adoption seems to be advancing.

But when that person rests, work stops. When they move to another Team, the way of working disappears with them. Newcomers cannot reproduce it. The Security officer does not know what is permitted. The Manager cannot judge whether results come from personal Skill or from the mechanism.

This is a strong individual, not yet a strong Organization.

```text
An individual can do it
↓
Can explain the method
↓
Necessary Context / Rule / Evidence is externalized
↓
Another person or AI can reproduce it
↓
Enters the Team's normal Flow
↓
Is measured and maintained
↓
Holds even when moved to another Team
```

Only at this point does it approach organizational capability.

Suppose in FlowDesk only one Engineer could build the proxy-approval Feature fast with AI. That person's Local environment has convenient Scripts, their head holds Domain Rules, and they know the Review pressure points. Looking only at the deliverable, it is a success.

But tell the next Team "do the same with AI" and it does not reproduce. The conditions that produced the success remain inside that person.

What is needed then is not distributing their Prompts to everyone. What was delegated. Which Context was needed. Which Failures occurred. By what was correctness confirmed. Which judgments were left to Humans. Which Control prevented recurrence.

Extract these and convert them into Work Design, Training, Harness, and Standard. Only here does individual success become a company asset.

Conversely, over-standardizing also breaks it. Fix an excellent person's procedure word for word and force everyone onto the same Tool, same Prompt, same Agent setup, and it will not work in Teams with different Context.

What should be rolled out horizontally is not the completed work procedure. **It is the principles that produced reproducibility, and the Artifacts each Team can reconstruct in its own Context.**

```text
Individual Practice
↓
Observed Friction / Success
↓
Extract Principle / Context / Evidence
↓
Convert into Standard / Harness / Training
↓
Re-run in another Team
↓
Learn the differences
↺
```

High Tool utilization and many Prompt-training attendees do not by themselves prove Organization Capability. What to look at is whether the same kind of work can be safely delegated, evaluated, and improved even without any one person's skill.

> **Individual AI use creates speed. Organization capability creates a state where that speed reproduces even when the person changes.**

This difference is why DeepRail does not end education at "more people who can use the Tool."

### 19.16.2 Turn Individual Skill into Team Reproducibility

Do not close the education outcome at "participants could use the Tool." Include the following Transfer in the learning design.

```text
Individual Practice
Use AI / delegate to AI
        ↓
Real Theme Team Practice
Handle a near-real Theme as a Team
        ↓
Shared Reality / Context Assets
Align understanding, externalize specs, vocabulary, constraints, decision reasons
        ↓
Reproducibility
Another member reproduces the same work
        ↓
Standard / Harness / Training
Convert into reusable mechanisms
        ↓
Organization Rollout
Deploy to other Teams
```

The reason for handling a real Theme is not "build production code in Training." Real Themes surface **implicit assumptions, perception gaps per Role, Decision Owners, and Context Gaps** that fictional assignments tend to hide.

In Team Training, involve Business / Product / Decision Owner as needed and align the following.

- Problem / Outcome
- Assumptions and constraints
- Domain Vocabulary
- Human / AI roles
- Decision Owner
- Acceptance / Evidence
- The next small Scope to try

However, do not treat this single case as proving DeepRail's `Delegation / Evaluation / Harness / Organizational Capability` as a whole. **Treat it as a limited practical example concerning Team Practice / Context Asset / Adoption**, and distinguish the Standardization / Harness / Organization Learning beyond it as DeepRail's own design.

## 19.17 The Golden Path Is Not a "Model Answer" but a Failure-Separation Device

Operators run the assignment End-to-End in advance and hold a Golden Path.

The purpose is not to show participants the answer.

It is to separate:

```text
Material-side Failure
Harness-side Failure
Environment-side Failure
Participant's Delegation / Judgment Failure
```

Re-run the Golden Path itself when the Harness / Runtime is updated, and do not keep stale success examples as teaching material.

## 19.18 Do Not Detach Teaching Material Too Far from Operational Assets

Mass-duplicating education-only Rules / Skills / Manuals creates a new maintenance job: Drift between operational assets and teaching material.

Recommended structure:

```text
Operational Rule / Skill / Decision Record / Eval
        ↓ reference
Training Scenario / Exercise
```

Reuse operational assets themselves as teaching material, and let the education scenario define "what to read" and "what to experience."

Also, change the education evaluation function by organizational maturity.

```text
Exploration
→ Were good Failures discovered and returned to the Harness

Team Adoption
→ Could it be reproduced by another member / another environment

Standardization+
→ Can Delegation / Evaluation / Enforcement be operated reproducibly
```

> **In early learning, the occurrence of Failure itself is not failure. Hiding Failure and completing the run is the failure.**

## 19.19 Separate Human Capability from Delegation Qualification

`HC0–HC6` is a growth learning Profile. On the other hand, whether Decision Rights can be delegated in real engagements is judged by the OC-4 qualifications `H-1 / H-2 / H-3`.

```text
HC = what has been learned, which abilities are held
H- = can this person be a delegator / judge in this Operating Context
```

Being good at Tool operation alone does not make someone H-3. For H-3, confirm at least Failure Routing, Evidence evaluation, Delegation Scope, and Stop / Escalation judgment through practical work.

# Part E. Governance / Quality / Production
