import contextlib
import importlib.util
import io
import tempfile
import unittest
from pathlib import Path
from unittest import mock

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "eval_status.py"
SPEC = importlib.util.spec_from_file_location("eval_status", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
eval_status = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(eval_status)


class EvalStatusTests(unittest.TestCase):
    def test_main_reports_missing_db_as_zero_pending_for_end_gate(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            missing_db = Path(tmpdir) / "evals.sqlite"
            with mock.patch.object(eval_status, "EVAL_DB_PATH", missing_db):
                with mock.patch.object(
                    eval_status,
                    "parse_args",
                    return_value=mock.Mock(require_zero_pending=True),
                ):
                    stderr = io.StringIO()
                    with contextlib.redirect_stderr(stderr):
                        status = eval_status.main()

        self.assertEqual(status, 0)
        self.assertEqual(stderr.getvalue(), "")

    def test_main_fails_when_pending_rows_exist(self) -> None:
        with mock.patch.object(
            eval_status,
            "load_counts",
            return_value={"total": 10, "pass": 7, "fail": 1, "pending": 2},
        ):
            with mock.patch.object(
                eval_status,
                "parse_args",
                return_value=mock.Mock(require_zero_pending=True),
            ):
                stderr = io.StringIO()
                with contextlib.redirect_stderr(stderr):
                    status = eval_status.main()

        self.assertEqual(status, 1)
        self.assertIn("end-pending-check: FAIL", stderr.getvalue())
        self.assertIn("pending=2", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
