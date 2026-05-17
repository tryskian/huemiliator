import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "read_startup_docs.py"
SPEC = importlib.util.spec_from_file_location("read_startup_docs", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
read_startup_docs = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(read_startup_docs)


class ReadStartupDocsTests(unittest.TestCase):
    def test_extract_title_prefers_first_h1(self) -> None:
        text = "# First Title\n\n## Second\n"
        self.assertEqual(read_startup_docs.extract_title(text), "First Title")

    def test_find_last_updated_reads_iso_marker(self) -> None:
        text = "Last updated: 2026-05-17\n"
        self.assertEqual(read_startup_docs.find_last_updated(text), "2026-05-17")

    def test_summarize_doc_includes_title_and_last_updated(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "sample.md"
            path.write_text("# Sample\n\nLast updated: 2026-05-17\n", encoding="utf-8")

            summary = read_startup_docs.summarize_doc(path)

        self.assertIn("sample.md", summary)
        self.assertIn("Sample", summary)
        self.assertIn("2026-05-17", summary)


if __name__ == "__main__":
    unittest.main()
