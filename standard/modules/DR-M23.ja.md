# DR-M23 — 経営・AI導入・成熟度運用ガイド

> Status: **release-candidate v0.16.8**  
> Creator / Lead Author: **RIO AMADA**

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
