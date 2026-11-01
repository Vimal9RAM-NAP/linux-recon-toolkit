import unittest
import tempfile
from pathlib import Path
from unittest.mock import patch
from io import StringIO

from modules import file_info


class TestFileInfo(unittest.TestCase):

    def test_format_permissions(self):
        import stat

        permissions = file_info.format_permissions(
            stat.S_IFREG | 0o644
        )

        self.assertEqual(permissions, "-rw-r--r--")

    def test_file_information(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            test_file = Path(temp_dir) / "example.txt"
            test_file.write_text("Hello Linux Recon Toolkit!")

            output = StringIO()

            with patch("builtins.input", return_value=str(test_file)):
                with patch("sys.stdout", output):
                    file_info.show_file_info()

            result = output.getvalue()

            self.assertIn("example.txt", result)
            self.assertIn("Regular file", result)
            self.assertIn("Permissions", result)
            self.assertIn("Owner", result)

    def test_empty_path(self):
        output = StringIO()

        with patch("builtins.input", return_value=""):
            with patch("sys.stdout", output):
                file_info.show_file_info()

        self.assertIn("Path cannot be empty", output.getvalue())

    def test_missing_path(self):
        output = StringIO()

        with patch(
            "builtins.input",
            return_value="/this/path/should/not/exist/linux-recon-test",
        ):
            with patch("sys.stdout", output):
                file_info.show_file_info()

        self.assertIn("does not exist", output.getvalue())


if __name__ == "__main__":
    unittest.main()