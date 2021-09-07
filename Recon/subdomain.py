import sys
from colorama import Fore
import requests
import os.path
import pyfiglet
from os import path



def sub_domains():
  print(Fore.CYAN+"===========================================================")
  print(Fore.WHITE + "[*-*] Starting NIRO in SUBDOMAIN enumeration mode ...")
  print(Fore.CYAN+"===========================================================")

  s = pyfiglet.figlet_format("SUB-DOMAIN")
  print(Fore.MAGENTA+s)
  sub_file = str(input(Fore.BLUE+"[+] Enter subdomains file location : "+Fore.WHITE))
  if(path.exists(sub_file) == True):
    sub_list = open(sub_file).read()
    subdoms = sub_list.splitlines()
    for sub in subdoms:
      sub_domains = f"http://{sub}.{sys.argv[1]}"
      try :
          requests.get(sub_domains)
      except requests.ConnectionError:
          pass
      else:
          print(Fore.GREEN +"[+] --> Valid domain : ",sub_domains)

  else:
     print(Fore.RED+"[-] INVALID FILE")

  print(Fore.RED+"---------------END OF SUBDOMAIN ENUMERATION-----------------")
