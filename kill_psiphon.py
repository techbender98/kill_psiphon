import os
import sys
import psutil
import time

while 1:

    services = [x for x in psutil.process_iter() if x.name().lower().startswith('psiph')]
    data = []
    i = 0
    o = 0

    for item in services:
        m = services[i]
        m = str(m)
        m = m.replace("(",",")
        m = m.replace(")","")
        m = m.replace("=",",")
        m = m.replace("'","")
        n = list(m.split(","))
        data.append(n)
        i += 1
        
    for item in data:
        kill = data[o][4]
        kill = str(kill)
        os.system("TASKKILL /F /IM %s" % (kill))
        o += 1
        
    time.sleep(5)