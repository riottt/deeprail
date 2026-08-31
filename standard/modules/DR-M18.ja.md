# DR-M18 — Release・Production運用ガイド

> Status: **canonical v0.16.8**> Creator / Lead Author: **RIO AMADA**

## 22.1 開発完了とRelease完了を分ける

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

## 22.2 扱う項目

- CI/CD
- DEV/STG/PROD
- Migration
- Feature Flag
- Release Approval
- Rollback
- Hotfix
- Production Incident
- Monitoring
- Release後確認
- Production Access

---

## 22.3 AIのProduction操作

Harness成熟度が高くても、Production操作は別のRisk Policyで判断する。

自律化レベルだけで自動許可しない。

---
