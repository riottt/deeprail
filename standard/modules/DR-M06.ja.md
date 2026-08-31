# DR-M06 — 開発ループ設計ガイド

> Status: **canonical v0.16.8**> Creator / Lead Author: **RIO AMADA**

## 10.1 大ループ

開発外部まで含めたループ。

```text
Chat / Collaboration Channel
Work Management System
Figma
顧客要求
障害
問い合わせ
        ↓
要求候補
        ↓
Work Item化
        ↓
規模判定
        ↓
Development Lifecycle
        ↓
Release
        ↓
Reinvest / Learn
        ↓
Harness / 正本更新
        ↓
次の要求
```

チャットで出た要望から直接コード変更へ進ませない。

必ずWork Item化する境界を置く。

---

## 10.2 中ループ

Issue/Feature単位。

```text
Issue
↓
Context確認
↓
調査
↓
計画
↓
設計
↓
実装
↓
Test
↓
Review
↓
PR/MR
↓
Reinvest / Learn
```

チームメンバーが日常的に回す中心ループ。

---

## 10.3 小ループ

Agent内部のコード変更ループ。

```text
Read
↓
Hypothesis
↓
Edit
↓
Build
↓
Test
↓
Failure?
├ Yes → Analyze → Fix → Test
└ No  → Review
```

無限ループを防ぐため、停止条件を持つ。

例：

```text
同一原因で3回失敗
↓
試行内容を要約
↓
人間へEscalation
```

回数はプロジェクト特性で変更する。

---

## 10.4 ループごとにボトルネックを観測する

大・中・小ループは、単に処理を回すための構造ではない。
**どこでFlowが滞留しているかを観測する単位**としても利用する。

### 大ループで見るもの

- Requirement Lead Time
- Design Lead Time
- Review Queue
- Test Queue
- Release待ち
- 外部チーム待ち
- Security Approval待ち
- Living Document更新待ち

### 中ループで見るもの

- Issue Cycle Time
- PR/MR待ち時間
- Human Intervention回数
- Agent Retry回数
- Blocked時間
- Review手戻り

### 小ループで見るもの

- Build/Test失敗回数
- Retry回数
- Tool Error
- Context不足
- Agent Escalation

改善は次の循環で行う。

```text
Flow計測
↓
現在のBottleneck特定
↓
Harness改善対象を決定
↓
Rule / Skill / Agent / Tool / Gateを変更
↓
Eval
↓
再計測
↓
次のBottleneckへ
```

---
