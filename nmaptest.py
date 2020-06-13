import nmap3
nmap = nmap3.Nmap()
def port_scan(ip):
    try:
        results = nmap.scan_top_ports(ip)
        results = results[ip]
        for i in range(len(results)):
            if results[i]['state'] =='open':
                with open('nmap_open_ports.txt', 'a') as fz:
                    fz.write(results[i]['host']+ " has open port at "+results[i]['portid']+"\n")
                fz.close()
    except:
        port_scan(ip)

    return "Port scan successful"
