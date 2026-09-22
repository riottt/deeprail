# DR-M03 — Harness Composition and Usage Guide

> Status: **preview v0.16.8**> Creator / Lead Author: **riottt**

## 7.1 Responsibilities of AI Assets

Conceptually, distinguish the following.

| Asset | Purpose |
|---|---|
| Instruction / Rule | Constraints applied continuously |
| Skill | Repeated procedures and workflows |
| Agent | An execution agent with specialized responsibility |
| Hook | Processing executed deterministically on specific events |
| Tool | A capability by which an Agent acts |
| MCP | A boundary that connects external systems as Tools |
| Prompt | A temporary, single-purpose request |
| Living Document | Canonical Context describing the current state |
| Eval | A test that confirms Harness/Agent behavior |

---

## 7.2 Placement Decisions

```text
A constraint to observe every time?
→ Rule / Instruction

A repeated procedure?
→ Skill

Need expertise / an independent Context?
→ Agent

Processing you always want executed?
→ Hook / CI

Need external information or external operations?
→ Tool / MCP

Information that explains the current specification?
→ Living Document
```

---
