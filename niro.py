#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  This program is free software; you can redistribute it and/or modify
#  it.
#
#  Authored By : EN-NIARI AMR
#  Framed By   : EL MOSTAPHA CHAKIR



import os
import sys
from colorama import Fore

sys.path.append("..")

#The libraries I used

from niroIntro import welcome
from Recon import whois_enum4linux
from Recon import sub_domains
from Recon import Enum_directory
from Recon import scan_ports_tcp
from passwordSpraying.ssh_spraying import ssh_sprayingg
from passwordSpraying.ftp_spraying import ftp_sprayingg,ftp_login


def Program():

            welcome()                 #call the welcome function, it's about the logo of NIRO
            whois_enum4linux()        #call whois and enum4linux tools of kali linux for more informations  
            sub_domains()             #call function of search sub-domains  
            Enum_directory()          #call function of search directory
            scan_ports_tcp()          #call function of port scanning
            ssh_sprayingg()           #call function of ssh brute-forcing
            ftp_sprayingg()           #call function of ftp brute-forcing

if __name__ == "__main__":
       Program()                       #main program
       
