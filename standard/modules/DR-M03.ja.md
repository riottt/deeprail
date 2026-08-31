# DR-M03 — ハーネス構成・利用ガイド

> Status: **canonical v0.16.8**> Creator / Lead Author: **RIO AMADA**

## 7.1 AI資産の責務

概念上、次を区別する。

| 資産 | 用途 |
|---|---|
| Instruction / Rule | 継続適用する制約 |
| Skill | 繰り返す手順・ワークフロー |
| Agent | 専門責務を持つ実行主体 |
| Hook | 特定イベントで確定的に実行する処理 |
| Tool | Agentが行動する能力 |
| MCP | 外部システムをToolとして接続する境界 |
| Prompt | 一時的・特定用途の依頼 |
| Living Document | 現在状態の正本Context |
| Eval | Harness/Agentの挙動を確認する試験 |

---

## 7.2 配置判断

```text
毎回守る制約か？
→ Rule / Instruction

繰り返す手順か？
→ Skill

専門性・独立Contextが必要か？
→ Agent

必ず実行したい処理か？
→ Hook / CI

外部情報・外部操作が必要か？
→ Tool / MCP

現在仕様を説明する情報か？
→ Living Document
```

---
