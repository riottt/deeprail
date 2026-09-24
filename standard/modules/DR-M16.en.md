# DR-M16 — Security and AI Governance Guide

> Status: **preview v0.16.8**> Creator / Lead Author: **riottt**

## 20.1 Do Not Treat Permissions as One Bundle

Separate at least the following.

```text
Read
Write
Execute
External Send
Production Access
Secret Access
Approval
```

---

## 20.2 Principles

- Least privilege
- Do not write Secrets directly into Prompts/Documents
- Separate Production permission from normal development
- Define what information may be sent externally
- Tool/MCP Allowlist
- Restrict destructive Commands
- Audit Log
- Define operations that require Human Approval

---

## 20.3 Dangers of Hooks/Tools

Not only natural-language instructions to Agents, but also Hooks/Scripts/Tools that hold execution permission themselves are Review targets.

---
