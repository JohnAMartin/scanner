# Changes from previous version, we are going to allow multiple targets to be scanned.  Main changes here are we are omitting the closed ports from showing up as our list is growing larger.

# When we are accepting the input, we want it seperated with a comma and we will iterate over that list and split it on the comma and strip any whitespace so it is valid format

# We then pass the IP as a parameter in to the scan function, this scan function is going to call on the check_ip function to see if it is a domain or an ip and return them.  Then it will continue like it should 

import socket
from IPy import IP

# For us to see if a port is open, what we need to do is:
# 1. Connect to the target machine
# 2. Try to connect to port 80

def newLine():
    print('\n')


def scan(target):
    converted_ip = check_ip(target)
    newLine()
    print(f'Scanning Target: {target}')

    for port in range(75,85):
        scan_port(converted_ip, port)

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
       pass

targets = input('[+] Please Enter Target/s To Scan, Split with comma: ')

# Calling the function after use inputs the target
if ',' in targets:
    for ip_add in targets.split(','):
        scan(ip_add.strip(' '))
else:
    scan(targets)
newLine()

