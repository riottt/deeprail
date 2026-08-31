
import sys,tempfile,unittest,yaml
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/"runtime"))
from deeprail_runtime.state import new_work,add_evidence,load_work
from deeprail_runtime.gates import evaluate_gate
from deeprail_runtime.engine import advance

class GatePolicyTest(unittest.TestCase):
 def setUp(self):
  self.t=tempfile.TemporaryDirectory(); self.p=Path(self.t.name); (self.p/".deeprail").mkdir();
  profile=yaml.safe_load((ROOT/"profiles/standard.yaml").read_text()); (self.p/".deeprail/project.yaml").write_text(yaml.safe_dump(profile),encoding="utf-8"); self.profile=profile
 def tearDown(self): self.t.cleanup()
 def test_discover_requires_non_self_report(self):
  w=new_work(self.p,"x","x"); advance(ROOT,self.p,self.profile,w["id"],"discover","human")
  add_evidence(self.p,w["id"],"self_report","done",actor="ai")
  self.assertFalse(evaluate_gate(ROOT,load_work(self.p,w["id"]))["pass"])
  add_evidence(self.p,w["id"],"observed_behavior","inspected",verified=True)
  self.assertTrue(evaluate_gate(ROOT,load_work(self.p,w["id"]))["pass"])
 def test_verify_requires_independent(self):
  w=new_work(self.p,"x","x"); data=load_work(self.p,w["id"]); data["current_workflow"]="verify"; from deeprail_runtime.state import save_work; save_work(self.p,data)
  add_evidence(self.p,w["id"],"machine_check","tests",verified=True,actor="tool")
  add_evidence(self.p,w["id"],"observed_behavior","ui",verified=True,actor="ai")
  self.assertFalse(evaluate_gate(ROOT,load_work(self.p,w["id"]))["pass"])
  add_evidence(self.p,w["id"],"independent_evaluation","independent review",verified=True,actor="ai",independent=True)
  self.assertTrue(evaluate_gate(ROOT,load_work(self.p,w["id"]))["pass"])
if __name__=="__main__": unittest.main()
