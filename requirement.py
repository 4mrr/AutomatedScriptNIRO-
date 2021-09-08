import os 
from colorama import Fore

try :
 print(Fore.MAGENTA+"[!] Installing tools ...  ")

 print(Fore.BLUE+"\nInstalling NIKTO : ")
 print(Fore.WHITE+"")
 os.system("sudo apt-get install nikto")
 
 print(Fore.BLUE+"\nInstalling enum4linux : ")
 print(Fore.WHITE+"")
 os.system("sudo apt-get install enum4linux")

 print(Fore.BLUE+"\nInstalling DMITRY : ")
 print(Fore.WHITE+"")
 os.system("sudo apt-get install dmitry")

 print(Fore.BLUE+"\nInstalling WHOIS : ")
 print(Fore.WHITE+"")
 os.system("sudo apt-get install whois")

 print(Fore.GREEN+"[+] DONE")
except:
 print(Fore.RED+"[-] Try Again something wrong")

