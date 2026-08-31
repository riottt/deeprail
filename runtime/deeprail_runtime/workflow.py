
from pathlib import Path
import yaml
from .resources_api import resource_root


def workflow_root(root=None):
    return Path(root) / "workflows" if root else resource_root() / "workflows"


def list_workflows(root=None):
    r = workflow_root(root)
    return sorted(p.name for p in r.iterdir() if p.is_dir() and (p / "workflow.yaml").exists())


def load_workflow(root, name=None):
    # Backward compatible: load_workflow(repo_root, name) or load_workflow(None, name)
    if name is None:
        name = root
        root = None
    p = workflow_root(root) / name / "workflow.yaml"
    if not p.exists():
        raise FileNotFoundError(f"Unknown DeepRail workflow: {name}")
    return yaml.safe_load(p.read_text(encoding="utf-8"))
