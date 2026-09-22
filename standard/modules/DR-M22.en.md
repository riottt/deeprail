# DR-M22 — AI-Native Organization Operating Model Guide

> Status: **preview v0.16.8**> Creator / Lead Author: **riottt**

**Layer:** Organization / Operating Model
**Purpose:** Design an organization where Humans and AI are mixed as a structure of Role, Decision, Authority, Context, Evaluation, and Learning.

## M22.1 Strategy-to-Execution

```text
Strategy / Intent
↓
Portfolio / Initiative
↓
Demand / Requirement
↓
Operating Model
↓
Engineering / Business Execution
↓
Evidence
↓
Outcome
↓
Organizational Learning
↓
Next Strategy
```

Do not make upper-level Intent and lower-level Execution separate systems.

## M22.2 Human / AI Role Model

A Role is defined not by title but by the following contract.

```text
Purpose
Input
Output
Decision rights
Allowed actions
Forbidden actions
Required context
Escalation
Evaluation
Owner
```

Do not treat adding Agents as Organization Design.
Push deterministic processing to Script / Rule / Tool, and make something an Agent only when Role separation is needed.

## M22.3 Decision Rights

Explicitly assign at least the following responsibilities.

- Human Owner
- Decision Owner
- Approval Owner
- Escalation Owner
- Standard Owner
- Harness Owner
- Eval Owner
- Risk Owner
- Environment / Operations Owner

At M0-M1, concurrent holding is acceptable.
As maturity rises, separate them according to Risk and load.

## M22.4 Decision Ledger

For important decisions, record not only the result but also:

```text
Decision
Context
Options
Rationale
Owner
Evidence
Scope
Expiry / Revisit condition
```

"Decisions not adopted" are also a target of organizational learning.

## M22.5 Authority / Permission

Separate Autonomy from Permission.

```text
Autonomy
= how far it may proceed on its own

Permission
= what it may execute
```

Even with high Autonomy, it does not need Production Write or External Send.

## M22.6 Escalation

"Return to a human" is not enough for Escalation.

Define through:

```text
Cause Class
↓
Destination Owner
↓
Expected decision
↓
SLA / timeout
↓
Fallback
```

## M22.7 Organizational Source of Truth

Organizational knowledge uses

```text
Canonical Source
+
Declared Projection
+
Drift Check
```

as the basic form.

Do not prohibit copies; prohibit **undeclared copies**.

## M22.8 Organizational Memory

```text
Feedback / Incident / Decision
↓
Classification
↓
Rewrite
↓
Policy / Rule / Skill / Process / Eval / Living Document
↓
Capability
```

Sharing is done not as a simple Export but as **cleanup and generalization into a reusable form**.

## M22.9 Policy Architecture

Connect Organization Policy to the Enforcement Ledger too.

```text
Policy
├ machine block
├ machine nudge
├ human review
├ measurement
└ declared-only
```

Do not pretend everything can be machine-enforced.

## M22.10 Capability Model

A Capability is not established by "we contracted the Tool" or "a Skill file exists."

Include up to the following in the Capability Lifecycle.

```text
Available
→ Discoverable
→ Usable
→ Measured
→ Maintained
→ Transferable
```

### M22.10-A Experience × AI-Native Capability — Do Not Decide Hiring, Placement, and Evaluation by Years Alone

In an AI Native Organization, do not collapse `years of experience` and `can use AI` onto one axis. Separate at least the following.

```text
Domain / Technical Experience
AI Delegation Capability
Evaluation / Evidence Capability
Work Class Fit
Context / Harness Leverage
Accountability / Escalation Judgment
```

This Profile is not a personnel Rating itself. It is an Operating Input for deciding **who is entrusted with which Work Class under which Delegation Envelope**.

The organization avoids the following false simplifications.

- Assuming "a new graduate, therefore strong at AI Native"
- Assuming "a Senior, therefore automatically the strongest once using AI"
- Directly tying AI usage volume to Performance evaluation
- Directly tying AI-generated Output volume to individual Productivity
- Using Juniors getting faster with AI as grounds that Mentoring is unnecessary

In hiring, placement, and development, observe the following more concretely than years.

```text
Can they define an Outcome
Can they split work into Verifiable Units
Can they hand AI Scope / Permission / Evidence
Can they explain weaknesses of AI Output
Can they Escalate without hiding Unknowns
Can they externalize experience into Rule / Context / Eval / Harness
```

> **A strong person in the AI era is neither someone who can do everything alone without AI, nor someone who throws everything at AI. It is someone who can safely complete larger Outcomes as a Human + AI System.**

From this viewpoint, an AI Native newcomer ramping up fast on Bounded Work is compatible with an AI Native experienced person amplifying Tacit Knowledge to carry larger Decisions.

## M22.11 Organizational Evals

Example evaluation targets:

- Decision Quality
- Execution Quality
- Escalation Accuracy
- Human Intervention
- Rework
- Lead Time
- Knowledge Reuse
- Policy Compliance
- Risk Incident
- Business Outcome

Do not translate AI Worker evaluation directly into human personnel evaluation.

## M22.12 Organizational Learning

The learning Loop itself is also an observation target.

Even if retrospectives, suggestion systems, and automatic learning exist, if they are unused / broken / never reach improvement, they are not a Capability.

---
