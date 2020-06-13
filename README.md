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

> This project is only intended for educational/research purposes. Misuse of program may lead to legal and criminal consequences. Credit author if you use this for personal/academic use.
