import subprocess


def monitor():
    print("[*]Checking for monitor mode")
    result = subprocess.run("iwconfig", shell=True, capture_output=True).stdout.decode()
    if "Managed" in result:
        return False
    elif "Monitor" in result:
        return True
