# DR-M02 — ハーネス設計原則

> Status: **release-candidate v0.16.8**  
> Creator / Lead Author: **RIO AMADA**

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
