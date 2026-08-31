
from .language import resolve_language, runtime_language_instruction

def build_runtime_context(profile, workflow=None):
    dr = profile["deeprail"]
    lang = resolve_language(profile)
    lines = [
        "# DeepRail Runtime Context",
        "",
        f"DeepRail version: {dr.get('version', 'unknown')}",
        f"Project type: {dr.get('project_type', 'unknown')}",
        f"Risk profile: {dr.get('risk_profile', 'unknown')}",
        f"Execution autonomy: {dr.get('autonomy', {}).get('execution', 'unknown')}",
        f"Evaluation authority: {dr.get('autonomy', {}).get('evaluation', 'unknown')}",
        f"Approval strength: {dr.get('autonomy', {}).get('approval', 'unknown')}",
        "",
        runtime_language_instruction(lang),
        "",
        "Core invariant: Work advances only on approved evidence.",
        "Step/Gate invariant: a step is not owned by a permanent human actor; it is a controlled transition with evidence, exit conditions, and failure return paths.",
    ]
    if workflow:
        lines += [
            "",
            f"## Active Workflow: {workflow['id']}",
            f"Purpose: {workflow['purpose']}",
            "Required Evidence:",
            *[f"- {x}" for x in workflow.get("required_evidence", [])],
            f"Exit Condition: {workflow['exit_condition']}",
            f"Decision Rights: {workflow['decision_rights']}",
        ]
    return "\n".join(lines) + "\n"
