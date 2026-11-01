def print_header(title):
    """Display a consistent section header."""
    width = 45

    print("\n" + "=" * width)
    print(title.center(width))
    print("=" * width)


def print_section(title):
    """Display a subsection heading."""
    print(f"\n--- {title} ---")


def format_bytes(size):
    """Convert bytes into a readable size."""
    units = ["B", "KB", "MB", "GB", "TB"]

    value = float(size)

    for unit in units:
        if value < 1024 or unit == units[-1]:
            return f"{value:.2f} {unit}"

        value /= 1024

    return f"{value:.2f} TB"


def get_non_empty_input(prompt):
    """Keep asking until the user enters a non-empty value."""
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")
