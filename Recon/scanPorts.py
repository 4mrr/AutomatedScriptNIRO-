import socket
import sys
import pyfiglet
import requests
import os.path
from os import path
from colorama import Fore


def intro_scanPort():
 print(Fore.CYAN+"===========================================================")
 print(Fore.WHITE + "[*-*] Starting NIRO in PORT SCANNING mode ...")
 print(Fore.CYAN+"===========================================================")
 
 p = pyfiglet.figlet_format("PORT-SCANNING")
 print(Fore.MAGENTA+p)


def probe_port(ip,port,result=1):
   try:
     sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
     sock.settimeout(5)
     r= sock.connect_ex((ip,port))
     if r == 0:
        result = r
     sock.close()
   except Exception as e:
     pass
   return result


def scan_ports_tcp():
  intro_scanPort()
  open_ports=[]
  ports=range(1,5000)
  for port in ports:
     sys.stdout.flush()
     response= probe_port(sys.argv[1],port)
     if response == 0:
         open_ports.append(port)

  if open_ports:
    print(Fore.GREEN+"Open Ports are : ")
    print(sorted(open_ports))
  else:
    print(Fore.RED+"[-] Looks like no ports are open") 
  
  print(Fore.RED+"---------------END OF PORT SCANNING-----------------")

