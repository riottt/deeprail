# DR-M21 — Enforcement・標準観測ガイド

> Status: **canonical v0.16.8**> Creator / Lead Author: **RIO AMADA**

**レイヤ:** Execution Harness / Governance  
**目的:** 宣言したRule・Policy・Gateが実際にどこまで強制され、その強制機構自体が正常に動いているかを監査可能にする。

> **Rule exists ≠ Rule enforced ≠ Enforcement healthy ≠ Control effective.**

## M21.1 Enforcement Lifecycle

Rule / Policyの生涯を次のLoopで管理する。

```text
Declare
↓
Register
↓
Enforce
↓
Verify the Enforcer
↓
Audit
↓
Improve / Retire
```

事故・Decision・外部借用から新Ruleが生まれたら、Rule本文だけを追加せず、Enforcement Ledger登録を同一変更で行う。

## M21.2 Enforcement Ledger

```yaml
- rule_id:
  statement:
  canonical_source:
  source_or_provenance:
  layer: ExH | OpM | EngStd | Org
  status: draft | provisional | effective | retired
  enforcement:
    level: declared_only | nudge | block | measured | human_review
    checker:
    checker_due:
    fixtures: []
  coverage:
    paths: {}
  escape_hatch:
    mode: none | opt_in | temporary | emergency
    expiry:
  owner:
  evidence:
  exception_policy:
```

`declared_only` は禁止しない。ただし「守られている」ではなく、**守られているか機構上は判定できない**状態として表示する。

Org Layerの一部Policyは機械強制不能でよい。その場合は `not_machine_enforceable` を明示し、単なる未実装と区別する。

## M21.3 Enforcement Coverage

```text
Coverage
= block / measured / explicitly human-reviewed rules
  / rules that are enforceable in the declared layer
```

CoverageをKPI目標にしない。用途は、`declared_only` の長期滞留・期限超過・Coverage Gapの発見である。

## M21.4 Gate Coverage Map — Gateが「どこまで効くか」を宣言する

Gateごとに最低限6項目を持つ。

| 観点 | 問い |
|---|---|
| Match Set | 何を許可・禁止の全集合として照合するか |
| Path Coverage | AI Tool / Human CLI / CI / External Toolのどこを通るか |
| Enforcement Mode | block / nudge / after-the-fact review / static deny のどれか |
| Fail Direction | fail-closed / fail-open / fail-silent のどれか、なぜか |
| Blocked-Actor Behavior | block時、Agentは何回で止まり、どこへEscalateするか |
| Limitation | このGateで防げないことは何か |

さらにOperationとEnvironmentを関連付ける。

```text
Operation: Read / Write / Execute / External Send / Production / Secret / Approval
Environment: Windows / macOS / Linux / Container / Cloud / Shared Legacy
```

「AI経路はGuardされるがHuman CLIは素通り」「Hookは警告だけなのにBlockと思われている」等を暗黙にしない。

## M21.5 Guard the Guards

Control Mechanismの変更を通常コードより軽く扱わない。

### Class 1 — Regression Fixture

Gate / Checker変更には、最低でも次の対を持つ。

```text
should_pass fixture
should_block fixture
```

### Class 2 — Doctor

日常的に回せる、冪等・定型・短時間のHarness Health Checkを持つ。長時間化した検査はAuditへ移す。

### Class 3 — Generator + Check

生成物を持つ仕組みは、可能な限り次を対にする。

```text
generator
+
generator --check
```

### Class 4 — PROVENANCE

外部由来のSkill / Rule / Script / Templateには、借用元・取得時点・変更有無・更新方針を残す。

### Class 5 — Quarantine

外部由来の実行可能Assetを、取得直後から本番探索Pathへ置かない。検査→昇格を分離する。

### Class 6 — Audit / Triangulation

宣言・実体・使用痕跡の三点を突合する。

```text
Declared
vs
Exists
vs
Actually used
```

## M21.6 Meta-Health

観測・Learning・Audit Pipeline自体の故障を別系統から検出する。

最低限候補：

- Liveness
- parse error rate
- output/event count deviation
- dropped event
- redaction status
- schema drift
- latency
- Production telemetry / Eval telemetry separation
- cross-platform matrix where relevant

> **「問題が観測されていない」と「観測装置が死んでいる」を区別する。**

fail-silentを許容する系には、別系統のLiveness / Quality Checkを置く。

### M21.6-A Harness Assumption Register — Controlの前提にも寿命がある

Harness / Guard / Workaroundは、作った時点のModel Capability・Runtime・Tool制約について何らかのAssumptionを持つ。その前提が変われば、かつて必要だったControlが過剰になったり、逆に新しいFailureを見逃したりする。

最低限、重要Controlには次を残す。

```text
Assumption
このControlは何ができない / 壊れやすい前提で存在するか

Capability / Environment Dependency
どのModel / Tool / Runtime / Work Classに依存するか

Control Justified
その前提によって何をBlock / Guide / Verifyしているか

Evidence
前提が今も成立していると判断する根拠

Review Trigger
Model更新 / Tool更新 / False Reject増加 / Incident / Eval改善

Expiry / Review Date
再評価する期限

Status
active / simplify-candidate / remove-candidate / superseded
```

Guard the Guardsは「Guardが壊れていないか」だけを問わない。**Guardを必要とした前提そのものが、まだ生きているか**も問う。

> **Harnessは足し算だけで育てない。能力が上がったなら、古い補助輪を外すこともReinvestmentである。**

## M21.7 Environment Matrix for Controls

Gate / Checker / Observerは、必要なOperating Contextで次を試す。

```text
CRLF / LF
UTF-8 / BOM / legacy encoding
non-ASCII path
space-containing path
long path
proxy / network path where relevant
```

「自分のMacでは動いた」だけをControlの完成条件にしない。

## M21.8 Audit Evidence Contract

「ログを残す」を5次元へ分解する。

```text
Structure  : schemaを先に決める
Protection : redaction / append-only / writer ownership
Failure    : evidence capture failure自体を記録
Quality    : path / evidence grade / null semantics
Retention  : retention / deletion / access policy
```

証跡取得に失敗した場合、その失敗自体を証跡化する。

## M21.9 Enforcement Backlog

Enforcementの未整備はHarness Backlogへ入れる。

```text
declared_only aging
checker_due expired
fixture missing
path coverage gap
meta-health missing
stale provenance
human-only control with excessive load
```

ただしCoverage比率を上げること自体を目的にせず、現在のFailure / Risk / Human Bottleneckから優先順位を決める。

---
