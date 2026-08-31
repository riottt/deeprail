# DR-M15 — AI時代の人材育成・習熟・実践ガイド

> Status: **release-candidate v0.16.8**  
> Creator / Lead Author: **RIO AMADA**

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

## 19.19 Human CapabilityとDelegation Qualificationを分ける

`HC0〜HC6`は成長の学習Profileである。一方、実案件でDecision Rightsを委譲できるかはOC-4の資格 `H-1 / H-2 / H-3` で判断する。

```text
HC = 何を学び、どの能力を持つか
H- = このOperating Contextで委任元・判定者になれるか
```

Tool操作が上手いだけではH-3ではない。H-3には少なくとも、Failure Routing、Evidence評価、Delegation Scope、Stop / Escalation判断を実技で確認する。

# Part E. Governance / Quality / Production
