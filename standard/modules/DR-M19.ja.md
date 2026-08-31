# DR-M19 — AI権限委譲・自律化運用ガイド

> Status: **release-candidate v0.16.8**  
> Creator / Lead Author: **RIO AMADA**

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
