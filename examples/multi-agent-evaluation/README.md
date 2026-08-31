# Golden Path — ExecutorとEvaluatorを分離する

Verify Gateでは `independent_required: true`。同じExecutorのself-reportだけではPASSしません。

このExampleは、Execution Agent → Independent Evaluation → DecisionというActor-neutral Flowを示します。
