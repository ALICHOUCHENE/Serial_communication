import sys
import serial
import serial.tools.list_ports
import glob 
# initialisation 
ports=[]
# for linux core :
if sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
    ports = glob.glob('/dev/tty[A-Za-z]*')

for port, desc, hwid in sorted(ports):
    print(port)
    print(type(desc))
    print(desc)
    print(type(hwid))
    print(hwid)