# DR-M16 — セキュリティ・AIガバナンスガイド

> Status: **canonical v0.16.8**> Creator / Lead Author: **RIO AMADA**

## 20.1 権限を一括で考えない

最低でも次を分ける。

```text
Read
Write
Execute
External Send
Production Access
Secret Access
Approval
```

---

## 20.2 原則

- 最小権限
- SecretをPrompt/Documentへ直書きしない
- Production権限は通常開発から分離
- 外部送信可能情報を定義
- Tool/MCP Allowlist
- 破壊的Commandの制限
- Audit Log
- Human Approvalが必要な操作を定義

---

## 20.3 Hook/Toolの危険性

Agentの自然言語指示だけでなく、実行権限を持つHook/Script/Tool自体もReview対象とする。

---
