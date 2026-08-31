# Production Adoption Guide

本番Projectでは一気にEA/Aを上げません。

1. `deeprail init --profile standard --adapter claude`
2. 1 Work Classを選ぶ
3. Human-led / AI-assistedでEvidence Contractを校正する
4. Shadow Evaluationを回す
5. Failure Detectability / Reversibility / Auditabilityを確認する
6. A / EA / SをWork Class単位で変更する
7. Human InterventionをReinvestmentへ戻す
8. 条件が弱くなれば委譲を戻す

DeepRailは成熟度競争ではなく、責務を移してよい条件を管理します。
