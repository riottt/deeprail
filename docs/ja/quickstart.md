# DeepRail 10分Quickstart

DeepRailを最初から全部読む必要はありません。1つのWorkでEnd-to-Endに試します。

## 0. Install（Repository checkoutから）

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
deeprail version
```

## 1. 対象Projectへ導入

Claude Codeを使う例:

```bash
deeprail init \
  --target /path/to/your-project \
  --profile lightweight \
  --communication ja \
  --artifacts ja \
  --adapter claude
```

既存 `CLAUDE.md` がある場合もDeepRail管理Blockだけを追加し、全文置換しません。

## 2. Doctor

```bash
deeprail doctor --project /path/to/your-project
```

## 3. Workを開始

```bash
deeprail work-start \
  --project /path/to/your-project \
  --title "代理承認" \
  --intent "承認者不在時に認可された代理者が承認できるようにする"
```

返された `DRW-...` を控えます。

## 4. AgentへTask Packetを渡す

```bash
deeprail task --project /path/to/your-project --work-id DRW-... --write
```

`.deeprail/runs/<WORK_ID>/...md` が、現在のWorkflow・Evidence・Decision Rightsを含む実行Contractです。

## 5. Evidenceを記録する

例:

```bash
deeprail evidence-add \
  --project /path/to/your-project \
  --work-id DRW-... \
  --type observed_behavior \
  --description "現行の承認挙動を再現して確認" \
  --verified
```

## 6. Gateを確認して進む

```bash
deeprail gate --project /path/to/your-project --work-id DRW-...
deeprail work-advance --project /path/to/your-project --work-id DRW-... --to shape --actor human
```

Gateが満たされなければTransitionは拒否されます。

## 7. Verifyでは独立Evidenceを要求

```bash
deeprail evidence-add ... --type machine_check --actor tool --verified
deeprail evidence-add ... --type independent_evaluation --actor ai --independent --verified
```

## 8. Audit

```bash
deeprail audit-verify --project /path/to/your-project --work-id DRW-...
```

State mutationはHash-chain Auditへ残ります。

## 次

- [Runnable Example](../../examples/approval-delegation/README.md)
- [Evidence Gate](evidence-gates.md)
- [Production Adoption](production-adoption.md)
- [Diagnostic](diagnostic.md)
- [Book](../../book/ja/chapters/README.md)
