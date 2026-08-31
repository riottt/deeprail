
from .workflow import load_workflow

NON_SELF_REPORT_TYPES = {"observed_behavior","machine_check","human_decision","independent_evaluation","other"}


def workflow_evidence(work, workflow_name=None):
    name = workflow_name or work["current_workflow"]
    return [e for e in work.get("evidence",[]) if e.get("workflow") == name]


def evaluate_evidence_policy(workflow, work):
    policy = workflow.get("evidence_policy") or {"min_count":0}
    ev = workflow_evidence(work, workflow["id"].replace("deeprail-", ""))
    failures=[]
    min_count=int(policy.get("min_count",0))
    usable=[e for e in ev if e.get("result") != "fail"]
    if len(usable) < min_count:
        failures.append(f"requires at least {min_count} usable evidence item(s); found {len(usable)}")
    if not policy.get("allow_self_report",False):
        non_self=[e for e in usable if e.get("type") != "self_report"]
        if min_count and not non_self:
            failures.append("executor self-report cannot satisfy the evidence gate")
    for required in policy.get("required_types",[]):
        if not any(e.get("type") == required and e.get("result") != "fail" for e in ev):
            failures.append(f"missing required evidence type: {required}")
    for group in policy.get("any_of",[]):
        if group and not any(e.get("type") in group and e.get("result") != "fail" for e in ev):
            failures.append("requires one of: " + ", ".join(group))
    if policy.get("verified_required") and not any(e.get("verified") for e in usable):
        failures.append("requires at least one verified evidence item")
    if policy.get("independent_required") and not any(e.get("independent") for e in usable):
        failures.append("requires independent evaluation evidence")
    if any(e.get("result") == "fail" for e in ev) and not policy.get("allow_failed_evidence",False):
        failures.append("failed evidence is unresolved")
    return {
        "pass": not failures,
        "workflow": workflow["id"],
        "policy": policy,
        "evidence_count": len(ev),
        "usable_count": len(usable),
        "failures": failures,
    }


def evaluate_gate(root, work):
    wf=load_workflow(root,work["current_workflow"])
    return evaluate_evidence_policy(wf,work)
