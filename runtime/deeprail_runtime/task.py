
from pathlib import Path
import datetime, json
from .workflow import load_workflow
from .language import resolve_language
from .render import render_workflow, localized
from .gates import evaluate_gate
from .policy import policy_summary


def _runs_dir(project, work_id):
    p=Path(project)/".deeprail"/"runs"/work_id
    p.mkdir(parents=True,exist_ok=True)
    return p


def build_task_packet(root, project, profile, work):
    wf=load_workflow(root,work["current_workflow"])
    lang=resolve_language(profile)
    comm=lang["communication_language"]
    gate=evaluate_gate(root,work)
    labels = {
      "ja": {"title":"DeepRail Task Packet","intent":"Intent","state":"現在の状態","policy":"Operating Profile","contract":"Workflow Contract","instructions":"Agent実行指示","gate":"Evidence Gate","rules":"不変条件"},
      "en": {"title":"DeepRail Task Packet","intent":"Intent","state":"Current State","policy":"Operating Profile","contract":"Workflow Contract","instructions":"Agent Instructions","gate":"Evidence Gate","rules":"Invariants"}
    }[comm]
    display_wf=localized(wf,comm)
    instructions = display_wf.get("agent_instructions", [])
    if not instructions:
        instructions=[
          "Perform only work inside the active workflow responsibility.",
          "Do not silently redefine the objective or acceptance criteria.",
          "Record artifacts and evidence through the DeepRail CLI.",
          "If required evidence cannot be produced, return to the declared failure path or escalate."
        ]
    out=[f"# {labels['title']} — {work['id']}","",f"## {labels['intent']}",work['intent'],"",f"## {labels['state']}",f"- Work: `{work['id']}`",f"- Workflow: `{work['current_workflow']}`",f"- Status: `{work['status']}`","",f"## {labels['policy']}","```json",json.dumps(policy_summary(profile),ensure_ascii=False,indent=2),"```","",f"## {labels['contract']}",render_workflow(wf,comm),f"## {labels['instructions']}"]
    out += [f"- {x}" for x in instructions]
    out += ["",f"## {labels['gate']}","```json",json.dumps(gate,ensure_ascii=False,indent=2),"```","",f"## {labels['rules']}","- Work advances only on approved evidence.","- Executor self-report alone is never completion evidence.","- Stable IDs, schema keys and machine enum values are not translated.","- A / EA / S are independent axes."]
    return "\n".join(out)+"\n"


def write_task_packet(root, project, profile, work):
    text=build_task_packet(root,project,profile,work)
    stamp=datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    p=_runs_dir(project,work["id"])/f"{stamp}-{work['current_workflow']}.md"
    p.write_text(text,encoding="utf-8")
    return p,text
