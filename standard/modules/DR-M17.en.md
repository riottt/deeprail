# DR-M17 — Quality Evaluation and Harness Evals Guide

> Status: **preview v0.16.8**> Creator / Lead Author: **riottt**

## 21.-1 Trust Architecture — Decomposing "Trusting AI"

Think of DeepRail's trust mechanism in four layers.

```text
1. Principle
   What to believe
   → Evidence, not Executor Self-report

2. Evaluation Design
   How to judge
   → Acceptance / Evidence Level / Independent Evaluation / EA

3. Enforcement
   Who stops it
   → CI / Hook / Checker / Permission / Human Gate

4. Meta-Health
   Is the mechanism itself alive
   → fixture / doctor / audit / telemetry health
```

> **Do not trust AI. Trust the evaluation mechanism — and trust, through Evidence, that the evaluation mechanism is operating normally.**

## 21.0 Evidence Discipline

Separate "the executing agent's self-report" from "completion evidence."

| Grade | Name | Content | Treatment |
|---|---|---|---|
| EV-3 | Observed-behavior evidence | Real-environment logs, read-back, screenshots, recordings, observed results | Primary completion basis for user-visible changes |
| EV-2 | Machine-check evidence | lint, typecheck, UT, CI, coverage, schema/checker passes | Auxiliary evidence. Does not alone guarantee real behavior |
| EV-1 | Self-report | "I implemented it," "tests passed," etc. | Not evidence. Breaking news / reference information |

Do not accept the following as a completion basis.

- A green summary with 0 executed items
- Treating only mocks as real-environment evidence
- Counting skipped Tests as passes
- Using a capture that includes an error state as success evidence
- Advancing on the AI's own "it is done" report alone

The evaluator re-runs and re-observes where possible, and separates the generation Context from the evaluation Context.

## 21.0-A Evaluation Functions by Maturity

Do not apply the same KPI to every organization.

```text
M0 Exploration
→ Learning volume, problem extraction, Failure classification, discovery of unknowns

M1 Controlled Adoption
→ Reproducibility, standard compliance, Human Intervention, retries

M2 Standardization
→ Flow Metrics, Enforcement Coverage, Quality, Rework

M3 Scaled Adoption
→ Multi-team Lead Time, Review Capacity, operating cost, Risk

M4 Continuous Optimization
→ Business Outcome, Portfolio optimization, Capability improvement
```

Do not fill unmeasurable values with guesses. Mark unmeasured values as `null`, and building the required measurement foundation itself can be a maturity promotion condition.

## 21.1 Give the Harness Tests Too

Just as code changes have Regression Tests, Harness changes have standard assignments.

---

## 21.2 Evaluation Metrics

- Task Success Rate
- Build Success
- Test Success
- Review comment count
- Rule violations
- Human Intervention
- Retry count
- Lead Time
- Human Time
- Token
- Cost
- Reinvest / Learn omissions
- Security Violation
- PR/MR rework
- Reopen rate

Furthermore, evaluate the Flow of the entire SDLC, not the Harness alone.

### Flow Metrics by Stage

- Requirement Lead Time
- Design Lead Time
- Build Lead Time
- Review Lead Time
- Test Lead Time
- Release Lead Time
- Maintain/Incident Resolution Time
- Queue Time
- WIP
- Blocked Time
- Human Wait Time
- External Dependency Wait Time

### Reviewability Metrics

- Review Time / PR
- Human Review Minutes
- Change volume per PR/MR
- High-risk Diff volume Humans should check
- Review Queue Length
- Review Rework rate
- Spec Surprise count
- Un-agreed Decision discovery count
- Requirement re-confirmation count during Review
- Count of Humans reverse-engineering intent from Code
- Review Packet omission rate

Even if Build time shrinks, if the Review Queue is growing, do not conclude the Harness as a whole improved.

If "why this design" is being discussed for the first time in the review stage, classify the Failure as an upstream Grill/Spec process shortage.

---

## 21.3 Comparing Harness Effects

Example:

| Condition | Quality | Time | Token | Human |
|---|---:|---:|---:|---:|
| High Model + no Harness | measure | measure | measure | measure |
| High Model + Harness | measure | measure | measure | measure |
| Light Model + Harness | measure | measure | measure | measure |

Confirm "works even with a lightweight model" by experiment.

---

## 21.4 Harness Change Gate

```text
Harness Change
↓
Eval Suite
↓
Baseline comparison
↓
Quality degraded?
├ Yes → Reject / Fix
└ No  → Review
        ↓
       Merge
```

---

## 21.X Human Evaluation Interface

This is the Canonical Home of the Human Review / Evidence Interface. Earlier sections dealt only with the symptom that "the Review Queue clogs"; here we design the decision Interface in earnest for the first time.

When AI asks a human for a judgment, it must not hand over Raw Artifacts as-is.

The form for passing judgment material to a Human Gate is called the **Human Evaluation Interface**.

Basic principle:

> **AI does not hand humans artifacts; it hands them decisions.**

When requesting human judgment, AI presents at least the following.

```text
Decision
Recommendation
Reason
Options
Evidence
Risk
Unknown
Reversibility
Requested Action
```

### Human Attention Principle

Human Attention is a finite organizational resource.

AI deliverable quality includes not only Correctness / Security / Maintainability but also
**Human Reviewability**.

If a human cannot quickly judge

```text
what to decide
why it needs deciding
what AI recommends
what is proven
what is unconfirmed
what the Risk is
whether it can be reverted
```

then the Human Evaluation Interface quality is considered low.

### 21.X.0.1 Why — Why Can Human Review Become the New Bottleneck?

Implementation got faster with AI.

And yet, development as a whole does not get as fast as expected.

This can happen. The reason is simple: **the design where a human reads everything at the end remains as-is.**

Consider FlowDesk's proxy approval. Frontend, Backend, permission judgment, audit Log, Test. If the work can be divided into independent units, AI can advance multiple changes in parallel. Deliverables awaiting Review line up in less time than before.

So far, as intended.

The problem is what comes next.

A human Reviewer opens each Diff one by one. Hunts the change reason from the Issue. Re-reads the specification. Looks at Test results. Considers the impact on permissions. Replays combinations with other changes in their head. If unclear, asks the Agent.

One is readable.

When several arrive at once, it suddenly gets heavy.

AI-side execution capacity grew, but if only the final evaluation method remains "a human re-reads the Raw Artifact from the top," the constraint moves to the Review side. AI is not slow. **The place that clogs simply moved to after the stage that got faster.**

Here, making only "reduce Review" the goal is dangerous.

Humans looking is not itself bad. The problem is that what to look at is decided inside each Reviewer's head every time.

For work like Security-related changes, Data Migration, hard-to-reverse Architecture changes, and hard-to-detect Failures, the meaning of humans directly reading Code and Diffs remains. Zero Human Review is not the goal.

Still, not every change needs to require the same depth of checking.

For example, in FlowDesk, suppose you want to confirm that "the original Approver ID is recorded in the Audit Log during proxy approval." Rather than a human starting to search a huge Diff, judgment is faster looking first at Acceptance, the Verification performed, the actual Log, and the remaining Unknowns. If needed, descend to the Code from there.

Change the order.

```text
Read all Raw Artifacts
↓
Reconstruct intent and Risk in your head
↓
Judge
```

becomes:

```text
See what to judge
↓
Confirm with Evidence
↓
Look at Risk / Unknown
↓
Descend to Raw Artifacts only where needed
```

What supports this order is the Human Evaluation Interface. Decision Packets and Review Packets do not hide information. They point human Attention first at the places where judgment is needed.

The more AI produces at scale, the bigger this difference becomes.

It is not a matter of "add one implementer, add reviewers the same way." Reviewers may need scarce Context like Domain understanding, Architecture, Security, and Production circumstances. Adding headcount does not always replicate the same judgment ability quickly.

If adding people cannot solve it, the only option is to reorganize the Review work itself.

- What can be dropped earlier by Machine Check
- Can AI's first-pass evaluation be calibrated in Shadow
- What Evidence is needed per Work Class
- Which Failures should humans see directly
- Where can we move to Sampling
- Which Decisions should still remain at a Human Gate

Only with all of this in place can AI's speed finally be absorbed across the whole Delivery.

And the Review work itself changes too.

At first, look at Artifacts. Next, look at Decisions and Evidence. As the evaluation system matures further, look at Exceptions and high-Risk Decisions. In the end, the weight shifts toward reviewing the Evaluation Function and Risk Policy themselves rather than individual changes.

Human Review does not disappear soon.

What changes first is **what is looked at**.

Back to the FlowDesk scene. Multiple deliverables are lined up awaiting Review. What is needed here is not to hurry the humans. It is to rebuild the job of reading everything into a job that can judge without reading everything.

> **A mechanism in which people see everything cannot exceed human speed. What AI-Native adoption should change is not only generation speed, but what a human finally looks at to issue GO.**

### 21.X.0.2 Why — Why Treat Evidence as an Interface?

The AI said "it's done."

That single phrase contains almost no information.

There may be Code. Tests may even be passing. But what the deciding side really wants to know is not only "what was made." **On what grounds can we say this change may proceed.**

Take FlowDesk's proxy approval as an example. The Agent finished implementation and created a Pull Request. The change is 1,200 lines. If a human reads the whole Diff, they will understand the implementation to a degree.

Still, questions remain that reading alone cannot easily answer. Is a User whose proxy period expired really rejected? For high-value applications, is the Compliance Approver not skipped? Does the Audit Log retain both the original Approver and the Proxy Approver? Is compatibility with existing Clients preserved?

Code is an Artifact. Judgment needs a form one level different.

So make Evidence the entrance to judgment.

There is a reason Evidence is called an Interface. Appended material attached at the end is not enough. We want to pass verification results in a form the side making the next Decision can use as-is.

```text
Intent / Acceptance
↓
Verification
↓
Observed Result
↓
Evidence
↓
Decision
```

For example, for an Acceptance like "an expired proxy cannot approve," what is wanted is not the Agent's explanation. It is the result of actually operating under the expired condition and being rejected, the Log at that time, the Environment used, and the unconfirmed conditions.

In this form, not only humans but also another AI Evaluator can read it. The next stage's Gate can use it. A later Audit can trace it. If re-runnable, it can be re-verified after conditions change.

The value of reading Code remains. For judgments like Architecture, Security, and Maintainability, the Raw Artifact itself should be seen. When needed, descend that far.

However, if every Decision is settled "inside the head of the person who read all the Code," that judgment is hard to reuse. What was confirmed and why it was OK stays closed inside the individual Reviewer.

Making Evidence an Interface brings the judgment material outside.

```text
Not "I read it and it seems fine," but

what was confirmed
what was observed
what is still unknown
which Risk remains
```

can be shared.

If Evidence is weak, do not widen Decision Rights. If Evidence is strong enough, Failure can be detected, and it is reproducible, part of the judgment can move to AI Evaluation.

Making Evidence the last Documentation is too slow. Place it in the middle — after work is delegated and before its result is trusted enough to proceed.

> **Code is a deliverable. Evidence is the Interface for deciding whether that deliverable may proceed.**

Even when FlowDesk produces a 1,200-line Diff, what should be seen first is not necessarily 1,200 lines. What should be seen first is the basis for saying "proxy approval holds correctly."

---

## 21.X.1 Decision Packet

Do not close the Review Packet as a PR/MR-only deliverable.
Its generalization to Human Decisions in general is the **Decision Packet**.

```markdown
# Decision Packet

## 1. Decision Required
What you want the human to decide this time

## 2. Recommendation
AI's recommended option

## 3. Why Human Decision Is Required
Why it exceeds the delegation scope

## 4. Outcome Impact
How this decision affects the Outcome

## 5. Options
Choices
- Option A
- Option B
- Option C

## 6. Evidence
EV-3 Observed Behavior
EV-2 Machine Check
Other grounds

## 7. Risk
Risk Class / Failure Mode / Blast Radius

## 8. Unknowns
Unconfirmed matters / uncertainty

## 9. Reversibility
Rollback feasibility / Cost / Time

## 10. Requested Action
Approve / Reject / Request Change / Defer / Escalate
```

AI does not throw a bare "please confirm" at a Human.

### 21.X.1.1 Delegation Decision Trail

For long-duration, multi-Phase, unattended execution, make not only the final Decision Packet but also the path of important decisions traceable.
Do not assume a Human reads the full Transcript.

A Decision Trail has at least the following.

```text
ts / phase
Decision
Rationale
Evidence Pointer
Result
Deviation / Pivot
Unknown / Open Risk
```

Principles:

1. **Record only important decision points** — do not record every Tool Call or the entire reasoning process.
2. **Prefer Pointers for Evidence** — make it traceable to Commit / Test Result / Trace / Screenshot / Artifact etc.
3. **Append-only as the base** — decision changes do not rewrite the past; add a new Entry as Supersede / Revert.
4. **Keep the Result** — record what happened after the decision: `accepted / reverted / inconclusive / open` etc.
5. **Compress at Handoff** — summarize Outcome / Important Decisions / Evidence / Deviations / Unknowns into a Decision Packet for the Human.

```text
Autonomous Execution
↓
Decision Trail
↓
Outcome + Evidence + Important Decisions
↓
Decision Packet / Review Packet
↓
Human / Policy Decision
```

A Decision Trail is not a verbatim log for surveillance; it is **an Audit / Review Interface for reconstructing later "why this Outcome resulted."**

---

## 21.X.2 Progressive Disclosure

Presentation to humans basically follows this order:

```text
Level 0
Decision only

↓ Drill-down

Level 1
Summary
Intent / Recommendation / Risk / Evidence / Unknown

↓ Drill-down

Level 2
Evidence
Acceptance Criteria / Test / Decision / Traceability

↓ Drill-down

Level 3
Raw Artifact
Spec / Design / Diff / Code / Log / Trace
```

Do not make people read a huge Diff or Raw Log from the start.
Create a state where only those who need to can dig deeper.

This order is not for hiding information. It lets a Human first understand "the decision to approve," trace only the Evidence needed for that decision, and descend to Code when necessary.

**Code / Diff can be important Raw Evidence at Level 3, but it is not the default entrance to Human Review.**

---

## 21.X.3 Management View by Work Level

Do not show the same information to every Role.

| Work Level | What humans mainly evaluate |
|---|---|
| Portfolio | Investment / Strategic Fit / Outcome / Risk |
| Epic | Outcome / Scope / Owner / Dependency / Risk |
| Feature | Capability / Acceptance / Boundary |
| Issue | Intent / Acceptance / Evidence / Exception |
| PR / MR | Decision / High-risk Diff / Automated Evidence |
| Release | Release Scope / Residual Risk / Rollback |
| Transformation | Constraint / Approval / Adoption / Outcome |

AI changes the View according to the recipient's Role and Decision Rights.

---

## 21.X.4 Evaluation Maturity

What humans evaluate changes with maturity and Autonomy.

```text
Stage 1
Human reviews Artifact

Stage 2
Human reviews Decision + Evidence

Stage 3
AI evaluates Artifact
Human reviews Exception / High-risk Decision

Stage 4
Human defines Evaluation Function
AI executes + evaluates + retries

Stage 5
Human reviews
Outcome / Risk / Investment / Exception
```

Even in the final state, Human Review does not reach zero.

The abstraction level of Review rises.

Note: do not measure maturity by "the percentage of Code Humans stopped looking at." What is evaluated is whether, for the target Work Class, the required Failure Modes are detectable, Approved Evidence holds, and Decision Rights can be safely delegated according to Risk.

---

## 21.X.5 Evaluation Authority — How Far to Give AI Evaluation GO Authority

Do not design the Human / AI evaluation split by ratios like "human 30%, AI 70%."
Evaluation authority is defined **per Work Class / Decision Class**.

Evaluation Authority is expressed as `EA0–EA4`.

| Level | Name | AI evaluation authority | Human involvement |
|---|---|---|---|
| EA0 | Human Evaluation | AI evaluation is not used as Gate basis | Human evaluates and issues GO |
| EA1 | Shadow Evaluation | AI also evaluates in parallel but has no GO authority | Human judges every case. Differences are used for Calibration |
| EA2 | AI-First / Human Decision | AI evaluation is adopted as first-pass | Human issues final GO from Decision Packet / Evidence |
| EA3 | Audited Autonomy | AI can evaluate and issue GO in defined Work Classes | Human handles Exception / Sampling / Audit |
| EA4 | Policy-Governed Autonomy | AI performs evaluation, GO, and Retry within Policy | Human manages Evaluation Function / Risk Appetite / Policy / Exception |

`EA` is a separate axis from both AI Execution Autonomy `A0–A5` and Approval Strength `S1–S5`.

```text
A  = what AI can execute
EA = what AI can evaluate and issue GO on
S  = in what strength and form approval holds
```

Examples:

```text
A3 × EA1 × S4
AI advances execution inside a Feature
AI evaluation is recorded as Shadow
Final GO is approved by a human on an asynchronous ledger

A3 × EA3 × S1
Execution and evaluation inside a Feature are delegated to AI in a defined scope
Humans audit Sampling / Exception
AI records approval based on the delegation rules
```

AI being highly capable is not itself an EA promotion condition.
Require that, for the target Work Class, the necessary Evidence, Failure detection, Rollback, and Audit hold.

---

## 21.X.6 Introduction Procedure for Evaluation Delegation

Trust in AI evaluation is built not from explanations or demos but from **comparative track records**.

### Step 0: Fix the Work Class and Evaluation Contract

```text
Target Work Class
Acceptance Criteria
Evaluation Criteria
Required Evidence
Risk Class
Failure Detectability
Reversibility
Accountability Owner
```

Narrow the target rather than asking "can AI in general be trusted."

### Step 1: Shadow Evaluation

Human and AI evaluate the same target independently. AI's judgment does not yet affect the Gate.

```text
AI  : GO / NG / UNKNOWN + Evidence
Human: GO / NG / UNKNOWN + Reason
```

### Step 2: Classify Disagreements

Do not simply fix the Human as correct.

```text
AI Error
Human Error
Ambiguous Criteria
Missing Evidence
Environment Mismatch
Requirement / Spec Drift
Unknown / Unclassifiable
```

Judgment variance between humans is also a Calibration target.

### Step 3: Accumulate Calibration Evidence

Observe at least the following.

```text
True Accept
True Reject
False Accept   # AI issued GO but it was actually NG. Most important
False Reject
Unknown Rate
Human Override Rate
Missing Evidence Rate
Escaped Defect
Rollback / Incident
```

No common promotion threshold is specified across all domains. The organization defines Exit Criteria according to Risk Appetite and Work Class.

### Step 4: Bounded Delegation

Raise EA **only for the bounded Work Classes** where sufficient Evidence was obtained.

```text
EA1 → EA2
AI does first-pass evaluation
Human confirms mainly Decision / Evidence

EA2 → EA3
AI issues normal GO
Human moves to Exception / Sampling / Audit
```

### Step 5: Audit / Drift Monitoring

Do not fix things after delegation either.

- Model changes
- Prompt / Context / Harness changes
- Test changes
- Environment changes
- Domain changes
- Failure Pattern changes

If any occur, re-Calibrate.

### Step 6: Expand or Roll Back

If quality is maintained, expand to adjacent Work Classes.
If False Accepts, serious Incidents, Evidence gaps, or Eval Drift increase, lower EA back.

> **Evaluation Authority is not a maturity badge; it is an operating Profile raised and lowered per target domain.**

---

## 21.X.7 Independent Evaluation Contract

Before raising Evaluation Authority, design the evaluation system itself.

### Generation / Evaluation Separation

Do not raise EA on the implementing agent's self-evaluation alone.

```text
Executor
  ↓ Artifact + minimal provenance
Evaluator: Standards axis
Evaluator: Specification axis
  ↓
Independent Evidence
```

Recommended principles:

1. **fresh context** — do not pass the long implementation conversation history straight to evaluation.
2. **axis separation** — evaluate Standards and Specification on separate axes.
3. **AND semantics** — a pass on one axis does not offset a fail on the other.
4. **positive context list** — limit the case-specific Context given to evaluators to canonical sources such as GLOSSARY / ADR / Contract.
5. **disagreement escalation** — do not close disagreement between independent Evaluators by majority vote alone; make it an Unknown / Human Decision candidate.

### Failure-Mode Independence / Evaluator Diversity

Evaluator Independence is not judged only by the form of "another Agent," "another Model," or "another Prompt."
If they share the same wrong Specification, the same Context Gap, the same Model Family, or the same unobservable points, multiple Evaluators may make the same wrong judgment.

Confirm independence from the following viewpoints.

```text
Evaluation Axis Diversity
→ Specification / Standards / Security / Runtime / UX / Policy

Evidence Source Diversity
→ Test / Static Analysis / Runtime Observation / Trace / External Source

Context Independence
→ Do not over-depend on the Executor's conversation history or self-explanation

Model / Method Diversity
→ Combine different Models / Algorithms / Human Judgment only when needed

Failure Correlation
→ Evaluate the possibility of missing the same Failure Mode simultaneously
```

```text
Multiple Evaluators agree
→ High-signal candidate
→ Not necessarily Truth

Evaluators disagree
→ Reconfirm Criteria / Context / Unknown / Environment
→ If needed, Human / Domain Decision
```

Majority vote is not a substitute for Independent Evaluation.
The goal is not to increase Evaluator count but **to lower the correlation of missing an important Failure at the same time**.

For low-Risk Work Classes where Deterministic Checks suffice, multi-system evaluation may be omitted. The cost of independence itself is also adjusted by Risk.

## 21.X.8 Evaluator Re-execution Principle

Make the basis for pass/fail, where possible, **observations the judge re-ran or re-acquired themselves**.

```text
Usable as grounds
→ Evaluator's own test / query / read-back / observation

Reference information
→ Executor's explanation
→ Logs pasted by the Executor
→ Executor's "tested" self-report
```

For Write-type operations, include read-back in the completion conditions. For destructive or irreversible operations, do not re-execute; substitute read-back / immutable log / environment evidence.

### 21.X.8.1 Reproducible Evidence Principle

Do not confuse Evidence Strength with Reproducibility.
Even EV-3 Observed Behavior may be reproducible only once. On the other hand, a low-Risk Machine Check can be re-run easily.

Where possible, link the following to Evidence.

```text
What was verified
Verification Procedure
Input / Preconditions
Environment / Version / Provenance
Observed Result
Evidence Location
Cleanup / Side Effect
Re-run Constraint
```

When the actual User Path / Runtime Behavior / External Effect can be verified, do not replace the Verification Procedure with only a Proxy.
Also run the generated Verification Script / Skill / Checker itself at least once to confirm it holds.

```text
Executor Self Report
→ weak grounds

Snapshot / Log / Screenshot
→ observed Evidence

Re-runnable Test / Checker / Script / Eval
→ re-confirmable Evidence

Integrated into CI / Hook / Gate
→ an Evidence System that is continuously re-evaluated
```

However, do not treat Machine Re-execution as omnipotent. For Domain Judgment / Security Exception / Legal / Irreversible Operation etc., keep Human Decision or Immutable Evidence, and choose the optimal Evidence Contract per Work Class.

## 21.X.9 Evaluator Permission Isolation

Make the evaluating agent Read-only on the Tool side where possible.

```text
Evaluator
Read   ✓
Test   ✓ (non-destructive)
Write  ✗
Merge  ✗
Release ✗
```

If it is only written in the Prompt "do not change anything," it is not considered enforced; mark it `declared_only` in the Enforcement Ledger.

If automatic fixing is needed, separate the Evaluator and the Fixer into different systems.

## 21.X.10 Human Gate Quality

The success condition of a Human Gate is not

```text
a human opened the screen
a human pressed Approve
```

Evaluate by whether the following are satisfied.

```text
The Decision target is clear
Necessary Evidence is complete
Risk is disclosed
Unknowns are not hidden
Alternatives are comparable
The human holds Decision Rights
The judgment is Traceable
```

If Approval remains only in form, do not count it as a Gate being present. See it as a Failure.

---
