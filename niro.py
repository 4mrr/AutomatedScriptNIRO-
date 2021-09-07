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

from niroIntro import welcome
from Recon import whois_enum4linux
from Recon import sub_domains
from Recon import Enum_directory
from Recon import scan_ports_tcp
from passwordSpraying.ssh_spraying import ssh_sprayingg
from passwordSpraying.ftp_spraying import ftp_sprayingg,ftp_login


def Program():

            welcome()
            whois_enum4linux()
            sub_domains()
            Enum_directory()
            scan_ports_tcp()
            ssh_sprayingg()
            ftp_sprayingg()

if __name__ == "__main__":
       Program()
       
