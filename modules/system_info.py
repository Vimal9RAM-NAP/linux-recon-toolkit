import platform
import os
import shutil


def show_system_info():
    print("\n" + "=" * 45)
    print("           SYSTEM INFORMATION")
    print("=" * 45)

    print(f"Operating System : {platform.system()}")
    print(f"OS Release       : {platform.release()}")
    print(f"Architecture     : {platform.machine()}")
    print(f"Hostname         : {platform.node()}")
    print(f"Python Version   : {platform.python_version()}")

    print("\n" + "-" * 45)
    print("DISK INFORMATION")
    print("-" * 45)

    disk = shutil.disk_usage(os.path.expanduser("~"))

    total = disk.total / (1024 ** 3)
    used = disk.used / (1024 ** 3)
    free = disk.free / (1024 ** 3)

    print(f"Total Space : {total:.2f} GB")
    print(f"Used Space  : {used:.2f} GB")
    print(f"Free Space  : {free:.2f} GB")

    print("=" * 45)
