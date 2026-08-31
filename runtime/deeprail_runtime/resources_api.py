
from pathlib import Path
import os


def checkout_root():
    candidate = Path(__file__).resolve().parents[2]
    if (candidate / "workflows").exists() and (candidate / "profiles").exists():
        return candidate
    return None


def resource_root():
    override = os.getenv("DEEPRAIL_HOME")
    if override:
        p = Path(override).expanduser().resolve()
        if not (p / "workflows").exists():
            raise RuntimeError(f"DEEPRAIL_HOME is not a valid DeepRail resource root: {p}")
        return p
    checkout = checkout_root()
    if checkout:
        return checkout
    packaged = Path(__file__).resolve().parent / "resources"
    if not packaged.exists():
        raise RuntimeError("DeepRail packaged resources are missing")
    return packaged
