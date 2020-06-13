# Port-Scanning-on-IP-s-open-to-WAN
Uses BeyondPing first to get a list of randomly generated IP addresses that are open to WAN ping and attempt port scanning on the selected IP Addresses using portscanner 

### PRE-REQUISITES:
Open cmd and cd into your virtual environment. Then, 
```python
pip install -r requirements.txt
```

### STEPS:

1) Find IP addresses open to WAN ping which may be better candidates for open ports by running randomping.py. Output is saved to open_ips.txt
2) Using the results of open_ips.txt, perform port scanning on the suspected IPs using Nmap by running port_scan.py.
3) Analyse output from nmap_open_ports.txt where you will find a list of open ports on the above IP addresses.

#### DISCLAIMER:

>Use of this program means agreement to the following terms:

>1. Information provided in here are for educational purposes only. The author is no way responsible for any misuse of the information.

>2. I will not be responsible for any direct or indirect damage caused due to the usage of the information provided on this site.This project is only intended for educational/research purposes. Misuse of program may lead to legal and criminal consequences.

>3. Credit author if you use this for personal/academic use.
