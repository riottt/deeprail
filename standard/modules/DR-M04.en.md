# DR-M04 — Environment Setup Guide

> Status: **preview v0.16.8**> Creator / Lead Author: **riottt**

## 8.1 Covered Targets

At a minimum, consider the following environment differences.

- Windows
- macOS
- Linux
- WSL
- Local development
- Dev Container
- Cloud Development Environment
- Sandbox-type Agent Runtime

---

## 8.2 Cautions When OSes Are Mixed

- `/` and `\`
- bash / zsh / PowerShell
- LF / CRLF
- chmod
- symbolic link
- Case-sensitivity handling
- PATH
- Versions of Node/Python/JDK etc.
- package manager
- Docker Desktop dependency
- `.env`
- Where credentials are stored
- CLI differences
- Script execution permission

Where possible, consider cross-platform implementations in Python/Node etc. rather than relying only on OS-dependent Shell Scripts.

---

## 8.3 Setup Completion Conditions

```text
Repository can be obtained
Build succeeds
Frontend starts
Backend starts
DB connection
Tests run
AI Runtime starts
Harness Rules load
Skill invocation
Agent invocation
Required Tools connect
PR/MR can be created
```

---

# Part B. Development Process
