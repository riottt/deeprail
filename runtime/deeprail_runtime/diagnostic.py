
from pathlib import Path
import json, yaml
from .resources_api import resource_root


def load_questions():
    return yaml.safe_load((resource_root()/"diagnostics"/"questions.yaml").read_text(encoding="utf-8"))


def load_problem_map():
    return yaml.safe_load((resource_root()/"diagnostics"/"problem-map.yaml").read_text(encoding="utf-8"))


def assess(answers):
    q=load_questions(); pmap=load_problem_map(); dims={}
    missing=[]
    for item in q["questions"]:
        if item["id"] not in answers:
            missing.append(item["id"]); continue
        value=int(answers[item["id"]])
        if value<0 or value>3: raise ValueError(f"answer {item['id']} must be 0..3")
        dims.setdefault(item["dimension"],[]).append(value)
    result=[]
    for dim,vals in dims.items():
        score=round(sum(vals)/len(vals),2)
        severity="critical" if score<1 else "high" if score<1.67 else "medium" if score<2.34 else "low"
        result.append({"dimension":dim,"score":score,"severity":severity,**pmap[dim]})
    result.sort(key=lambda x:x["score"])
    return {"pass":not missing,"missing_answers":missing,"dimensions":result,"top_bottlenecks":result[:3]}


def render_markdown(result):
    lines=["# DeepRail Assessment","","## Top Bottlenecks"]
    for x in result["top_bottlenecks"]:
        lines += [f"### {x['label_ja']} — {x['score']} / 3 ({x['severity']})",f"- Book: " + ", ".join(f"Ch.{n}" for n in x['book_chapters']),f"- Standard: " + ", ".join(x['modules']),f"- Workflows: " + ", ".join(x['workflows']),""]
    if result["missing_answers"]:
        lines += ["## Missing Answers",", ".join(result["missing_answers"])]
    return "\n".join(lines)+"\n"
