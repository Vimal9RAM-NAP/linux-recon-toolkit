import subprocess
import shutil


def run_command(command):
    """Run a Linux command and return its output."""
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=5,
            check=False
        )

        if result.returncode == 0:
            return result.stdout.strip()

        return "Information unavailable."

    except (FileNotFoundError, subprocess.TimeoutExpired):
        return "Command unavailable or timed out."


def show_network_info():
    print("\n" + "=" * 45)
    print("           NETWORK INFORMATION")
    print("=" * 45)

    commands = [
        ("Network Interfaces", ["ip", "-brief", "address"]),
        ("Routing Table", ["ip", "route"]),
        ("Default Gateway", ["ip", "route", "show", "default"]),
    ]

    for title, command in commands:
        print(f"\n--- {title} ---")

        if shutil.which(command[0]):
            output = run_command(command)
            print(output or "No information found.")
        else:
            print(f"Required command '{command[0]}' not found.")

    print("\n--- DNS CONFIGURATION ---")

    try:
        with open("/etc/resolv.conf", "r", encoding="utf-8") as file:
            dns_entries = [
                line.strip()
                for line in file
                if line.strip().startswith("nameserver")
            ]

        if dns_entries:
            print("\n".join(dns_entries))
        else:
            print("No nameserver entries found.")

    except OSError:
        print("Unable to read DNS configuration.")

    print("\n" + "=" * 45)