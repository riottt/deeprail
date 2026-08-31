# DR-M08 — 開発手法別 AI駆動適用ガイド

> Status: **canonical v0.16.8**> Creator / Lead Author: **RIO AMADA**

共通Lifecycleの責務は維持し、Methodに応じて工程の束ね方・Gate・Evidenceを変える。

---

## 12.1 Agile

```text
Epic
↓
Feature
↓
Issue
↓
Issue単位Lifecycle
↓
PR
↓
Reinvest / Learn
↓
次Issue
```

特徴：

- 小さな単位で反復
- Living Documentを頻繁に更新
- Issueは価値・振る舞い単位を中心に切る
- 並列Agentとの相性を考慮
- Sprint/Kanbanの周期へ合わせる

---

## 12.2 Waterfall

```text
要求
↓ Gate
要件
↓ Gate
設計
↓ Gate
実装
↓
試験
↓ Gate
Reinvest / Learn
```

特徴：

- 工程Gateを明示
- 成果物承認を強くする
- Issueを工程・成果物単位で管理する場合がある
- Traceabilityを強化
- AIに任せても工程の目的は消さない

---

## 12.3 Hybrid

企業開発では有力な適用方式。

```text
上流
Waterfall型
要求・基本設計をFormal Gate

        ↓

実装
Agile型
Feature / Issue単位で高速反復

        ↓

統合・Release
Waterfall型
Formal Test / Release Gate

        ↓

Reinvest / Learn
正本統合
```

---

## 12.4 開発手法 × 規模

運用は一軸では決めない。

```text
             Agile   Waterfall   Hybrid
Small        Light      Light      Light
Medium       Std        Std        Std
Large        Full       Full       Full
```

同じ「中規模」でもIssue分割やGate配置は異なる。

---
