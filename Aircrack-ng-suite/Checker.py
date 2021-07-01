import subprocess
import time
import sys
import os
import colorama

colorama.init(autoreset=True)


def check():
    TITLE = "The Aircrack-ng Suite"
    LEN_TIT = len(TITLE)
    # Check for Linux and root
    if sys.platform.startswith("linux"):
        if os.getuid() != 0: sys.exit(colorama.Fore.RED + "[-]Run With Sudo!")
    else:
        sys.exit(colorama.Fore.RED + "[-]Works only with linux,LOL")

    print("-" * LEN_TIT)
    print(TITLE)
    print("-" * LEN_TIT)
    print(colorama.Fore.CYAN+"Finding Your OS\n")

    os_name = subprocess.run("cat /etc/os-release", shell=True, capture_output=True).stdout.decode()
    name = os_name.splitlines()
    print(colorama.Fore.GREEN+name[0])

    print("\nChecking availability of tools:\n")
    time.sleep(1)
    check_aircrack = subprocess.run("whereis aircrack-ng", shell=True, capture_output=True).stdout.decode()
    if "/usr/bin/aircrack-ng" in check_aircrack:
        print(colorama.Fore.LIGHTCYAN_EX + "[+]You got all the tools required , u are good to go!\n")
    else:
        print(colorama.Fore.RED + "[-]You don't have the tools required")
        sys.exit(colorama.Fore.RED + "Consider installing aircrack-ng\n")
