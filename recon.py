from modules import system_info, network_info, file_info, port_scanner


def display_banner():
    print("=" * 45)
    print("          LINUX RECON TOOLKIT")
    print("=" * 45)
    print("  A beginner-friendly Linux learning tool")
    print()


def display_menu():
    print("[1] System Information")
    print("[2] Network Information")
    print("[3] File Information")
    print("[4] Port Scanner")
    print("[5] Exit")
    print()


def main():
    display_banner()

    while True:
        display_menu()
        choice = input("Select an option: ").strip()

        if choice == "1":
            system_info.show_system_info()

        elif choice == "2":
            network_info.show_network_info()
        
        elif choice == "3":
            print("\nFile Information is coming soon.")

        elif choice == "4":
            print("\nPort Scanner is coming soon.")

        elif choice == "5":
            print("\nExiting Linux Recon Toolkit. Goodbye!")
            break

        else:
            print("\nInvalid option. Please enter a number from 1 to 5.")

        print()


if __name__ == "__main__":
    main()
