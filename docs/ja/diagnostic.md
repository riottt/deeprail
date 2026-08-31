# DeepRail Diagnostic — 困りごとから入る

35万文字のBookを最初から読む必要はありません。現在の詰まりを18問で確認し、Book / Standard / Workflowへ接続します。

```bash
deeprail assess --questionnaire > answers.json
# answers.jsonの各値を0〜3で入力
deeprail assess --answers answers.json --format md
```

評価軸:
- Shared Reality
- Evidence
- Human Review
- Delegation
- Delivery System
- Reinvestment

これは組織の優劣を決める成熟度ランキングではなく、**次にどこを設計すべきかを見つけるNavigation**です。
