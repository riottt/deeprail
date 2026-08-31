# DR-M04 — 環境構築・セットアップガイド

> Status: **release-candidate v0.16.8**  
> Creator / Lead Author: **RIO AMADA**

## 8.1 対応対象

最低限、次の環境差を考慮する。

- Windows
- macOS
- Linux
- WSL
- ローカル開発
- Dev Container
- Cloud Development Environment
- Sandbox型Agent Runtime

---

## 8.2 OS混在時の注意点

- `/` と `\`
- bash / zsh / PowerShell
- LF / CRLF
- chmod
- symbolic link
- 大文字小文字の扱い
- PATH
- Node/Python/JDK等のVersion
- package manager
- Docker Desktop依存
- `.env`
- 認証情報の保存先
- CLIの差
- Scriptの実行権限

可能であれば、OS依存Shell Scriptだけに寄せず、Python/Node等のクロスプラットフォームな実装を検討する。

---

## 8.3 セットアップ完了条件

```text
Repository取得可能
Build成功
Frontend起動
Backend起動
DB接続
Test実行
AI Runtime起動
Harness Rule読込
Skill呼出
Agent呼出
必要Tool接続
PR/MR作成可能
```

---

# Part B. 開発プロセス
