
from pathlib import Path
import yaml

def load_project_profile(project_dir):
    p = Path(project_dir) / ".deeprail" / "project.yaml"
    if not p.exists():
        raise FileNotFoundError(f"DeepRail project profile not found: {p}")
    data = yaml.safe_load(p.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or "deeprail" not in data:
        raise ValueError("Invalid DeepRail project profile")
    return data
