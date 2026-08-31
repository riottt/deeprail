
import sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/"runtime"))
from deeprail_runtime.diagnostic import load_questions,assess
class DiagnosticTest(unittest.TestCase):
 def test_review_evidence_surface(self):
  q=load_questions(); answers={x["id"]:(0 if x["dimension"] in {"review","evidence"} else 3) for x in q["questions"]}; r=assess(answers); names=[x["dimension"] for x in r["top_bottlenecks"]]; self.assertIn("review",names); self.assertIn("evidence",names)
if __name__=="__main__": unittest.main()
