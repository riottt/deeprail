# DR-M11 — External Tool Integration Guide

> Status: **preview v0.16.8**> Creator / Lead Author: **RIO AMADA**

## 15.1 Organize Tools by Source of Truth

```text
Communication
├ Chat / Collaboration Channel
└ Mattermost

Work Management
├ Work Management
├ Legacy Work Management
├ Issue / Work Item
└ Issue / Work Item

Design
└ Figma

Source
├ SCM Platform
└ SCM Platform

Development Knowledge
└ Harness Workspace / Living Documents
```

---

## 15.2 Information Responsibility

The state to avoid most:

```text
Spec A is in Chat
Spec B is in Work Management
Spec C is in Figma comments
Old spec is in the README
New spec is in someone's head
```

External tools are for "input, notification, and work management"; clearly state which is the final canonical source.

---

## 15.3 Chat / Collaboration Channel

Main uses:

- Conversation
- Notification
- Approval requests
- Incident notification
- Agent completion notification
- Requirement candidates before Work Item conversion

Example rule:

```text
Request on Chat
↓
Formally adopted
↓
Convert to a Work Item in the Work Management System / SCM / Collaboration Platform etc.
↓
Update Living Documents as needed
```

Do not make a single chat message a permanent specification.

---

## 15.4 Work Management System

Treat as a Work Item management Adapter.

Common concepts:

```text
Epic / Parent
↓
Issue / Story / Task
↓
Subtask
```

Even when using Legacy Work Management, map product-specific Tracker/Status/Workflow to the common Work Item model.

---

## 15.5 Figma

Decide the canonical scope of design.

Example:

```text
Visual / Interaction
→ Figma

System Behavior / API / Data Contract
→ Living Document

Correspondence with implementation
→ Trace via Link / ID
```

Do not leave specification decisions only in Figma comments.

---
