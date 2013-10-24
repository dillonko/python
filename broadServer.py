#broadServer.py - Liam McSherry

import socket
import time
import urllib

DEV = True
gip = "http://automation.whatismyip.com/n09230945.asp"

# Miscellaneous
def fopen(filename):
        filename = open(filename, 'w')
        filename.close()
def fwrite(filename, lines):
        filename = open(filename, 'w')
        count = 0
        while len(lines) -1 >= count:
                filename.write(lines[count] + "\n")
                count += 1
        filename.close()
def fread(filename):
        filename = open(filename)
        __read = filename.read()
        filename.close()
        return __read

# broadServer Methods
def RunSrv():
        host = raw_input("Host>")
        port = input("Port>")
        data = raw_input("Data>")
        t = input("Time (sec)>")
                
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        doRun = True
        timesRun = 0
        while doRun:
                s.sendto(data, (host,port))
                if timesRun < 1:
                        print("Sent: " + data)
                        timesRun += 1
                else:
                        timesRun += 1
                if timesRun == t:
                        print("Finished sending.")
                        doRun = False
                time.sleep(1)
def intCmd(command):
        if command == "broadcast":
                RunSrv()
        elif command == "exit":
                exit()
        elif command == "packet":
                print("\nPacket Controls")
                print("->create    :  Create a .EEPF file for broadcasting.")
                print("")
        elif command == "packet->create":
                createPkt()
def createPkt():
        pHdr = raw_input("Method [MSG]?> ") # Packet Header
        pTyp = raw_input("Type [TEXT\PLAIN]?> ") # Transmit Type
        uip = urllib.urlopen(gip).read()
        pSIP = uip
        print("Sender IP?> " + pSIP)
        pCtn = raw_input("Content?> ")
        pFtr = "END"
        print("Packet Footer:" + pFtr)
        if DEV:
                print("\nDebug Print")
                print("-- -- -- -- -- -- -- --")
                print(
                        "PKTHDR:"+pHdr+"\n"+
                        "PKTTYP:"+pTyp+"\n"+
                        "PKTSDR:"+pSIP+"\n"+
                        "PKTCTN:"+pCtn+"\n"+
                        "PKTFTR:"+pFtr)
                print("-- -- -- -- -- -- -- --")
        fwrite("packet.epf", ["%EEPF",pHDR,pTyp,pSIP,pCtn,pFtr])
i = 0
keep = True
keepServer = True
print("Broadcast Server...")
print("Starting up...")
print("Please Wait...")
while keep:
        intCmd(raw_input("EmuOS:BroadcastServer?>"))
                        