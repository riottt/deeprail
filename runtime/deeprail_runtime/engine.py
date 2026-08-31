
from .state import load_work, save_work
from .policy import transition_allowed
from .workflow import load_workflow
from .gates import evaluate_gate
from .audit import append_event
import datetime


def advance(repo_root, project, profile, work_id, target, actor="human"):
    work=load_work(project,work_id)
    current=load_workflow(repo_root,work["current_workflow"])
    if target not in current.get("next",[]):
        raise ValueError(f"{current['id']} cannot transition to {target}")
    gate=evaluate_gate(repo_root,work)
    if not gate["pass"]:
        raise PermissionError("evidence gate failed: " + "; ".join(gate["failures"]))
    allowed,reason=transition_allowed(profile,work,target,actor)
    if not allowed:
        raise PermissionError(reason)
    old=work["current_workflow"]
    work["current_workflow"]=target
    event={"event":"transition","from":old,"to":target,"actor":actor,"reason":reason,"at":datetime.datetime.now(datetime.timezone.utc).isoformat()}
    work["history"].append(event)
    save_work(project,work)
    append_event(project,work_id,{"type":"transition",**event})
    return work
