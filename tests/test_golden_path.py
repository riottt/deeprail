
import sys, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "runtime"))
from deeprail_runtime.workflow import load_workflow

class GoldenPathTest(unittest.TestCase):
    def test_start_can_reach_reinvest(self):
        seen=set()
        frontier=["start"]
        while frontier:
            x=frontier.pop()
            if x in seen: continue
            seen.add(x)
            if x=="reinvest": break
            wf=load_workflow(ROOT,x)
            frontier.extend(n for n in wf.get("next",[]) if n not in seen)
        self.assertIn("reinvest",seen)

if __name__ == "__main__": unittest.main()
