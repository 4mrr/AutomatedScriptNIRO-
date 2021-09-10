from datetime import datetime
import sys
import pyfiglet
from colorama import Fore



def welcome():
	intro1 = pyfiglet.figlet_format("--->\\NIRO/<---")
	print(Fore.RED + intro1)


	now =datetime.now()
	dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

	print(Fore.WHITE+"************************************************")
	print("---------------------------------------------------------------------------------------")
	print(Fore.YELLOW + "+ URL      :            http://"+sys.argv[1])
	print(Fore.YELLOW + "+ Time     :            "+ dt_string)
	print(Fore.YELLOW + "+ Type     :            Information gathering  ")
	print(Fore.WHITE + "---------------------------------------------------------------------------------------")
	print("************************************************")
