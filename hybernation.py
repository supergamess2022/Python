from colorama import Fore, init
import os
import time

init()
system = int(input(Fore.BLUE + "Вкажть свою систему: 1)Windows 2)Linux  (1 або 2)  "))

if system == 2:
    time.sleep(0.5)
    print(Fore.GREEN + "Wait.")
    time.sleep(0.8)
    print(Fore.YELLOW + "Wait..")
    time.sleep(0.8)
    print(Fore.RED + "Wait...")
    time.sleep(2)
    os.system("sudo pm-suspend")

if system == 1:
    time.sleep(0.5)
    print(Fore.GREEN + "Wait.")
    time.sleep(0.8)
    print(Fore.YELLOW + "Wait..")
    time.sleep(0.8)
    print(Fore.RED + "Wait...")
    time.sleep(2)
    os.system("shutdown /s")