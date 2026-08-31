# DeepRailはどう動くか

DeepRailは、AIに指示を出すPrompt集ではありません。

```text
Book
なぜそうするか
        ↓
Standard
何を守るか
        ↓
Workflow
どう進めるか
        ↓
Template / Eval
何を作り、どう確かめるか
        ↓
Project Profile
このProjectではどこまで任せるか
        ↓
Runtime Adapter
利用中のAgentへ渡す
```

## Step / GateはActor-neutral

Stepが残ることと、人間が各Stepに残ることは同じではありません。

DeepRailが固定するのは、人間の工程ではなく **仕事が次へ進んでよい条件** です。

## 3軸

- `A0〜A5`: Execution Autonomy
- `EA0〜EA4`: Evaluation Authority
- `S1〜S5`: Approval Strength

3軸を1つの成熟度へ潰しません。

## Evidence

AI self-reportではなく、Machine Check / Observed Behavior / Human Decision等のApproved Evidenceで前進します。

## Reinvestment

毎回の人間介入・Failure・Unknownを、Rule / Skill / Eval / Harnessへ戻します。
