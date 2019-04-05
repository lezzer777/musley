import libtvs
import time
import datetime
import random

class addr:
    openPorts = []
    ip = ""
    isActive = False

    def __init__(self, openPorts, ip, isActive):
        self.openPorts = openPorts
        self.ip = ip
        self.isActive = isActive

# Initializtation
evilcorp = addr(["tcp", "smb"], "228.6.6.31", True)
adresses = [evilcorp]

def nmap(ip):
    obj = None
    print("Starting Nmap 7.70 ( https://nmap.org ) at " + str(datetime.date.today()))
    time.sleep(4)

    for adress in adresses:
        if ip == adress.ip:
            obj  = adress
    
    if obj != None:
        print("Nmap scan report for " + ip)
        print("Host is up (" + str(random.random()) + " lattency).")
        print("Not shown: " + str(1000 - len(adress.openPorts)) + " closed ports")
        print("PORT    STATE    SERVICE")
        if "smb" in adress.openPorts:
            print("139/smb   open    windows")
        if "tcp" in adress.openPorts:
            print("8080      open    whoknows")
    else:
        print("Host is down")
nmap("228.6.6.31")
nmap("flex")
