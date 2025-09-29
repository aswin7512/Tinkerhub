import socket
import sys
from datetime import datetime
# Get target from user input
target = input("Enter the target IP address: ")
# Set a range of ports to scan
start_port = 1
end_port = 1000
print("-" * 50)
print("Scanning target: " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)
try:
    # Loop through all ports
    for port in range(start_port, end_port + 1):
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        # Check if the port is open
        result = s.connect_ex((target, port))
        if result == 0:
            print("Port {} is open".format(port))
        # Close the socket
        s.close()
except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()
except socket.error:
    print("Could not connect to server.")
    sys.exit()