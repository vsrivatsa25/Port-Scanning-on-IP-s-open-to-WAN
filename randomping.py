import subprocess
import re
import random
import socket
import struct
import multiprocessing
import time

def gen_ip():
    return(socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff))))


def osping(ip):
    try:
        command = 'ping ' + ip + ' -n 1 -l 1 -w 1000'
        ans = str(subprocess.check_output(command, shell=True))
        pattern = "(time)=([0-9]+)ms TTL"
        regex = re.compile(pattern)
        ans2 = regex.findall(ans)
        if len(ans2) == 1:
            return ans2[0][1]
    except:
        pass


def multiprocessing_func(i):
    try:
        ip = gen_ip()
        ans = osping(ip)
        if ans:
            return(ip)
    except:
        pass


if __name__ == '__main__':
    starttime = time.time()
    #set number of processes basd on your CPU capacity
    pool = multiprocessing.Pool(processes=50)
    print("Starting the ping process...")
    vals = pool.map(multiprocessing_func, range(1000))
    print("Ping successful...")
    print('That took {} seconds...'.format(time.time() - starttime))
    pool.close()
    with open('open_ips.txt', 'a+') as f:
        print("File opened...")
        for ip in vals:
            if ip:
                f.write("%s\n" % ip)
    print("File closed...")
    f.close()