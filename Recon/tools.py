import pyfiglet 
from colorama import Fore
import sys
import os 



def tools_recon():
  
  #*****************************run the tool WHOIS *******************************
  
  print(Fore.CYAN+"===========================================================")
  print(Fore.WHITE + "[*-*] Starting NIRO with WHOIS Enemuration ...")
  print(Fore.CYAN+"===========================================================")
 
  p = pyfiglet.figlet_format("WHOIS")
  print(Fore.MAGENTA+p)
  print(Fore.YELLOW+"")
  
  os.system("whois "+sys.argv[1])    
  
  print(Fore.RED+"---------------END OF WHOIS-----------------")
  
  #*****************************run the tool Enum4linux *******************************
  
  print(Fore.CYAN+"===========================================================")
  print(Fore.WHITE + "[*-*] Starting NIRO with Enum4linux Enemuration ...")
  print(Fore.CYAN+"===========================================================")
  
  p = pyfiglet.figlet_format("WHOIS")
  print(Fore.MAGENTA+p)
  print(Fore.YELLOW+"")
  
  os.system("enum4linux -a "+sys.argv[1]) 
  
  print(Fore.RED+"---------------END OF Enum4linux-----------------")
  
  #*****************************run the tool NIKTO *******************************
  
  print(Fore.CYAN+"===========================================================")
  print(Fore.WHITE + "[*-*] Starting NIRO with NIKTO Enemuration ...")
  print(Fore.CYAN+"===========================================================")
  
  p = pyfiglet.figlet_format("NIKTO")
  print(Fore.MAGENTA+p)
  print(Fore.YELLOW+"")
  
  os.system("nikto --host "+sys.argv[1])   
  
  print(Fore.RED+"---------------END OF NIKTO-----------------")
  
  #*****************************run the tool DMITRY *******************************
  
  print(Fore.CYAN+"===========================================================")
  print(Fore.WHITE + "[*-*] Starting NIRO with DMITRY Enemuration ...")
  print(Fore.CYAN+"===========================================================")
  
  p = pyfiglet.figlet_format("DMITRY")
  print(Fore.MAGENTA+p)
  print(Fore.YELLOW+"")
  
  os.system("dmitry "+sys.argv[1])  
  
  print(Fore.RED+"---------------END OF Dmitry-----------------")
  
  #*****************************run the tool WAFW00F *******************************
  
  print(Fore.CYAN+"===========================================================")
  print(Fore.WHITE + "[*-*] Starting NIRO with WafW00f Detection ...")
  print(Fore.CYAN+"===========================================================")
  
  os.system("wafw00f -a -v "+sys.argv[1])
  
  print(Fore.RED+"---------------END OF waffW00f-----------------")
