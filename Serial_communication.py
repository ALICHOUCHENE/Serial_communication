import os
import serial
import serial.tools.list_ports
import time
import json 
import glob 
# initialisation 
ports=[]




                    ########## detecting availables ports#########

def ports_availables() :
    
    #for win systems (just for testing)
    p = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(p):
        if  desc == "Arduino Uno ("+str(port)+")" :
        
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
print(ports)
connect(ports)    
try:
    while True :
        if port.in_waiting :
            data=(port.readline()).decode()
            print(data)
except KeyboardInterrup :
        pass
