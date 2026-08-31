
import sys,tempfile,unittest,yaml
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/"runtime"))
from deeprail_runtime.state import new_work
from deeprail_runtime.task import build_task_packet
class TaskPacketTest(unittest.TestCase):
 def test_packet_contains_gate(self):
  with tempfile.TemporaryDirectory() as t:
   p=Path(t); (p/".deeprail").mkdir(); profile=yaml.safe_load((ROOT/"profiles/standard.yaml").read_text()); w=new_work(p,"x","intent"); text=build_task_packet(ROOT,p,profile,w); self.assertIn("Evidence Gate",text); self.assertIn("DRW-",text)
if __name__=="__main__": unittest.main()
