import os
import stat
import pwd
import grp
from pathlib import Path
from datetime import datetime


def format_permissions(mode):
    """Convert file permission bits into readable Linux permissions."""
    return stat.filemode(mode)


def show_file_info():
    print("\n" + "=" * 45)
    print("             FILE INFORMATION")
    print("=" * 45)

    user_path = input("Enter a file or directory path: ").strip()

    if not user_path:
        print("Error: Path cannot be empty.")
        return

    path = Path(user_path).expanduser()

    try:
        if not path.exists() and not path.is_symlink():
            print(f"Error: '{path}' does not exist.")
            return

        info = path.lstat()

        print("\n--- BASIC INFORMATION ---")
        print(f"Path             : {path.resolve(strict=False)}")
        print(f"Name             : {path.name or str(path)}")

        if path.is_symlink():
            print("Type             : Symbolic link")
            print(f"Link Target      : {os.readlink(path)}")
        elif path.is_file():
            print("Type             : Regular file")
        elif path.is_dir():
            print("Type             : Directory")
        else:
            print("Type             : Other")

        print("\n--- SIZE INFORMATION ---")

        if stat.S_ISREG(info.st_mode):
            print(f"Size             : {info.st_size} bytes")
            print(f"Size             : {info.st_size / 1024:.2f} KB")
        elif stat.S_ISDIR(info.st_mode):
            print("Size             : Directory metadata size")
            print(f"Size             : {info.st_size} bytes")
            print("Note             : Contents are not included.")
        else:
            print(f"Size             : {info.st_size} bytes")

        print("\n--- PERMISSIONS ---")
        print(f"Permissions      : {format_permissions(info.st_mode)}")
        print(f"Permission Bits  : {stat.S_IMODE(info.st_mode):04o}")

        print("\n--- OWNER INFORMATION ---")

        try:
            owner = pwd.getpwuid(info.st_uid).pw_name
        except KeyError:
            owner = str(info.st_uid)

        try:
            group = grp.getgrgid(info.st_gid).gr_name
        except KeyError:
            group = str(info.st_gid)

        print(f"Owner            : {owner}")
        print(f"Group            : {group}")

        print("\n--- TIMESTAMPS ---")

        modified = datetime.fromtimestamp(info.st_mtime)
        changed = datetime.fromtimestamp(info.st_ctime)

        print(f"Last Modified    : {modified}")
        print(f"Metadata Changed : {changed}")

        print("\n" + "=" * 45)

    except PermissionError:
        print("Error: You do not have permission to inspect this path.")
    except OSError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    show_file_info()