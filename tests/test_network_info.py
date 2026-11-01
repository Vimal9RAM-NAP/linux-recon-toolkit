import unittest
from unittest.mock import patch, mock_open
from io import StringIO

from modules import network_info


class TestNetworkInfo(unittest.TestCase):

    @patch("modules.network_info.shutil.which", return_value="/usr/sbin/ip")
    @patch("modules.network_info.run_command", return_value="eth0 UP 192.168.1.10")
    @patch("sys.stdout", new_callable=StringIO)
    def test_show_network_info(
        self,
        mock_stdout,
        mock_run_command,
        mock_which,
    ):
        with patch(
            "builtins.open",
            mock_open(read_data="nameserver 8.8.8.8\n"),
        ):
            network_info.show_network_info()

        output = mock_stdout.getvalue()

        self.assertIn("NETWORK INFORMATION", output)
        self.assertIn("eth0 UP 192.168.1.10", output)
        self.assertIn("8.8.8.8", output)

    @patch("modules.network_info.shutil.which", return_value=None)
    @patch("sys.stdout", new_callable=StringIO)
    def test_missing_ip_command(self, mock_stdout, mock_which):
        network_info.show_network_info()

        output = mock_stdout.getvalue()
        self.assertIn("not found", output)


if __name__ == "__main__":
    unittest.main()