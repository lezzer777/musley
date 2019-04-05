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

def nmap(addr):
    print("Starting Nmap 7.70 ( https://nmap.org ) at " + str(datetime.date.today()))
    time. sleep(4)
    print("Nmap scan report for " + addr.ip)
    print("Host is up (" + str(random.random()) + " lattency).")
    print("Not shown: " + str(1000 - len(addr.openPorts)) + " closed ports")
    print("PORT    STATE    SERVICE")
    if "smb" in addr.openPorts:
        print("139/smb   open    windows")
    if "tcp" in addr.openPorts:
        print("8080    open    whoknows")
nmap(evilcorp)
