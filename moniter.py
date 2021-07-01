import subprocess
import colorama
import re


def monitor():
    print("[*]Checking for monitor mode")
    result = subprocess.run("iwconfig", shell=True, capture_output=True).stdout.decode()
    if "Managed" in result:
        print("[-]ur wireless network card is in Managed mode")
    elif "Monitor" in result:
        print("[+]its in Monitor mode")
    else:
        print("no network card")


monitor()
