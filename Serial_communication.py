import os
import serial
import serial.tools.list_ports
import time
import json 
import glob 
# initialisation 
ports=[]




                    ########## detecting availables ports#########

#for win systems (just for testing)
def ports_availables() :
    p= serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(p):
        ports.append(port)
    return(ports)
    # for linux core :
    #sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
    # this excludes your current terminal "/dev/tty"
    #ports = glob.glob('/dev/tty[A-Za-z]*')

    
def connect(ports):
    global port
    baudrate=9600
    bytesize=8
    #parity=PARITY_ODD
    #stopbits=STOPBITS_ONE
    
    
    for port in ports :
        try:
            port = serial.Serial(port,baudrate,bytesize)
            print('connected sucsessefully')
        except:
            print('faile')

            
            
ports=ports_availables()
connect(ports)    
print(port)

while True :
    data=(port.readline()).decode()
    print(data)
