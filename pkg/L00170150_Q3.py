""""
#
# File              :L00170150_Q3.py
# created           :29/11/2021 21:14
# Author            :Neha Tripathi
# Version           :v1.0.0
# Licencing         :2021 Neha Tripathi
# Description       :Open SSH connection and check connection
#                    
#
#
"""

import paramiko
import time
import re


# Open SSH connection to the device
# first install ssh-server on the VM
#           sudo apt install openssh-server openssh-client
#
def ssh_connection(ip):
    """
      Establish a connection to the virtual machine using
      an instance of the paramiko.SSHClient()

      Parameters:
          ip address of virtual machine

      Returns:
          none
    """
    try:
        username = "l00170150"
        password = "Study10"

        print("Establishing a connection...")
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip.rstrip("\n"), username=username, password=password)
        connection = session.invoke_shell()
        time.sleep(1)

        vm_output = connection.recv(65535)
        if re.search(b"% Invalid input", vm_output):
            print("There was at least one IOS syntax error on device {}".format(ip))
        else:
            print("Commands successfully executed on {}".format(ip))
        session.close()
    except paramiko.AuthenticationException:
        print("Authentication Error")


if __name__ == "__main__":
    '''
      Main method of application
    
    '''
    ssh_connection("192.168.43.128")  # ip address of my VM, adjust to suit
