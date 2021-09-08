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
#---> The library Recon is about functions of footprinting & reconnaissance
#---> The library passwordSpraying is about brute force attack (FTP & SSH)


from niroIntro import welcome
from Recon import tools_recon
from Recon import sub_domains
from Recon import Enum_directory
from Recon import scan_ports_tcp
from passwordSpraying.ssh_spraying import ssh_sprayingg
from passwordSpraying.ftp_spraying import ftp_sprayingg,ftp_login


def Program():

            welcome()                 #call the welcome function, it's about the logo of NIRO
            tools_recon()             #call some of tools of kali linux for more informations (whois/enum4linux/dmitry/nikto ...)  
            sub_domains()             #call function of search sub-domains  
            Enum_directory()          #call function of search directory
            scan_ports_tcp()          #call function of port scanning
            ssh_sprayingg()           #call function of ssh brute-forcing
            ftp_sprayingg()           #call function of ftp brute-forcing

if __name__ == "__main__":
       Program()                       #main program
       
