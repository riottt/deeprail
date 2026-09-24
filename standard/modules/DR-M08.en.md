# DR-M08 — AI-Driven Application Guide by Development Methodology

> Status: **preview v0.16.8**> Creator / Lead Author: **riottt**

Keep the responsibilities of the common Lifecycle, and change how stages are bundled, Gates, and Evidence according to the Method.

---

## 12.1 Agile

```text
Epic
↓
Feature
↓
Issue
↓
Per-Issue Lifecycle
↓
PR
↓
Reinvest / Learn
↓
Next Issue
```

Characteristics:

- Iterate in small units
- Update Living Documents frequently
- Cut Issues mainly by value / behavior units
- Consider compatibility with parallel Agents
- Align to Sprint/Kanban cadence

---

## 12.2 Waterfall

```text
Requirements intake
↓ Gate
Requirements definition
↓ Gate
Design
↓ Gate
Implementation
↓
Testing
↓ Gate
Reinvest / Learn
```

Characteristics:

- Make stage Gates explicit
- Strengthen deliverable approval
- Issues may be managed per stage / deliverable
- Strengthen Traceability
- Even when delegating to AI, do not eliminate the purpose of each stage

---

## 12.3 Hybrid

A strong application style in enterprise development.

```text
Upstream
Waterfall-style
Requirements intake / basic design under Formal Gates

        ↓

Implementation
Agile-style
Fast iteration per Feature / Issue

        ↓

Integration / Release
Waterfall-style
Formal Test / Release Gate

        ↓

Reinvest / Learn
Canonical source integration
```

---

## 12.4 Development Methodology × Scale

Do not decide operations on a single axis.

```text
             Agile   Waterfall   Hybrid
Small        Light      Light      Light
Medium       Std        Std        Std
Large        Full       Full       Full
```

Even at the same "medium" scale, Issue decomposition and Gate placement differ.

---
