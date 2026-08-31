
import sys,tempfile,unittest,yaml
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/"runtime"))
from deeprail_runtime.adapter import install_adapter,uninstall_adapter
class AdapterTest(unittest.TestCase):
 def test_claude_preserves_existing(self):
  with tempfile.TemporaryDirectory() as t:
   p=Path(t); (p/"CLAUDE.md").write_text("# Existing\n",encoding="utf-8")
   install_adapter(p,"claude"); txt=(p/"CLAUDE.md").read_text(); self.assertIn("# Existing",txt); self.assertIn("deeprail:start",txt)
   install_adapter(p,"claude"); self.assertEqual((p/"CLAUDE.md").read_text().count("deeprail:start"),1)
   uninstall_adapter(p); self.assertEqual((p/"CLAUDE.md").read_text(),"# Existing\n")
if __name__=="__main__": unittest.main()
