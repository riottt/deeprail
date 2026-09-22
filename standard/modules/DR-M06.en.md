# DR-M06 — Development Loop Design Guide

> Status: **preview v0.16.8**> Creator / Lead Author: **riottt**

## 10.1 The Large Loop

A loop that includes the outside of development.

```text
Chat / Collaboration Channel
Work Management System
Figma
Customer requests
Failures
Inquiries
        ↓
Requirement candidates
        ↓
Work Item conversion
        ↓
Scale assessment
        ↓
Development Lifecycle
        ↓
Release
        ↓
Reinvest / Learn
        ↓
Harness / canonical source update
        ↓
Next request
```

Do not let requests raised in chat proceed directly to code changes.

Always place a boundary where they become Work Items.

---

## 10.2 The Medium Loop

Per Issue/Feature.

```text
Issue
↓
Confirm Context
↓
Investigate
↓
Plan
↓
Design
↓
Implement
↓
Test
↓
Review
↓
PR/MR
↓
Reinvest / Learn
```

The central loop team members run daily.

---

## 10.3 The Small Loop

The code-change loop inside an Agent.

```text
Read
↓
Hypothesis
↓
Edit
↓
Build
↓
Test
↓
Failure?
├ Yes → Analyze → Fix → Test
└ No  → Review
```

To prevent infinite loops, have a stop condition.

Example:

```text
Fails 3 times with the same cause
↓
Summarize what was tried
↓
Escalate to a human
```

Change the count per project characteristics.

---

## 10.4 Observe Bottlenecks per Loop

The large, medium, and small loops are not just structures for running processes.
**They are also used as units for observing where Flow is stagnating.**

### What to Watch in the Large Loop

- Requirement Lead Time
- Design Lead Time
- Review Queue
- Test Queue
- Waiting for Release
- Waiting on external teams
- Waiting for Security Approval
- Waiting on Living Document updates

### What to Watch in the Medium Loop

- Issue Cycle Time
- PR/MR wait time
- Human Intervention count
- Agent Retry count
- Blocked time
- Review rework

### What to Watch in the Small Loop

- Build/Test failure count
- Retry count
- Tool Errors
- Context shortage
- Agent Escalation

Improvement runs in the following cycle.

```text
Measure Flow
↓
Identify the current Bottleneck
↓
Decide the Harness improvement target
↓
Change Rule / Skill / Agent / Tool / Gate
↓
Eval
↓
Re-measure
↓
To the next Bottleneck
```

---
