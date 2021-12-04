"""
#
# File              :L00170150_Q4.py
# created           :01/12/2021 23:12
# Author            :Neha Tripathi
# Version           :v1.0.0
# Licencing         :2021 Neha Tripathi
# Description       :Find the ports are open and display the info
#
#
"""

import socket
import subprocess
import sys
from datetime import datetime


def port_scan():
    """
      Function to scan ports on a system to find open ports

    """
    # Clear the screen  #use clear if running in  *nix
    subprocess.call("cls", shell=True)

    # Ask for input
    remote_server = input("Enter a remote host to scan: ")
    remote_server_ip = socket.gethostbyname(remote_server)

    # Print a nice banner with information on which host we are about to scan
    print("-" * 60)
    print("Please wait, scanning remote host", remote_server_ip)
    print("-" * 60)

    # Check what time the scan started
    t1 = datetime.now()

    # Using the range function to specify ports (here it will scans all ports between 1 and 1024)
    # We also put in some error handling for catching errors
    port_dict = {
        22: "SSH",
        80: 'HTTP'
    }
    try:
        # try 1, 1025 if you have time
        for port in range(1, 81):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remote_server_ip, port))
            if result == 0:
                print("Port {}: 	 Open".format(port_dict.get(port)))
            sock.close()
    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

    # Checking the time again
    t2 = datetime.now()

    # Calculates the difference of time, to see how long it took to run the script
    total = t2 - t1

    # Printing the information to screen
    print('Scanning Completed in: ', total)


if __name__ == "__main__":
    '''
          Main method of application

    '''
    port_scan()
