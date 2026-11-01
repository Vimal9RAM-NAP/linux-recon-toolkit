import unittest
from unittest.mock import patch
from io import StringIO

from modules import system_info


class TestSystemInfo(unittest.TestCase):

    @patch("modules.system_info.platform.system", return_value="Linux")
    @patch("modules.system_info.platform.release", return_value="6.1.0")
    @patch("modules.system_info.platform.machine", return_value="x86_64")
    @patch("modules.system_info.platform.node", return_value="test-machine")
    @patch("modules.system_info.platform.python_version", return_value="3.12.0")
    @patch("modules.system_info.shutil.disk_usage")
    def test_show_system_info(
        self,
        mock_disk_usage,
        mock_node,
        mock_machine,
        mock_release,
        mock_system,
        mock_python_version,
    ):
        mock_disk_usage.return_value = type(
            "DiskUsage",
            (),
            {
                "total": 100 * 1024**3,
                "used": 40 * 1024**3,
                "free": 60 * 1024**3,
            },
        )()

        output = StringIO()

        with patch("sys.stdout", output):
            system_info.show_system_info()

        result = output.getvalue()

        self.assertIn("Linux", result)
        self.assertIn("test-machine", result)
        self.assertIn("100.00 GB", result)
        self.assertIn("40.00 GB", result)
        self.assertIn("60.00 GB", result)


if __name__ == "__main__":
    unittest.main()