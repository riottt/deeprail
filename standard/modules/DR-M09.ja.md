# DR-M09 — チーム・役割運用ガイド

> Status: **canonical v0.16.8**> Creator / Lead Author: **RIO AMADA**

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

## 13.2 Planning / Executionの責務境界

DeepRailでは、PlanningとExecutionを同じ責務として扱わない。Planningは「何を成立させるか・どのApproachを採るか・何を完了とするか」を扱い、Executionは「どのArtifactを変更するか・どの操作を行うか・どのCheckを実行するか」を扱う。

ただし、Planningを永久にHuman-onlyへ固定しない。Work Class、Risk、Evidence Reliability、Failure Detectability、Reversibility、Permission、Accountabilityに応じて、Planning側の責務も段階的に委譲できる。

Team Leadershipの初期設計では、次の分離から始める。

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

# Part C. Repository / Tool / AI Runtime

## 13.4 Team Management Review

Human + AI Teamでは、AIが報告可能な状態情報を人間の会議で読み上げない。

人間の同期時間はDecisionへ集中させる。

```text
Planning
→ Priority / Objective / Boundary

Refinement
→ AI分解案のOutcome / Risk / Dependency確認

Daily / Async
→ AIがStatus / Blocker / Evidenceを集約
→ HumanはDecision / Escalationだけ処理

Review
→ Decision Packet / Evidence / Risk中心

Retro
→ FailureをRule / Skill / Eval / Processへ還元
```

Team運営上の重要な指標：

```text
Execution Capacity
Review Capacity
Approval Capacity
Environment Capacity
Decision Capacity
```

Agent数そのものをThroughputとみなさない。

---
