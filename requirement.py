import os 
from colorama import Fore

try :
 print(Fore.MAGENTA+"[!] Installing tools ...  ")

 print(Fore.BLUE+"\n[+] Installing NIKTO : ")
 print(Fore.WHITE+"")
 os.system("sudo apt-get install nikto")
 
 print(Fore.BLUE+"\n[+] Installing enum4linux : ")
 print(Fore.WHITE+"")
 os.system("sudo apt-get install enum4linux")

 print(Fore.BLUE+"\n[+] Installing DMITRY : ")
 print(Fore.WHITE+"")
 os.system("sudo apt-get install dmitry")

 print(Fore.BLUE+"\n[+] Installing WHOIS : ")
 print(Fore.WHITE+"")
 os.system("sudo apt-get install whois")

 print(Fore.BLUE+"\n[+] Installing WafW00f : ")
 print(Fore.WHITE+"")
 os.system("sudo apt-get install wafw00f")
 
 
 print(Fore.BLUE+"\n[+] Installing TheHarvester : ")
 print(Fore.WHITE+"")
 os.system("sudo apt-get install theharvester")
 
 
 print(Fore.GREEN+"[+] DONE")
except:
 print(Fore.RED+"[-] Try Again something WRONG")

