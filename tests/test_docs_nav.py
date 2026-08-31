import unittest,yaml
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class DocsNavTest(unittest.TestCase):
 def test_nav_targets_exist(self):
  cfg=yaml.safe_load((ROOT/"mkdocs.yml").read_text(encoding="utf-8"))
  targets=[]
  def walk(x):
   if isinstance(x,str): targets.append(x)
   elif isinstance(x,list):
    for i in x: walk(i)
   elif isinstance(x,dict):
    for v in x.values(): walk(v)
  walk(cfg.get("nav",[]))
  for rel in targets:
   self.assertTrue((ROOT/rel).exists(),rel)
if __name__=="__main__": unittest.main()
