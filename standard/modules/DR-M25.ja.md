# DR-M25 — AI導入推進・組織移行マネジメントガイド

> Status: **release-candidate v0.16.8**  
> Creator / Lead Author: **RIO AMADA**

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
