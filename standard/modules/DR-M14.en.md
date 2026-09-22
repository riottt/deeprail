# DR-M14 — Living Documents and Knowledge Management Guide

> Status: **preview v0.16.8**> Creator / Lead Author: **RIO AMADA**

## 18.1 Definition of a Living Document

A Living Document is the canonical source that shows not history but "the current correct state."

---

## 18.2 Difference from a Change Log

```text
Change Log
→ What changed in the past

Living Document
→ How things are now
```

When both are needed, separate them.

---

## 18.3 Source of Truth

Give each piece of information an Owner.

### Artifact Consumer Contract

Each artifact declares "who is the primary consumer."

```text
AI-first
→ machine-checkable / stable ID / fixed vocabulary / partial-read safe

Human-first
→ reviewable / visual / decision-oriented / explainable

Both
→ machine-readable Canonical Source + human-readable View
```

In the Both case, the human-facing View must not change the meaning of the canonical source. Reordering, summarizing, and visualization are allowed, but content changes are made on the canonical side. Also clearly state the canonical source's writer (Human / AI / Shared).

| Information | Canonical source example |
|---|---|
| UI design | Figma |
| API Contract | API specification |
| DB Schema | Schema + DB design |
| Work Status | Work Management System/Issue |
| Source | Git |
| Architecture Decision | ADR/Design Doc |
| AI development rules | Harness Documents |

---

## 18.4 Reinvest / Learn Completion Conditions

```text
Code and canonical sources match
Test results reflected
Related ADRs updated
Necessary Agent/Skill improvements done
Referenceable by the next Agent
No broken links
No old specification remains as canonical
```

---

## 18.4.1 Structural Reinvestment — Returning Learning to Structure

In Reinvest / Learn, do not close learning with just "adding a cautionary note."
For recurring Failure / Human Correction / Useful Pattern, move it to the most reproducible Control in the following order.

```text
One-time judgment
→ Decision Record / Context Asset

Repeated knowledge shortage
→ Living Document / Rule / Skill

Mechanically decidable Failure
→ Test / Checker / Hook / CI Gate

Needs continuous observation
→ Eval / Monitoring / Meta-Health

Permission / Risk problem
→ Permission / Delegation Contract / Human Gate
```

Do not make "a human remembers and takes care next time" the final form where possible.
However, do not make it a goal to convert everything into Automation either. Things whose essence is tacit knowledge, Context dependence, or Human Judgment may remain as Decision Interface / Training / Sampling.

Completion judgment includes **whether Evidence can confirm that the next Execution or Evaluation actually changed**.

### 18.4.1.1 Why — Why Learning Must Be Embedded into Structure

"Let's be careful next time" sounds like learning.

But if the next execution is the same, the mechanism has learned nothing.

Suppose that in FlowDesk's proxy approval, the Agent forgot to record the original Approver's ID in the audit Log. A human noticed in Review and fixed it. The Retro minutes said "in proxy approval, always record the original approver."

If it ends there, the same thing can happen in the next Session. Another Agent may not read those minutes. Another Team may not even know they exist. Humans will forget in a few months.

The knowledge remained. Behavior did not change.

DeepRail weighs Reinvestment heavily because of this difference.

There are kinds of learning. Not everything should become Automation. Things strongly dependent on Context, like Business Judgment, are better kept in Decision Records or Training. On the other hand, things that can be mechanically decided — "this Field must always be in the Audit Log" — can be dropped into Tests or Checkers.

```text
Learned
↓
Classify
↓
Place it in the strongest location that changes the next execution

Knowledge → Context / Document
Procedure → Skill / Workflow
Deterministic Rule → Test / Checker / Hook
Risk Boundary → Permission / Gate
Evaluation Gap → Eval / Evidence Contract
```

Done this far, a failure is no longer a one-time loss. It becomes an asset that cheaply prevents the same Failure from next time on.

Conversely, if a Human makes the same point every time, it may not be that the person is diligent — the System may be outsourcing learning to human memory.

Of course, Structure also has Cost. Add too many Rules and Context becomes heavy. Add Gates and Flow slows. If a Checker misjudges, it creates another Failure. So choose the placement by recurrence frequency, Risk, Detectability, and Maintenance Cost.

And embedding is not the end. Does the Test actually catch the Failure? Is the Rule referenced? Has the Gate become a hollow formality? Is it fixing an outdated assumption? Evaluate the Structure itself, and weaken or remove it when no longer needed.

For FlowDesk's audit Log problem: add a Regression Test, include Audit Evidence in the Verification Procedure, and shape it so another Team can reuse it when creating proxy Decisions. The next time the same kind of work arrives, the mechanism works before a human remembers.

> **Whether an organization has learned is judged not by whether documents increased, but by whether the next Execution changed.**

Embedding learning into Structure is not to solidify knowledge. It is to make it work on the next job without depending on human memory.

## 18.5 Do Not Consume Human "Corrections" Inside the Session

Returning corrections to an AI Agent itself is unavoidable.

If the same pointing-out is repeated in the next Session and the one after, it is better to stop once.

```text
AI makes a mistake
↓
Human corrects it in Chat
↓
Fixed in that Session
↓
Session ends
↓
Same mistake next time
```

See this recurrence not as an individual's lack of care but as a Harness-side Failure.

Return repeated Feedback to one of the following.

```text
Insufficient understanding
→ Living Document

Permanent constraint
→ Rule / Instruction

Repeated working method
→ Skill

Specialized judgment
→ Agent

Mechanically decidable
→ Hook / CI / Test

Want to detect quality degradation
→ Eval Case
```

Feedback Flow:

```text
Human Correction
↓
Judge: one-time fix or recurring
↓
Recurring
↓
Convert to a Harness Asset
↓
Add Eval
↓
Automatically applied from the next Session
```

In Reinvest / Learn, confirm not only the canonicalization of code but also **whether the corrections a human made this time include knowledge that can be returned to the Harness for future use**.

---
