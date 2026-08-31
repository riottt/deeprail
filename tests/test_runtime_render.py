
import sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/"runtime"))
from deeprail_runtime.workflow import load_workflow
from deeprail_runtime.render import render_workflow
class RenderTest(unittest.TestCase):
 def test_ja(self):
  t=render_workflow(load_workflow(ROOT,"discover"),"ja"); self.assertIn("目的",t); self.assertIn("Codebase",t); self.assertIn("調査",t)
 def test_en(self):
  t=render_workflow(load_workflow(ROOT,"discover"),"en"); self.assertIn("Purpose",t); self.assertIn("Reduce unknowns",t)
if __name__=="__main__": unittest.main()
