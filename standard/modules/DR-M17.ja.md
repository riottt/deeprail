# DR-M17 — 品質評価・Harness Evalsガイド

> Status: **canonical v0.16.8**> Creator / Lead Author: **RIO AMADA**

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
