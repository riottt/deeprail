# DR-M24 — 要求供給・受入運用ガイド

> Status: **canonical v0.16.8**> Creator / Lead Author: **RIO AMADA**

**レイヤ:** Organization ↔ Operating Model ↔ Engineering  
**主な読者:** Product / Business / PM / PO / Engineering Lead / Architect  
**目的:** Business Intentを、EngineeringがAIとともに実行・検証可能なDemandへ変換し、完成物を受け入れるまでのInterfaceを標準化する。

M24は単なる「要件定義の書き方」ではない。
OrganizationとEngineeringの間にある**Demand / Acceptance Contract**を扱う。

## M24.1 Demand Flow

```text
Business Intent
↓
Outcome
↓
Demand
↓
Requirement / Constraint
↓
Acceptance Criteria
↓
Unknown / Assumption
↓
Alignment
↓
Engineering
↓
Acceptance
↓
Feedback
```

## M24.2 Demand Contract

最低限次を持つ。

```yaml
demand:
  intent:
  expected_outcome:
  scope:
  non_goals:
  constraints:
  acceptance_criteria:
  unknowns:
  assumptions:
  risk:
  primary_consumer:
  failure_detectability:
  decision_owner:
  acceptance_owner:
  change_path:
```

未定事項を推測で埋めない。

## M24.3 Acceptance Criteria

Acceptance Criteriaは「実装方法」ではなく、期待する観測可能な結果を書く。

悪い例：

```text
Reactでダイアログを作る
```

良い例：

```text
ユーザーが操作Xを行ったとき、
条件Yでは状態Zが画面上で確認できる
```

## M24.4 Unwritten Expectation

すべての期待値を完全に文書化できるとは仮定しない。

暗黙仕様への対応は明示的に選ぶ。

```text
1. Explicit
   → 文書化する

2. Visualize
   → Mock / Prototype / Exampleで先に固定する

3. Human Catch
   → Human Acceptance Testを正式な検出工程として置く

4. Standardize
   → UI / Domain / Architecture Standardへ昇格する
```

暗黙仕様を放置することと、意図的にHuman Catchへ委ねることを区別する。

## M24.5 Pre-implementation Alignment

実装前に、

- 未確定Decision
- Domain terminology
- Acceptance Criteria
- Visual expectation
- Constraint
- Non-goal
- Risk
- Testability

を確認する。

質問SkillやInterview Toolは実装手段の一つであり、DeepRail Coreには依存させない。

## M24.6 Business / Product Gate

上流のHuman Gateには、EngineeringだけでなくDemand Ownerが参加する。

EngineeringがBusiness Intentを推測して確定しない。

## M24.7 Requirement Change

変更は会話だけで差し込まない。

```text
Change Request
↓
Impact
↓
Affected Requirement / Decision / Test
↓
Re-approval
↓
Work Item update
```

変更履歴をTraceabilityへ接続する。

## M24.8 Acceptance

Acceptanceは「テストがgreen」だけで終了しない。

必要に応じて、

```text
Machine Check
+
Observed Behavior
+
Human Acceptance
```

を組み合わせる。

## M24.9 Requirement Quality Metrics

例：

- Acceptance Criteria completeness
- Unknowns resolved before Build
- Requirement change rate
- implicit-expectation rework rate
- acceptance rejection rate
- requirement surprise found during Review
- business-side waiting time
- engineering clarification loops

これらを「要件担当者の人事評価」へ直結させない。
目的はSystem Improvementである。

## M24.10 Learning Back

Acceptanceで発見された暗黙期待・判断・制約は、

```text
Current Work Fix
+
Future Prevention
```

に分ける。

再発性がある場合は、Requirement Template / Domain Rule / Design Standard / Test / Living Documentへ還元する。

---
