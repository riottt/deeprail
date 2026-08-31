
import sys,tempfile,unittest,yaml
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/"runtime"))
from deeprail_runtime.state import new_work,add_evidence,load_work,save_work,set_decision
from deeprail_runtime.engine import advance
class EngineTest(unittest.TestCase):
 def setUp(self):
  self.t=tempfile.TemporaryDirectory(); self.p=Path(self.t.name); (self.p/".deeprail").mkdir(); self.profile=yaml.safe_load((ROOT/"profiles/standard.yaml").read_text()); (self.p/".deeprail/project.yaml").write_text(yaml.safe_dump(self.profile),encoding="utf-8")
 def tearDown(self): self.t.cleanup()
 def test_verify_blocks_without_evidence(self):
  w=new_work(self.p,"x","x"); data=load_work(self.p,w["id"]); data["current_workflow"]="verify"; save_work(self.p,data)
  with self.assertRaises(PermissionError): advance(ROOT,self.p,self.profile,w["id"],"decide","human")
 def test_start_can_advance(self):
  w=new_work(self.p,"x","x"); out=advance(ROOT,self.p,self.profile,w["id"],"discover","human"); self.assertEqual(out["current_workflow"],"discover")
if __name__=="__main__": unittest.main()
