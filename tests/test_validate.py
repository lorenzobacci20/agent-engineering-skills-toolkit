import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate", ROOT / "scripts/validate.py")
validate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validate)


class TestDistribution(unittest.TestCase):
    def test_manifest_covers_catalog(self):
        catalog, errors = validate.package_errors(ROOT)
        self.assertEqual(errors, [])
        self.assertEqual(validate.path_errors(ROOT), [])
        self.assertEqual(validate.check_manifest(ROOT, catalog), 10)

    def test_skill_cannot_link_to_resource_outside_package(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            skill = root / "skills" / "sample"
            skill.mkdir(parents=True)
            (root / "shared.md").touch()
            (skill / "SKILL.md").write_text("[shared](../../shared.md)", encoding="utf-8")
            self.assertEqual(len(validate.path_errors(root)), 1)

    def test_manifest_rejects_invalid_case_inputs_and_criteria(self):
        original = json.loads((ROOT / "evals/scenarios.json").read_text(encoding="utf-8"))["cases"][0]
        for edit in ("escape", "missing", "doubled", "type"):
            with self.subTest(edit=edit):
                case = copy.deepcopy(original)
                if edit == "escape":
                    case["inputs"] = ["examples/synthetic-project/../../README.md"]
                elif edit == "missing":
                    case["inputs"] = ["examples/synthetic-project/absent.json"]
                elif edit == "doubled":
                    case["criteria"].append(case["criteria"][0])
                else:
                    case["criteria"][0]["critical"] = 1
                with self.assertRaises(ValueError):
                    validate.check_case(ROOT, case, {original["skill"]})


if __name__ == "__main__":
    unittest.main()
