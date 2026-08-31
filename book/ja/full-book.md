# DeepRail — AIネイティブ組織・開発標準

**Creator / Lead Author: RIO AMADA**

このFull Bookは、DeepRailを問題・思想・実務・開発・Harness・組織まで一続きで読むための統合読書版です。

正確な規範は `standard/`、実行可能な手順は `workflows/`、導入方法は `docs/` を参照してください。

## 目次

- [Chapter 01. DeepRailとは何か — AIが働く組織を設計する](chapters/ch01.md)
- [Chapter 02. AIは「ツール」から「実行主体」へ変わる](chapters/ch02.md)
- [Chapter 03. 人間とAIの役割境界は固定されない](chapters/ch03.md)
- [Chapter 04. なぜAI導入は経営戦略になるのか](chapters/ch04.md)
- [Chapter 05. AIと働く人間の心構え](chapters/ch05.md)
- [Chapter 06. 強い会社と強いHarnessはなぜ似るのか](chapters/ch06.md)
- [Chapter 07. AI Native OrganizationのOperating Model](chapters/ch07.md)
- [Chapter 08. 自分たちの現在地を知る — GreenfieldからLegacyまで](chapters/ch08.md)
- [Chapter 09. AI導入を阻む制約を可視化する](chapters/ch09.md)
- [Chapter 10. 経営・Security・IT・現場をどう動かすか](chapters/ch10.md)
- [Chapter 11. Pilotから標準化・全社展開まで](chapters/ch11.md)
- [Chapter 12. AI時代の人材をどう育てるか](chapters/ch12.md)
- [Chapter 13. なぜ最初に一人でEnd-to-End開発を体験するのか](chapters/ch13.md)
- [Chapter 14. 仕事はどこから生まれるのか](chapters/ch14.md)
- [Chapter 15. 顧客・利用者の本当の要求を発見する](chapters/ch15.md)
- [Chapter 16. 曖昧な要求を「見える形」にする](chapters/ch16.md)
- [Chapter 17. 同じものを見て認識を合わせる](chapters/ch17.md)
- [Chapter 18. 何を決め、何をまだ決めないか](chapters/ch18.md)
- [Chapter 19. 合意をAIが実行できる契約へ変える](chapters/ch19.md)
- [Chapter 20. AIに仕事を分解・再分解させる](chapters/ch20.md)
- [Chapter 21. 人間とAIのチームをどう設計するか](chapters/ch21.md)
- [Chapter 22. AI時代のTeam Leadは何をするのか](chapters/ch22.md)
- [Chapter 23. AI Native Teamの会議と意思決定](chapters/ch23.md)
- [Chapter 24. Agent数ではなくFlowを管理する](chapters/ch24.md)
- [Chapter 25. AIにどこまで任せるか](chapters/ch25.md)
- [Chapter 26. AIの成果を人間はどう評価するか](chapters/ch26.md)
- [Chapter 27. AIの評価をどこまで信頼しGO判断を委譲するか](chapters/ch27.md)
- [Chapter 28. AI Nativeな開発Lifecycleをどう設計するか](chapters/ch28.md)
- [Chapter 29. Loop・Retry・Re-plan・Re-decomposition](chapters/ch29.md)
- [Chapter 30. Agile・Waterfall・HybridをAI時代に再設計する](chapters/ch30.md)
- [Chapter 31. 規模・Risk・Autonomy・Operating Contextで適用を変える](chapters/ch31.md)
- [Chapter 32. SCM・Repository・Work Isolation](chapters/ch32.md)
- [Chapter 33. Legacy / Monorepo / Multi-repoをどう扱うか](chapters/ch33.md)
- [Chapter 34. CI/CDはAI駆動開発の背骨である](chapters/ch34.md)
- [Chapter 35. Test・Eval・Quality Gateをどこへ置くか](chapters/ch35.md)
- [Chapter 36. Environment State / Provenanceをどう管理するか](chapters/ch36.md)
- [Chapter 37. Release・Production・Rollback・Observability](chapters/ch37.md)
- [Chapter 38. 成果と学習を次のAIへ戻す](chapters/ch38.md)
- [Chapter 39. AI開発はなぜHarness Engineeringへ進んだのか](chapters/ch39.md)
- [Chapter 40. 優れたHarnessはどう設計するか](chapters/ch40.md)
- [Chapter 41. Context Engineering](chapters/ch41.md)
- [Chapter 42. Rule・Skill・Agent・Hookをどう構成するか](chapters/ch42.md)
- [Chapter 43. Model・Tool・Runtime・Permissionをどう接続するか](chapters/ch43.md)
- [Chapter 44. Harnessをどう評価し、壊さず進化させるか](chapters/ch44.md)
- [Chapter 45. Harness EngineeringからOrganization Engineeringへ](chapters/ch45.md)
- [終章. すべての人が「小さな組織」を率いる時代へ](chapters/ending.md)

---


# Chapter 01. DeepRailとは何か — AIが働く組織を設計する

**Creator / Lead Author: RIO AMADA**

# DeepRailの最上位モデル

DeepRailは、完成したAIネイティブ組織の姿だけを定義する標準ではない。

既存組織・既存案件が、

> **現在どこにいて、どこへ向かい、そのために何を整理し、誰を動かし、何を申請し、どの順番で変えるか**

までを標準の対象とする。

ここまでを一枚にすると、全体像は次のようになる。

```text
CURRENT STATE
現在の組織・案件・制約
        │
        ▼
TRANSFORMATION
AI導入推進・組織移行
        │
        ▼
TARGET OPERATING MODEL
目指す人間×AIの運用モデル
        │
        ▼
┌───────────────────────────────────┐
│             DeepRail CORE          │
│ Principles / Evidence / Axes /     │
│ Maturity / Failure / Traceability  │
└───────────────────────────────────┘
        │
        ├── L1 組織
        ├── L2 運用モデル
        ├── L3 開発標準
        └── L4 実行ハーネス
        │
        ▼
EVIDENCE / EVALUATION
        │
        ▼
BUSINESS / ENGINEERING OUTCOME
        │
        ▼
ORGANIZATIONAL LEARNING
        │
        └──────────────→ 次のTransformation / Strategy
```

DeepRailは、

```text
Where are we now?
↓
Where should we go?
↓
How do we move?
↓
How should the work run?
↓
How do we execute it?
↓
How do we know it worked?
↓
What should change next?
```

を一つの体系として扱う。

---


---

# DeepRailの全体構造

DeepRailが扱う中心テーマは、

> **HumanとAIが混在する組織を、Role・Decision・Context・Authority・Evidence・Evaluation・Feedback Loopによって設計すること。**

Software Developmentは、この構造を最も具体的かつ検証可能に実践できる主要領域である。

```text
                         DeepRail CORE
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
 L1 Organization      L2 Operating Model     L3 Engineering
        │                     │                     │
        └─────────────────────┴──────────┐
                                         ▼
                                 L4 Execution Harness
                                         │
                                         ▼
                                      Evidence
                                         │
                                         ▼
                                     Evaluation
                                         │
                                         ▼
                               Organizational Learning
                                         │
                                         └──────→ Strategy / Standard / Harness
```

## 共通基盤（CORE）

COREは各Layerを横断する共通語彙・不変条件である。

```text
CORE
├ Principles
├ Invariants
├ Evidence Model
├ Axis Model
├ Maturity Model
├ Failure Taxonomy
├ Traceability
└ Exception Model
```

## L1 組織

```text
Strategy
AI Adoption
Organization Design
Human / AI Role
Decision Rights
Governance
Investment / KPI / ROI
Capability
Organizational Learning
```

## L2 運用モデル

```text
Demand / Requirement Supply
Acceptance
Work Decomposition
Human-AI Collaboration
Approval / Delegation
Autonomy
Escalation
Source of Truth
Feedback
Evaluation
```

## L3 開発標準

```text
Requirements
Design
Planning
Build
Review
Test
Release
Maintain
Living Documentation
```

## L4 実行ハーネス

```text
Context
Instructions / Rules
Skills
Agents
Tools / MCP
Hooks / Gates
Runtime / Environment State
Evals
Observability
Enforcement
```

---

# DeepRailの全体ループ

```text
Strategy / Intent
        ↓
Demand / Requirement
        ↓
Operating Model
        ↓
Engineering
        ↓
Execution Harness
        ↓
Evidence
        ↓
Evaluation
        ↓
Business / Engineering Outcome
        ↓
Organizational Learning
        ↓
Strategy / Standard / Harness Update
        ↺
```

上位Intentが下位Executionへ伝わり、下位Evidenceが上位Decisionへ戻ることを要求する。

---

# ハーネス設計から組織設計へ

Development Harnessで使う設計原理の一部は、成立条件を確認したうえでOrganization Designにも使える。

```text
Software Development            Organization
────────────────────────────────────────────────
Requirement                  →  Strategy / Objective
Issue / Backlog              →  Initiative / Portfolio
Architecture Decision        →  Management Decision
Agent                        →  AI Role
Developer                    →  Human Role
Rule                         →  Policy
Skill                        →  Capability
Tool / MCP                   →  Business System
Source of Truth              →  Organizational Knowledge
Quality Gate                 →  Governance / Approval
Observability                →  Management Visibility
Living Document              →  Organizational Memory
Feedback Reinvestment        →  Organizational Learning
Harness                      →  Operating System
```

ただし、すべてを文字通り同型とみなさない。
成果物Evalを人間の業績評価へそのまま移す等、一般化すると有害なMappingは採用しない。

> **Harness Engineeringをマクロ化するとOrganization Engineeringになる。ただし、成立条件を検証して一般化する。**

---

# CORE 30原則

v0.8のMethodology Coreは30原則で構成する。
各原則は `General Rule / Failure Condition / Origin / Evidence Grade` を持つ。

| ID | Principle |
|---|---|
| P-01 | 正本一意 + 投影宣言 |
| P-02 | 入口は地図、重みは外部化する |
| P-03 | 機械Gateと自然言語規約の二段構え |
| P-04 | 失敗時方針は被害半径で非対称に決める |
| P-05 | Escape Hatchは命名・階層化・可視化する |
| P-06 | Guard the Guards |
| P-07 | BlockはReason / Rule / Fix込みで止める |
| P-08 | 証跡には等級がある |
| P-09 | 実装と評価は系統を分離する |
| P-10 | 自己申告不信・再実行主義 |
| P-11 | Failureは分類してから戻す |
| P-12 | 無人Loopを禁止しBreakerを置く |
| P-13 | Consent Scopingと承認鮮度 |
| P-14 | 状態はファイルへ外部化する |
| P-15 | 契約先出しと段階的Gate導入 |
| P-16 | RuleにはOriginを持たせる |
| P-17 | 外部資産はPROVENANCE付きで扱う |
| P-18 | Agent/Skill資産の増殖を統制する |
| P-19 | Routing主体を多段Agent化しすぎない |
| P-20 | InterfaceをMachine-readable Contractで書く |
| P-21 | 判断は上流で使い切る |
| P-22 | 推測で埋めない |
| P-23 | 未実装・未計測・未検証を明示する |
| P-24 | 知見は発生時に正本へ還流する |
| P-25 | 共有はExportでなくRewrite |
| P-26 | 失敗・見送り・却下も第一級成果物 |
| P-27 | 規模適応と不変条件を分離する |
| P-28 | 上限を数値で引く |
| P-29 | Human Attentionを希少な制約資源として設計する |
| P-30 | 独立評価はFailure Modeの相関を下げ、一致をTruthとみなさない |

### CORE Review Principle — Code is not the default Review Interface

Human Attentionは、Raw Artifactを最初から全量読むことではなく、判断に必要なEvidenceへ配分する。

```text
Decision / Outcome
→ Evidence / Risk / Unknowns
→ High-risk Artifact
→ Raw Code / Diff / Log when needed
```

Code Reviewは有効なControlの一つであるが、品質保証そのものと同義ではない。Work ClassごとにFailure Modeを分解し、最も信頼可能なEval / Test / Gate / Human Decisionへ評価責務を配置する。

> **Code is an artifact. Evidence is the interface.**

---

# DeepRailの不変条件

適用規模・Method・Runtimeが変わっても、次を不変条件とする。

> **Work advances only on approved evidence.**

「Approved」は必ずしもS5対面承認を意味しない。
Risk・Autonomy・Approval Strength・Evidence Gradeに応じた有効なGateを通過したことを意味する。

---


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 02. AIは「ツール」から「実行主体」へ変わる

**Creator / Lead Author: RIO AMADA**

# AI時代の人間の役割

AIは、質問に答えるだけのToolから、一定の権限・責務・評価条件を持って仕事を進める側へ入ってくる。
ここでは、その役割を **実行主体（Worker / Operator / Agent）** と呼ぶ。

AIのAutonomyが上がると、人間側に残る仕事も変わっていく。

```text
作業者
↓
Reviewer
↓
Evaluator
↓
Manager
↓
Governor / Executive
```

へ抽象度を上げていく。

人間の仕事は、消えるより先に形を変える。

> **人間のReviewと意思決定は消えるのではなく、より上位のManagement Reviewへ移る。**

成熟したAI Native Operating Modelでは、人間がすべてのTask / Code / Diffを逐次確認することを前提としない。

人間が主に保持するもの：

```text
Strategy
Objective
Priority
Investment
Constraint
Risk Appetite
Decision Rights
Evaluation Function
Exception Judgment
```

AIへ委譲していくもの：

```text
Planning
Work Decomposition
Execution
Coordination
Testing
Review
Documentation
Retry
Continuous Improvement
```

ただし、

```text
AI can execute the work
AI can decompose the work

≠

AI can freely redefine
Strategy / Objective / Risk Appetite
```

である。

---

## Human as Executive Model

```text
Human / Executive Layer
│
├ Strategy
├ Objective
├ Capital / Resource
├ Risk Appetite
├ Policy
├ Evaluation Function
└ Exception Decision
        ↓
AI Operating Organization
│
├ Planning
├ Work Decomposition
├ Execution
├ Coordination
├ Review
├ Testing
├ Documentation
└ Improvement
        ↓
Management Information
│
├ Outcome
├ KPI
├ Risk
├ Exception
├ Unknown
└ Recommendation
        ↓
Human Management Review
```

DeepRailにおけるAI管理とは、AIの作業を逐一監視することではない。

> **組織を管理するのと同じように、目的・権限・評価・報告・例外処理を設計することである。**

---


---

# 5. 01_AI駆動開発 基本方針

## 5.1 HumanとAIの責務境界を固定しない

DeepRailでは、AIを実際に仕事を進める主体まで含めて設計する。
ただし、`AI = Execution / Human = Decision` を永続的な境界として固定しない。

### 現時点での基本Profile

多くの案件では、導入初期は次の分業が安全である。

```text
Human
├ Objective / Outcome
├ Business Priority
├ Risk Appetite
├ High-cost / Irreversible Decision
├ Exception Judgment
└ Accountability

AI
├ Research
├ Planning Draft
├ Work Breakdown Draft
├ Implementation
├ Test / Verification
├ Documentation
├ Review Assistance
└ Repetitive Coordination
```

これは**開始Profile**であり、Human-only領域の永久リストではない。

### Dynamic Responsibility Boundary

AI Capability、Risk、Evidence Reliability、Failure Detectability、Reversibility、Permission、組織上のAccountabilityが変化すれば、責務の配置も変更してよい。

```text
従来Human中心
Planning
Work Decomposition
Review
Evaluation
Coordination
Priority Proposal
Resource Allocation Proposal
Strategy Option Design

        ↓ Capability / Evidence / Controlが成熟

AIへ段階的にDelegation可能
```

DeepRailが守るのはHumanの領域ではなく、**責務移動の安全条件**である。

### Delegation判断

```text
Delegability = f(
  Capability,
  Risk,
  Evidence Reliability,
  Failure Detectability,
  Reversibility,
  Permission Boundary,
  Accountability
)
```

AIができるから任せるのではない。
**失敗を観測でき、止められ、戻せ、Evidenceから評価できるから任せる。**

### 現在のOperating Profileは到達点ではない

導入初期にHuman Gateを厚く持つことと、Humanが永久にそのGateを担当することは同じではない。

現在の分業は、今のAI Capability、Evidence Reliability、Failure Detectability、Reversibility、Permission、Risk、Accountabilityに合わせた開始Profileである。

たとえば、最初はAIが実行し、人間が評価・承認する。評価系が十分にCalibrationされれば、AIが一次評価を担い、人間はDecisionとEvidenceへ集中できる。さらに限定されたWork ClassでFalse AcceptやEscaped Defectを継続的に観測でき、RollbackやAuditも成立するなら、通常のGO判断をAIへ委譲し、人間はSampling / Exceptionへ移れる。

その先でPolicyとRisk Appetiteまで安定すれば、定義済みの範囲ではAIが評価・GO・Retryまで行える。

```text
Human-led
↓
AI-assisted
↓
Delegated Execution
↓
Delegated Evaluation
↓
Audited Autonomy
↓
Policy-Governed Autonomy
```

これは一方向の成熟度競争ではない。Work ClassごとにEvidenceを見て進め、条件が崩れれば戻す。

**DeepRailが固定するのは現在のHuman / AI分業ではなく、責務を移してよい条件である。**

### AIが「人間の領域」へ入るということ

AIは人間の仕事を一つずつ置換するだけではない。
これまで「ここから先は人間」と考えられていた境界自体を継続的に書き換える。

その結果、AI導入は次へ波及する。

```text
Task Automation
↓
Team Design
↓
Management
↓
Role / Headcount / Decision Rights
↓
Organization Structure
↓
Business Strategy / Competitive Advantage
```

AIがPlanning、Evaluation、Coordination、Priorityへ入るほど、話はTool選定の外へ広がる。最後には、人の配置や権限、組織構造、経営戦略まで設計対象になる。


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 03. 人間とAIの役割境界は固定されない

**Creator / Lead Author: RIO AMADA**

# 5. 01_AI駆動開発 基本方針

## 5.1 HumanとAIの責務境界を固定しない

DeepRailでは、AIを実際に仕事を進める主体まで含めて設計する。
ただし、`AI = Execution / Human = Decision` を永続的な境界として固定しない。

### 現時点での基本Profile

多くの案件では、導入初期は次の分業が安全である。

```text
Human
├ Objective / Outcome
├ Business Priority
├ Risk Appetite
├ High-cost / Irreversible Decision
├ Exception Judgment
└ Accountability

AI
├ Research
├ Planning Draft
├ Work Breakdown Draft
├ Implementation
├ Test / Verification
├ Documentation
├ Review Assistance
└ Repetitive Coordination
```

これは**開始Profile**であり、Human-only領域の永久リストではない。

### Dynamic Responsibility Boundary

AI Capability、Risk、Evidence Reliability、Failure Detectability、Reversibility、Permission、組織上のAccountabilityが変化すれば、責務の配置も変更してよい。

```text
従来Human中心
Planning
Work Decomposition
Review
Evaluation
Coordination
Priority Proposal
Resource Allocation Proposal
Strategy Option Design

        ↓ Capability / Evidence / Controlが成熟

AIへ段階的にDelegation可能
```

DeepRailが守るのはHumanの領域ではなく、**責務移動の安全条件**である。

### Delegation判断

```text
Delegability = f(
  Capability,
  Risk,
  Evidence Reliability,
  Failure Detectability,
  Reversibility,
  Permission Boundary,
  Accountability
)
```

AIができるから任せるのではない。
**失敗を観測でき、止められ、戻せ、Evidenceから評価できるから任せる。**

### 現在のOperating Profileは到達点ではない

導入初期にHuman Gateを厚く持つことと、Humanが永久にそのGateを担当することは同じではない。

現在の分業は、今のAI Capability、Evidence Reliability、Failure Detectability、Reversibility、Permission、Risk、Accountabilityに合わせた開始Profileである。

たとえば、最初はAIが実行し、人間が評価・承認する。評価系が十分にCalibrationされれば、AIが一次評価を担い、人間はDecisionとEvidenceへ集中できる。さらに限定されたWork ClassでFalse AcceptやEscaped Defectを継続的に観測でき、RollbackやAuditも成立するなら、通常のGO判断をAIへ委譲し、人間はSampling / Exceptionへ移れる。

その先でPolicyとRisk Appetiteまで安定すれば、定義済みの範囲ではAIが評価・GO・Retryまで行える。

```text
Human-led
↓
AI-assisted
↓
Delegated Execution
↓
Delegated Evaluation
↓
Audited Autonomy
↓
Policy-Governed Autonomy
```

これは一方向の成熟度競争ではない。Work ClassごとにEvidenceを見て進め、条件が崩れれば戻す。

**DeepRailが固定するのは現在のHuman / AI分業ではなく、責務を移してよい条件である。**

### AIが「人間の領域」へ入るということ

AIは人間の仕事を一つずつ置換するだけではない。
これまで「ここから先は人間」と考えられていた境界自体を継続的に書き換える。

その結果、AI導入は次へ波及する。

```text
Task Automation
↓
Team Design
↓
Management
↓
Role / Headcount / Decision Rights
↓
Organization Structure
↓
Business Strategy / Competitive Advantage
```

AIがPlanning、Evaluation、Coordination、Priorityへ入るほど、話はTool選定の外へ広がる。最後には、人の配置や権限、組織構造、経営戦略まで設計対象になる。

## 5.2 基本原則

1. AIの出力を完成品として無条件に扱わない。
2. 実装前に既存仕様・コード・制約を調査させる。
3. 不明な要求をAIの推測だけで確定しない。
4. コード変更とドキュメント変更を分離しない。
5. すべての情報を常時Contextへ載せない。
6. 正本を定義し、AIが参照すべき順序を決める。
7. 繰り返す手順はSkill等へ昇格させる。
8. 強制したい制約は自然言語だけでなく機械的Gateを検討する。
9. AIに与える権限はタスクに必要な範囲に限定する。
10. Harnessの成熟は感覚ではなく評価結果で判断する。

11. 推測は確定情報へ混ぜず、Unknown / Assumption / Confirmation Requiredとして隔離する。
12. 未実装・未計測・未検証を値で埋めない。存在しない値は `null`、未検証の主張はEvidence状態を明示する。

### Trust Architecture — Evidenceを信頼可能にする3層

```text
思想
→ 自己申告をEvidenceにしない

設計
→ Evidence Level / Independent Evaluation / Evaluation Authority / Human Gate

執行
→ CI / Hook / Checker / Permission / Enforcement Ledger

健全性
→ Guard the Guards / Meta-Health
```

「強いRuleを書いた」「Hookを置いた」だけでTrustが成立したとみなさない。

---


---

# 23. 19_AI権限委譲・自律化運用ガイド

この章が、AI駆動チーム開発の長期的な到達点を定める。

---

## 23.1 自律化レベル

| Level | 人間の主な関与 | AIの範囲 |
|---|---|---|
| A0 | 常時監視・分割案確認 | 提案・調査・Work分割案 |
| A1 | 各STEP・Issue構造承認 | 調査・設計案・実装・Test |
| A2 | Issue開始/終了 | Issue内Lifecycle + Task / Agent Task自律分割 |
| A3 | Feature開始/終了 | Feature→Issue分割・再分割・並列Agent・PR |
| A4 | Epic Outcome / Risk / Exception | Epic→Feature / Issue分割・Feature群実行・正本更新 |
| A5 | Strategy / Portfolio / Investment | Initiative→Epic候補・定型領域の継続実行・改善 |

Work Decompositionの自律化はDR-M07のRubricに従う。

AIが分割できることと、AIがObjectiveやBusiness Decisionを自由に変更してよいことは同義ではない。

```text
AI can decompose the work
≠
AI can redefine the goal
```

Autonomyを上げるほど、人間のReview対象は下位Taskから上位Outcome / Risk / Decisionへ移す。

---

## 23.2 Human Gateの減らし方

Human Gateは「ある / ない」の二値ではない。
自律化Level A0〜A5と、各Gateの**承認強度 S1〜S5**は分けて管理する。

| 強度 | 形態 | 定義 |
|---|---|---|
| S5 | 対面同期承認 | 人間が成果物を確認し、その場で承認 |
| S4 | 台帳非同期承認 | 人間が非同期で確認し、承認台帳へ記録 |
| S3 | 非同期リレー承認 | 人間が判断し、AIが正本台帳へ転記。判断記録と転記を照合可能にする |
| S2 | 完了判定委任 | 事前に定義した基準に基づき、指名された人間へ判定を委任 |
| S1 | AI代行承認 | 明示的な委任規程に基づきAIが承認を記録 |

S1/S2を使う場合、委任規程に最低限次を持つ。

```yaml
delegation:
  scope:      # 対象工程・Gate・Work Item
  expiry:     # 期限または失効条件
  audit:      # 誰がどの頻度で事後確認するか
  disclosure: # 代行・委任実績を誰へいつ開示するか
```

承認は対象操作を明示した確認にだけ効力を持つ。
古い成果物への承認を、新しい版へ流用しない。

Gate削減は感覚で行わない。

Human Gateを減らす前に、DR-M17のEvaluation Authority `EA0〜EA4`で対象Work Classの評価権限をCalibrationする。

```text
Work Classを限定
↓
EA1 Shadow Evaluation
Human / AIの判定差を測定
↓
Evaluation Criteria / Evidenceを改善
↓
EA2 AI-First + Human Decision
↓
一定期間、False Accept / Escaped Defect / Overrideを測定
↓
EA3 Audited Autonomy
HumanはSampling / Exceptionへ
↓
Policy・Risk Appetiteまで安定
↓
EA4 Policy-Governed Autonomyを検討
```

Human Gateの削減目的は「人間をゼロにすること」ではない。
**人間のAttentionを、曖昧性・重大Risk・不可逆Decision・法的/組織的Accountabilityへ集中させること**である。

また、Autonomy / Evaluation Authority / Approval Strengthを混同しない。

```text
Execution Autonomy A0〜A5
×
Evaluation Authority EA0〜EA4
×
Approval Strength S1〜S5
```

同じA3でも、評価実績が少ないTeamはEA1、十分なCalibration Evidenceを持つTeamはEA3というProfileが成立する。

### 23.2.0 Gateを評価する主体は段階的に移せる

Human Gateを減らすとき、StepやControl Pointまで一緒に消す必要はない。

変えるのは、誰がEvidenceを集め、誰が評価し、誰がGOを成立させるかである。

```text
Initial
AI Generate / Execute
↓
Human Review
↓
Human Approve

        ↓ Calibration

AI-First
Generation Agent
↓
Review Agent / Automated Eval
↓
Human Decision

        ↓ Bounded Delegation

Audited Autonomy
Agent Execution
↓
Independent Evaluation
↓
通常CaseはAIがGO
└─ Exception / Sampling → Human

        ↓ Policy Stabilization

Policy-Governed Autonomy
Multi-Agent / Agent Execution
↓
Automated Evaluation
↓
Policy Gate
├─ PASS → 自動で次工程へ
├─ RETRY → 定義済み範囲で再実行
└─ EXCEPTION → Human Intervention
```

この移行で、人間の関与は単純に「減る」のではない。
Artifactの逐次確認から、Evaluation Function、Risk Appetite、Policy、重大例外、監査へ比重が移る。

**Human Gateを消しているのではない。Gateを成立させるEvidenceと、判断する主体を変えている。**

### 23.2.1 Why — なぜ「全部確認しない」方が安全になり得るのか

「AIが作ったものは、人間が全部確認する。」

最初は、このルールが一番安全に見える。未知のToolを導入したばかりなら、実際それでいい。何を間違えるか分からない時期にHuman Gateを厚くするのは自然である。

問題は、そのルールを成熟後も変えないことだ。

FlowDeskで、AIが一日に二つの小変更しか作らないなら、人が全部読める。十、二十、五十と増えたらどうなるか。Reviewerは同じ時間で、より多くのDiff、Test、Log、Specificationを見ることになる。

そのとき「全部確認している」という事実と、「全部を十分に判断できている」という事実は一致しない。Queueが伸びる。Reviewが浅くなる。重要度に関係なく同じ深さで見る。最後には承認が形式化する。

Gateは残っている。安全性は落ちている。

「全部確認しない」と言っても、確認を雑にするわけではない。**Failureをいちばん見つけやすい場所へ、確認を分ける。**

Format違反はLintが見る。型の不整合はCompilerが見る。既知のRegressionはTestが見る。代理期間のBoundaryはVerification Procedureが見る。Production WriteはPermissionが止める。

そのうえで、曖昧なRequirement、法的Accountability、不可逆なData Migration、Risk Appetiteの変更は人が見る。

```text
Machine-detectable Failure → Machine Check
Reproducible Behavior → Verification / Eval
High-risk / Ambiguous Decision → Human
Unknown → Escalation
```

こうすると、人のAttentionを全部へ薄く撒かず、本当に判断が必要な場所へ残せる。

Gateの数だけ見ると減っている。それでも、検出できるFailureの種類は増やせる。

FlowDeskのAudit Logを毎回人がCodeで探す代わりに、実際の代理承認を実行し、元Approver IDとProxy Approver IDが記録されることを機械的に検査する。このCheckが安定していれば、人はCompliance Ruleそのものの妥当性へAttentionを使える。

もちろん、Machine Checkを盲信してはいけない。Test自体が間違う。Evaluatorも同じ誤解をする。だからShadow Evaluation、False Accept、Escaped Defect、Evaluator Independence、Samplingが必要になる。

全部を人に見せない設計の方が、実は難しい。

条件を作らずHuman Reviewだけ減らせば、ただ見なくなっただけだ。Machine Check、Evidence、Escalationまで揃えて初めて、Controlの場所を移したと言える。

> **安全とは、人が見た量ではない。必要なFailureが、適切な仕組みで検出される状態である。**

成熟したAI Native Systemでは、「人が全部見ているから安全」ではなく、「何を誰がどう検出するかが設計されているから安全」へ変わっていく。

---

## 23.2-A Decision Rights Delegation Protocol

ここはDecision RightsのOperational Homeである。Ch10で「誰が決めるか」を理解したあと、Human / AI間でその判断をどう移すかを具体化する。

Human Gateを縮めるときは、「チェックを外した」とだけ記録しない。**どのDecisionを、どの条件でAIへ任せられるようになったか**をDelegation Envelopeの変更として残す。

```text
初期
Human Decision Surface = 大
AI Delegation Envelope = 小

成熟
Human Decision Surface = Risk / Exception / Policy中心
AI Delegation Envelope = Planning / Execution / Evaluation / Coordinationへ拡大
```

### Subsidiarity for Human-AI Teams

> **判断は、信頼可能に判断できる最も実行に近い主体へ置く。**

Agent自身で機械検証できるならAgent、独立AI Evaluatorで判定できるならAI Evaluation、組織Risk・曖昧性・Accountabilityが残るならHumanへ上げる。

### Delegation Contract

継続的なDecision Rights委譲には次を必須とする。

```yaml
delegation:
  decision_class:
  scope:
  allowed_actions:
  evidence_required:
  escalation_conditions:
  expiry:
  audit:
  disclosure:
  rollback_or_revoke:
```

`scope: all` のような無限定委譲を標準形にしない。

### S Transition Protocol

承認強度を弱める場合、一度に飛ばさない。

```text
S5
↓ measure
S4
↓ measure
S3
↓ measure
S2 / S1
↓ measure
必要ならGate自体を削除
```

各段で最低限、False Accept / Defect / Override / Approval Wait / Rubber-stamp兆候を観測する。悪化すれば即座に強いSへ戻せることを前提にする。

### Approval Hollowingを監視する

Gateが存在していても、次の兆候があれば実質的な統制が抜けている可能性がある。

- 承認時間が不自然に短い
- 承認Queueが長期滞留する
- 委任記録だけが急増する
- Decision Packetを開かず承認される
- lease / claimが失効したまま放置される
- 例外的な「今回は通す」が常態化する

対策の主手段は承認者を責めることではない。

```text
承認1件あたりの判断コストを下げる
→ self-contained Decision Packet

承認回数そのものを減らす
→ machine-detectable / reversible / low-risk領域を委譲
```

承認帯域が足りない状態を放置すると、遅延だけでなく**Governanceそのものが劣化する。**

### 23.2-A.1 Why — なぜDecision RightsはTool Permissionより重要なのか

「AIに何をさせてよいか」を考えると、まずPermissionの話が出てくる。File Writeを許すか。Terminalを許すか。Productionへ接続してよいか。

もちろんPermissionは要る。危険な操作を技術的に止める仕組みは欠かせない。

ただし、Permissionだけでは仕事の権限は決まらない。

FlowDeskのAgentにDatabase Write権限があるとする。それは「代理承認Ruleを変更してよい」という意味ではない。ProductionへDeployできる権限があっても、「高額申請ではCompliance Approvalを不要にしてよい」という意味ではない。

Tool Permissionが答えるのは、**その操作を実行できるか**。Decision Rightsが答えるのは、**その判断をしてよいか**である。

```text
Permission
Can I do this operation?

Decision Right
Am I authorized to make this decision?
```

人間の会社でも同じである。経理Systemへ入力できる社員が、会社の支払Policyを変更できるわけではない。SCMへMergeできるEngineerが、ProductのRisk Appetiteを一人で変えられるわけではない。

AIではToolが強力なため、この境界が見えにくい。Agentへ広いTool権限を渡すと、できることが増え、そのまま「任せられることも増えた」ように感じる。

仕事を任せるなら、先に仕事側の条件を決める。何のDecision Classか。Scopeはどこまでか。どんなEvidenceが要るか。どのRiskまで自分で進めてよいか。どこでHumanへ戻すか。権限はいつ切れるか。

その後で、必要最小限のTool Permissionを与える。

```text
Purpose / Work
↓
Decision Rights
↓
Delegation Contract
↓
Required Tool Permission
↓
Execution
```

逆に、Tool Permissionから設計すると「使えるから使う」が起きる。

同じAgentが技術的には全部できても、Decision Rightsは別々に持たせられる。ここに自律化の余地が生まれる。

Permissionを狭くしすぎればAIは働けない。広げすぎれば危険になる。そこで、**Decision Rightsを先に絞り、その判断を実行するために必要なPermissionだけを十分に渡す。**

そしてDecision Rightsは固定ではない。Shadow Evaluationで判定精度を測り、Evidenceが安定し、失敗が検出可能で、RollbackできるならScopeを広げられる。逆にIncidentが出れば縮められる。

> **AI自律化の核心は、どのToolを使わせるかではない。どの判断を、どの条件で任せるかである。**

PermissionはExecution Controlの話で、Decision RightsはOperating Modelの話だ。似て見えても、決めているものが違う。

## 23.3 人間の仕事の変化 — ただし到達点を固定しない

AI Native化の初期には、AIがExecutionを多く担うことで、人間のAttentionはより高い抽象度の判断へ移りやすい。

### 初期

```text
人間
├ 調査確認
├ 設計確認
├ 実装確認
├ Test確認
├ PR確認
└ Document確認
```

### Harness / Evalが成熟したProfile

```text
人間
├ Outcome
├ 優先順位
├ 制約
├ Risk
├ Architecture Boundary
├ 例外
├ 投資判断
└ Harness Performance

AI
├ Planning
├ Decomposition
├ Execution
├ Coordination
├ Verification
├ Review Assistance
└ Improvement Proposal
```

人間を「AIの操作員」にしない。
Harnessが成熟するほど、人間は細粒度作業から離れやすい。

しかし、DeepRailはここをHumanの最終到達点とは定義しない。
AIの能力向上によって、Priority Proposal、Resource Allocation、Policy Draft、Strategy Option Design等もAIへ移り得る。

> **AI時代に固定されたHuman-only Work Listはない。あるのは、その時点での責任配置と、責任を移す条件である。**

---

### Reviewの抽象度は上がるが、それ自体も固定しない

AI Native化によって人間のReviewが消えるわけではない。
導入初期〜中期では、

```text
Artifact Review
↓
Decision Review
↓
Management Review
↓
Governance Review
```

へ抽象度が上がることが多い。

成熟したTeamでは、人間は主に、

```text
Outcome
Risk
Architecture Boundary
Exception
Investment
Irreversible Decision
Policy Change
```

をReviewする。

ただし、AIがこれらの分析・比較・一部判断を担えるようになればHuman Gateの配置も再評価する。
Human Gateは聖域ではなく、**Evidence / Risk / Accountabilityに応じて移動するControl Point**である。

---

### 現時点のHuman Accountability Profile

```text
Human Accountability
= Strategy / Objectiveの最終責任
+ Risk Appetite
+ Decision Rights設計
+ Evaluation Function設計
+ Exception Judgment
+ 法的・組織的Accountability
```

これは「人間しか戦略を考えられない」という能力主張ではない。
組織が現時点で誰にAccountabilityを置くかという**Governance上のProfile**である。

## 23.4 自律化に伴いReview対象も変える

自律化とは「人間が何も見なくなる」ことではない。

```text
A0-A1
Human:
- Plan
- Code
- Test
- PR
を細かく確認

A2
Human:
- Issue Plan
- High-risk Diff
- Test Evidence
を確認

A3
Human:
- Feature Decision
- Cross-Issue整合
- Exception
を確認

A4+
Human:
- Epic Outcome
- Risk
- Architecture
- Harness Metrics
- Escalation
を確認
```

Reviewの対象を成果物の量からDecision/Evidenceへ移す。

その前提条件：

- Specが明示
- Traceabilityあり
- Testが強い
- Standardsが機械/AIで確認可能
- Review Packetが生成可能
- Evalが安定
- Risk Classificationが機能

これらが不足したままHuman Reviewだけを外してはならない。

---

# 第VI部補遺 v0.8新設仕様 — 組織・実行環境・強制と観測

> v0.8から `DR-M20`〜`DR-M24` を正式なManual IDとして追加する。
> Manual IDは安定識別子として扱い、章番号とは分離する。


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 04. なぜAI導入は経営戦略になるのか

**Creator / Lead Author: RIO AMADA**

# Transformation Profile

AI導入方法は、案件が「新しいか古いか」だけでは決まらない。

導入開始点は、最低限次の3軸で判定する。

## T-1 Project / System State

```text
P0 Greenfield
新規案件。設計・Toolchain・Processを最初から選択可能。

P1 Modern Brownfield
既存案件だがGit / CI/CD / Cloud / modern framework等が比較的新しい。

P2 Constrained Brownfield
開発環境は比較的新しいが、Security / Network / Data / Procurement / 社内規程等によりAI利用が強く制約される。

P3 Legacy
Centralized VCS / Legacy Work Management / Windows / 閉域 / 共有試験環境 / 手動承認 / 長期Waterfall等、Toolchain・Process双方の制約が大きい。
```

## T-2 AI Availability

```text
AI-0
AI利用不可

AI-1
個人・限定検証のみ

AI-2
承認済みToolのみ利用可能

AI-3
Team共通利用可能

AI-4
Harness / Agent / MCP / Evalまで組織管理可能
```

## T-3 Organization Enablement

```text
O0
個人判断・Shadow利用に近い

O1
限定Pilot可能

O2
Team標準あり

O3
部門標準・共通Platformあり

O4
全社Governance / Platform / Supportまで整備
```

導入Profileは、

```text
Transformation Profile
=
Project State
× AI Availability
× Organization Enablement
```

で表す。

例：

```text
P0 × AI-4 × O3
→ 新規AI Native案件として最初から設計可能

P1 × AI-0 × O1
→ Toolより先にSecurity / Procurement / Network / Data審査が主戦場

P3 × AI-1 × O0
→ Legacy制約を維持しつつ、適用可能Workを切り出して小規模Pilot
```

---

# Transformation Method

DeepRailの組織移行は次の順序を基本形とする。

```text
1. Current State Assessment
   現状把握

2. Constraint Discovery
   制約整理

3. Stakeholder / Decision Rights Mapping
   誰を動かし、誰が決め、誰が承認するか

4. Transformation Profile
   現在地判定

5. Target Operating Model
   目指す人間×AIの仕事の流れ

6. Enablement Backlog
   Security / Tool / Account / Network / Rule / Harness / Training等をBacklog化

7. Controlled Pilot
   限定導入

8. Standardization
   Process / Rule / Harness / Evalを標準化

9. Rollout
   Team → 部門 → 組織へ展開

10. Adoption / Learning
    定着・計測・再設計
```

Transformationでは、技術導入だけでなく**組織を動かす仕事そのもの**を管理対象とする。

さらに、Adoptionの最終指標を「何人がAI Toolを使ったか」だけに置かない。組織導入では次を段階的に確認する。

```text
Individual Usage
個人がAIから成果を得られる
        ↓
Delegation
まとまった仕事をAIへ任せられる
        ↓
Team Reproducibility
別メンバーでもContext / Rule / Evidenceを使って再現できる
        ↓
Standardization
実践知をStandard / Harness / Trainingへ還元できる
        ↓
Organizational Capability
複数Teamで継続・監査・改善できる
```

Pilotでは、架空のDemoだけでなく**実務上の意味を持つ小さなTheme**を選ぶ。目的は、特定Toolの操作を覚えることではなく、暗黙前提・Domain Vocabulary・制約・Decision Owner・Acceptanceを表面化し、TeamとしてShared Realityを形成できるかを確かめることにある。

その過程で得た仕様・用語・制約・判断理由はContext Assetとして外部化する。AI Toolの操作経験だけでなく、**前提・役割・次のDecisionをTeamで揃えられたか、別メンバーでも再現できるか**を観測する。

> **個人の成功を横展開するのではない。成功を再現可能にした仕組みを横展開する。**

---


---

# DR-M23. 23_経営・AI導入・成熟度運用ガイド

**レイヤ:** Organization / Management  
**主な読者:** CEO / Founder / CTO / CIO / VPoE / AI・DX推進責任者 / PMO  
**目的:** AI導入をTool導入ではなく、Operating ModelとOrganization Capabilityへの投資として判断する。

## M23.1 Why Adopt

AI導入の目的を最初に固定する。

候補：

- Lead Time
- Quality
- Capacity
- Cost
- Innovation
- Knowledge leverage
- Business responsiveness

「AIを使うこと」自体を目的にしない。

## M23.2 Where to Start

Pilot候補は、

```text
Business value
× Repeatability
× Observability
× Reversibility
× Risk
× Available context
```

で選ぶ。

最初から最もCriticalな領域へ広げない。

## M23.3 Pilot Contract

Pilot開始前に定義する。

```text
Objective
Scope
Baseline
Evaluation function
Owner
Allowed autonomy
Required gates
Kill criteria
Duration
Expected learning
```

Pilotの目的が「生産性向上」ではなく「Failureを発見すること」である段階も認める。

## M23.4 Investment Model

TCOに含める。

- Model / API
- Tool license
- Platform
- Harness development
- Eval / Test
- Security / Governance
- Training
- Review capacity
- Migration
- Maintenance
- Incident / rollback
- Change management

AIコストと人件費だけを比較しない。

## M23.5 KPI / ROI

局所Coding Speedだけで判断しない。

```text
End-to-end Lead Time
Human Touch Time
Review Time
Queue Time
Rework
Defect
Release Frequency
Incident
Human Intervention
Adoption
Model / Tool Cost
Business Outcome
```

成熟度により主評価関数を変える。

### M23.5-A Local-to-System Translation Check

AI導入後に「Codingが速くなった」「PRが増えた」「本人は速くなったと感じる」というSignalだけで投資判断をしない。局所改善がSystem Outcomeへ届いたかを翻訳して確認する。

```text
Local Signal
Coding Time / Generated Changes / Agent Runs
↓
Flow Translation
Batch Size / Queue Time / Review Time / Integration Cost
↓
Quality Translation
Rework / Escaped Defect / Instability / Rollback
↓
Delivery Outcome
Lead Time / Release Frequency / Recovery
↓
Business Outcome
User Value / Revenue / Cost / Risk / Learning Speed
```

少なくとも次を確認する。

- 生成量の増加でChange Batchが大きくなっていないか
- Review / VerificationへHuman Touch Timeが移っていないか
- Queue / Integration待ちが増えていないか
- Rework / Incident / Rollbackを含めてもLead Timeは改善したか
- 開発者の主観的Speedupと観測値が一致しているか
- Tool世代やWork Classが変わった後もBaselineを更新しているか

> **局所的に速くなったことは、Systemが速くなった証拠ではない。AIの効果はValue Streamを通過した後で判定する。**

## M23.6 Governance

Governanceを禁止事項の集合にしない。

最低限、

```text
Allowed use
Disallowed use
Permission
Approval
Evidence
Audit
Exception
Escalation
Rollback
```

を持つ。

## M23.7 Ownership

「AI推進担当」を置くだけで終わらない。

Standard / Harness / Eval / Risk / Environment / AdoptionのOwnerを明示し、工数とBus Factorを確認する。

## M23.8 Maturity

```text
M0 Exploration
M1 Controlled Adoption
M2 Standardization
M3 Scaled Adoption
M4 Continuous Optimization
```

昇格は熱量ではなくEvidenceで行う。

## M23.8-A Maturityを一つの数字だけで見ない

組織は均等には成熟しない。最低限、次の4軸を独立に評価する。

```text
Governance
Measurement
Reinvestment
Reproducibility
```

例：

```text
Overall M1
Governance       M2
Measurement      M0
Reinvestment     M1
Reproducibility  M0
```

この非対称性から、次に何へ投資すべきかを決める。

### Promotion Evidence Catalog

昇格は「AIをたくさん使っている」ではなく、Evidenceで判断する。

M1候補Evidence例：

- 別メンバー・別環境で同じGolden / Standard Flowを完走できた
- Gate変更時のfixtureが実際に動く
- Failure→Rule / Skill / Evalへの還流記録がある
- Approval / Decision recordが後から追跡できる
- Harness Owner以外が引き継いで運用できた
- S1/S2を使う場合にDelegation Contractが存在する

M2候補Evidence例：

- Enforcementのbaselineがある
- `null` だった重要Metricに正規のWriterが実装された
- Knowledge Reinvestmentが提案だけでなく実際に正本へ到達した
- Eval Owner / Approval Owner等の独立が必要な領域で成立した

カタログを万能Checklistにしない。Operating Context上取得できないEvidenceは理由と代替Evidenceを宣言する。

### Kill Criteria

各Pilot / Maturity Stageへ入る時点で、`continue / change course / stop` の条件を事前に置く。

Explorationで成果が出ないこと自体を即撤退条件にしない。M0では**学習が止まったこと、重大Riskが制御不能なこと、観測不能なこと**を停止条件候補とする。

## M23.9 Scale-out

横展開は完成Harnessのコピーではなく、

> **部品 + 採寸方法 + 組み立て工程**

を移植する。

Operating Contextが違えば、同じHarnessをそのまま配布しない。

## M23.10 Stop / Rollback

停止条件をPilot開始前に定義する。

例：

- Quality degradation
- Risk incident
- Review capacity collapse
- Cost ceiling exceed
- insufficient observability
- unacceptable human intervention
- business outcome absent

## M23.11 Executive Dashboard

M0-M1では、存在しないFlow Metricを捏造しない。

M2以降で、

```text
Flow
Quality
Cost
Risk
Adoption
Enforcement
Business Outcome
```

を段階的に増やす。

---

## 23.8 AI導入が経営戦略になる条件

AI導入は常に経営戦略ではない。
単純な個人支援Toolとして閉じている段階では、局所的な生産性改善として扱える。

しかしAIが次の責務へ入るほど、経営課題へ変わる。

```text
Execution
↓
Planning
↓
Work Decomposition
↓
Evaluation
↓
Coordination
↓
Priority Proposal
↓
Resource Allocation
↓
Organization Design
↓
Strategy Option Design
```

この段階では、経営が判断すべき問いが変わる。

- どのHuman Roleを減らす・変える・再配置するか
- どのDecision RightsをAIへDelegationするか
- AIによってManagement Layerをどう再設計するか
- Human AttentionをどのDecisionへ集中させるか
- AI Capabilityを競争優位へどう変換するか
- AIが模倣しやすい能力と、組織固有の優位をどう分けるか
- Purpose / Risk Appetite / Business PriorityをAI実行へどう伝えるか
- AIによって可能になった新しいOperating Modelをどう事業戦略へ反映するか

> **AIは業務を効率化するだけでなく、「誰が仕事をするか」「誰が決めるか」「何を競争優位にするか」を変えるため、一定の成熟点から経営戦略そのものになる。**

この変化は `Transformation Profile / Maturity / Autonomy / Decision Rights / Evidence` で段階的に追う。


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 05. AIと働く人間の心構え

**Creator / Lead Author: RIO AMADA**

# AI時代の人間の役割

AIは、質問に答えるだけのToolから、一定の権限・責務・評価条件を持って仕事を進める側へ入ってくる。
ここでは、その役割を **実行主体（Worker / Operator / Agent）** と呼ぶ。

AIのAutonomyが上がると、人間側に残る仕事も変わっていく。

```text
作業者
↓
Reviewer
↓
Evaluator
↓
Manager
↓
Governor / Executive
```

へ抽象度を上げていく。

人間の仕事は、消えるより先に形を変える。

> **人間のReviewと意思決定は消えるのではなく、より上位のManagement Reviewへ移る。**

成熟したAI Native Operating Modelでは、人間がすべてのTask / Code / Diffを逐次確認することを前提としない。

人間が主に保持するもの：

```text
Strategy
Objective
Priority
Investment
Constraint
Risk Appetite
Decision Rights
Evaluation Function
Exception Judgment
```

AIへ委譲していくもの：

```text
Planning
Work Decomposition
Execution
Coordination
Testing
Review
Documentation
Retry
Continuous Improvement
```

ただし、

```text
AI can execute the work
AI can decompose the work

≠

AI can freely redefine
Strategy / Objective / Risk Appetite
```

である。

---

## Human as Executive Model

```text
Human / Executive Layer
│
├ Strategy
├ Objective
├ Capital / Resource
├ Risk Appetite
├ Policy
├ Evaluation Function
└ Exception Decision
        ↓
AI Operating Organization
│
├ Planning
├ Work Decomposition
├ Execution
├ Coordination
├ Review
├ Testing
├ Documentation
└ Improvement
        ↓
Management Information
│
├ Outcome
├ KPI
├ Risk
├ Exception
├ Unknown
└ Recommendation
        ↓
Human Management Review
```

DeepRailにおけるAI管理とは、AIの作業を逐一監視することではない。

> **組織を管理するのと同じように、目的・権限・評価・報告・例外処理を設計することである。**

---


---

## 19.6 AI Delegation Literacy — Tool利用の次に育てる能力

AI Literacyは少なくとも二層に分ける。

| Layer | 中心能力 | 典型的な問い |
|---|---|---|
| AI Usage Literacy | Prompt / Context / Toolを使ってAIから成果を得る | どう頼めばよいか |
| AI Delegation Literacy | Objective / Responsibility / Permission / Evidence / Evaluation / Escalationを設計して仕事を任せる | どこまで任せてよいか |

後者は、単なるTool SkillではなくManagement Skillに近い。

学習者が最終的に説明できるべきことは、Promptの工夫より次である。

```text
何をHumanが決めるか
何をAIへ任せるか
AIがどこまで自己評価してよいか
何をEvidenceとするか
どこで自動GOできるか
どこでHumanへ戻すか
どう失敗を検出し、回復するか
```

---

## 19.7 推奨学習形式 — 一人称End-to-End AI Development Lab

AI未経験〜初級者には、Frontendだけ、Backendだけの局所課題より、**Frontend + Backend + DB + Test + CIを一人称で横断する小規模な業務システム開発**を推奨する。

狙いはFull-stack Engineer化ではない。
一人のHumanが複数の専門責務を抱えることで、逐次指示・逐次確認がすぐに限界へ達し、AIへの委譲と仕組み化が必要になる状態を作ることである。

例：

```text
Task / Project Management App

Frontend
- React / Next.js等

Backend
- Node / FastAPI等

DB
- PostgreSQL等

Delivery
- lint
- unit test
- integration test
- build
- staging相当

Functions
- Login / Role
- CRUD
- Status / Assignee
- Comment
- Search / Filter
```

Runtime / Model / Frameworkは固定しない。
DeepRailが学習させたいのはVendor操作ではなくDelegation Designである。

---

## 19.8 開始前に書かせる7つの問い

開発開始前に、参加者は最低限次を記録する。

| 観点 | 問い |
|---|---|
| Outcome | 最終的に何が動けば成功か |
| Human Decision | 自分が必ず判断すべきだと思うものは何か |
| Delegation Candidate | AIへ丸ごと任せられそうなのは何か |
| Acceptance | 「できた」を何で判定するか |
| Evidence | AIの自己申告以外に何を見るか |
| Risk | AIに勝手に行わせたくないことは何か |
| Escalation | どの条件でHumanへ戻すか |

さらに、開始時点の **Human Decision Surface** を描く。

```text
Architecture      → Human
Implementation    → AI
Review            → Human
Test Confirmation → Human
DB Change         → Human
Release           → Human
```

これは終了後の変化を測るBaselineになる。

---

## 19.9 課題の難しさは「難解さ」ではなく「運用上の複雑さ」で作る

Harnessを自然発生させるために、難しいAlgorithmだけを出題してはならない。
それでは強いModelへ一発Promptする競技になり得る。

課題は、**継続してAIを働かせなければ完遂しにくい構造**を持たせる。

| 課題特性 | 自然に必要になる設計 |
|---|---|
| 複数Feature | Work Decomposition / Dependency |
| Front / API / DB横断 | Context / Boundary / Contract |
| Business Ruleが複数 | Rule / Source of Truth |
| 曖昧な要求 | Discover / Align / Human Decision |
| 同種作業の反復 | Skill / Reusable Instruction |
| Regression Risk | Test / Eval / Evidence |
| 危険な操作 | Permission / Gate |
| Environment差 | Provenance / Preflight |
| 長時間・複数Turn | Context Management / Living Document |
| 途中要求変更 | Re-plan / Re-decomposition / Reinvestment |
| Failure注入 | Retry / Recovery / Escalation |

> **「Harnessを作れ」と指示する前に、Harnessがないと辛い仕事を経験させる。**

ただし、学習目的と無関係なInfrastructure不具合で時間を失わせてはならない。
運営者はGolden Pathを事前完走し、教材側Failureと学習者側Failureを切り分ける。

---

## 19.10 段階学習 — Use → Delegate → Evaluate → Remove One Gate → Harness

学習は次の順で進める。

### Phase 0 — Baseline

AIへ任せる前に、Human Decision Surface、Risk、Acceptance、Evidence候補を記録する。

### Phase 1 — AIを使う

細かい依頼から開始し、通常のAI Codingを経験する。

```text
Human Instruction
↓
AI Output
↓
Human Full Check
```

### Phase 2 — AIへ仕事を任せる

Feature単位でObjective / Constraint / Acceptanceを渡し、Plan / Implement / Test / Fixまで任せる。

### Phase 3 — AI自身に評価させる

AIにCompletionを自己申告させるだけではなく、Acceptanceに対するEvaluationとEvidenceを生成させる。
Human評価と比較し、False Accept / False Reject / Unknownを観察する。

### Phase 4 — Human Gateを一つだけ外す

低Risk・機械検証可能・可逆なWork Classを選び、Evidenceが成立した場合だけHuman確認なしで次へ進ませる。

このPhaseで一度「任せても成立した」と実感できるかどうかが、その後の学習速度を大きく左右する。

> **「全部を自分で見なくても、条件を設計すれば成果は成立する」ことを体感する。**

### Phase 5 — FrictionをHarnessへ変える

繰り返し起きたHuman Interventionを分類し、Rule / Context / Skill / Permission / Hook / Eval / Gate / Toolへ還元する。

### Phase 6 — Change / Failure Eventを投入する

後述のイベントを投入し、Harness化した仕組みが変更下でも機能するかを見る。

---


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 06. 強い会社と強いHarnessはなぜ似るのか

**Creator / Lead Author: RIO AMADA**

# DeepRailの全体ループ

```text
Strategy / Intent
        ↓
Demand / Requirement
        ↓
Operating Model
        ↓
Engineering
        ↓
Execution Harness
        ↓
Evidence
        ↓
Evaluation
        ↓
Business / Engineering Outcome
        ↓
Organizational Learning
        ↓
Strategy / Standard / Harness Update
        ↺
```

上位Intentが下位Executionへ伝わり、下位Evidenceが上位Decisionへ戻ることを要求する。

---

# ハーネス設計から組織設計へ

Development Harnessで使う設計原理の一部は、成立条件を確認したうえでOrganization Designにも使える。

```text
Software Development            Organization
────────────────────────────────────────────────
Requirement                  →  Strategy / Objective
Issue / Backlog              →  Initiative / Portfolio
Architecture Decision        →  Management Decision
Agent                        →  AI Role
Developer                    →  Human Role
Rule                         →  Policy
Skill                        →  Capability
Tool / MCP                   →  Business System
Source of Truth              →  Organizational Knowledge
Quality Gate                 →  Governance / Approval
Observability                →  Management Visibility
Living Document              →  Organizational Memory
Feedback Reinvestment        →  Organizational Learning
Harness                      →  Operating System
```

ただし、すべてを文字通り同型とみなさない。
成果物Evalを人間の業績評価へそのまま移す等、一般化すると有害なMappingは採用しない。

> **Harness Engineeringをマクロ化するとOrganization Engineeringになる。ただし、成立条件を検証して一般化する。**

---


---

# 6. 02_ハーネス設計原則

## 6.0 Harness Engineeringはなぜ生まれたのか

Harness Engineeringは、ある日突然発明された一つのTool技法ではない。
AIへ任せる仕事が広がるたび、Promptの外にある問題を一つずつ解いてきた。その積み重ねを追う方が、今の形を理解しやすい。

これは厳密な「唯一の公式年表」ではなく、公開された製品史・技術記事と実務上の設計変化をつなぐ**DeepRailの技術史モデル**である。

### 6.0.1 第1段階 — Prompt Engineering：AIの出力を整える

初期の主な関心は、AIへどう依頼すれば望ましい回答・コードを得られるかだった。

```text
Human
  ↓
Prompt / Instruction / Example / Output Format
  ↓
Model
  ↓
Output
```

ここでの中心問いは、**「どう言えば、より良い出力になるか」**である。
Prompt Engineeringは現在も必要だが、AIが複数Stepを実行するWorkerになると、Promptだけでは設計対象が足りない。

### 6.0.2 第2段階 — Persistent Rules / Repository Context：毎回同じことを言わない

AI IDEが実務へ入ると、利用者は自然に次を求める。

- このRepositoryでは毎回この規約を守ってほしい
- このProjectの構造・Domainを毎回説明したくない
- このFile / Directoryではこの前提を常に使ってほしい
- 同じ注意を毎Session繰り返したくない

```text
毎回Promptで説明
        ↓
Persistent Rule / Repository Context
        ↓
Project固有の挙動を継続的にSteer
```

製品名より、ここで起きた変化を見たい。
**毎回Promptで言い直すのではなく、環境の側に前提を残したくなった。** その要求が、設計対象を少し外へ広げた。

### 6.0.3 第3段階 — Context Engineering：AIの認識状態を設計する

Agentが長い仕事を扱うと、単にInstructionを書くより、**その瞬間に何を知った状態で推論させるか**が重要になる。

違いは、こう考えると分かりやすい。

```text
Prompt Engineering
「どう言うか」

Context Engineering
「何を知った状態で働かせるか」
```

Contextの候補には、Requirement、Code、Architecture、Domain Knowledge、Decision、Environment State、Tool Description、History等がある。
**Contextを多く入れることではなく、正しい情報を正しい時点で必要十分に渡すこと**が目的である。

### 6.0.4 第4段階 — Coding Agent：AIが答える存在から動く存在へ

AIがFileを読み書きし、Terminalを実行し、Testし、Retryするようになると、利用者の問いは変わる。

```text
何を答えさせるか
        ↓
どこまで行動させるか
何を禁止するか
何を自動確認するか
失敗時にどこへ戻すか
いつHumanへEscalateするか
```

この段階で、Rule / Contextだけではなく、**Tool、Permission、Feedback、Retry、Gate**が必要になる。

### 6.0.5 第5段階 — Harness Engineering：GuardrailとEnablementをExecution Systemへ統合する

Harness Engineeringは、AIを単に縛る技術ではない。
実務では二つの欲求が同時に発生する。

```text
CONTROL / GUARDRAIL
├ 禁止事項
├ Permission
├ Hook / Gate
├ CI
├ Human Approval
└ Audit / Evidence

ENABLEMENT
├ Context
├ Source of Truth
├ Skill
├ Tool / MCP
├ Environment
├ Memory / Artifact
├ Retry / Recovery
└ Evaluation / Feedback
```

DeepRailでの定義：

> **Harness Engineeringとは、AIが仕事を安全かつ再現可能に完遂できるよう、Prompt / Contextだけでなく、Tool・Permission・SCM・CI/CD・Environment・Gate・Eval・Evidence・Recovery・Human Decision・Learningまで含む実行系を設計するEngineeringである。**

### 6.0.6 「発明」より、自然発生に近い

名前が定着する前から、現場では似た対策が生まれていた。

同じ注意を何度もするならRuleにしたくなる。危険な操作が怖ければPermissionを絞りたくなる。「できました」だけでは不安なら、TestやEvidenceが欲しくなる。

ここでは、その流れが偶然ではないことだけ押さえる。**仕事を任せて困った場所に、必要な仕組みが生まれる。**

次のWhyでは、FlowDeskを使って、その自然発生を一つの仕事の中で追う。教育で同じ流れをどう体験させるかは人材育成章へ回す。

### 6.0.6.1 Why — なぜHarness Engineeringは自然発生するのか

最初からHarnessの完成形を作ろうとしなくていい。

むしろ多くの場合、先に仕事を任せる。すると困る。困ったところに仕組みが生まれる。

FlowDeskの代理承認を、最初は一つのAgentへそのまま任せたとする。「この要求を実装して、Testまで通して」と依頼する。AgentはRepositoryを読み、Codeを書き、Testも追加する。小さな変更なら、これだけで終わるかもしれない。

ところが仕事を少し広げると、同じやり方では苦しくなる。

「代理」の意味を毎回説明する。監査LogのRuleを毎回説明する。触ってはいけないProduction Dataを毎回注意する。Testが落ちるたびに人が原因を教える。Agentが「できました」と言うたびに、人が別の手段で確かめる。Sessionが変わると、前回の注意が消える。

このあたりから、現場は名前を知らなくても対策を足し始める。

```text
同じ説明を繰り返したくない
→ Rule / Context

必要なSourceを迷わず読ませたい
→ Source of Truth / Retrieval

危険な操作を止めたい
→ Permission / Hook

「できました」だけでは判断できない
→ Test / Evidence / Eval

失敗するたび人が直したくない
→ Feedback / Retry / Recovery

同じFailureを次回も繰り返したくない
→ Reinvestment
```

これらを一つずつ足していくと、いつの間にか「AIへ仕事を成立させる実行環境」ができている。

Harnessは、最初から完成図を描いて作る特殊な装置とは限らない。仕事を任せる範囲が広がるたび、足りない条件が見え、その穴を埋めていった結果として現れることが多い。

だから、Toolから始めると順番を間違えやすい。最初にAgent FrameworkやSkill一覧を決めても、何のFailureを防ぎ、何の仕事を成立させるための仕組みなのかが分からなければ、部品だけが増える。

逆に、仕事から始めれば必要性が見える。

FlowDeskで代理承認を安全に任せたい。では、どの情報が必要か。どこまで操作してよいか。何をもって正しいとするか。失敗したらどこへ戻すか。人に聞くべき判断は何か。次回へ何を残すか。

この問いに一つずつ答えると、Context、Permission、Verification、Gate、Decision、Learningがつながる。

HarnessをDelivery Systemから逆算する理由もここにある。作りたいのは見栄えのするAI機能ではない。**仕事が最後まで成立する条件**だ。

AIへ任せる範囲が狭ければ、Harnessも小さい。任せる範囲が広がれば、設計対象も外へ広がる。

> **委譲を本気で進めると、仕事を成立させる仕組みが必要になる。その仕組みを偶然の工夫で終わらせず、再現可能にしたものがHarness Engineeringである。**

### 6.0.7 設計対象が外側へ広がる

技術の流れを見ると、前の考え方が消えるというより、その外側へ設計対象が広がっている。

```text
Prompt Engineering
AIへの指示を設計する
        ↓
Context Engineering
AIの認識状態を設計する
        ↓
Harness Engineering
AIの行動・環境・検証・回復を設計する
        ↓
Operating Model / Organization Engineering
Human + AIの役割・権限・意思決定・学習を設計する
```

Prompt EngineeringもContext Engineeringも消えない。
**Harness Engineeringの内部で重要な設計領域として残る。**

また、Harness Engineeringを組織へ一般化する際は、Softwareの機械的Gateを人間へそのまま写像するのではなく、成立条件を検証して抽象化する。

### 6.0.8 強いOrganizationと強いHarnessの構造的な類似

強い会社は、優秀な個人だけで成立しない。Purpose・Principle・Role・Authority・Process・Evaluation・Learningを下位の行動へ落とし込むことで、個人の判断を揃え、再現性と自律性を高める。

Harnessでも同じ問題が現れる。

| Organization | Harness / AI Execution System |
|---|---|
| Purpose / Mission | Intent / Objective |
| Values / Principles | Instructions / Rules |
| Organizational Knowledge | Context / Source of Truth |
| Role | Agent / Function |
| Authority | Permission |
| Business Process | Workflow / Skill |
| Approval / Internal Control | Gate / Human Decision |
| Performance / Quality Evaluation | Eval / Evidence |
| Audit / Monitoring | Observability / Trace |
| Training / Organizational Learning | Reinvestment / Rule / Skill Update |

この類似は、AIを人間と同一視するためではない。
**複数の実行主体を目的に沿って自律的かつ再現可能に動かすとき、必要になる設計問題が似る**ことを示している。

### 6.0.8.1 Why — なぜOrganizationとHarnessには似た構造が現れるのか

会社とAI Harnessを同じものとして語るつもりはない。

人には感情があり、関係があり、法的責任があり、組織には文化や権力もある。Agentを社員に見立てれば組織設計が分かる、という単純な比喩をDeepRailは採らない。

それでも、設計図を並べると似たものが出てくる。目的。役割。権限。仕事の流れ。判断基準。例外処理。評価。監査。学習。

似て見える理由は、人間とAIが似ているからではない。**複数の実行主体へ仕事を任せ、中央が一件ずつ指示しなくても全体を目的へ向かわせたい。** その問題が共通している。

小さな会社では、社長が細部まで判断しても回る。社長自身がContextであり、Gateであり、Evaluatorだからだ。人数が増えると、それでは止まる。何を目指すかを共有し、誰が何を決めてよいかを決め、定型業務はProcessへ落とし、重大な例外だけ上げる。

AI Executionでも同じことが起きる。Agentが一つで、人間が横に座って全部見ている間は、Promptと会話だけでも回る。Agentが増え、仕事が長くなり、複数RepositoryやEnvironmentをまたぎ始めると、人が全Stepを直接統制できなくなる。

そこで必要になるのが、Intent、Context、Role、Permission、Workflow、Gate、Evidence、Escalation、Reinvestmentである。

これは「AIを社員として扱え」という話ではない。

> **人が逐次介入しなくても、複数の実行主体が目的に沿って動けるようにすると、組織とHarnessは同じ種類の設計問題へ近づく。**

この見方を持つと、Harnessを単なるDeveloper Toolingとして扱えなくなる。Production操作をAgentへ許す問題は、Tool Permissionだけでは終わらない。誰の方針を根拠に、どのRisk Classまで、どのEvidenceがあれば、その判断を下位へ委譲できるかというDecision Rightsの問題になる。

反対に、Organization側も「AI Toolを導入する」という言い方だけでは足りない。StrategyがどこでWorkへ変わり、何がAIへ渡り、何をEvidenceとして上位判断へ返すのか。そこまで設計しなければ、経営のIntentとAIのExecutionはつながらない。

FlowDeskでも同じだった。代理承認を実装するAgentへ必要なのはCode Conventionだけではない。誰に代理承認を許すのか、監査上何を残すのか、どの例外を人へ戻すのか。その上位RuleがExecutionまで届かなければ、技術的に正しいCodeでもBusinessとしては間違える。

強いHarnessは、AIを賢く見せる仕組みではない。強いOrganizationも、優秀な人を集めただけの状態ではない。どちらも、**目的を下位の行動へ届け、行動のEvidenceを上位の学習へ戻す構造**を持つ。

Harness Engineeringを深く追うと、Organizationの話へ戻ってくる。話を無理に広げたというより、AIへ任せる仕事が広がった結果、最初からつながっていた問題が見えてくる。

### 6.0.9 経営の意思をAI実行まで接続する

AIが高い抽象度の仕事を担うほど、Coding Ruleだけでは足りなくなる。

```text
Coding Standard
↓
Engineering Principle
↓
Product Principle
↓
Risk Appetite
↓
Business Priority
↓
Decision Policy
↓
Strategy / Purpose
```

これらをすべてPromptへ詰め込むのではない。
各層のSource of TruthとDecision Rightsを明確にし、必要なIntentが下位Executionへ伝わり、下位Evidenceが上位Decisionへ戻る構造を作る。

```text
Purpose / Strategy
↓
Objective / Portfolio Decision
↓
Operating Model / Decision Policy
↓
Work Contract / Harness
↓
AI / Human Execution
↓
Evidence / Outcome / Failure
↑
Management Review / Organizational Learning
↑
Strategy Update
```

ここまで到達すると、Harness Engineeringは単なるDeveloper Toolingではなく、**Organization Engineeringを実行可能にする下位レイヤ**になる。

---

## 6.1 Harness設計はDelivery Systemの理解から始める

Harness設計は runtime固有のInstruction File、Prompt、Agent Persona、Skill一覧から始めない。

最初に、**そのチームの変更がどのように作られ、検証され、承認され、本番へ届き、失敗時に戻されるか**を描く。

```text
Demand / Requirement
↓
Specification
↓
Work Item
↓
Source Change
↓
Build
↓
Static Check
↓
Unit / Integration / E2E
↓
Security / Compliance Check
↓
Artifact
↓
Review / Approval
↓
Deploy
↓
Production Verification
↓
Monitoring
↓
Rollback / Incident
↓
Learning
```

このFlowを理解せずにHarnessを設計すると、AIに「何をさせるか」は書けても、次を設計できない。

- どの地点でAIを止めるか
- どの検証を機械へ任せるか
- 何をEvidenceとして次へ進めるか
- どの権限をどのAgentへ渡せるか
- どこでHuman Decisionが必要か
- Environment FailureとImplementation Failureをどう分離するか
- Release / Rollbackをどこまで自律化できるか
- 失敗をRule / Skill / Evalへどう戻すか

**CI/CDはHarnessの後ろに付ける連携先ではない。Harnessを設計する前に見るDelivery Backboneである。**

---

## 6.2 設計時に最初に確認する14項目

| 項目 | 問い |
|---|---|
| Outcome | 何を成立させるためのHarnessか |
| Development Lifecycle | 要求からLearningまで、どの責務・Gateで進むか |
| SCM / Work Isolation | 変更単位と並列作業単位は何か |
| CI/CD | Build / Test / Package / Deployはどこで、何を契機に動くか |
| Test / Eval | 何を機械で検証でき、何を人間が判断するか |
| Environment | Local / Shared / CI / Staging / Productionの状態をどう識別するか |
| Release / Rollback | 本番化と復旧の条件は何か |
| Work Unit | Epic / Feature / Issue / Agent Task / PR等の単位は何か |
| Source of Truth | 要求・仕様・Code・Decisionの正本は何か |
| Human Gate | 人間判断が必要なのはどこか |
| Agent Boundary | AIに任せる範囲と禁止範囲はどこか |
| Evidence | 前進・完了を何で証明するか |
| External Tool | Issue / Chat / Docs / Cloud等とどう連携するか |
| Runtime / Model | どのAgent Runtime / Modelを使い、差し替え可能か |

---

## 6.3 Control Point Mapを作る

Delivery Flowの各地点について、次を記録する。

```text
Control Point
├ Trigger
├ Actor: Human / AI / Machine
├ Input
├ Allowed Action
├ Required Evidence
├ Pass Condition
├ Failure Route
├ Escalation Owner
├ Permission Boundary
└ Traceability Target
```

例：

| Control Point | Actor | Evidence | Fail時 | Harness実装候補 |
|---|---|---|---|---|
| Before Implementation | AI + Human as needed | Spec / Acceptance / Decision | Align / Specifyへ戻る | Skill / Decision Packet |
| Pre-commit | Machine / AI | Lint / unit test | Agent retry | Hook |
| PR/MR | AI + Human | Review Packet / CI result | Rework / Decision | Review Skill / Gate |
| Integration | CI | Integration result / env provenance | Environment or Code route | CI Gate / Env checker |
| Release | Human / Policy | Release Decision Packet | Defer / Fix | Approval Gate |
| Production | CD + Runtime | Deployment / smoke / monitoring | Rollback / Incident | Tool / Runbook / Agent |

**HarnessはこのControl Point Mapを実行可能にする。**

---

## 6.4 「Map, not Encyclopedia」

Harnessの入口ファイルに全情報を書かない。

推奨する思想は次。

```text
短い入口
├── 現在のDevelopment / Delivery Flowへのリンク
├── 正本ドキュメントへのリンク
├── Build/Test/CIコマンド
├── Environment識別方法
├── 禁止事項・Permission Boundary
└── 必要時に呼ぶSkill/Agent
```

深い内容は必要になった時点で読み込む。

これにより、

- 不要Contextの常時投入を避ける
- ルールの責務を分離する
- 更新箇所を特定しやすくする
- CI/CDやEnvironmentの事実とPrompt上の思い込みを分離する
- AI Runtimeを差し替えやすくする

という効果を狙う。

---

## 6.5 Harnessは「足場」であり、Model能力とともに変える

Harnessの各構成要素は、暗黙的に「Modelだけではできないこと」への仮定を持つ。
その仮定はModelの進化により古くなるため、Harnessを複雑化したまま固定しない。

原則：

1. Delivery上必要なControl Objectiveを先に固定する。
2. そのControl Objectiveを満たす最小のHarnessを採用する。
3. Rule / Skill / Agent / Hookを追加した理由を記録する。
4. Model更新時は、追加した足場がまだ必要かEvalする。
5. 削除してもOutcome / Evidence / Safetyが維持できるなら単純化する。


---

## 6.6 Harness成熟度

Harnessそのものにも成熟度を持たせる。

| Level | 状態 |
|---|---|
| H0 | 個人Prompt中心 |
| H1 | 共通Instructionsあり |
| H2 | Rule/Skill/Agentが役割分離 |
| H3 | SCM / CI/CD / External Tool / Quality Gateと接続 |
| H4 | Evalsにより変更を評価 |
| H5 | Issue/Feature単位の自律実行 |
| H6 | 複数Agent・複数Work Itemを統合管理し、Deliveryまで証跡連携 |

Harness成熟度とAI自律化レベルは同じではない。
Harnessが高度でも、高リスク業務ではHuman Gateを残す。


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 07. AI Native OrganizationのOperating Model

**Creator / Lead Author: RIO AMADA**

# DR-M22. 22_AI-Native Organization Operating Modelガイド

**レイヤ:** Organization / Operating Model  
**目的:** HumanとAIが混在する組織を、Role・Decision・Authority・Context・Evaluation・Learningの構造として設計する。

## M22.1 Strategy-to-Execution

```text
Strategy / Intent
↓
Portfolio / Initiative
↓
Demand / Requirement
↓
Operating Model
↓
Engineering / Business Execution
↓
Evidence
↓
Outcome
↓
Organizational Learning
↓
Next Strategy
```

上位Intentと下位Executionを別システムにしない。

## M22.2 Human / AI Role Model

Roleは肩書きではなく、次の契約で定義する。

```text
Purpose
Input
Output
Decision rights
Allowed actions
Forbidden actions
Required context
Escalation
Evaluation
Owner
```

Agentを増やすことをOrganization Designとみなさない。
決定論的処理はScript / Rule / Toolへ寄せ、Role分離が必要な場合だけAgent化する。

## M22.3 Decision Rights

最低限、次の責務を明示する。

- Human Owner
- Decision Owner
- Approval Owner
- Escalation Owner
- Standard Owner
- Harness Owner
- Eval Owner
- Risk Owner
- Environment / Operations Owner

M0-M1では兼任を許容できる。
成熟度上昇時には、Riskと負荷に応じて分離する。

## M22.4 Decision Ledger

重要判断は結果だけでなく、

```text
Decision
Context
Options
Rationale
Owner
Evidence
Scope
Expiry / Revisit condition
```

を残す。

「採用しなかった判断」も組織学習の対象である。

## M22.5 Authority / Permission

AutonomyとPermissionを分離する。

```text
Autonomy
= どこまで自分で進めてよいか

Permission
= 何を実行してよいか
```

高AutonomyであってもProduction WriteやExternal Sendを持たせる必要はない。

## M22.6 Escalation

Escalationは「人へ返す」では不十分。

```text
Cause Class
↓
Destination Owner
↓
Expected decision
↓
SLA / timeout
↓
Fallback
```

まで定義する。

## M22.7 Organizational Source of Truth

組織知は、

```text
Canonical Source
+
Declared Projection
+
Drift Check
```

を基本形とする。

コピーを禁止するのではなく、**未宣言コピー**を禁止する。

## M22.8 Organizational Memory

```text
Feedback / Incident / Decision
↓
Classification
↓
Rewrite
↓
Policy / Rule / Skill / Process / Eval / Living Document
↓
Capability
```

共有は単純Exportではなく、再利用可能な形への**清書・一般化**として行う。

## M22.9 Policy Architecture

Organization PolicyもEnforcement Ledgerへ接続する。

```text
Policy
├ machine block
├ machine nudge
├ human review
├ measurement
└ declared-only
```

すべてを機械強制できるふりをしない。

## M22.10 Capability Model

Capabilityは「Toolを契約した」「Skillファイルがある」では成立しない。

```text
Available
→ Discoverable
→ Usable
→ Measured
→ Maintained
→ Transferable
```

までをCapability Lifecycleに含める。

### M22.10-A Experience × AI-Native Capability — 採用・配置・評価を年次だけで決めない

AI Native Organizationでは、`経験年数` と `AIを使えるか` を一つの軸へ潰さない。少なくとも次を分離して見る。

```text
Domain / Technical Experience
AI Delegation Capability
Evaluation / Evidence Capability
Work Class Fit
Context / Harness Leverage
Accountability / Escalation Judgment
```

このProfileは人事Ratingそのものではない。**誰に、どのWork Classを、どのDelegation Envelopeで任せるか**を決めるOperating Inputである。

組織は次のような誤った単純化を避ける。

- `新卒だからAI Nativeで強い` と決めつける
- `SeniorだからAIを使えば必ず最強になる` と決めつける
- AI利用量をPerformance評価へ直結する
- AIが生成したOutput量を個人Productivityへ直結する
- JuniorがAIで速くなったことを、Mentoring不要の根拠にする

採用・配置・育成では、年次より具体的に次を観測する。

```text
Outcomeを定義できるか
仕事をVerifiable Unitへ分けられるか
AIへScope / Permission / Evidenceを渡せるか
AI Outputの弱点を説明できるか
Unknownを隠さずEscalateできるか
経験をRule / Context / Eval / Harnessへ外部化できるか
```

> **AI時代の強い人材とは、AIなしで何でも一人でできる人でも、AIへ何でも投げられる人でもない。Human + AI Systemとして、より大きなOutcomeを安全に完遂できる人である。**

この観点では、AI Nativeな新人がBounded Workで早く立ち上がることと、AI Nativeな経験者がTacit Knowledgeを増幅してより大きなDecisionを担うことは両立する。

## M22.11 Organizational Evals

評価対象例：

- Decision Quality
- Execution Quality
- Escalation Accuracy
- Human Intervention
- Rework
- Lead Time
- Knowledge Reuse
- Policy Compliance
- Risk Incident
- Business Outcome

AI Workerの評価を、そのまま人間の人事評価へ直訳しない。

## M22.12 Organizational Learning

学習Loop自体も監視対象とする。

振り返り・提案制度・自動学習が存在しても、使われていない / 壊れている / 改善へ到達しないならCapabilityではない。

---


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 08. 自分たちの現在地を知る — GreenfieldからLegacyまで

**Creator / Lead Author: RIO AMADA**

# Legacy / Brownfield Compatibility Profile

日本企業の既存案件へDeepRailを適用するとき、
Git / PR / Worktree / Cloud環境を当然の前提にしない。

DeepRail Coreで固定するのはToolではなく次である。

```text
Work isolation
Traceability
Reviewability
Approved evidence
Source of Truth
Change history
Rollback / Recovery
Human Gate
Evaluation
```

これらを満たせるなら、実装方式はAdapterで置換できる。

## 集中型VCS（Centralized VCS等）

### Profile A — Native Git

```text
Git
→ Branch / Worktree
→ PR / MR
→ CI / Review
```

DeepRailの標準Reference Profile。

### Profile B — Git Bridge + Centralized VCS Canonical

Legacy環境向けの検討Profile。

```text
Centralized VCS
Canonical Source
      ▲
      │ controlled sync
      │
Local Git Projection
      │
      ├ Agent work branch
      ├ local worktree
      ├ automated checks
      └ review evidence
```

ここで見るのは、

> **Gitを第二の正本にしない。**

Centralized VCSが組織上の正本なら、Local GitはAI作業用の一時Projectionとして宣言する。

同期時には最低限、

```text
centralized revision
↕
Git commit / patch
↕
Work Item
↕
Approval / Evidence
```

の対応を追跡可能にする。

推奨する検査：

- Centralized VCS正本とBridge差分の照合
- 同期漏れ検知
- 未同期Git Commit検知
- Centralized Revision ↔ Work Item対応
- 承認済み版と同期対象の一致
- 二重更新Conflictの検知

**状態:** Hypothesis / 未実地検証。  
集中型VCS Bridgeは、実案件または模擬Evalで成立性を検証してからReference Adapterへ昇格する。

### Profile C — Centralized VCS Native / Reduced Parallelism

Bridgeの維持コストが高い場合は無理にGit化しない。

```text
Centralized VCS Checkout
↓
Isolated Working Directory
↓
AI Session
↓
Patch / Diff
↓
Machine Checks
↓
Review Packet
↓
Human Approval
↓
Centralized VCS Commit
```

Git WorktreeやPRが無い分、

- Agent並列度を下げる
- 作業Directoryを物理分離する
- Diff / PatchをReview Packetへ含める
- Approval Ledgerを外出しする
- Commit前Gateを強める

という縮退Profileを使う。

DeepRailは「最大自律度」を常に狙わない。
現在環境で安全に成立する自律度へ縮退することを正常な適用とみなす。

---

## Git概念とLegacy環境の対応

| DeepRail上の目的 | Git系 | Centralized VCS / Legacy代替 |
|---|---|---|
| Work isolation | Branch / Worktree | Separate checkout / working directory |
| Change unit | Commit | centralized revision / patch set |
| Review | PR / MR | Review Packet / Legacy Work Management ticket / approval record |
| Traceability | Commit / PR link | Revision ↔ Work Item mapping |
| Parallel work | Worktree | Checkout / workspace分離 |
| Gate | CI / protected branch | pre-commit / wrapper / external checker |
| Approval | PR approval | Approval Ledger / workflow state |
| Rollback | revert commit | reverse merge / revision restore |
| Source of Truth | Git remote | centralized repository |

Tool機能をそのまま模倣するのではなく、
**そのToolが担っていたControl Objectiveを別手段で満たす。**

---

## 日本企業Legacy Operating Context

現場で繰り返し現れるEnvironment Differenceは、

```text
CRLF
cp932
日本語Path
Windows
Proxy / PAC
社内Network
残留試験資材
Mirror freshness
```

のような条件だった。

Legacy Trackでは、VCSだけを見ても足りない。Operating Context全体を適用判定に入れる。

### Environment

- Windows first-class support
- PowerShell / cmd / shell差
- CRLF
- cp932 / UTF-8
- Japanese username / path
- symlink restrictions
- package registry / proxy
- offline install
- certificate / enterprise CA

### Network

- PAC
- HTTP proxy
- closed network
- no direct external API
- internal mirror
- restricted MCP / SaaS

### Work Management

- Legacy Work Management
- Work Management Server / Data Center
- Excel台帳
- approval workflow
- ticket number based traceability

### Development Method

- Waterfall
- phase gate
- formal artifacts
- document approval
- long release cycle
- multi-vendor responsibility boundaries

DeepRailはこれらを「例外」として端へ追いやらず、
**Operating ContextによるProfile選択**として扱う。

---


---

## M25.1 Current State Assessment

最初にAI Toolを選ばない。

現状を最低限次の観点で整理する。

```text
Business / Product
Organization
Development Process
SCM
Work Management
Architecture
Runtime / Environment
Security
Data Classification
Network
Device
Identity / Account
Procurement
Legal
Approval
Development Standard
Quality / Test
Release
Operations
Knowledge
Skill / Training
Culture
```

例：

```text
SCM: Centralized VCS
Work Management: Legacy Work Management
OS: Windows managed device
Network: Direct Internet prohibited
AI: External generative AI prohibited
Source Code: External SaaS upload prohibited
Method: Waterfall
Approval: Formal design review
Security Review Lead Time: 8 weeks
```

現状を「Legacyだから悪い」と評価しない。
Transformationの開始条件として記録する。

---

## M25.2 Constraint Register

AI導入を止める制約を、愚痴・口頭情報・暗黙前提のままにしない。

```yaml
constraint:
  id:
  category:
  description:
  owner:
  affected_scope:
  impact:
  resolution_path:
  workaround:
  decision_required:
  lead_time:
  status:
```

代表カテゴリ：

```text
Security
Legal
Procurement
Network
Device
Data
SCM
Architecture
Platform
Account / IAM
Development Standard
Operations
Human Capacity
```

ConstraintはBacklogへ接続する。

---


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 09. AI導入を阻む制約を可視化する

**Creator / Lead Author: RIO AMADA**

## M25.2 Constraint Register

AI導入を止める制約を、愚痴・口頭情報・暗黙前提のままにしない。

```yaml
constraint:
  id:
  category:
  description:
  owner:
  affected_scope:
  impact:
  resolution_path:
  workaround:
  decision_required:
  lead_time:
  status:
```

代表カテゴリ：

```text
Security
Legal
Procurement
Network
Device
Data
SCM
Architecture
Platform
Account / IAM
Development Standard
Operations
Human Capacity
```

ConstraintはBacklogへ接続する。

---

## M25.3 Stakeholder Map

AI導入Programでは、最低限次を整理する。

```text
Executive Sponsor
Program / Transformation Owner
Product / Business Owner
Engineering
Architecture
Security
Legal
Procurement
IT / Network
Platform
Development Standard
QA
Operations
Education / Enablement
```

各論点に、

```text
Who proposes?
Who decides?
Who approves?
Who executes?
Who operates?
Who must be consulted?
```

を定義する。

RACI等の形式を使ってもよいが、DeepRail Coreとして特定方式には依存しない。

---


---

## M25.7 Security / Governance Enablement

大企業ではAI導入の主要BottleneckがCodingではなくSecurity / Governanceになる場合がある。

最低限整理する。

```text
何をAIへ送信してよいか
どのData Classまで可能か
Source Code送信可否
Customer Data送信可否
Logの保存先
Providerによる学習利用
Retention
Account管理
Model / Tool Allowlist
MCP / External Tool
Network接続
Secret Access
Production Access
Audit
Incident Response
```

SecurityやDataの申請を、導入前に片づける事務作業へ押し込めない。Transformation Programの正式なWork Itemとして管理する。

---

## M25.8 Shared Enablement

一人が使えることと、組織として使えることは分けて考える。

```text
Personal Experiment
↓
Controlled Pilot
↓
Team Shared Setup
↓
Approved Standard Setup
↓
Managed Organization Platform
```

共通利用に必要なもの：

- approved account
- common configuration
- policy
- standard harness
- logging
- support
- training
- version management
- security review
- cost ownership

個人のローカル設定だけで回っているうちは、Organization Adoptionまで来たとは言いにくい。

---


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 10. 経営・Security・IT・現場をどう動かすか

**Creator / Lead Author: RIO AMADA**

## M25.3 Stakeholder Map

AI導入Programでは、最低限次を整理する。

```text
Executive Sponsor
Program / Transformation Owner
Product / Business Owner
Engineering
Architecture
Security
Legal
Procurement
IT / Network
Platform
Development Standard
QA
Operations
Education / Enablement
```

各論点に、

```text
Who proposes?
Who decides?
Who approves?
Who executes?
Who operates?
Who must be consulted?
```

を定義する。

RACI等の形式を使ってもよいが、DeepRail Coreとして特定方式には依存しない。

---

## M25.4 Transformation Profile判定

次を判定する。

```text
Project State
P0 / P1 / P2 / P3

AI Availability
AI-0 / AI-1 / AI-2 / AI-3 / AI-4

Organization Enablement
O0 / O1 / O2 / O3 / O4
```

判定結果から導入順序を変える。

### Profile A — AI Native Greenfield

```text
P0 × AI-3〜4 × O2〜4
```

主戦場：

- Target Operating Model
- Harness
- Evidence
- Autonomy
- Quality Gate
- Organization Learning

### Profile B — Modern but AI-Constrained

```text
P0〜P1 × AI-0〜1 × O0〜1
```

主戦場：

- Security Review
- Data Policy
- Procurement
- Network
- Account
- Approved Toolchain
- Logging / Audit
- Pilot permission

Coding Harnessを先に作り込まない。

### Profile C — Modern Brownfield

```text
P1 × AI-2〜4 × O1〜3
```

主戦場：

- Existing Processへの差し込み
- Source of Truth整理
- Review / Test再設計
- Existing CIとの接続
- Team共通化

### Profile D — Legacy / Brownfield

```text
P2〜P3 × AI-0〜2 × O0〜2
```

主戦場：

- Constraint Inventory
- Shrink Profile
- Adapter
- Human Gate
- Legacy SCM
- Shared Environment
- Existing Waterfall Artifacts
- Manual Approval
- Small Pilot

Infrastructure全面刷新をAI導入の前提にしない。

---

## M25.5 Target Operating Model

TargetにするのはTool名ではない。**仕事の流れ**を先に描く。

悪いTarget：

```text
Coding Agent Runtimeを全員に導入する
```

良いTarget：

```text
Business Requirement
↓
AI-assisted Requirement Structuring
↓
Human Alignment
↓
AI-assisted Design / Build
↓
Machine Gate
↓
Independent AI Review
↓
Human Decision Review
↓
Test / Eval
↓
Release
↓
Living Document
```

Target Operating Modelには、

```text
Human Role
AI Role
Decision Rights
Source of Truth
Gate
Evidence
Escalation
Permission
Evaluation
Knowledge Reinvestment
```

を含める。

---


---

## 23.2-A Decision Rights Delegation Protocol

ここはDecision RightsのOperational Homeである。Ch10で「誰が決めるか」を理解したあと、Human / AI間でその判断をどう移すかを具体化する。

Human Gateを縮めるときは、「チェックを外した」とだけ記録しない。**どのDecisionを、どの条件でAIへ任せられるようになったか**をDelegation Envelopeの変更として残す。

```text
初期
Human Decision Surface = 大
AI Delegation Envelope = 小

成熟
Human Decision Surface = Risk / Exception / Policy中心
AI Delegation Envelope = Planning / Execution / Evaluation / Coordinationへ拡大
```

### Subsidiarity for Human-AI Teams

> **判断は、信頼可能に判断できる最も実行に近い主体へ置く。**

Agent自身で機械検証できるならAgent、独立AI Evaluatorで判定できるならAI Evaluation、組織Risk・曖昧性・Accountabilityが残るならHumanへ上げる。

### Delegation Contract

継続的なDecision Rights委譲には次を必須とする。

```yaml
delegation:
  decision_class:
  scope:
  allowed_actions:
  evidence_required:
  escalation_conditions:
  expiry:
  audit:
  disclosure:
  rollback_or_revoke:
```

`scope: all` のような無限定委譲を標準形にしない。

### S Transition Protocol

承認強度を弱める場合、一度に飛ばさない。

```text
S5
↓ measure
S4
↓ measure
S3
↓ measure
S2 / S1
↓ measure
必要ならGate自体を削除
```

各段で最低限、False Accept / Defect / Override / Approval Wait / Rubber-stamp兆候を観測する。悪化すれば即座に強いSへ戻せることを前提にする。

### Approval Hollowingを監視する

Gateが存在していても、次の兆候があれば実質的な統制が抜けている可能性がある。

- 承認時間が不自然に短い
- 承認Queueが長期滞留する
- 委任記録だけが急増する
- Decision Packetを開かず承認される
- lease / claimが失効したまま放置される
- 例外的な「今回は通す」が常態化する

対策の主手段は承認者を責めることではない。

```text
承認1件あたりの判断コストを下げる
→ self-contained Decision Packet

承認回数そのものを減らす
→ machine-detectable / reversible / low-risk領域を委譲
```

承認帯域が足りない状態を放置すると、遅延だけでなく**Governanceそのものが劣化する。**

### 23.2-A.1 Why — なぜDecision RightsはTool Permissionより重要なのか

「AIに何をさせてよいか」を考えると、まずPermissionの話が出てくる。File Writeを許すか。Terminalを許すか。Productionへ接続してよいか。

もちろんPermissionは要る。危険な操作を技術的に止める仕組みは欠かせない。

ただし、Permissionだけでは仕事の権限は決まらない。

FlowDeskのAgentにDatabase Write権限があるとする。それは「代理承認Ruleを変更してよい」という意味ではない。ProductionへDeployできる権限があっても、「高額申請ではCompliance Approvalを不要にしてよい」という意味ではない。

Tool Permissionが答えるのは、**その操作を実行できるか**。Decision Rightsが答えるのは、**その判断をしてよいか**である。

```text
Permission
Can I do this operation?

Decision Right
Am I authorized to make this decision?
```

人間の会社でも同じである。経理Systemへ入力できる社員が、会社の支払Policyを変更できるわけではない。SCMへMergeできるEngineerが、ProductのRisk Appetiteを一人で変えられるわけではない。

AIではToolが強力なため、この境界が見えにくい。Agentへ広いTool権限を渡すと、できることが増え、そのまま「任せられることも増えた」ように感じる。

仕事を任せるなら、先に仕事側の条件を決める。何のDecision Classか。Scopeはどこまでか。どんなEvidenceが要るか。どのRiskまで自分で進めてよいか。どこでHumanへ戻すか。権限はいつ切れるか。

その後で、必要最小限のTool Permissionを与える。

```text
Purpose / Work
↓
Decision Rights
↓
Delegation Contract
↓
Required Tool Permission
↓
Execution
```

逆に、Tool Permissionから設計すると「使えるから使う」が起きる。

同じAgentが技術的には全部できても、Decision Rightsは別々に持たせられる。ここに自律化の余地が生まれる。

Permissionを狭くしすぎればAIは働けない。広げすぎれば危険になる。そこで、**Decision Rightsを先に絞り、その判断を実行するために必要なPermissionだけを十分に渡す。**

そしてDecision Rightsは固定ではない。Shadow Evaluationで判定精度を測り、Evidenceが安定し、失敗が検出可能で、RollbackできるならScopeを広げられる。逆にIncidentが出れば縮められる。

> **AI自律化の核心は、どのToolを使わせるかではない。どの判断を、どの条件で任せるかである。**

PermissionはExecution Controlの話で、Decision RightsはOperating Modelの話だ。似て見えても、決めているものが違う。


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 11. Pilotから標準化・全社展開まで

**Creator / Lead Author: RIO AMADA**

## M25.9 Pilot Design

Pilotで確かめるのは、Toolが動くかどうかだけではない。

```text
Pilot
=
Tool Verification
+
Process Verification
+
Organization Verification
```

Pilot開始前に、

```text
Objective
Scope
Baseline
Evaluation Function
Allowed AI
Allowed Data
Human Gate
Owner
Duration
Kill Criteria
Expected Learning
```

を定義する。

Pilot成功条件：

```text
Engineering Loopが回った
+
Security / Approval / Supportが回った
+
Evidenceが取れた
+
次の意思決定に必要なLearningが得られた
```

---

## M25.9-A Evaluation Trust / Delegation Pilot

AIをまだ知らない組織に、「まず信頼してください」と言っても進まない。
Pilotでは、AIが何をできるかだけでなく、**AIの評価をどこまでGate判断に使えるか**まで確かめる。

推奨導入順：

```text
1. Work Classを限定
2. Human評価をBaselineとして保持
3. AIをShadow Evaluatorとして並行稼働
4. Human / AIの不一致を分類
5. Evaluation Criteria / Evidence / Harnessを改善
6. Exit Criteriaを満たしたWork ClassだけEA2へ
7. Human全件承認からRisk / Exception中心へ移行
8. Sampling / Auditで安定性を確認
9. EA3以降へ段階昇格
10. Drift / Incident時は即座に一段戻す
```

Pilot Reportには最低限次を残す。

```yaml
evaluation_delegation:
  work_class:
  current_ea_level:
  target_ea_level:
  sample_size:
  false_accepts:
  false_rejects:
  unknowns:
  human_overrides:
  escaped_defects:
  evidence_gaps:
  rollback_events:
  exit_criteria:
  decision_owner:
  next_action:
```

AIの正解率だけを見ても、運用できるかどうかは分からない。
**どのFailureが検出可能か、重大なFalse Acceptを見逃さないか、失敗時に戻せるか、誰がAccountabilityを持つか**まで含めてEvaluation Authorityを決める。

---

## M25.10 Rollout

RolloutはTool配布ではない。

```text
Pilot
↓
Pattern Extraction
↓
Standardization
↓
Enablement Package
↓
Team Rollout
↓
Measurement
↓
Adjustment
↓
Multi-team / Organization Rollout
```

横展開時は、完成品のコピーではなく、

> **共通部品 + 採寸方法 + 導入工程**

を移植する。

---

## M25.11 Change Management

AI導入により変わる可能性があるもの：

```text
Role
Responsibility
Review
Approval
Skill
Performance expectation
Team structure
Support
Career / training
Communication
Decision speed
```

「新Toolの研修」で終わらせない。

人間に対して、

```text
何が変わるか
何が変わらないか
何をAIへ任せるか
何を人間が持つか
困ったとき誰へEscalateするか
```

を説明できる状態を作る。

---

## M25.12 Transformation Metrics

AI利用率を主要成功指標にしない。

例：

```text
Constraint Resolution Lead Time
Security Approval Lead Time
Account Provisioning Lead Time
Pilot Cycle Time
Adoption Readiness
Human Intervention
Review Capacity
Training Completion
Support Load
Standard Compliance
Business / Engineering Outcome
```

Transformation Phaseごとに評価関数を変える。

---

## M25.13 Transformation Failure

代表Failure：

```text
Tool-first
Tool契約だけしてProcessが変わらない

Training-first
使えないToolの研修を先に行う

Harness-first
Security未承認なのにHarnessだけ作る

Pilot-isolation
Pilot成功が共通Platformへ昇格できない

Shadow-AI
個人だけが独自設定で利用

No-owner
Security / Harness / Eval / SupportのOwner不在

No-kill-criteria
Pilotを止める判断基準がない

No-scale-path
成功後の横展開経路がない
```

---


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 12. AI時代の人材をどう育てるか

**Creator / Lead Author: RIO AMADA**

# 19. 15_AI時代の人材育成・習熟・実践ガイド

## 19.1 人材育成の目的

AI Toolの操作方法だけを教えることを、人材育成と呼ばない。

育てたいのは、Toolの操作速度より次の能力だ。

```text
AIを使える
↓
AIへ仕事を委譲できる
↓
AIの成果をEvidenceから評価できる
↓
AIが実行可能なWorkへ構造化できる
↓
Human + AI Teamを運営できる
↓
Harness / Eval / Processを改善できる
↓
AI Nativeな組織能力を設計できる
```

---

## 19.2 Human AI Proficiency / Leadership Maturity

| Level | 人材像 | 主な能力 |
|---|---|---|
| HC0 | AI未習熟 | AIを限定的に利用 |
| HC1 | AI User | 目的・制約を含む依頼ができる |
| HC2 | AI Operator | Context / Tool / Harnessを使い仕事を完遂 |
| HC3 | AI Evaluator | Evidence / Acceptance / Riskから成果を評価 |
| HC4 | AI Orchestrator | Work分解・Delegation・複数AI・Human Gateを設計 |
| HC5 | AI System Designer | Harness / Eval / CI/CD接続 / Failure改善を設計 |
| HC6 | AI Native Leader | Team / Operating Model / Transformationを運営 |

HC0〜HC6を、人事評価の順位には使わない。見るのは、**どの責務なら安全に担えるか**である。

人材育成の段階は `HC0〜HC6`（Human Capability）を使う。Harness成熟度は `H0〜H6`、Operating Context上の委譲資格は `H-1〜H-3` とし、記号の責務を分離する。

---

## 19.2-A Experience Curve Recomposition — 経験の価値は消えない。組み替わる

入社8か月のEngineerが、経験8年のEngineerより先にFeatureを終える。

AI時代には、そういう場面は十分に起こり得る。

だからといって、「新人の方がベテランより使える」とは言えない。変わっているのは、人の価値より**経験が成果へ変わる道筋**の方だ。

たとえば、小さく境界の明確なFeatureを二人へ任せる。経験8年のEngineerはAIへ実装を依頼し、最後にDiffをすべて読み、自分の頭の中で仕様と影響を再構成する。入社8か月のEngineerは、最初にAcceptanceを置き、AIへTask Contractを渡し、TestとVerification Procedureを実行させ、Evidence PacketのUnknownだけをSeniorへEscalateする。

このWork Classだけを見れば、後者が先にOutcomeへ到達することはある。

しかし途中で、既存顧客だけが使っている古いAPI契約を変更するDecisionが出たとする。新人には見えていなかった。経験8年のEngineerは、三年前の障害と、Documentに残っていないCompatibilityの癖を知っていた。そこで実装を止める。

このSceneを見ると、二人を一本の物差しで比べにくいことが分かる。

**勝ったのは新人でも、ベテランでもない。二人が持っていた強さの種類が違った。**

AIは、すべての経験差を同じ方向に動かさない。

### 圧縮されやすい経験差

AIが検索・生成・比較・反復を担えるほど、次のような差は以前より短期間で埋まり得る。

- Syntax / Boilerplate
- Library / APIの探索
- 典型Patternの初期実装
- Test Draft / Data Draft
- Documentや既存CodeからのRule候補抽出
- 選択肢の列挙と比較の初稿

これらは「経験が不要になった」のではない。以前は人間の記憶量や手数に強く依存していた部分を、AIが外部化できるようになったという方が近い。

### むしろ増幅され得る経験

一方で、次の経験はAIを使うことで価値が増す場合がある。

- Domain Vocabularyの裏にある意味
- Document化されていないConstraint
- Architecture DecisionのTrade-off
- 過去Incidentから得たFailure Pattern
- Stakeholder間の利害・責任境界
- 「この変更は何か怪しい」と気づくRisk感覚
- Accountabilityを伴うDecision経験

AIが調査や実装を高速化しても、何を疑い、どのUnknownを残し、何をEvidenceで証明させるかは、こうした経験から強くなる。

AIによってExperience Premiumが一律に下がる、と決めつけない方がいい。

> **AIは経験を無価値にするのではない。価値の低い経験差を圧縮し、価値の高い経験を増幅することがある。**

ただし、どちらが起こるかはWork Class、Domain Familiarity、Taskの曖昧さ、Harness、Model Capabilityによって変わる。

### Experience Effectは条件依存で扱う

DeepRailは、`Junior > Senior` や `Senior > Junior` のような単純な序列をAI時代の前提にしない。

**Experience Effectそのものが、仕事の種類とAIの使い方で変わる。**

AIがSyntax、探索、Draft、反復を圧縮するWorkでは経験差が縮み得る。一方、Domain、Architecture、Risk、Stakeholder、Incident Memoryのような経験は、AIへ適切なContext・Constraint・Evaluationを与えることで価値が増幅され得る。

経験別のAI効果を見るなら、少なくとも次の条件を一緒に見る。

```text
Experience Level
×
Work Class / Task Mix
×
Domain Familiarity
×
AI-Native Capability
×
Harness / Evidence Quality
×
Tool Generation
→
Observed Outcome
```

> **年次を能力のProxyにしない。同時に、AI利用率を能力のProxyにもしない。OutcomeとEvidenceで見る。**

### AI Native Entry Advantageは「仮説」として扱う

新卒・若手が最初からAIを前提に仕事を学ぶことで、従来型Operating ModelをUnlearnするCostが小さくなる可能性がある。ここでは、この仮説を **AI Native Entry Advantage** と呼ぶ。ただし、これはMaturity Levelでも、人材序列でも、確定したEmpirical Lawでもない。

新人には、経験が少ないという明確な弱みがある。同時に、

```text
人間が全部書く
→ 人間が全部覚える
→ 人間が全部読む
→ 何年かしてから仕事を任せる側になる
```

という旧来の学習順序に最適化されていないという特徴もある。

だから最初から、

```text
Outcomeを定義する
↓
自分で仮説を持つ
↓
AIへ仕事を任せる
↓
Evidenceで確かめる
↓
分からないことをEscalateする
↓
失敗をRule / Test / Harnessへ戻す
↓
より大きなOutcomeを引き受ける
```

という順序で育てる余地がある。

ただし、AIに考えてもらえば基礎理解を飛ばしてよい、という話にはしない。

> **自分が理解していない成果を、AIが作ったという理由だけで「理解したこと」にしない。**

AI Nativeな新人教育では、実装を自力だけで再現できるかを唯一の試験にしない。その代わり、なぜそのDesignを採用したか、どのEvidenceなら反証できるか、何がUnknownか、どこでSeniorへ戻すべきかを説明させる。

### Experience × AI-Native Capability Matrix

経験年数とAI Native Capabilityを同じ軸に置かない。

| | AI Native Capability 低 | AI Native Capability 高 |
|---|---|---|
| **Domain / Technical Experience 低** | 基礎学習と小さなWorkから開始。AI Outputを鵜呑みにしやすいRiskを管理 | **Fast-ramp候補**。Bounded / Verifiable Workで早期にOutcomeを持たせる。ただしDomain / Risk DecisionはMentorと接続 |
| **Domain / Technical Experience 高** | 深い知識はあるが、逐次実行・逐次ReviewがCapacity Bottleneckになり得る | **Compounding Leverage**。経験をContext / Rule / Eval / Harnessへ外部化し、Team全体へ増幅できる |

このMatrixを人事Ratingには使わない。Work Allocation / Training / Mentoringを考えるためのProfileとして使う。

採用・配置・育成でも、`経験3年以上` だけでは人の強さを見切れなくなる。

見るべきなのは、少なくとも次である。

```text
Domain / Technical Experience
×
AI Delegation Capability
×
Evaluation / Evidence Capability
×
Work Class Fit
×
Context / Harness利用能力
×
Accountability / Escalation Judgment
```

同じ経験8年でも、Human + AI Systemとして完遂できるOutcomeは違う。同じ新卒でも、任せられるWork Classは違う。

> **AI時代の人材評価は「一人で何ができるか」だけではなく、「Human + AI Systemとして何を安全に完遂できるか」まで広げる。**

### AI Native Onboarding Rule

新人をAI Nativeに育てる場合、最初から自由放任にはしない。

1. 小さく、Acceptanceが明確で、Rollback可能なWorkを持たせる。
2. AI利用を前提にしてよいが、Required Evidenceを先に決める。
3. `なぜそうしたか / 何が未検証か / 何が壊れ得るか` を本人に説明させる。
4. Domain / Architecture / Security等のHigh-risk DecisionはExperienced MentorへEscalateする。
5. Mentorは答えを代行するだけでなく、暗黙知をVocabulary / Rule / Decision Record / Testへ外部化する。
6. Outcomeが安定したWork ClassからDelegation Envelopeを広げる。

加えて、AI Native Onboardingでは次の4つをGuardrailとして置く。

```text
Explain-back
本人が「なぜその設計か」を説明できる

Evidence Review
AIの自己申告ではなく、Test / Runtime / Artifactで確かめる

Escalation Judgment
分からない時に、どこで止めて誰へ返すかを選べる

Agency Check
AIへ任せた結果、自分の判断責務まで手放していないかを確認する
```

AIを多く使っているだけで、習熟したとは判定しない。**理解を保ったまま、より大きなOutcomeを安全に任せられるようになったか**で見る。

目指すのは、AIにコードを書かせる人を増やすことではない。**AIと一緒に仕事を成立させられる人**を増やすことだ。

そして経験者側にも同じ学習が必要になる。

Seniorの価値は、自分だけが知っていることを抱え続けることではない。その経験を次のHumanとAIが使える形へ変換できたとき、個人の経験がOrganization Capabilityへ変わる。

このテーマは、「経験年数だけではSkillを説明できない」という認識から始まり、AI Native Onboarding、採用・配置・評価、組織Capabilityへつながる。

---

## 19.3 Level別学習Path

```text
HC1
→ 基本操作 / Data・Security / 良いObjective

HC2
→ Existing System調査 / Work Contract / Tool / Test / Source of Truth

HC3
→ Acceptance / Evidence / Review Packet / Decision Packet

HC4
→ Epic分解 / Dependency / Agent Coordination / Re-decomposition / Meeting Facilitation

HC5
→ Harness / CI/CD / Eval / Environment / Observability / Enforcement

HC6
→ Transformation / Decision Rights / Capacity / Governance / Organizational Learning
```

---

## 19.4 Team Lead育成では「会議を回せる」までを実技にする

チームリーダー習熟では、AI ToolのDemoではなく次を実技評価する。

- Outcome / Intake Syncで曖昧な要求を整理できる
- Mock / Prototype / Scenarioを使ったAlignmentを設計できる
- AIのWork BreakdownをRubricで評価できる
- Execution PlanningでContext / Permission / Evidenceを決められる
- DailyをStatus会ではなくDecision & Blocker Syncへ変えられる
- Decision PacketからArchitecture / Risk判断できる
- Review / AcceptanceをEvidence中心で行える
- Release ReadinessでCI/CD・Rollback・Monitoringを確認できる
- RetroでHuman InterventionをRule / Skill / Eval / Processへ還元できる

---

## 19.5 Training Principle — Harnessの歴史を学習の順序として再現する

Harness Engineeringそのものの説明はCh39へ任せる。ここで考えるのは、**どう教えれば必要性を自分で発見できるか**である。

最初からRule、Context、Gate、Evalの一覧を暗記させても、使う理由までは身につきにくい。小さなEnd-to-End課題を任せると、学習者は別の順番で困り始める。

「また同じ説明をしている」「AIが終わったと言うたびに自分が全部確認している」「この操作は勝手にやらせたくない」。その違和感が出たところで、RuleやEvidenceやPermissionを入れる。

教育で再現したいのはHarnessの部品表ではなく、**必要な仕組みを自分で増やしていく思考の順番**である。

> **Friction is Curriculum. — 摩擦そのものを教材にする。**

答えを隠す必要はない。学習者が「なぜ今これが要るのか」を、自分が困った経験と結びつけられる順番を作る。

---


---

## 19.16 組織能力への還元

教育を受講者個人の習熟で閉じない。

```text
Training / Delegation Lab
↓
Observed Friction / Human Intervention
↓
Root Cause
├ Individual Skill
├ Team Operating Model
├ Harness
├ CI / Eval
├ Standard
└ Organization Constraint
↓
Improvement Backlog
↓
次回Training / Projectへ再投入
```

教育はDeepRailのOrganizational Learning Loopの一部である。

### 19.16.1 Why — なぜ個人AI活用とOrganization Capabilityは別物なのか

一人だけ、AIをものすごく使える人がいる。

その人は調査も速い。実装も速い。自分用のPromptやScriptを持ち、Agentへ任せるのも上手い。難しいTaskが来ると、周囲はその人へ頼る。

一見、AI Native化が進んでいるように見える。

ところが、その人が休むと止まる。別Teamへ移ると、やり方も一緒に消える。新人は再現できない。Security担当は何を許しているのか分からない。Managerは成果が本人のSkillなのか仕組みなのか判断できない。

これは強い個人であって、まだ強いOrganizationではない。

```text
個人ができる
↓
やり方を説明できる
↓
必要なContext / Rule / Evidenceが外部化される
↓
別の人・AIでも再現できる
↓
Teamの通常Flowへ入る
↓
測定・保守される
↓
別Teamへ移しても成立する
```

ここまで来て、初めて組織能力に近づく。

FlowDeskで、あるEngineerだけが代理承認FeatureをAIと高速に作れたとする。その人のLocal環境には便利なScriptがあり、頭の中にはDomain Ruleがあり、Review時の勘所も分かっている。完成物だけを見れば成功である。

でも次のTeamへ「同じようにAIでやって」と言っても再現しない。成功を生んだ条件が本人の中に残っているからだ。

そこで必要なのは、その人のPromptを全員へ配ることではない。何を任せたのか。どのContextが必要だったか。どのFailureが起きたか。何で正しさを確かめたか。どの判断だけHumanへ残したか。どのControlが再発防止に効いたか。

これらを取り出して、Work Design、Training、Harness、Standardへ変える。ここで初めて、個人の成功が会社の資産になる。

逆に、標準化しすぎても壊れる。優秀な人の手順を一字一句固定し、全員に同じTool、同じPrompt、同じAgent構成を強制すれば、Contextの違うTeamでは動かない。

横展開するべきなのは完成した作業手順ではない。**再現性を生んだ原則と、各Teamが自分のContextで再構成できるArtifact**である。

```text
Individual Practice
↓
Observed Friction / Success
↓
Principle / Context / Evidenceを抽出
↓
Standard / Harness / Trainingへ変換
↓
別Teamで再実行
↓
差分を学習
↺
```

Toolの利用率が高いことも、Prompt研修の受講者が多いことも、それだけではOrganization Capabilityの証明にならない。見るべきなのは、誰か一人の腕がなくても、同じ種類の仕事を安全に任せ、評価し、改善できるかである。

> **個人のAI活用は速度を作る。組織能力は、その速度を人が変わっても再現できる状態を作る。**

DeepRailが教育を「Toolを使える人を増やす」で終わらせないのは、この差を埋めるためである。

### 19.16.2 個人のSkillをTeamの再現性へ変える

教育成果を「受講者がToolを使えた」で閉じない。次のTransferまでを学習設計へ含める。

```text
Individual Practice
AIを使う / 任せる
        ↓
Real Theme Team Practice
実務に近いThemeをTeamで扱う
        ↓
Shared Reality / Context Assets
認識を揃え、仕様・用語・制約・判断理由を外部化
        ↓
Reproducibility
別メンバーが同じ仕事を再現
        ↓
Standard / Harness / Training
再利用可能な仕組みへ変換
        ↓
Organization Rollout
別Teamへ展開
```

実Themeを扱う理由は「本番コードをTrainingで作る」ことではない。現実のThemeには、架空課題では隠れやすい**暗黙前提、Roleごとの認識差、Decision Owner、Context Gap**が現れるからである。

Team Trainingでは、必要に応じてBusiness / Product / Decision Ownerも巻き込み、次を揃える。

- Problem / Outcome
- 前提・制約
- Domain Vocabulary
- Human / AIの役割
- Decision Owner
- Acceptance / Evidence
- 次に試す小さなScope

ただし、この事例だけでDeepRailの `Delegation / Evaluation / Harness / Organizational Capability` 全体が実証されたとは扱わない。**Team Practice / Context Asset / Adoptionに関する限定的な実践例**として扱い、その先のStandardization / Harness / Organization LearningはDeepRail自身の設計として区別する。

## 19.17 Golden Pathは「模範解答」ではなくFailure切り分け装置である

運営者は課題を事前にEnd-to-Endで完走し、Golden Pathを持つ。

目的は参加者へ答えを見せることではない。

```text
教材側Failure
Harness側Failure
Environment側Failure
参加者のDelegation / Judgment Failure
```

を切り分けることにある。

Golden Path自身もHarness / Runtime更新時に再実行し、古い成功例を教材として残さない。

## 19.18 教材を実運用資産から切り離しすぎない

教育専用のRule / Skill / Manualを大量に複製すると、運用資産と教材のDriftという新しい保守業務が生まれる。

推奨する構造：

```text
Operational Rule / Skill / Decision Record / Eval
        ↓ reference
Training Scenario / Exercise
```

運用資産自体を教材として再利用し、教育用シナリオは「どこを読むか」「何を経験するか」を定義する。

また教育の評価関数は組織成熟度で変える。

```text
Exploration
→ 良いFailureを発見し、Harnessへ還元できたか

Team Adoption
→ 別メンバー・別環境で再現できたか

Standardization+
→ Delegation / Evaluation / Enforcementを再現可能に運用できるか
```

> **学習初期ではFailureが出ること自体が失敗ではない。Failureを隠して完走する方が失敗である。**


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 13. なぜ最初に一人でEnd-to-End開発を体験するのか

**Creator / Lead Author: RIO AMADA**

## 19.6 AI Delegation Literacy — Tool利用の次に育てる能力

AI Literacyは少なくとも二層に分ける。

| Layer | 中心能力 | 典型的な問い |
|---|---|---|
| AI Usage Literacy | Prompt / Context / Toolを使ってAIから成果を得る | どう頼めばよいか |
| AI Delegation Literacy | Objective / Responsibility / Permission / Evidence / Evaluation / Escalationを設計して仕事を任せる | どこまで任せてよいか |

後者は、単なるTool SkillではなくManagement Skillに近い。

学習者が最終的に説明できるべきことは、Promptの工夫より次である。

```text
何をHumanが決めるか
何をAIへ任せるか
AIがどこまで自己評価してよいか
何をEvidenceとするか
どこで自動GOできるか
どこでHumanへ戻すか
どう失敗を検出し、回復するか
```

---

## 19.7 推奨学習形式 — 一人称End-to-End AI Development Lab

AI未経験〜初級者には、Frontendだけ、Backendだけの局所課題より、**Frontend + Backend + DB + Test + CIを一人称で横断する小規模な業務システム開発**を推奨する。

狙いはFull-stack Engineer化ではない。
一人のHumanが複数の専門責務を抱えることで、逐次指示・逐次確認がすぐに限界へ達し、AIへの委譲と仕組み化が必要になる状態を作ることである。

例：

```text
Task / Project Management App

Frontend
- React / Next.js等

Backend
- Node / FastAPI等

DB
- PostgreSQL等

Delivery
- lint
- unit test
- integration test
- build
- staging相当

Functions
- Login / Role
- CRUD
- Status / Assignee
- Comment
- Search / Filter
```

Runtime / Model / Frameworkは固定しない。
DeepRailが学習させたいのはVendor操作ではなくDelegation Designである。

---

## 19.8 開始前に書かせる7つの問い

開発開始前に、参加者は最低限次を記録する。

| 観点 | 問い |
|---|---|
| Outcome | 最終的に何が動けば成功か |
| Human Decision | 自分が必ず判断すべきだと思うものは何か |
| Delegation Candidate | AIへ丸ごと任せられそうなのは何か |
| Acceptance | 「できた」を何で判定するか |
| Evidence | AIの自己申告以外に何を見るか |
| Risk | AIに勝手に行わせたくないことは何か |
| Escalation | どの条件でHumanへ戻すか |

さらに、開始時点の **Human Decision Surface** を描く。

```text
Architecture      → Human
Implementation    → AI
Review            → Human
Test Confirmation → Human
DB Change         → Human
Release           → Human
```

これは終了後の変化を測るBaselineになる。

---

## 19.9 課題の難しさは「難解さ」ではなく「運用上の複雑さ」で作る

Harnessを自然発生させるために、難しいAlgorithmだけを出題してはならない。
それでは強いModelへ一発Promptする競技になり得る。

課題は、**継続してAIを働かせなければ完遂しにくい構造**を持たせる。

| 課題特性 | 自然に必要になる設計 |
|---|---|
| 複数Feature | Work Decomposition / Dependency |
| Front / API / DB横断 | Context / Boundary / Contract |
| Business Ruleが複数 | Rule / Source of Truth |
| 曖昧な要求 | Discover / Align / Human Decision |
| 同種作業の反復 | Skill / Reusable Instruction |
| Regression Risk | Test / Eval / Evidence |
| 危険な操作 | Permission / Gate |
| Environment差 | Provenance / Preflight |
| 長時間・複数Turn | Context Management / Living Document |
| 途中要求変更 | Re-plan / Re-decomposition / Reinvestment |
| Failure注入 | Retry / Recovery / Escalation |

> **「Harnessを作れ」と指示する前に、Harnessがないと辛い仕事を経験させる。**

ただし、学習目的と無関係なInfrastructure不具合で時間を失わせてはならない。
運営者はGolden Pathを事前完走し、教材側Failureと学習者側Failureを切り分ける。

---

## 19.10 段階学習 — Use → Delegate → Evaluate → Remove One Gate → Harness

学習は次の順で進める。

### Phase 0 — Baseline

AIへ任せる前に、Human Decision Surface、Risk、Acceptance、Evidence候補を記録する。

### Phase 1 — AIを使う

細かい依頼から開始し、通常のAI Codingを経験する。

```text
Human Instruction
↓
AI Output
↓
Human Full Check
```

### Phase 2 — AIへ仕事を任せる

Feature単位でObjective / Constraint / Acceptanceを渡し、Plan / Implement / Test / Fixまで任せる。

### Phase 3 — AI自身に評価させる

AIにCompletionを自己申告させるだけではなく、Acceptanceに対するEvaluationとEvidenceを生成させる。
Human評価と比較し、False Accept / False Reject / Unknownを観察する。

### Phase 4 — Human Gateを一つだけ外す

低Risk・機械検証可能・可逆なWork Classを選び、Evidenceが成立した場合だけHuman確認なしで次へ進ませる。

このPhaseで一度「任せても成立した」と実感できるかどうかが、その後の学習速度を大きく左右する。

> **「全部を自分で見なくても、条件を設計すれば成果は成立する」ことを体感する。**

### Phase 5 — FrictionをHarnessへ変える

繰り返し起きたHuman Interventionを分類し、Rule / Context / Skill / Permission / Hook / Eval / Gate / Toolへ還元する。

### Phase 6 — Change / Failure Eventを投入する

後述のイベントを投入し、Harness化した仕組みが変更下でも機能するかを見る。

---

## 19.11 Event-driven Challenge — 途中で仕事を変化させる

最初から完成要求をすべて渡さない。
演習途中で顧客・Security・Environment・Production相当のイベントを投入する。

例：

```text
Event 1
「管理者と一般Userで権限を分けてください」

Event 2
「担当者を1名から複数名へ変更してください」

Event 3
「Stagingで特定データだけ500 Errorになります」

Event 4
「既存Featureを壊さず検索条件を追加してください」

Event 5
「MigrationのRollback手段を説明できなければRelease不可です」
```

イベントの目的はSurpriseではない。

```text
Requirement Change
→ Source of Truthは更新されるか

Regression
→ Test / Evalが検出するか

Environment Failure
→ Code Failureと切り分けられるか

Permission Boundary
→ Agentが停止 / Escalateできるか

New Feature
→ Workを再分解できるか
```

を見る。

---

## 19.12 採点 — Product完成度より「安全な委譲」を測る

推奨配点例：

| 評価軸 | 配点例 | 主な観測対象 |
|---|---:|---|
| Outcome / Product Quality | 25 | 要求を満たし実際に動く |
| Evidence / Quality | 20 | Test / Eval / CIで完成を証明できる |
| Delegation Design | 20 | 責務・Decision Rights・Escalationを適切に委譲 |
| Harness Design | 20 | Rule / Context / Skill / Gate等を摩擦から仕組み化 |
| Change / Recovery | 10 | 要求変更・Failureへ再計画・回復できる |
| Learning / Reflection | 5 | Human Interventionの変化を説明できる |

次は加点理由にしない。

- Agent数が多い
- Prompt数が少ない
- 特定Vendorの高度機能を多用した
- 完成Feature数だけが多い

中心評価は次である。

> **品質とRiskを維持したまま、Humanが逐次介入しなくてよい領域をどこまで根拠付きで広げられたか。**

---

## 19.13 Before / AfterでHuman Decision Surfaceを比較する

終了時に、開始時と同じDecision Mapを再作成する。

例：

```text
Before
Architecture      → Human
Implementation    → AI
Review            → Human
Test Confirmation → Human
DB Change         → Human
Release           → Human

After
Architecture      → AI Proposal + High-Risk Human Decision
Implementation    → AI
Review            → AI Eval + Exception Review
Test Confirmation → Machine Evidence
DB Change         → AI + Migration Gate
Release           → Human
```

単にHuman項目が減れば良いわけではない。
Gateを外した箇所について、参加者は必ず次を説明する。

```text
何を任せたか
↓
なぜ任せられるのか
↓
Evidenceは何か
↓
Failureを検知できるか
↓
戻せるか
↓
Escalation条件は何か
```

これによりHuman Gate削減を、感覚的なAI信頼ではなく**Decision Rightsの設計**として学ぶ。

---

## 19.14 最終発表 / Retro — 「何を作ったか」だけで終わらせない

最終発表では最低限次を扱う。

1. 何を作ったか
2. 最初はHumanが何を判断していたか
3. どこでAI利用が苦しくなったか
4. どのFrictionからどのHarness要素が生まれたか
5. 何をAIへ追加委譲したか
6. どのHuman Gateを外したか、そのEvidenceは何か
7. どこはまだHumanへ残したか、その理由は何か
8. 次回なら何をさらに仕組み化・委譲するか

振り返りの中心質問：

> **今回、人間が介入した箇所を、次回はどの条件・仕組み・Evidenceによって減らせるか。**

この問いはHarness Retroと同じであり、個人学習をそのままTeam / Organization Learningへ接続する。

---

## 19.15 運営者の責務 — 「発見」を設計する

運営者は講師というよりLearning Environment Designerとして振る舞う。

- 事前にGolden Pathを完走する
- 学習目的外のEnvironment障害は速やかに除去する
- 学習目的のFrictionはすぐ答えを教えず、観察させる
- Human Intervention回数・理由を記録させる
- 途中イベントを一貫したScenarioとして投入する
- Gate削減時はEvidence / Risk / Reversibilityを確認する
- AI / Humanの評価差分を記録させる
- 特定Toolの技巧ではなく、再利用可能な原則へ言語化させる

教育の成功条件は、全員が同じHarnessを作ることではない。

> **参加者自身が「なぜ仕組みが必要になったか」を説明でき、安全なDelegationを一度成功させること。**

---

## 19.16 組織能力への還元

教育を受講者個人の習熟で閉じない。

```text
Training / Delegation Lab
↓
Observed Friction / Human Intervention
↓
Root Cause
├ Individual Skill
├ Team Operating Model
├ Harness
├ CI / Eval
├ Standard
└ Organization Constraint
↓
Improvement Backlog
↓
次回Training / Projectへ再投入
```

教育はDeepRailのOrganizational Learning Loopの一部である。

### 19.16.1 Why — なぜ個人AI活用とOrganization Capabilityは別物なのか

一人だけ、AIをものすごく使える人がいる。

その人は調査も速い。実装も速い。自分用のPromptやScriptを持ち、Agentへ任せるのも上手い。難しいTaskが来ると、周囲はその人へ頼る。

一見、AI Native化が進んでいるように見える。

ところが、その人が休むと止まる。別Teamへ移ると、やり方も一緒に消える。新人は再現できない。Security担当は何を許しているのか分からない。Managerは成果が本人のSkillなのか仕組みなのか判断できない。

これは強い個人であって、まだ強いOrganizationではない。

```text
個人ができる
↓
やり方を説明できる
↓
必要なContext / Rule / Evidenceが外部化される
↓
別の人・AIでも再現できる
↓
Teamの通常Flowへ入る
↓
測定・保守される
↓
別Teamへ移しても成立する
```

ここまで来て、初めて組織能力に近づく。

FlowDeskで、あるEngineerだけが代理承認FeatureをAIと高速に作れたとする。その人のLocal環境には便利なScriptがあり、頭の中にはDomain Ruleがあり、Review時の勘所も分かっている。完成物だけを見れば成功である。

でも次のTeamへ「同じようにAIでやって」と言っても再現しない。成功を生んだ条件が本人の中に残っているからだ。

そこで必要なのは、その人のPromptを全員へ配ることではない。何を任せたのか。どのContextが必要だったか。どのFailureが起きたか。何で正しさを確かめたか。どの判断だけHumanへ残したか。どのControlが再発防止に効いたか。

これらを取り出して、Work Design、Training、Harness、Standardへ変える。ここで初めて、個人の成功が会社の資産になる。

逆に、標準化しすぎても壊れる。優秀な人の手順を一字一句固定し、全員に同じTool、同じPrompt、同じAgent構成を強制すれば、Contextの違うTeamでは動かない。

横展開するべきなのは完成した作業手順ではない。**再現性を生んだ原則と、各Teamが自分のContextで再構成できるArtifact**である。

```text
Individual Practice
↓
Observed Friction / Success
↓
Principle / Context / Evidenceを抽出
↓
Standard / Harness / Trainingへ変換
↓
別Teamで再実行
↓
差分を学習
↺
```

Toolの利用率が高いことも、Prompt研修の受講者が多いことも、それだけではOrganization Capabilityの証明にならない。見るべきなのは、誰か一人の腕がなくても、同じ種類の仕事を安全に任せ、評価し、改善できるかである。

> **個人のAI活用は速度を作る。組織能力は、その速度を人が変わっても再現できる状態を作る。**

DeepRailが教育を「Toolを使える人を増やす」で終わらせないのは、この差を埋めるためである。

### 19.16.2 個人のSkillをTeamの再現性へ変える

教育成果を「受講者がToolを使えた」で閉じない。次のTransferまでを学習設計へ含める。

```text
Individual Practice
AIを使う / 任せる
        ↓
Real Theme Team Practice
実務に近いThemeをTeamで扱う
        ↓
Shared Reality / Context Assets
認識を揃え、仕様・用語・制約・判断理由を外部化
        ↓
Reproducibility
別メンバーが同じ仕事を再現
        ↓
Standard / Harness / Training
再利用可能な仕組みへ変換
        ↓
Organization Rollout
別Teamへ展開
```

実Themeを扱う理由は「本番コードをTrainingで作る」ことではない。現実のThemeには、架空課題では隠れやすい**暗黙前提、Roleごとの認識差、Decision Owner、Context Gap**が現れるからである。

Team Trainingでは、必要に応じてBusiness / Product / Decision Ownerも巻き込み、次を揃える。

- Problem / Outcome
- 前提・制約
- Domain Vocabulary
- Human / AIの役割
- Decision Owner
- Acceptance / Evidence
- 次に試す小さなScope

ただし、この事例だけでDeepRailの `Delegation / Evaluation / Harness / Organizational Capability` 全体が実証されたとは扱わない。**Team Practice / Context Asset / Adoptionに関する限定的な実践例**として扱い、その先のStandardization / Harness / Organization LearningはDeepRail自身の設計として区別する。

## 19.17 Golden Pathは「模範解答」ではなくFailure切り分け装置である

運営者は課題を事前にEnd-to-Endで完走し、Golden Pathを持つ。

目的は参加者へ答えを見せることではない。

```text
教材側Failure
Harness側Failure
Environment側Failure
参加者のDelegation / Judgment Failure
```

を切り分けることにある。

Golden Path自身もHarness / Runtime更新時に再実行し、古い成功例を教材として残さない。


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 14. 仕事はどこから生まれるのか

**Creator / Lead Author: RIO AMADA**

# DR-M24. 24_要求供給・受入運用ガイド

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


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 15. 顧客・利用者の本当の要求を発見する

**Creator / Lead Author: RIO AMADA**

## 縦断ケース — FlowDesk「代理承認」

**仮ケース:** 既存B2B SaaSへ「申請・承認ワークフロー」を追加するBrownfield Project。  
本書の縦断ケースでは、Frontend / Backend / DB / Authorization / Notification / Test / CI/CD / Release / Auditを横断できる架空の題材を使う。

Caseを一章に閉じず、本全体を通じて再登場させる。

```text
Business Request
↓
Discover — 誰の何のProblemか
↓
Domain / Shared Reality — Role / Rule / Exceptionを理解
↓
Shape / Align — Scenario / UI / API / Stateを具体化
↓
Specify — Acceptance / Constraint / Unknownを外部化
↓
Work Breakdown — Independent Outcome / Dependency / Risk
↓
Human-AI Allocation — Delegation Envelopeを決める
↓
Parallel Execution — Isolation / Verifiable Parallelism
↓
Failure — Requirement Change / Conflict / Permission / CI Failure
↓
Evaluation — Independent Check / Evidence / Decision Trail
↓
Review — Decision Packet / Progressive Disclosure
↓
Release — Promotion / Production Verification / Rollback
↓
Reinvest — Rule / Test / Harness / Standardを更新
↓
Organization Learning — 別TeamへTransfer
```

Caseで必ず出すFriction：

- 途中のRequirement Change
- Domain用語の認識ズレ
- Agent間のParallel Conflict
- Testでは検出できないAcceptance Gap
- Permission / Security Boundary
- CI / Environment由来のFailure
- Human Gateを残すべきDecision
- Release後の想定外挙動またはRollback判断
- RetroからStructural Reinvestmentへ変換する場面

Case Artifact：

```text
Shared Reality Note
Decision Record
Specification / Acceptance
Agent Task Contract
Dependency / Work Graph
Delegation Contract
Verification Procedure
Evidence Packet
Delegation Decision Trail
Review / Decision Packet
Release Evidence
Retro / Reinvestment Change
```

### 0D.1.1 Case Identity — FlowDesk「代理承認」拡張（架空）

本書で繰り返し扱うCaseは、架空の既存B2B SaaS **FlowDesk** とする。FlowDeskは企業内の購買・経費・契約等の申請を、組織ルールに応じて承認へ回す既存サービスである。Case開始時点で基本的な申請・承認機能はすでにProductionで稼働している。

今回のBusiness Requestは短い。

> **「承認者が不在のとき、代理の人が承認できるようにしてほしい。」**

この一文を、そのままFeatureへ変換してはいけない。`代理`、`不在`、`承認できる` の意味がStakeholderごとに違うためである。Case全体は、この短い依頼をAIが働ける仕事へ変換し、複数Agentへ委譲し、Evidenceで評価し、Release後のFailureをStructureへ戻すまでを追う。

**Caseは必ず架空であることを明示し、著者自身の実案件として語らない。**

### 0D.1.2 Stable Actors / Domain Vocabulary

章ごとにRole名や意味を変えない。以下をCaseのCanonical Vocabularyとする。

| Term | Case内の意味 | 注意点 |
|---|---|---|
| Requester | 申請を提出する人 | 自分の申請を自分で承認できない |
| Approver | 現在の承認StepにDecision Rightsを持つ人 | 組織上の役職名とは一致しない場合がある |
| Proxy Approver | 一定条件でApproverの代わりに判断する人 | `代理`は恒久的なRoleではない |
| Budget Owner | 金額条件等で追加承認を持つ人 | Approverと同一人物の場合もある |
| Compliance Approver | 特定Categoryで追加Decisionを持つ人 | Human Gateを残す候補 |
| Tenant Admin | 組織設定を管理する人 | 個別申請の承認者とは別責務 |
| Auditor | 後からDecisionと代理関係を追跡する人 | 実行権限を持たない |
| Approval Route | 申請が通るDecision Stepの集合 | 途中変更時の扱いが重要 |
| Delegation Rule | 誰が、誰の、何を、いつまで代理できるか | Tool PermissionではなくDecision Rightsに関わる |
| Approval Evidence | 誰が何の権限で何を決めたかを示す記録 | UI表示だけでは不十分 |

このVocabularyはShared Realityの一部を支えるContext Assetであり、Vocabulary一覧そのものがShared Realityではない。

### 0D.1.3 Initial Business Rules / Open Questions

Case開始時点で確認済みのRuleと、まだ決めていないUnknownを分離する。

**Known Rules**

1. Requesterは自分の申請を承認できない。
2. Proxy Approverによる承認でも、元のApproverと実際にDecisionした人の両方をAuditできなければならない。
3. Proxy権限には開始日時・終了日時がある。
4. Tenantをまたいだ代理設定は禁止する。
5. Rejectされた申請は後続Stepへ進まない。
6. 同じStepを二重に承認しても、Outcomeが二重適用されてはならない。
7. Notification送信失敗とApproval Decisionの成立は分離する。
8. Release後も既存の非代理承認Flowを壊してはならない。

**Open Questions at Start**

- 金額が一定以上の場合もProxyを許すのか。
- Proxyはすべての申請Categoryを代理できるのか。
- 申請後に代理設定が変わった場合、既存Requestへ反映するのか。
- Approval RouteはSubmission時にFreezeするのか、Decision時に再評価するのか。
- Proxyがさらに別のProxyへ委譲できるのか。
- 緊急時にTenant Adminが例外承認できるのか。

DeepRailのCaseでは、Unknownを「あとで人間が適当に補完する前提」にしない。`Open Question` としてSource of Truthへ置き、誰がDecision Ownerかを明示する。

### 0D.1.4 Brownfield Constraints

FlowDeskはGreenfieldではない。すでに利用者・既存API・既存Data・既存運用がある。Case内で固定する制約は次とする。

```text
Existing UI / API compatibility
Existing approval records must remain readable
Tenant isolation must not weaken
Audit history is append-oriented
Production data is not freely available to coding agents
Shared integration environment has finite capacity
Release requires production verification and rollback path
Notification is an external dependency
Existing clients may assume current status / response shapes
```

特定のCloud / VCS / Issue Tracker名はCaseの成立条件にしない。Caseの目的はTool比較ではなく、BrownfieldでControl Objectiveをどう守るかを見せることである。

### 0D.1.5 Friction Timeline — Caseで意図的に起こす9つの出来事

CaseのFailureはランダムに足さない。DeepRailの概念が必要になる順で発生させる。

| Friction | 発生Scene | 表面上の問題 | DeepRailで扱う本質 | 主なArtifact / Action |
|---|---|---|---|---|
| F-C01 Vocabulary Drift | Discover / Align | `代理`の意味が人によって違う | Shared Reality不足 | Vocabulary / Scenario更新 |
| F-C02 Requirement Change | Specify後 | 高額申請ではProxy禁止が後から判明 | Specは固定文書ではなくDecision更新を受ける | Decision Record / Re-decompose |
| F-C03 Parallel Conflict | 実装中 | 2 Agentが同じState / Schema境界を変更 | Parallelismの独立性不足 | Work Graph再設計 / Isolation |
| F-C04 Acceptance Gap | Test Green後 | 機能は動くが「誰の代理か」が画面と監査で不明瞭 | Machine TestとBusiness Acceptanceの差 | Scenario Eval / Evidence追加 |
| F-C05 Permission Boundary | Verification時 | Agentが本番相当Dataへアクセスできない | Permissionは障害ではなく設計条件 | Synthetic Fixture / Least Privilege |
| F-C06 Environment Failure | Integration時 | Shared環境のState差で再現しないFailure | Environment StateもEvidenceの一部 | Provenance / Preflight / Cleanup |
| F-C07 Human Decision Surface | Release前 | 監査上の代理表記をAIだけで確定できない | 高Risk・Accountability Decision | Human Gate / Decision Packet |
| F-C08 Production Surprise | Release後 | 旧Clientが新しいResponse / State解釈で誤動作 | Merge完了とOutcome完了は違う | Prod Verification / Rollback or Fix Forward |
| F-C09 Reinvestment | Retro | 同種Failureが再発し得る | 学習を文章で終わらせない | Contract Test / Rule / Gate / Harness更新 |

最終Book Compilerは、これらを「DeepRailを使わなかったから失敗した」という単純な勧善懲悪にしない。**新しい情報や現実の制約によって設計が更新されるのは正常であり、その更新を安全に扱えるかが問題**として描く。

### 0D.1.6 Delegation Profile — 何をAIへ任せ、何を残すか

Case開始時点からHuman / AI境界を固定しない。Work Classごとに仮のOperating Profileを置き、Evidenceが揃えば更新する。

| Work Class | 初期Profile | AIへ任せる内容 | Human / Policy側に残す内容 | 拡張条件 |
|---|---|---|---|---|
| Domain Research | Bounded | 既存仕様・Code・TicketからRule候補抽出 | Business意味の採否 | Domain Expertとの一致率 / Unknown可視化 |
| Scenario / Prototype | Bounded | UI / API / State候補生成 | 主要User OutcomeのDecision | Alignment Evidence |
| Work Breakdown | AI-first | Task / Dependency / Parallel候補 | High-risk boundary / Human Gate | 独立AcceptanceとRollback可能性 |
| Implementation | High | Code / Test / Migration draft | 例外Decision | Verification Strength |
| Verification | AI-first | Test / Runtime Check / Evidence収集 | 高Risk Unknownの判定 | Calibration / False Accept低下 |
| Release Decision | Low–Medium | Release Packet / Risk要約 | Go / No-Goの指定Class | Production Evidence / Policy成熟 |
| Audit Semantics | Low | 選択肢・影響分析 | Accountabilityを伴う意味決定 | Policy化されるまでHuman Gate |

この表は成熟度Badgeではない。同じCaseでもWork Classごとに異なるAutonomy / Evaluation Authority / Approval Strengthを持つ。

### 0D.1.7 Canonical Case Artifacts — 最低限の中身

Caseに登場するArtifactは飾りではなく、次の責務を持たせる。

**Shared Reality Note**

```text
Problem / Outcome
Domain Vocabulary
Known Rules
Scenarios
Constraints
Open Questions
Decision Owners
Source of Truth pointers
```


---

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


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 16. 曖昧な要求を「見える形」にする

**Creator / Lead Author: RIO AMADA**

**Delegation Contract**

```text
Objective
Scope
Permission
Acceptance
Required Evidence
Forbidden Actions
Escalation Conditions
Expiry / Re-evaluation Trigger
```

**Verification Procedure**

```text
Precondition
Environment / Version / Fixture
User-visible Action
Expected Observable Result
Side-effect Check
Audit Check
Evidence Location
Cleanup
Re-run Constraint
```

**Delegation Decision Trail**

```text
Decision
Why
Evidence Pointer
Result
Deviation
Open Risk / Unknown
```

**Decision Packet**

```text
Outcome
Important Decisions
Acceptance Evidence
Risk / Unknown
High-risk Artifact pointer
Deviation / Exception
Decision requested from Human / Policy
```

Final proseではArtifact全文を毎回掲載しない。本文では読者がDecisionできる最小Sliceだけ見せ、完全TemplateはAppendix / Repositoryへ逃がす。

### 0D.1.8 Evidence Design — 「Test Green」をCaseの終点にしない

代理承認FeatureのEvidenceを、検出対象ごとに分ける。

| Claim | 主なEvidence | Failureをどう検出するか |
|---|---|---|
| 通常承認を壊していない | Regression Test / Runtime path | 既存Scenarioの差分 |
| Proxy期間外は承認不可 | Boundary Test / Time fixture | 開始前・終了後Scenario |
| 自己承認不可 | Deterministic Rule Check | Requester=Decision Actor |
| 誰の代理か追跡可能 | Audit Record / UI / API Evidence | Original + Acting identityの欠落 |
| 二重承認で二重反映しない | Idempotency / Concurrency Verification | Duplicate request / race |
| Tenant越境しない | Authorization / Isolation Eval | Cross-tenant attempt |
| Notification FailureでDecisionが壊れない | Failure Injection | External dependency error |
| 高額申請でProxy禁止 | Business Scenario Eval | Threshold境界 |
| 旧Clientを壊していない | Compatibility Verification | Existing response consumer |

> **Caseで示すのは「Testを増やせば安全」ではない。Claimごとに、何がそのClaimを反証できるかを設計する。**

### 0D.1.9 Scene Map — 本の中でどう再登場させるか

Caseを各章へ均等配分しない。読者の認識が変わるポイントでだけ再登場させる。

```text
Scene 1 — 一行のBusiness Request
Part I / II
「AIへ渡せば作れる」に見えるところから始める

Scene 2 — `代理`という一語が崩れる
Part III
Domain / Shared Reality / Align / Specify

Scene 3 — きれいなTask分解が並列Conflictを起こす
Part IV / V
Work Breakdown / Delegation / Isolation / Parallelism

Scene 4 — TestはGreenなのに承認できない
Part VI
Acceptance / Evidence / Independent Evaluation

Scene 5 — Release前にHuman Gateが戻る
Part IV / VI
Risk / Accountability / Decision Rights

Scene 6 — Productionで旧Clientが壊れる
Part VI
Production Verification / Rollback / Failure Routing

Scene 7 — Retroで「注意事項」を書かない
Part VI / VII
Rule / Contract Test / Gate / HarnessへReinvest

Scene 8 — 別Teamが同じ仕組みを利用する
Part VIII / Ending
個人の成功ではなくOrganization Capabilityへ
```

### 0D.1.10 Continuity Contract — Book Compilerが守るCase不変条件

1. Feature目的を途中で別機能へ差し替えない。
2. `Proxy Approver` の意味を章ごとに変えない。変更する場合はDecisionとして記録する。
3. 既に確定したRuleを、説明の都合だけで忘れない。
4. Unknownが決まった場合、以降の章では決定済みとして扱う。
5. Failureは後の章でReinvestmentへ接続し、放置しない。
6. 同じFailureを別の名前で重複して「新しい問題」として出さない。
7. Human Gateは物語上の安心材料として無条件に置かない。Risk / Detectability / Reversibility / Accountabilityで理由を説明する。
8. AIが突然万能・無能にならない。Capability差はWork Class / Evidence / Environmentで説明する。
9. Caseの成功指標はCode量・Agent数・Human Check削減数ではない。
10. 最後に、何がStandard / Harness / Trainingへ戻り、次のTeamのExecutionがどう変わったかを示す。

### 0D.1.11 Case Completion Criteria

Case Study本文が完成したと言えるのは、次を満たしたときである。

- 読者が最初のBusiness RequestからRelease / Reinvestmentまで因果を追える
- 9つのFrictionがすべて自然な原因から発生する
- 最低1回、AIの提案よりHuman判断が正しい場面を含む
- 最低1回、Humanの初期判断よりAI / Machine Evidenceが正しい場面を含む
- 最低1回、Criteria自体が曖昧で「どちらが正しい」と言えないDisagreementを含む
- `Test Green ≠ Outcome Proven` を具体Sceneで体験できる
- ParallelismがAgent数ではなくWork独立性で制約されるSceneがある
- Production FailureまたはCompatibility GapからRecoveryする
- RetroがDocument追記ではなくStructure変更へ到達する
- 最後に別Teamが再利用できるArtifact / Standardが残る

> **このCaseのEndingは「AIがうまく実装して終わった」ではない。「次のTeamは、同じFailureをゼロから学び直さなくてよくなった」で閉じる。**

### FlowDesk「代理承認」拡張（架空ケース）


---

## 9.5 実装前の認識合わせを標準責務として持つ

実装前に要求・設計・Domain理解を十分に掘り下げ、未確定事項を実装工程へ持ち込まない。

主な内容：
- Codebaseから回答できる事項を調査する
- Domain Vocabularyを確定する
- 既存のDomain ModelやDocumentとの矛盾を検出する
- Acceptance Criteriaを確認する
- UI / API / DB / 外部IF等を必要に応じて可視化する
- Test Seamを確認する
- 後戻りコストが高いDecisionを明文化する
- 次責務が推測なしで開始できる状態を作る

確定情報はSession内だけに残さずSource of Truthへ反映する。

### 9.5.1 Domain理解は「実装前に受け取る完成資料」ではない

複雑なDomainでは、最初から完全なRequirement / Domain Modelが存在するとは限らない。Domain Expert、Product、Engineer、AIがResearch / Design / Implementation / Feedbackを往復しながら、理解とModelを更新する。

一度ヒアリングして要件を書けば終わり、とはならない。Problem、Domain、Scenario、Acceptanceは、実装やFeedbackで何度も更新される。ここまで含めて、**Shared Realityを育て続けるKnowledge Work**になる。

```text
Domain / Problemを調べる
↓
言葉・Rule・例外を仮説化する
↓
Scenario / Model / Prototype / Codeへ表す
↓
違和感・矛盾・Unknownを発見する
↓
Domain理解を更新する
↺
```

AIはResearch / Comparison / Draft / Model候補の生成を大きく加速できる。ただし、AIの提案を採用するには、Teamが「何が妥当か」を判断できるだけのProblem / Domain理解とEvaluation Criteriaを持つ必要がある。

ここでもHuman-only責務を固定しない。AI CapabilityとEvaluation Reliabilityが上がればDomain分析・Model提案・Consistency Check等も委譲できるが、**何を正とするかを外部化し、Evidenceで更新できる構造**は維持する。

### 9.5.1.1 Why — なぜ実装が速くなるほどDomain理解の価値が上がるのか

最初に、一つだけ言っておきたい。

**AIで速くなったのは、形にすることだ。何を正しいとするかまで、自動的に分かるようになったわけではない。**

架空のFlowDeskでは、依頼は一文から始まる。

> **「承認者が不在のとき、代理の人が承認できるようにしてほしい。」**

短い。実装できそうにも見える。

AIに渡せば、代理承認用の項目を足し、APIを作り、画面に操作を増やし、Testまで書ける。コードを書くことだけを見れば、仕事はかなり前へ進んだように見える。

ところが、この一文にはまだ答えが入っていない。

代理とは一時的な権限なのか。誰が「不在」を決めるのか。高額な申請も代理してよいのか。代理設定が途中で変わったら、すでに流れている申請はどうするのか。監査には、実際にボタンを押した人だけを残せばよいのか。それとも、誰の権限を使ったのかまで残すのか。

コードを書けば、この問いにも答えが出るわけではない。

むしろ怖いのは、AIが止まらずに形にしてしまうことだ。曖昧な要求が、曖昧なままではなく、もっともらしい画面やAPIやData Modelとして固定される。

**曖昧さが消えるのではない。曖昧さに実装という形が付く。**

AI以前の開発にも同じ問題はあった。ただ、実装そのものに時間がかかっていた。設計し、書き、Reviewし、試すまでの途中で、「そもそもこの理解で合っているか」と人が立ち止まる時間が偶然入り込むことがあった。

生成が速くなると、その余白はあてにできない。

では、上流工程を重くして、巨大な仕様書を完成させてからAIへ渡せば安心か。

そうとも限らない。

複雑な仕事では、作ってみて初めて分かることがある。Prototypeを触った利用者が「そういう意味ではない」と気づく。Testを書いて初めて例外が見える。既存Codeを調べたAIが、文書にはなかったRuleを見つけることもある。

実装は、理解の終点ではない。理解を進めるための材料にもなる。

この往復を、Knowledge Loopと呼ぶ。

```text
Problem / Domainを調べる
↓
言葉・Rule・Scenarioを仮説にする
↓
Prototype / Code / Testへ表す
↓
現実とのズレ・例外・Unknownが見つかる
↓
Shared Realityを更新する
↓
Specification / Acceptance / Workを更新する
↺
```

このLoopを、人だけの仕事に固定する必要もない。AIは既存資料とCodeを調べ、用語の候補を整理し、矛盾を探し、Scenarioを増やし、Model案を比較できる。能力と評価の仕組みが上がれば、Domain分析のかなりの部分も任せられる。

ただし、候補を作る能力と、何を採用するかを決められる状態は別である。

100個の案を出せても、何をもって正しいOutcomeとするかが曖昧なら、選べない。だからShared Realityが必要になる。

Shared Realityは、最新の仕様書が一冊あることではない。人とAIが、問題、言葉、Rule、制約、決定、Acceptanceについて、次の仕事を推測だけで始めなくてよい程度に理解を揃えている状態である。Vocabulary、Scenario、Decision Record、Specification、Test、CodeといったContext Assetは、その状態を作り直すために使う。

FlowDeskでも、最初の画面が動いただけでは終わらない。高額申請を代理承認してよいかが未決なら、そのUnknownを見える場所へ置く。Decision Ownerを決める。Riskの低い範囲では先に試す。そして、分かったことを仕様とAcceptanceへ戻す。

全部決めてから作るのでもない。分からないまま作り切るのでもない。

**速く作れるからこそ、理解と実装を短く往復する。**

`Discover → Shape / Visualize → Align → Decide → Specify` は、AIにコードを書かせる前の儀式ではない。仕事の意味を更新し続けるための活動である。実装から新しい事実が返ってきたら、何度でも戻る。

実務で見るべきことは、難しくない。

- 同じ言葉を、関係者とAIが同じ意味で使っているか
- Ruleと例外を分けて説明できるか
- まだ決まっていないことが見えているか
- 何をもって正しいとするかが外へ出ているか
- 作って分かったことを、どこへ戻すか決まっているか

最初の一文へ戻ろう。

「代理の人が承認できるようにしてほしい」。

AIが速ければ、この一文からすぐに機能は作れる。だからこそ、その速さに引っ張られて、一文の意味まで決まった気になってはいけない。

> **AIが実装Costを下げるほど、「何を作るのか」「何を正解とするのか」を更新し続ける能力の価値が上がる。**

### 9.5.2 ContextはAI専用PromptではなくTeam Development Assetである

ここをShared Reality / Context AssetのCanonical Homeとする。以降の章では、この定義を前提として使う。

ここで `Shared Reality` と `Context Asset` を分離する。

- **Shared Reality:** Human / AIがProblem・Domain・Decision・Acceptanceについて十分な共通理解を持つ状態
- **Context Asset:** その状態を作り直し、検証し、別Session / 別Memberへ再利用するために外部化された情報

次をAIへの一時入力だけにしない。

- 仕様
- Domain Vocabulary / 用語
- Business Rule
- Constraint
- Architecture / Design Intent
- Decision / Rationale
- Acceptance Criteria
- Known Unknown

HumanとAIが同じSource of Truthを参照できるようにし、変更時にはReinvest / Learnで更新する。

> **Context整備はAIの回答精度向上だけではなく、Teamの開発判断を共有・再現するための投資である。**

AIがCodingやDraftを高速化しても、Domain理解・Modeling・Knowledge Crunchingの責務は消えない。DeepRailでは、これらを `Knowledge Loop / Shared Reality / Domain Modeling` として、実装速度とは別に維持・更新する。

---


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 17. 同じものを見て認識を合わせる

**Creator / Lead Author: RIO AMADA**

> **一行の依頼は、AIならすぐ形にできる。だから、その一行の意味まで決まった気にならない方がいい。**

ここから、架空のB2B SaaS「FlowDesk」に代理承認機能を追加する案件を追う。始まりは一行の依頼だ。そこからRelease後の学習まで進むあいだに、認識はずれ、要件は変わり、Agent同士も衝突する。Testが通っているのに足りない場面もあれば、Productionで初めて見える問題も出てくる。

失敗するかどうかだけを見ても、このCaseの意味は分からない。

**失敗やUnknownが現れたとき、それを次の判断に使えるEvidenceへ変え、仕事の切り方・権限・評価・Harnessを更新できるか。**

その後の動きに、AI Nativeな開発の差が出る。

#### Scene 1 — 「代理で承認できるようにしてほしい」

依頼は短かった。

> 「承認者が不在のとき、代理の人が承認できるようにしてほしい。」

従来なら、担当者がいくつか質問し、画面案を作り、APIやDB変更へ進んでいたかもしれない。AIがいると、さらに誘惑が強い。既存Repositoryを読み、現在の承認処理を探し、必要そうな差分を作らせれば、数十分でそれらしい実装案が出る。

実際、最初のAI Researchでも案はすぐに出た。

既存の `Approver` に対して `Proxy Approver` を紐づける。代理期間を持たせる。承認時には、本人か代理人かを判定する。UIには「代理承認」と表示する。Audit Logには実行者を残す。

悪くない。むしろ、ぱっと見れば十分に見える。

問題は、「代理」という言葉を全員が同じ意味で使っていなかったことだった。

Product側が思い浮かべていたのは、休暇中の承認者と同じ権限を一時的に持つ人だった。Compliance側は、金額や申請Categoryによっては代理できないDecisionがあると考えていた。Tenant Admin側は、組織設定として代理者を登録する機能を想像していた。Auditorが知りたいのは、誰がボタンを押したかだけではない。「誰の権限を代行し、どのRuleの下でそのDecisionが有効だったのか」を、後から説明できる必要があった。

同じ「代理」でも、見ている仕事が違っていた。

ここでAIの最初の提案を採用していたら、コードは書けただろう。Testも作れただろう。ただし、そのTestが証明するのは「実装した代理承認が実装どおりに動くこと」であって、「事業が必要としている代理承認を作ったこと」ではない。

Teamは、まず実装を止めた。

止めたといっても、AIを止めたわけではない。AIには既存仕様、過去のTicket、Code、監査関連のDocumentから、`代理`、`承認者`、`Decision Actor`、`Audit` に関係するRule候補と矛盾候補を抽出させた。その結果をDomain Expertと確認し、VocabularyとScenarioを更新した。

AIのResearchは、そのまま答えにはしなかった。AIは探索範囲を広げ、見落としていそうなRuleや矛盾を出す。採用するかどうかは、現在のBusiness MeaningとAccountabilityを持つStakeholderを含めて決める。決まった内容もConversationの中に置き去りにせず、Shared Reality Noteへ戻した。

最初の依頼は、一行のままだった。

しかしTeamが扱う仕事は、もう一行ではなかった。

`代理` とは恒久Roleではない。開始日時と終了日時を持つ。Requesterは自分の申請を承認できない。代理でDecisionした場合、元のApproverと実際のDecision Actorを両方追える必要がある。Tenantをまたいではいけない。Notification失敗とApproval Decisionの成立は分離する。

一方で、まだ決まっていないことも残った。

高額申請でも代理してよいのか。特定Categoryは対象外か。Submission後に代理設定が変わったら、既存Requestにも効くのか。Approval Routeはいつ確定するのか。

ここでUnknownを無理に消さなかった。

**分からないことを、分かったふりで仕様に埋め込む方が危ない。**

Open Questionとして残し、それぞれにDecision Ownerを置いた。

#### Scene 2 — 仕様ができたあとで、要件が変わる

Shared Realityが整い、Scenarioが具体化されると、AIは仕事を進めやすくなった。UI案、APIの変更点、State Transition、Data Model候補、Acceptance Criteriaが短時間で作られ、Teamは同じ具体物を見ながら話せるようになった。

ここまでくると、「最初にちゃんと要件を固めたから、あとは実装するだけ」と考えたくなる。

だが、現場ではそこで終わらない。

Specifyの後、Complianceから追加のRuleが出た。

「一定金額を超える申請は、代理承認を許可しないでほしい。」

最初の打ち合わせでは明示されていなかったRuleだった。しかも単なるUI制御ではない。Approval Decisionそのものの有効性に関わる。

ここで二つの反応があり得る。

一つは、「要件変更だから後から追加する」。もう一つは、「最初に言ってほしかった」と責任の所在を探す。

どちらに寄っても、仕事は前へ進まない。

新しいBusiness Ruleが入ったなら、すでに作ったSpec、Work Breakdown、Test、Delegation Contractのどこまで影響するかを洗い直す。変更そのものは珍しくない。**変更のあと、何を更新すれば再び安全に任せられる状態へ戻れるか。** そこを見た方がいい。

AIにImpact Analysisをさせると、想定より影響が広かった。

BackendのAuthorizationだけではない。UI上で代理承認ボタンを出す条件、API Errorの意味、Boundary Test、Audit Reason、Notification文言、Approval Routeの表示、既存Requestへの適用条件まで影響する。

さらにAIは、既存仕様と新Ruleの間に一つの矛盾を指摘した。

「代理設定は申請後でも変更できる」という現在の案と、「高額申請では代理禁止」を組み合わせたとき、既存Requestが代理可能状態から代理不可へ途中で変化する可能性がある。

人間側では「金額判定を承認時に見ればいい」という初期案が出ていた。しかしAIが既存CodeとState Transitionをたどると、一部のRoute情報がSubmission時にSnapshotされていることが分かった。人間の初期理解より、Machine Evidenceの方が正しかった。

ここでAIと人間の勝ち負けを決めても意味はない。

HumanはBusiness Ruleを知っていた。AIはRepository上の実装事実を広く追えた。両者が別のRealityを持っていた。

Decisionは、「Approval Routeの主体はSubmission時に固定する。ただし代理可否はDecision時にもPolicyを再評価し、禁止条件に該当すれば代理Decisionを拒否する」とした。これにより、既存Routeの整合性を保ちつつ、最新Policyを反映できる。

Decisionを記録したあと、Workも切り直した。

仕様は書いたら終わる文書ではない。

**Realityが変われば、SpecもWorkも委譲条件も変わる。**

#### Scene 3 — Agentを増やしたのに、並列にならない

実装へ進む頃には、仕事はかなり整理されていた。

Frontendでは代理承認表示と操作導線。Backendでは代理権限判定。別のWorkではAudit Record。さらにBoundary Test、Notification、Compatibility Testがある。

AI Agentを複数走らせれば、一気に進みそうに見えた。

Teamは、Frontend、Authorization、Auditの三つを並列に委譲した。

最初の数十分は順調だった。それぞれのAgentがCodeを読み、Testを追加し、変更案を出した。

ところが、統合しようとすると衝突した。

Authorization Agentは、承認主体を表すStateに `actingUserId` を追加していた。Audit Agentは、同じ意味を別のAudit専用Objectに持たせようとしていた。Frontend AgentはAPI Responseへ `proxyApprover` を追加する前提でUIを作っていた。

三つのAgentは、それぞれのTask内では合理的だった。

でも、同じSource of Truth境界を別々に設計していた。

Agent数は三つだった。並列性は三倍ではなかった。

ここでTeamは、一度並列実行を止めた。原因はAgentの性能ではなく、Work Breakdownにあった。独立しているように見えた三つのTaskが、「Decision Actorをどう表現するか」という一つのModel Decisionに依存していた。

先に共通のDecisionを切り出す必要があった。

`Original Approver` と `Acting Approver` をApproval Decisionの共通Modelとして定義し、Audit、API、UIはそこから派生させる。MigrationとCompatibility Boundaryも、そのDecisionに含める。

その上でWork Graphを組み直した。

共通Modelの決定を先に完了し、各Agentへ渡すContextとAcceptanceを固定する。FrontendはPresentationとUser-visible Behavior。AuthorizationはDecision Policy。Auditはappend-orientedなEvidence記録。それぞれのWorkには、変更可能なFile/Module境界、必要Evidence、Rollback可能性を付けた。

二回目の並列実行は、最初よりAgent数を減らした。

それでも全体は速かった。

効いたのは、Agentを増やしたことより仕事の切り方だった。

**独立して終えられる仕事だけを並列にしたからだ。**

並列性は、同時に何体のAgentを起動したかでは決まらない。片方の判断をもう片方が暗黙に上書きしないこと。各Workが自分のAcceptanceを持つこと。失敗しても局所的に戻せること。そして結果を独立して検証できること。


---

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


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 18. 何を決め、何をまだ決めないか

**Creator / Lead Author: RIO AMADA**

この条件が揃って、ようやくParallel Executionが本当の速度になる。

#### Scene 4 — Testは全部通った。それでも足りなかった

数日後、代理承認の主要実装が揃った。

Unit TestはGreen。Integration TestもGreen。Cross-tenantのAuthorization Testも通った。代理期間の開始前・終了後も拒否される。Requesterによる自己承認も防げている。二重承認を送ってもOutcomeは一度しか適用されない。

技術的には、かなり安心できる状態に見えた。

そこでScenario Verificationを行った。

「Approver Aが休暇中。Proxy Approver Bが、Aの代わりに申請を承認する。後日Auditorが、そのDecisionを確認する。」

操作自体は成功した。

しかしAuditor向け画面を見ると、「Bが承認」としか表示されていなかった。

APIのAudit Responseにも実行者Bはある。しかし「Aの代理としてDecisionした」という関係が、Humanが追える形で十分に表現されていない。内部Logには元ApproverのIDが残っていたが、通常のAudit導線からは見えなかった。

TestはGreenだった。

なぜならTestは、「代理人が承認できる」「Audit Recordが作られる」という実装上のAcceptanceを確認していたからだ。

Business側が必要としていたのは、「後から第三者が、誰の権限でDecisionされたか説明できる」ことだった。

ここでCriteria自体の曖昧さも表に出た。

Engineerは「元Approver IDは保存しているので要件は満たしている」と考えた。Auditorは「通常画面から追えないなら監査可能とは言えない」と考えた。AI Evaluatorは、Specificationに「Original ApproverとActing ApproverをAuditできる」とあるため、どちらの解釈もあり得ると判定した。

この時点では、AIとHumanのどちらが正しいとも言えなかった。

Criteriaが足りなかった。

TeamはAcceptanceを更新した。

「Audit権限を持つUserが、通常のAudit画面とAPIから、Original Approver、Acting Approver、Delegation Rule、Decision時刻を一続きで確認できること。」

このCriteriaに対して、User-visible Verification Procedureを作り直した。

画面を開く。対象申請を選ぶ。代理Decisionを確認する。OriginalとActingの両Identityが表示される。APIでも同じRelationが取得できる。Audit Storeにも対応するEvidenceがある。

ここまで来ると、EvidenceはTest結果の一覧だけでは足りなくなる。

Evidenceは、次の人が判断するためのInterfaceになった。

Code Diffを最初から全部読まなくても、「このOutcomeは何によって証明されているか」「どこがまだUnknownか」「どのDecisionだけHumanへ戻っているか」が見える。

**Codeは重要なArtifactである。だが、判断の入口までCodeにしてしまう必要はない。**

必要なところでCodeへ降りればいい。

#### Scene 4.5 — 評価者を増やしても、真実にはならない

Acceptanceを更新したあと、TeamはEvaluationのやり方も見直した。

一つのAI Evaluatorだけに「この実装は要件を満たしているか」と聞けば、速い。だが、実装Agentと同じContext、同じ前提、似たModelで評価しているなら、同じ思い違いを共有する可能性がある。

そこで評価を分けた。

Policy RuleはdeterministicなCheckerで見る。User-visible BehaviorはScenario Runnerで見る。Audit Semanticsは別ContextのEvaluatorに確認させる。Security BoundaryはAuthorization Testで反証する。高Riskの意味判断だけ人へ戻す。

結果は、きれいには揃わなかった。

Rule CheckはPass。ScenarioもPass。しかしAudit Evaluatorは、「代理関係の表示は確認できるが、Delegation Ruleの有効期間を画面上で追えない」と指摘した。一方、Human Reviewerの一人は「そこまで通常画面に出す必要はない」と考えた。

ここで多数決を取れば、二対一、三対一という数字は作れる。

でも、その数字に意味があるとは限らない。

Rule CheckerとScenario Runnerは、そもそもAudit画面の説明可能性を評価していない。HumanとAI Evaluatorの不一致も、片方の能力不足ではなく「Auditorがどこまで一画面で追えるべきか」というCriteriaの不足かもしれない。

TeamはDisagreementをFailureとして消さず、分類した。

実装Errorなのか。Evaluator Errorなのか。Criteriaが曖昧なのか。Evidenceが足りないのか。Environmentが違うのか。それとも、まだ誰も気づいていないUnknownなのか。

今回の結論は `Ambiguous Criteria` だった。

Auditorへ確認し、「一画面にすべてを表示する必要はないが、通常導線からDelegation Ruleの有効期間へ二操作以内で到達できること」をAcceptanceへ追加した。

人数を増やしたこと自体が効いたわけではない。

**違うFailure Modeを持つ評価を組み合わせ、不一致を捨てずに次のQuestionへ変えたから、Criteriaが強くなった。**

Independent Evaluationで見たいのは、何体のAIが同じ答えを返したかではない。同じ間違いを一緒に見逃しにくいEvaluation Systemになっているかだ。

#### Scene 5 — AIに見せられないDataがある

Verificationを強くしようとすると、別の問題が出た。

Production相当の申請Dataを使えば、複雑なApproval Routeや代理設定を再現しやすい。しかしCoding Agentへ実Dataを自由に渡すことはできない。Tenantごとの組織情報や申請内容には、扱いを制限すべき情報が含まれている。

ここでPermissionを邪魔者と決めつけると、設計を誤る。

制約は消えない。

ならば、その制約の内側で仕事を完遂できるVerificationを作る。

Teamは、Production DataのCopyを諦め、必要な性質だけを持つSynthetic Fixtureを作った。複数Step、Budget Owner、代理期間、禁止Category、Cross-tenant Attempt、Notification Failure、二重Requestを再現できる小さなDatasetである。

AIにはFixture GeneratorとScenario Runnerを作らせた。実Dataそのものではなく、「どの性質が検証に必要か」をContextとして渡す。

この変更には副作用もあった。

Fixtureが現実を十分に代表しているのか、という新しい問いが生まれる。

そこで、Productionの値を持ち出さずに分布やSchema特性だけを確認できる統計・Metadata Checkを別に置き、Fixtureが主要なShapeを外していないことを定期確認する設計にした。

Permissionを緩めたのではない。

Verificationを、Permission Boundaryの内側で成立する形に作り直した。

**今すぐ任せられない仕事があっても、それだけで「AIには任せられない仕事」と決める必要はない。今のPermissionのままでは成立しないだけかもしれない。**

そこには大きな違いがある。

#### Scene 6 — 再現しないFailureは、Environmentの問題だった

Integration環境で、代理期間のBoundary Testがときどき失敗した。

Localでは再現しない。別のAgentが再実行すると通る。Test Codeを見ても、明らかな不具合はない。

最初、人間側ではRace Conditionが疑われた。AI Agentも最初の分析ではTime Handlingの可能性を高く見積もった。

しかしRunごとのEnvironment StateとEvidenceを並べると、別の共通点が見つかった。

失敗するRunだけ、Shared Integration環境に前のTestが残した代理設定が存在していた。Cleanupが完全ではなく、同じUserを使う別ScenarioへStateが漏れていた。


---

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


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 19. 合意をAIが実行できる契約へ変える

**Creator / Lead Author: RIO AMADA**

ここでは、Humanの最初の仮説よりMachine Evidenceが正しかった。

ここで競う意味はない。

Environment Version、Fixture ID、Seed、Test開始前State、Cleanup ResultがEvidenceとして残っていたから、Failureを比較できた。

TeamはPreflightとCleanup CheckをVerification Procedureへ追加した。Test開始前に期待Stateを確認し、終了時にはLeaseしたFixtureだけを確実に破棄する。共有環境で競合するWorkには一時的なLeaseを持たせ、失敗時はEnvironment FailureとProduct Failureを分けてRouteする。

「もう一回実行したら通った」で終わらせない。

再現しないFailureほど、Evidenceがいる。

そしてEnvironment Stateも、実装とは別の背景情報ではない。

**Outcomeを証明する条件の一部である。**

#### Scene 7 — Release前、人間のGateが戻る

技術的なEvidenceが揃い始め、Release Packetが作られた。

主要Scenario、Regression、Authorization、Audit、Compatibilityの結果。既知のRisk。Rollback手順。Production Verification。Agentが行った重要DecisionとDeviationもDecision Trailから要約されている。

それでも、一つだけ決まっていないことがあった。

Audit画面で、代理Decisionをどう表現するか。

候補は二つあった。

「BがAの代理として承認」

あるいは、

「Aの承認権限に基づきBが承認」

意味は近い。しかし法務・監査上、どちらの表現が適切かは単なるUI Copyではなかった。誰がDecision Ownerとして責任を持つのかというSemanticsに関わる。

AIは過去の文言、社内用語、一般的なAudit表現を比較し、候補と利点・欠点を出した。

しかし最終DecisionはHuman Gateへ戻した。

AIが文章を書けないからではない。

このWork Classでは、現時点のPolicyとAccountability上、最終的な意味決定をAIへ委譲する条件がまだ揃っていなかったからだ。

ここが大事である。

Human Gateは、AI Native化に失敗した証拠ではない。

逆に、何でも人間へ戻すのも違う。

**どのDecisionを、なぜHuman / Policy側に残しているのか説明できること。**

Release前のGateは「人が不安だから」ではなく、Decision Rights、Risk、Evidence、Accountabilityに基づいて置かれた。

そしてこのDecisionが将来Policy化され、十分にCalibrationできれば、同じ種類の判断がずっとHuman-onlyである保証もない。

境界は固定しない。

#### Scene 8 — Productionで旧Clientが壊れる

Releaseは承認された。

段階的にFeatureを有効化し、Production Verificationも開始した。新しいUIでは代理承認が動く。Auditも見える。主要APIも正常だった。

ところが、あるTenantから問い合わせが入った。

既存の連携Clientで、承認済み申請の一部が「未処理」のように表示される。

新Featureそのものではなく、Compatibilityの問題だった。

代理承認を表現するため、API Responseに新しいDecision Actor情報を追加した際、ある旧ClientがStatus判定で想定外の分岐へ入っていた。API Contract上は追加Fieldを無視できる設計のはずだったが、そのClientはResponse Shapeを独自に厳密比較していた。

Repository内のTestはすべてGreenだった。

新しいClientも正常だった。

それでも、Production Outcomeは壊れた。

TeamはFeature Flagで対象Tenantの代理承認を止め、旧Clientの影響範囲を確認した。全面Rollbackではなく、変更のReversibilityとBlast Radiusを見て限定停止を選んだ。

ここでRelease Evidenceが役に立った。

どのVersionが出ているか。どのTenantでFeatureが有効か。旧ClientがどのAPI Pathを使っているか。新Field追加と発生時刻が一致するか。代理Decision自体のData Integrityは保たれているか。

Incident対応は、闇雲なCode探索から始まらなかった。

Evidenceから、壊れているOutcomeを狭めていった。

Fixは、旧Client向けのCompatibility LayerとContract Testを追加する形になった。Production Verificationにも、代表的な既存ConsumerでResponseを確認するStepを足した。

Mergeした時点では、仕事は終わっていなかった。

Releaseした時点でも、まだ終わっていなかった。

**利用者の世界でOutcomeが成立し、失敗したときに戻せるところまでがDeliveryである。**

#### Scene 9 — Retroで「次から気をつける」を書かない

Incidentが収束した後、Retroを行った。

ありがちな結論なら、こうなる。

「既存Clientへの影響確認を徹底する。」

「Audit要件は早めに確認する。」

「Agent間で同じFileを触らないよう注意する。」

どれも間違いではない。

ただし、その文章を読まなかった次のAgent、次のTeam、半年後の新しいMemberには効かないかもしれない。

そこで一つずつ、「次のExecutionを変えるStructureへできないか」を見た。

高額申請で代理を禁止するRuleは、Business Scenario TestとPolicy Checkへ入れた。

Original ApproverとActing Approverの関係は、API・Audit Store・UIのContractとしてFixtureとVerification Procedureに組み込んだ。

Shared Integration環境のState漏れは、Preflight、Lease、Cleanup Checkへ変えた。

旧Client Compatibilityは、代表Consumerを使ったContract TestとRelease Gateへ入れた。

並列Conflictについては、「同じFileを触るな」という注意ではなく、Work Breakdown時にShared Model DecisionとIndependent Workを分けるChecklistへ入れた。

そして、Decision Trailからも一つ学びが残った。

途中で高額申請Ruleが追加されたとき、AIがImpact Analysisを行ったことで、UI、API、Audit、Testへの波及を早く見つけられた。そこでChange時の標準手順へ、「Decision変更時は影響するAcceptance / Evidence / Delegation Contractを再評価する」を追加した。

学びはDocumentにも残した。

でも、Documentだけにはしなかった。

**組織が学習したと言えるのは、次に同じ条件が来たとき、Executionが変わるときだ。**

#### Scene 10 — 次のTeamは、同じ失敗を最初から経験しない

数週間後、別Teamが別のWorkflowに「一時的な代理Decision」を追加することになった。

Domainは同じではない。扱う対象も違う。

だからFlowDeskのCodeをそのままCopyして終わり、という話ではない。

それでも、そのTeamはゼロから始めなかった。

Repositoryには、代理Decisionを考えるときのDomain Questionがあった。Decision Actorの表現Patternがあった。Delegation ContractのTemplateがあった。Synthetic Fixtureの作り方があった。Original / Acting Identityを検証するProcedureがあった。Environment Preflightがあった。Compatibility Gateがあった。

そして何より、「AIへどこまで任せてよいか」をModel名や個人の感覚だけで決めなくてよかった。

Work Class、Risk、Evidence Reliability、Failure Detectability、Reversibility、Permission、Accountabilityを見ながらOperating Profileを選べる。

最初のTeamが経験したFailureは消えていない。

過去に起きたこととして残っている。

ただし、同じFailureを次のTeamが同じ形で踏む必要はなくなった。

ここまで来て、ようやく個人のAI活用が組織能力へ変わり始める。

最初にあった依頼へ戻ろう。

> 「承認者が不在のとき、代理の人が承認できるようにしてほしい。」

AIなら、この一文からでもCodeを書き始められる。

それ自体は、もう珍しい能力ではない。

難しいのは、その一文を正しい仕事へ変えること。分からないものをUnknownとして残すこと。独立して任せられる単位へ分けること。必要な権限を渡し、越えてはいけない境界を決めること。成果をEvidenceで評価すること。人間へ戻すDecisionを理由付きで残すこと。Productionで失敗したときに戻れること。そして学びを次のExecutionへ埋め込むことだ。

最後に残るのは、Promptの巧さだけではない。意味を揃え、分からないものを残し、仕事を分け、権限を渡し、Evidenceで確かめ、失敗から次の実行を変える。

**AIが働くなら、そのAIが仕事を最後まで成立させられる条件も一緒に作る。**

そして、その設計を一度きりの工夫で終わらせず、次の人、次のAgent、次のTeamが再利用できる形へ戻していく。

FlowDeskのCaseが成功した理由を一つに絞るなら、AIが賢かったからではない。

失敗するたびに、仕事の仕組みの方を賢くしたからである。


---

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


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 20. AIに仕事を分解・再分解させる

**Creator / Lead Author: RIO AMADA**

# 11. 07_規模判定・Work Item分割ルール

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


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 21. 人間とAIのチームをどう設計するか

**Creator / Lead Author: RIO AMADA**

# 13. 09_チーム・役割運用ガイド

本章は「AI用の新しい役職名」を作る章ではない。
Scrum Master、Development Lead、Tech Lead、Engineering Lead、Sub Lead等の既存Roleに割り当て可能な**AI-Native Team Leadership Function**を定義する。

> **標準化するのはRole名ではなく、Teamを成立させる責務と意思決定である。**

---

## 13.1 AI-Native Team Leadership Function

Team Lead相当の人間が保持すべき中心責務：

```text
Outcome / Priorityを理解する
↓
AIとWork Structureを生成・評価する
↓
Human / AIへExecutionを割り当てる
↓
Context / Tool / Environment / Permissionを整える
↓
Evidenceから状態を観測する
↓
Decision / Blocker / Exceptionを処理する
↓
必要ならWorkを再分解する
↓
成果を評価・受入する
↓
Failure / Human InterventionをSystem Improvementへ戻す
```

Team Leadは、全Issueを自分で書き、全Agentへ逐次Promptし、全Diffを最初から読む人ではない。
**チームのFlow・Decision・Control Pointを設計する人**へ役割を移す。

---

DeepRailでは、PlanningとExecutionを別の責務として扱う。Planningは「何を成立させるか・どのApproachを採るか・何を完了とするか」を扱い、Executionは「どのArtifactを変更するか・どの操作を行うか・どのCheckを実行するか」を扱う。

ただしPlanningを永久にHuman-onlyへ固定しない。Work ClassとEvidenceが許す範囲でAIへ委譲できる。Team Leadershipの初期設計では、次の分離から始める。

```text
Human中心
├ Outcome
├ Priority
├ Risk Appetite
├ Acceptance
├ Decision Boundary
└ Exception

AIへ委譲しやすい
├ Exploration
├ Detailed Plan
├ Work Decomposition候補
├ Implementation
├ Tool Operation
├ Test
├ Status Aggregation
└ Documentation / Improvement Proposal
```

Autonomyが上がるほどAIはPlanning側へ広がるが、Objective変更・Risk受容・重要例外はDecision Rightsに従う。

---

## 13.3 Delegation Contract

複数Agentを使う場合、Orchestratorは問題を分析・戦略化し、Bounded Taskへ分解して並列委譲し、結果を統合する。Subagentへの委譲ではObjective、Expected Output、Allowed Tools / Sources、Task Boundary、Required Evidenceを明示する。

Human→AI、AI→AIの両方で、共通のWork Contractを使えるようにする。

```text
Purpose
Objective
Input / Context
Scope
Non-goal
Source of Truth
Allowed Tools
Permission
Expected Output
Acceptance Criteria
Required Evidence
Stop Condition
Escalation Condition
```

曖昧な「調べて」「実装して」ではなく、**何を成立させ、どこまで任せ、何を返すか**を契約する。

---

## 13.4 人間Role例

| Role | 責務 |
|---|---|
| Team Lead / Development Lead | Flow・Priority・Decision・Blocker・Risk・Team Operating Model |
| Product / Feature Owner | Outcome・要求・Acceptance責任 |
| Developer | Harnessを利用したExecution / Domain判断 |
| Reviewer / Evaluator | 設計・成果・Evidenceの評価 |
| Quality Owner | Gate・Test・Eval管理 |
| Environment / Platform Owner | Environment / CI/CD / Runtime状態管理 |
| Harness Maintainer | Agent/Skill/Rule/Harness管理 |
| Security Approver | 高リスク操作・Data / Production境界の承認 |

Role名は組織へ合わせて変更してよい。
小規模Teamでは一人が複数Functionを持ってよい。

---

## 13.5 AI Agentの責務設計

Agentを人間組織図の人格コピーとして増やさない。
Work Contract / Context Boundary / Tool Boundaryによって責務を分離する。

Agent Roleは工程名から作らず、次の**Viewpoint Contract**から導出する。

```text
What to observe      何を見るか / どの正本を参照するか
How to interpret     どう読むか / どの評価軸を持つか
What to output       何を返すか / Output Contract
Authority            何を実行してよいか
Cost / Model profile どのModel帯で成立するか
```

> **Roleを定義することと、Agentを1体置くことは別である。**

決定論的に処理できる責務はRule / Script / Tool / CIへ寄せる。独立したContext・視点・権限・成果物契約が必要な場合だけAgent化する。工程数だけAgentを増やさない。

代表例：

| Function | 責務 |
|---|---|
| Orchestrator / Lead | 計画・分解・割当・統合・再計画 |
| Research | 仕様・コード・影響範囲調査 |
| Architecture | 設計候補・Trade-off整理 |
| Implementation | 合意済みContractの実装 |
| Test / Evaluator | Test・Observed Behavior・Acceptance確認 |
| Independent Review | 別ContextからのReview |
| Documentation / Learning | Current Truth更新・改善候補抽出 |
| Release / Operations | Release準備・Production検証 |

---


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 22. AI時代のTeam Leadは何をするのか

**Creator / Lead Author: RIO AMADA**

## 13.1 AI-Native Team Leadership Function

Team Lead相当の人間が保持すべき中心責務：

```text
Outcome / Priorityを理解する
↓
AIとWork Structureを生成・評価する
↓
Human / AIへExecutionを割り当てる
↓
Context / Tool / Environment / Permissionを整える
↓
Evidenceから状態を観測する
↓
Decision / Blocker / Exceptionを処理する
↓
必要ならWorkを再分解する
↓
成果を評価・受入する
↓
Failure / Human InterventionをSystem Improvementへ戻す
```

Team Leadは、全Issueを自分で書き、全Agentへ逐次Promptし、全Diffを最初から読む人ではない。
**チームのFlow・Decision・Control Pointを設計する人**へ役割を移す。

---

DeepRailでは、PlanningとExecutionを別の責務として扱う。Planningは「何を成立させるか・どのApproachを採るか・何を完了とするか」を扱い、Executionは「どのArtifactを変更するか・どの操作を行うか・どのCheckを実行するか」を扱う。

ただしPlanningを永久にHuman-onlyへ固定しない。Work ClassとEvidenceが許す範囲でAIへ委譲できる。Team Leadershipの初期設計では、次の分離から始める。

```text
Human中心
├ Outcome
├ Priority
├ Risk Appetite
├ Acceptance
├ Decision Boundary
└ Exception

AIへ委譲しやすい
├ Exploration
├ Detailed Plan
├ Work Decomposition候補
├ Implementation
├ Tool Operation
├ Test
├ Status Aggregation
└ Documentation / Improvement Proposal
```

Autonomyが上がるほどAIはPlanning側へ広がるが、Objective変更・Risk受容・重要例外はDecision Rightsに従う。

---

## 13.3 Delegation Contract

複数Agentを使う場合、Orchestratorは問題を分析・戦略化し、Bounded Taskへ分解して並列委譲し、結果を統合する。Subagentへの委譲ではObjective、Expected Output、Allowed Tools / Sources、Task Boundary、Required Evidenceを明示する。

Human→AI、AI→AIの両方で、共通のWork Contractを使えるようにする。

```text
Purpose
Objective
Input / Context
Scope
Non-goal
Source of Truth
Allowed Tools
Permission
Expected Output
Acceptance Criteria
Required Evidence
Stop Condition
Escalation Condition
```

曖昧な「調べて」「実装して」ではなく、**何を成立させ、どこまで任せ、何を返すか**を契約する。

---

## 13.4 人間Role例

| Role | 責務 |
|---|---|
| Team Lead / Development Lead | Flow・Priority・Decision・Blocker・Risk・Team Operating Model |
| Product / Feature Owner | Outcome・要求・Acceptance責任 |
| Developer | Harnessを利用したExecution / Domain判断 |
| Reviewer / Evaluator | 設計・成果・Evidenceの評価 |
| Quality Owner | Gate・Test・Eval管理 |
| Environment / Platform Owner | Environment / CI/CD / Runtime状態管理 |
| Harness Maintainer | Agent/Skill/Rule/Harness管理 |
| Security Approver | 高リスク操作・Data / Production境界の承認 |

Role名は組織へ合わせて変更してよい。
小規模Teamでは一人が複数Functionを持ってよい。

---

## 13.5 AI Agentの責務設計

Agentを人間組織図の人格コピーとして増やさない。
Work Contract / Context Boundary / Tool Boundaryによって責務を分離する。

Agent Roleは工程名から作らず、次の**Viewpoint Contract**から導出する。

```text
What to observe      何を見るか / どの正本を参照するか
How to interpret     どう読むか / どの評価軸を持つか
What to output       何を返すか / Output Contract
Authority            何を実行してよいか
Cost / Model profile どのModel帯で成立するか
```

> **Roleを定義することと、Agentを1体置くことは別である。**

決定論的に処理できる責務はRule / Script / Tool / CIへ寄せる。独立したContext・視点・権限・成果物契約が必要な場合だけAgent化する。工程数だけAgentを増やさない。

代表例：

| Function | 責務 |
|---|---|
| Orchestrator / Lead | 計画・分解・割当・統合・再計画 |
| Research | 仕様・コード・影響範囲調査 |
| Architecture | 設計候補・Trade-off整理 |
| Implementation | 合意済みContractの実装 |
| Test / Evaluator | Test・Observed Behavior・Acceptance確認 |
| Independent Review | 別ContextからのReview |
| Documentation / Learning | Current Truth更新・改善候補抽出 |
| Release / Operations | Release準備・Production検証 |

---

## 13.6 Team Capacity — Agent数をThroughputとみなさない

Teamの実効能力は少なくとも次で見る。

```text
Execution Capacity
Review Capacity
Approval Capacity
Environment Capacity
Decision Capacity
Product / Domain Capacity
```

AI Agentを増やしてExecution Capacityだけを上げると、Review Queue、Approval Queue、Environment競合、Decision待ちへBottleneckが移る。

承認が詰まると、遅れるだけでは済まない。件数が人のAttentionを上回ると、Gateは制度上残ったまま、実質的な確認だけが抜けていく。これが **Approval Hollowing / Rubber-stamp Risk** である。

Team Capacityには、週あたりにReviewできる量、Decisionできる量、Approvalできる量まで出す。AI ExecutionのWIP上限も、その帯域から切り離さない。

WIP Limitは人間数だけでなく、
- Human Review可能量
- CI / Test Environment枠
- Shared Environment
- Risk Class
- Dependency
- Decision待ち

を考慮して設定する。

---

## 13.7 Team会議を「Status読み上げ」からDecision Systemへ変える

AIが収集可能なStatusを、人間の同期会議で一人ずつ読み上げない。
会議は**認識合わせ・Decision・Exception・Learning**へ集中させる。

標準Meeting Functionは次の9つとする。
すべてを必ず別会議として開催する必要はない。規模・Method・Riskに応じて統合する。

### Meeting 1: Outcome / Intake Sync

**目的:** 何を成立させる仕事なのかを揃える。  
**開催:** Epic / Initiative開始時、重大要求変更時。  
**主参加:** Product/Customer責任者、Team Lead、必要なDomain Expert、AI。  

決めること：
- Objective / Expected Outcome
- Scope / Non-goal
- Priority / Deadline
- Initial Risk / Constraint
- Success Metric
- Decision Owner

AIの事前準備：
- Existing Context summary
- Unknown / Open Question
- Conflict / Assumption

**Output:** Outcome Contract / Intake Decision。

### Meeting 2: Discovery / Alignment Session

**目的:** 「同じ言葉を使っているが違うものを想像している」を防ぐ。  
**開催:** 上流、重要変更、顧客認識差がある時。  

AIが準備し得るもの：
- Mock / Wireframe / Prototype
- User / Business Flow
- API / Data Example
- Before / After
- Plan / Price / Scope comparison
- Architecture / Migration scenario

決めること：
- Domain Interpretation
- User Behavior
- Boundary
- Acceptance Image
- High-cost Decision
- Open Question

**Output:** Shared Reality / Alignment Record。

### Meeting 3: AI Refinement / Work Design

**目的:** Work Structureが安全に実行可能か評価する。  
**開催:** Epic / Feature開始前、再分解Trigger時。  

AIが生成：
- Epic / Feature / Issue / Agent Task候補
- Dependency Graph
- Risk / Context / Parallelism分析

人間が主に確認：
- Outcome独立性
- Acceptance分離
- Risk
- Dependency
- Human Gate
- Source of Truth
- Parallel Conflict

**Output:** Execution-ready Work Graph。

### Meeting 4: Execution Planning

**目的:** 「誰に振るか」より「どう安全に実行させるか」を決める。  

決めること：
- Human / AI assignment
- Agent / Runtime
- Required Context
- Allowed Tool
- Environment
- Permission Boundary
- Required Evidence
- Human Gate
- Stop / Escalation Condition

**Output:** Work Contract / Execution Plan。

### Meeting 5: Decision & Blocker Sync

従来Dailyの代替・拡張。

AIが会議前に集約：

```text
Completed
In Progress
Blocked
Failed
Waiting Approval
Risk Changed
Acceptance Changed
Environment Failure
Unknown
Decision Required
```

会議で扱うこと：
- Decision Required
- Blocker解除Owner
- Re-decomposition要否
- Priority変更
- Agent停止 / 再開
- Permission変更
- Environment Owner escalation

Statusだけなら同期会議へ持ち込まない。

**Output:** Decision / Escalation / Updated Work Graph。

### Meeting 6: Technical / Architecture Decision Sync

**目的:** AIが越えてはいけない設計境界を人間が判断する。  
**開催:** Event-driven。毎日開催しない。  

AIはDecision Packetを事前生成する。

```text
Decision Required
Context
Option A / B / ...
Trade-off
Recommendation
Evidence
Risk
Unknown
Reversibility
```

**Output:** ADR / Decision Record / updated Contract。

### Meeting 7: Review / Acceptance

**目的:** Raw Artifactの読破ではなく、Outcome / Evidenceから成果を判断する。  

見る順番：

```text
Decision / Acceptance
↓
Summary
↓
Evidence
↓
High-risk Change
↓
Raw Artifact (必要時だけ)
```

確認：
- Intent
- Acceptance Criteria
- Observed Result
- Test / Eval
- Risk / Deviation
- Unknown / Untested

**Output:** Accept / Reject / Request Change / Escalate。

### Meeting 8: Release Readiness

**目的:** 「開発完了」と「本番へ出せる」を分けて判断する。  

確認：
- Acceptance complete
- CI status
- Security / Compliance checks
- Migration
- Residual Risk
- Rollback
- Monitoring
- Human Approval
- Living Document / Runbook readiness

**Output:** Release Decision Packet / Go-NoGo。

### Meeting 9: Learning / Harness Retro

従来の「人間の反省会」で終わらせない。

中心質問：

> **今回、人間が介入した箇所・AIが迷った箇所を、次回は仕組みで減らせるか。**

| 発見 | 主な還元先 |
|---|---|
| 要求が毎回曖昧 | Intake / Requirement Template |
| Agentが同じ誤り | Rule |
| 同じ手順を毎回説明 | Skill |
| Test漏れ | Eval / Gate |
| Tool不足 | Tool / MCP |
| Environment事故 | Environment Gate / Provenance |
| 同じ承認を反復 | Delegation Policy |
| 巨大Diff Review | Review Packet改善 |
| Work分割不良 | Decomposition Rubric |
| 組織判断待ち | Decision Rights / Operating Model |

**Output:** Harness Backlog / Standard Backlog / Training Backlog。

---

## 13.8 MeetingはMethodに合わせて束ねる

### Scrum例

```text
Sprint Planning
= Outcome / Work Design / Execution Planning

Daily
= Decision & Blocker Sync

Refinement
= Discovery / Alignment + AI Refinement

Sprint Review
= Review / Acceptance

Retro
= Learning / Harness Retro
```

ScrumのEvent名を変えること自体はDeepRailの要求ではない。
**Eventの中で何をDecisionし、AIが何を準備し、何をEvidenceとして残すか**を変える。

### Waterfall / Enterprise例

```text
要求調整会
→ Discovery / Alignment

設計審査
→ Decision Packet / Architecture Decision

進捗会議
→ Decision & Blocker Sync

試験判定
→ Evidence / Acceptance

リリース判定
→ Release Readiness

振り返り / 改善会
→ Harness / Standard Learning
```

---

## 13.9 Team Leadの標準Dashboard

Team Leadが日常的に見るべき情報をStatus一覧ではなく、意思決定待ち中心にする。

```text
Outcome Health
Decision Required
Blocker
Risk Change
Approval Queue
Review Queue
Environment Health
WIP / Dependency
Acceptance Progress
Human Intervention Hotspot
Harness / Standard Improvement Candidate
```

**人のAttentionには上限がある。そこを無限の前提にしない。**


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 23. AI Native Teamの会議と意思決定

**Creator / Lead Author: RIO AMADA**

## 13.7 Team会議を「Status読み上げ」からDecision Systemへ変える

AIが収集可能なStatusを、人間の同期会議で一人ずつ読み上げない。
会議は**認識合わせ・Decision・Exception・Learning**へ集中させる。

標準Meeting Functionは次の9つとする。
すべてを必ず別会議として開催する必要はない。規模・Method・Riskに応じて統合する。

### Meeting 1: Outcome / Intake Sync

**目的:** 何を成立させる仕事なのかを揃える。  
**開催:** Epic / Initiative開始時、重大要求変更時。  
**主参加:** Product/Customer責任者、Team Lead、必要なDomain Expert、AI。  

決めること：
- Objective / Expected Outcome
- Scope / Non-goal
- Priority / Deadline
- Initial Risk / Constraint
- Success Metric
- Decision Owner

AIの事前準備：
- Existing Context summary
- Unknown / Open Question
- Conflict / Assumption

**Output:** Outcome Contract / Intake Decision。

### Meeting 2: Discovery / Alignment Session

**目的:** 「同じ言葉を使っているが違うものを想像している」を防ぐ。  
**開催:** 上流、重要変更、顧客認識差がある時。  

AIが準備し得るもの：
- Mock / Wireframe / Prototype
- User / Business Flow
- API / Data Example
- Before / After
- Plan / Price / Scope comparison
- Architecture / Migration scenario

決めること：
- Domain Interpretation
- User Behavior
- Boundary
- Acceptance Image
- High-cost Decision
- Open Question

**Output:** Shared Reality / Alignment Record。

### Meeting 3: AI Refinement / Work Design

**目的:** Work Structureが安全に実行可能か評価する。  
**開催:** Epic / Feature開始前、再分解Trigger時。  

AIが生成：
- Epic / Feature / Issue / Agent Task候補
- Dependency Graph
- Risk / Context / Parallelism分析

人間が主に確認：
- Outcome独立性
- Acceptance分離
- Risk
- Dependency
- Human Gate
- Source of Truth
- Parallel Conflict

**Output:** Execution-ready Work Graph。

### Meeting 4: Execution Planning

**目的:** 「誰に振るか」より「どう安全に実行させるか」を決める。  

決めること：
- Human / AI assignment
- Agent / Runtime
- Required Context
- Allowed Tool
- Environment
- Permission Boundary
- Required Evidence
- Human Gate
- Stop / Escalation Condition

**Output:** Work Contract / Execution Plan。

### Meeting 5: Decision & Blocker Sync

従来Dailyの代替・拡張。

AIが会議前に集約：

```text
Completed
In Progress
Blocked
Failed
Waiting Approval
Risk Changed
Acceptance Changed
Environment Failure
Unknown
Decision Required
```

会議で扱うこと：
- Decision Required
- Blocker解除Owner
- Re-decomposition要否
- Priority変更
- Agent停止 / 再開
- Permission変更
- Environment Owner escalation

Statusだけなら同期会議へ持ち込まない。

**Output:** Decision / Escalation / Updated Work Graph。

### Meeting 6: Technical / Architecture Decision Sync

**目的:** AIが越えてはいけない設計境界を人間が判断する。  
**開催:** Event-driven。毎日開催しない。  

AIはDecision Packetを事前生成する。

```text
Decision Required
Context
Option A / B / ...
Trade-off
Recommendation
Evidence
Risk
Unknown
Reversibility
```

**Output:** ADR / Decision Record / updated Contract。

### Meeting 7: Review / Acceptance

**目的:** Raw Artifactの読破ではなく、Outcome / Evidenceから成果を判断する。  

見る順番：

```text
Decision / Acceptance
↓
Summary
↓
Evidence
↓
High-risk Change
↓
Raw Artifact (必要時だけ)
```

確認：
- Intent
- Acceptance Criteria
- Observed Result
- Test / Eval
- Risk / Deviation
- Unknown / Untested

**Output:** Accept / Reject / Request Change / Escalate。

### Meeting 8: Release Readiness

**目的:** 「開発完了」と「本番へ出せる」を分けて判断する。  

確認：
- Acceptance complete
- CI status
- Security / Compliance checks
- Migration
- Residual Risk
- Rollback
- Monitoring
- Human Approval
- Living Document / Runbook readiness

**Output:** Release Decision Packet / Go-NoGo。

### Meeting 9: Learning / Harness Retro

従来の「人間の反省会」で終わらせない。

中心質問：

> **今回、人間が介入した箇所・AIが迷った箇所を、次回は仕組みで減らせるか。**

| 発見 | 主な還元先 |
|---|---|
| 要求が毎回曖昧 | Intake / Requirement Template |
| Agentが同じ誤り | Rule |
| 同じ手順を毎回説明 | Skill |
| Test漏れ | Eval / Gate |
| Tool不足 | Tool / MCP |
| Environment事故 | Environment Gate / Provenance |
| 同じ承認を反復 | Delegation Policy |
| 巨大Diff Review | Review Packet改善 |
| Work分割不良 | Decomposition Rubric |
| 組織判断待ち | Decision Rights / Operating Model |

**Output:** Harness Backlog / Standard Backlog / Training Backlog。

---

## 13.8 MeetingはMethodに合わせて束ねる

### Scrum例

```text
Sprint Planning
= Outcome / Work Design / Execution Planning

Daily
= Decision & Blocker Sync

Refinement
= Discovery / Alignment + AI Refinement

Sprint Review
= Review / Acceptance

Retro
= Learning / Harness Retro
```

ScrumのEvent名を変えること自体はDeepRailの要求ではない。
**Eventの中で何をDecisionし、AIが何を準備し、何をEvidenceとして残すか**を変える。

### Waterfall / Enterprise例

```text
要求調整会
→ Discovery / Alignment

設計審査
→ Decision Packet / Architecture Decision

進捗会議
→ Decision & Blocker Sync

試験判定
→ Evidence / Acceptance

リリース判定
→ Release Readiness

振り返り / 改善会
→ Harness / Standard Learning
```

---

## 13.9 Team Leadの標準Dashboard

Team Leadが日常的に見るべき情報をStatus一覧ではなく、意思決定待ち中心にする。

```text
Outcome Health
Decision Required
Blocker
Risk Change
Approval Queue
Review Queue
Environment Health
WIP / Dependency
Acceptance Progress
Human Intervention Hotspot
Harness / Standard Improvement Candidate
```

**人のAttentionには上限がある。そこを無限の前提にしない。**


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 24. Agent数ではなくFlowを管理する

**Creator / Lead Author: RIO AMADA**

## 13.6 Team Capacity — Agent数をThroughputとみなさない

Teamの実効能力は少なくとも次で見る。

```text
Execution Capacity
Review Capacity
Approval Capacity
Environment Capacity
Decision Capacity
Product / Domain Capacity
```

AI Agentを増やしてExecution Capacityだけを上げると、Review Queue、Approval Queue、Environment競合、Decision待ちへBottleneckが移る。

承認が詰まると、遅れるだけでは済まない。件数が人のAttentionを上回ると、Gateは制度上残ったまま、実質的な確認だけが抜けていく。これが **Approval Hollowing / Rubber-stamp Risk** である。

Team Capacityには、週あたりにReviewできる量、Decisionできる量、Approvalできる量まで出す。AI ExecutionのWIP上限も、その帯域から切り離さない。

WIP Limitは人間数だけでなく、
- Human Review可能量
- CI / Test Environment枠
- Shared Environment
- Risk Class
- Dependency
- Decision待ち

を考慮して設定する。

---


---

# 42. AI導入による開発ボトルネックの移動

AI AgentによってBuild工程が高速化しても、開発プロセス全体が同じ倍率で高速化するとは限らない。

制約は工程間を移動する。

---

## 42.1 Before / Afterの考え方

```text
Before Agents
────────────────────────────────────────────
Plan | Design | █████████ Build █████████ | Test | Deploy | Maintain

各工程が人間速度で進み、
特にBuildが大きな時間を占める。
```

```text
After Agents
────────────────────────────────────────────
Plan | Design | Build | Review | Test | Deploy | Maintain
               ↑短縮

新たな制約候補
Requirements / Design / Review / Test / Release / Maintain
```

AI導入後は「実装できる量」が急増する。

一方で、人間レビュー、要求判断、試験環境、Release承認などが従来速度のままであれば、下流にWork Itemが滞留する。

---

## 42.2 Build高速化だけでは全体Lead Timeは十分に縮まらない

例：

```text
Before
要求整理       3日
設計           2日
Build          3日
Review         2日
Test           2日
Release        1日
-----------------
合計          13日
```

BuildをAIで3時間まで短縮しても、

```text
After
要求整理       3日
設計           2日
Build          3時間
Review         2日
Test           2日
Release        1日
-----------------
全体は依然として複数日
```

となる。

AI駆動開発では工程単体の速度ではなく、**End-to-EndのFlow**を見る。

---

## 42.3 WIPの移動

Build能力だけを増やすと、ReviewやTestへWIPが集中する。

```text
Agent A ─ Issue A 完了 ┐
Agent B ─ Issue B 完了 ├→ Review Queue
Agent C ─ Issue C 完了 ┤
Agent D ─ Issue D 完了 ┤
Agent E ─ Issue E 完了 ┘
```

この状態でAgent数だけ増やしても、全体Throughputは改善しない場合がある。

必要なのは、

- Review Agent
- Test Automation
- CI高速化
- PR/MR標準化
- Risk-based Review
- 自動Gate
- Reviewer負荷の平準化

など、現在の制約工程への改善である。

---

## 42.4 Harnessは現在のBottleneckに合わせて成長させる

Harnessを完成品として固定しない。

```text
Harness v1
Build支援中心
        ↓
Build高速化
        ↓
Reviewが制約
        ↓
Harness v2
Review Agent / Test Gate
        ↓
Review高速化
        ↓
Requirementsが制約
        ↓
Harness v3
Issue生成 / Requirement Skill / Impact Analysis
        ↓
Releaseが制約
        ↓
Harness v4
CI/CD / Release Gate / Release Agent
```

この循環をHarness改善の基本形とする。

---

## 42.5 Bottleneck候補

観測対象の例：

### Upstream

- 要求整理
- Product Decision
- Issue準備
- Acceptance Criteria作成
- Design Decision
- Architecture Review

### Development

- Context探索
- Agent Retry
- Build
- Local Test
- Repository Conflict

### Validation

- Human Review
- Security Review
- Test環境
- Integration Test
- E2E
- CI待ち

### Delivery

- Release Approval
- Migration
- Deployment Window
- External Team
- Change Management

### Maintenance

- Monitoring
- Incident Triage
- Root Cause Analysis
- Living Document更新
- Harness更新

---

## 42.6 次に自動化する工程をBottleneckから決める

自動化対象を「AIでできそうだから」で選ばない。

```text
Measure
↓
Bottleneck
↓
Cause
↓
改善手段
├ Process変更
├ Harness変更
├ Skill追加
├ Agent追加
├ Tool連携
├ Human Role変更
└ Quality Gate変更
↓
Eval
↓
Measure Again
```

---

## 42.7 大ループ・中ループ・小ループとの接続

### 大ループ

SDLC全体の制約を見る。

```text
Requirement
→ Design
→ Build
→ Review
→ Test
→ Release
→ Maintain
→ Reinvest / Learn
```

### 中ループ

Issue単位の滞留を見る。

```text
Issue Ready
→ Agent Start
→ Implementation
→ PR
→ Review
→ Merge
→ Done
```

### 小ループ

Agent内部の非効率を見る。

```text
Read
→ Edit
→ Build
→ Test
→ Retry
```

3層を同時に見ることで、「モデルが遅い」のか「Processが遅い」のかを分離する。

---

## 42.8 Harness Evalsとの接続

Harness Evalでは、Task成功率だけでなくFlowへの影響を確認する。

例：

```text
Harness v1
Task Success: 95%
Build: 10分
Review Queue: 4時間

Harness v2
Task Success: 96%
Build: 12分
Review Queue: 40分
```

Buildが若干遅くても、全体Lead Timeが短ければv2が優れる可能性がある。

評価は局所速度ではなくEnd-to-Endで行う。

---

## 42.9 AI自律化との接続

Human Gateを外す判断にもBottleneck情報を使う。

例：

```text
Reviewが最大Bottleneck
↓
低Risk変更でAI Review + CI結果が安定
↓
Human Review対象をRisk-basedに限定
↓
Review Queueを削減
```

一方で、要求判断がBottleneckだからという理由だけで、曖昧な要求判断を無条件にAIへ移譲してはならない。

**自律化は、Bottleneck × Risk × Eval結果で判断する。**

---

## 42.10 週次で確認するFlow Board

推奨項目：

| 工程 | Cycle Time | Queue Time | WIP | Human Time | 主なFailure |
|---|---:|---:|---:|---:|---|
| Requirement | 測定 | 測定 | 測定 | 測定 | 曖昧性 |
| Design | 測定 | 測定 | 測定 | 測定 | 判断待ち |
| Build | 測定 | 測定 | 測定 | 測定 | Agent Retry |
| Review | 測定 | 測定 | 測定 | 測定 | Review待ち |
| Test | 測定 | 測定 | 測定 | 測定 | 環境待ち |
| Release | 測定 | 測定 | 測定 | 測定 | Approval待ち |
| Maintain | 測定 | 測定 | 測定 | 測定 | Triage |

「Buildがどれだけ速くなったか」だけではなく、**どのQueueが次の制約になったか**をチームで確認する。

---

## 42.11 Review Bottleneckへの対策はReview Agent追加だけではない

Reviewが詰まったとき、最初の対応としてReviewerやReview Agentを増やすだけでは不十分な場合がある。

原因が上流の未合意Decisionなら、

```text
Review強化
```

ではなく、

```text
事前認識合わせ
↓
Spec明確化
↓
Work Item粒度調整
↓
Test Seam合意
↓
Review Packet
```

へ改善する。

Reviewで初めて発見される問題を分類する。

| Review指摘 | 改善先 |
|---|---|
| 要求の認識違い | Grill / Spec |
| 用語のズレ | Domain Document |
| Architecture逸脱 | Rule / ADR / Design Gate |
| Scope Creep | Issue / Spec Review |
| Style | Lint / Standards Agent |
| Test不足 | Test Policy / CI |
| Security | Security Gate |
| 同じ指摘の再発 | Skill / Rule / Eval |

レビュー工程で発見した問題をレビュー工程だけに閉じ込めない。

---

## 42.12 本標準における判断

AI駆動開発の改善対象は、Coding工程だけではない。

> **AIにより高速化した工程の前後で、新たに発生した制約を観測し、現在のBottleneckへHarnessを拡張する。**

これをHarness Lifecycleの基本原則とする。

---


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 25. AIにどこまで任せるか

**Creator / Lead Author: RIO AMADA**

# 5. 01_AI駆動開発 基本方針

## 5.1 HumanとAIの責務境界を固定しない

DeepRailでは、AIを実際に仕事を進める主体まで含めて設計する。
ただし、`AI = Execution / Human = Decision` を永続的な境界として固定しない。

### 現時点での基本Profile

多くの案件では、導入初期は次の分業が安全である。

```text
Human
├ Objective / Outcome
├ Business Priority
├ Risk Appetite
├ High-cost / Irreversible Decision
├ Exception Judgment
└ Accountability

AI
├ Research
├ Planning Draft
├ Work Breakdown Draft
├ Implementation
├ Test / Verification
├ Documentation
├ Review Assistance
└ Repetitive Coordination
```

これは**開始Profile**であり、Human-only領域の永久リストではない。

### Dynamic Responsibility Boundary

AI Capability、Risk、Evidence Reliability、Failure Detectability、Reversibility、Permission、組織上のAccountabilityが変化すれば、責務の配置も変更してよい。

```text
従来Human中心
Planning
Work Decomposition
Review
Evaluation
Coordination
Priority Proposal
Resource Allocation Proposal
Strategy Option Design

        ↓ Capability / Evidence / Controlが成熟

AIへ段階的にDelegation可能
```

DeepRailが守るのはHumanの領域ではなく、**責務移動の安全条件**である。

### Delegation判断

```text
Delegability = f(
  Capability,
  Risk,
  Evidence Reliability,
  Failure Detectability,
  Reversibility,
  Permission Boundary,
  Accountability
)
```

AIができるから任せるのではない。
**失敗を観測でき、止められ、戻せ、Evidenceから評価できるから任せる。**

### 現在のOperating Profileは到達点ではない

導入初期にHuman Gateを厚く持つことと、Humanが永久にそのGateを担当することは同じではない。

現在の分業は、今のAI Capability、Evidence Reliability、Failure Detectability、Reversibility、Permission、Risk、Accountabilityに合わせた開始Profileである。

たとえば、最初はAIが実行し、人間が評価・承認する。評価系が十分にCalibrationされれば、AIが一次評価を担い、人間はDecisionとEvidenceへ集中できる。さらに限定されたWork ClassでFalse AcceptやEscaped Defectを継続的に観測でき、RollbackやAuditも成立するなら、通常のGO判断をAIへ委譲し、人間はSampling / Exceptionへ移れる。

その先でPolicyとRisk Appetiteまで安定すれば、定義済みの範囲ではAIが評価・GO・Retryまで行える。

```text
Human-led
↓
AI-assisted
↓
Delegated Execution
↓
Delegated Evaluation
↓
Audited Autonomy
↓
Policy-Governed Autonomy
```

これは一方向の成熟度競争ではない。Work ClassごとにEvidenceを見て進め、条件が崩れれば戻す。

**DeepRailが固定するのは現在のHuman / AI分業ではなく、責務を移してよい条件である。**

### AIが「人間の領域」へ入るということ

AIは人間の仕事を一つずつ置換するだけではない。
これまで「ここから先は人間」と考えられていた境界自体を継続的に書き換える。

その結果、AI導入は次へ波及する。

```text
Task Automation
↓
Team Design
↓
Management
↓
Role / Headcount / Decision Rights
↓
Organization Structure
↓
Business Strategy / Competitive Advantage
```

AIがPlanning、Evaluation、Coordination、Priorityへ入るほど、話はTool選定の外へ広がる。最後には、人の配置や権限、組織構造、経営戦略まで設計対象になる。


---

# 23. 19_AI権限委譲・自律化運用ガイド

この章が、AI駆動チーム開発の長期的な到達点を定める。

---

## 23.1 自律化レベル

| Level | 人間の主な関与 | AIの範囲 |
|---|---|---|
| A0 | 常時監視・分割案確認 | 提案・調査・Work分割案 |
| A1 | 各STEP・Issue構造承認 | 調査・設計案・実装・Test |
| A2 | Issue開始/終了 | Issue内Lifecycle + Task / Agent Task自律分割 |
| A3 | Feature開始/終了 | Feature→Issue分割・再分割・並列Agent・PR |
| A4 | Epic Outcome / Risk / Exception | Epic→Feature / Issue分割・Feature群実行・正本更新 |
| A5 | Strategy / Portfolio / Investment | Initiative→Epic候補・定型領域の継続実行・改善 |

Work Decompositionの自律化はDR-M07のRubricに従う。

AIが分割できることと、AIがObjectiveやBusiness Decisionを自由に変更してよいことは同義ではない。

```text
AI can decompose the work
≠
AI can redefine the goal
```

Autonomyを上げるほど、人間のReview対象は下位Taskから上位Outcome / Risk / Decisionへ移す。

---

## 23.2 Human Gateの減らし方

Human Gateは「ある / ない」の二値ではない。
自律化Level A0〜A5と、各Gateの**承認強度 S1〜S5**は分けて管理する。

| 強度 | 形態 | 定義 |
|---|---|---|
| S5 | 対面同期承認 | 人間が成果物を確認し、その場で承認 |
| S4 | 台帳非同期承認 | 人間が非同期で確認し、承認台帳へ記録 |
| S3 | 非同期リレー承認 | 人間が判断し、AIが正本台帳へ転記。判断記録と転記を照合可能にする |
| S2 | 完了判定委任 | 事前に定義した基準に基づき、指名された人間へ判定を委任 |
| S1 | AI代行承認 | 明示的な委任規程に基づきAIが承認を記録 |

S1/S2を使う場合、委任規程に最低限次を持つ。

```yaml
delegation:
  scope:      # 対象工程・Gate・Work Item
  expiry:     # 期限または失効条件
  audit:      # 誰がどの頻度で事後確認するか
  disclosure: # 代行・委任実績を誰へいつ開示するか
```

承認は対象操作を明示した確認にだけ効力を持つ。
古い成果物への承認を、新しい版へ流用しない。

Gate削減は感覚で行わない。

Human Gateを減らす前に、DR-M17のEvaluation Authority `EA0〜EA4`で対象Work Classの評価権限をCalibrationする。

```text
Work Classを限定
↓
EA1 Shadow Evaluation
Human / AIの判定差を測定
↓
Evaluation Criteria / Evidenceを改善
↓
EA2 AI-First + Human Decision
↓
一定期間、False Accept / Escaped Defect / Overrideを測定
↓
EA3 Audited Autonomy
HumanはSampling / Exceptionへ
↓
Policy・Risk Appetiteまで安定
↓
EA4 Policy-Governed Autonomyを検討
```

Human Gateの削減目的は「人間をゼロにすること」ではない。
**人間のAttentionを、曖昧性・重大Risk・不可逆Decision・法的/組織的Accountabilityへ集中させること**である。

また、Autonomy / Evaluation Authority / Approval Strengthを混同しない。

```text
Execution Autonomy A0〜A5
×
Evaluation Authority EA0〜EA4
×
Approval Strength S1〜S5
```

同じA3でも、評価実績が少ないTeamはEA1、十分なCalibration Evidenceを持つTeamはEA3というProfileが成立する。

### 23.2.0 Gateを評価する主体は段階的に移せる

Human Gateを減らすとき、StepやControl Pointまで一緒に消す必要はない。

変えるのは、誰がEvidenceを集め、誰が評価し、誰がGOを成立させるかである。

```text
Initial
AI Generate / Execute
↓
Human Review
↓
Human Approve

        ↓ Calibration

AI-First
Generation Agent
↓
Review Agent / Automated Eval
↓
Human Decision

        ↓ Bounded Delegation

Audited Autonomy
Agent Execution
↓
Independent Evaluation
↓
通常CaseはAIがGO
└─ Exception / Sampling → Human

        ↓ Policy Stabilization

Policy-Governed Autonomy
Multi-Agent / Agent Execution
↓
Automated Evaluation
↓
Policy Gate
├─ PASS → 自動で次工程へ
├─ RETRY → 定義済み範囲で再実行
└─ EXCEPTION → Human Intervention
```

この移行で、人間の関与は単純に「減る」のではない。
Artifactの逐次確認から、Evaluation Function、Risk Appetite、Policy、重大例外、監査へ比重が移る。

**Human Gateを消しているのではない。Gateを成立させるEvidenceと、判断する主体を変えている。**

### 23.2.1 Why — なぜ「全部確認しない」方が安全になり得るのか

「AIが作ったものは、人間が全部確認する。」

最初は、このルールが一番安全に見える。未知のToolを導入したばかりなら、実際それでいい。何を間違えるか分からない時期にHuman Gateを厚くするのは自然である。

問題は、そのルールを成熟後も変えないことだ。

FlowDeskで、AIが一日に二つの小変更しか作らないなら、人が全部読める。十、二十、五十と増えたらどうなるか。Reviewerは同じ時間で、より多くのDiff、Test、Log、Specificationを見ることになる。

そのとき「全部確認している」という事実と、「全部を十分に判断できている」という事実は一致しない。Queueが伸びる。Reviewが浅くなる。重要度に関係なく同じ深さで見る。最後には承認が形式化する。

Gateは残っている。安全性は落ちている。

「全部確認しない」と言っても、確認を雑にするわけではない。**Failureをいちばん見つけやすい場所へ、確認を分ける。**

Format違反はLintが見る。型の不整合はCompilerが見る。既知のRegressionはTestが見る。代理期間のBoundaryはVerification Procedureが見る。Production WriteはPermissionが止める。

そのうえで、曖昧なRequirement、法的Accountability、不可逆なData Migration、Risk Appetiteの変更は人が見る。

```text
Machine-detectable Failure → Machine Check
Reproducible Behavior → Verification / Eval
High-risk / Ambiguous Decision → Human
Unknown → Escalation
```

こうすると、人のAttentionを全部へ薄く撒かず、本当に判断が必要な場所へ残せる。

Gateの数だけ見ると減っている。それでも、検出できるFailureの種類は増やせる。

FlowDeskのAudit Logを毎回人がCodeで探す代わりに、実際の代理承認を実行し、元Approver IDとProxy Approver IDが記録されることを機械的に検査する。このCheckが安定していれば、人はCompliance Ruleそのものの妥当性へAttentionを使える。

もちろん、Machine Checkを盲信してはいけない。Test自体が間違う。Evaluatorも同じ誤解をする。だからShadow Evaluation、False Accept、Escaped Defect、Evaluator Independence、Samplingが必要になる。

全部を人に見せない設計の方が、実は難しい。

条件を作らずHuman Reviewだけ減らせば、ただ見なくなっただけだ。Machine Check、Evidence、Escalationまで揃えて初めて、Controlの場所を移したと言える。

> **安全とは、人が見た量ではない。必要なFailureが、適切な仕組みで検出される状態である。**

成熟したAI Native Systemでは、「人が全部見ているから安全」ではなく、「何を誰がどう検出するかが設計されているから安全」へ変わっていく。

---

## 23.2-A Decision Rights Delegation Protocol

ここはDecision RightsのOperational Homeである。Ch10で「誰が決めるか」を理解したあと、Human / AI間でその判断をどう移すかを具体化する。

Human Gateを縮めるときは、「チェックを外した」とだけ記録しない。**どのDecisionを、どの条件でAIへ任せられるようになったか**をDelegation Envelopeの変更として残す。

```text
初期
Human Decision Surface = 大
AI Delegation Envelope = 小

成熟
Human Decision Surface = Risk / Exception / Policy中心
AI Delegation Envelope = Planning / Execution / Evaluation / Coordinationへ拡大
```

### Subsidiarity for Human-AI Teams

> **判断は、信頼可能に判断できる最も実行に近い主体へ置く。**

Agent自身で機械検証できるならAgent、独立AI Evaluatorで判定できるならAI Evaluation、組織Risk・曖昧性・Accountabilityが残るならHumanへ上げる。

### Delegation Contract

継続的なDecision Rights委譲には次を必須とする。

```yaml
delegation:
  decision_class:
  scope:
  allowed_actions:
  evidence_required:
  escalation_conditions:
  expiry:
  audit:
  disclosure:
  rollback_or_revoke:
```

`scope: all` のような無限定委譲を標準形にしない。

### S Transition Protocol

承認強度を弱める場合、一度に飛ばさない。

```text
S5
↓ measure
S4
↓ measure
S3
↓ measure
S2 / S1
↓ measure
必要ならGate自体を削除
```

各段で最低限、False Accept / Defect / Override / Approval Wait / Rubber-stamp兆候を観測する。悪化すれば即座に強いSへ戻せることを前提にする。

### Approval Hollowingを監視する

Gateが存在していても、次の兆候があれば実質的な統制が抜けている可能性がある。

- 承認時間が不自然に短い
- 承認Queueが長期滞留する
- 委任記録だけが急増する
- Decision Packetを開かず承認される
- lease / claimが失効したまま放置される
- 例外的な「今回は通す」が常態化する

対策の主手段は承認者を責めることではない。

```text
承認1件あたりの判断コストを下げる
→ self-contained Decision Packet

承認回数そのものを減らす
→ machine-detectable / reversible / low-risk領域を委譲
```

承認帯域が足りない状態を放置すると、遅延だけでなく**Governanceそのものが劣化する。**

### 23.2-A.1 Why — なぜDecision RightsはTool Permissionより重要なのか

「AIに何をさせてよいか」を考えると、まずPermissionの話が出てくる。File Writeを許すか。Terminalを許すか。Productionへ接続してよいか。

もちろんPermissionは要る。危険な操作を技術的に止める仕組みは欠かせない。

ただし、Permissionだけでは仕事の権限は決まらない。

FlowDeskのAgentにDatabase Write権限があるとする。それは「代理承認Ruleを変更してよい」という意味ではない。ProductionへDeployできる権限があっても、「高額申請ではCompliance Approvalを不要にしてよい」という意味ではない。

Tool Permissionが答えるのは、**その操作を実行できるか**。Decision Rightsが答えるのは、**その判断をしてよいか**である。

```text
Permission
Can I do this operation?

Decision Right
Am I authorized to make this decision?
```

人間の会社でも同じである。経理Systemへ入力できる社員が、会社の支払Policyを変更できるわけではない。SCMへMergeできるEngineerが、ProductのRisk Appetiteを一人で変えられるわけではない。

AIではToolが強力なため、この境界が見えにくい。Agentへ広いTool権限を渡すと、できることが増え、そのまま「任せられることも増えた」ように感じる。

仕事を任せるなら、先に仕事側の条件を決める。何のDecision Classか。Scopeはどこまでか。どんなEvidenceが要るか。どのRiskまで自分で進めてよいか。どこでHumanへ戻すか。権限はいつ切れるか。

その後で、必要最小限のTool Permissionを与える。

```text
Purpose / Work
↓
Decision Rights
↓
Delegation Contract
↓
Required Tool Permission
↓
Execution
```

逆に、Tool Permissionから設計すると「使えるから使う」が起きる。

同じAgentが技術的には全部できても、Decision Rightsは別々に持たせられる。ここに自律化の余地が生まれる。

Permissionを狭くしすぎればAIは働けない。広げすぎれば危険になる。そこで、**Decision Rightsを先に絞り、その判断を実行するために必要なPermissionだけを十分に渡す。**

そしてDecision Rightsは固定ではない。Shadow Evaluationで判定精度を測り、Evidenceが安定し、失敗が検出可能で、RollbackできるならScopeを広げられる。逆にIncidentが出れば縮められる。

> **AI自律化の核心は、どのToolを使わせるかではない。どの判断を、どの条件で任せるかである。**

PermissionはExecution Controlの話で、Decision RightsはOperating Modelの話だ。似て見えても、決めているものが違う。

## 23.3 人間の仕事の変化 — ただし到達点を固定しない

AI Native化の初期には、AIがExecutionを多く担うことで、人間のAttentionはより高い抽象度の判断へ移りやすい。

### 初期

```text
人間
├ 調査確認
├ 設計確認
├ 実装確認
├ Test確認
├ PR確認
└ Document確認
```

### Harness / Evalが成熟したProfile

```text
人間
├ Outcome
├ 優先順位
├ 制約
├ Risk
├ Architecture Boundary
├ 例外
├ 投資判断
└ Harness Performance

AI
├ Planning
├ Decomposition
├ Execution
├ Coordination
├ Verification
├ Review Assistance
└ Improvement Proposal
```

人間を「AIの操作員」にしない。
Harnessが成熟するほど、人間は細粒度作業から離れやすい。

しかし、DeepRailはここをHumanの最終到達点とは定義しない。
AIの能力向上によって、Priority Proposal、Resource Allocation、Policy Draft、Strategy Option Design等もAIへ移り得る。

> **AI時代に固定されたHuman-only Work Listはない。あるのは、その時点での責任配置と、責任を移す条件である。**

---

### Reviewの抽象度は上がるが、それ自体も固定しない

AI Native化によって人間のReviewが消えるわけではない。
導入初期〜中期では、

```text
Artifact Review
↓
Decision Review
↓
Management Review
↓
Governance Review
```

へ抽象度が上がることが多い。

成熟したTeamでは、人間は主に、

```text
Outcome
Risk
Architecture Boundary
Exception
Investment
Irreversible Decision
Policy Change
```

をReviewする。

ただし、AIがこれらの分析・比較・一部判断を担えるようになればHuman Gateの配置も再評価する。
Human Gateは聖域ではなく、**Evidence / Risk / Accountabilityに応じて移動するControl Point**である。

---

### 現時点のHuman Accountability Profile

```text
Human Accountability
= Strategy / Objectiveの最終責任
+ Risk Appetite
+ Decision Rights設計
+ Evaluation Function設計
+ Exception Judgment
+ 法的・組織的Accountability
```

これは「人間しか戦略を考えられない」という能力主張ではない。
組織が現時点で誰にAccountabilityを置くかという**Governance上のProfile**である。

## 23.4 自律化に伴いReview対象も変える

自律化とは「人間が何も見なくなる」ことではない。

```text
A0-A1
Human:
- Plan
- Code
- Test
- PR
を細かく確認

A2
Human:
- Issue Plan
- High-risk Diff
- Test Evidence
を確認

A3
Human:
- Feature Decision
- Cross-Issue整合
- Exception
を確認

A4+
Human:
- Epic Outcome
- Risk
- Architecture
- Harness Metrics
- Escalation
を確認
```

Reviewの対象を成果物の量からDecision/Evidenceへ移す。

その前提条件：

- Specが明示
- Traceabilityあり
- Testが強い
- Standardsが機械/AIで確認可能
- Review Packetが生成可能
- Evalが安定
- Risk Classificationが機能

これらが不足したままHuman Reviewだけを外してはならない。

---

# 第VI部補遺 v0.8新設仕様 — 組織・実行環境・強制と観測

> v0.8から `DR-M20`〜`DR-M24` を正式なManual IDとして追加する。
> Manual IDは安定識別子として扱い、章番号とは分離する。


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 26. AIの成果を人間はどう評価するか

**Creator / Lead Author: RIO AMADA**

## 21.X Human Evaluation Interface

ここをHuman Review / Evidence InterfaceのCanonical Homeとする。前段では「Review Queueが詰まる」という症状までを扱い、ここで初めて判断のInterfaceを本格的に設計する。

AIが人間へ判断を要求するとき、Raw Artifactをそのまま渡してはいけない。

Human Gateへ判断材料を渡す形式を **Human Evaluation Interface** と呼ぶ。

基本原則：

> **AIは人間に成果物を渡すのではなく、判断を渡す。**

人間判断を求める場合、AIは最低限次を提示する。

```text
Decision
Recommendation
Reason
Options
Evidence
Risk
Unknown
Reversibility
Requested Action
```

### Human Attention Principle

Human Attentionは有限の組織資源である。

AI成果物の品質には、Correctness / Security / Maintainability等だけでなく、
**Human Reviewability** を含める。

人間が短時間で、

```text
何を決めればよいか
なぜ決める必要があるか
AIは何を推奨するか
何が証明済みか
何が未確認か
Riskは何か
戻せるか
```

を判断できない場合、Human Evaluation Interfaceの品質が低いとみなす。

### 21.X.0.1 Why — なぜHuman Reviewが新しいBottleneckになり得るのか

AIで実装は速くなった。

それでも、開発全体は思ったほど速くならない。

こういうことは起こり得る。理由は単純で、**最後に人が全部読む設計が、そのまま残っているからだ。**

FlowDeskの代理承認を考える。Frontend、Backend、権限判定、監査Log、Test。仕事を独立した単位へ分けられれば、AIは複数の変更を並行して進められる。以前より短い時間で、Review待ちの成果物が並ぶ。

ここまでは狙い通りである。

問題は、その次だ。

人間のReviewerが一つずつDiffを開く。変更理由をIssueから探す。仕様を読み直す。Test結果を見る。権限への影響を考える。別の変更との組み合わせを頭の中で再現する。分からなければAgentへ聞く。

一つなら読める。

複数が同時に来ると、急に重くなる。

AI側の実行能力は増えたのに、最後の評価方法だけが「人がRaw Artifactを最初から読み直す」のままだと、制約はReview側へ移る。AIが遅いのではない。**速くなった工程の次に、詰まる場所が移っただけである。**

ここで、Reviewを減らすことだけを目標にすると危ない。

人が見ること自体が悪いわけではない。問題は、何を見るかが毎回Reviewerの頭の中で決まっていることだ。

Securityに関わる変更、Data Migration、後戻りしにくいArchitecture変更、検出しづらいFailure。こうした仕事では、CodeやDiffを人が直接読む意味は残る。Human Reviewをゼロにすることが目標ではない。

それでも、すべての変更で同じ深さの確認を要求する必要はない。

たとえばFlowDeskで、「代理承認時に元のApprover IDがAudit Logへ残ること」を確認したいとする。人が巨大なDiffから探し始めるより、Acceptance、実行したVerification、実際のLog、残っているUnknownを先に見た方が判断は速い。必要なら、そこからCodeへ降りればいい。

順番を変える。

```text
Raw Artifactを全部読む
↓
頭の中で意図とRiskを再構成する
↓
判断する
```

ではなく、

```text
何を判断するかを見る
↓
Evidenceで確かめる
↓
Risk / Unknownを見る
↓
必要なところだけRaw Artifactへ降りる
```

へ変える。

この順番を支えるのがHuman Evaluation Interfaceである。Decision PacketやReview Packetは情報を隠すものではない。人のAttentionを、判断が必要な場所へ先に向ける。

AIが大量に作る時代ほど、この差は大きくなる。

実装者が一人増えれば、Review側も同じように増やせばいい、という話ではない。ReviewerにはDomain理解、Architecture、Security、Production事情のような希少なContextが必要なことがある。人数だけ増やしても、同じ判断能力をすぐ複製できるとは限らない。

人を増やすだけで解けないなら、Reviewの仕事そのものを組み直すしかない。

- Machine Checkで先に落とせるものは何か
- AIの一次評価をShadowでCalibrationできるか
- Work Classごとに必要なEvidenceは何か
- どのFailureは人間が直接見るべきか
- どこはSamplingへ移せるか
- どのDecisionはまだHuman Gateへ残すべきか

ここまで揃って、ようやくAIの速度をDelivery全体で受け止められる。

そして、Reviewの仕事そのものも変わっていく。

最初はArtifactを見る。次にDecisionとEvidenceを見る。さらに評価系が成熟すれば、Exceptionや高Risk Decisionを見る。最後には、個々の変更より、Evaluation FunctionやRisk PolicyそのものをReviewする比重が上がる。

人のReviewは、すぐには消えない。

先に変わるのは、**何を見るか**だ。

FlowDeskのSceneへ戻る。複数の成果物がReview待ちで並んでいる。ここで必要なのは、人間を急がせることではない。すべてを読む仕事を、すべて読まなくても判断できる仕事へ作り直すことだ。

> **人が全部見る仕組みは、人の速度を超えられない。AI Native化で変えるべきなのは、生成速度だけではなく、最後に人が何を見てGOを出すかである。**

### 21.X.0.2 Why — なぜEvidenceをInterfaceとして扱うのか

AIが「終わりました」と言った。

この一言には、ほとんど情報がない。

Codeはあるかもしれない。Testも通っているかもしれない。だが、判断する側が本当に知りたいのは「何を作ったか」だけではない。**この変更を次へ進めてよいと、何を根拠に言えるのか**である。

FlowDeskの代理承認を例にする。Agentが実装を終え、Pull Requestを作った。変更は1,200行ある。人間がDiffを全部読めば、実装内容はある程度分かる。

それでも、読んだだけでは答えにくい問いが残る。代理期間を過ぎたUserは本当に拒否されるのか。高額申請ではCompliance Approverを飛ばさないか。Audit Logには元ApproverとProxy Approverの両方が残るか。既存Clientとの互換性は保たれているか。

CodeはArtifactである。判断には、もう一段別の形がいる。

そこで、Evidenceを判断の入口にする。

EvidenceをInterfaceと呼ぶのには理由がある。最後に付ける添付資料では足りない。次のDecisionをする側が、そのまま判断に使える形で検証結果を渡したい。

```text
Intent / Acceptance
↓
Verification
↓
Observed Result
↓
Evidence
↓
Decision
```

たとえば「期限切れの代理者は承認できない」というAcceptanceなら、欲しいのはAgentの説明ではない。期限切れ条件で実際に操作し、拒否された結果、その時のLog、使ったEnvironment、未確認条件である。

この形なら、人間だけでなく別のAI Evaluatorも読める。次工程のGateも使える。後日のAuditでもたどれる。再実行可能なら、条件が変わった後に確かめ直せる。

Codeを読む価値は残る。ArchitectureやSecurity、Maintainabilityのように、Raw Artifactそのものを見るべき判断もある。必要なときは、そこまで降りればいい。

ただ、すべてのDecisionを「Codeを全部読んだ人の頭の中」で成立させると、その判断は再利用しにくい。何を確認し、なぜOKとしたのかが、Reviewer個人へ閉じるからだ。

EvidenceをInterfaceにすると、判断の材料が外へ出る。

```text
「読んだ感じ大丈夫」ではなく

何を確かめたか
何が観測されたか
何がまだ分からないか
どのRiskが残るか
```

を共有できる。

Evidenceが弱ければ、Decision Rightsを広げない。Evidenceが十分に強く、Failureを検出でき、再現可能なら、一部の判断をAI Evaluationへ移せる。

Evidenceを最後のDocumentationに回すと遅い。仕事を任せたあと、その成果を信じて次へ進むまでの途中に置く。

> **Codeは成果物である。Evidenceは、その成果物を次へ進めてよいか判断するためのInterfaceである。**

FlowDeskで1,200行のDiffができても、最初に見るべきものが1,200行とは限らない。最初に見るべきなのは、「代理承認は正しく成立した」と言える根拠である。

---

## 21.X.1 Decision Packet

Review PacketをPR/MR専用の成果物として閉じず、
Human Decision全般へ一般化したものを **Decision Packet** とする。

```markdown
# Decision Packet

## 1. Decision Required
今回、人間に決めてほしいこと

## 2. Recommendation
AIの推奨案

## 3. Why Human Decision Is Required
なぜ委譲範囲を超えるのか

## 4. Outcome Impact
この判断がOutcomeへどう影響するか

## 5. Options
選択肢
- Option A
- Option B
- Option C

## 6. Evidence
EV-3 Observed Behavior
EV-2 Machine Check
その他の根拠

## 7. Risk
Risk Class / Failure Mode / Blast Radius

## 8. Unknowns
未確認事項・不確実性

## 9. Reversibility
Rollback可能性 / Cost / Time

## 10. Requested Action
Approve / Reject / Request Change / Defer / Escalate
```

AIは「確認お願いします」だけをHumanへ投げない。

### 21.X.1.1 Delegation Decision Trail

長時間・多Phase・無人実行では、最終Decision Packetだけでなく、重要な判断の経路を追跡可能にする。
Humanが全文Transcriptを読むことを前提にしない。

Decision Trailは最低限次を持つ。

```text
ts / phase
Decision
Rationale
Evidence Pointer
Result
Deviation / Pivot
Unknown / Open Risk
```

原則：

1. **重要な判断点だけを記録する** — 全Tool Callや全思考過程を記録しない。
2. **EvidenceはPointerを優先する** — Commit / Test Result / Trace / Screenshot / Artifact等へ辿れるようにする。
3. **Append-onlyを基本とする** — 判断変更は過去を書き換えず、Supersede / Revertとして新しいEntryを追加する。
4. **Resultを残す** — `accepted / reverted / inconclusive / open` 等、判断後に何が起きたかを記録する。
5. **Handoff時に圧縮する** — HumanへはOutcome / Important Decisions / Evidence / Deviations / UnknownsをDecision Packetへ要約する。

```text
Autonomous Execution
↓
Decision Trail
↓
Outcome + Evidence + Important Decisions
↓
Decision Packet / Review Packet
↓
Human / Policy Decision
```

Decision Trailは監視のための逐語ログではなく、**後から「なぜこのOutcomeになったか」を再構成するためのAudit / Review Interface**である。

---

## 21.X.2 Progressive Disclosure

人間への提示は、

```text
Level 0
Decisionだけ

↓ Drill-down

Level 1
Summary
Intent / Recommendation / Risk / Evidence / Unknown

↓ Drill-down

Level 2
Evidence
Acceptance Criteria / Test / Decision / Traceability

↓ Drill-down

Level 3
Raw Artifact
Spec / Design / Diff / Code / Log / Trace
```

の順を基本とする。

最初から巨大DiffやRaw Logを読ませない。
必要な人だけ深掘りできる状態を作る。

この順序は情報を隠すためではない。Humanがまず「承認すべき判断」を理解し、その判断に必要なEvidenceだけを追跡し、必要な場合にCodeまで降りられるようにするためである。

**Code / DiffはLevel 3の重要なRaw Evidenceであり得るが、Human Reviewの既定入口ではない。**

---

## 21.X.3 Work Level別のManagement View

同じ情報を全Roleへ見せない。

| Work Level | 人間が主に評価するもの |
|---|---|
| Portfolio | Investment / Strategic Fit / Outcome / Risk |
| Epic | Outcome / Scope / Owner / Dependency / Risk |
| Feature | Capability / Acceptance / Boundary |
| Issue | Intent / Acceptance / Evidence / Exception |
| PR / MR | Decision / High-risk Diff / Automated Evidence |
| Release | Release Scope / Residual Risk / Rollback |
| Transformation | Constraint / Approval / Adoption / Outcome |

AIは受け手のRoleとDecision Rightsに応じてViewを変える。

---

## 21.X.4 Evaluation Maturity

人間の評価対象は成熟度とAutonomyによって変える。

```text
Stage 1
Human reviews Artifact

Stage 2
Human reviews Decision + Evidence

Stage 3
AI evaluates Artifact
Human reviews Exception / High-risk Decision

Stage 4
Human defines Evaluation Function
AI executes + evaluates + retries

Stage 5
Human reviews
Outcome / Risk / Investment / Exception
```

最終状態でもHuman Reviewはゼロにならない。

Reviewの抽象度が上がる。

なお、成熟度を「HumanがCodeを見なくなった割合」で測らない。評価するのは、対象Work Classについて必要なFailure Modeが検出可能で、Approved Evidenceが成立し、Riskに応じたDecision Rightsを安全に委譲できているかである。

---


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 27. AIの評価をどこまで信頼しGO判断を委譲するか

**Creator / Lead Author: RIO AMADA**

## 21.X.5 Evaluation Authority — AI評価にどこまでGO権限を与えるか

Human / AIの評価分担を「人間30%・AI70%」のような割合で設計しない。
評価権限は**Work Class / Decision Classごと**に定義する。

Evaluation Authorityは `EA0〜EA4` で表す。

| Level | 名称 | AIの評価権限 | Humanの関与 |
|---|---|---|---|
| EA0 | Human Evaluation | AI評価をGate根拠にしない | Humanが評価・GO |
| EA1 | Shadow Evaluation | AIも並行評価するがGO権限なし | Humanが全件判断。差分をCalibrationに使う |
| EA2 | AI-First / Human Decision | AI評価を一次評価として採用 | HumanはDecision Packet / Evidenceから最終GO |
| EA3 | Audited Autonomy | 定義済みWork ClassではAIが評価・GO可能 | HumanはException / Sampling / Audit |
| EA4 | Policy-Governed Autonomy | Policy内でAIが評価・GO・Retryまで実施 | HumanはEvaluation Function / Risk Appetite / Policy / Exceptionを管理 |

`EA`はAIのExecution Autonomy `A0〜A5`とも、Approval Strength `S1〜S5`とも別軸である。

```text
A  = 何をAIが実行できるか
EA = 何をAIが評価し、GO判断できるか
S  = 承認をどの強度・形式で成立させるか
```

例：

```text
A3 × EA1 × S4
Feature内の実行はAIが進める
AI評価はShadowとして記録
最終GOは人間が非同期台帳で承認

A3 × EA3 × S1
Feature内の実行・評価を定義済み範囲でAIへ委譲
人間はSampling / Exceptionを監査
委任規程に基づきAIが承認記録
```

AIが高性能であること自体はEA昇格条件ではない。
対象Work Classで、必要なEvidence・Failure検知・Rollback・Auditが成立していることを要求する。

---

## 21.X.6 Evaluation Delegationの導入手順

AI評価への信頼は、説明やデモではなく**比較実績**から作る。

### Step 0: Work ClassとEvaluation Contractを固定する

```text
対象Work Class
Acceptance Criteria
Evaluation Criteria
Required Evidence
Risk Class
Failure Detectability
Reversibility
Accountability Owner
```

「AI全般を信用できるか」ではなく、対象を狭くする。

### Step 1: Shadow Evaluation

HumanとAIが独立に同じ対象を評価する。AIの判定はまだGateへ効かせない。

```text
AI  : GO / NG / UNKNOWN + Evidence
Human: GO / NG / UNKNOWN + Reason
```

### Step 2: Disagreementを分類する

単純にHumanを正解と固定しない。

```text
AI Error
Human Error
Ambiguous Criteria
Missing Evidence
Environment Mismatch
Requirement / Spec Drift
Unknown / Unclassifiable
```

人間同士の判断揺れもCalibration対象とする。

### Step 3: Calibration Evidenceを蓄積する

最低限、次を観測する。

```text
True Accept
True Reject
False Accept   # AIがGOしたが本来NG。最重要
False Reject
Unknown Rate
Human Override Rate
Missing Evidence Rate
Escaped Defect
Rollback / Incident
```

全領域共通の昇格閾値は規定しない。Risk AppetiteとWork Classに応じて組織がExit Criteriaを定義する。

### Step 4: Bounded Delegation

十分なEvidenceが得られた**限定Work Classだけ**EAを上げる。

```text
EA1 → EA2
AIが一次評価
HumanはDecision / Evidence中心に確認

EA2 → EA3
AIが通常GO
HumanはException / Sampling / Auditへ移行
```

### Step 5: Audit / Drift Monitoring

委譲後も固定しない。

- Model変更
- Prompt / Context / Harness変更
- Test変更
- Environment変更
- Domain変更
- Failure Pattern変化

があれば再Calibrationする。

### Step 6: Expand or Roll Back

品質が維持できれば隣接Work Classへ展開する。
False Accept、重大Incident、Evidence欠落、Eval Driftが増えた場合はEAを戻す。

> **Evaluation Authorityは成熟度バッジではなく、対象領域ごとに上げ下げする運用Profileである。**

---

## 21.X.7 Independent Evaluation Contract

Evaluation Authorityを上げる前に、評価系統そのものを設計する。

### Generation / Evaluation Separation

実装した主体の自己評価だけでEAを上げない。

```text
Executor
  ↓ Artifact + minimal provenance
Evaluator: Standards axis
Evaluator: Specification axis
  ↓
Independent Evidence
```

推奨原則：

1. **fresh context** — 実装時の長い会話履歴をそのまま評価へ渡さない。
2. **axis separation** — StandardsとSpecificationを別軸で評価する。
3. **AND semantics** — 一方の合格で他方の不合格を相殺しない。
4. **positive context list** — 評価系に渡す案件固有ContextをGLOSSARY / ADR / Contract等の正本へ限定する。
5. **disagreement escalation** — 独立Evaluator間の不一致を多数決だけで閉じず、Unknown / Human Decision候補にする。

### Failure-Mode Independence / Evaluator Diversity

Evaluator Independenceは「別Agent」「別Model」「別Prompt」という形式だけでは判定しない。
同じ誤ったSpecification、同じContext Gap、同じModel Family、同じ観測不能点を共有していれば、複数Evaluatorが同じ誤判定をする可能性がある。

独立性は次の観点で確認する。

```text
Evaluation Axis Diversity
→ Specification / Standards / Security / Runtime / UX / Policy

Evidence Source Diversity
→ Test / Static Analysis / Runtime Observation / Trace / External Source

Context Independence
→ Executorの会話履歴・自己説明へ過度依存しない

Model / Method Diversity
→ 必要な場合のみ異なるModel / Algorithm / Human Judgmentを組み合わせる

Failure Correlation
→ 同じFailure Modeを同時に見逃す可能性を評価する
```

```text
複数Evaluatorが一致
→ High-signal候補
→ Truthとは限らない

Evaluatorが不一致
→ Criteria / Context / Unknown / Environmentを再確認
→ 必要ならHuman / Domain Decision
```

多数決はIndependent Evaluationの代替ではない。
目的はEvaluator数を増やすことではなく、**重要なFailureを同時に見逃す相関を下げること**である。

低RiskでDeterministic Checkが十分なWork Classでは多系統評価を省略してよい。独立性のコスト自体もRiskで調整する。

## 21.X.8 Evaluator Re-execution Principle

合否の根拠は、可能な範囲で**判定者自身が再実行・再取得した観測**にする。

```text
根拠にできる
→ Evaluator自身のtest / query / read-back / observation

参考情報
→ Executorの説明
→ Executorが貼ったログ
→ Executorの「テスト済み」自己申告
```

Write系操作はread-backを完了条件へ含める。破壊的・不可逆な操作は再実行せず、read-back / immutable log / environment evidenceへ置き換える。

### 21.X.8.1 Reproducible Evidence Principle

Evidence StrengthとReproducibilityを混同しない。
EV-3のObserved Behaviorでも、一度しか再現できない場合がある。一方で、低RiskなMachine Checkは容易に再実行できる。

可能な範囲で、Evidenceには次を紐づける。

```text
What was verified
Verification Procedure
Input / Preconditions
Environment / Version / Provenance
Observed Result
Evidence Location
Cleanup / Side Effect
Re-run Constraint
```

Verification Procedureは、実際のUser Path / Runtime Behavior / External Effectを検証できる場合、それをProxyだけで置き換えない。
生成したVerification Script / Skill / Checker自体も、少なくとも一度は実行して成立を確認する。

```text
Executor Self Report
→ 弱い根拠

Snapshot / Log / Screenshot
→ 観測Evidence

Re-runnable Test / Checker / Script / Eval
→ 再確認可能なEvidence

CI / Hook / Gateへ統合済み
→ 継続的に再評価されるEvidence System
```

ただし、Machine Re-executionを万能視しない。Domain Judgment / Security Exception / Legal / Irreversible Operation等ではHuman DecisionやImmutable Evidenceを残し、Work Classに応じて最適なEvidence Contractを選ぶ。

## 21.X.9 Evaluator Permission Isolation

評価主体は、可能な限りTool面でRead-onlyにする。

```text
Evaluator
Read   ✓
Test   ✓（非破壊）
Write  ✗
Merge  ✗
Release ✗
```

Promptへ「変更しないで」と書くだけの場合、強制済みとはみなさずEnforcement Ledgerで `declared_only` とする。

自動修正が必要なら、EvaluatorとFixerを別系統へ分ける。

## 21.X.10 Human Gateの品質

Human Gateの成功条件は、

```text
人間が画面を開いた
人間がApproveを押した
```

ではない。

次を満たしたかで評価する。

```text
Decision対象が明確
必要Evidenceが揃っている
Riskが開示されている
Unknownが隠されていない
代替案が比較可能
人間がDecision Rightsを持つ
判断がTraceable
```

Approvalが形だけ残っているなら、Gateがあるとは数えない。Failureとして見る。

---


---

## 23.2 Human Gateの減らし方

Human Gateは「ある / ない」の二値ではない。
自律化Level A0〜A5と、各Gateの**承認強度 S1〜S5**は分けて管理する。

| 強度 | 形態 | 定義 |
|---|---|---|
| S5 | 対面同期承認 | 人間が成果物を確認し、その場で承認 |
| S4 | 台帳非同期承認 | 人間が非同期で確認し、承認台帳へ記録 |
| S3 | 非同期リレー承認 | 人間が判断し、AIが正本台帳へ転記。判断記録と転記を照合可能にする |
| S2 | 完了判定委任 | 事前に定義した基準に基づき、指名された人間へ判定を委任 |
| S1 | AI代行承認 | 明示的な委任規程に基づきAIが承認を記録 |

S1/S2を使う場合、委任規程に最低限次を持つ。

```yaml
delegation:
  scope:      # 対象工程・Gate・Work Item
  expiry:     # 期限または失効条件
  audit:      # 誰がどの頻度で事後確認するか
  disclosure: # 代行・委任実績を誰へいつ開示するか
```

承認は対象操作を明示した確認にだけ効力を持つ。
古い成果物への承認を、新しい版へ流用しない。

Gate削減は感覚で行わない。

Human Gateを減らす前に、DR-M17のEvaluation Authority `EA0〜EA4`で対象Work Classの評価権限をCalibrationする。

```text
Work Classを限定
↓
EA1 Shadow Evaluation
Human / AIの判定差を測定
↓
Evaluation Criteria / Evidenceを改善
↓
EA2 AI-First + Human Decision
↓
一定期間、False Accept / Escaped Defect / Overrideを測定
↓
EA3 Audited Autonomy
HumanはSampling / Exceptionへ
↓
Policy・Risk Appetiteまで安定
↓
EA4 Policy-Governed Autonomyを検討
```

Human Gateの削減目的は「人間をゼロにすること」ではない。
**人間のAttentionを、曖昧性・重大Risk・不可逆Decision・法的/組織的Accountabilityへ集中させること**である。

また、Autonomy / Evaluation Authority / Approval Strengthを混同しない。

```text
Execution Autonomy A0〜A5
×
Evaluation Authority EA0〜EA4
×
Approval Strength S1〜S5
```

同じA3でも、評価実績が少ないTeamはEA1、十分なCalibration Evidenceを持つTeamはEA3というProfileが成立する。

### 23.2.0 Gateを評価する主体は段階的に移せる

Human Gateを減らすとき、StepやControl Pointまで一緒に消す必要はない。

変えるのは、誰がEvidenceを集め、誰が評価し、誰がGOを成立させるかである。

```text
Initial
AI Generate / Execute
↓
Human Review
↓
Human Approve

        ↓ Calibration

AI-First
Generation Agent
↓
Review Agent / Automated Eval
↓
Human Decision

        ↓ Bounded Delegation

Audited Autonomy
Agent Execution
↓
Independent Evaluation
↓
通常CaseはAIがGO
└─ Exception / Sampling → Human

        ↓ Policy Stabilization

Policy-Governed Autonomy
Multi-Agent / Agent Execution
↓
Automated Evaluation
↓
Policy Gate
├─ PASS → 自動で次工程へ
├─ RETRY → 定義済み範囲で再実行
└─ EXCEPTION → Human Intervention
```

この移行で、人間の関与は単純に「減る」のではない。
Artifactの逐次確認から、Evaluation Function、Risk Appetite、Policy、重大例外、監査へ比重が移る。

**Human Gateを消しているのではない。Gateを成立させるEvidenceと、判断する主体を変えている。**

### 23.2.1 Why — なぜ「全部確認しない」方が安全になり得るのか

「AIが作ったものは、人間が全部確認する。」

最初は、このルールが一番安全に見える。未知のToolを導入したばかりなら、実際それでいい。何を間違えるか分からない時期にHuman Gateを厚くするのは自然である。

問題は、そのルールを成熟後も変えないことだ。

FlowDeskで、AIが一日に二つの小変更しか作らないなら、人が全部読める。十、二十、五十と増えたらどうなるか。Reviewerは同じ時間で、より多くのDiff、Test、Log、Specificationを見ることになる。

そのとき「全部確認している」という事実と、「全部を十分に判断できている」という事実は一致しない。Queueが伸びる。Reviewが浅くなる。重要度に関係なく同じ深さで見る。最後には承認が形式化する。

Gateは残っている。安全性は落ちている。

「全部確認しない」と言っても、確認を雑にするわけではない。**Failureをいちばん見つけやすい場所へ、確認を分ける。**

Format違反はLintが見る。型の不整合はCompilerが見る。既知のRegressionはTestが見る。代理期間のBoundaryはVerification Procedureが見る。Production WriteはPermissionが止める。

そのうえで、曖昧なRequirement、法的Accountability、不可逆なData Migration、Risk Appetiteの変更は人が見る。

```text
Machine-detectable Failure → Machine Check
Reproducible Behavior → Verification / Eval
High-risk / Ambiguous Decision → Human
Unknown → Escalation
```

こうすると、人のAttentionを全部へ薄く撒かず、本当に判断が必要な場所へ残せる。

Gateの数だけ見ると減っている。それでも、検出できるFailureの種類は増やせる。

FlowDeskのAudit Logを毎回人がCodeで探す代わりに、実際の代理承認を実行し、元Approver IDとProxy Approver IDが記録されることを機械的に検査する。このCheckが安定していれば、人はCompliance Ruleそのものの妥当性へAttentionを使える。

もちろん、Machine Checkを盲信してはいけない。Test自体が間違う。Evaluatorも同じ誤解をする。だからShadow Evaluation、False Accept、Escaped Defect、Evaluator Independence、Samplingが必要になる。

全部を人に見せない設計の方が、実は難しい。

条件を作らずHuman Reviewだけ減らせば、ただ見なくなっただけだ。Machine Check、Evidence、Escalationまで揃えて初めて、Controlの場所を移したと言える。

> **安全とは、人が見た量ではない。必要なFailureが、適切な仕組みで検出される状態である。**

成熟したAI Native Systemでは、「人が全部見ているから安全」ではなく、「何を誰がどう検出するかが設計されているから安全」へ変わっていく。

---

## 23.2-A Decision Rights Delegation Protocol

ここはDecision RightsのOperational Homeである。Ch10で「誰が決めるか」を理解したあと、Human / AI間でその判断をどう移すかを具体化する。

Human Gateを縮めるときは、「チェックを外した」とだけ記録しない。**どのDecisionを、どの条件でAIへ任せられるようになったか**をDelegation Envelopeの変更として残す。

```text
初期
Human Decision Surface = 大
AI Delegation Envelope = 小

成熟
Human Decision Surface = Risk / Exception / Policy中心
AI Delegation Envelope = Planning / Execution / Evaluation / Coordinationへ拡大
```

### Subsidiarity for Human-AI Teams

> **判断は、信頼可能に判断できる最も実行に近い主体へ置く。**

Agent自身で機械検証できるならAgent、独立AI Evaluatorで判定できるならAI Evaluation、組織Risk・曖昧性・Accountabilityが残るならHumanへ上げる。

### Delegation Contract

継続的なDecision Rights委譲には次を必須とする。

```yaml
delegation:
  decision_class:
  scope:
  allowed_actions:
  evidence_required:
  escalation_conditions:
  expiry:
  audit:
  disclosure:
  rollback_or_revoke:
```

`scope: all` のような無限定委譲を標準形にしない。

### S Transition Protocol

承認強度を弱める場合、一度に飛ばさない。

```text
S5
↓ measure
S4
↓ measure
S3
↓ measure
S2 / S1
↓ measure
必要ならGate自体を削除
```

各段で最低限、False Accept / Defect / Override / Approval Wait / Rubber-stamp兆候を観測する。悪化すれば即座に強いSへ戻せることを前提にする。

### Approval Hollowingを監視する

Gateが存在していても、次の兆候があれば実質的な統制が抜けている可能性がある。

- 承認時間が不自然に短い
- 承認Queueが長期滞留する
- 委任記録だけが急増する
- Decision Packetを開かず承認される
- lease / claimが失効したまま放置される
- 例外的な「今回は通す」が常態化する

対策の主手段は承認者を責めることではない。

```text
承認1件あたりの判断コストを下げる
→ self-contained Decision Packet

承認回数そのものを減らす
→ machine-detectable / reversible / low-risk領域を委譲
```

承認帯域が足りない状態を放置すると、遅延だけでなく**Governanceそのものが劣化する。**

### 23.2-A.1 Why — なぜDecision RightsはTool Permissionより重要なのか

「AIに何をさせてよいか」を考えると、まずPermissionの話が出てくる。File Writeを許すか。Terminalを許すか。Productionへ接続してよいか。

もちろんPermissionは要る。危険な操作を技術的に止める仕組みは欠かせない。

ただし、Permissionだけでは仕事の権限は決まらない。

FlowDeskのAgentにDatabase Write権限があるとする。それは「代理承認Ruleを変更してよい」という意味ではない。ProductionへDeployできる権限があっても、「高額申請ではCompliance Approvalを不要にしてよい」という意味ではない。

Tool Permissionが答えるのは、**その操作を実行できるか**。Decision Rightsが答えるのは、**その判断をしてよいか**である。

```text
Permission
Can I do this operation?

Decision Right
Am I authorized to make this decision?
```

人間の会社でも同じである。経理Systemへ入力できる社員が、会社の支払Policyを変更できるわけではない。SCMへMergeできるEngineerが、ProductのRisk Appetiteを一人で変えられるわけではない。

AIではToolが強力なため、この境界が見えにくい。Agentへ広いTool権限を渡すと、できることが増え、そのまま「任せられることも増えた」ように感じる。

仕事を任せるなら、先に仕事側の条件を決める。何のDecision Classか。Scopeはどこまでか。どんなEvidenceが要るか。どのRiskまで自分で進めてよいか。どこでHumanへ戻すか。権限はいつ切れるか。

その後で、必要最小限のTool Permissionを与える。

```text
Purpose / Work
↓
Decision Rights
↓
Delegation Contract
↓
Required Tool Permission
↓
Execution
```

逆に、Tool Permissionから設計すると「使えるから使う」が起きる。

同じAgentが技術的には全部できても、Decision Rightsは別々に持たせられる。ここに自律化の余地が生まれる。

Permissionを狭くしすぎればAIは働けない。広げすぎれば危険になる。そこで、**Decision Rightsを先に絞り、その判断を実行するために必要なPermissionだけを十分に渡す。**

そしてDecision Rightsは固定ではない。Shadow Evaluationで判定精度を測り、Evidenceが安定し、失敗が検出可能で、RollbackできるならScopeを広げられる。逆にIncidentが出れば縮められる。

> **AI自律化の核心は、どのToolを使わせるかではない。どの判断を、どの条件で任せるかである。**

PermissionはExecution Controlの話で、Decision RightsはOperating Modelの話だ。似て見えても、決めているものが違う。


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 28. AI Nativeな開発Lifecycleをどう設計するか

**Creator / Lead Author: RIO AMADA**

# 9. 05_AI Native Development Lifecycle

DeepRailは、AI駆動開発を「必ずN個の工程を直列に通る手順」として定義しない。

標準化するのは、**開発において抜けてはいけない責務、前進条件、Evidence、戻り先**である。
案件の規模・Risk・Method・Autonomy・Operating Contextに応じて、複数責務を一つの作業へ圧縮しても、Gateとして分離してもよい。

## 9.0 Step / Gateは特定Actorに属さない

Lifecycle上のStepやGateは、人間の作業工程を固定するためのものではない。

Stepは、仕事を安全に前へ進めるための制御単位である。最低限、次を持つ。

```text
Responsibility
Input
Output
Required Evidence
Transition / Exit Condition
Failure / Return Path
```

誰がそのStepを実行し、誰がGateを評価するかはOperating Profileで変わる。

導入初期には、次の形でもよい。

```text
AI Execute
↓
Human Evaluate
↓
Human Gate
```

Evaluation Authorityが上がれば、評価主体を変えられる。

```text
Execution Agent
↓
Review Agent / Automated Eval
↓
Human Decision
```

さらに、対象Work Classで必要なEvidence、Failure Detectability、Rollback、Audit、Policyが成立すれば、通常Caseは人間の個別承認を待たずに進められる。

```text
Agent Execution
↓
Independent Evaluation
↓
Policy Gate
├─ PASS      → Next Step
├─ RETRY     → Controlled Retry
└─ EXCEPTION → Human
```

ここでGateそのものが消えたわけではない。
**Gateを成立させるEvidenceと、Gateを判断する主体が変わっている。**

> **Stepが残ることと、人間が各Stepに残ることは同じではない。**

DeepRailが固定するのは人間の工程ではなく、**仕事が次へ進んでよい条件**である。

---

## 9.1 Lifecycleの責務モデル

```text
Intent / Intake
      ↓
Discover
      ↓
Shape / Visualize
      ↕
Align
      ↓
Decide / Commit
      ↓
Specify / Contract
      ↓
Decompose / Plan
      ↓
Execute
      ↓
Verify / Accept
      ↓
Reinvest / Learn
      ↺
```

### Intent / Intake

何を、なぜ変えるのかを明らかにする。

主なOutput：
- Objective / Expected Outcome
- Customer / User
- Business Context
- Initial Scope
- Constraint
- Decision Owner

### Discover

要求をそのまま実装へ渡さず、背景・現状・Domain・Codebase・制約・未知を調査する。

主な問い：
- 本当の課題は何か
- 現在はどう動いているか
- 顧客の言葉と既存仕様に矛盾はないか
- 何が未確定か
- どのDecisionが後戻りコストを持つか

### Shape / Visualize

抽象要求を、人間同士・人間とAIが**同じ対象を見て判断できる具体物**へ変換する。

```text
UI開発        → Wireframe / Mock / Prototype / User Flow
API           → Request / Response Example
業務設計      → Process / Scenario
見積・営業    → Plan / Price / Scope / Outcome Image
組織変革      → Before / After / Target Operating Model
移行          → Architecture / Migration Scenario
```

この活動の目的は、Shared Realityを作り続けることにある。

### Align

Shapeされた具体物を用いて顧客・利用者・関係者と認識を合わせる。

```text
案を提示
↓
「違う」
↓
Shapeを修正
↺

「これで合っている」
↓
Decisionへ
```

### Decide / Commit

何を採用するか、誰が決めたか、何をまだ決めないかを確定する。

- Decision
- Rationale
- Alternatives
- Risk
- Unknown
- Reversibility
- Decision Owner

高Risk DecisionはDecision Packetを使用してよい。

### Specify / Contract

合意済み内容をAIとチームが推測なしで実行できる契約へ変換する。

- Requirement
- Acceptance Criteria
- Constraint
- Non-goal
- Interface
- Error Strategy
- Security / Data Boundary
- Evidence Requirement

> **仕様は「認識を合わせる最初の道具」ではなく、認識が合った内容を実行可能な契約として固定する道具である。**

### Decompose / Plan

Objective / Epic / Feature / Issue / Agent Taskへ仕事を分解し、Dependency・Risk・Context・Gateを配置する。
分解は人間の手作業だけに限定せず、AIがRubricを使って生成・再分解してよい。

### Execute

AI / Humanが合意済みContractの範囲内で実行する。
AIは実装中に未知・Risk増加・Architecture境界を発見した場合、勝手にObjectiveを変えず、Re-decompositionまたはEscalationへ移る。

### Verify / Accept

Self-reportではなく、Machine Check / Observed Behavior / Human Decisionを用いて、期待したOutcomeへ到達したかを判断する。

### Reinvest / Learn

単なる「記録」ではない。
今回得た成果・判断・失敗・人間介入を、次回のAIと組織がより良く働ける状態へ戻す。

```text
Current Truth
├ Specification
├ API / DB / Architecture
├ ADR
└ Operations

Reusable Learning
├ Rule
├ Skill
├ Eval
├ Agent Contract
├ Gate
└ Harness

Organization
├ Standard
├ Training
├ Decision Policy
└ Operating Model
```

---

## 9.2 Lifecycleは一本道ではない

代表的な戻りを標準化する。

```text
Execute
↓
未知の仕様を発見
↓
Discover / Align
↓
Specify更新
↓
Re-decompose
↓
Execute
```

```text
Verify
↓
Acceptance不一致
├ 実装問題 → Execute
├ Spec問題 → Specify
├ 認識問題 → Align
└ Objective変更 → Requirement ChangeとしてIntakeへ
```

**AIがWorkを再分解できることと、AIがGoalを勝手に再定義できることは別である。**

---

## 9.3 小規模では圧縮し、高Riskでは分離する

### Lightweight例

```text
Intent + Discover + Specify
↓
Execute
↓
Verify
↓
Reinvest
```

### Standard例

```text
Intent
↓
Discover
↓
Shape / Align
↓
Specify
↓
Decompose
↓
Execute
↓
Verify
↓
Reinvest
```

### High Risk / Enterprise例

```text
Intent
↓
Research / Discover
↓
Alignment Gate
↓
Requirement / Architecture Decision
↓
Specification
↓
Decomposition
↓
Planning Gate
↓
Execution
↓
Verification
↓
Acceptance Gate
↓
Release
↓
Reinvestment
```

工程数ではなく、**責務が消えていないこと**を確認する。

---

## 9.4 Evaluation / EvidenceはLifecycle全体を横断するControl Plane

Reviewは最後に一度だけ行う工程ではない。

```text
                 EVALUATION / EVIDENCE
────────────────────────────────────────────
Intent
Discover
Shape / Align
Specify
Decompose
Execute
Verify
Reinvest
────────────────────────────────────────────
```

例：
- Requirement Review
- Alignment Decision
- Architecture Review
- Work Breakdown Review
- Automated Test / Eval
- PR/MR Review
- Acceptance Review
- Release Decision
- Management Review

人間のReview負荷を下げる方法はReviewを消すことではなく、**適切な抽象度・適切な時点へReviewを移すこと**である。

---

## 9.5 実装前の認識合わせを標準責務として持つ

実装前に要求・設計・Domain理解を十分に掘り下げ、未確定事項を実装工程へ持ち込まない。

主な内容：
- Codebaseから回答できる事項を調査する
- Domain Vocabularyを確定する
- 既存のDomain ModelやDocumentとの矛盾を検出する
- Acceptance Criteriaを確認する
- UI / API / DB / 外部IF等を必要に応じて可視化する
- Test Seamを確認する
- 後戻りコストが高いDecisionを明文化する
- 次責務が推測なしで開始できる状態を作る

確定情報はSession内だけに残さずSource of Truthへ反映する。

### 9.5.1 Domain理解は「実装前に受け取る完成資料」ではない

複雑なDomainでは、最初から完全なRequirement / Domain Modelが存在するとは限らない。Domain Expert、Product、Engineer、AIがResearch / Design / Implementation / Feedbackを往復しながら、理解とModelを更新する。

一度ヒアリングして要件を書けば終わり、とはならない。Problem、Domain、Scenario、Acceptanceは、実装やFeedbackで何度も更新される。ここまで含めて、**Shared Realityを育て続けるKnowledge Work**になる。

```text
Domain / Problemを調べる
↓
言葉・Rule・例外を仮説化する
↓
Scenario / Model / Prototype / Codeへ表す
↓
違和感・矛盾・Unknownを発見する
↓
Domain理解を更新する
↺
```

AIはResearch / Comparison / Draft / Model候補の生成を大きく加速できる。ただし、AIの提案を採用するには、Teamが「何が妥当か」を判断できるだけのProblem / Domain理解とEvaluation Criteriaを持つ必要がある。

ここでもHuman-only責務を固定しない。AI CapabilityとEvaluation Reliabilityが上がればDomain分析・Model提案・Consistency Check等も委譲できるが、**何を正とするかを外部化し、Evidenceで更新できる構造**は維持する。

### 9.5.1.1 Why — なぜ実装が速くなるほどDomain理解の価値が上がるのか

最初に、一つだけ言っておきたい。

**AIで速くなったのは、形にすることだ。何を正しいとするかまで、自動的に分かるようになったわけではない。**

架空のFlowDeskでは、依頼は一文から始まる。

> **「承認者が不在のとき、代理の人が承認できるようにしてほしい。」**

短い。実装できそうにも見える。

AIに渡せば、代理承認用の項目を足し、APIを作り、画面に操作を増やし、Testまで書ける。コードを書くことだけを見れば、仕事はかなり前へ進んだように見える。

ところが、この一文にはまだ答えが入っていない。

代理とは一時的な権限なのか。誰が「不在」を決めるのか。高額な申請も代理してよいのか。代理設定が途中で変わったら、すでに流れている申請はどうするのか。監査には、実際にボタンを押した人だけを残せばよいのか。それとも、誰の権限を使ったのかまで残すのか。

コードを書けば、この問いにも答えが出るわけではない。

むしろ怖いのは、AIが止まらずに形にしてしまうことだ。曖昧な要求が、曖昧なままではなく、もっともらしい画面やAPIやData Modelとして固定される。

**曖昧さが消えるのではない。曖昧さに実装という形が付く。**

AI以前の開発にも同じ問題はあった。ただ、実装そのものに時間がかかっていた。設計し、書き、Reviewし、試すまでの途中で、「そもそもこの理解で合っているか」と人が立ち止まる時間が偶然入り込むことがあった。

生成が速くなると、その余白はあてにできない。

では、上流工程を重くして、巨大な仕様書を完成させてからAIへ渡せば安心か。

そうとも限らない。

複雑な仕事では、作ってみて初めて分かることがある。Prototypeを触った利用者が「そういう意味ではない」と気づく。Testを書いて初めて例外が見える。既存Codeを調べたAIが、文書にはなかったRuleを見つけることもある。

実装は、理解の終点ではない。理解を進めるための材料にもなる。

この往復を、Knowledge Loopと呼ぶ。

```text
Problem / Domainを調べる
↓
言葉・Rule・Scenarioを仮説にする
↓
Prototype / Code / Testへ表す
↓
現実とのズレ・例外・Unknownが見つかる
↓
Shared Realityを更新する
↓
Specification / Acceptance / Workを更新する
↺
```

このLoopを、人だけの仕事に固定する必要もない。AIは既存資料とCodeを調べ、用語の候補を整理し、矛盾を探し、Scenarioを増やし、Model案を比較できる。能力と評価の仕組みが上がれば、Domain分析のかなりの部分も任せられる。

ただし、候補を作る能力と、何を採用するかを決められる状態は別である。

100個の案を出せても、何をもって正しいOutcomeとするかが曖昧なら、選べない。だからShared Realityが必要になる。

Shared Realityは、最新の仕様書が一冊あることではない。人とAIが、問題、言葉、Rule、制約、決定、Acceptanceについて、次の仕事を推測だけで始めなくてよい程度に理解を揃えている状態である。Vocabulary、Scenario、Decision Record、Specification、Test、CodeといったContext Assetは、その状態を作り直すために使う。

FlowDeskでも、最初の画面が動いただけでは終わらない。高額申請を代理承認してよいかが未決なら、そのUnknownを見える場所へ置く。Decision Ownerを決める。Riskの低い範囲では先に試す。そして、分かったことを仕様とAcceptanceへ戻す。

全部決めてから作るのでもない。分からないまま作り切るのでもない。

**速く作れるからこそ、理解と実装を短く往復する。**

`Discover → Shape / Visualize → Align → Decide → Specify` は、AIにコードを書かせる前の儀式ではない。仕事の意味を更新し続けるための活動である。実装から新しい事実が返ってきたら、何度でも戻る。

実務で見るべきことは、難しくない。

- 同じ言葉を、関係者とAIが同じ意味で使っているか
- Ruleと例外を分けて説明できるか
- まだ決まっていないことが見えているか
- 何をもって正しいとするかが外へ出ているか
- 作って分かったことを、どこへ戻すか決まっているか

最初の一文へ戻ろう。

「代理の人が承認できるようにしてほしい」。

AIが速ければ、この一文からすぐに機能は作れる。だからこそ、その速さに引っ張られて、一文の意味まで決まった気になってはいけない。

> **AIが実装Costを下げるほど、「何を作るのか」「何を正解とするのか」を更新し続ける能力の価値が上がる。**

### 9.5.2 ContextはAI専用PromptではなくTeam Development Assetである

ここをShared Reality / Context AssetのCanonical Homeとする。以降の章では、この定義を前提として使う。

ここで `Shared Reality` と `Context Asset` を分離する。

- **Shared Reality:** Human / AIがProblem・Domain・Decision・Acceptanceについて十分な共通理解を持つ状態
- **Context Asset:** その状態を作り直し、検証し、別Session / 別Memberへ再利用するために外部化された情報

次をAIへの一時入力だけにしない。

- 仕様
- Domain Vocabulary / 用語
- Business Rule
- Constraint
- Architecture / Design Intent
- Decision / Rationale
- Acceptance Criteria
- Known Unknown

HumanとAIが同じSource of Truthを参照できるようにし、変更時にはReinvest / Learnで更新する。

> **Context整備はAIの回答精度向上だけではなく、Teamの開発判断を共有・再現するための投資である。**

AIがCodingやDraftを高速化しても、Domain理解・Modeling・Knowledge Crunchingの責務は消えない。DeepRailでは、これらを `Knowledge Loop / Shared Reality / Domain Modeling` として、実装速度とは別に維持・更新する。

---

## 9.6 Workflow / Skill Chainの位置づけ

特定のOSS、Skill名、Agent RuntimeをDeepRailの工程名にはしない。
外部の実装例は次の抽象責務へマッピングして利用する。

| 実装パターン | DeepRail上の責務 |
|---|---|
| Interview / research workflow | Discover |
| Mock / prototype generation | Shape / Visualize |
| Spec generation | Specify / Contract |
| Ticket generation | Decompose / Plan |
| Coding agent | Execute |
| Code review / test agent | Verify |
| Documentation / rule feedback | Reinvest / Learn |

外部実装が廃止・変更されても、上位標準が壊れない構造を維持する。


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 29. Loop・Retry・Re-plan・Re-decomposition

**Creator / Lead Author: RIO AMADA**

# 10. 06_開発ループ設計ガイド

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


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 30. Agile・Waterfall・HybridをAI時代に再設計する

**Creator / Lead Author: RIO AMADA**

# 12. 08_開発手法別 AI駆動適用ガイド

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


---

# 36. Agileでの一例

```text
Sprint Planning
↓
Epic / Feature確認
↓
Issue準備
↓
各IssueでHarness実行
↓
Agentが調査・計画
↓
必要ならHuman Gate
↓
Implementation
↓
Test
↓
PR
↓
Review
↓
Merge
↓
Reinvest / Learn
↓
Sprint Review
↓
Harness改善Issue
```

AIによりIssue処理速度が上がる場合、Sprint長を短くすることだけが答えではない。

WIP、レビュー能力、Release能力、要求供給量が新しいボトルネックになる。

---

# 37. Waterfallでの一例

```text
Requirement Phase
├ AI調査
├ Draft作成
└ Human Approval
      ↓
Design Phase
├ AI影響分析
├ Design Draft
└ Formal Gate
      ↓
Implementation
├ Issue分割
├ Agent実装
└ PR/MR
      ↓
Testing
├ Test生成
├ Integration
└ Formal Gate
      ↓
Release
      ↓
Reinvest / Learn
```

AIで成果物作成が高速になっても、工程Gateの存在理由が残る場合は削除しない。

---

# 38. Hybridでの一例

```text
要件/基本設計
→ Formal

実装
→ Agile Issue Loop

Test
→ Continuous + Formal Integration

Release
→ Formal Gate

Document
→ Continuous + Final Consolidation
```

---


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 31. 規模・Risk・Autonomy・Operating Contextで適用を変える

**Creator / Lead Author: RIO AMADA**

# 11. 07_規模判定・Work Item分割ルール

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


---

# 24. 二群のAxisを合成して運用を決める

DeepRail v0.8では、判断軸を「Work Itemの属性」と「Operating Contextの属性」に分離する。

## 24.1 Work Item Axes

```text
Scale
Individual / Small / Medium / Large / Multi-team

Method
Agile / Waterfall / Hybrid

Risk
R1 / R2 / R3 / R4 / R5

Autonomy
A0 / A1 / A2 / A3 / A4 / A5
```

Work Item Axesは主に、工程の重さ、分割粒度、必要Review、基本的なHuman Gate密度を決める。

## 24.2 Operating Context Axes

### OC-1 環境状態成熟度

| 水準 | 定義 | 運用 |
|---|---|---|
| E-0 履歴不明 | 共用環境で過去利用・残留状態が不明 | Environment Preflight必須 |
| E-1 手順あり | Cleanup手順と出自台帳がある | 台帳照合を中心に軽量Preflight |
| E-2 新品保証 | 使い捨て・毎回初期化が保証 | 環境Gateを軽量化可能 |

### OC-2 成果物の一次消費者

`AI / Human / Both`

AI向けは機械照合可能性を、人間向けは説明可能性・Reviewabilityを優先する。
Bothの場合は、機械可読の正本と人間可読Viewを分離する。

### OC-3 Failure Detectability

`Machine-detectable / Human-dependent / Mixed`

Riskが低くても、現時点でHuman判断に依存してしか検出できないFailureにはHuman Gateが必要になる。
Riskが高くても契約・Schema等で機械検出可能なら、Machine Gateを厚くできる。
`Human-dependent` は永久的な能力区分ではない。Model / Tool / Eval / Observabilityが変わればDetectabilityを再評価する。

### OC-4 Human AI Proficiency

| 水準 | 定義 | 運用 |
|---|---|---|
| H-1 初学 | 環境・停止判断・報告に支援が必要 | 自律度を抑え、DoRへ環境準備を含める |
| H-2 運用可 | 標準運用と停止・Escalationが可能 | 標準A1〜A2の適用候補 |
| H-3 判定者級 | 手戻り分類・委任適否・評価関数判断が可能 | Delegation Owner / Evaluator候補 |

## 24.3 合成規則

```text
工程プロファイル = f(Scale, Method, Risk)

Gate強度
= f(Risk, Failure Detectability, Approval Strength)

Environment Gate
= f(Environment State)

Artifact Format
= f(Primary Consumer)

Delegation / Autonomy
= f(Autonomy, Human AI Proficiency, Eval Stability)

Evaluation Authority
= f(Risk, Evidence Reliability, Failure Detectability, Reversibility, Accountability, Calibration Evidence)
```

不変条件はどの組み合わせでも省略しない。

> **Work advances only on approved evidence.**

DeepRailは固定Processを全案件へ強制する標準ではなく、Axisの合成から必要なProcess / Gate / Evidence / Human Involvementを導出する標準である。

---


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 32. SCM・Repository・Work Isolation

**Creator / Lead Author: RIO AMADA**

# 14. 10_SCM・Repository運用ガイド

## 14.1 SCM / Collaboration Adapter共通標準

製品名ではなくGit運用から定義する。

- Branch命名
- Worktree利用
- Commit粒度
- PR/MR粒度
- Reviewer
- Approval
- CI
- Merge方式
- Conflict
- Release Branch
- Protected Branch
- Issueリンク
- Auto Merge条件

---

## 14.2 SCM Adapter

例：

```text
Work Item → Issue / Work Item
Review → Pull Request
Automation → CI/CD Automation
Protection → Branch Protection / Rulesets
```

---

## 14.3 Collaboration Adapter

例：

```text
Work Item → Issue / Work Item
Review → Merge Request
Automation → CI/CD Automation
Protection → Protected Branch
```

---

## 14.4 Branch / Worktree

AI並列開発ではWorktreeを積極的に検討する。

```text
Developer A
└ Issue A
  └ Worktree A
    └ Agent A

Developer B
└ Issue B
  └ Worktree B
    └ Agent B
```

共通ファイルを複数Agentが同時編集する場合は、所有範囲か統合順を決める。

---

## 14.5 PR/MR標準フロー

```text
Issue
↓
Branch / Worktree
↓
Implementation
↓
Self Review
↓
Test
↓
Living Document Check
↓
PR / MR
↓
CI
↓
Independent Review
↓
Approval
↓
Merge
```

---

## 14.6 PR/MR本文の共通項目

```markdown
## Why
なぜこの変更を行うか

## What
何を変更したか

## Impact
影響範囲

## Verification
何を確認したか

## Documents
更新した正本

## Risks
残存リスク・既知制約

## Work Item
関連Epic / Feature / Issue
```

AIにPR/MR本文を生成させる場合も、この構造をHarnessから強制する。

---

## 14.7 AI時代のPR/MR Reviewを4層へ分ける

AI出力を人間が一律に全量Reviewする方式を標準にはしない。

### Layer 1: Deterministic Check

- Build
- Type Check
- Lint
- Unit Test
- Integration Test
- Security Scan
- Policy Check

機械的に判定できるものはCI/Hookへ寄せる。

### Layer 2: AI Standards Review

確認対象：

- Repository規約
- Coding Standards
- Architecture Rule
- 既知のCode Smell
- 不要Scope拡大

### Layer 3: AI Spec Review

確認対象：

- Issue/Specを満たすか
- Acceptance Criteria漏れ
- Scope Creep
- 仕様との差
- Testが仕様を証明しているか

StandardsとSpecは混ぜずに別軸で判定する。

### Layer 4: Human Decision Review

人間は主に次を見る。

- 意図
- Business Decision
- Architecture上の重大判断
- Risk
- Security
- 例外
- Testで証明できない性質
- AIがEscalationした論点

Harness成熟後は、人間のReviewを「全Diffの逐語確認」から「重要DecisionとEvidence確認」へ移行できる領域を増やす。

ただし高Risk変更、Production影響、Security、Data Migration等は別PolicyでHuman Reviewを維持する。

### 14.7.1 Code Reviewを目的から手段へ戻す

DeepRailは「Code Reviewをしないこと」を成熟の証拠にしない。HumanがCodeを見たかどうかもKPIにしない。

先に問うのは、従来Code Reviewで何を検出しようとしていたかである。

| 検出したいもの | Primary Control候補 |
|---|---|
| Requirement / Acceptance不適合 | Spec Eval / Acceptance Test / Traceability |
| Regression | Unit / Integration / E2E / Differential Test |
| Coding Rule違反 | Lint / Static Analysis / Policy Check |
| Security Risk | SAST / DAST / Security Eval / Human Security Decision |
| Architecture逸脱 | Architecture Rule / Independent AI Review / Human Decision |
| Maintainability Risk | Metrics / Smell Detection / Sampling Review |
| Unknown / Low-detectability Risk | Human Deep Review / Experiment / Escalation |

この分解の後に、Human Code Reviewが最良のControlであるWork ClassではCodeを見る。そうでないWork Classでは、Machine / AI EvaluationをPrimaryにしHumanはDecision / Exceptionへ移る。

Review Interfaceは、まず次の順で見る。

```text
Decision / Outcome
↓
Evidence / Risk / Unknowns
↓
High-risk Diff
↓
Raw Diff / Code / Log
```

とする。Raw Artifactは隠さない。ただし**最初に読ませるInterfaceにはしない**。

> **Code Reviewをなくすのではない。Code Reviewによって担保していた品質を、より検証可能なEvidence Systemへ再設計する。**

---

## 14.8 Review Packet

人間が巨大Diffから設計意図を発掘しなくて済むよう、PR/MRにReview Packetを添付する。

```markdown
## Intent
何を成立させる変更か

## Decisions
実装前に確定した主要判断

## Spec Evidence
どのAcceptance Criteriaをどの変更/Testが満たすか

## High-risk Diff
人間に特に見てほしい箇所

## Automated Evidence
Build / Test / CI / Security結果

## Deviations
当初計画から変わった点

## Open Questions
未解決事項
```

Review Packet自体もAI生成可能だが、内容はIssue・Spec・Test・Diffから追跡可能でなければならない。

### Review Packet v2 — 「未検証」と「計画外判断」を隠さない

Review Packetは成功内容だけをまとめない。最低限、次のキーを持つ。

```text
Intent
Decisions
Spec Evidence
High-risk Diff
Automated Evidence
what_untested
Agent-initiated Decisions
Deviations / Rulings
Open Questions
```

`what_untested` は空でもキーを残す。キーが無い状態と「未検証なし」を区別する。

AgentがDesign / Contract確定後に独自判断でScope・Implementation Strategyを変更した場合、`Agent-initiated Decisions`へ記録し、Riskに応じてIndependent Evaluation / Human DecisionへEscalateする。

### 差し戻しは「不合格通知」ではなく次のWork Contractである

```text
Rework Package
├ Failed condition + Evidence
├ Remaining work — 何を積めば合格に届くか
├ causeClass — Failure Routing
└ Re-evaluation scope — 前回不合格 + 新規diff
```

「ダメでした」だけでExecutorへ返さない。Failure Routingによって戻り先を決め、再評価範囲を限定する。

### Review PacketとDecision Packetの関係

Review PacketはDecision PacketのEngineering / PR向けProfileである。

```text
Decision Packet
├ Epic Decision Packet
├ Feature Acceptance Packet
├ Issue Gate Packet
├ PR / MR Review Packet
├ Release Decision Packet
├ Security Decision Packet
└ Transformation Decision Packet
```

正本となるHuman Evaluation Interfaceの原則はDR-M17に置く。

---

## 14.X 集中型VCS・Legacy SCM Adapter

SCM / Collaboration PlatformはDeepRail Coreの必須要件ではない。

集中型VCSを正本とする環境では、次の順で選択する。

```text
1. Native profileでControl Objectiveを満たせるか
2. 不足する場合だけGit Bridgeを置く
3. Bridgeの二重正本Riskが高ければReduced Parallelismへ縮退
```

集中型VCS Adapterは現時点では未検証であり、
「対応済み」とは記述しない。

Validation対象：

- sync drift
- revision ↔ evidence traceability
- reviewability
- parallelism benefit
- bridge operational cost
- rollback
- auditability

成立性が確認されるまで `experimental / unverified` とする。


---

# 54. Worktree戦略

複数Agent並列実行時：

```text
main
├ worktree/issue-A
├ worktree/issue-B
└ worktree/issue-C
```

共有変更が多いIssueは並列化しない。

Worktreeは競合を消すものではなく、作業空間を分離する仕組みである。

---

# 55. Monorepo / Multi-repo

## Monorepo

- path-specific Rule
- package別AGENTS/Instruction
- Owner
- Test範囲
- Agent編集範囲

## Multi-repo

- Cross-repo Work Item
- 変更順序
- Interface Contract
- PR/MR依存
- Release順
- Version整合

大規模Featureでは「1 Issue = 1 Repo」に固定せず、統合Epicから複数Issueへ切る。

---

# 56. CI/CDとの接続

CI/CDはHarnessの後付け連携にしない。AI駆動開発のDelivery Backboneとして先に見る。
Harness設計前に、PipelineとControl Pointを可視化する。

```text
Source / Change
↓
Build
↓
Lint / Static Analysis
↓
Unit Test
↓
Integration / E2E
↓
Security / Compliance
↓
Artifact
↓
Review / Approval
↓
Deploy
↓
Smoke / Production Verification
↓
Monitoring
↓
Rollback / Incident
```

各Stageについて最低限次を定義する。

| Question | 内容 |
|---|---|
| Trigger | 何を契機に動くか |
| Actor | CI / AI / Humanの誰が実行するか |
| Environment | どの環境で実行されるか |
| Evidence | 何を成功証跡とするか |
| Permission | AIが実行・再実行・設定変更できる範囲 |
| Gate | 失敗時に前進を止めるか |
| Retry | 自動Retry可能か |
| Escalation | 誰へ上げるか |
| Traceability | Work Item / Commit / Build / Releaseをどう結ぶか |
| Rollback | 失敗時にどこまで戻せるか |

Harnessへ落とす際は、CI/CDの各Stageを無条件にAgentへ置換しない。
確定的処理はCI / Hook / Scriptへ、判断を要する処理はAgent / Decision Packetへ、Risk受容はHuman Gateへ配置する。

```text
Deterministic Check → CI / Hook / Script
Reasoning          → Agent / Skill
Quality Judgment   → Eval / Reviewer
Business / Risk    → Human Decision
```

AIがCI失敗を修正する場合も、失敗原因をImplementation / Environment / Dependency / Flaky Test等へ分類し、無限Retryを防ぐ。

---


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 33. Legacy / Monorepo / Multi-repoをどう扱うか

**Creator / Lead Author: RIO AMADA**

# Legacy / Brownfield Compatibility Profile

日本企業の既存案件へDeepRailを適用するとき、
Git / PR / Worktree / Cloud環境を当然の前提にしない。

DeepRail Coreで固定するのはToolではなく次である。

```text
Work isolation
Traceability
Reviewability
Approved evidence
Source of Truth
Change history
Rollback / Recovery
Human Gate
Evaluation
```

これらを満たせるなら、実装方式はAdapterで置換できる。

## 集中型VCS（Centralized VCS等）

### Profile A — Native Git

```text
Git
→ Branch / Worktree
→ PR / MR
→ CI / Review
```

DeepRailの標準Reference Profile。

### Profile B — Git Bridge + Centralized VCS Canonical

Legacy環境向けの検討Profile。

```text
Centralized VCS
Canonical Source
      ▲
      │ controlled sync
      │
Local Git Projection
      │
      ├ Agent work branch
      ├ local worktree
      ├ automated checks
      └ review evidence
```

ここで見るのは、

> **Gitを第二の正本にしない。**

Centralized VCSが組織上の正本なら、Local GitはAI作業用の一時Projectionとして宣言する。

同期時には最低限、

```text
centralized revision
↕
Git commit / patch
↕
Work Item
↕
Approval / Evidence
```

の対応を追跡可能にする。

推奨する検査：

- Centralized VCS正本とBridge差分の照合
- 同期漏れ検知
- 未同期Git Commit検知
- Centralized Revision ↔ Work Item対応
- 承認済み版と同期対象の一致
- 二重更新Conflictの検知

**状態:** Hypothesis / 未実地検証。  
集中型VCS Bridgeは、実案件または模擬Evalで成立性を検証してからReference Adapterへ昇格する。

### Profile C — Centralized VCS Native / Reduced Parallelism

Bridgeの維持コストが高い場合は無理にGit化しない。

```text
Centralized VCS Checkout
↓
Isolated Working Directory
↓
AI Session
↓
Patch / Diff
↓
Machine Checks
↓
Review Packet
↓
Human Approval
↓
Centralized VCS Commit
```

Git WorktreeやPRが無い分、

- Agent並列度を下げる
- 作業Directoryを物理分離する
- Diff / PatchをReview Packetへ含める
- Approval Ledgerを外出しする
- Commit前Gateを強める

という縮退Profileを使う。

DeepRailは「最大自律度」を常に狙わない。
現在環境で安全に成立する自律度へ縮退することを正常な適用とみなす。

---

## Git概念とLegacy環境の対応

| DeepRail上の目的 | Git系 | Centralized VCS / Legacy代替 |
|---|---|---|
| Work isolation | Branch / Worktree | Separate checkout / working directory |
| Change unit | Commit | centralized revision / patch set |
| Review | PR / MR | Review Packet / Legacy Work Management ticket / approval record |
| Traceability | Commit / PR link | Revision ↔ Work Item mapping |
| Parallel work | Worktree | Checkout / workspace分離 |
| Gate | CI / protected branch | pre-commit / wrapper / external checker |
| Approval | PR approval | Approval Ledger / workflow state |
| Rollback | revert commit | reverse merge / revision restore |
| Source of Truth | Git remote | centralized repository |

Tool機能をそのまま模倣するのではなく、
**そのToolが担っていたControl Objectiveを別手段で満たす。**

---

## 日本企業Legacy Operating Context

現場で繰り返し現れるEnvironment Differenceは、

```text
CRLF
cp932
日本語Path
Windows
Proxy / PAC
社内Network
残留試験資材
Mirror freshness
```

のような条件だった。

Legacy Trackでは、VCSだけを見ても足りない。Operating Context全体を適用判定に入れる。

### Environment

- Windows first-class support
- PowerShell / cmd / shell差
- CRLF
- cp932 / UTF-8
- Japanese username / path
- symlink restrictions
- package registry / proxy
- offline install
- certificate / enterprise CA

### Network

- PAC
- HTTP proxy
- closed network
- no direct external API
- internal mirror
- restricted MCP / SaaS

### Work Management

- Legacy Work Management
- Work Management Server / Data Center
- Excel台帳
- approval workflow
- ticket number based traceability

### Development Method

- Waterfall
- phase gate
- formal artifacts
- document approval
- long release cycle
- multi-vendor responsibility boundaries

DeepRailはこれらを「例外」として端へ追いやらず、
**Operating ContextによるProfile選択**として扱う。

---


---

## 14.X 集中型VCS・Legacy SCM Adapter

SCM / Collaboration PlatformはDeepRail Coreの必須要件ではない。

集中型VCSを正本とする環境では、次の順で選択する。

```text
1. Native profileでControl Objectiveを満たせるか
2. 不足する場合だけGit Bridgeを置く
3. Bridgeの二重正本Riskが高ければReduced Parallelismへ縮退
```

集中型VCS Adapterは現時点では未検証であり、
「対応済み」とは記述しない。

Validation対象：

- sync drift
- revision ↔ evidence traceability
- reviewability
- parallelism benefit
- bridge operational cost
- rollback
- auditability

成立性が確認されるまで `experimental / unverified` とする。


---

# 55. Monorepo / Multi-repo

## Monorepo

- path-specific Rule
- package別AGENTS/Instruction
- Owner
- Test範囲
- Agent編集範囲

## Multi-repo

- Cross-repo Work Item
- 変更順序
- Interface Contract
- PR/MR依存
- Release順
- Version整合

大規模Featureでは「1 Issue = 1 Repo」に固定せず、統合Epicから複数Issueへ切る。

---


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 34. CI/CDはAI駆動開発の背骨である

**Creator / Lead Author: RIO AMADA**

# 56. CI/CDとの接続

CI/CDはHarnessの後付け連携にしない。AI駆動開発のDelivery Backboneとして先に見る。
Harness設計前に、PipelineとControl Pointを可視化する。

```text
Source / Change
↓
Build
↓
Lint / Static Analysis
↓
Unit Test
↓
Integration / E2E
↓
Security / Compliance
↓
Artifact
↓
Review / Approval
↓
Deploy
↓
Smoke / Production Verification
↓
Monitoring
↓
Rollback / Incident
```

各Stageについて最低限次を定義する。

| Question | 内容 |
|---|---|
| Trigger | 何を契機に動くか |
| Actor | CI / AI / Humanの誰が実行するか |
| Environment | どの環境で実行されるか |
| Evidence | 何を成功証跡とするか |
| Permission | AIが実行・再実行・設定変更できる範囲 |
| Gate | 失敗時に前進を止めるか |
| Retry | 自動Retry可能か |
| Escalation | 誰へ上げるか |
| Traceability | Work Item / Commit / Build / Releaseをどう結ぶか |
| Rollback | 失敗時にどこまで戻せるか |

Harnessへ落とす際は、CI/CDの各Stageを無条件にAgentへ置換しない。
確定的処理はCI / Hook / Scriptへ、判断を要する処理はAgent / Decision Packetへ、Risk受容はHuman Gateへ配置する。

```text
Deterministic Check → CI / Hook / Script
Reasoning          → Agent / Skill
Quality Judgment   → Eval / Reviewer
Business / Risk    → Human Decision
```

AIがCI失敗を修正する場合も、失敗原因をImplementation / Environment / Dependency / Flaky Test等へ分類し、無限Retryを防ぐ。

---


---

# 22. 18_Release・Production運用ガイド

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


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 35. Test・Eval・Quality Gateをどこへ置くか

**Creator / Lead Author: RIO AMADA**

# 21. 17_品質評価・Harness Evalsガイド

## 21.-1 Trust Architecture — 「AIを信頼する」を分解する

DeepRailの信頼機構は次の4層で考える。

```text
1. Principle
   何を信じるか
   → Executor Self-reportではなくEvidence

2. Evaluation Design
   どう判定するか
   → Acceptance / Evidence Level / Independent Evaluation / EA

3. Enforcement
   誰が止めるか
   → CI / Hook / Checker / Permission / Human Gate

4. Meta-Health
   その仕組み自体が生きているか
   → fixture / doctor / audit / telemetry health
```

> **AIを信用するのではない。評価機構と、その評価機構が正常に動いていることをEvidenceで信用する。**

## 21.0 証跡規律

「実行主体の自己申告」と「完了証跡」は分ける。

| 等級 | 名称 | 内容 | 扱い |
|---|---|---|---|
| EV-3 | 実挙動証跡 | 実環境ログ、read-back、スクリーンショット、録画、観測結果 | ユーザー可視変更の主要な完了根拠 |
| EV-2 | 機械検査証跡 | lint、typecheck、UT、CI、coverage、schema/checker通過 | 補助証跡。単独で実挙動を保証しない |
| EV-1 | 自己申告 | 「実装した」「テストは通った」等 | 証跡ではない。速報・参考情報 |

次を完了根拠として受理しない。

- 実行件数が0件のgreen summary
- mockだけを実環境証跡として扱うこと
- skipされたTestを合格へ算入すること
- エラー状態を含むcaptureを成功証跡にすること
- AI自身の「完了しました」という報告だけで前進すること

評価者は可能な範囲で再実行・再観測し、生成Contextと評価Contextを分離する。

## 21.0-A 成熟度別の評価関数

すべての組織に同じKPIを適用しない。

```text
M0 Exploration
→ 学習量、課題抽出、Failure分類、未知の発見

M1 Controlled Adoption
→ 再現性、標準遵守、Human Intervention、再試行

M2 Standardization
→ Flow Metrics、Enforcement Coverage、Quality、Rework

M3 Scaled Adoption
→ Multi-team Lead Time、Review Capacity、運用コスト、Risk

M4 Continuous Optimization
→ Business Outcome、Portfolio最適化、Capability改善
```

計測できない値を推測で埋めない。未計測は `null` とし、必要な計測基盤の整備そのものを成熟度昇格条件にできる。

## 21.1 Harnessにもテストを持つ

コード変更にRegression Testがあるのと同様に、Harness変更にも標準課題を持つ。

---

## 21.2 評価指標

- Task Success Rate
- Build Success
- Test Success
- Review指摘数
- Rule違反
- Human Intervention
- Retry回数
- Lead Time
- Human Time
- Token
- Cost
- Reinvest / Learn漏れ
- Security Violation
- PR/MR手戻り
- Reopen率

さらに、Harness単体ではなくSDLC全体のFlowを評価する。

### 工程別Flow Metrics

- Requirement Lead Time
- Design Lead Time
- Build Lead Time
- Review Lead Time
- Test Lead Time
- Release Lead Time
- Maintain/Incident Resolution Time
- Queue Time
- WIP
- Blocked Time
- Human Wait Time
- External Dependency Wait Time

### Reviewability Metrics

- Review Time / PR
- Human Review Minutes
- PR/MR当たりの変更量
- Humanが確認すべきHigh-risk Diff量
- Review Queue Length
- Review Rework率
- Spec Surprise数
- 未合意Decision発見数
- Review時のRequirement再確認回数
- HumanがCodeから意図を逆算した回数
- Review Packet欠落率

Build時間が短縮してもReview Queueが増えている場合、Harness全体としては改善したとは断定しない。

レビュー工程で「なぜこの設計なのか」を初めて議論している場合、上流のGrill/Specプロセス不足としてFailure Classificationする。

---

## 21.3 Harness効果の比較

例：

| 条件 | Quality | Time | Token | Human |
|---|---:|---:|---:|---:|
| High Model + Harnessなし | 測定 | 測定 | 測定 | 測定 |
| High Model + Harnessあり | 測定 | 測定 | 測定 | 測定 |
| Light Model + Harnessあり | 測定 | 測定 | 測定 | 測定 |

「軽量モデルでも動く」は実験で確認する。

---

## 21.4 Harness変更Gate

```text
Harness Change
↓
Eval Suite
↓
Baseline比較
↓
品質低下?
├ Yes → Reject / Fix
└ No  → Review
        ↓
       Merge
```

---

## 21.X Human Evaluation Interface

ここをHuman Review / Evidence InterfaceのCanonical Homeとする。前段では「Review Queueが詰まる」という症状までを扱い、ここで初めて判断のInterfaceを本格的に設計する。

AIが人間へ判断を要求するとき、Raw Artifactをそのまま渡してはいけない。

Human Gateへ判断材料を渡す形式を **Human Evaluation Interface** と呼ぶ。

基本原則：

> **AIは人間に成果物を渡すのではなく、判断を渡す。**

人間判断を求める場合、AIは最低限次を提示する。

```text
Decision
Recommendation
Reason
Options
Evidence
Risk
Unknown
Reversibility
Requested Action
```

### Human Attention Principle

Human Attentionは有限の組織資源である。

AI成果物の品質には、Correctness / Security / Maintainability等だけでなく、
**Human Reviewability** を含める。

人間が短時間で、

```text
何を決めればよいか
なぜ決める必要があるか
AIは何を推奨するか
何が証明済みか
何が未確認か
Riskは何か
戻せるか
```

を判断できない場合、Human Evaluation Interfaceの品質が低いとみなす。

### 21.X.0.1 Why — なぜHuman Reviewが新しいBottleneckになり得るのか

AIで実装は速くなった。

それでも、開発全体は思ったほど速くならない。

こういうことは起こり得る。理由は単純で、**最後に人が全部読む設計が、そのまま残っているからだ。**

FlowDeskの代理承認を考える。Frontend、Backend、権限判定、監査Log、Test。仕事を独立した単位へ分けられれば、AIは複数の変更を並行して進められる。以前より短い時間で、Review待ちの成果物が並ぶ。

ここまでは狙い通りである。

問題は、その次だ。

人間のReviewerが一つずつDiffを開く。変更理由をIssueから探す。仕様を読み直す。Test結果を見る。権限への影響を考える。別の変更との組み合わせを頭の中で再現する。分からなければAgentへ聞く。

一つなら読める。

複数が同時に来ると、急に重くなる。

AI側の実行能力は増えたのに、最後の評価方法だけが「人がRaw Artifactを最初から読み直す」のままだと、制約はReview側へ移る。AIが遅いのではない。**速くなった工程の次に、詰まる場所が移っただけである。**

ここで、Reviewを減らすことだけを目標にすると危ない。

人が見ること自体が悪いわけではない。問題は、何を見るかが毎回Reviewerの頭の中で決まっていることだ。

Securityに関わる変更、Data Migration、後戻りしにくいArchitecture変更、検出しづらいFailure。こうした仕事では、CodeやDiffを人が直接読む意味は残る。Human Reviewをゼロにすることが目標ではない。

それでも、すべての変更で同じ深さの確認を要求する必要はない。

たとえばFlowDeskで、「代理承認時に元のApprover IDがAudit Logへ残ること」を確認したいとする。人が巨大なDiffから探し始めるより、Acceptance、実行したVerification、実際のLog、残っているUnknownを先に見た方が判断は速い。必要なら、そこからCodeへ降りればいい。

順番を変える。

```text
Raw Artifactを全部読む
↓
頭の中で意図とRiskを再構成する
↓
判断する
```

ではなく、

```text
何を判断するかを見る
↓
Evidenceで確かめる
↓
Risk / Unknownを見る
↓
必要なところだけRaw Artifactへ降りる
```

へ変える。

この順番を支えるのがHuman Evaluation Interfaceである。Decision PacketやReview Packetは情報を隠すものではない。人のAttentionを、判断が必要な場所へ先に向ける。

AIが大量に作る時代ほど、この差は大きくなる。

実装者が一人増えれば、Review側も同じように増やせばいい、という話ではない。ReviewerにはDomain理解、Architecture、Security、Production事情のような希少なContextが必要なことがある。人数だけ増やしても、同じ判断能力をすぐ複製できるとは限らない。

人を増やすだけで解けないなら、Reviewの仕事そのものを組み直すしかない。

- Machine Checkで先に落とせるものは何か
- AIの一次評価をShadowでCalibrationできるか
- Work Classごとに必要なEvidenceは何か
- どのFailureは人間が直接見るべきか
- どこはSamplingへ移せるか
- どのDecisionはまだHuman Gateへ残すべきか

ここまで揃って、ようやくAIの速度をDelivery全体で受け止められる。

そして、Reviewの仕事そのものも変わっていく。

最初はArtifactを見る。次にDecisionとEvidenceを見る。さらに評価系が成熟すれば、Exceptionや高Risk Decisionを見る。最後には、個々の変更より、Evaluation FunctionやRisk PolicyそのものをReviewする比重が上がる。

人のReviewは、すぐには消えない。

先に変わるのは、**何を見るか**だ。

FlowDeskのSceneへ戻る。複数の成果物がReview待ちで並んでいる。ここで必要なのは、人間を急がせることではない。すべてを読む仕事を、すべて読まなくても判断できる仕事へ作り直すことだ。

> **人が全部見る仕組みは、人の速度を超えられない。AI Native化で変えるべきなのは、生成速度だけではなく、最後に人が何を見てGOを出すかである。**

### 21.X.0.2 Why — なぜEvidenceをInterfaceとして扱うのか

AIが「終わりました」と言った。

この一言には、ほとんど情報がない。

Codeはあるかもしれない。Testも通っているかもしれない。だが、判断する側が本当に知りたいのは「何を作ったか」だけではない。**この変更を次へ進めてよいと、何を根拠に言えるのか**である。

FlowDeskの代理承認を例にする。Agentが実装を終え、Pull Requestを作った。変更は1,200行ある。人間がDiffを全部読めば、実装内容はある程度分かる。

それでも、読んだだけでは答えにくい問いが残る。代理期間を過ぎたUserは本当に拒否されるのか。高額申請ではCompliance Approverを飛ばさないか。Audit Logには元ApproverとProxy Approverの両方が残るか。既存Clientとの互換性は保たれているか。

CodeはArtifactである。判断には、もう一段別の形がいる。

そこで、Evidenceを判断の入口にする。

EvidenceをInterfaceと呼ぶのには理由がある。最後に付ける添付資料では足りない。次のDecisionをする側が、そのまま判断に使える形で検証結果を渡したい。

```text
Intent / Acceptance
↓
Verification
↓
Observed Result
↓
Evidence
↓
Decision
```

たとえば「期限切れの代理者は承認できない」というAcceptanceなら、欲しいのはAgentの説明ではない。期限切れ条件で実際に操作し、拒否された結果、その時のLog、使ったEnvironment、未確認条件である。

この形なら、人間だけでなく別のAI Evaluatorも読める。次工程のGateも使える。後日のAuditでもたどれる。再実行可能なら、条件が変わった後に確かめ直せる。

Codeを読む価値は残る。ArchitectureやSecurity、Maintainabilityのように、Raw Artifactそのものを見るべき判断もある。必要なときは、そこまで降りればいい。

ただ、すべてのDecisionを「Codeを全部読んだ人の頭の中」で成立させると、その判断は再利用しにくい。何を確認し、なぜOKとしたのかが、Reviewer個人へ閉じるからだ。

EvidenceをInterfaceにすると、判断の材料が外へ出る。

```text
「読んだ感じ大丈夫」ではなく

何を確かめたか
何が観測されたか
何がまだ分からないか
どのRiskが残るか
```

を共有できる。

Evidenceが弱ければ、Decision Rightsを広げない。Evidenceが十分に強く、Failureを検出でき、再現可能なら、一部の判断をAI Evaluationへ移せる。

Evidenceを最後のDocumentationに回すと遅い。仕事を任せたあと、その成果を信じて次へ進むまでの途中に置く。

> **Codeは成果物である。Evidenceは、その成果物を次へ進めてよいか判断するためのInterfaceである。**

FlowDeskで1,200行のDiffができても、最初に見るべきものが1,200行とは限らない。最初に見るべきなのは、「代理承認は正しく成立した」と言える根拠である。

---

## 21.X.1 Decision Packet

Review PacketをPR/MR専用の成果物として閉じず、
Human Decision全般へ一般化したものを **Decision Packet** とする。

```markdown
# Decision Packet

## 1. Decision Required
今回、人間に決めてほしいこと

## 2. Recommendation
AIの推奨案

## 3. Why Human Decision Is Required
なぜ委譲範囲を超えるのか

## 4. Outcome Impact
この判断がOutcomeへどう影響するか

## 5. Options
選択肢
- Option A
- Option B
- Option C

## 6. Evidence
EV-3 Observed Behavior
EV-2 Machine Check
その他の根拠

## 7. Risk
Risk Class / Failure Mode / Blast Radius

## 8. Unknowns
未確認事項・不確実性

## 9. Reversibility
Rollback可能性 / Cost / Time

## 10. Requested Action
Approve / Reject / Request Change / Defer / Escalate
```

AIは「確認お願いします」だけをHumanへ投げない。

### 21.X.1.1 Delegation Decision Trail

長時間・多Phase・無人実行では、最終Decision Packetだけでなく、重要な判断の経路を追跡可能にする。
Humanが全文Transcriptを読むことを前提にしない。

Decision Trailは最低限次を持つ。

```text
ts / phase
Decision
Rationale
Evidence Pointer
Result
Deviation / Pivot
Unknown / Open Risk
```

原則：

1. **重要な判断点だけを記録する** — 全Tool Callや全思考過程を記録しない。
2. **EvidenceはPointerを優先する** — Commit / Test Result / Trace / Screenshot / Artifact等へ辿れるようにする。
3. **Append-onlyを基本とする** — 判断変更は過去を書き換えず、Supersede / Revertとして新しいEntryを追加する。
4. **Resultを残す** — `accepted / reverted / inconclusive / open` 等、判断後に何が起きたかを記録する。
5. **Handoff時に圧縮する** — HumanへはOutcome / Important Decisions / Evidence / Deviations / UnknownsをDecision Packetへ要約する。

```text
Autonomous Execution
↓
Decision Trail
↓
Outcome + Evidence + Important Decisions
↓
Decision Packet / Review Packet
↓
Human / Policy Decision
```

Decision Trailは監視のための逐語ログではなく、**後から「なぜこのOutcomeになったか」を再構成するためのAudit / Review Interface**である。

---

## 21.X.2 Progressive Disclosure

人間への提示は、

```text
Level 0
Decisionだけ

↓ Drill-down

Level 1
Summary
Intent / Recommendation / Risk / Evidence / Unknown

↓ Drill-down

Level 2
Evidence
Acceptance Criteria / Test / Decision / Traceability

↓ Drill-down

Level 3
Raw Artifact
Spec / Design / Diff / Code / Log / Trace
```

の順を基本とする。

最初から巨大DiffやRaw Logを読ませない。
必要な人だけ深掘りできる状態を作る。

この順序は情報を隠すためではない。Humanがまず「承認すべき判断」を理解し、その判断に必要なEvidenceだけを追跡し、必要な場合にCodeまで降りられるようにするためである。

**Code / DiffはLevel 3の重要なRaw Evidenceであり得るが、Human Reviewの既定入口ではない。**

---

## 21.X.3 Work Level別のManagement View

同じ情報を全Roleへ見せない。

| Work Level | 人間が主に評価するもの |
|---|---|
| Portfolio | Investment / Strategic Fit / Outcome / Risk |
| Epic | Outcome / Scope / Owner / Dependency / Risk |
| Feature | Capability / Acceptance / Boundary |
| Issue | Intent / Acceptance / Evidence / Exception |
| PR / MR | Decision / High-risk Diff / Automated Evidence |
| Release | Release Scope / Residual Risk / Rollback |
| Transformation | Constraint / Approval / Adoption / Outcome |

AIは受け手のRoleとDecision Rightsに応じてViewを変える。

---

## 21.X.4 Evaluation Maturity

人間の評価対象は成熟度とAutonomyによって変える。

```text
Stage 1
Human reviews Artifact

Stage 2
Human reviews Decision + Evidence

Stage 3
AI evaluates Artifact
Human reviews Exception / High-risk Decision

Stage 4
Human defines Evaluation Function
AI executes + evaluates + retries

Stage 5
Human reviews
Outcome / Risk / Investment / Exception
```

最終状態でもHuman Reviewはゼロにならない。

Reviewの抽象度が上がる。

なお、成熟度を「HumanがCodeを見なくなった割合」で測らない。評価するのは、対象Work Classについて必要なFailure Modeが検出可能で、Approved Evidenceが成立し、Riskに応じたDecision Rightsを安全に委譲できているかである。

---

## 21.X.5 Evaluation Authority — AI評価にどこまでGO権限を与えるか

Human / AIの評価分担を「人間30%・AI70%」のような割合で設計しない。
評価権限は**Work Class / Decision Classごと**に定義する。

Evaluation Authorityは `EA0〜EA4` で表す。

| Level | 名称 | AIの評価権限 | Humanの関与 |
|---|---|---|---|
| EA0 | Human Evaluation | AI評価をGate根拠にしない | Humanが評価・GO |
| EA1 | Shadow Evaluation | AIも並行評価するがGO権限なし | Humanが全件判断。差分をCalibrationに使う |
| EA2 | AI-First / Human Decision | AI評価を一次評価として採用 | HumanはDecision Packet / Evidenceから最終GO |
| EA3 | Audited Autonomy | 定義済みWork ClassではAIが評価・GO可能 | HumanはException / Sampling / Audit |
| EA4 | Policy-Governed Autonomy | Policy内でAIが評価・GO・Retryまで実施 | HumanはEvaluation Function / Risk Appetite / Policy / Exceptionを管理 |

`EA`はAIのExecution Autonomy `A0〜A5`とも、Approval Strength `S1〜S5`とも別軸である。

```text
A  = 何をAIが実行できるか
EA = 何をAIが評価し、GO判断できるか
S  = 承認をどの強度・形式で成立させるか
```

例：

```text
A3 × EA1 × S4
Feature内の実行はAIが進める
AI評価はShadowとして記録
最終GOは人間が非同期台帳で承認

A3 × EA3 × S1
Feature内の実行・評価を定義済み範囲でAIへ委譲
人間はSampling / Exceptionを監査
委任規程に基づきAIが承認記録
```

AIが高性能であること自体はEA昇格条件ではない。
対象Work Classで、必要なEvidence・Failure検知・Rollback・Auditが成立していることを要求する。

---

## 21.X.6 Evaluation Delegationの導入手順

AI評価への信頼は、説明やデモではなく**比較実績**から作る。

### Step 0: Work ClassとEvaluation Contractを固定する

```text
対象Work Class
Acceptance Criteria
Evaluation Criteria
Required Evidence
Risk Class
Failure Detectability
Reversibility
Accountability Owner
```

「AI全般を信用できるか」ではなく、対象を狭くする。

### Step 1: Shadow Evaluation

HumanとAIが独立に同じ対象を評価する。AIの判定はまだGateへ効かせない。

```text
AI  : GO / NG / UNKNOWN + Evidence
Human: GO / NG / UNKNOWN + Reason
```

### Step 2: Disagreementを分類する

単純にHumanを正解と固定しない。

```text
AI Error
Human Error
Ambiguous Criteria
Missing Evidence
Environment Mismatch
Requirement / Spec Drift
Unknown / Unclassifiable
```

人間同士の判断揺れもCalibration対象とする。

### Step 3: Calibration Evidenceを蓄積する

最低限、次を観測する。

```text
True Accept
True Reject
False Accept   # AIがGOしたが本来NG。最重要
False Reject
Unknown Rate
Human Override Rate
Missing Evidence Rate
Escaped Defect
Rollback / Incident
```

全領域共通の昇格閾値は規定しない。Risk AppetiteとWork Classに応じて組織がExit Criteriaを定義する。

### Step 4: Bounded Delegation

十分なEvidenceが得られた**限定Work Classだけ**EAを上げる。

```text
EA1 → EA2
AIが一次評価
HumanはDecision / Evidence中心に確認

EA2 → EA3
AIが通常GO
HumanはException / Sampling / Auditへ移行
```

### Step 5: Audit / Drift Monitoring

委譲後も固定しない。

- Model変更
- Prompt / Context / Harness変更
- Test変更
- Environment変更
- Domain変更
- Failure Pattern変化

があれば再Calibrationする。

### Step 6: Expand or Roll Back

品質が維持できれば隣接Work Classへ展開する。
False Accept、重大Incident、Evidence欠落、Eval Driftが増えた場合はEAを戻す。

> **Evaluation Authorityは成熟度バッジではなく、対象領域ごとに上げ下げする運用Profileである。**

---

## 21.X.7 Independent Evaluation Contract

Evaluation Authorityを上げる前に、評価系統そのものを設計する。

### Generation / Evaluation Separation

実装した主体の自己評価だけでEAを上げない。

```text
Executor
  ↓ Artifact + minimal provenance
Evaluator: Standards axis
Evaluator: Specification axis
  ↓
Independent Evidence
```

推奨原則：

1. **fresh context** — 実装時の長い会話履歴をそのまま評価へ渡さない。
2. **axis separation** — StandardsとSpecificationを別軸で評価する。
3. **AND semantics** — 一方の合格で他方の不合格を相殺しない。
4. **positive context list** — 評価系に渡す案件固有ContextをGLOSSARY / ADR / Contract等の正本へ限定する。
5. **disagreement escalation** — 独立Evaluator間の不一致を多数決だけで閉じず、Unknown / Human Decision候補にする。

### Failure-Mode Independence / Evaluator Diversity

Evaluator Independenceは「別Agent」「別Model」「別Prompt」という形式だけでは判定しない。
同じ誤ったSpecification、同じContext Gap、同じModel Family、同じ観測不能点を共有していれば、複数Evaluatorが同じ誤判定をする可能性がある。

独立性は次の観点で確認する。

```text
Evaluation Axis Diversity
→ Specification / Standards / Security / Runtime / UX / Policy

Evidence Source Diversity
→ Test / Static Analysis / Runtime Observation / Trace / External Source

Context Independence
→ Executorの会話履歴・自己説明へ過度依存しない

Model / Method Diversity
→ 必要な場合のみ異なるModel / Algorithm / Human Judgmentを組み合わせる

Failure Correlation
→ 同じFailure Modeを同時に見逃す可能性を評価する
```

```text
複数Evaluatorが一致
→ High-signal候補
→ Truthとは限らない

Evaluatorが不一致
→ Criteria / Context / Unknown / Environmentを再確認
→ 必要ならHuman / Domain Decision
```

多数決はIndependent Evaluationの代替ではない。
目的はEvaluator数を増やすことではなく、**重要なFailureを同時に見逃す相関を下げること**である。

低RiskでDeterministic Checkが十分なWork Classでは多系統評価を省略してよい。独立性のコスト自体もRiskで調整する。

## 21.X.8 Evaluator Re-execution Principle

合否の根拠は、可能な範囲で**判定者自身が再実行・再取得した観測**にする。

```text
根拠にできる
→ Evaluator自身のtest / query / read-back / observation

参考情報
→ Executorの説明
→ Executorが貼ったログ
→ Executorの「テスト済み」自己申告
```

Write系操作はread-backを完了条件へ含める。破壊的・不可逆な操作は再実行せず、read-back / immutable log / environment evidenceへ置き換える。

### 21.X.8.1 Reproducible Evidence Principle

Evidence StrengthとReproducibilityを混同しない。
EV-3のObserved Behaviorでも、一度しか再現できない場合がある。一方で、低RiskなMachine Checkは容易に再実行できる。

可能な範囲で、Evidenceには次を紐づける。

```text
What was verified
Verification Procedure
Input / Preconditions
Environment / Version / Provenance
Observed Result
Evidence Location
Cleanup / Side Effect
Re-run Constraint
```

Verification Procedureは、実際のUser Path / Runtime Behavior / External Effectを検証できる場合、それをProxyだけで置き換えない。
生成したVerification Script / Skill / Checker自体も、少なくとも一度は実行して成立を確認する。

```text
Executor Self Report
→ 弱い根拠

Snapshot / Log / Screenshot
→ 観測Evidence

Re-runnable Test / Checker / Script / Eval
→ 再確認可能なEvidence

CI / Hook / Gateへ統合済み
→ 継続的に再評価されるEvidence System
```

ただし、Machine Re-executionを万能視しない。Domain Judgment / Security Exception / Legal / Irreversible Operation等ではHuman DecisionやImmutable Evidenceを残し、Work Classに応じて最適なEvidence Contractを選ぶ。

## 21.X.9 Evaluator Permission Isolation

評価主体は、可能な限りTool面でRead-onlyにする。

```text
Evaluator
Read   ✓
Test   ✓（非破壊）
Write  ✗
Merge  ✗
Release ✗
```

Promptへ「変更しないで」と書くだけの場合、強制済みとはみなさずEnforcement Ledgerで `declared_only` とする。

自動修正が必要なら、EvaluatorとFixerを別系統へ分ける。

## 21.X.10 Human Gateの品質

Human Gateの成功条件は、

```text
人間が画面を開いた
人間がApproveを押した
```

ではない。

次を満たしたかで評価する。

```text
Decision対象が明確
必要Evidenceが揃っている
Riskが開示されている
Unknownが隠されていない
代替案が比較可能
人間がDecision Rightsを持つ
判断がTraceable
```

Approvalが形だけ残っているなら、Gateがあるとは数えない。Failureとして見る。

---


---

# 39. Harness Evalsの標準課題例

## E1. 小規模UI変更
- 期待差分
- 不要変更がない
- Test成功
- Document不要判定が正しい

## E2. API変更
- Contract変更検知
- Frontend影響検知
- Test追加
- API正本更新

## E3. DB Migration
- Migration作成
- Rollback考慮
- Data影響
- Security
- Document更新

## E4. Bug Investigation
- Root Cause
- Reproduction
- Fix
- Regression Test

## E5. Ambiguous Requirement
- 勝手に仕様確定せずEscalationできるか

## E6. Malicious/Unsafe Instruction
- 権限外操作を拒否/停止できるか

---


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 36. Environment State / Provenanceをどう管理するか

**Creator / Lead Author: RIO AMADA**

# DR-M20. 20_環境・実行基盤 状態管理ガイド

**レイヤ:** Execution Harness / Operating Context  
**目的:** 使用中の実行環境を「時間方向に状態を持つ資源」として管理し、環境由来Failureを開発Failureへ誤分類しない。

## M20.1 対象

対象は次を含む。

- Local Development Environment
- Test / Integration Environment
- Ephemeral Environment
- Container / VM / Pod
- Worktree / Port / Lane resource
- Mirror / Cache
- Generated fixture / residual resource

初期SetupそのものはDR-M04、Production運用はDR-M18を正本とする。
M20は、その中間にある**使用中の環境状態**を扱う。

## M20.2 Environment Lifecycle

```text
Allocate
↓
Initialize
↓
Use
↓
Observe
↓
Contamination Check
↓
Cleanup / Recreate
↓
Release / Return
```

各段階でOwnerとEvidenceを定義する。

## M20.3 Environment State

OC-1として次を使う。

```text
E-0: History Unknown
E-1: Managed / Cleanup Procedure Exists
E-2: Fresh / Disposable Guaranteed
```

E-0ではTest開始前のEnvironment Preflightを必須とする。
E-2では環境状態Gateを軽量化できる。

## M20.4 Environment Preflight

最低限確認する。

- Version / generation
- residual data / resource
- required service health
- dependency reachability
- cache / mirror freshness
- required credentials presence
- expected configuration
- port / resource collision
- workspace / worktree identity

Preflight失敗は、実装差し戻しへ入れる前にEnvironment OwnerへEscalateする。

## M20.5 Environment Provenance

共有環境では、可能な範囲で次を追跡する。

```text
environment_id
owner
allocated_at
work_item
generation
last_cleanup
known_residuals
freshness
last_verified_at
```

環境の状態を「人間の記憶」に置かない。

## M20.6 Lane

並列実行時のLaneを、

```text
Human
× Work Item
× Environment
× Resource
```

の組で管理する。

Agent数だけを増やしても、Environment / Review / Human Gateの供給能力が不足すればThroughputは上がらない。

## M20.6-A Lane / Lease — EnvironmentをExecution Capacityとして管理する

Shared Environmentや排他Resourceがある場合、Environmentは「存在するか」ではなく「いつ、誰が、どのWork Itemで占有しているか」で管理する。

```text
lane_id
├ Human / Agent Session
├ Work Item
├ Environment
├ Worktree / Workspace
├ Port / Exclusive Resource
├ acquired_at
├ lease_expiry
└ release_status
```

lease失効は放置しない。失効した占有はEnvironment Debtとして可視化し、次の実行主体が「空いていると思って壊す」状態を防ぐ。

### Supply Lead Time

環境払い出しに外部承認・閉域申請・アカウント発行等が必要なら、DoRより前のExternal Dependencyとして管理する。AI実装が速くてもEnvironment Supplyが数日なら、そこがFlowの制約になる。

## M20.7 Environment Failure

Environment FailureはImplementation Retryへ流し続けない。

```text
Failure
↓ cause routing
Environment State / Availability / Encoding / Network / Shared Resource
↓
Environment / Platform Owner
```

Soloでは本人が終端Ownerでよいが、工程内Failureとして無限Retryしない。

環境起因と判断したFailureは、Code修正Loopへ無制限に戻さない。

```text
Failure
↓
Reproduce on fresh/known environment?
├ Yes → Product / Implementation investigation
└ No  → Environment State Failure
          ↓
       Environment Owner
```

---


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 37. Release・Production・Rollback・Observability

**Creator / Lead Author: RIO AMADA**

# 22. 18_Release・Production運用ガイド

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


---

# 57. Observability

Harness自体を観測する。

ログ候補：

- Agent開始/終了
- Tool Error
- Retry
- Human Intervention
- Test結果
- Eval結果
- Cost
- Model
- Duration
- Work Item
- Failure Category

---


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 38. 成果と学習を次のAIへ戻す

**Creator / Lead Author: RIO AMADA**

# 18. 14_生きたドキュメント・知識管理ガイド

## 18.1 Living Documentの定義

Living Documentとは、履歴ではなく「現在の正しい状態」を示す正本。

---

## 18.2 Change Logとの違い

```text
Change Log
→ 過去に何が変わったか

Living Document
→ 今どうなっているか
```

両方必要な場合は分離する。

---

## 18.3 Source of Truth

各情報にOwnerを持たせる。

### Artifact Consumer Contract

成果物は「誰が一次消費者か」を宣言する。

```text
AI-first
→ machine-checkable / stable ID / fixed vocabulary / partial-read safe

Human-first
→ reviewable / visual / decision-oriented / explainable

Both
→ machine-readable Canonical Source + human-readable View
```

Bothの場合、人間向けViewは正本の意味を変更してはならない。並べ替え・要約・可視化は許すが、内容変更は正本側で行う。正本の書き手（Human / AI / Shared）も明示する。

| 情報 | 正本例 |
|---|---|
| UIデザイン | Figma |
| API Contract | API仕様書 |
| DB Schema | Schema + DB設計 |
| Work Status | Work Management System/Issue |
| Source | Git |
| Architecture Decision | ADR/Design Doc |
| AI開発ルール | Harness Documents |

---

## 18.4 Reinvest / Learnの完了条件

```text
Codeと正本が一致
Test結果反映済み
関連ADR更新済み
必要なAgent/Skill改善済み
次のAgentが参照可能
リンク切れなし
旧仕様が正本として残っていない
```

---

## 18.4.1 Structural Reinvestment — 学びを構造へ還元する

Reinvest / Learnでは、学びを「注意事項の追加」だけで閉じない。
再発性のあるFailure / Human Correction / Useful Patternは、次の順で最も再現性の高いControlへ寄せる。

```text
一度きりの判断
→ Decision Record / Context Asset

繰り返す知識不足
→ Living Document / Rule / Skill

機械判定できるFailure
→ Test / Checker / Hook / CI Gate

継続観測が必要
→ Eval / Monitoring / Meta-Health

権限・Risk問題
→ Permission / Delegation Contract / Human Gate
```

「同じことを次回も人間が思い出して注意する」は、可能なら最終形にしない。
ただし、全てをAutomationへ変換することも目的化しない。暗黙知・Context依存・Human Judgmentが本質のものは、Decision Interface / Training / Samplingとして残してよい。

完了判定は、**次回のExecutionまたはEvaluationが実際に変わったことをEvidenceで確認できるか**まで含める。

### 18.4.1.1 Why — なぜ学習をStructureへ埋め込む必要があるのか

「次から気をつけよう」は、学習したように聞こえる。

けれど、次の実行が同じなら、仕組みは何も学んでいない。

FlowDeskの代理承認で、Agentが監査Logへ元ApproverのIDを残し忘れたとする。Reviewで人が気づき、修正した。Retroでは「代理承認では元承認者を必ず記録する」と議事録へ書いた。

ここで終わると、次のSessionではまた同じことが起こり得る。別のAgentはその議事録を読まないかもしれない。別Teamは存在すら知らないかもしれない。人間も数か月後には忘れる。

知識は残った。Behaviorは変わっていない。

DeepRailがReinvestmentを重く見るのは、この差があるからだ。

学びには種類がある。すべてをAutomationにすればよいわけではない。Business JudgmentのようにContext依存が強いものはDecision RecordやTrainingへ残す方がよい。一方、「このFieldが必ずAudit Logへ入っていなければならない」のように機械判定できるものは、TestやCheckerへ落とせる。

```text
知った
↓
分類する
↓
次回の実行を変える最も強い場所へ置く

Knowledge → Context / Document
Procedure → Skill / Workflow
Deterministic Rule → Test / Checker / Hook
Risk Boundary → Permission / Gate
Evaluation Gap → Eval / Evidence Contract
```

ここまでやると、失敗は一回分の損失だけではなくなる。次回から同じFailureを安く防げる資産へ変わる。

反対に、毎回Humanが同じ指摘をしているなら、それは人が丁寧なのではなく、Systemが学習を人の記憶へ外注している可能性がある。

もちろん、StructureにもCostはある。Ruleを増やしすぎればContextは重くなる。Gateを増やせばFlowは遅くなる。Checkerが誤判定すれば、別のFailureを作る。だから、再発頻度、Risk、Detectability、Maintenance Costを見て置き場所を選ぶ。

そして、埋め込んだ後も終わりではない。Testが本当にFailureを捕まえるか。Ruleが参照されているか。Gateが形骸化していないか。古い前提を固定していないか。Structure自体も評価し、不要になれば弱めるか消す。

FlowDeskの監査Log問題なら、Regression Testを追加し、Verification ProcedureへAudit Evidenceを含め、別Teamが代理Decisionを作るときにも再利用できる形へする。次に同じ種類の仕事が来たとき、人が思い出す前に仕組みが働く。

> **組織が学んだかどうかは、文章が増えたかではなく、次のExecutionが変わったかで判断する。**

学習をStructureへ埋め込むのは、知識を固めるためではない。人間の記憶に依存せず、次の仕事へ効かせるためである。

## 18.5 人間の「ツッコミ」をSession内で消費しない

AI Agentへ修正を返すこと自体は避けられない。

同じ指摘を次のSessionでも、その次でも繰り返しているなら、そこで一度止まった方がいい。

```text
AIが誤る
↓
人間がChatで修正
↓
そのSessionでは直る
↓
Session終了
↓
次回また同じ誤り
```

この繰り返しは、個人の注意不足よりHarness側のFailureとして見る。

繰り返すFeedbackは、次のいずれかへ還元する。

```text
認識不足
→ Living Document

恒常制約
→ Rule / Instruction

繰り返す作業方法
→ Skill

専門判断
→ Agent

機械判定可能
→ Hook / CI / Test

品質劣化を検知したい
→ Eval Case
```

Feedback Flow：

```text
Human Correction
↓
一時修正か再発性ありか判定
↓
再発性あり
↓
Harness Assetへ変換
↓
Eval追加
↓
次Sessionから自動適用
```

Reinvest / Learnではコードの正本化だけでなく、**今回人間が行った修正のうち、次回以降も有効な知識をHarnessへ還元できないか**を確認する。

---


---

# 59. Harness Backlog

Harness改善も通常開発と同様にBacklog管理する。

```text
Harness Epic
├ Context改善
├ Skill改善
├ Agent改善
├ Eval追加
├ Tool Adapter
└ Documentation
```

---

# 60. Definition of Ready / Done

## AI Issue Ready

- 目的が明確
- Scopeが定義
- 正本リンクあり
- Acceptance Criteriaあり
- 必要権限が利用可能
- 依存Issue明記
- Risk判定済み

## AI Issue Done

- Acceptance Criteria達成
- Test成功
- Review完了
- PR/MR処理
- Reinvest / Learn完了
- Harness改善要否判定
- Traceability確保

---


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 39. AI開発はなぜHarness Engineeringへ進んだのか

**Creator / Lead Author: RIO AMADA**

# 6. 02_ハーネス設計原則

## 6.0 Harness Engineeringはなぜ生まれたのか

Harness Engineeringは、ある日突然発明された一つのTool技法ではない。
AIへ任せる仕事が広がるたび、Promptの外にある問題を一つずつ解いてきた。その積み重ねを追う方が、今の形を理解しやすい。

これは厳密な「唯一の公式年表」ではなく、公開された製品史・技術記事と実務上の設計変化をつなぐ**DeepRailの技術史モデル**である。

### 6.0.1 第1段階 — Prompt Engineering：AIの出力を整える

初期の主な関心は、AIへどう依頼すれば望ましい回答・コードを得られるかだった。

```text
Human
  ↓
Prompt / Instruction / Example / Output Format
  ↓
Model
  ↓
Output
```

ここでの中心問いは、**「どう言えば、より良い出力になるか」**である。
Prompt Engineeringは現在も必要だが、AIが複数Stepを実行するWorkerになると、Promptだけでは設計対象が足りない。

### 6.0.2 第2段階 — Persistent Rules / Repository Context：毎回同じことを言わない

AI IDEが実務へ入ると、利用者は自然に次を求める。

- このRepositoryでは毎回この規約を守ってほしい
- このProjectの構造・Domainを毎回説明したくない
- このFile / Directoryではこの前提を常に使ってほしい
- 同じ注意を毎Session繰り返したくない

```text
毎回Promptで説明
        ↓
Persistent Rule / Repository Context
        ↓
Project固有の挙動を継続的にSteer
```

製品名より、ここで起きた変化を見たい。
**毎回Promptで言い直すのではなく、環境の側に前提を残したくなった。** その要求が、設計対象を少し外へ広げた。

### 6.0.3 第3段階 — Context Engineering：AIの認識状態を設計する

Agentが長い仕事を扱うと、単にInstructionを書くより、**その瞬間に何を知った状態で推論させるか**が重要になる。

違いは、こう考えると分かりやすい。

```text
Prompt Engineering
「どう言うか」

Context Engineering
「何を知った状態で働かせるか」
```

Contextの候補には、Requirement、Code、Architecture、Domain Knowledge、Decision、Environment State、Tool Description、History等がある。
**Contextを多く入れることではなく、正しい情報を正しい時点で必要十分に渡すこと**が目的である。

### 6.0.4 第4段階 — Coding Agent：AIが答える存在から動く存在へ

AIがFileを読み書きし、Terminalを実行し、Testし、Retryするようになると、利用者の問いは変わる。

```text
何を答えさせるか
        ↓
どこまで行動させるか
何を禁止するか
何を自動確認するか
失敗時にどこへ戻すか
いつHumanへEscalateするか
```

この段階で、Rule / Contextだけではなく、**Tool、Permission、Feedback、Retry、Gate**が必要になる。

### 6.0.5 第5段階 — Harness Engineering：GuardrailとEnablementをExecution Systemへ統合する

Harness Engineeringは、AIを単に縛る技術ではない。
実務では二つの欲求が同時に発生する。

```text
CONTROL / GUARDRAIL
├ 禁止事項
├ Permission
├ Hook / Gate
├ CI
├ Human Approval
└ Audit / Evidence

ENABLEMENT
├ Context
├ Source of Truth
├ Skill
├ Tool / MCP
├ Environment
├ Memory / Artifact
├ Retry / Recovery
└ Evaluation / Feedback
```

DeepRailでの定義：

> **Harness Engineeringとは、AIが仕事を安全かつ再現可能に完遂できるよう、Prompt / Contextだけでなく、Tool・Permission・SCM・CI/CD・Environment・Gate・Eval・Evidence・Recovery・Human Decision・Learningまで含む実行系を設計するEngineeringである。**

### 6.0.6 「発明」より、自然発生に近い

名前が定着する前から、現場では似た対策が生まれていた。

同じ注意を何度もするならRuleにしたくなる。危険な操作が怖ければPermissionを絞りたくなる。「できました」だけでは不安なら、TestやEvidenceが欲しくなる。

ここでは、その流れが偶然ではないことだけ押さえる。**仕事を任せて困った場所に、必要な仕組みが生まれる。**

次のWhyでは、FlowDeskを使って、その自然発生を一つの仕事の中で追う。教育で同じ流れをどう体験させるかは人材育成章へ回す。

### 6.0.6.1 Why — なぜHarness Engineeringは自然発生するのか

最初からHarnessの完成形を作ろうとしなくていい。

むしろ多くの場合、先に仕事を任せる。すると困る。困ったところに仕組みが生まれる。

FlowDeskの代理承認を、最初は一つのAgentへそのまま任せたとする。「この要求を実装して、Testまで通して」と依頼する。AgentはRepositoryを読み、Codeを書き、Testも追加する。小さな変更なら、これだけで終わるかもしれない。

ところが仕事を少し広げると、同じやり方では苦しくなる。

「代理」の意味を毎回説明する。監査LogのRuleを毎回説明する。触ってはいけないProduction Dataを毎回注意する。Testが落ちるたびに人が原因を教える。Agentが「できました」と言うたびに、人が別の手段で確かめる。Sessionが変わると、前回の注意が消える。

このあたりから、現場は名前を知らなくても対策を足し始める。

```text
同じ説明を繰り返したくない
→ Rule / Context

必要なSourceを迷わず読ませたい
→ Source of Truth / Retrieval

危険な操作を止めたい
→ Permission / Hook

「できました」だけでは判断できない
→ Test / Evidence / Eval

失敗するたび人が直したくない
→ Feedback / Retry / Recovery

同じFailureを次回も繰り返したくない
→ Reinvestment
```

これらを一つずつ足していくと、いつの間にか「AIへ仕事を成立させる実行環境」ができている。

Harnessは、最初から完成図を描いて作る特殊な装置とは限らない。仕事を任せる範囲が広がるたび、足りない条件が見え、その穴を埋めていった結果として現れることが多い。

だから、Toolから始めると順番を間違えやすい。最初にAgent FrameworkやSkill一覧を決めても、何のFailureを防ぎ、何の仕事を成立させるための仕組みなのかが分からなければ、部品だけが増える。

逆に、仕事から始めれば必要性が見える。

FlowDeskで代理承認を安全に任せたい。では、どの情報が必要か。どこまで操作してよいか。何をもって正しいとするか。失敗したらどこへ戻すか。人に聞くべき判断は何か。次回へ何を残すか。

この問いに一つずつ答えると、Context、Permission、Verification、Gate、Decision、Learningがつながる。

HarnessをDelivery Systemから逆算する理由もここにある。作りたいのは見栄えのするAI機能ではない。**仕事が最後まで成立する条件**だ。

AIへ任せる範囲が狭ければ、Harnessも小さい。任せる範囲が広がれば、設計対象も外へ広がる。

> **委譲を本気で進めると、仕事を成立させる仕組みが必要になる。その仕組みを偶然の工夫で終わらせず、再現可能にしたものがHarness Engineeringである。**

### 6.0.7 設計対象が外側へ広がる

技術の流れを見ると、前の考え方が消えるというより、その外側へ設計対象が広がっている。

```text
Prompt Engineering
AIへの指示を設計する
        ↓
Context Engineering
AIの認識状態を設計する
        ↓
Harness Engineering
AIの行動・環境・検証・回復を設計する
        ↓
Operating Model / Organization Engineering
Human + AIの役割・権限・意思決定・学習を設計する
```

Prompt EngineeringもContext Engineeringも消えない。
**Harness Engineeringの内部で重要な設計領域として残る。**

また、Harness Engineeringを組織へ一般化する際は、Softwareの機械的Gateを人間へそのまま写像するのではなく、成立条件を検証して抽象化する。

### 6.0.8 強いOrganizationと強いHarnessの構造的な類似

強い会社は、優秀な個人だけで成立しない。Purpose・Principle・Role・Authority・Process・Evaluation・Learningを下位の行動へ落とし込むことで、個人の判断を揃え、再現性と自律性を高める。

Harnessでも同じ問題が現れる。

| Organization | Harness / AI Execution System |
|---|---|
| Purpose / Mission | Intent / Objective |
| Values / Principles | Instructions / Rules |
| Organizational Knowledge | Context / Source of Truth |
| Role | Agent / Function |
| Authority | Permission |
| Business Process | Workflow / Skill |
| Approval / Internal Control | Gate / Human Decision |
| Performance / Quality Evaluation | Eval / Evidence |
| Audit / Monitoring | Observability / Trace |
| Training / Organizational Learning | Reinvestment / Rule / Skill Update |

この類似は、AIを人間と同一視するためではない。
**複数の実行主体を目的に沿って自律的かつ再現可能に動かすとき、必要になる設計問題が似る**ことを示している。

### 6.0.8.1 Why — なぜOrganizationとHarnessには似た構造が現れるのか

会社とAI Harnessを同じものとして語るつもりはない。

人には感情があり、関係があり、法的責任があり、組織には文化や権力もある。Agentを社員に見立てれば組織設計が分かる、という単純な比喩をDeepRailは採らない。

それでも、設計図を並べると似たものが出てくる。目的。役割。権限。仕事の流れ。判断基準。例外処理。評価。監査。学習。

似て見える理由は、人間とAIが似ているからではない。**複数の実行主体へ仕事を任せ、中央が一件ずつ指示しなくても全体を目的へ向かわせたい。** その問題が共通している。

小さな会社では、社長が細部まで判断しても回る。社長自身がContextであり、Gateであり、Evaluatorだからだ。人数が増えると、それでは止まる。何を目指すかを共有し、誰が何を決めてよいかを決め、定型業務はProcessへ落とし、重大な例外だけ上げる。

AI Executionでも同じことが起きる。Agentが一つで、人間が横に座って全部見ている間は、Promptと会話だけでも回る。Agentが増え、仕事が長くなり、複数RepositoryやEnvironmentをまたぎ始めると、人が全Stepを直接統制できなくなる。

そこで必要になるのが、Intent、Context、Role、Permission、Workflow、Gate、Evidence、Escalation、Reinvestmentである。

これは「AIを社員として扱え」という話ではない。

> **人が逐次介入しなくても、複数の実行主体が目的に沿って動けるようにすると、組織とHarnessは同じ種類の設計問題へ近づく。**

この見方を持つと、Harnessを単なるDeveloper Toolingとして扱えなくなる。Production操作をAgentへ許す問題は、Tool Permissionだけでは終わらない。誰の方針を根拠に、どのRisk Classまで、どのEvidenceがあれば、その判断を下位へ委譲できるかというDecision Rightsの問題になる。

反対に、Organization側も「AI Toolを導入する」という言い方だけでは足りない。StrategyがどこでWorkへ変わり、何がAIへ渡り、何をEvidenceとして上位判断へ返すのか。そこまで設計しなければ、経営のIntentとAIのExecutionはつながらない。

FlowDeskでも同じだった。代理承認を実装するAgentへ必要なのはCode Conventionだけではない。誰に代理承認を許すのか、監査上何を残すのか、どの例外を人へ戻すのか。その上位RuleがExecutionまで届かなければ、技術的に正しいCodeでもBusinessとしては間違える。

強いHarnessは、AIを賢く見せる仕組みではない。強いOrganizationも、優秀な人を集めただけの状態ではない。どちらも、**目的を下位の行動へ届け、行動のEvidenceを上位の学習へ戻す構造**を持つ。

Harness Engineeringを深く追うと、Organizationの話へ戻ってくる。話を無理に広げたというより、AIへ任せる仕事が広がった結果、最初からつながっていた問題が見えてくる。

### 6.0.9 経営の意思をAI実行まで接続する

AIが高い抽象度の仕事を担うほど、Coding Ruleだけでは足りなくなる。

```text
Coding Standard
↓
Engineering Principle
↓
Product Principle
↓
Risk Appetite
↓
Business Priority
↓
Decision Policy
↓
Strategy / Purpose
```

これらをすべてPromptへ詰め込むのではない。
各層のSource of TruthとDecision Rightsを明確にし、必要なIntentが下位Executionへ伝わり、下位Evidenceが上位Decisionへ戻る構造を作る。

```text
Purpose / Strategy
↓
Objective / Portfolio Decision
↓
Operating Model / Decision Policy
↓
Work Contract / Harness
↓
AI / Human Execution
↓
Evidence / Outcome / Failure
↑
Management Review / Organizational Learning
↑
Strategy Update
```

ここまで到達すると、Harness Engineeringは単なるDeveloper Toolingではなく、**Organization Engineeringを実行可能にする下位レイヤ**になる。

---


---

## v0.13.0 追加編集方針 — Harnessの歴史を「学習の順序」へ変換する

v0.13.0では、Harness Engineeringの歴史を単なる背景説明で終わらせず、**人材育成・ハッカソン・Pilotの学習設計そのものへ接続する**。

AIを使い込んだ人が自然に身につけるのは、Promptの技巧だけではない。
実際の仕事を任せる過程で、同じ指示の反復、Context不足、勝手な変更、完成自己申告への不安、Regression、Permission、Environment差、要求変更といった摩擦にぶつかり、次の順で仕組みを作り始める。

```text
AIを使う
↓
大きめの仕事を任せる
↓
Frictionが発生する
↓
Rule / Context / Test / Permission / Gateが必要になる
↓
AI自身にEvaluation / Retryを任せる
↓
Harnessとして体系化する
↓
Evidenceを根拠にDecision Rightsを委譲する
↓
HumanはObjective / Policy / Risk / Exceptionへ集中する
```

これはHarness Engineeringが実務で自然発生してきた順序と同型である。
教育でも、最初から完成形のHarnessを暗記させるだけにはしない。

> **Harness Engineeringが歴史的に自然発生したのであれば、教育でもその自然発生を意図的に再現する。**

そのため、AI未経験〜初級者には、ある程度複雑で変更が入り、Frontend / Backend / DB / Test / CI等を横断する**一人称のEnd-to-End開発経験**を推奨する。
目的は完成アプリの数ではなく、次の認識変化を起こすことである。

```text
AIを使う
↓
AIへ仕事を任せる
↓
AIへ評価も任せる
↓
任せられる条件を設計する
↓
Human Gateを一つ外して成功する
↓
「全部を自分で確認しなくても成果は成立する」と体感する
↓
Delegation / Harness / Organizationの意味を理解する
```

### v0.13.0 中心命題3 — AI教育の核心は「委譲の成功体験」である

DeepRailは、AI Literacyを二段階に分ける。

```text
AI Usage Literacy
AIへ適切に依頼し、Context / Toolを使い、出力を扱う能力

        ↓

AI Delegation Literacy
Objective / Responsibility / Permission / Acceptance / Evidence / Evaluation / Escalationを設計し、
Humanが逐次介入しなくてもAIが仕事を完遂できる状態を作る能力
```

AIを十分に使ったことがない人と、日常的にAgentへ仕事を任せている人の認識差は、操作知識だけではない。
後者は経験を通じて、**「全部を人間が確認すること」ではなく「任せられる仕組みを作ること」が安全性とScaleを生む**と理解している。

教育ではこの認識差を説明だけで埋めようとせず、実際にDelegation Envelopeを広げる経験で埋める。

```text
開始時
Human Decision Surface = 大
AI Delegation Envelope = 小

        ↓ Evidence / Harness / Calibration

終了時
Human Decision Surface = 必要な例外へ縮小
AI Delegation Envelope = 安全に拡大
```

Human Checkpoint削減を目的化してはならない。
学習者は、Gateを外すたびに次を説明できなければならない。

- 何をAIへ委譲したか
- なぜ委譲可能と判断したか
- 何をAcceptance / Evidenceとしたか
- Failureをどう検知できるか
- 間違えた場合に戻せるか
- どの条件ならHumanへEscalateするか

この経験によって、Human Gate削減は「AIを信用したから」ではなく、**Decision Rightsを安全条件付きで委譲した結果**として理解される。

---

## v0.14.1 追加編集方針 — 思想をOperational Mechanicsへ接続する

v0.14.1では、ここまでの対話で確立したHuman-AI Boundary / Delegation / Evaluation Authority / Harness History / Education Philosophyを正本思想として維持したまま、旧来の実務標準から**現場で壊れずに回すためのOperational Mechanics**を再統合する。

統合方針は次のとおり。

```text
WHY / WHAT（v0.13までに強化）
Human-AI Boundary
Delegation
Evaluation Authority
Organization Engineering
Harness History
Experiential Learning
        +
HOW / CONTROL（v0.14で強化）
Trust Architecture
Independent Evaluation
Enforcement Lifecycle
Gate Coverage
Guard the Guards
Failure Routing
Delegation Contract
Maturity Evidence
Environment Lane / Lease
Artifact Consumer Contract
        ↓
DeepRail v0.14
思想と実行機構を分離せず接続する
```

### v0.14.1 中心命題4 — 「書いてある」と「効いている」を分ける

標準・Rule・Policy・Gateは、文書に存在するだけでは統制にならない。

> **Declared is not Enforced. Enforced is not Healthy. Healthy is not Effective.**

信頼機構は3層に分ける。

```text
Layer 1 — Trust Principle
何を信じるか
自己申告ではなくEvidenceを信頼する

Layer 2 — Trust Design
どう信じられる状態を作るか
Evidence / Independent Evaluation / Permission / Human Gate / Evaluation Authority

Layer 3 — Enforcement & Meta-Health
誰が実際に止め、守る仕組みが生きているか
Hook / CI / Checker / Enforcement Ledger / Guard the Guards / Meta-Health
```

> **Hookは警備員であって、警備計画そのものではない。**

### v0.14.1 中心命題5 — Failure分類の目的は「名前を付けること」ではなく「次の一手を決めること」

Failure Taxonomyを、日常のRoutingと、週次・組織学習用のAnalyticsに分離する。

```text
Failure
↓
Routing Class
→ 今どこへ返すかを一往復で決める
↓
必要に応じてDetailed Failure Taxonomy
→ 統計 / Harness投資 / 組織学習へ使う
```

### v0.14.1 中心命題6 — Decision Rightsの委譲は契約とEvidenceで広げる

ここで覚えておくのは一つだけでいい。Human Gateの数を減らすこと自体は目的ではない。

実行できる範囲 `A`、評価してよい範囲 `EA`、承認の強さ `S` は別に管理する。どの判断を任せるかはScope / Evidence / Expiry / Auditと一緒に決める。

> **信頼可能に判断できる最も実行に近い主体へ、条件付きでDecision Rightsを移す。**

詳細な委譲手順は `23.2-A Decision Rights Delegation Protocol` を正本とし、他の章では定義を繰り返さず、適用するScaleを広げる。


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 40. 優れたHarnessはどう設計するか

**Creator / Lead Author: RIO AMADA**

## 6.1 Harness設計はDelivery Systemの理解から始める

Harness設計は runtime固有のInstruction File、Prompt、Agent Persona、Skill一覧から始めない。

最初に、**そのチームの変更がどのように作られ、検証され、承認され、本番へ届き、失敗時に戻されるか**を描く。

```text
Demand / Requirement
↓
Specification
↓
Work Item
↓
Source Change
↓
Build
↓
Static Check
↓
Unit / Integration / E2E
↓
Security / Compliance Check
↓
Artifact
↓
Review / Approval
↓
Deploy
↓
Production Verification
↓
Monitoring
↓
Rollback / Incident
↓
Learning
```

このFlowを理解せずにHarnessを設計すると、AIに「何をさせるか」は書けても、次を設計できない。

- どの地点でAIを止めるか
- どの検証を機械へ任せるか
- 何をEvidenceとして次へ進めるか
- どの権限をどのAgentへ渡せるか
- どこでHuman Decisionが必要か
- Environment FailureとImplementation Failureをどう分離するか
- Release / Rollbackをどこまで自律化できるか
- 失敗をRule / Skill / Evalへどう戻すか

**CI/CDはHarnessの後ろに付ける連携先ではない。Harnessを設計する前に見るDelivery Backboneである。**

---

## 6.2 設計時に最初に確認する14項目

| 項目 | 問い |
|---|---|
| Outcome | 何を成立させるためのHarnessか |
| Development Lifecycle | 要求からLearningまで、どの責務・Gateで進むか |
| SCM / Work Isolation | 変更単位と並列作業単位は何か |
| CI/CD | Build / Test / Package / Deployはどこで、何を契機に動くか |
| Test / Eval | 何を機械で検証でき、何を人間が判断するか |
| Environment | Local / Shared / CI / Staging / Productionの状態をどう識別するか |
| Release / Rollback | 本番化と復旧の条件は何か |
| Work Unit | Epic / Feature / Issue / Agent Task / PR等の単位は何か |
| Source of Truth | 要求・仕様・Code・Decisionの正本は何か |
| Human Gate | 人間判断が必要なのはどこか |
| Agent Boundary | AIに任せる範囲と禁止範囲はどこか |
| Evidence | 前進・完了を何で証明するか |
| External Tool | Issue / Chat / Docs / Cloud等とどう連携するか |
| Runtime / Model | どのAgent Runtime / Modelを使い、差し替え可能か |

---

## 6.3 Control Point Mapを作る

Delivery Flowの各地点について、次を記録する。

```text
Control Point
├ Trigger
├ Actor: Human / AI / Machine
├ Input
├ Allowed Action
├ Required Evidence
├ Pass Condition
├ Failure Route
├ Escalation Owner
├ Permission Boundary
└ Traceability Target
```

例：

| Control Point | Actor | Evidence | Fail時 | Harness実装候補 |
|---|---|---|---|---|
| Before Implementation | AI + Human as needed | Spec / Acceptance / Decision | Align / Specifyへ戻る | Skill / Decision Packet |
| Pre-commit | Machine / AI | Lint / unit test | Agent retry | Hook |
| PR/MR | AI + Human | Review Packet / CI result | Rework / Decision | Review Skill / Gate |
| Integration | CI | Integration result / env provenance | Environment or Code route | CI Gate / Env checker |
| Release | Human / Policy | Release Decision Packet | Defer / Fix | Approval Gate |
| Production | CD + Runtime | Deployment / smoke / monitoring | Rollback / Incident | Tool / Runbook / Agent |

**HarnessはこのControl Point Mapを実行可能にする。**

---

## 6.4 「Map, not Encyclopedia」

Harnessの入口ファイルに全情報を書かない。

推奨する思想は次。

```text
短い入口
├── 現在のDevelopment / Delivery Flowへのリンク
├── 正本ドキュメントへのリンク
├── Build/Test/CIコマンド
├── Environment識別方法
├── 禁止事項・Permission Boundary
└── 必要時に呼ぶSkill/Agent
```

深い内容は必要になった時点で読み込む。

これにより、

- 不要Contextの常時投入を避ける
- ルールの責務を分離する
- 更新箇所を特定しやすくする
- CI/CDやEnvironmentの事実とPrompt上の思い込みを分離する
- AI Runtimeを差し替えやすくする

という効果を狙う。

---

## 6.5 Harnessは「足場」であり、Model能力とともに変える

Harnessの各構成要素は、暗黙的に「Modelだけではできないこと」への仮定を持つ。
その仮定はModelの進化により古くなるため、Harnessを複雑化したまま固定しない。

原則：

1. Delivery上必要なControl Objectiveを先に固定する。
2. そのControl Objectiveを満たす最小のHarnessを採用する。
3. Rule / Skill / Agent / Hookを追加した理由を記録する。
4. Model更新時は、追加した足場がまだ必要かEvalする。
5. 削除してもOutcome / Evidence / Safetyが維持できるなら単純化する。


---

## 6.6 Harness成熟度

Harnessそのものにも成熟度を持たせる。

| Level | 状態 |
|---|---|
| H0 | 個人Prompt中心 |
| H1 | 共通Instructionsあり |
| H2 | Rule/Skill/Agentが役割分離 |
| H3 | SCM / CI/CD / External Tool / Quality Gateと接続 |
| H4 | Evalsにより変更を評価 |
| H5 | Issue/Feature単位の自律実行 |
| H6 | 複数Agent・複数Work Itemを統合管理し、Deliveryまで証跡連携 |

Harness成熟度とAI自律化レベルは同じではない。
Harnessが高度でも、高リスク業務ではHuman Gateを残す。


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 41. Context Engineering

**Creator / Lead Author: RIO AMADA**

# 16. 12_AI実行基盤・モデル選定ガイド

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


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 42. Rule・Skill・Agent・Hookをどう構成するか

**Creator / Lead Author: RIO AMADA**

# 7. 03_ハーネス構成・利用ガイド

## 7.1 AI資産の責務

概念上、次を区別する。

| 資産 | 用途 |
|---|---|
| Instruction / Rule | 継続適用する制約 |
| Skill | 繰り返す手順・ワークフロー |
| Agent | 専門責務を持つ実行主体 |
| Hook | 特定イベントで確定的に実行する処理 |
| Tool | Agentが行動する能力 |
| MCP | 外部システムをToolとして接続する境界 |
| Prompt | 一時的・特定用途の依頼 |
| Living Document | 現在状態の正本Context |
| Eval | Harness/Agentの挙動を確認する試験 |

---

## 7.2 配置判断

```text
毎回守る制約か？
→ Rule / Instruction

繰り返す手順か？
→ Skill

専門性・独立Contextが必要か？
→ Agent

必ず実行したい処理か？
→ Hook / CI

外部情報・外部操作が必要か？
→ Tool / MCP

現在仕様を説明する情報か？
→ Living Document
```

---


---

# 30. 子ハーネスの提案フォルダ

名称はプロジェクトへ合わせて変更する。

```text
開発ハーネス/
└── workspace/
    └── 開発ドキュメント/
        ├── _doc-harness/
        │   ├── agents/
        │   ├── skills/
        │   ├── rules/
        │   ├── templates/
        │   ├── evals/
        │   └── README.md
        │
        ├── 01_基本方針・Harness設計/
        │   ├── 01_AI駆動開発基本方針.md
        │   ├── 02_Harness設計原則.md
        │   ├── 03_Harness構成利用ガイド.md
        │   └── 04_環境構築セットアップ.md
        │
        ├── 02_開発プロセス/
        │   ├── 05_AI_Native_Development_Lifecycle.md
        │   ├── 06_開発ループ設計.md
        │   ├── 07_規模判定WorkItem分割.md
        │   ├── 08_開発手法別AI駆動適用.md
        │   └── 09_チーム役割運用.md
        │
        ├── 03_Tool_AI_Runtime/
        │   ├── 10_SCMRepository運用.md
        │   ├── 11_外部Tool連携.md
        │   └── 12_AI実行基盤Model選定.md
        │
        ├── 04_Lifecycle_教育/
        │   ├── 13_AI資産Harness変更管理.md
        │   ├── 14_LivingDocument知識管理.md
        │   └── 15_習熟教育Hackathon.md
        │
        └── 05_Governance_Quality_Production/
            ├── 16_SecurityAIガバナンス.md
            ├── 17_HarnessEvals.md
            ├── 18_ReleaseProduction.md
            └── 19_AI権限委譲自律化.md
```

---

# 31. 子ハーネスに置くAgent候補

```text
document-architect
standard-writer
consistency-reviewer
source-of-truth-reviewer
workflow-designer
harness-reviewer
security-reviewer
eval-designer
tool-adapter-writer
living-document-reviewer
```

Agent数は最初から増やしすぎない。

責務が重複する場合は統合する。

---

# 32. 子ハーネスに置くSkill候補

```text
/create-manual
/update-manual
/review-manual
/check-cross-links
/check-terminology
/design-work-item-policy
/design-harness-structure
/design-hackathon
/run-harness-eval
/update-living-docs
/generate-pr-description
```

名称は利用Runtimeへ合わせる。

---


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 43. Model・Tool・Runtime・Permissionをどう接続するか

**Creator / Lead Author: RIO AMADA**

# 16. 12_AI実行基盤・モデル選定ガイド

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


---

# 48. AI Runtime差し替え

Harness構造は次の二層に分ける。

```text
Vendor Neutral Core
├ Process
├ Documents
├ Evals
├ Policy
└ Templates

Runtime Adapter
├ Coding Agent Runtime
├ Coding Agent Runtime
└ Coding Agent
```

共通正本をRuntime別ファイルへコピーし続けるのではなく、可能な範囲で参照関係を作る。

---

# 49. トークン削減を狙う設計パターン

保証ではなく設計上の仮説として扱う。

1. Always-on情報を短くする
2. 深い情報は必要時のみ取得
3. Code Mapを持つ
4. Build/Testコマンドを明記
5. 既知の探索方法をSkill化
6. Subagentで探索Contextを分離
7. Tool結果を構造化
8. 長い会話履歴ではなく正本へ戻す
9. Reinvest / Learnで次回探索を減らす
10. Evalsで軽量Model利用可能領域を特定

---

# 50. 「しょぼいモデルでも動く」を標準用語へ変換する

文書内では次のように定義する。

> **Harnessによる手順制約、必要Contextの明示、Tool境界、機械的Quality Gate、再利用可能なSkillが十分に整備された定型領域では、より低コスト・低レイテンシのモデルでも要求品質を満たせる可能性がある。採用可否はHarness Evalにより確認する。**

これなら組織文書でも利用できる。

---


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 44. Harnessをどう評価し、壊さず進化させるか

**Creator / Lead Author: RIO AMADA**

# 17. 13_AI資産・Harness変更管理ガイド

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


---

# 21. 17_品質評価・Harness Evalsガイド

## 21.-1 Trust Architecture — 「AIを信頼する」を分解する

DeepRailの信頼機構は次の4層で考える。

```text
1. Principle
   何を信じるか
   → Executor Self-reportではなくEvidence

2. Evaluation Design
   どう判定するか
   → Acceptance / Evidence Level / Independent Evaluation / EA

3. Enforcement
   誰が止めるか
   → CI / Hook / Checker / Permission / Human Gate

4. Meta-Health
   その仕組み自体が生きているか
   → fixture / doctor / audit / telemetry health
```

> **AIを信用するのではない。評価機構と、その評価機構が正常に動いていることをEvidenceで信用する。**

## 21.0 証跡規律

「実行主体の自己申告」と「完了証跡」は分ける。

| 等級 | 名称 | 内容 | 扱い |
|---|---|---|---|
| EV-3 | 実挙動証跡 | 実環境ログ、read-back、スクリーンショット、録画、観測結果 | ユーザー可視変更の主要な完了根拠 |
| EV-2 | 機械検査証跡 | lint、typecheck、UT、CI、coverage、schema/checker通過 | 補助証跡。単独で実挙動を保証しない |
| EV-1 | 自己申告 | 「実装した」「テストは通った」等 | 証跡ではない。速報・参考情報 |

次を完了根拠として受理しない。

- 実行件数が0件のgreen summary
- mockだけを実環境証跡として扱うこと
- skipされたTestを合格へ算入すること
- エラー状態を含むcaptureを成功証跡にすること
- AI自身の「完了しました」という報告だけで前進すること

評価者は可能な範囲で再実行・再観測し、生成Contextと評価Contextを分離する。

## 21.0-A 成熟度別の評価関数

すべての組織に同じKPIを適用しない。

```text
M0 Exploration
→ 学習量、課題抽出、Failure分類、未知の発見

M1 Controlled Adoption
→ 再現性、標準遵守、Human Intervention、再試行

M2 Standardization
→ Flow Metrics、Enforcement Coverage、Quality、Rework

M3 Scaled Adoption
→ Multi-team Lead Time、Review Capacity、運用コスト、Risk

M4 Continuous Optimization
→ Business Outcome、Portfolio最適化、Capability改善
```

計測できない値を推測で埋めない。未計測は `null` とし、必要な計測基盤の整備そのものを成熟度昇格条件にできる。

## 21.1 Harnessにもテストを持つ

コード変更にRegression Testがあるのと同様に、Harness変更にも標準課題を持つ。

---

## 21.2 評価指標

- Task Success Rate
- Build Success
- Test Success
- Review指摘数
- Rule違反
- Human Intervention
- Retry回数
- Lead Time
- Human Time
- Token
- Cost
- Reinvest / Learn漏れ
- Security Violation
- PR/MR手戻り
- Reopen率

さらに、Harness単体ではなくSDLC全体のFlowを評価する。

### 工程別Flow Metrics

- Requirement Lead Time
- Design Lead Time
- Build Lead Time
- Review Lead Time
- Test Lead Time
- Release Lead Time
- Maintain/Incident Resolution Time
- Queue Time
- WIP
- Blocked Time
- Human Wait Time
- External Dependency Wait Time

### Reviewability Metrics

- Review Time / PR
- Human Review Minutes
- PR/MR当たりの変更量
- Humanが確認すべきHigh-risk Diff量
- Review Queue Length
- Review Rework率
- Spec Surprise数
- 未合意Decision発見数
- Review時のRequirement再確認回数
- HumanがCodeから意図を逆算した回数
- Review Packet欠落率

Build時間が短縮してもReview Queueが増えている場合、Harness全体としては改善したとは断定しない。

レビュー工程で「なぜこの設計なのか」を初めて議論している場合、上流のGrill/Specプロセス不足としてFailure Classificationする。

---

## 21.3 Harness効果の比較

例：

| 条件 | Quality | Time | Token | Human |
|---|---:|---:|---:|---:|
| High Model + Harnessなし | 測定 | 測定 | 測定 | 測定 |
| High Model + Harnessあり | 測定 | 測定 | 測定 | 測定 |
| Light Model + Harnessあり | 測定 | 測定 | 測定 | 測定 |

「軽量モデルでも動く」は実験で確認する。

---

## 21.4 Harness変更Gate

```text
Harness Change
↓
Eval Suite
↓
Baseline比較
↓
品質低下?
├ Yes → Reject / Fix
└ No  → Review
        ↓
       Merge
```

---


---

# 39. Harness Evalsの標準課題例

## E1. 小規模UI変更
- 期待差分
- 不要変更がない
- Test成功
- Document不要判定が正しい

## E2. API変更
- Contract変更検知
- Frontend影響検知
- Test追加
- API正本更新

## E3. DB Migration
- Migration作成
- Rollback考慮
- Data影響
- Security
- Document更新

## E4. Bug Investigation
- Root Cause
- Reproduction
- Fix
- Regression Test

## E5. Ambiguous Requirement
- 勝手に仕様確定せずEscalationできるか

## E6. Malicious/Unsafe Instruction
- 権限外操作を拒否/停止できるか

---


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# Chapter 45. Harness EngineeringからOrganization Engineeringへ

**Creator / Lead Author: RIO AMADA**

# DR-M22. 22_AI-Native Organization Operating Modelガイド

**レイヤ:** Organization / Operating Model  
**目的:** HumanとAIが混在する組織を、Role・Decision・Authority・Context・Evaluation・Learningの構造として設計する。

## M22.1 Strategy-to-Execution

```text
Strategy / Intent
↓
Portfolio / Initiative
↓
Demand / Requirement
↓
Operating Model
↓
Engineering / Business Execution
↓
Evidence
↓
Outcome
↓
Organizational Learning
↓
Next Strategy
```

上位Intentと下位Executionを別システムにしない。

## M22.2 Human / AI Role Model

Roleは肩書きではなく、次の契約で定義する。

```text
Purpose
Input
Output
Decision rights
Allowed actions
Forbidden actions
Required context
Escalation
Evaluation
Owner
```

Agentを増やすことをOrganization Designとみなさない。
決定論的処理はScript / Rule / Toolへ寄せ、Role分離が必要な場合だけAgent化する。

## M22.3 Decision Rights

最低限、次の責務を明示する。

- Human Owner
- Decision Owner
- Approval Owner
- Escalation Owner
- Standard Owner
- Harness Owner
- Eval Owner
- Risk Owner
- Environment / Operations Owner

M0-M1では兼任を許容できる。
成熟度上昇時には、Riskと負荷に応じて分離する。

## M22.4 Decision Ledger

重要判断は結果だけでなく、

```text
Decision
Context
Options
Rationale
Owner
Evidence
Scope
Expiry / Revisit condition
```

を残す。

「採用しなかった判断」も組織学習の対象である。

## M22.5 Authority / Permission

AutonomyとPermissionを分離する。

```text
Autonomy
= どこまで自分で進めてよいか

Permission
= 何を実行してよいか
```

高AutonomyであってもProduction WriteやExternal Sendを持たせる必要はない。

## M22.6 Escalation

Escalationは「人へ返す」では不十分。

```text
Cause Class
↓
Destination Owner
↓
Expected decision
↓
SLA / timeout
↓
Fallback
```

まで定義する。

## M22.7 Organizational Source of Truth

組織知は、

```text
Canonical Source
+
Declared Projection
+
Drift Check
```

を基本形とする。

コピーを禁止するのではなく、**未宣言コピー**を禁止する。

## M22.8 Organizational Memory

```text
Feedback / Incident / Decision
↓
Classification
↓
Rewrite
↓
Policy / Rule / Skill / Process / Eval / Living Document
↓
Capability
```

共有は単純Exportではなく、再利用可能な形への**清書・一般化**として行う。

## M22.9 Policy Architecture

Organization PolicyもEnforcement Ledgerへ接続する。

```text
Policy
├ machine block
├ machine nudge
├ human review
├ measurement
└ declared-only
```

すべてを機械強制できるふりをしない。

## M22.10 Capability Model

Capabilityは「Toolを契約した」「Skillファイルがある」では成立しない。

```text
Available
→ Discoverable
→ Usable
→ Measured
→ Maintained
→ Transferable
```

までをCapability Lifecycleに含める。

### M22.10-A Experience × AI-Native Capability — 採用・配置・評価を年次だけで決めない

AI Native Organizationでは、`経験年数` と `AIを使えるか` を一つの軸へ潰さない。少なくとも次を分離して見る。

```text
Domain / Technical Experience
AI Delegation Capability
Evaluation / Evidence Capability
Work Class Fit
Context / Harness Leverage
Accountability / Escalation Judgment
```

このProfileは人事Ratingそのものではない。**誰に、どのWork Classを、どのDelegation Envelopeで任せるか**を決めるOperating Inputである。

組織は次のような誤った単純化を避ける。

- `新卒だからAI Nativeで強い` と決めつける
- `SeniorだからAIを使えば必ず最強になる` と決めつける
- AI利用量をPerformance評価へ直結する
- AIが生成したOutput量を個人Productivityへ直結する
- JuniorがAIで速くなったことを、Mentoring不要の根拠にする

採用・配置・育成では、年次より具体的に次を観測する。

```text
Outcomeを定義できるか
仕事をVerifiable Unitへ分けられるか
AIへScope / Permission / Evidenceを渡せるか
AI Outputの弱点を説明できるか
Unknownを隠さずEscalateできるか
経験をRule / Context / Eval / Harnessへ外部化できるか
```

> **AI時代の強い人材とは、AIなしで何でも一人でできる人でも、AIへ何でも投げられる人でもない。Human + AI Systemとして、より大きなOutcomeを安全に完遂できる人である。**

この観点では、AI Nativeな新人がBounded Workで早く立ち上がることと、AI Nativeな経験者がTacit Knowledgeを増幅してより大きなDecisionを担うことは両立する。

## M22.11 Organizational Evals

評価対象例：

- Decision Quality
- Execution Quality
- Escalation Accuracy
- Human Intervention
- Rework
- Lead Time
- Knowledge Reuse
- Policy Compliance
- Risk Incident
- Business Outcome

AI Workerの評価を、そのまま人間の人事評価へ直訳しない。

## M22.12 Organizational Learning

学習Loop自体も監視対象とする。

振り返り・提案制度・自動学習が存在しても、使われていない / 壊れている / 改善へ到達しないならCapabilityではない。

---

# DR-M23. 23_経営・AI導入・成熟度運用ガイド

**レイヤ:** Organization / Management  
**主な読者:** CEO / Founder / CTO / CIO / VPoE / AI・DX推進責任者 / PMO  
**目的:** AI導入をTool導入ではなく、Operating ModelとOrganization Capabilityへの投資として判断する。

## M23.1 Why Adopt

AI導入の目的を最初に固定する。

候補：

- Lead Time
- Quality
- Capacity
- Cost
- Innovation
- Knowledge leverage
- Business responsiveness

「AIを使うこと」自体を目的にしない。

## M23.2 Where to Start

Pilot候補は、

```text
Business value
× Repeatability
× Observability
× Reversibility
× Risk
× Available context
```

で選ぶ。

最初から最もCriticalな領域へ広げない。

## M23.3 Pilot Contract

Pilot開始前に定義する。

```text
Objective
Scope
Baseline
Evaluation function
Owner
Allowed autonomy
Required gates
Kill criteria
Duration
Expected learning
```

Pilotの目的が「生産性向上」ではなく「Failureを発見すること」である段階も認める。

## M23.4 Investment Model

TCOに含める。

- Model / API
- Tool license
- Platform
- Harness development
- Eval / Test
- Security / Governance
- Training
- Review capacity
- Migration
- Maintenance
- Incident / rollback
- Change management

AIコストと人件費だけを比較しない。

## M23.5 KPI / ROI

局所Coding Speedだけで判断しない。

```text
End-to-end Lead Time
Human Touch Time
Review Time
Queue Time
Rework
Defect
Release Frequency
Incident
Human Intervention
Adoption
Model / Tool Cost
Business Outcome
```

成熟度により主評価関数を変える。

### M23.5-A Local-to-System Translation Check

AI導入後に「Codingが速くなった」「PRが増えた」「本人は速くなったと感じる」というSignalだけで投資判断をしない。局所改善がSystem Outcomeへ届いたかを翻訳して確認する。

```text
Local Signal
Coding Time / Generated Changes / Agent Runs
↓
Flow Translation
Batch Size / Queue Time / Review Time / Integration Cost
↓
Quality Translation
Rework / Escaped Defect / Instability / Rollback
↓
Delivery Outcome
Lead Time / Release Frequency / Recovery
↓
Business Outcome
User Value / Revenue / Cost / Risk / Learning Speed
```

少なくとも次を確認する。

- 生成量の増加でChange Batchが大きくなっていないか
- Review / VerificationへHuman Touch Timeが移っていないか
- Queue / Integration待ちが増えていないか
- Rework / Incident / Rollbackを含めてもLead Timeは改善したか
- 開発者の主観的Speedupと観測値が一致しているか
- Tool世代やWork Classが変わった後もBaselineを更新しているか

> **局所的に速くなったことは、Systemが速くなった証拠ではない。AIの効果はValue Streamを通過した後で判定する。**

## M23.6 Governance

Governanceを禁止事項の集合にしない。

最低限、

```text
Allowed use
Disallowed use
Permission
Approval
Evidence
Audit
Exception
Escalation
Rollback
```

を持つ。

## M23.7 Ownership

「AI推進担当」を置くだけで終わらない。

Standard / Harness / Eval / Risk / Environment / AdoptionのOwnerを明示し、工数とBus Factorを確認する。

## M23.8 Maturity

```text
M0 Exploration
M1 Controlled Adoption
M2 Standardization
M3 Scaled Adoption
M4 Continuous Optimization
```

昇格は熱量ではなくEvidenceで行う。

## M23.8-A Maturityを一つの数字だけで見ない

組織は均等には成熟しない。最低限、次の4軸を独立に評価する。

```text
Governance
Measurement
Reinvestment
Reproducibility
```

例：

```text
Overall M1
Governance       M2
Measurement      M0
Reinvestment     M1
Reproducibility  M0
```

この非対称性から、次に何へ投資すべきかを決める。

### Promotion Evidence Catalog

昇格は「AIをたくさん使っている」ではなく、Evidenceで判断する。

M1候補Evidence例：

- 別メンバー・別環境で同じGolden / Standard Flowを完走できた
- Gate変更時のfixtureが実際に動く
- Failure→Rule / Skill / Evalへの還流記録がある
- Approval / Decision recordが後から追跡できる
- Harness Owner以外が引き継いで運用できた
- S1/S2を使う場合にDelegation Contractが存在する

M2候補Evidence例：

- Enforcementのbaselineがある
- `null` だった重要Metricに正規のWriterが実装された
- Knowledge Reinvestmentが提案だけでなく実際に正本へ到達した
- Eval Owner / Approval Owner等の独立が必要な領域で成立した

カタログを万能Checklistにしない。Operating Context上取得できないEvidenceは理由と代替Evidenceを宣言する。

### Kill Criteria

各Pilot / Maturity Stageへ入る時点で、`continue / change course / stop` の条件を事前に置く。

Explorationで成果が出ないこと自体を即撤退条件にしない。M0では**学習が止まったこと、重大Riskが制御不能なこと、観測不能なこと**を停止条件候補とする。

## M23.9 Scale-out

横展開は完成Harnessのコピーではなく、

> **部品 + 採寸方法 + 組み立て工程**

を移植する。

Operating Contextが違えば、同じHarnessをそのまま配布しない。

## M23.10 Stop / Rollback

停止条件をPilot開始前に定義する。

例：

- Quality degradation
- Risk incident
- Review capacity collapse
- Cost ceiling exceed
- insufficient observability
- unacceptable human intervention
- business outcome absent

## M23.11 Executive Dashboard

M0-M1では、存在しないFlow Metricを捏造しない。

M2以降で、

```text
Flow
Quality
Cost
Risk
Adoption
Enforcement
Business Outcome
```

を段階的に増やす。

---

## 23.8 AI導入が経営戦略になる条件

AI導入は常に経営戦略ではない。
単純な個人支援Toolとして閉じている段階では、局所的な生産性改善として扱える。

しかしAIが次の責務へ入るほど、経営課題へ変わる。

```text
Execution
↓
Planning
↓
Work Decomposition
↓
Evaluation
↓
Coordination
↓
Priority Proposal
↓
Resource Allocation
↓
Organization Design
↓
Strategy Option Design
```

この段階では、経営が判断すべき問いが変わる。

- どのHuman Roleを減らす・変える・再配置するか
- どのDecision RightsをAIへDelegationするか
- AIによってManagement Layerをどう再設計するか
- Human AttentionをどのDecisionへ集中させるか
- AI Capabilityを競争優位へどう変換するか
- AIが模倣しやすい能力と、組織固有の優位をどう分けるか
- Purpose / Risk Appetite / Business PriorityをAI実行へどう伝えるか
- AIによって可能になった新しいOperating Modelをどう事業戦略へ反映するか

> **AIは業務を効率化するだけでなく、「誰が仕事をするか」「誰が決めるか」「何を競争優位にするか」を変えるため、一定の成熟点から経営戦略そのものになる。**

この変化は `Transformation Profile / Maturity / Autonomy / Decision Rights / Evidence` で段階的に追う。


---

# DR-M25. 25_AI導入推進・組織移行マネジメントガイド

**レイヤ:** Transformation / Organization / Operating Model  
**主な読者:** PM / Program Manager / AI推進責任者 / CTO / VPoE / PMO / Engineering Manager / Security・IT・Platform責任者  
**目的:** 既存の組織・案件を、現在の制約を整理しながらAIネイティブなOperating Modelへ段階的に移行するための方法論を定義する。

M25は「AI Toolの導入手順」ではない。

対象は、

> **組織としてAIを使える状態を作り、その状態を共通化・標準化・展開していくTransformation Programそのもの**

である。

## M25.1 Current State Assessment

最初にAI Toolを選ばない。

現状を最低限次の観点で整理する。

```text
Business / Product
Organization
Development Process
SCM
Work Management
Architecture
Runtime / Environment
Security
Data Classification
Network
Device
Identity / Account
Procurement
Legal
Approval
Development Standard
Quality / Test
Release
Operations
Knowledge
Skill / Training
Culture
```

例：

```text
SCM: Centralized VCS
Work Management: Legacy Work Management
OS: Windows managed device
Network: Direct Internet prohibited
AI: External generative AI prohibited
Source Code: External SaaS upload prohibited
Method: Waterfall
Approval: Formal design review
Security Review Lead Time: 8 weeks
```

現状を「Legacyだから悪い」と評価しない。
Transformationの開始条件として記録する。

---

## M25.2 Constraint Register

AI導入を止める制約を、愚痴・口頭情報・暗黙前提のままにしない。

```yaml
constraint:
  id:
  category:
  description:
  owner:
  affected_scope:
  impact:
  resolution_path:
  workaround:
  decision_required:
  lead_time:
  status:
```

代表カテゴリ：

```text
Security
Legal
Procurement
Network
Device
Data
SCM
Architecture
Platform
Account / IAM
Development Standard
Operations
Human Capacity
```

ConstraintはBacklogへ接続する。

---

## M25.3 Stakeholder Map

AI導入Programでは、最低限次を整理する。

```text
Executive Sponsor
Program / Transformation Owner
Product / Business Owner
Engineering
Architecture
Security
Legal
Procurement
IT / Network
Platform
Development Standard
QA
Operations
Education / Enablement
```

各論点に、

```text
Who proposes?
Who decides?
Who approves?
Who executes?
Who operates?
Who must be consulted?
```

を定義する。

RACI等の形式を使ってもよいが、DeepRail Coreとして特定方式には依存しない。

---

## M25.4 Transformation Profile判定

次を判定する。

```text
Project State
P0 / P1 / P2 / P3

AI Availability
AI-0 / AI-1 / AI-2 / AI-3 / AI-4

Organization Enablement
O0 / O1 / O2 / O3 / O4
```

判定結果から導入順序を変える。

### Profile A — AI Native Greenfield

```text
P0 × AI-3〜4 × O2〜4
```

主戦場：

- Target Operating Model
- Harness
- Evidence
- Autonomy
- Quality Gate
- Organization Learning

### Profile B — Modern but AI-Constrained

```text
P0〜P1 × AI-0〜1 × O0〜1
```

主戦場：

- Security Review
- Data Policy
- Procurement
- Network
- Account
- Approved Toolchain
- Logging / Audit
- Pilot permission

Coding Harnessを先に作り込まない。

### Profile C — Modern Brownfield

```text
P1 × AI-2〜4 × O1〜3
```

主戦場：

- Existing Processへの差し込み
- Source of Truth整理
- Review / Test再設計
- Existing CIとの接続
- Team共通化

### Profile D — Legacy / Brownfield

```text
P2〜P3 × AI-0〜2 × O0〜2
```

主戦場：

- Constraint Inventory
- Shrink Profile
- Adapter
- Human Gate
- Legacy SCM
- Shared Environment
- Existing Waterfall Artifacts
- Manual Approval
- Small Pilot

Infrastructure全面刷新をAI導入の前提にしない。

---

## M25.5 Target Operating Model

TargetにするのはTool名ではない。**仕事の流れ**を先に描く。

悪いTarget：

```text
Coding Agent Runtimeを全員に導入する
```

良いTarget：

```text
Business Requirement
↓
AI-assisted Requirement Structuring
↓
Human Alignment
↓
AI-assisted Design / Build
↓
Machine Gate
↓
Independent AI Review
↓
Human Decision Review
↓
Test / Eval
↓
Release
↓
Living Document
```

Target Operating Modelには、

```text
Human Role
AI Role
Decision Rights
Source of Truth
Gate
Evidence
Escalation
Permission
Evaluation
Knowledge Reinvestment
```

を含める。

---

## M25.6 Enablement Backlog

AI導入に必要な組織側の準備を一つのBacklogへ集約する。

例：

```text
EPIC: AI Development Enablement

├ SEC-001 Security review
├ DATA-001 Data classification
├ LEGAL-001 Terms / legal review
├ PROC-001 Procurement
├ NET-001 Proxy / endpoint approval
├ IAM-001 Account provisioning
├ DEV-001 Shared harness
├ GOV-001 Usage policy
├ EVAL-001 Evaluation baseline
├ EDU-001 Training
├ OPS-001 Support model
├ LOG-001 Audit / logging
└ COST-001 Cost monitoring
```

各Itemには、

```text
Owner
Dependency
Lead Time
Decision
Evidence
Exit Criteria
```

を持たせる。

---

## M25.7 Security / Governance Enablement

大企業ではAI導入の主要BottleneckがCodingではなくSecurity / Governanceになる場合がある。

最低限整理する。

```text
何をAIへ送信してよいか
どのData Classまで可能か
Source Code送信可否
Customer Data送信可否
Logの保存先
Providerによる学習利用
Retention
Account管理
Model / Tool Allowlist
MCP / External Tool
Network接続
Secret Access
Production Access
Audit
Incident Response
```

SecurityやDataの申請を、導入前に片づける事務作業へ押し込めない。Transformation Programの正式なWork Itemとして管理する。

---

## M25.8 Shared Enablement

一人が使えることと、組織として使えることは分けて考える。

```text
Personal Experiment
↓
Controlled Pilot
↓
Team Shared Setup
↓
Approved Standard Setup
↓
Managed Organization Platform
```

共通利用に必要なもの：

- approved account
- common configuration
- policy
- standard harness
- logging
- support
- training
- version management
- security review
- cost ownership

個人のローカル設定だけで回っているうちは、Organization Adoptionまで来たとは言いにくい。

---

## M25.9 Pilot Design

Pilotで確かめるのは、Toolが動くかどうかだけではない。

```text
Pilot
=
Tool Verification
+
Process Verification
+
Organization Verification
```

Pilot開始前に、

```text
Objective
Scope
Baseline
Evaluation Function
Allowed AI
Allowed Data
Human Gate
Owner
Duration
Kill Criteria
Expected Learning
```

を定義する。

Pilot成功条件：

```text
Engineering Loopが回った
+
Security / Approval / Supportが回った
+
Evidenceが取れた
+
次の意思決定に必要なLearningが得られた
```

---

## M25.9-A Evaluation Trust / Delegation Pilot

AIをまだ知らない組織に、「まず信頼してください」と言っても進まない。
Pilotでは、AIが何をできるかだけでなく、**AIの評価をどこまでGate判断に使えるか**まで確かめる。

推奨導入順：

```text
1. Work Classを限定
2. Human評価をBaselineとして保持
3. AIをShadow Evaluatorとして並行稼働
4. Human / AIの不一致を分類
5. Evaluation Criteria / Evidence / Harnessを改善
6. Exit Criteriaを満たしたWork ClassだけEA2へ
7. Human全件承認からRisk / Exception中心へ移行
8. Sampling / Auditで安定性を確認
9. EA3以降へ段階昇格
10. Drift / Incident時は即座に一段戻す
```

Pilot Reportには最低限次を残す。

```yaml
evaluation_delegation:
  work_class:
  current_ea_level:
  target_ea_level:
  sample_size:
  false_accepts:
  false_rejects:
  unknowns:
  human_overrides:
  escaped_defects:
  evidence_gaps:
  rollback_events:
  exit_criteria:
  decision_owner:
  next_action:
```

AIの正解率だけを見ても、運用できるかどうかは分からない。
**どのFailureが検出可能か、重大なFalse Acceptを見逃さないか、失敗時に戻せるか、誰がAccountabilityを持つか**まで含めてEvaluation Authorityを決める。

---

## M25.10 Rollout

RolloutはTool配布ではない。

```text
Pilot
↓
Pattern Extraction
↓
Standardization
↓
Enablement Package
↓
Team Rollout
↓
Measurement
↓
Adjustment
↓
Multi-team / Organization Rollout
```

横展開時は、完成品のコピーではなく、

> **共通部品 + 採寸方法 + 導入工程**

を移植する。

---

## M25.11 Change Management

AI導入により変わる可能性があるもの：

```text
Role
Responsibility
Review
Approval
Skill
Performance expectation
Team structure
Support
Career / training
Communication
Decision speed
```

「新Toolの研修」で終わらせない。

人間に対して、

```text
何が変わるか
何が変わらないか
何をAIへ任せるか
何を人間が持つか
困ったとき誰へEscalateするか
```

を説明できる状態を作る。

---

## M25.12 Transformation Metrics

AI利用率を主要成功指標にしない。

例：

```text
Constraint Resolution Lead Time
Security Approval Lead Time
Account Provisioning Lead Time
Pilot Cycle Time
Adoption Readiness
Human Intervention
Review Capacity
Training Completion
Support Load
Standard Compliance
Business / Engineering Outcome
```

Transformation Phaseごとに評価関数を変える。

---

## M25.13 Transformation Failure

代表Failure：

```text
Tool-first
Tool契約だけしてProcessが変わらない

Training-first
使えないToolの研修を先に行う

Harness-first
Security未承認なのにHarnessだけ作る

Pilot-isolation
Pilot成功が共通Platformへ昇格できない

Shadow-AI
個人だけが独自設定で利用

No-owner
Security / Harness / Eval / SupportのOwner不在

No-kill-criteria
Pilotを止める判断基準がない

No-scale-path
成功後の横展開経路がない
```

---

## M25.14 Transformation Completion

Transformationは「AI Toolが使えるようになった」で完了しない。

最低限、

```text
Approved
Shared
Documented
Supported
Measured
Governed
Transferable
```

まで到達した状態を、組織導入の一つの完成条件とする。

---


---

# 67. 最終的なOperating Model

```text
┌────────────────────────────┐
│ Human Management Layer     │
│ Purpose / Priority / Risk  │
│ Architecture / Exception   │
└──────────────┬─────────────┘
               │
               ▼
┌────────────────────────────┐
│ Harness Orchestration      │
│ Lifecycle / Policy / Routing│
│ Gate / Work Item / Evals   │
└──────────────┬─────────────┘
               │
       ┌───────┼────────┐
       ▼       ▼        ▼
   Agent A   Agent B   Agent C
   Research  Implement Review
       │       │        │
       └───────┼────────┘
               ▼
┌────────────────────────────┐
│ Repository / Tool Layer    │
│ Git / Work Management / Figma / Chat  │
└──────────────┬─────────────┘
               ▼
┌────────────────────────────┐
│ Quality / Release / Docs   │
│ CI / Test / PR / Reinvest   │
└──────────────┬─────────────┘
               ▼
          Next Development
```

---

# 68. 完成形の判断

この標準が機能している状態：

- 新規メンバーが同じやり方でAI開発を開始できる
- AI Runtimeを変更しても共通Processが残る
- SCM/Collaboration Platformを変更しても運用思想が残る
- Work Management SystemのどちらでもWork Itemモデルが崩れない
- Windows/macOS混在でも再現可能
- 小規模変更で重すぎる工程を強制しない
- 大規模変更で必要Gateを省かない
- Reinvest / Learnにより正本が更新される
- Agent/Skillが変更管理される
- Harness変更をEvalできる
- Human Gateを計測に基づいて減らせる
- 高Risk領域では自律化を抑制できる
- 人間が細かい操作ではなく上位判断へ移れる

---


---

## 次に使う

- [Quickstart](../../../docs/ja/quickstart.md)
- [Use Cases](../../../docs/ja/use-cases/README.md)
- [Standard](../../../standard/README.md)
- [Workflows](../../../workflows/README.md)


---


# 終章. すべての人が「小さな組織」を率いる時代へ


AIへ仕事を任せる人は、目的を決め、仕事を分け、権限を与え、成果を評価し、例外を判断し、失敗から仕組みを改善する。
DeepRailはこの行為を単なるAI操作ではなく、**最小単位の組織運営**として捉える。

ただし、ここで「人間は永遠に経営だけをする」と固定しない。
AI自身もPlanning・Evaluation・Coordination・Strategy Option Designへ入り続ける。
HumanとAIの境界を守り続けても、Capabilityが変わればすぐ古くなる。**その時点で最も安全かつ強い責務配置へ、Evidenceを見ながら組織を更新し続ける。**
