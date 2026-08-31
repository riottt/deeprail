
import sys,unittest,yaml
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/"runtime"))
from deeprail_runtime.policy import decision_allowed
class PolicyTest(unittest.TestCase):
 def test_high_risk_ai_go_denied(self):
  p=yaml.safe_load((ROOT/"profiles/high-risk.yaml").read_text()); self.assertFalse(decision_allowed(p,"pass","ai")[0])
if __name__=="__main__": unittest.main()
