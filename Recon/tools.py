import pyfiglet 
from colorama import Fore
import sys
import os 



def whois_enum4linux():
  print(Fore.CYAN+"===========================================================")
  print(Fore.WHITE + "[*-*] Starting NIRO with WHOIS Enemuration ...")
  print(Fore.CYAN+"===========================================================")
 
  p = pyfiglet.figlet_format("WHOIS")
  print(Fore.MAGENTA+p)
  print(Fore.YELLOW+"")
  
  os.system("whois "+sys.argv[1])   #run the whois command
  
  print(Fore.RED+"---------------END OF WHOIS-----------------")
  
  print(Fore.CYAN+"===========================================================")
  print(Fore.WHITE + "[*-*] Starting NIRO with WHOIS Enemuration ...")
  print(Fore.CYAN+"===========================================================")
  
  p = pyfiglet.figlet_format("WHOIS")
  print(Fore.MAGENTA+p)
  print(Fore.YELLOW+"")
  
  os.system("enum4linux -a "+sys.argv[1])   #run the "enum4linux -a" command
  
  print(Fore.RED+"---------------END OF Enum4linux-----------------")
