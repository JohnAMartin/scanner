# Changes from previous version, This version is going to allow us to convert domain names to IP addresses

import socket
from IPy import IP

# For us to see if a port is open, what we need to do is:
# 1. Connect to the target machine
# 2. Try to connect to port 80

def newLine():
    print('\n')

# We are checking to see whether the user entered an IP or a domain.  So the first part of IP(ip) will pretty much do nothing if the parameter is in the form of an IP address, just returning that.  The method of gethostname() is going to convert the domain to an IP address, and will ONLY run if we get a ValueError, which is what we will get if IP address isn't given.  
def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)
    
    
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

# Calling the function after use inputs the target
converted_ip = check_ip(ip_address)
newLine()

# Changing the IP address on this program to the converted_ip variable
for port in range(75,85):
    scan_port(converted_ip, port)
