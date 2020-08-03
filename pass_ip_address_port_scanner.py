# Changes from previous scanner, going to wrap this in a function so that we can pass in IP Address and predefined port scanner

import socket
from IPy import IP

# For us to see if a port is open, what we need to do is:
# 1. Connect to the target machine
# 2. Try to connect to port 80

def newLine():
    print('\n')

def scan_port(ip_address, port):
    
    try :
        # Socket declaration
        sock = socket.socket()
        
        # Socket timeout is how long we want to check on each port, the longer we check the more accurate we are but we do not want to take forever
        sock.settimeout(0.5)
        
        sock.connect((ip_address, port))
        print(f'[+] - Port {port} is open')

    except:
        # Handles the error of a port being closed
        print(f'[-] - Port {port} is closed')

ip_address = input('[+] Please Enter A Target To Scan: ')
newLine()

# Usually port 80 will be open on whatever website IP you decide to scan, but you can substitute the range numbers for whichever ports you would like to scan, the scan will start at the first number, and then go up to but not including the second number
for port in range(75,85):
    scan_port(ip_address, port)
