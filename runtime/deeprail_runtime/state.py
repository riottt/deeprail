
from pathlib import Path
import json, uuid, datetime
from .audit import append_event

FLOW = ["start","discover","shape","align","specify","decompose","execute","verify","decide","reinvest"]


def _now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def state_dir(project):
    p = Path(project)/".deeprail"/"state"
    p.mkdir(parents=True, exist_ok=True)
    return p


def work_path(project, work_id):
    return state_dir(project)/f"{work_id}.json"


def new_work(project, title, intent):
    work_id = "DRW-" + uuid.uuid4().hex[:10]
    data = {
        "id": work_id,
        "title": title,
        "intent": intent,
        "current_workflow": "start",
        "status": "active",
        "artifacts": [],
        "evidence": [],
        "decisions": [],
        "history": [{"event":"created","workflow":"start","at":_now()}],
        "reinvestment": []
    }
    save_work(project, data)
    append_event(project, work_id, {"type":"work_created","workflow":"start","title":title,"intent":intent})
    return data


def load_work(project, work_id):
    p=work_path(project,work_id)
    if not p.exists():
        raise FileNotFoundError(work_id)
    return json.loads(p.read_text(encoding="utf-8"))


def save_work(project, data):
    work_path(project,data["id"]).write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")


def add_artifact(project, work_id, kind, location, description=""):
    data=load_work(project,work_id)
    item={"id":"DRA-"+uuid.uuid4().hex[:8],"workflow":data["current_workflow"],"kind":kind,"location":location,"description":description,"at":_now()}
    data["artifacts"].append(item)
    data["history"].append({"event":"artifact","workflow":data["current_workflow"],"artifact_id":item["id"],"at":_now()})
    save_work(project,data)
    append_event(project,work_id,{"type":"artifact_added",**item})
    return item


def add_evidence(project, work_id, evidence_type, description, location=None, verified=False, actor="human", independent=False, result="pass"):
    data=load_work(project,work_id)
    ev={
        "id":"DRE-"+uuid.uuid4().hex[:8],
        "workflow":data["current_workflow"],
        "type":evidence_type,
        "description":description,
        "location":location,
        "verified":bool(verified),
        "actor":actor,
        "independent":bool(independent),
        "result":result,
        "at":_now(),
    }
    data["evidence"].append(ev)
    data["history"].append({"event":"evidence","workflow":data["current_workflow"],"evidence_id":ev["id"],"at":_now()})
    save_work(project,data)
    append_event(project,work_id,{"type":"evidence_added",**ev})
    return ev


def set_decision(project, work_id, value, actor, reason):
    data=load_work(project,work_id)
    d={"id":"DRD-"+uuid.uuid4().hex[:8],"value":value,"actor":actor,"reason":reason,"workflow":data["current_workflow"],"at":_now()}
    data["decisions"].append(d)
    data["history"].append({"event":"decision","decision_id":d["id"],"decision":value,"actor":actor,"at":_now()})
    save_work(project,data)
    append_event(project,work_id,{"type":"decision_recorded",**d})
    return d


def add_reinvestment(project, work_id, proposal, evidence):
    data=load_work(project,work_id)
    item={"id":"DRR-"+uuid.uuid4().hex[:8],"proposal":proposal,"evidence":evidence,"at":_now()}
    data["reinvestment"].append(item)
    data["history"].append({"event":"reinvestment","reinvestment_id":item["id"],"at":_now()})
    save_work(project,data)
    append_event(project,work_id,{"type":"reinvestment_added",**item})
    return item
