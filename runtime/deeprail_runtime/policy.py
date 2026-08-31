
def _num(v, prefix):
    if not v.startswith(prefix):
        raise ValueError(v)
    return int(v[len(prefix):])


def policy_summary(profile):
    a=profile["deeprail"]["autonomy"]
    return {"execution":a["execution"],"evaluation":a["evaluation"],"approval":a["approval"],"risk":profile["deeprail"].get("risk_profile","medium")}


def can_agent_execute(profile):
    return _num(profile["deeprail"]["autonomy"]["execution"],"A") >= 2


def can_ai_evaluate(profile):
    return _num(profile["deeprail"]["autonomy"]["evaluation"],"EA") >= 1


def can_ai_issue_go(profile):
    ea=_num(profile["deeprail"]["autonomy"]["evaluation"],"EA")
    s=_num(profile["deeprail"]["autonomy"]["approval"],"S")
    risk=profile["deeprail"].get("risk_profile","medium")
    return ea >= 3 and s <= 3 and risk in {"low","medium"}


def can_policy_issue_go(profile):
    ea=_num(profile["deeprail"]["autonomy"]["evaluation"],"EA")
    s=_num(profile["deeprail"]["autonomy"]["approval"],"S")
    risk=profile["deeprail"].get("risk_profile","medium")
    return ea >= 4 and s <= 3 and risk in {"low","medium"}


def decision_allowed(profile, value, actor):
    if value != "pass":
        return True, "non-GO decision allowed"
    if actor == "human":
        return True, "human GO allowed by current project accountability"
    if actor == "ai":
        return (can_ai_issue_go(profile), "AI GO allowed" if can_ai_issue_go(profile) else "current EA/S/Risk policy does not permit AI GO")
    if actor == "policy":
        return (can_policy_issue_go(profile), "policy GO allowed" if can_policy_issue_go(profile) else "current EA/S/Risk policy does not permit policy GO")
    return False, "unknown decision actor"


def transition_allowed(profile, work, target, actor):
    current=work["current_workflow"]
    if current=="execute" and target=="verify" and actor=="ai" and not can_agent_execute(profile):
        return False, "execution autonomy does not permit AI-owned execution"
    if current=="verify" and actor=="ai" and not can_ai_evaluate(profile):
        return False, "evaluation authority does not permit AI-owned evaluation transition"
    if current=="decide":
        decisions=[d for d in work.get("decisions",[]) if d.get("workflow")=="decide"]
        if not decisions:
            return False, "decide transition requires an explicit decision"
        last=decisions[-1]
        allowed,reason=decision_allowed(profile,last["value"],last["actor"])
        if not allowed:
            return False,reason
        if last["value"]=="retry" and target!="execute":
            return False,"retry must return to execute"
        if last["value"]=="pass" and target not in {"reinvest"}:
            return False,"pass must advance to reinvest"
    return True,"allowed"
