import sys
import requests
import pyfiglet
from colorama import Fore
import os.path
from os import path



def Enum_directory():
 print(Fore.CYAN+"===========================================================")
 print(Fore.WHITE+"[*-*] Starting NIRO in DIRECTORY enumeration mode ...")
 print(Fore.CYAN+"===========================================================")

 d = pyfiglet.figlet_format("Search<->DIRECTORY")
 print(Fore.MAGENTA+d)

 dir_file = str(input(Fore.BLUE+"[+] Enter directory name file location : "+Fore.WHITE))

 if (path.exists(dir_file) == True):
   directory = open(dir_file).read()
   directory_name = directory.splitlines()

   for dir in directory_name :
     dir_enum = f"http://{sys.argv[1]}/{dir}"
     r= requests.get(dir_enum)
     if r.status_code == 404:
        pass
     else:
        print(Fore.GREEN+"[+] ---> Valid Directory : ",dir_enum)

   directory.close()
 else :
    print(Fore.RED+"[-] INVALID FILE")

 print(Fore.RED+"---------------END OF DIRECTORY ENUMERATION-----------------")
