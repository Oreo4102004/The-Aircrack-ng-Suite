import sys
import os
import subprocess
import re
import time

import colorama
import Checker

colorama.init(autoreset=True)
Checker.check()

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



print(colorama.Fore.LIGHTCYAN_EX + "[+]Putting the interface to monitor mode!")
time.sleep(1)
subprocess.run("sudo airmon-ng check kill", shell=True)
subprocess.run(f"sudo airmon-ng start {wifi_interface}", shell=True)
print(subprocess.run(f"sudo airodump-ng  {wifi_interface}mon", shell=True, capture_output=True).stdout.decode())
