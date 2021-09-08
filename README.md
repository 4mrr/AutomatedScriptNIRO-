# ScriptAutomatis-
 
![Supported Python versions](https://img.shields.io/badge/python-3.8+-blue.svg)
 
Created By  : EN-NIARI AMR </br>
Framed By   : EL Mostapha chakir </br>
Inspired By : ReconFTW & Black-Dragon & SN1PER </br>

 
 
 
# Description
 
**NIRO** automates the entire process of reconnaisance for you.

it is used in the phase of Footprinting & reconnaissance.
 
* NIRO uses lot of tactiques for reconnaissance for example : subdomain enumeration and search directory and ports scanning which helps you getting the maximum and the most interesting subdomains and directory so that you be ahead of the competition.

* NIRO also use WHOIS and Enum4linux tools of linux in order to properly collect information. 

* NIRO is intended to be a speedy, massively parallel, modular, login brute-forcer.The goal is to support two services that allow remote authentication as possible :

#### SSH brute force attack :

* NIRO performs SSH brute force, because it is one of the most reliable ways to gain SSH access to servers is by brute-forcing credentials. that will ultimately lead to the discovery of valid login credentials. 
 
#### FTP brute force attack :

* NIRO performs FTP brute force, because FTP (File Transfer Protocol ) is a network protocol used to transfer files, it is also the most way to gain access to FTP server for collectiong more informations. 

So, what are you waiting for Go Go Go!  :boom:


# 💿 Installation & Usage 💿 :
**Niro** is a script of python3, so first of all you have to download python version > 3 :

```bash
sudo apt-get update
sudo apt-get install python3.6
```
or 

```bash
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.8
```
depending on the version of the machine used

and then download the script with the command line linux :</br>
Note: *To use tools of niro you should to download them by  **requirement.py**: `python3 requirement.py`*

**All in one:**
```bash
git clone https://github.com/amr-en-niari/AutomatedScriptNIRO-.git
cd AutomatedScriptNIRO-/
python3 requirement.py
python3 niro.py <Target IP>
```
and you can download also the wordlist of subdomains and directory by the command line linux for using them in the script or use another wordlist :
```bash
wget https://raw.githubusercontent.com/amr-en-niari/AutomatedScriptNIRO-/main/the%20Wordlists/Subdomain.txt
wget https://raw.githubusercontent.com/amr-en-niari/AutomatedScriptNIRO-/main/the%20Wordlists/directory-list-2.3-medium.txt
wget https://raw.githubusercontent.com/amr-en-niari/AutomatedScriptNIRO-/main/the%20Wordlists/ftp_wordlist.txt
wget https://raw.githubusercontent.com/amr-en-niari/AutomatedScriptNIRO-/main/the%20Wordlists/ssh_wordlist.txt
```
and at the end to run the script you have to write the command line :
```bash
python3 niro.py <IP Target>
```
# :fire: Features :fire:

* WHOIS
* enum4linux
* Nikto
* Dmitry
* SUBDOMAINS
* SEARCH DIRECTORY ONLINE OF WEB
* PORT SCANNING
* PASSWORD SPRYING :<br/>
[+] SSH Brute Force.<br/>
[+] FTP Brute Force

# :boom: Simple Usage :boom:

there's some pictures of NIRO :

* Whois

![Screenshot (800)](https://user-images.githubusercontent.com/65505262/132423381-bff536b3-1153-4cb6-9499-9b625ba35c5b.png)

* enum4linux

![Screenshot (801)](https://user-images.githubusercontent.com/65505262/132423417-ac28c407-42ae-4067-b3f0-8b35965906c8.png)

* Sub domain :

![Screenshot (793)](https://user-images.githubusercontent.com/65505262/132023360-30a2ec10-f7d5-403a-ad51-b18ac36b1211.png)

* Search Directory :

![Screenshot (794)](https://user-images.githubusercontent.com/65505262/132024338-a5df8060-640f-4a27-8be4-b7963eca4f74.png)


* Port Scanning :

![Screenshot (795)](https://user-images.githubusercontent.com/65505262/132029006-7c8caa8c-0fed-437d-abd9-93ac2c596588.png)


* SSH Brute Force :

![Screenshot (798)](https://user-images.githubusercontent.com/65505262/132051333-e7a0a1bf-d46e-4f0e-95ad-d17e978cf5af.png)


* FTP Brute Force :

![Screenshot (799)](https://user-images.githubusercontent.com/65505262/132051246-bc64f008-36be-416c-bf77-0c9b5055fb41.png)


