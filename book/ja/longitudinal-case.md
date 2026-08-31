# DeepRail Longitudinal Case — FlowDesk「代理承認」

### FlowDesk「代理承認」拡張（架空ケース）

> **一行の依頼は、AIならすぐ形にできる。だから、その一行の意味まで決まった気にならない方がいい。**

ここから、架空のB2B SaaS「FlowDesk」に代理承認機能を追加する案件を追う。始まりは一行の依頼だ。そこからRelease後の学習まで進むあいだに、認識はずれ、要件は変わり、Agent同士も衝突する。Testが通っているのに足りない場面もあれば、Productionで初めて見える問題も出てくる。

失敗するかどうかだけを見ても、このCaseの意味は分からない。

**失敗やUnknownが現れたとき、それを次の判断に使えるEvidenceへ変え、仕事の切り方・権限・評価・Harnessを更新できるか。**

その後の動きに、AI Nativeな開発の差が出る。

#### Scene 1 — 「代理で承認できるようにしてほしい」

依頼は短かった。

> 「承認者が不在のとき、代理の人が承認できるようにしてほしい。」

従来なら、担当者がいくつか質問し、画面案を作り、APIやDB変更へ進んでいたかもしれない。AIがいると、さらに誘惑が強い。既存Repositoryを読み、現在の承認処理を探し、必要そうな差分を作らせれば、数十分でそれらしい実装案が出る。

実際、最初のAI Researchでも案はすぐに出た。

既存の `Approver` に対して `Proxy Approver` を紐づける。代理期間を持たせる。承認時には、本人か代理人かを判定する。UIには「代理承認」と表示する。Audit Logには実行者を残す。

悪くない。むしろ、ぱっと見れば十分に見える。

問題は、「代理」という言葉を全員が同じ意味で使っていなかったことだった。

Product側が思い浮かべていたのは、休暇中の承認者と同じ権限を一時的に持つ人だった。Compliance側は、金額や申請Categoryによっては代理できないDecisionがあると考えていた。Tenant Admin側は、組織設定として代理者を登録する機能を想像していた。Auditorが知りたいのは、誰がボタンを押したかだけではない。「誰の権限を代行し、どのRuleの下でそのDecisionが有効だったのか」を、後から説明できる必要があった。

同じ「代理」でも、見ている仕事が違っていた。

ここでAIの最初の提案を採用していたら、コードは書けただろう。Testも作れただろう。ただし、そのTestが証明するのは「実装した代理承認が実装どおりに動くこと」であって、「事業が必要としている代理承認を作ったこと」ではない。

Teamは、まず実装を止めた。

止めたといっても、AIを止めたわけではない。AIには既存仕様、過去のTicket、Code、監査関連のDocumentから、`代理`、`承認者`、`Decision Actor`、`Audit` に関係するRule候補と矛盾候補を抽出させた。その結果をDomain Expertと確認し、VocabularyとScenarioを更新した。

AIのResearchは、そのまま答えにはしなかった。AIは探索範囲を広げ、見落としていそうなRuleや矛盾を出す。採用するかどうかは、現在のBusiness MeaningとAccountabilityを持つStakeholderを含めて決める。決まった内容もConversationの中に置き去りにせず、Shared Reality Noteへ戻した。

最初の依頼は、一行のままだった。

しかしTeamが扱う仕事は、もう一行ではなかった。

`代理` とは恒久Roleではない。開始日時と終了日時を持つ。Requesterは自分の申請を承認できない。代理でDecisionした場合、元のApproverと実際のDecision Actorを両方追える必要がある。Tenantをまたいではいけない。Notification失敗とApproval Decisionの成立は分離する。

一方で、まだ決まっていないことも残った。

高額申請でも代理してよいのか。特定Categoryは対象外か。Submission後に代理設定が変わったら、既存Requestにも効くのか。Approval Routeはいつ確定するのか。

ここでUnknownを無理に消さなかった。

**分からないことを、分かったふりで仕様に埋め込む方が危ない。**

Open Questionとして残し、それぞれにDecision Ownerを置いた。

#### Scene 2 — 仕様ができたあとで、要件が変わる

Shared Realityが整い、Scenarioが具体化されると、AIは仕事を進めやすくなった。UI案、APIの変更点、State Transition、Data Model候補、Acceptance Criteriaが短時間で作られ、Teamは同じ具体物を見ながら話せるようになった。

ここまでくると、「最初にちゃんと要件を固めたから、あとは実装するだけ」と考えたくなる。

だが、現場ではそこで終わらない。

Specifyの後、Complianceから追加のRuleが出た。

「一定金額を超える申請は、代理承認を許可しないでほしい。」

最初の打ち合わせでは明示されていなかったRuleだった。しかも単なるUI制御ではない。Approval Decisionそのものの有効性に関わる。

ここで二つの反応があり得る。

一つは、「要件変更だから後から追加する」。もう一つは、「最初に言ってほしかった」と責任の所在を探す。

どちらに寄っても、仕事は前へ進まない。

新しいBusiness Ruleが入ったなら、すでに作ったSpec、Work Breakdown、Test、Delegation Contractのどこまで影響するかを洗い直す。変更そのものは珍しくない。**変更のあと、何を更新すれば再び安全に任せられる状態へ戻れるか。** そこを見た方がいい。

AIにImpact Analysisをさせると、想定より影響が広かった。

BackendのAuthorizationだけではない。UI上で代理承認ボタンを出す条件、API Errorの意味、Boundary Test、Audit Reason、Notification文言、Approval Routeの表示、既存Requestへの適用条件まで影響する。

さらにAIは、既存仕様と新Ruleの間に一つの矛盾を指摘した。

「代理設定は申請後でも変更できる」という現在の案と、「高額申請では代理禁止」を組み合わせたとき、既存Requestが代理可能状態から代理不可へ途中で変化する可能性がある。

人間側では「金額判定を承認時に見ればいい」という初期案が出ていた。しかしAIが既存CodeとState Transitionをたどると、一部のRoute情報がSubmission時にSnapshotされていることが分かった。人間の初期理解より、Machine Evidenceの方が正しかった。

ここでAIと人間の勝ち負けを決めても意味はない。

HumanはBusiness Ruleを知っていた。AIはRepository上の実装事実を広く追えた。両者が別のRealityを持っていた。

Decisionは、「Approval Routeの主体はSubmission時に固定する。ただし代理可否はDecision時にもPolicyを再評価し、禁止条件に該当すれば代理Decisionを拒否する」とした。これにより、既存Routeの整合性を保ちつつ、最新Policyを反映できる。

Decisionを記録したあと、Workも切り直した。

仕様は書いたら終わる文書ではない。

**Realityが変われば、SpecもWorkも委譲条件も変わる。**

#### Scene 3 — Agentを増やしたのに、並列にならない

実装へ進む頃には、仕事はかなり整理されていた。

Frontendでは代理承認表示と操作導線。Backendでは代理権限判定。別のWorkではAudit Record。さらにBoundary Test、Notification、Compatibility Testがある。

AI Agentを複数走らせれば、一気に進みそうに見えた。

Teamは、Frontend、Authorization、Auditの三つを並列に委譲した。

最初の数十分は順調だった。それぞれのAgentがCodeを読み、Testを追加し、変更案を出した。

ところが、統合しようとすると衝突した。

Authorization Agentは、承認主体を表すStateに `actingUserId` を追加していた。Audit Agentは、同じ意味を別のAudit専用Objectに持たせようとしていた。Frontend AgentはAPI Responseへ `proxyApprover` を追加する前提でUIを作っていた。

三つのAgentは、それぞれのTask内では合理的だった。

でも、同じSource of Truth境界を別々に設計していた。

Agent数は三つだった。並列性は三倍ではなかった。

ここでTeamは、一度並列実行を止めた。原因はAgentの性能ではなく、Work Breakdownにあった。独立しているように見えた三つのTaskが、「Decision Actorをどう表現するか」という一つのModel Decisionに依存していた。

先に共通のDecisionを切り出す必要があった。

`Original Approver` と `Acting Approver` をApproval Decisionの共通Modelとして定義し、Audit、API、UIはそこから派生させる。MigrationとCompatibility Boundaryも、そのDecisionに含める。

その上でWork Graphを組み直した。

共通Modelの決定を先に完了し、各Agentへ渡すContextとAcceptanceを固定する。FrontendはPresentationとUser-visible Behavior。AuthorizationはDecision Policy。Auditはappend-orientedなEvidence記録。それぞれのWorkには、変更可能なFile/Module境界、必要Evidence、Rollback可能性を付けた。

二回目の並列実行は、最初よりAgent数を減らした。

それでも全体は速かった。

効いたのは、Agentを増やしたことより仕事の切り方だった。

**独立して終えられる仕事だけを並列にしたからだ。**

並列性は、同時に何体のAgentを起動したかでは決まらない。片方の判断をもう片方が暗黙に上書きしないこと。各Workが自分のAcceptanceを持つこと。失敗しても局所的に戻せること。そして結果を独立して検証できること。

この条件が揃って、ようやくParallel Executionが本当の速度になる。

#### Scene 4 — Testは全部通った。それでも足りなかった

数日後、代理承認の主要実装が揃った。

Unit TestはGreen。Integration TestもGreen。Cross-tenantのAuthorization Testも通った。代理期間の開始前・終了後も拒否される。Requesterによる自己承認も防げている。二重承認を送ってもOutcomeは一度しか適用されない。

技術的には、かなり安心できる状態に見えた。

そこでScenario Verificationを行った。

「Approver Aが休暇中。Proxy Approver Bが、Aの代わりに申請を承認する。後日Auditorが、そのDecisionを確認する。」

操作自体は成功した。

しかしAuditor向け画面を見ると、「Bが承認」としか表示されていなかった。

APIのAudit Responseにも実行者Bはある。しかし「Aの代理としてDecisionした」という関係が、Humanが追える形で十分に表現されていない。内部Logには元ApproverのIDが残っていたが、通常のAudit導線からは見えなかった。

TestはGreenだった。

なぜならTestは、「代理人が承認できる」「Audit Recordが作られる」という実装上のAcceptanceを確認していたからだ。

Business側が必要としていたのは、「後から第三者が、誰の権限でDecisionされたか説明できる」ことだった。

ここでCriteria自体の曖昧さも表に出た。

Engineerは「元Approver IDは保存しているので要件は満たしている」と考えた。Auditorは「通常画面から追えないなら監査可能とは言えない」と考えた。AI Evaluatorは、Specificationに「Original ApproverとActing ApproverをAuditできる」とあるため、どちらの解釈もあり得ると判定した。

この時点では、AIとHumanのどちらが正しいとも言えなかった。

Criteriaが足りなかった。

TeamはAcceptanceを更新した。

「Audit権限を持つUserが、通常のAudit画面とAPIから、Original Approver、Acting Approver、Delegation Rule、Decision時刻を一続きで確認できること。」

このCriteriaに対して、User-visible Verification Procedureを作り直した。

画面を開く。対象申請を選ぶ。代理Decisionを確認する。OriginalとActingの両Identityが表示される。APIでも同じRelationが取得できる。Audit Storeにも対応するEvidenceがある。

ここまで来ると、EvidenceはTest結果の一覧だけでは足りなくなる。

Evidenceは、次の人が判断するためのInterfaceになった。

Code Diffを最初から全部読まなくても、「このOutcomeは何によって証明されているか」「どこがまだUnknownか」「どのDecisionだけHumanへ戻っているか」が見える。

**Codeは重要なArtifactである。だが、判断の入口までCodeにしてしまう必要はない。**

必要なところでCodeへ降りればいい。

#### Scene 4.5 — 評価者を増やしても、真実にはならない

Acceptanceを更新したあと、TeamはEvaluationのやり方も見直した。

一つのAI Evaluatorだけに「この実装は要件を満たしているか」と聞けば、速い。だが、実装Agentと同じContext、同じ前提、似たModelで評価しているなら、同じ思い違いを共有する可能性がある。

そこで評価を分けた。

Policy RuleはdeterministicなCheckerで見る。User-visible BehaviorはScenario Runnerで見る。Audit Semanticsは別ContextのEvaluatorに確認させる。Security BoundaryはAuthorization Testで反証する。高Riskの意味判断だけ人へ戻す。

結果は、きれいには揃わなかった。

Rule CheckはPass。ScenarioもPass。しかしAudit Evaluatorは、「代理関係の表示は確認できるが、Delegation Ruleの有効期間を画面上で追えない」と指摘した。一方、Human Reviewerの一人は「そこまで通常画面に出す必要はない」と考えた。

ここで多数決を取れば、二対一、三対一という数字は作れる。

でも、その数字に意味があるとは限らない。

Rule CheckerとScenario Runnerは、そもそもAudit画面の説明可能性を評価していない。HumanとAI Evaluatorの不一致も、片方の能力不足ではなく「Auditorがどこまで一画面で追えるべきか」というCriteriaの不足かもしれない。

TeamはDisagreementをFailureとして消さず、分類した。

実装Errorなのか。Evaluator Errorなのか。Criteriaが曖昧なのか。Evidenceが足りないのか。Environmentが違うのか。それとも、まだ誰も気づいていないUnknownなのか。

今回の結論は `Ambiguous Criteria` だった。

Auditorへ確認し、「一画面にすべてを表示する必要はないが、通常導線からDelegation Ruleの有効期間へ二操作以内で到達できること」をAcceptanceへ追加した。

人数を増やしたこと自体が効いたわけではない。

**違うFailure Modeを持つ評価を組み合わせ、不一致を捨てずに次のQuestionへ変えたから、Criteriaが強くなった。**

Independent Evaluationで見たいのは、何体のAIが同じ答えを返したかではない。同じ間違いを一緒に見逃しにくいEvaluation Systemになっているかだ。

#### Scene 5 — AIに見せられないDataがある

Verificationを強くしようとすると、別の問題が出た。

Production相当の申請Dataを使えば、複雑なApproval Routeや代理設定を再現しやすい。しかしCoding Agentへ実Dataを自由に渡すことはできない。Tenantごとの組織情報や申請内容には、扱いを制限すべき情報が含まれている。

ここでPermissionを邪魔者と決めつけると、設計を誤る。

制約は消えない。

ならば、その制約の内側で仕事を完遂できるVerificationを作る。

Teamは、Production DataのCopyを諦め、必要な性質だけを持つSynthetic Fixtureを作った。複数Step、Budget Owner、代理期間、禁止Category、Cross-tenant Attempt、Notification Failure、二重Requestを再現できる小さなDatasetである。

AIにはFixture GeneratorとScenario Runnerを作らせた。実Dataそのものではなく、「どの性質が検証に必要か」をContextとして渡す。

この変更には副作用もあった。

Fixtureが現実を十分に代表しているのか、という新しい問いが生まれる。

そこで、Productionの値を持ち出さずに分布やSchema特性だけを確認できる統計・Metadata Checkを別に置き、Fixtureが主要なShapeを外していないことを定期確認する設計にした。

Permissionを緩めたのではない。

Verificationを、Permission Boundaryの内側で成立する形に作り直した。

**今すぐ任せられない仕事があっても、それだけで「AIには任せられない仕事」と決める必要はない。今のPermissionのままでは成立しないだけかもしれない。**

そこには大きな違いがある。

#### Scene 6 — 再現しないFailureは、Environmentの問題だった

Integration環境で、代理期間のBoundary Testがときどき失敗した。

Localでは再現しない。別のAgentが再実行すると通る。Test Codeを見ても、明らかな不具合はない。

最初、人間側ではRace Conditionが疑われた。AI Agentも最初の分析ではTime Handlingの可能性を高く見積もった。

しかしRunごとのEnvironment StateとEvidenceを並べると、別の共通点が見つかった。

失敗するRunだけ、Shared Integration環境に前のTestが残した代理設定が存在していた。Cleanupが完全ではなく、同じUserを使う別ScenarioへStateが漏れていた。

ここでは、Humanの最初の仮説よりMachine Evidenceが正しかった。

ここで競う意味はない。

Environment Version、Fixture ID、Seed、Test開始前State、Cleanup ResultがEvidenceとして残っていたから、Failureを比較できた。

TeamはPreflightとCleanup CheckをVerification Procedureへ追加した。Test開始前に期待Stateを確認し、終了時にはLeaseしたFixtureだけを確実に破棄する。共有環境で競合するWorkには一時的なLeaseを持たせ、失敗時はEnvironment FailureとProduct Failureを分けてRouteする。

「もう一回実行したら通った」で終わらせない。

再現しないFailureほど、Evidenceがいる。

そしてEnvironment Stateも、実装とは別の背景情報ではない。

**Outcomeを証明する条件の一部である。**

#### Scene 7 — Release前、人間のGateが戻る

技術的なEvidenceが揃い始め、Release Packetが作られた。

主要Scenario、Regression、Authorization、Audit、Compatibilityの結果。既知のRisk。Rollback手順。Production Verification。Agentが行った重要DecisionとDeviationもDecision Trailから要約されている。

それでも、一つだけ決まっていないことがあった。

Audit画面で、代理Decisionをどう表現するか。

候補は二つあった。

「BがAの代理として承認」

あるいは、

「Aの承認権限に基づきBが承認」

意味は近い。しかし法務・監査上、どちらの表現が適切かは単なるUI Copyではなかった。誰がDecision Ownerとして責任を持つのかというSemanticsに関わる。

AIは過去の文言、社内用語、一般的なAudit表現を比較し、候補と利点・欠点を出した。

しかし最終DecisionはHuman Gateへ戻した。

AIが文章を書けないからではない。

このWork Classでは、現時点のPolicyとAccountability上、最終的な意味決定をAIへ委譲する条件がまだ揃っていなかったからだ。

ここが大事である。

Human Gateは、AI Native化に失敗した証拠ではない。

逆に、何でも人間へ戻すのも違う。

**どのDecisionを、なぜHuman / Policy側に残しているのか説明できること。**

Release前のGateは「人が不安だから」ではなく、Decision Rights、Risk、Evidence、Accountabilityに基づいて置かれた。

そしてこのDecisionが将来Policy化され、十分にCalibrationできれば、同じ種類の判断がずっとHuman-onlyである保証もない。

境界は固定しない。

#### Scene 8 — Productionで旧Clientが壊れる

Releaseは承認された。

段階的にFeatureを有効化し、Production Verificationも開始した。新しいUIでは代理承認が動く。Auditも見える。主要APIも正常だった。

ところが、あるTenantから問い合わせが入った。

既存の連携Clientで、承認済み申請の一部が「未処理」のように表示される。

新Featureそのものではなく、Compatibilityの問題だった。

代理承認を表現するため、API Responseに新しいDecision Actor情報を追加した際、ある旧ClientがStatus判定で想定外の分岐へ入っていた。API Contract上は追加Fieldを無視できる設計のはずだったが、そのClientはResponse Shapeを独自に厳密比較していた。

Repository内のTestはすべてGreenだった。

新しいClientも正常だった。

それでも、Production Outcomeは壊れた。

TeamはFeature Flagで対象Tenantの代理承認を止め、旧Clientの影響範囲を確認した。全面Rollbackではなく、変更のReversibilityとBlast Radiusを見て限定停止を選んだ。

ここでRelease Evidenceが役に立った。

どのVersionが出ているか。どのTenantでFeatureが有効か。旧ClientがどのAPI Pathを使っているか。新Field追加と発生時刻が一致するか。代理Decision自体のData Integrityは保たれているか。

Incident対応は、闇雲なCode探索から始まらなかった。

Evidenceから、壊れているOutcomeを狭めていった。

Fixは、旧Client向けのCompatibility LayerとContract Testを追加する形になった。Production Verificationにも、代表的な既存ConsumerでResponseを確認するStepを足した。

Mergeした時点では、仕事は終わっていなかった。

Releaseした時点でも、まだ終わっていなかった。

**利用者の世界でOutcomeが成立し、失敗したときに戻せるところまでがDeliveryである。**

#### Scene 9 — Retroで「次から気をつける」を書かない

Incidentが収束した後、Retroを行った。

ありがちな結論なら、こうなる。

「既存Clientへの影響確認を徹底する。」

「Audit要件は早めに確認する。」

「Agent間で同じFileを触らないよう注意する。」

どれも間違いではない。

ただし、その文章を読まなかった次のAgent、次のTeam、半年後の新しいMemberには効かないかもしれない。

そこで一つずつ、「次のExecutionを変えるStructureへできないか」を見た。

高額申請で代理を禁止するRuleは、Business Scenario TestとPolicy Checkへ入れた。

Original ApproverとActing Approverの関係は、API・Audit Store・UIのContractとしてFixtureとVerification Procedureに組み込んだ。

Shared Integration環境のState漏れは、Preflight、Lease、Cleanup Checkへ変えた。

旧Client Compatibilityは、代表Consumerを使ったContract TestとRelease Gateへ入れた。

並列Conflictについては、「同じFileを触るな」という注意ではなく、Work Breakdown時にShared Model DecisionとIndependent Workを分けるChecklistへ入れた。

そして、Decision Trailからも一つ学びが残った。

途中で高額申請Ruleが追加されたとき、AIがImpact Analysisを行ったことで、UI、API、Audit、Testへの波及を早く見つけられた。そこでChange時の標準手順へ、「Decision変更時は影響するAcceptance / Evidence / Delegation Contractを再評価する」を追加した。

学びはDocumentにも残した。

でも、Documentだけにはしなかった。

**組織が学習したと言えるのは、次に同じ条件が来たとき、Executionが変わるときだ。**

#### Scene 10 — 次のTeamは、同じ失敗を最初から経験しない

数週間後、別Teamが別のWorkflowに「一時的な代理Decision」を追加することになった。

Domainは同じではない。扱う対象も違う。

だからFlowDeskのCodeをそのままCopyして終わり、という話ではない。

それでも、そのTeamはゼロから始めなかった。

Repositoryには、代理Decisionを考えるときのDomain Questionがあった。Decision Actorの表現Patternがあった。Delegation ContractのTemplateがあった。Synthetic Fixtureの作り方があった。Original / Acting Identityを検証するProcedureがあった。Environment Preflightがあった。Compatibility Gateがあった。

そして何より、「AIへどこまで任せてよいか」をModel名や個人の感覚だけで決めなくてよかった。

Work Class、Risk、Evidence Reliability、Failure Detectability、Reversibility、Permission、Accountabilityを見ながらOperating Profileを選べる。

最初のTeamが経験したFailureは消えていない。

過去に起きたこととして残っている。

ただし、同じFailureを次のTeamが同じ形で踏む必要はなくなった。

ここまで来て、ようやく個人のAI活用が組織能力へ変わり始める。

最初にあった依頼へ戻ろう。

> 「承認者が不在のとき、代理の人が承認できるようにしてほしい。」

AIなら、この一文からでもCodeを書き始められる。

それ自体は、もう珍しい能力ではない。

難しいのは、その一文を正しい仕事へ変えること。分からないものをUnknownとして残すこと。独立して任せられる単位へ分けること。必要な権限を渡し、越えてはいけない境界を決めること。成果をEvidenceで評価すること。人間へ戻すDecisionを理由付きで残すこと。Productionで失敗したときに戻れること。そして学びを次のExecutionへ埋め込むことだ。

最後に残るのは、Promptの巧さだけではない。意味を揃え、分からないものを残し、仕事を分け、権限を渡し、Evidenceで確かめ、失敗から次の実行を変える。

**AIが働くなら、そのAIが仕事を最後まで成立させられる条件も一緒に作る。**

そして、その設計を一度きりの工夫で終わらせず、次の人、次のAgent、次のTeamが再利用できる形へ戻していく。

FlowDeskのCaseが成功した理由を一つに絞るなら、AIが賢かったからではない。

失敗するたびに、仕事の仕組みの方を賢くしたからである。
