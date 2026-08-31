
import sys, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "runtime"))
from deeprail_runtime.language import resolve_language

class RuntimeLanguageTest(unittest.TestCase):
    def profile(self, c, a):
        return {"deeprail":{"language":{"communication":c,"artifacts":a}}}

    def test_ja_ja(self): self.assertEqual(resolve_language(self.profile("ja","ja"))["artifact_output_language"], "ja")
    def test_en_en(self): self.assertEqual(resolve_language(self.profile("en","en"))["communication_language"], "en")
    def test_ja_en(self):
        r=resolve_language(self.profile("ja","en"))
        self.assertEqual((r["communication_language"],r["artifact_output_language"]),("ja","en"))
    def test_en_ja(self):
        r=resolve_language(self.profile("en","ja"))
        self.assertEqual((r["communication_language"],r["artifact_output_language"]),("en","ja"))
    def test_invalid(self):
        with self.assertRaises(ValueError): resolve_language(self.profile("xx","ja"))

if __name__ == "__main__": unittest.main()
