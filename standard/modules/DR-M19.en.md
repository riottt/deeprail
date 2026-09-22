# DR-M19 — AI Authority Delegation and Autonomy Operations Guide

> Status: **preview v0.16.8**> Creator / Lead Author: **riottt**

This chapter defines the long-term destination of AI-driven team development.

---

## 23.1 Autonomy Levels

| Level | Main human involvement | AI scope |
|---|---|---|
| A0 | Constant supervision, decomposition-plan confirmation | Proposals, investigation, Work decomposition plans |
| A1 | Approval of each STEP / Issue structure | Investigation, design proposals, implementation, Test |
| A2 | Issue start/end | In-Issue Lifecycle + autonomous Task / Agent Task decomposition |
| A3 | Feature start/end | Feature→Issue decomposition / re-decomposition, parallel Agents, PR |
| A4 | Epic Outcome / Risk / Exception | Epic→Feature / Issue decomposition, Feature-group execution, canonical updates |
| A5 | Strategy / Portfolio / Investment | Initiative→Epic candidates, continuous execution and improvement of routine domains |

Work Decomposition autonomy follows the DR-M07 Rubric.

That AI can decompose work is not synonymous with AI being free to change the Objective or Business Decisions.

```text
AI can decompose the work
≠
AI can redefine the goal
```

As Autonomy rises, move human Review targets from lower-level Tasks to higher-level Outcome / Risk / Decision.

---

## 23.2 How to Reduce Human Gates

A Human Gate is not a binary of "present / absent."
Manage autonomy Level A0–A5 and each Gate's **Approval Strength S1–S5** separately.

| Strength | Form | Definition |
|---|---|---|
| S5 | Face-to-face synchronous approval | A human confirms the deliverable and approves on the spot |
| S4 | Asynchronous ledger approval | A human confirms asynchronously and records it in the approval ledger |
| S3 | Asynchronous relay approval | A human judges and AI transcribes it to the canonical ledger; the judgment record and transcription can be cross-checked |
| S2 | Delegated completion judgment | Judgment delegated to a named human based on predefined criteria |
| S1 | AI proxy approval | AI records approval based on explicit delegation rules |

When using S1/S2, the delegation rules hold at least the following.

```yaml
delegation:
  scope:      # target stages, Gates, Work Items
  expiry:     # deadline or expiry conditions
  audit:      # who confirms afterward, at what frequency
  disclosure: # to whom and when proxy/delegation results are disclosed
```

Approval is valid only for confirmation that specifies the target operation.
Do not reuse approval given to an old deliverable for a new version.

Do not reduce Gates by feel.

Before reducing a Human Gate, calibrate the evaluation authority of the target Work Class with DR-M17's Evaluation Authority `EA0–EA4`.

```text
Bound the Work Class
↓
EA1 Shadow Evaluation
Measure Human / AI judgment differences
↓
Improve Evaluation Criteria / Evidence
↓
EA2 AI-First + Human Decision
↓
For a period, measure False Accept / Escaped Defect / Override
↓
EA3 Audited Autonomy
Humans move to Sampling / Exception
↓
Once Policy and Risk Appetite are stable
↓
Consider EA4 Policy-Governed Autonomy
```

The purpose of reducing Human Gates is not "to reduce humans to zero."
**It is to concentrate human Attention on ambiguity, significant Risk, irreversible Decisions, and legal/organizational Accountability.**

Also, do not confuse Autonomy / Evaluation Authority / Approval Strength.

```text
Execution Autonomy A0–A5
×
Evaluation Authority EA0–EA4
×
Approval Strength S1–S5
```

Even at the same A3, a Profile where a Team with little evaluation track record stays at EA1 while a Team with sufficient Calibration Evidence is at EA3 is valid.

### 23.2.0 The Agent Evaluating a Gate Can Move in Stages

When reducing a Human Gate, you do not have to remove the Step or Control Point with it.

What changes is who collects the Evidence, who evaluates, and who establishes GO.

```text
Initial
AI Generate / Execute
↓
Human Review
↓
Human Approve

        ↓ Calibration

AI-First
Generation Agent
↓
Review Agent / Automated Eval
↓
Human Decision

        ↓ Bounded Delegation

Audited Autonomy
Agent Execution
↓
Independent Evaluation
↓
AI issues GO for normal Cases
└─ Exception / Sampling → Human

        ↓ Policy Stabilization

Policy-Governed Autonomy
Multi-Agent / Agent Execution
↓
Automated Evaluation
↓
Policy Gate
├─ PASS → proceed to next stage automatically
├─ RETRY → re-execute within defined scope
└─ EXCEPTION → Human Intervention
```

In this transition, human involvement does not simply "decrease."
The weight shifts from sequential Artifact confirmation to Evaluation Function, Risk Appetite, Policy, significant exceptions, and audit.

**We are not eliminating the Human Gate. We are changing the Evidence that makes the Gate hold and the agent that judges it.**

### 23.2.1 Why — Why Can "Not Checking Everything" Be Safer?

"Everything AI makes, a human checks all of it."

At first, this rule looks safest. When you have just adopted an unknown Tool, that is actually fine. Making the Human Gate thick while you do not know how it fails is natural.

The problem is not changing that rule after maturing.

In FlowDesk, if AI makes only two small changes a day, a person can read all of them. What happens when it becomes ten, twenty, fifty? The Reviewer sees more Diffs, Tests, Logs, and Specifications in the same time.

At that point, the fact of "checking everything" and the fact of "being able to judge everything sufficiently" do not coincide. The Queue grows. Review gets shallow. Everything is seen at the same depth regardless of importance. In the end, approval becomes a formality.

The Gate remains. Safety has dropped.

Saying "do not check everything" does not mean checking sloppily. **It means dividing checks toward the places where each Failure is easiest to find.**

Lint watches format violations. The Compiler watches type mismatches. Tests watch known Regressions. The Verification Procedure watches proxy-period Boundaries. Permission stops Production Writes.

On top of that, humans watch ambiguous Requirements, legal Accountability, irreversible Data Migration, and Risk Appetite changes.

```text
Machine-detectable Failure → Machine Check
Reproducible Behavior → Verification / Eval
High-risk / Ambiguous Decision → Human
Unknown → Escalation
```

This way, human Attention is not spread thin over everything but kept for the places that truly need judgment.

Measured by Gate count alone, it looks reduced. Still, the kinds of Failure that can be detected can be increased.

Instead of a human searching the Code for FlowDesk's Audit Log every time, actually execute a proxy approval and mechanically verify that the original Approver ID and Proxy Approver ID are recorded. If this Check is stable, the human can spend Attention on the validity of the Compliance Rule itself.

Of course, do not blindly trust Machine Checks. A Test itself can be wrong. Evaluators can share the same misunderstanding. That is why Shadow Evaluation, False Accept, Escaped Defect, Evaluator Independence, and Sampling are needed.

A design that does not show humans everything is actually harder.

If you reduce Human Review without building the conditions, you have merely stopped looking. Only when Machine Check, Evidence, and Escalation are all in place can you say the Control location moved.

> **Safety is not the amount a human saw. It is a state where the necessary Failures are detected by the appropriate mechanisms.**

In a mature AI Native System, it shifts from "safe because a human saw everything" to "safe because what is detected by whom and how is designed."

---

## 23.2-A Decision Rights Delegation Protocol

This is the Operational Home of Decision Rights. After understanding "who decides" in Ch10, here we concretize how that judgment moves between Human / AI.

When shrinking a Human Gate, do not record only "removed a check." Record **which Decision can now be delegated to AI under which conditions** as a change to the Delegation Envelope.

```text
Initial
Human Decision Surface = large
AI Delegation Envelope = small

Mature
Human Decision Surface = centered on Risk / Exception / Policy
AI Delegation Envelope = expands into Planning / Execution / Evaluation / Coordination
```

### Subsidiarity for Human-AI Teams

> **Place judgment with the agent closest to execution that can judge it reliably.**

If the Agent itself can verify mechanically, the Agent; if an independent AI Evaluator can judge, AI Evaluation; if organizational Risk, ambiguity, or Accountability remains, raise it to a Human.

### Delegation Contract

Continuous Decision Rights delegation requires the following.

```yaml
delegation:
  decision_class:
  scope:
  allowed_actions:
  evidence_required:
  escalation_conditions:
  expiry:
  audit:
  disclosure:
  rollback_or_revoke:
```

Do not make unbounded delegation like `scope: all` the standard form.

### S Transition Protocol

When weakening Approval Strength, do not skip levels at once.

```text
S5
↓ measure
S4
↓ measure
S3
↓ measure
S2 / S1
↓ measure
Remove the Gate itself if needed
```

At each stage, observe at least False Accept / Defect / Override / Approval Wait / Rubber-stamp signs. Premise that you can immediately return to a stronger S if it worsens.

### Monitor Approval Hollowing

Even when a Gate exists, the following signs may indicate that substantive control has drained away.

- Approval time is unnaturally short
- The approval Queue stagnates long-term
- Only delegation records spike
- Approvals happen without opening the Decision Packet
- lease / claim are left expired
- Exceptional "let it pass this time" becomes normal

The main countermeasure is not blaming approvers.

```text
Lower the judgment cost per approval
→ self-contained Decision Packet

Reduce the number of approvals itself
→ delegate machine-detectable / reversible / low-risk areas
```

Leaving a state where approval bandwidth is insufficient degrades not only latency but **Governance itself**.

### 23.2-A.1 Why — Why Are Decision Rights More Important than Tool Permission?

When thinking about "what may AI do," Permission comes up first. Allow File Write? Allow the Terminal? May it connect to Production?

Of course Permission is needed. A mechanism that technically stops dangerous operations is indispensable.

However, Permission alone does not determine work authority.

Suppose the FlowDesk Agent has Database Write permission. That does not mean "it may change the proxy-approval Rule." Even with permission to Deploy to Production, it does not mean "it may make Compliance Approval unnecessary for high-value applications."

What Tool Permission answers is **can this operation be executed**. What Decision Rights answer is **may this decision be made**.

```text
Permission
Can I do this operation?

Decision Right
Am I authorized to make this decision?
```

The same holds in a human company. An employee who can enter data into the accounting System cannot change the company's payment Policy. An Engineer who can Merge to the SCM cannot alone change the Product's Risk Appetite.

With AI, this boundary is hard to see because the Tools are powerful. Give an Agent broad Tool permissions and it can do more, which feels like "more can be delegated."

If you delegate work, decide the work-side conditions first. Which Decision Class. How far the Scope goes. What Evidence is needed. Up to which Risk it may proceed on its own. Where it returns to a Human. When the authority expires.

After that, grant the minimum necessary Tool Permission.

```text
Purpose / Work
↓
Decision Rights
↓
Delegation Contract
↓
Required Tool Permission
↓
Execution
```

Conversely, designing from Tool Permission produces "use it because it is usable."

Even when the same Agent can technically do everything, Decision Rights can be held separately. This is where room for autonomy is born.

Make Permission too narrow and AI cannot work. Too broad and it becomes dangerous. So **narrow Decision Rights first, then fully grant only the Permission needed to execute that judgment.**

And Decision Rights are not fixed. Measure judgment accuracy with Shadow Evaluation; if Evidence is stable, failures are detectable, and Rollback is possible, the Scope can be widened. Conversely, if an Incident occurs, it can be narrowed.

> **The core of AI autonomy is not which Tools to let it use. It is which judgments to delegate under which conditions.**

Permission is an Execution Control matter; Decision Rights are an Operating Model matter. They look similar, but what is being decided is different.

## 23.3 How Human Work Changes — Without Fixing the Destination

In the early stages of AI-Native adoption, as AI takes on more Execution, human Attention tends to move toward higher-abstraction judgments.

### Initial

```text
Human
├ Confirm investigation
├ Confirm design
├ Confirm implementation
├ Confirm Test
├ Confirm PR
└ Confirm Document
```

### Profile with Mature Harness / Eval

```text
Human
├ Outcome
├ Priority
├ Constraints
├ Risk
├ Architecture Boundary
├ Exception
├ Investment judgment
└ Harness Performance

AI
├ Planning
├ Decomposition
├ Execution
├ Coordination
├ Verification
├ Review Assistance
└ Improvement Proposal
```

Do not make humans "AI operators."
The more the Harness matures, the easier humans move away from fine-grained work.

However, DeepRail does not define this as the final destination for Humans.
As AI capability improves, Priority Proposal, Resource Allocation, Policy Draft, Strategy Option Design, and more can also move to AI.

> **There is no fixed Human-only Work List in the AI era. What exists is the responsibility placement at that point in time, and the conditions for moving responsibilities.**

---

### Review Abstraction Rises, but That Too Is Not Fixed

AI-Native adoption does not eliminate human Review.
In early-to-mid adoption, abstraction often rises as:

```text
Artifact Review
↓
Decision Review
↓
Management Review
↓
Governance Review
```

In a mature Team, humans mainly review:

```text
Outcome
Risk
Architecture Boundary
Exception
Investment
Irreversible Decision
Policy Change
```

However, once AI can carry the analysis, comparison, and part of the judgment for these, re-evaluate the Human Gate placement as well.
A Human Gate is not a sanctuary; it is **a Control Point that moves according to Evidence / Risk / Accountability**.

---

### Current Human Accountability Profile

```text
Human Accountability
= Final responsibility for Strategy / Objective
+ Risk Appetite
+ Decision Rights design
+ Evaluation Function design
+ Exception Judgment
+ Legal and organizational Accountability
```

This is not a capability claim that "only humans can think strategy."
It is a **Governance Profile** of where the organization currently places Accountability.

## 23.4 Change Review Targets Along with Autonomy

Autonomization does not mean "humans stop looking at anything."

```text
A0-A1
Human:
- Plan
- Code
- Test
- PR
checked in detail

A2
Human:
- Issue Plan
- High-risk Diff
- Test Evidence
checked

A3
Human:
- Feature Decision
- Cross-Issue consistency
- Exception
checked

A4+
Human:
- Epic Outcome
- Risk
- Architecture
- Harness Metrics
- Escalation
checked
```

Move Review targets from artifact volume to Decision/Evidence.

Prerequisites:

- Spec is explicit
- Traceability exists
- Tests are strong
- Standards are machine/AI-checkable
- Review Packet can be generated
- Eval is stable
- Risk Classification functions

Do not remove only Human Review while these are insufficient.

---

# Part VI Supplement — v0.8 New Specification: Organization, Execution Environment, Enforcement and Observation

> From v0.8, `DR-M20`–`DR-M24` are added as formal Manual IDs.
> Treat Manual IDs as stable identifiers, separate from chapter numbers.
