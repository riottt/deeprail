
import sys,unittest,yaml
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/"runtime"))
from deeprail_runtime.template import render_template
class TemplateTest(unittest.TestCase):
 def test_ja_artifact(self):
  p=yaml.safe_load((ROOT/"profiles/standard.yaml").read_text()); p["deeprail"]["language"]["artifacts"]="ja"; self.assertIn("現在の挙動",render_template(p,"specification"))
 def test_en_artifact(self):
  p=yaml.safe_load((ROOT/"profiles/standard.yaml").read_text()); p["deeprail"]["language"]["artifacts"]="en"; self.assertIn("Current Behavior",render_template(p,"specification"))
if __name__=="__main__": unittest.main()
