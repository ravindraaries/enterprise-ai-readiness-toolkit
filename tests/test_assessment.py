import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from assessment import report, validate


class AssessmentTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / "examples/sample_assessment.json").read_text())

    def test_sample_valid(self):
        self.assertEqual(validate(self.data), self.data)

    def test_report_contains_five_domains(self):
        output = report(self.data)
        for label in ("Cloud migration", "Application modernization", "Custom software development", "AI server infrastructure", "Network optimization"):
            self.assertIn(label, output)

    def test_reject_boolean_score(self):
        self.data["domains"]["cloud_migration"][0]["score"] = True
        with self.assertRaises(ValueError):
            validate(self.data)

    def test_reject_missing_domain(self):
        del self.data["domains"]["ai_infrastructure"]
        with self.assertRaises(ValueError):
            validate(self.data)


if __name__ == "__main__":
    unittest.main()
