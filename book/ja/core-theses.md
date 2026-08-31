# DeepRail Core Theses — Reader Edition

### v0.12.0 中心命題1 — HumanとAIの役割境界は動き続ける

DeepRailは、`AI = Execution / Human = Management` を永久固定された分業として定義しない。
これは現時点で有効なOperating Profileの一つにすぎない。

AI Capabilityが上がり、EvidenceとControlの信頼性が上がれば、AIは次のように従来Human側に置かれていた責務へ入っていく。

```text
実装
↓
調査
↓
計画
↓
Work Breakdown
↓
Review / Evaluation
↓
Coordination
↓
Priority Proposal
↓
Resource Allocation Proposal
↓
Strategy Option Design
```

固定したいのは「人間の仕事一覧」ではない。**責務をいつ、どの条件ならAIへ渡せるのかを判断する仕組み**である。

```text
Delegability = f(
  AI Capability,
  Risk,
  Evidence Reliability,
  Failure Detectability,
  Reversibility,
  Permission,
  Accountability
)
```

AIは人間の仕事を一つずつ代替するだけではない。
**「ここから先は人間の仕事」と考えていた境界そのものを継続的に書き換える。**

このため、AI導入は最終的にIT導入だけでは閉じない。
人間をどこへ再配置するか、どのDecision RightsをAIへ委譲するか、組織をどう薄く・速く・学習可能にするか、競争優位をどこへ置くかという**経営戦略の問題**へ到達する。

### v0.12.0 中心命題2 — AIを信頼するのではなく、任せられる条件を検証する

AI導入初期に起こる「どこまで人間が判断すべきか」という議論を、DeepRailはAIへの信仰・不信の問題として扱わない。

問いを次へ置き換える。

> **この種類の仕事・判断について、AIの評価結果を次工程へ進むApproved Evidenceとして扱えるか。**

信頼対象はModel単体ではなく、次を含むEvaluation Systemである。

```text
AI Capability
+ Evaluation Criteria
+ Evidence
+ Independent Check
+ Failure Detectability
+ Environment Reliability
+ Reversibility
+ Auditability
+ Accountability
```

そのため、導入初期はHumanとAIを並行評価させる。

```text
AI Evaluation ─┐
               ├→ Compare / Calibrate
Human Evaluation┘
        ↓
Disagreementを分類
        ↓
AI Error / Human Error / Ambiguous Criteria / Missing Evidence / Environment / Requirement Drift
        ↓
対象Work Classで信頼性をEvidence化
        ↓
限定範囲だけEvaluation Authorityを委譲
        ↓
Sampling / Audit / Exception Review
        ↓
維持できれば拡大、崩れればRollback
```

Human Gateを減らすこと自体を成功条件にしない。
目的は、**Human Attentionを、本当に人間判断が必要な曖昧性・高Risk・不可逆Decision・Accountabilityへ集中させること**である。

> **AIを信頼するのではない。AIに任せられる条件を設計し、その条件が満たされたことを信頼する。**

---

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
