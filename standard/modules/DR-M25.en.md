# DR-M25 — AI Adoption Promotion and Organizational Transition Management Guide

> Status: **preview v0.16.8**> Creator / Lead Author: **RIO AMADA**

**Layer:** Transformation / Organization / Operating Model
**Main readers:** PM / Program Manager / AI promotion lead / CTO / VPoE / PMO / Engineering Manager / Security, IT, Platform leads
**Purpose:** Define the methodology for transitioning existing organizations and engagements step by step toward an AI-native Operating Model while organizing current constraints.

M25 is not "an AI Tool adoption procedure."

Its target is:

> **the Transformation Program itself — creating a state where the organization can use AI, then commonalizing, standardizing, and rolling out that state**

## M25.1 Current State Assessment

Do not pick an AI Tool first.

Organize the current state from at least the following viewpoints.

```text
Business / Product
Organization
Development Process
SCM
Work Management
Architecture
Runtime / Environment
Security
Data Classification
Network
Device
Identity / Account
Procurement
Legal
Approval
Development Standard
Quality / Test
Release
Operations
Knowledge
Skill / Training
Culture
```

Example:

```text
SCM: Centralized VCS
Work Management: Legacy Work Management
OS: Windows managed device
Network: Direct Internet prohibited
AI: External generative AI prohibited
Source Code: External SaaS upload prohibited
Method: Waterfall
Approval: Formal design review
Security Review Lead Time: 8 weeks
```

Do not evaluate the current state as "bad because it is Legacy."
Record it as the starting condition of the Transformation.

---

## M25.2 Constraint Register

Do not leave constraints that block AI adoption as complaints, verbal information, or implicit assumptions.

```yaml
constraint:
  id:
  category:
  description:
  owner:
  affected_scope:
  impact:
  resolution_path:
  workaround:
  decision_required:
  lead_time:
  status:
```

Representative categories:

```text
Security
Legal
Procurement
Network
Device
Data
SCM
Architecture
Platform
Account / IAM
Development Standard
Operations
Human Capacity
```

Connect Constraints to the Backlog.

---

## M25.3 Stakeholder Map

In an AI adoption Program, organize at least the following.

```text
Executive Sponsor
Program / Transformation Owner
Product / Business Owner
Engineering
Architecture
Security
Legal
Procurement
IT / Network
Platform
Development Standard
QA
Operations
Education / Enablement
```

For each issue, define:

```text
Who proposes?
Who decides?
Who approves?
Who executes?
Who operates?
Who must be consulted?
```

A form such as RACI may be used, but DeepRail Core does not depend on a specific method.

---

## M25.4 Transformation Profile Assessment

Assess the following.

```text
Project State
P0 / P1 / P2 / P3

AI Availability
AI-0 / AI-1 / AI-2 / AI-3 / AI-4

Organization Enablement
O0 / O1 / O2 / O3 / O4
```

Change the adoption order based on the assessment result.

### Profile A — AI Native Greenfield

```text
P0 × AI-3〜4 × O2〜4
```

Main battlegrounds:

- Target Operating Model
- Harness
- Evidence
- Autonomy
- Quality Gate
- Organization Learning

### Profile B — Modern but AI-Constrained

```text
P0〜P1 × AI-0〜1 × O0〜1
```

Main battlegrounds:

- Security Review
- Data Policy
- Procurement
- Network
- Account
- Approved Toolchain
- Logging / Audit
- Pilot permission

Do not build out the Coding Harness first.

### Profile C — Modern Brownfield

```text
P1 × AI-2〜4 × O1〜3
```

Main battlegrounds:

- Insertion into Existing Processes
- Source of Truth organization
- Review / Test redesign
- Connection with existing CI
- Team commonalization

### Profile D — Legacy / Brownfield

```text
P2〜P3 × AI-0〜2 × O0〜2
```

Main battlegrounds:

- Constraint Inventory
- Shrink Profile
- Adapter
- Human Gate
- Legacy SCM
- Shared Environment
- Existing Waterfall Artifacts
- Manual Approval
- Small Pilot

Do not make a full Infrastructure rebuild a prerequisite for AI adoption.

---

## M25.5 Target Operating Model

The Target is not a Tool name. **Draw the flow of work first.**

Bad Target:

```text
Roll out the Coding Agent Runtime to everyone
```

Good Target:

```text
Business Requirement
↓
AI-assisted Requirement Structuring
↓
Human Alignment
↓
AI-assisted Design / Build
↓
Machine Gate
↓
Independent AI Review
↓
Human Decision Review
↓
Test / Eval
↓
Release
↓
Living Document
```

Include the following in the Target Operating Model.

```text
Human Role
AI Role
Decision Rights
Source of Truth
Gate
Evidence
Escalation
Permission
Evaluation
Knowledge Reinvestment
```

---

## M25.6 Enablement Backlog

Consolidate the organization-side preparation needed for AI adoption into one Backlog.

Example:

```text
EPIC: AI Development Enablement

├ SEC-001 Security review
├ DATA-001 Data classification
├ LEGAL-001 Terms / legal review
├ PROC-001 Procurement
├ NET-001 Proxy / endpoint approval
├ IAM-001 Account provisioning
├ DEV-001 Shared harness
├ GOV-001 Usage policy
├ EVAL-001 Evaluation baseline
├ EDU-001 Training
├ OPS-001 Support model
├ LOG-001 Audit / logging
└ COST-001 Cost monitoring
```

Give each Item:

```text
Owner
Dependency
Lead Time
Decision
Evidence
Exit Criteria
```

---

## M25.7 Security / Governance Enablement

In large enterprises, the main Bottleneck of AI adoption can be Security / Governance rather than Coding.

Organize at least the following.

```text
What may be sent to AI
Up to which Data Class is possible
Whether Source Code may be sent
Whether Customer Data may be sent
Where Logs are stored
Provider's use for training
Retention
Account management
Model / Tool Allowlist
MCP / External Tool
Network connection
Secret Access
Production Access
Audit
Incident Response
```

Do not push Security and Data applications into clerical work to be cleared before adoption. Manage them as formal Work Items of the Transformation Program.

---

## M25.8 Shared Enablement

Distinguish "one person can use it" from "the organization can use it."

```text
Personal Experiment
↓
Controlled Pilot
↓
Team Shared Setup
↓
Approved Standard Setup
↓
Managed Organization Platform
```

What common usage requires:

- approved account
- common configuration
- policy
- standard harness
- logging
- support
- training
- version management
- security review
- cost ownership

While it runs only on individuals' local settings, it is hard to say Organization Adoption has been reached.

---

## M25.9 Pilot Design

What a Pilot verifies is not only whether the Tool works.

```text
Pilot
=
Tool Verification
+
Process Verification
+
Organization Verification
```

Before the Pilot starts, define:

```text
Objective
Scope
Baseline
Evaluation Function
Allowed AI
Allowed Data
Human Gate
Owner
Duration
Kill Criteria
Expected Learning
```

Pilot success conditions:

```text
The Engineering Loop ran
+
Security / Approval / Support ran
+
Evidence was captured
+
The Learning needed for the next decision was obtained
```

---

## M25.9-A Evaluation Trust / Delegation Pilot

Telling an organization that does not yet know AI to "please trust it first" does not move anything.
In the Pilot, verify not only what AI can do but also **how far AI evaluation can be used for Gate judgment**.

Recommended introduction order:

```text
1. Bound the Work Class
2. Keep Human evaluation as the Baseline
3. Run AI in parallel as a Shadow Evaluator
4. Classify Human / AI disagreements
5. Improve Evaluation Criteria / Evidence / Harness
6. Move only Work Classes meeting Exit Criteria to EA2
7. Shift from Human full approval to Risk / Exception focus
8. Confirm stability via Sampling / Audit
9. Promote in stages to EA3 and beyond
10. On Drift / Incident, immediately step back one level
```

Keep at least the following in the Pilot Report.

```yaml
evaluation_delegation:
  work_class:
  current_ea_level:
  target_ea_level:
  sample_size:
  false_accepts:
  false_rejects:
  unknowns:
  human_overrides:
  escaped_defects:
  evidence_gaps:
  rollback_events:
  exit_criteria:
  decision_owner:
  next_action:
```

Looking only at AI's accuracy does not tell you whether it can be operated.
**Decide Evaluation Authority including which Failures are detectable, whether serious False Accepts are not missed, whether failure can be rolled back, and who holds Accountability.**

---

## M25.10 Rollout

Rollout is not Tool distribution.

```text
Pilot
↓
Pattern Extraction
↓
Standardization
↓
Enablement Package
↓
Team Rollout
↓
Measurement
↓
Adjustment
↓
Multi-team / Organization Rollout
```

For horizontal rollout, transplant not a copy of the finished product but:

> **common parts + how to measure + the adoption process**

---

## M25.11 Change Management

What AI adoption may change:

```text
Role
Responsibility
Review
Approval
Skill
Performance expectation
Team structure
Support
Career / training
Communication
Decision speed
```

Do not end it at "new Tool training."

Create a state where you can explain to humans:

```text
What changes
What does not change
What is delegated to AI
What humans hold
Whom to Escalate to when in trouble
```

---

## M25.12 Transformation Metrics

Do not make AI utilization the main success metric.

Examples:

```text
Constraint Resolution Lead Time
Security Approval Lead Time
Account Provisioning Lead Time
Pilot Cycle Time
Adoption Readiness
Human Intervention
Review Capacity
Training Completion
Support Load
Standard Compliance
Business / Engineering Outcome
```

Change the evaluation function per Transformation Phase.

---

## M25.13 Transformation Failure

Representative Failures:

```text
Tool-first
Contracted the Tool but the Process does not change

Training-first
Training for a Tool that cannot be used yet comes first

Harness-first
Building only the Harness while Security is unapproved

Pilot-isolation
Pilot success cannot be promoted to a common Platform

Shadow-AI
Only individuals use it with their own settings

No-owner
No Owner for Security / Harness / Eval / Support

No-kill-criteria
No criteria for stopping the Pilot

No-scale-path
No horizontal rollout path after success
```

---

## M25.14 Transformation Completion

A Transformation is not complete at "the AI Tool became usable."

Treat reaching at least the following state as one completion condition of organizational adoption.

```text
Approved
Shared
Documented
Supported
Measured
Governed
Transferable
```

---
