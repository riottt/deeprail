
from pathlib import Path
import json, hashlib, datetime


def _audit_dir(project):
    p = Path(project) / ".deeprail" / "audit"
    p.mkdir(parents=True, exist_ok=True)
    return p


def _path(project, work_id):
    return _audit_dir(project) / f"{work_id}.jsonl"


def _canonical(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def append_event(project, work_id, event):
    p = _path(project, work_id)
    prev_hash = None
    if p.exists():
        lines = [x for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]
        if lines:
            prev_hash = json.loads(lines[-1])["hash"]
    body = {
        "at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "work_id": work_id,
        "event": event,
        "prev_hash": prev_hash,
    }
    body["hash"] = hashlib.sha256(((prev_hash or "") + _canonical(body)).encode("utf-8")).hexdigest()
    with p.open("a", encoding="utf-8") as f:
        f.write(json.dumps(body, ensure_ascii=False, sort_keys=True) + "\n")
    return body


def verify_audit(project, work_id):
    p = _path(project, work_id)
    if not p.exists():
        return {"pass": False, "reason": "audit log missing", "events": 0}
    prev = None
    count = 0
    for line in p.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        obj = json.loads(line)
        got = obj.get("hash")
        body = {k:v for k,v in obj.items() if k != "hash"}
        expected = hashlib.sha256(((prev or "") + _canonical(body)).encode("utf-8")).hexdigest()
        if obj.get("prev_hash") != prev or got != expected:
            return {"pass": False, "reason": f"hash-chain mismatch at event {count+1}", "events": count}
        prev = got
        count += 1
    return {"pass": True, "reason": "audit chain valid", "events": count, "head": prev}
