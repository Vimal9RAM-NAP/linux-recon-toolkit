import unittest
from unittest.mock import patch
from io import StringIO

from modules import port_scanner


class TestPortScanner(unittest.TestCase):

    @patch("builtins.input", return_value="")
    @patch("sys.stdout", new_callable=StringIO)
    def test_empty_hostname(self, mock_stdout, mock_input):
        port_scanner.scan_host()

        self.assertIn("Invalid hostname", mock_stdout.getvalue())

    @patch("builtins.input", return_value="invalid host name")
    @patch("sys.stdout", new_callable=StringIO)
    def test_hostname_with_spaces(self, mock_stdout, mock_input):
        port_scanner.scan_host()

        self.assertIn("Invalid hostname", mock_stdout.getvalue())

    @patch("builtins.input", return_value="invalid.example.invalid")
    @patch("modules.port_scanner.socket.gethostbyname", side_effect=OSError("Not found"))
    @patch("sys.stdout", new_callable=StringIO)
    def test_unresolvable_hostname(
        self,
        mock_stdout,
        mock_resolve,
        mock_input,
    ):
        import socket
        mock_resolve.side_effect = socket.gaierror("Not found")

        port_scanner.scan_host()

        self.assertIn("Could not resolve", mock_stdout.getvalue())


if __name__ == "__main__":
    unittest.main()