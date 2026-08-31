
from pathlib import Path
import json, re
from .resources_api import resource_root

START="<!-- deeprail:start -->"
END="<!-- deeprail:end -->"


def _template(adapter):
    root=resource_root()
    if adapter=="claude":
        p=root/"adapters"/"claude"/"project-block.md"
    elif adapter=="generic":
        p=root/"adapters"/"generic"/"project-instructions.md"
    else:
        raise ValueError(f"unsupported adapter: {adapter}")
    return p.read_text(encoding="utf-8").strip()+"\n"


def install_adapter(project, adapter):
    project=Path(project).resolve()
    dr=project/".deeprail"; dr.mkdir(parents=True,exist_ok=True)
    if adapter=="claude":
        target=project/"CLAUDE.md"
        block=_template("claude")
        existing=target.read_text(encoding="utf-8") if target.exists() else ""
        if START in existing and END in existing:
            existing=re.sub(re.escape(START)+r".*?"+re.escape(END),block.strip(),existing,flags=re.S)
        else:
            existing=(existing.rstrip()+"\n\n" if existing.strip() else "")+block
        target.write_text(existing.rstrip()+"\n",encoding="utf-8")
        managed=str(target)
    else:
        target=dr/"AGENT.md"
        target.write_text(_template("generic"),encoding="utf-8")
        managed=str(target)
    state={"adapter":adapter,"managed_file":managed,"version":1}
    (dr/"adapter.json").write_text(json.dumps(state,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    return state


def uninstall_adapter(project):
    project=Path(project).resolve(); state_path=project/".deeprail"/"adapter.json"
    if not state_path.exists(): return {"removed":False,"reason":"adapter not installed"}
    state=json.loads(state_path.read_text(encoding="utf-8"))
    target=Path(state["managed_file"])
    if state["adapter"]=="claude" and target.exists():
        text=target.read_text(encoding="utf-8")
        text=re.sub(r"\n?"+re.escape(START)+r".*?"+re.escape(END)+r"\n?","\n",text,flags=re.S).strip()
        if text: target.write_text(text+"\n",encoding="utf-8")
        else: target.unlink()
    elif target.exists():
        target.unlink()
    state_path.unlink()
    return {"removed":True,"adapter":state["adapter"]}
