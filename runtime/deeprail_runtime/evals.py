
def eval_evidence_packet(packet):
    failures=[]
    evidence=packet.get("evidence",[])
    if not evidence:
        failures.append("no evidence")
    usable=[e for e in evidence if e.get("result","pass") != "fail"]
    if usable and all(e.get("type")=="self_report" for e in usable):
        failures.append("executor self-report cannot be the only evidence")
    if any(e.get("result")=="fail" for e in evidence):
        failures.append("failed evidence is unresolved")
    if "unknowns" not in packet:
        failures.append("unknowns missing")
    if packet.get("decision") not in {"pass","retry","reject","escalate","defer"}:
        failures.append("invalid decision")
    return {"pass":not failures,"failures":failures}


def eval_specification(spec_text):
    required=["Intent","Acceptance Criteria","Required Evidence","Unknown"]
    missing=[x for x in required if x.lower() not in spec_text.lower()]
    return {"pass":not missing,"missing":missing}


def eval_delegation(profile):
    dr=profile.get("deeprail",{})
    missing=[]
    for key in ["risk_profile","autonomy"]:
        if key not in dr: missing.append(key)
    a=dr.get("autonomy",{})
    for key in ["execution","evaluation","approval"]:
        if key not in a: missing.append("autonomy."+key)
    constraints=dr.get("constraints",[])
    if dr.get("risk_profile") in {"high","regulated"} and "rollback-required" not in constraints and "auditability" not in constraints:
        missing.append("high-risk control: rollback-required or auditability")
    return {"pass":not missing,"missing":missing}
