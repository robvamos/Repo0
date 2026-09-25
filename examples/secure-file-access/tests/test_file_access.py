import importlib.util
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).parents[1] / "after" / "file_access.py"
SPEC = importlib.util.spec_from_file_location("secure_file_access", MODULE_PATH)
assert SPEC and SPEC.loader
file_access = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(file_access)


class SecureFileAccessTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_directory = tempfile.TemporaryDirectory()
        self.base = Path(self.temp_directory.name)
        self.workspace = self.base / "workspace"
        self.workspace.mkdir()
        (self.workspace / "allowed.txt").write_text("public demo", encoding="utf-8")
        (self.base / "secret.txt").write_text("must stay outside", encoding="utf-8")

    def tearDown(self) -> None:
        self.temp_directory.cleanup()

    def test_reads_regular_file_inside_workspace(self) -> None:
        self.assertEqual(
            file_access.read_workspace_file(self.workspace, "allowed.txt"),
            "public demo",
        )

    def test_rejects_parent_traversal(self) -> None:
        with self.assertRaises(file_access.UnsafePathError):
            file_access.read_workspace_file(self.workspace, "../secret.txt")

    def test_rejects_absolute_path_outside_workspace(self) -> None:
        with self.assertRaises(file_access.UnsafePathError):
            file_access.read_workspace_file(self.workspace, str(self.base / "secret.txt"))

    def test_rejects_missing_file(self) -> None:
        with self.assertRaises(FileNotFoundError):
            file_access.read_workspace_file(self.workspace, "missing.txt")

    def test_rejects_directory(self) -> None:
        with self.assertRaises(file_access.UnsafePathError):
            file_access.read_workspace_file(self.workspace, ".")

    def test_rejects_empty_and_nul_paths(self) -> None:
        for value in ("", "bad\x00name"):
            with self.subTest(value=value):
                with self.assertRaises(file_access.UnsafePathError):
                    file_access.read_workspace_file(self.workspace, value)


if __name__ == "__main__":
    unittest.main()
