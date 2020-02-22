# Basic port scanner
import sys, socket, subprocess
from datetime import datetime
 
subprocess.call('clear', shell=True)
remoteServer1 = input("Enter the remote host to scan: ")
remoteServerIP1 = socket.gethostbyname(remoteServer1)
print("Wait... scanning host", remoteServerIP1)
# start timer
t01 = datetime.now()
# Use range function to scan a range of ports like this:
try:
    for port in range(1025):
        print(port)
        socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = socket1.connect_ex((remoteServerIP1, port))
    if result == 0:
        print("Port {}: Open".format(port))
        socket1.close()
    # Handle errors:
except KeyboardInterrupt:
    print("Ctrl+C pressed ")
    sys.exit()
except socket.gaierror:
    print('Hostname unresolved... quitting')
    sys.exit()
except socket.error:
    print("Connection to server failed")
    sys.exit()
# time duration
t02 = datetime.now()
totalTime = t02 - t01
print('Scan duration: ', totalTime)
