import socket


COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP Alternative",
}


def scan_host():
    print("\n" + "=" * 45)
    print("             TCP PORT SCANNER")
    print("=" * 45)

    host = input("Enter a hostname or IP address you are authorized to test: ").strip()

    if not host or any(char.isspace() for char in host):
        print("Invalid hostname or IP address.")
        return

    try:
        ip_address = socket.gethostbyname(host)
    except socket.gaierror:
        print("Could not resolve the hostname.")
        return

    print(f"\nTarget: {host} ({ip_address})")
    print("Scanning selected TCP ports...\n")

    for port, service in COMMON_PORTS.items():
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
                connection.settimeout(0.5)
                result = connection.connect_ex((ip_address, port))

                if result == 0:
                    print(f"[OPEN]   Port {port:<5} {service}")

        except OSError:
            continue

    print("\nScan complete.")
    print("=" * 45)


if __name__ == "__main__":
    scan_host()
