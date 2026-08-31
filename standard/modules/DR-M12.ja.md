# DR-M12 — AI実行基盤・モデル選定ガイド

> Status: **canonical v0.16.8**> Creator / Lead Author: **RIO AMADA**

## 16.1 Runtime Adapter

対応対象例：

- Coding Agent Runtime
- Coding Agent Runtime
- Coding Agent
- 将来追加するCoding Agent

共通標準はRuntimeから分離する。

---

## 16.2 Coding Agent Runtime Adapter

例：

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

本標準とも整合する。

---

## 16.4 Coding Agent Adapter

Harness共通標準をSCM Platform固有の設定構造へAdapterする。

---

## 16.5 Model Routing

モデルを一種類に固定しない。

```text
Level A: High Reasoning
- Architecture
- 複雑な障害
- 高リスクReview
- 大規模影響分析

Level B: Standard
- 通常実装
- Test
- 一般的なReview
- 中規模Issue

Level C: Lightweight
- 定型調査
- Document整形
- 機械的分類
- 単純修正
```

---

## 16.6 HarnessとToken/Cost

「Harnessがあると必ずTokenが減る」とは定義しない。

仮説としては次。

```text
Harnessなし
↓
毎回長いPrompt
↓
探索量が多い
↓
ルールを推測
↓
不要Contextを読みやすい

Harnessあり
↓
短いMap
↓
必要なRule/Skill/Documentへ誘導
↓
探索範囲を限定
↓
軽量Modelでも成功可能な領域が増える可能性
```

ただし、複数Agent・長時間Run・追加Reviewを増やせば総Tokenは増える場合がある。

評価軸はToken単独ではなく、

```text
Quality
× Lead Time
× Human Time
× Token
× Cost
× Retry
```

で見る。

---

# Part D. Harness Lifecycle / Knowledge / Education
