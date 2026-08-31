# DR-M01 — AI駆動開発 基本方針

> Status: **canonical v0.16.8**> Creator / Lead Author: **RIO AMADA**

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

## 5.3 AI導入後は「Build」から別工程へボトルネックが移る

AI Agentの導入効果を「コード生成速度」だけで評価しない。

従来のソフトウェア開発では、実装・Build工程が大きな時間を占めることが多かった。
AI Agentによってこの工程が急速に短縮されると、開発全体の制約は前後工程へ移る。

```text
Before

Requirements
    ↓
Design
    ↓
████████████████
     Build
████████████████
    ↓
Test
    ↓
Release
    ↓
Maintain

主な制約 = Build
```

```text
After AI Agents

Requirements ━━━━━━━
       ↓
Design       ━━━━━━━
       ↓
Build        ━
       ↓
Review       ━━━━━━━
       ↓
Test         ━━━━━━━
       ↓
Release      ━━━━━━━
       ↓
Maintain     ━━━━━━━
```

AI駆動開発を見るとき、Codingだけを切り出さない。Buildが速くなれば、次に詰まる場所が変わる。見る対象は、**SDLC全体のFlow**になる。

Harnessの対象はBuildだけではない。

```text
Requirements
├ 要求収集
├ 要求整理
├ Work Item化
└ 曖昧性・矛盾検知

Design
├ Impact Analysis
├ Architecture
├ Interface Design
└ Design Review

Build
├ Implementation
├ Refactoring
├ Local Build
└ Local Test

Review
├ AI Self Review
├ Independent AI Review
├ Human Review
└ Security Review

Test
├ Unit
├ Integration
├ E2E
└ Acceptance

Release
├ CI/CD
├ Release Gate
├ Migration
└ Rollback

Maintain
├ Monitoring
├ Incident
├ Bug Analysis
├ Operations
└ Living Documents
```

AIによってある工程が高速化した場合は、次にどの工程へ待ち時間・WIP・人間判断が集中したかを観測し、Harnessの改善対象を変更する。

---

## 5.4 AI時代のレビューは「完成物を全部読む」から「前提・決定を先にレビューする」へ移す

AI Agentは、人間より短時間で大量のコード・設計案・文書を生成できる。
AIが全部作ったあとに、人が成果物を最初から最後まで確認する。その順番を変えなければ、Review工程そのものが次のBottleneckになる。

```text
従来
人間が作る
↓
人間がReview
↓
Merge
```

```text
AI導入後の失敗例
AIが大量生成
↓
巨大Diff / 大量Document
↓
人間が後追いReview
↓
認知負荷増大
↓
Review Queue
↓
AIの速度を吸収できない
```

レビューは、最後の工程にだけ置かない。

```text
Intent
↓
前提合意
↓
用語・制約・設計判断を確定
↓
Specification
↓
実装
↓
機械検証 / AI Review
↓
Humanは判断点・Risk・例外を確認
```

人間が特に早い段階で確認する対象は次。

- 何を作るか
- 何を作らないか
- Domain用語
- Acceptance Criteria
- 既存仕様との矛盾
- Interface / Test Seam
- 外部依存
- Error Strategy
- Security / Data Boundary
- 後戻りコストが高い設計判断

レビュー負荷を減らす方法は「Reviewを省略すること」ではなく、**Reviewすべき判断を実装前へ移し、実装後に人間が初めて設計意図を発掘する状態を避けること**である。

ここではReview Queueがなぜ詰まるかと、判断を前へ出す原則までに留める。Evidenceをどう人へ渡すか、何を見ればGOを出せるかの本論は `21.X Human Evaluation Interface` へ集約する。

---
