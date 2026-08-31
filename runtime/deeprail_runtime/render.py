
LABELS = {
 "ja":{"purpose":"目的","inputs":"入力","outputs":"出力","evidence":"必要なEvidence","exit":"終了条件","decision":"Decision Rights","failure":"戻り先","next":"次"},
 "en":{"purpose":"Purpose","inputs":"Inputs","outputs":"Outputs","evidence":"Required Evidence","exit":"Exit Condition","decision":"Decision Rights","failure":"Failure / Return Path","next":"Next"}
}


def localized(workflow, language):
    if language=="en": return workflow
    projection=(workflow.get("i18n") or {}).get(language,{})
    merged=dict(workflow); merged.update({k:v for k,v in projection.items() if k in {"purpose","inputs","outputs","required_evidence","exit_condition","decision_rights","failure_return_path","next","agent_instructions"}})
    return merged


def render_workflow(workflow, language):
    if language not in LABELS: raise ValueError(language)
    wf=localized(workflow,language); L=LABELS[language]
    out=[f"# {workflow['id']}",f"## {L['purpose']}",wf['purpose']]
    for key,label in [("inputs",L["inputs"]),("outputs",L["outputs"]),("required_evidence",L["evidence"]),("failure_return_path",L["failure"]),("next",L["next"])]:
        out += [f"## {label}"] + [f"- {x}" for x in wf.get(key,[])]
    out += [f"## {L['exit']}",wf["exit_condition"],f"## {L['decision']}",wf["decision_rights"]]
    return "\n".join(out)+"\n"
