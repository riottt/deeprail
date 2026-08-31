
from .resources_api import resource_root
from .language import resolve_language

KINDS={"specification","decision-packet","review-packet","evidence-packet","reinvestment"}

def render_template(profile,kind):
    if kind not in KINDS: raise ValueError(f"unknown template: {kind}")
    lang=resolve_language(profile)["artifact_output_language"]
    p=resource_root()/"templates"/kind/f"template.{lang}.md"
    if not p.exists(): p=resource_root()/"templates"/kind/"template.md"
    return p.read_text(encoding="utf-8")
