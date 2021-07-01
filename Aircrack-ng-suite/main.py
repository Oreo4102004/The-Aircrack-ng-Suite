import sys
import subprocess
import time
import moniter
import colorama
import Checker


colorama.init(autoreset=True)

Checker.check()
wifi_interface = moniter.check_wireless()
monitor_check = moniter.monitor()

if monitor_check is True:
    print(colorama.Fore.LIGHTCYAN_EX + "[+]It is already in monitor mode")
    print(colorama.Fore.LIGHTCYAN_EX + "[+]Starting scan")

elif monitor_check is False:
    print(colorama.Fore.LIGHTCYAN_EX + "[+]Putting the interface to monitor mode!")
    time.sleep(1)
    subprocess.run("sudo airmon-ng check kill", shell=True)
    subprocess.run(f"sudo airmon-ng start {wifi_interface}", shell=True)

print(colorama.Fore.LIGHTCYAN_EX + "[+]Done!")

while True:
    start_scan = input("Start Scan? (Y/n):")
    if start_scan.lower() == 'y':
        print("[+]Starting The Scan!")
        # insert code here
        break
    elif start_scan.lower() == 'n':
        while True:
            exit_check = input("[*]Do You Want To Exit(Y/n):")
            if exit_check.lower() == 'n':
                break
            elif exit_check.lower() == 'y':
                sys.exit('Exiting!')
            else:
                print(colorama.Fore.RED + "[-]not a valid argument")
                continue
    else:
        print(colorama.Fore.RED + "[-]Not a valid argument")
        continue
