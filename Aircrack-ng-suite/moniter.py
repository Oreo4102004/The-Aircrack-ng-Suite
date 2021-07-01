import subprocess
import re
import colorama
import sys


def monitor():
    print("[*]Checking for monitor mode")
    result = subprocess.run("iwconfig", shell=True, capture_output=True).stdout.decode()
    if "Managed" in result:
        return False
    elif "Monitor" in result:
        return True


def check_wireless():
    wlan_pattern = re.compile("^wlp3s[0-9]+")

    wifi_check = wlan_pattern.findall(
        subprocess.run("iwconfig", shell=True, capture_output=True).stdout.decode())
    if len(wifi_check) == 0:
        sys.exit(colorama.Fore.RED + "[-]You got no wireless interface")

    print(colorama.Fore.BLUE + "The following wireless interface are available:")
    for index, item in enumerate(wifi_check):
        wifi_string = f"    {colorama.Fore.GREEN + str(index)}                {colorama.Fore.CYAN + str(item)}"
        print("-" * len(wifi_string))
        print(wifi_string)
        print("-" * len(wifi_string))

    while True:
        wifi_interface_choice = input("Select the number of the wifi interface:\n")
        try:
            if wifi_check[int(wifi_interface_choice)]:
                break
        except:
            print(colorama.Fore.RED + "[-]Not a valid choice")

    wifi_interface = wifi_check[int(wifi_interface_choice)]
    return wifi_interface
