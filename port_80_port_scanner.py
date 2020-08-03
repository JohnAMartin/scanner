import socket
from IPy import IP

# Allow user to input an IP address to scan
ip_address = input('[+] Please Enter A Target To Scan: ')
port = 80

try:
    
    # Socket declaration, if successful we will print that port 80 is open
    sock = socket.socket()
    sock.connect((ip_address, port))
    print(f'Port 80 is open')
    
except:
    # Handling any errors, which means if the port is closed we will not crash
    print('Port 80 is closed')
    
    
