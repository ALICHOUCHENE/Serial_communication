import sys
import serial
import serial.tools.list_ports
import glob 
# initialisation 
ports=[]
# for linux core :
ports = serial.tools.list_ports.comports()
print(ports)

for port, desc, hwid in sorted(ports):
    print(port)
    print(type(desc))
    print(desc)
    print(type(hwid))
    print(hwid)
