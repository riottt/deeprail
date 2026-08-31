# DR-M07 — 規模判定・Work Item分割ルール

> Status: **canonical v0.16.8**> Creator / Lead Author: **RIO AMADA**

本章は、人間がEpic / Feature / Issue / Taskを手作業で完全分割するための手順書ではない。

AIの能力とAutonomyが十分なら、**Work BreakdownそのものをAIが生成・再分割してよい**。

人間の責務は、

```text
Objective
Constraint
Risk
Non-goal
Acceptance
Decision Boundary
```

を明確にし、必要な粒度でAIが生成したWork Structureを評価・承認することへ移る。

本章では、次の基準で仕事を分ける。

> **人間向けの設計観点であると同時に、AIが自律的にWorkを分解・再構成するためのEvaluation Rubricである。**

---

## 11.1 規模判定

### 小規模

- 単一機能内
- API Contract変更なし
- DB Schema変更なし
- 他チーム影響なし
- Rollback容易
- 影響範囲が明確

### 中規模

- 複数コンポーネント
- APIまたはDBの限定的変更
- 複数ファイル / 複数Layer
- 一定の設計検討が必要
- Issue単位で管理可能

### 大規模

- 複数Repository
- Architecture変更
- DB Migration
- 外部IF変更
- 複数チーム影響
- Security影響
- 長期間・複数Issue
- Release計画が必要

---

## 11.2 規模 × Development Lifecycle

| 項目 | 小規模 | 中規模 | 大規模 |
|---|---|---|---|
| Lifecycle Responsibility | Lightweight | Standard | Full |
| 要件文書 | Issueで代替可 | 差分中心 | 正式成果物 |
| 設計 | 局所差分 | Design Delta | Formal Design |
| Human Gate | 少 | 標準 | 多 |
| Test | 局所 | 機能 | 統合含む |
| Reinvest / Learn | 影響箇所のみ | 関連正本 | 正本一式 |
| Work Item | Issue | Issue + Task | Epic + Issue |

小規模だからReinvest / Learn責務を消すのではない。

「更新対象・再投資対象がないことを確認して終了」もReinvest / Learnの有効な結果とする。

---

## 11.3 DeepRail Work Model

Work Itemは次の論理モデルで扱う。

```text
Business Objective / Outcome
        ↓
Initiative / Epic
        ↓
Feature / Capability
        ↓
Issue / Work Item
        ↓
Execution Task
        ↓
Agent Task
```

これはWork Management等の製品固有階層を強制するものではない。

各Toolでは名称・階層が異なってもよい。
揃えたいのは、名前より**意味と責務境界**だ。

| Level | 意味 | 主なOwner | 完了判断 |
|---|---|---|---|
| Objective / Outcome | 何を達成したいか | Business / Product | Outcomeが観測できる |
| Epic | 大きな変化・投資単位 | Epic Owner | Epic Outcomeを満たす |
| Feature | 利用可能な能力・価値 | Feature Owner | Feature Acceptance |
| Issue | 独立して完了判定できる変更 | Issue Owner | Evidence + Gate |
| Task | Issue内部の作業 | Human / AI | Task Output |
| Agent Task | AIへ渡す実行契約 | AI Runtime | Output Contract |

PR / MRはWork Item階層ではなく、Source変更の統合単位である。

---

## 11.4 Work Decompositionの基本思想

従来型：

```text
Human
↓
Epic分割
↓
Feature分割
↓
Issue分割
↓
Task分割
↓
Developerへ配布
```

AI Native：

```text
Human
├ Objective
├ Constraint
├ Risk
├ Non-goal
├ Acceptance
└ Decision Boundary
        ↓
AI
├ Epic候補
├ Feature候補
├ Issue候補
├ Dependency
├ Parallelization Plan
└ Agent Task
        ↓
Machine / AI Evaluation
        ↓
必要な箇所だけHuman Decision
        ↓
Execution
```

人間がWork Breakdown Structureを最初から完成させることをDeepRailの前提にしない。

---

## 11.5 Epic切り出しRubric

Epicは「大量のIssueを入れる箱」ではない。

**独立したOutcome・投資・責任・Riskを持つ大きな変化単位**とする。

AIがEpic候補を生成するとき、最低限次の観点を評価する。

| 観点 | 判定する問い |
|---|---|
| Outcome | 独立したBusiness / User Outcomeを持つか |
| Boundary | 他Epicと責務・目的境界が明確か |
| Acceptance | Epic単独で完了を判定できるか |
| Ownership | 意思決定Ownerを明示できるか |
| Dependency | 他Epicへの依存が過剰でないか |
| Architecture | 不自然に複数Architecture境界を横断していないか |
| Risk | 高Risk変更を独立して統制できるか |
| Reversibility | 独立して停止・縮退・Rollbackできるか |
| Context | 下位WorkをAIが扱えるContextへ分解できるか |
| Parallelism | 他Epic / Featureと、独立したExecution / Evidence / Retry / Rollback単位として安全に並列化できるか |
| Source of Truth | 更新する正本・責務範囲が明確か |
| Human Gate | 重要な人間判断境界を明示できるか |
| Evidence | Outcomeを独立したEvidenceで証明できるか |

### 11.5.1 Verifiable Parallelism

「複数Agentを起動できる」だけでは、Parallelismの成立条件を満たさない。
Workが次を満たすほど、Parallel Executionへ倒しやすい。

```text
Outcome Independence
Acceptance Independence
Context Sufficiency
State / Workspace Isolation
Independent Evidence
Failure Localization
Retry Independence
Rollback / Reversibility
Integration Boundary
```

特に、各Workが同じSource / Environment / Mutable Stateへ競合し、片方のFailureが他方のEvidenceを壊す場合は、Agent数を増やしても安全なParallelismとは扱わない。

```text
Agentを増やす
≠
Parallelismが上がる

Workを独立して実行・証明・回復できる
→
Parallelismを安全に上げられる
```

並列化できない場合は、Work再分解・Workspace分離・State分離・Acceptance再定義・Integration Gate追加を先に検討する。

### 11.5.1-A Parallel Fit — 「並列化できる」と「並列化する価値がある」を分ける

Verifiable Parallelismの条件を満たしても、必ずParallel Executionへ倒すわけではない。並列化の判断では、次も見る。

```text
Value of Earlier Completion
Work Independence
Coordination Cost
Evaluation Cost
Compute / Token Cost
Integration Cost
Failure Localization Cost
Human Attention Cost
```

```text
Parallelizable = 独立して実行・証明・回復できる
Worth Parallelizing = その独立性を作るCostを払っても、早く終わる価値が上回る
```

依存が密で頻繁な同期が必要なWork、同じContextを常時共有しなければならないWork、評価Costが実装Costを上回るWorkは、Agentを追加できてもSequential / Staged Executionの方がよい場合がある。

> **並列化は能力ではなく投資判断でもある。起動Costが低いことと、Coordination Costが低いことを混同しない。**

### 11.5.1.1 Why — なぜParallelismはAgent数ではなくVerifiabilityで決まるのか

Agentを十個立ち上げれば、仕事が十倍進む。

そう見える瞬間はある。画面には十個の実行が並び、同時にCodeが増えていく。人間一人で順番に作業するより、明らかに速い。

しかし、並列化の本当のコストは最後に出る。

FlowDeskで、Frontend、Backend、DB Migration、監査Log、Testを別々のAgentへ渡したとする。五つが同時に進んだ。ところがBackend Agentが代理承認のStateを変更し、DB Agentも同じSchemaを変更した。Frontendは古いResponse Shapeを前提に実装し、Test Agentは片方のBranchだけを見てGreenを出した。

五つのAgentは働いている。仕事は、前に進んでいない。

むしろ最後にIntegrationする人間が、五つの変更をほどく仕事を背負っている。

このSceneで詰まった理由は、Agentの性能より仕事の切り方にある。**並列にした仕事同士が、独立して完了を証明できる単位になっていなかった。**

```text
実行の独立性
片方が進んでも他方のStateを壊さない

判定の独立性
それぞれのAcceptanceを別々に確認できる

失敗の独立性
片方が落ちても原因と影響を局所化できる

回復の独立性
片方だけRetry / Rollbackできる
```

Agent数は最初に決める数字ではない。まずWorkを切る。SourceやWorkspaceを分ける。Mutable Stateを共有しすぎない。Acceptanceを明確にする。EvidenceをWorkごとに成立させる。Integration Boundaryを決める。そこで初めて、「これは同時に走らせてもよい」と言える。

逆に、この条件を満たさない仕事を無理に並列化すると、Local Throughputは上がってもSystem Throughputが落ちる。生成されたArtifactの数だけを見ると速く見えるため、発見が遅れる。

AIではAgentを追加するCostが低いため、この問題がさらに見えにくい。起動するCostが低いことと、統合するCostが低いことは別である。

FlowDeskの五つのWorkを本当に並列化したいなら、「Audit Logの契約を先に固定する」「API ContractをSource of Truthへ置く」「DB Migrationを独立したRelease / Rollback単位にする」「FrontendはContract Testで検証する」といった準備が要る。

それができれば、それぞれが自分のEvidenceを持ち、Integration時には境界だけを確認できる。

> **並列性は、同時に何個動かせるかではない。同時に動かしても、別々に正しさと失敗を扱えるかで決まる。**

Agentを増やす前に、仕事を分ける。この順番を忘れないために、Verifiable Parallelismという名前を付けている。

### Epicを分ける方向へ倒す条件

次のいずれかが強い場合、AIはEpic分割を提案する。

```text
Outcomeが複数存在する
Ownerが異なる
Risk Classが大きく異なる
Architecture境界が独立している
Release / Rollback単位が異なる
Business Decisionが独立している
依存なしで別時期に実行できる
Evidenceが別々に成立する
```

### Epicを分けすぎない条件

次の場合は別Epic化を避ける。

```text
単なるFrontend / Backend分離
単なる担当Team分離
同一Outcomeを技術Layerだけで分ける
常に同時Releaseが必要
Acceptanceが一体
分割によりCoordination Costだけ増える
```

技術構成をそのままBusiness Work Structureへ写像しない。

---

## 11.6 Epic Contract

Epicは最低限次を持つ。

```yaml
epic:
  objective:
  expected_outcome:
  owner:
  scope:
  non_goals:
  business_context:
  affected_capabilities:
  affected_systems:
  constraints:
  risk:
  success_metrics:
  dependencies:
  decision_points:
  target_operating_context:
  completion_evidence:
```

AIは不明な項目を推測で確定せず、Unknown / Questionとして残す。

---

## 11.7 Feature切り出しRubric

Featureは「実装Component」ではなく、原則として**利用可能なCapability / Behavior**として切る。

良い例：

```text
Epic: 契約手続きをオンライン化する

Feature A: 契約申請ができる
Feature B: 承認できる
Feature C: 進捗確認できる
```

避けたい例：

```text
Feature A: Frontend
Feature B: Backend
Feature C: Database
```

ただしArchitecture移行等、技術Capability自体がOutcomeの場合は技術軸のFeatureを認める。

Feature判定観点：

- 利用可能な能力として説明できる
- Acceptanceを独立して定義できる
- 下位Issueへ分割できる
- OutcomeとのTraceabilityがある
- 他Featureとの依存が説明可能
- Release / Feature Flag等で独立検証できる

---

## 11.8 Issue切り出しRubric

IssueはAI駆動実行の中心単位である。

良いIssueは概ね次を満たす。

```text
Independent Acceptance
× Testability
× Reviewability
× Context Fit
× Low Conflict
× Clear Source of Truth
× Evidenceability
```

判断観点：

- 独立した完了条件があるか
- Test可能か
- Review可能か
- Context量が過大でないか
- 他Issueとの競合が強すぎないか
- Source of Truthが特定できるか
- Required Evidenceが定義できるか
- PR / Patchとして妥当な差分になるか
- Failure時の差し戻し先が分かるか

AI駆動では「1 Issue = 1 Agent Session」に固定しない。

IssueはProduct / Project管理上の単位であり、
AI Runtime上は必要に応じて複数Agent Taskへ再分割できる。

---

## 11.9 Agent Task切り出しRubric

Agent TaskはAIへ渡す**最小の実行契約**である。

```text
Agent Task
=
One Clear Objective
+
Bounded Context
+
Bounded Permission
+
Explicit Output Contract
+
Verification
+
Stop / Escalation Condition
```

推奨条件：

- 1つの明確な目的
- 必要Contextを列挙できる
- 原則として1 fresh contextで扱える範囲
- Tool / Permission範囲が明確
- 出力形式が明確
- 完了確認方法がある
- 不明時の停止条件がある
- 他Agent Taskとの書込競合が管理できる

Agent TaskはWork Management等へ必ず登録する必要はない。
Runtime内部の一時的なExecution Unitでもよい。

---

## 11.10 AIによる自律分解Flow

```text
Objective / Epic
      ↓
AI Decomposition
      ↓
Feature候補
      ↓
Rubric Evaluation
      ↓
Issue候補
      ↓
Dependency / Risk / Context Analysis
      ↓
Agent Task候補
      ↓
Execution
      ↓
Context Overflow / New Finding / Failure
      ↓
Re-decomposition
      ↺
```

AIは実行途中でもWork Structureを再構成してよい。

Work Breakdownは静的な計画書ではなく、
**Evidenceと新しいContextで何度も更新されるLiving Structure**にする。

---

## 11.11 再分割Trigger

次の場合、AIはWork Itemの再分割を検討する。

- Contextがfresh windowを超える
- Acceptance Criteriaが複数の独立結果へ分裂した
- 予期しないArchitecture境界が判明した
- Riskが想定より高い領域を発見した
- Agent間の書込競合が増えた
- Test / Review単位として大きすぎる
- 別OwnerのDecisionが必要になった
- Environment / External Dependencyで独立待ちが発生した
- 変更範囲が宣言Scopeを超えた

再分割によってObjectiveやAcceptanceを変更する場合は、
ただTaskを割り直したことにはしない。Requirement Changeとして記録する。

---

## 11.12 Dependency Model

Dependencyを単なる「blocks」リンクで終わらせない。

最低限次を区別できるようにする。

```text
Data Dependency
Architecture Dependency
Decision Dependency
Environment Dependency
External Dependency
Human Approval Dependency
Release Dependency
Source-of-Truth Dependency
```

AIはDependency Graphを使って、

- 実行順
- 並列化可能性
- Human Gate
- Environment準備
- Escalation先

を判断する。

---

## 11.13 Work DecompositionとAutonomy

Work分割の自律度をA0〜A5へ接続する。

| Autonomy | Work Decomposition |
|---|---|
| A0 | AIは分割案を提案するだけ |
| A1 | HumanがIssue / Task分割を確認 |
| A2 | AIがIssue内部をTask / Agent Taskへ自律分割 |
| A3 | AIがFeatureからIssueを生成・再分割 |
| A4 | AIがEpicからFeature / Issue構造を生成。HumanはEpic Outcome / Risk / Exception中心 |
| A5 | AIがPortfolio / InitiativeからEpic候補まで生成。HumanはStrategy / Investment / Exception中心 |

Autonomyが上がるほど人間が見る粒度は上位へ移る。

```text
A0-A1
Human → Issue / Task

A2-A3
Human → Feature / Boundary

A4
Human → Epic Outcome / Risk

A5
Human → Strategy / Portfolio / Investment
```

AIが賢くなるほど、人間の価値を「細かく分割する能力」に固定しない。

---

## 11.14 Decomposition Gate

高Risk / 高影響のWorkではAI分割を無条件採用しない。

Humanが確認する主なポイント：

```text
Outcome
Scope Boundary
Non-goal
Architecture
Security / Compliance
Irreversible Decision
Cross-team Dependency
Investment
Acceptance
```

一方、低RiskかつEvaluation可能な下位分割はAIへ委譲できる。

---

## 11.15 ToolへのMapping

DeepRail Work Modelは特定製品に依存しない。

例：

```text
DeepRail      Work Management / SCM Platform等
Epic       → Epic / Initiative / Parent
Feature    → Feature / Story / Parent Issue
Issue      → Issue / Work Item / Story
Task       → Task / Subtask
Agent Task → Runtime内部Execution Unit
```

Toolの階層制約に合わせてMappingしてよい。

ただし論理的なTraceability：

```text
Objective
→ Epic
→ Feature
→ Issue
→ Evidence
→ Outcome
```

は維持する。

---
