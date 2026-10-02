import subprocess
from unicodedata import name

profiles = subprocess.check_output("netsh wlan show profiles",
                                   shell=True).decode()

names = [line.split(":")[1].strip()
         for line in profiles.split("\n") 
         if "All User Profile" in line]
for i, n in enumerate(names, 1):
    print(f"[{i}] {n}")

    ch = int(input("\n Choose Wifi number:"))
    wifi = name[ch - 1]
    result = subprocess.check_output(
f"netsh wlan show profile \"{wifi}\" key=clear", 
shell=True).decode()
    print("\n" + result)
    