
import sys,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/"runtime"))
from deeprail_runtime.state import new_work,add_evidence
from deeprail_runtime.audit import verify_audit
class AuditTest(unittest.TestCase):
 def test_chain(self):
  with tempfile.TemporaryDirectory() as t:
   w=new_work(t,"x","y"); add_evidence(t,w["id"],"other","x"); self.assertTrue(verify_audit(t,w["id"])["pass"])
if __name__=="__main__": unittest.main()
