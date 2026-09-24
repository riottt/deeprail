# DR-M18 — Release / Production Operations Guide

> Status: **preview v0.16.8**> Creator / Lead Author: **riottt**

## 22.1 Separate Development Complete from Release Complete

```text
Implementation
↓
PR/MR
↓
CI
↓
Merge
↓
Staging
↓
Release Gate
↓
Production
↓
Monitoring
↓
Reinvest / Learn
```

---

## 22.2 Items Covered

- CI/CD
- DEV/STG/PROD
- Migration
- Feature Flag
- Release Approval
- Rollback
- Hotfix
- Production Incident
- Monitoring
- Post-release confirmation
- Production Access

---

## 22.3 AI Production Operations

Even when Harness maturity is high, judge Production operations under a separate Risk Policy.

Do not auto-permit based on autonomy level alone.

---
