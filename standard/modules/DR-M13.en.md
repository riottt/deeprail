# DR-M13 — AI Asset and Harness Change Management Guide

> Status: **preview v0.16.8**> Creator / Lead Author: **RIO AMADA**

## 17.1 Managed Objects

- Agent
- Skill
- Rule
- Instruction
- Prompt
- Hook
- MCP
- Tool settings
- Harness Script
- Model Routing Rule
- Eval Case

---

## 17.2 Change Levels

### Minor

- Typos
- Additional explanation
- Non-functional formatting

### Behavior Change

- Agent instruction changes
- Skill procedure changes
- Tool usage changes
- Output format changes

### Structural Change

- Agent addition/removal
- Skill consolidation/abolition
- Harness structure changes
- Permission changes
- Model Routing changes
- External Tool additions

Vary Review/Eval intensity per change level.

---

## 17.3 Update Flow

```text
Improvement request
↓
Can existing assets handle it?
↓
Change proposal
↓
Local Test
↓
Eval
↓
Review
↓
Merge
↓
Release Note
↓
Apply to Team
```

---
