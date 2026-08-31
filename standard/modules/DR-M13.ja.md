# DR-M13 — AI資産・Harness変更管理ガイド

> Status: **canonical v0.16.8**> Creator / Lead Author: **RIO AMADA**

## 17.1 管理対象

- Agent
- Skill
- Rule
- Instruction
- Prompt
- Hook
- MCP
- Tool設定
- Harness Script
- Model Routing Rule
- Eval Case

---

## 17.2 変更レベル

### Minor

- 誤字
- 説明追記
- 非機能的な整形

### Behavior Change

- Agent指示変更
- Skill手順変更
- Tool利用方法変更
- Output形式変更

### Structural Change

- Agent追加/削除
- Skill統廃合
- Harness構造変更
- 権限変更
- Model Routing変更
- 外部Tool追加

変更レベルごとにReview/Eval強度を変える。

---

## 17.3 更新フロー

```text
改善要求
↓
既存資産で対応可能か
↓
変更案
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
Teamへ適用
```

---
