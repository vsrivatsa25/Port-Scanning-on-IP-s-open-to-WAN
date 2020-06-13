import time
import multiprocessing
import nmaptest

ips= []

with open('open_ips.txt', 'r') as f:
    for line in f:
        ips.append(line[0:-1])

def scan(i):
    print(nmaptest.port_scan(ips[i]),ips[i])

if __name__ == '__main__':
    starttime = time.time()
    #set number of processes basd on your CPU capacity
    pool = multiprocessing.Pool(processes=50)
    print("Starting the port scan process...")
    pool.map(scan, range(1,len(ips)))
    pool.close()
    print("Port Scan completed...")
    print('That took {} seconds...'.format(time.time() - starttime))
    f.close()
