# DR-M12 — AI Execution Platform and Model Selection Guide

> Status: **preview v0.16.8**> Creator / Lead Author: **RIO AMADA**

## 16.1 Runtime Adapter

Example targets:

- Coding Agent Runtime
- Coding Agent Runtime
- Coding Agent
- Coding Agents added in the future

Separate the common standard from the Runtime.

---

## 16.2 Coding Agent Runtime Adapter

Example:

```text
Always-on Context
→ Runtime Instruction / Rules

Reusable Procedure
→ Skill

Isolated Specialist
→ Subagent

Deterministic Enforcement
→ Hook
```

---

## 16.3 Coding Agent Runtime Adapter

Consistent with this standard as well.

---

## 16.4 Coding Agent Adapter

Adapt the common Harness standard into the SCM Platform-specific configuration structure.

---

## 16.5 Model Routing

Do not fix on a single model.

```text
Level A: High Reasoning
- Architecture
- Complex failures
- High-risk Review
- Large-scale impact analysis

Level B: Standard
- Normal implementation
- Test
- General Review
- Medium-scale Issues

Level C: Lightweight
- Routine investigation
- Document formatting
- Mechanical classification
- Simple fixes
```

---

## 16.6 Harness and Token/Cost

Do not define it as "a Harness always reduces Tokens."

The hypothesis is:

```text
Without Harness
↓
Long Prompt every time
↓
More exploration
↓
Guessing the rules
↓
Tends to read unnecessary Context

With Harness
↓
Short Map
↓
Guided to the needed Rule/Skill/Document
↓
Exploration scope is limited
↓
Potentially more areas where even a lightweight Model can succeed
```

However, adding more Agents, longer Runs, and extra Reviews may increase total Tokens.

The evaluation axis is not Token alone; look at:

```text
Quality
× Lead Time
× Human Time
× Token
× Cost
× Retry
```

---

# Part D. Harness Lifecycle / Knowledge / Education
