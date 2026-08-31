# Runnable Golden Path — 代理承認

このExampleはMarkdownだけではなく、最小の実行CodeとTestを含みます。

## 実行

```bash
cd examples/approval-delegation/app
python3 -m unittest -v test_approval.py
```

確認するFailure Mode:

- 登録済み代理者
- 未登録Actor
- 有効期限
- Revocation
- Audit identity (`actor` / `on_behalf_of`)

## Evidence Contract

[`evidence-packet.json`](evidence-packet.json) をDeepRail executable evalで確認できます。

```bash
./scripts/deeprail eval evidence --file examples/approval-delegation/evidence-packet.json
```

このExampleは「AIが作ったCode」ではなく、**Outcomeを何で証明して次へ進むか**を示します。
