
from pathlib import Path
import argparse, json, yaml
from . import __version__
from .resources_api import resource_root
from .profile import load_project_profile
from .language import resolve_language
from .workflow import load_workflow, list_workflows
from .context import build_runtime_context
from .state import new_work, load_work, add_evidence, set_decision, add_reinvestment, add_artifact
from .engine import advance
from .policy import policy_summary, decision_allowed
from .evals import eval_evidence_packet, eval_specification, eval_delegation
from .gates import evaluate_gate
from .task import build_task_packet, write_task_packet
from .adapter import install_adapter, uninstall_adapter
from .audit import verify_audit
from .diagnostic import load_questions, assess, render_markdown
from .template import render_template


def root(): return resource_root()

def cmd_version(args): print(__version__)

def cmd_init(args):
    target=Path(args.target).resolve(); src=root()/"profiles"/f"{args.profile}.yaml"
    if not src.exists(): raise SystemExit(f"Unknown profile: {args.profile}")
    outd=target/".deeprail"; outd.mkdir(parents=True,exist_ok=True); out=outd/"project.yaml"
    if out.exists() and not args.force: raise SystemExit(f"{out} exists; use --force")
    data=yaml.safe_load(src.read_text(encoding="utf-8")); data["deeprail"]["language"]["communication"]=args.communication; data["deeprail"]["language"]["artifacts"]=args.artifacts
    out.write_text(yaml.safe_dump(data,allow_unicode=True,sort_keys=False),encoding="utf-8")
    for d in ["state","audit","runs","artifacts"]: (outd/d).mkdir(exist_ok=True)
    print(out)
    if args.adapter:
        print(json.dumps(install_adapter(target,args.adapter),ensure_ascii=False,indent=2))

def cmd_doctor(args):
    p=load_project_profile(args.project); lang=resolve_language(p)
    checks={"profile":True,"language":lang,"policy":policy_summary(p),"workflows":list_workflows(root()),"adapter":None}
    ap=Path(args.project)/".deeprail"/"adapter.json"
    if ap.exists(): checks["adapter"]=json.loads(ap.read_text(encoding="utf-8"))
    print("DeepRail doctor: PASS"); print(json.dumps(checks,ensure_ascii=False,indent=2))

def cmd_context(args):
    p=load_project_profile(args.project); wf=load_workflow(root(),args.workflow) if args.workflow else None; print(build_runtime_context(p,wf),end="")

def cmd_work_start(args): print(json.dumps(new_work(args.project,args.title,args.intent),ensure_ascii=False,indent=2))

def cmd_work_status(args): print(json.dumps(load_work(args.project,args.work_id),ensure_ascii=False,indent=2))

def cmd_task(args):
    p=load_project_profile(args.project); work=load_work(args.project,args.work_id)
    if args.write:
        path,text=write_task_packet(root(),args.project,p,work); print(path)
    else: print(build_task_packet(root(),args.project,p,work),end="")

def cmd_gate(args):
    work=load_work(args.project,args.work_id); result=evaluate_gate(root(),work); print(json.dumps(result,ensure_ascii=False,indent=2));
    if not result["pass"]: raise SystemExit(2)

def cmd_work_advance(args):
    p=load_project_profile(args.project); data=advance(root(),args.project,p,args.work_id,args.to,args.actor); print(json.dumps(data,ensure_ascii=False,indent=2))

def cmd_artifact_add(args): print(json.dumps(add_artifact(args.project,args.work_id,args.kind,args.location,args.description),ensure_ascii=False,indent=2))

def cmd_evidence_add(args): print(json.dumps(add_evidence(args.project,args.work_id,args.type,args.description,args.location,args.verified,args.actor,args.independent,args.result),ensure_ascii=False,indent=2))

def cmd_decision(args):
    p=load_project_profile(args.project); allowed,reason=decision_allowed(p,args.value,args.actor)
    if not allowed: raise PermissionError(reason)
    print(json.dumps(set_decision(args.project,args.work_id,args.value,args.actor,args.reason),ensure_ascii=False,indent=2))

def cmd_reinvest(args): print(json.dumps(add_reinvestment(args.project,args.work_id,args.proposal,args.evidence),ensure_ascii=False,indent=2))

def cmd_eval(args):
    if args.kind=="evidence": result=eval_evidence_packet(json.loads(Path(args.file).read_text(encoding="utf-8")))
    elif args.kind=="spec": result=eval_specification(Path(args.file).read_text(encoding="utf-8"))
    else: result=eval_delegation(load_project_profile(args.project))
    print(json.dumps(result,ensure_ascii=False,indent=2));
    if not result["pass"]: raise SystemExit(2)

def cmd_adapter_install(args): print(json.dumps(install_adapter(args.project,args.adapter),ensure_ascii=False,indent=2))

def cmd_adapter_uninstall(args): print(json.dumps(uninstall_adapter(args.project),ensure_ascii=False,indent=2))

def cmd_audit_verify(args):
    r=verify_audit(args.project,args.work_id); print(json.dumps(r,ensure_ascii=False,indent=2));
    if not r["pass"]: raise SystemExit(2)

def cmd_template(args):
    p=load_project_profile(args.project); text=render_template(p,args.kind)
    if args.output: Path(args.output).write_text(text,encoding="utf-8"); print(args.output)
    else: print(text,end="")

def cmd_assess(args):
    q=load_questions()
    if args.questionnaire:
        print(json.dumps({x["id"]:0 for x in q["questions"]},ensure_ascii=False,indent=2)); return
    if not args.answers: raise SystemExit("--answers or --questionnaire is required")
    answers=json.loads(Path(args.answers).read_text(encoding="utf-8")); result=assess(answers)
    print(render_markdown(result) if args.format=="md" else json.dumps(result,ensure_ascii=False,indent=2),end="" if args.format=="md" else "\n")
    if not result["pass"]: raise SystemExit(2)

def main():
    p=argparse.ArgumentParser(prog="deeprail"); sub=p.add_subparsers(dest="command",required=True)
    s=sub.add_parser("version"); s.set_defaults(func=cmd_version)
    s=sub.add_parser("init"); s.add_argument("--target",required=True); s.add_argument("--profile",default="lightweight",choices=["lightweight","standard","enterprise","high-risk"]); s.add_argument("--communication",default="ja",choices=["ja","en"]); s.add_argument("--artifacts",default="ja",choices=["ja","en"]); s.add_argument("--adapter",choices=["claude","generic"]); s.add_argument("--force",action="store_true"); s.set_defaults(func=cmd_init)
    s=sub.add_parser("doctor"); s.add_argument("--project",required=True); s.set_defaults(func=cmd_doctor)
    s=sub.add_parser("context"); s.add_argument("--project",required=True); s.add_argument("--workflow"); s.set_defaults(func=cmd_context)
    s=sub.add_parser("work-start"); s.add_argument("--project",required=True); s.add_argument("--title",required=True); s.add_argument("--intent",required=True); s.set_defaults(func=cmd_work_start)
    s=sub.add_parser("work-status"); s.add_argument("--project",required=True); s.add_argument("--work-id",required=True); s.set_defaults(func=cmd_work_status)
    s=sub.add_parser("task"); s.add_argument("--project",required=True); s.add_argument("--work-id",required=True); s.add_argument("--write",action="store_true"); s.set_defaults(func=cmd_task)
    s=sub.add_parser("gate"); s.add_argument("--project",required=True); s.add_argument("--work-id",required=True); s.set_defaults(func=cmd_gate)
    s=sub.add_parser("work-advance"); s.add_argument("--project",required=True); s.add_argument("--work-id",required=True); s.add_argument("--to",required=True); s.add_argument("--actor",choices=["human","ai","policy"],default="human"); s.set_defaults(func=cmd_work_advance)
    s=sub.add_parser("artifact-add"); s.add_argument("--project",required=True); s.add_argument("--work-id",required=True); s.add_argument("--kind",required=True); s.add_argument("--location",required=True); s.add_argument("--description",default=""); s.set_defaults(func=cmd_artifact_add)
    s=sub.add_parser("evidence-add"); s.add_argument("--project",required=True); s.add_argument("--work-id",required=True); s.add_argument("--type",required=True,choices=["observed_behavior","machine_check","human_decision","independent_evaluation","other","self_report"]); s.add_argument("--description",required=True); s.add_argument("--location"); s.add_argument("--verified",action="store_true"); s.add_argument("--actor",choices=["human","ai","policy","tool"],default="human"); s.add_argument("--independent",action="store_true"); s.add_argument("--result",choices=["pass","fail","unknown"],default="pass"); s.set_defaults(func=cmd_evidence_add)
    s=sub.add_parser("decision"); s.add_argument("--project",required=True); s.add_argument("--work-id",required=True); s.add_argument("--value",required=True,choices=["pass","retry","reject","escalate","defer"]); s.add_argument("--actor",choices=["human","ai","policy"],default="human"); s.add_argument("--reason",required=True); s.set_defaults(func=cmd_decision)
    s=sub.add_parser("reinvest"); s.add_argument("--project",required=True); s.add_argument("--work-id",required=True); s.add_argument("--proposal",required=True); s.add_argument("--evidence",required=True); s.set_defaults(func=cmd_reinvest)
    s=sub.add_parser("eval"); s.add_argument("kind",choices=["evidence","spec","delegation"]); s.add_argument("--file"); s.add_argument("--project"); s.set_defaults(func=cmd_eval)
    a=sub.add_parser("adapter-install"); a.add_argument("--project",required=True); a.add_argument("--adapter",required=True,choices=["claude","generic"]); a.set_defaults(func=cmd_adapter_install)
    a=sub.add_parser("adapter-uninstall"); a.add_argument("--project",required=True); a.set_defaults(func=cmd_adapter_uninstall)
    a=sub.add_parser("audit-verify"); a.add_argument("--project",required=True); a.add_argument("--work-id",required=True); a.set_defaults(func=cmd_audit_verify)
    a=sub.add_parser("template"); a.add_argument("--project",required=True); a.add_argument("--kind",required=True,choices=["specification","decision-packet","review-packet","evidence-packet","reinvestment"]); a.add_argument("--output"); a.set_defaults(func=cmd_template)
    a=sub.add_parser("assess"); a.add_argument("--questionnaire",action="store_true"); a.add_argument("--answers"); a.add_argument("--format",choices=["json","md"],default="json"); a.set_defaults(func=cmd_assess)
    args=p.parse_args(); args.func(args)

if __name__=="__main__": main()
