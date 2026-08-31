# Specification — 代理承認

## Intent
承認者不在時に、事前に許可された代理者だけが有効期間内に承認できる。

## Scope
- 代理者の事前登録
- 有効期間
- 代理承認の監査記録
- UI上の代理表示

## Non-goals
- 組織階層の自動推論
- 無制限の代理権再委譲

## Acceptance Criteria
1. 有効期間外の代理承認は拒否される
2. 未登録ユーザーは代理承認できない
3. 代理承認は監査ログで本人承認と区別できる
4. 通常承認の既存挙動を壊さない

## Required Evidence
- Authorization tests
- Expiry behavior
- Observed UI behavior
- Audit-log read-back
- Existing approval regression
