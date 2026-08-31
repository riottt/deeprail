
import sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"runtime"))
from deeprail_runtime.evals import eval_evidence_packet

class EvalTest(unittest.TestCase):
    def test_self_report_only_fails(self):
        r=eval_evidence_packet({"evidence":[{"type":"self_report"}],"unknowns":[],"decision":"pass"})
        self.assertFalse(r["pass"])
    def test_real_evidence_passes(self):
        r=eval_evidence_packet({"evidence":[{"type":"machine_check"}],"unknowns":[],"decision":"pass"})
        self.assertTrue(r["pass"])

if __name__=="__main__": unittest.main()
