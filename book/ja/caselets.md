# DeepRail Before / After Caselets

## Before / After Caselets

> **Purpose:** 各Partで、そのPartの概念を定義する前に、読者が「自分の現場でも起きている」と感じられる短いSceneを置く。Caseletは成功談ではなく、従来のやり方にAIを足しただけではどこが詰まるのか、その詰まりをDeepRailがどう見直すのかを示す。
>
#### Caselet I — コードは速くなった。でも、仕事は終わらない。

最初の数日は、かなりうまくいっているように見える。

DeveloperがIssueをAIへ渡す。数分後には実装案が出る。Testも追加される。以前なら半日かかっていた変更が、一時間もしないうちにPull Requestになる。Teamの空気も変わる。「これなら開発速度をかなり上げられる」と誰もが思う。

ところが、一週間ほどすると別の数字が増え始める。Review待ちのPull Requestである。

一人のDeveloperが一日に作れる変更は増えた。AIを使う人が増えれば、さらに増える。だが、Merge前には人が仕様を読み、Diffを確認し、Testの意味を考え、影響範囲を頭の中で再構成している。生成側だけが速くなった結果、確認側に仕事が集まった。

ここで「AIの出力品質をもっと上げれば解決する」と考えたくなる。もちろん品質は大事だ。ただ、問題はそれだけではない。

人が最後にすべてを読み直さなければ前へ進めないなら、AIが速くなるほど確認側に仕事が集まる。

コードを書く方法は変わった。仕事を受け止める方法は、まだ変わっていなかった。

この時点では、解決策まで先回りしない。まず、**速くなった工程の次に新しい詰まりが生まれた**ことだけを掴む。何を人が見て、何をEvidenceに任せるかは、その先で考える。

---

#### Caselet II — 研修は盛り上がった。翌月、やり方は元に戻った。

全社AI研修を開いた。参加者は多かった。Promptの書き方を教え、便利な使い方を実演し、その場では「明日から使えそう」という反応も多い。

一か月後、現場を見る。

よく使っている人はいる。ほとんど使っていない人もいる。あるTeamではAIがTestまで書いているのに、別のTeamでは文章の要約だけに使われている。成功例を共有しても、「その人だからできる」「うちのRepositoryでは無理」と返ってくる。

研修自体が失敗だったわけではない。入口としては必要だった。

ただ、Toolの使い方を教えたことと、組織がAIへ仕事を任せられるようになったことは同じではない。

ここで必要なのは、優秀な利用者のPromptを配ることではない。実際の仕事を一つ選び、Teamで任せ、失敗し、その失敗から必要なContext、Rule、Test、Permission、Gateを見つけることである。

たとえば実案件の小さなFeatureを対象にする。AIへ任せる範囲を決める。どこで止まったかを見る。仕様不足ならContext Assetへ戻す。毎回同じ不具合を出すならTestやCheckerへ変える。人が判断している箇所ならDecision Criteriaを言語化する。

こうして残ったものは、個人のコツではない。

```text
Real Theme
→ Friction
→ Rule / Context / Evidence
→ Harness / Standard
→ Training Material
```

次のTeamは、最初のTeamと同じ失敗を一から経験しなくてよくなる。

それが起きたとき、AI研修は初めて組織能力へ変わり始める。

**「使える人を増やす」だけでは足りない。「任せ方を再現できる組織」を作る。**

---

#### Caselet III — 一時間の会議で決まったはずなのに、三日後に意味が崩れた。

FlowDeskに「代理承認」を追加する打ち合わせをした。

Product側は「承認者が休みなら代理の人が承認できればいい」と説明する。Engineerも理解したつもりになる。議事録には「代理承認機能を追加」と残る。AIへ渡せる程度には要件がまとまったように見える。

三日後、Prototypeを見たCompliance担当が言う。

「この代理って、高額申請でも使えるんですか？」

別の人が続ける。

「そもそも、申請を出した後に代理設定が変わったら、今進んでいる申請にも効くんですか？」

会議で決まっていなかったのではない。**同じ言葉を、違う意味で理解したまま会議が終わっていた**のである。

従来なら、このズレは実装後のReviewや受入試験で見つかることがある。AIを入れると、もっと厄介になる。曖昧な要求でも、AIはかなり速くそれらしい形へ変えてしまうからだ。

会議を増やすだけでは、同じ言葉のズレは残る。

「代理」という言葉をScenarioへ落とす。誰が、誰の代わりに、どの期間、どの金額、どのCategoryまでDecisionできるのか。UIを見せる。API状態を置く。例外を並べる。決まっていないものはOpen Questionとして残し、Decision Ownerを付ける。

すると議論の中心が変わる。

「この文章で伝わりますか」ではない。

**「このScenarioを見たとき、私たちは同じOutcomeを想像しているか」**になる。

要求定義の目的は、きれいな文書を完成させることではない。HumanとAIが次の仕事を、推測ではなく同じRealityから始められる状態を作ることである。

---

#### Caselet IV — Leadが優秀なほど、TeamがLeadの速度になる。

AIを使い始めてから、Team Leadの仕事が減ると思っていた。

実際には逆だった。

朝、複数のAgentが作った変更を確認する。昼にはDeveloperから「このTaskはどちらを優先しますか」と質問が来る。別のAgent同士が同じSchemaを触ってConflictしている。Security上の例外判断も待っている。夕方にはRelease可否の相談が来る。

実装者の手は速くなった。だから、判断がLeadへ集まる速度も上がった。

Leadが全部分かっていて、全部判断できるTeamは、一見強い。だが、そのTeamのCapacityはLead一人のAttentionから抜け出せない。

ここで変えるべきなのは、Leadをもっと効率化することではない。

どのDecisionを誰が持つのかを分ける。Work同士のDependencyを見えるようにする。既知のRuleで決められるものはPolicyへ落とす。Evidenceが十分ならAI側で次工程へ進める。人へ戻すのは、Riskが高いもの、Criteriaが曖昧なもの、Accountabilityを伴うもの、例外だけにする。

するとLeadの仕事は「すべてを処理する」から変わっていく。

```text
Assign everything      → Work Graphを整える
Review everything      → Evaluation条件を設計する
Answer everything      → Decision Rightsを明確にする
Watch everything       → Exceptionを扱う
```

もちろん、人が不要になるわけではない。

むしろ人が見るべきものを選べるようになる。

**強いLeadとは、すべての仕事を抱えられる人ではない。自分がいなくても成立するDecision Systemを増やせる人である。**

---

#### Caselet V — Agentを四つに増やしたら、四倍速くなると思っていた。

Featureを四つのTaskへ分け、四つのAgentを同時に動かした。

Frontend、Backend、Database、Test。見た目にはきれいに分かれている。開始直後は速い。各Agentが別々に成果物を返してくる。

問題はIntegrationで起きた。

Backend AgentはStatusを追加した。Database Agentも同じStateを別の名前で追加した。Frontend Agentは古いResponse Shapeを前提にUIを作った。Test Agentは自分が受け取ったSpecには忠実だが、他の三つの変更後の状態を知らない。

四つの仕事が並んでいたのではない。**四つのAgentが、同じ境界を別々の理解で変更していた。**

Agentを増やせることと、仕事を安全に並べられることは別だ。

Taskの数より先に、その仕事を本当に分けられるかを見る。

このWorkは別のBranchやWorktreeで隔離できるか。Source of Truthは一つに決まっているか。Acceptanceは単独で判定できるか。他のTaskを壊さずRetryできるか。失敗したとき、そのWorkだけ戻せるか。

これらが揃って初めて、Workは安全に並べられる。

逆に、共有Schemaの変更のように境界が強く結合しているなら、先にContractを固定するか、順序をつける。Agentを待たせることが遅いのではない。**検証不能な同時実行を増やして、最後に人間が統合作業をする方が遅い。**

並列性は計算資源から生まれない。

仕事を、独立して実行し、独立して証明できる単位へ変えたところから生まれる。

---

#### Caselet VI — CIは全部Greenだった。それでもReleaseを止めた。

FlowDeskの代理承認Featureは、CIを通過した。

Unit TestはGreen。Integration TestもGreen。Static Checkにも問題はない。通常承認のRegressionも通っている。数字だけを見れば、Releaseしてよさそうだった。

最後のBusiness Scenarioで、Auditor役の人が一つ質問した。

「半年後、この記録だけを見て、誰が誰の代理として承認したか分かりますか？」

画面上ではProxy Approverの名前が表示される。だが、Audit Recordには実際に操作した人しか残っていない。元のApproverとの代理関係がEvidenceとして再構成できなかった。

Codeは動いている。Testも通っている。

それでもOutcomeは証明できていない。

ここで「Test項目をもっと増やそう」だけで終えると、本質を外す。必要なのは、何を正しいと主張しているのかを分け、そのClaimごとに反証できるEvidenceを持つことだ。

通常Flowを壊していないか。Proxy期間外を拒否するか。Tenantを越境しないか。誰の代理か追跡できるか。旧Clientが壊れないか。Productionでも同じ条件が成立するか。

それぞれ必要なEvidenceは違う。

Release判断も、CIの一つのGreen/Redへ押し込めない。Machine Evidenceで十分なところは自動で進める。Business意味やAccountabilityを含むDecisionには必要なEvidenceをまとめてHuman Gateへ返す。Productionでは実際のBehaviorをもう一度確認し、Rollback条件も事前に持つ。

**品質は「何個Checkしたか」ではない。次へ進むためのClaimが、必要なEvidenceで成立しているかで決まる。**

---

#### Caselet VII — Ruleを足し続けたら、誰も全体を説明できなくなった。

AIが一度間違えるたびに、Ruleを一つ追加した。

「このDirectoryは触らない」
「Migration時はこの手順を使う」
「Testを必ず実行する」
「このAPIではこのFieldを変更しない」

半年後、Repositoryには大量のInstructionが残った。Agentは以前より賢くなっているはずなのに、作業開始時に読むContextは増え、Rule同士の矛盾も起きる。古い制約が残り、新しいToolでは意味を失った指示もある。

守りを増やした結果、仕事がしづらくなっていた。

ここで起きているのは「Ruleが足りない」問題ではない。

何のFailureを防ぐためのControlなのかが分からなくなっている。

Harnessを部品一覧から作り始めると、何のためのRuleか分からなくなりやすい。実際のDeliveryで起きたFailureから辿る方がいい。

たとえば「Migrationで本番互換性を壊した」というFailureなら、文章で注意するだけが答えではない。Schema Contract Testで検出できるならTestへ落とす。禁止操作ならPermissionへ落とす。Merge前に確実に止められるならGateへ落とす。人の判断が必要ならDecision Surfaceとして残す。

逆に、役目を終えたRuleは消す。

```text
Failure
→ Detectability
→ 最も弱く、確実に効くControl
→ Evidence
→ 継続評価
```

Harnessは、AIを縛る規則の山ではない。

**AIが仕事を完遂できるように、必要な境界だけを実行系へ埋め込んだもの**である。

---

#### Caselet VIII — 「あの人のやり方」を全社展開した瞬間に、再現しなくなった。

あるTeamでAI Native開発がうまくいった。

LeadはAIへの仕事の渡し方がうまい。Repositoryの事情も詳しい。どの変更なら任せられるか、どこで人が見るべきかを感覚的に分かっている。Releaseも速くなった。

会社はその成功を横展開しようとする。

勉強会を開く。LeadのPromptを共有する。録画を配る。他Teamにも「同じようにやってみてください」と伝える。

ところが再現しない。

別Teamには違うSecurity制約がある。Legacy Codeがある。Testの強さも違う。Decision Rightsも違う。最初のTeamではLeadの頭の中にあった判断条件が、共有されたPromptには入っていなかった。

成功者をコピーしようとしたことで、成功を支えていた構造が抜け落ちた。

全社展開で移すべきものは、やり方そのものではない。

何を任せたか。どのEvidenceを採用したか。どこでHuman Gateを残したか。何が失敗し、その学びをどのRule / Test / Harnessへ変えたか。どの条件なら別Teamでも使えるか。

そこまで外部化されて、初めて移植できる。

```text
Individual Practice
→ Team Practice
→ Reproducible Artifact
→ Standard / Harness / Training
→ Governance
→ Other Teams
```

もちろん、全Teamを同じOperating Profileへ揃える必要はない。RiskもEnvironmentも違うからだ。

全Teamへ同じ答えを配る必要はない。**答えを選ぶ条件と、結果から学ぶ仕組み**が共通なら、Localな違いを残せる。

個人の成功が組織能力へ変わるのは、成功者がいなくても、別のTeamが同じ原則から自分たちのやり方を再構成できたときだ。

---

### 0D.8.2 Caselet Completion Status
