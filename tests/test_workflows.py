
import sys, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "runtime"))
from deeprail_runtime.workflow import list_workflows, load_workflow

class WorkflowTest(unittest.TestCase):
    def test_workflow_set(self):
        names = list_workflows(ROOT)
        self.assertEqual(names, sorted(["start","discover","shape","align","specify","decompose","execute","verify","decide","reinvest"]))
    def test_contract(self):
        wf=load_workflow(ROOT,"verify")
        for k in ["purpose","inputs","outputs","required_evidence","exit_condition","decision_rights","failure_return_path","next"]:
            self.assertIn(k,wf)

if __name__ == "__main__": unittest.main()
