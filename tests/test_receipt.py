import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/deployment-verification/scripts/check-receipt.py"
FIXTURES = ROOT / "examples/synthetic-project"


def run_receipt(path):
    return subprocess.run(
        [sys.executable, str(SCRIPT), str(path)], capture_output=True, text=True, timeout=10
    )


class TestReceipt(unittest.TestCase):
    def fixture(self):
        return json.loads((FIXTURES / "release-current.json").read_text(encoding="utf-8"))

    def run_document(self, document):
        data = json.dumps(document).encode("utf-8") if isinstance(document, dict) else document
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "receipt.json"
            path.write_bytes(data)
            before = set(path.parent.iterdir())
            result = run_receipt(path)
            self.assertEqual(path.read_bytes(), data)
            self.assertEqual(set(path.parent.iterdir()), before)
        return result

    def expect_status(self, result, stage, expected):
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertEqual(json.loads(result.stdout)["verification_scope"], "supplied_receipt_consistency")
        self.assertFalse(json.loads(result.stdout)["complete"])
        self.assertEqual(json.loads(result.stdout)["stages"][stage], expected)

    def test_matching_release(self):
        result = run_receipt(FIXTURES / "release-current.json")
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["verification_scope"], "supplied_receipt_consistency")
        self.assertEqual(set(report["stages"].values()), {"VERIFIED"})

    def test_wrong_ci_commit_and_runtime_rollout(self):
        result = run_receipt(FIXTURES / "release-wrong-rollout.json")
        self.expect_status(result, "ci", "MISMATCH")
        self.expect_status(result, "runtime", "MISMATCH")
        self.assertEqual(json.loads(result.stdout)["stages"]["deployment"], "VERIFIED")

    def test_matching_old_deployment_and_runtime_cannot_verify_expected_rollout(self):
        document = self.fixture()
        document["stages"]["deployment"]["rollout"] = "rollout-39"
        document["stages"]["runtime"]["rollout"] = "rollout-39"
        result = self.run_document(document)
        self.expect_status(result, "deployment", "MISMATCH")
        self.expect_status(result, "runtime", "MISMATCH")

    def test_expected_rollout_is_needed_for_successful_verification(self):
        document = self.fixture()
        del document["candidate"]["rollout"]
        result = self.run_document(document)
        self.expect_status(result, "deployment", "MISSING")
        self.expect_status(result, "runtime", "MISSING")

    def test_failed_old_rollout_is_not_attributed_without_an_expected_rollout(self):
        document = self.fixture()
        del document["candidate"]["rollout"]
        for stage in ("deployment", "runtime"):
            document["stages"][stage].update(rollout="rollout-39", outcome="failed")
        result = self.run_document(document)
        self.expect_status(result, "deployment", "MISSING")
        self.expect_status(result, "runtime", "MISSING")

    def test_green_health_without_deployment(self):
        document = self.fixture()
        del document["stages"]["deployment"]
        result = self.run_document(document)
        self.expect_status(result, "deployment", "MISSING")
        self.expect_status(result, "runtime", "MISSING")

    def test_failed_deployment_cannot_link_successful_runtime(self):
        document = self.fixture()
        document["stages"]["deployment"]["outcome"] = "failed"
        result = self.run_document(document)
        self.expect_status(result, "deployment", "FAILED")
        self.expect_status(result, "runtime", "MISSING")

    def test_wrong_runtime_target(self):
        document = self.fixture()
        document["stages"]["runtime"]["target"] = "preview-east"
        self.expect_status(self.run_document(document), "runtime", "MISMATCH")

    def test_wrong_build_digest(self):
        document = self.fixture()
        document["stages"]["build"]["digest"] = "sha256:" + "e" * 64
        self.expect_status(self.run_document(document), "build", "MISMATCH")

    def test_failed_check(self):
        document = self.fixture()
        document["stages"]["ci"]["outcome"] = "failed"
        self.expect_status(self.run_document(document), "ci", "FAILED")

    def test_bad_inputs_are_rejected_without_echo(self):
        inputs = [
            b'{"candidate": {}, "candidate": {}, "stages": {}}',
            b"[" * 129_000,
            b"[" * 2_000,
            b"\xff",
            b" " * (128 * 1024 + 1),
            b"synthetic-invalid-input",
        ]
        for data in inputs:
            with self.subTest(size=len(data)):
                result = self.run_document(data)
                self.assertEqual(result.returncode, 2)
                self.assertEqual(result.stdout, "")
                self.assertNotIn("synthetic-invalid-input", result.stderr)

    def test_unknown_stage_extra_fields_and_invalid_id(self):
        for edit in ("stage", "field", "id", "outcome"):
            with self.subTest(edit=edit):
                document = self.fixture()
                if edit == "stage":
                    document["stages"]["unknown"] = {}
                elif edit == "field":
                    document["stages"]["deployment"]["unknown"] = True
                elif edit == "id":
                    document["candidate"]["commit"] = "short-name"
                else:
                    document["stages"]["runtime"]["outcome"] = True
                self.assertEqual(self.run_document(document).returncode, 2)


if __name__ == "__main__":
    unittest.main()
