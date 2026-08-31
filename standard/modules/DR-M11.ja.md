# DR-M11 — 外部ツール連携ガイド

> Status: **canonical v0.16.8**> Creator / Lead Author: **RIO AMADA**

## 15.1 ToolをSource of Truthで整理する

```text
Communication
├ Chat / Collaboration Channel
└ Mattermost

Work Management
├ Work Management
├ Legacy Work Management
├ Issue / Work Item
└ Issue / Work Item

Design
└ Figma

Source
├ SCM Platform
└ SCM Platform

Development Knowledge
└ Harness Workspace / Living Documents
```

---

## 15.2 情報責務

最も避けたい状態：

```text
仕様AはChat
仕様BはWork Management
仕様CはFigmaコメント
古い仕様はREADME
新しい仕様は人の頭
```

外部ツールは「入力・通知・作業管理」であり、どこを最終正本とするかを明記する。

---

## 15.3 Chat / Collaboration Channel

主用途：

- 会話
- 通知
- 承認依頼
- 障害通知
- Agent完了通知
- Work Item化前の要求候補

ルール例：

```text
Chat上の要求
↓
正式採用
↓
Work Management System/SCM/Collaboration Platform等へWork Item化
↓
必要に応じてLiving Document更新
```

チャットメッセージ単体を恒久仕様にしない。

---

## 15.4 Work Management System

Work Item管理Adapterとして扱う。

共通概念：

```text
Epic / Parent
↓
Issue / Story / Task
↓
Subtask
```

Legacy Work Managementを利用する場合も、製品固有のTracker/Status/Workflowを共通Work Itemモデルへマッピングする。

---

## 15.5 Figma

設計の正本範囲を決める。

例：

```text
Visual / Interaction
→ Figma

System Behavior / API / Data Contract
→ Living Document

実装との対応
→ Link / IDでTrace
```

Figmaコメントだけに仕様判断を残さない。

---
