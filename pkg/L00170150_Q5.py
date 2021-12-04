"""
#
# File              :L00170150_Q4.py
# created           :02/12/2021 02:07
# Author            :Neha Tripathi
# Version           :v1.0.0
# Licencing         :2021 Neha Tripathi
# Description       :Check the connection and run commands
#
#
"""

import paramiko
import time


def ssh_connection(ip):
    """
      Function to check ssh connection
    """
    global user_file
    global cmd_file
    try:
        # selected_user_file = open(user_file,'r')
        ip = "192.168.43.128"
        user_name = "l00170150".rstrip("\n")
        user_password = "Study10".rstrip("\n")
        session = paramiko.SSHClient()

        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip.rstrip("\n"), username=user_name, password=user_password)
        connection = session.invoke_shell()
        commands = ['sudo apt install curl', 'mkdir -p Labs/{Lab1,Lab2}', 'ls -l\n']
        for command in commands:
            print(f"{'#' * 10} Executing the command : {command} {'#' * 10}")
            stdin, stdout, stderr = session.exec_command(command)
            time.sleep(1)
            print(stdout.read().decode())

        session.close()
    except paramiko.AuthenticationException:
        print("Authentication Error")


if __name__ == "__main__":
    '''
          Main method of application

    '''
    ssh_connection("192.168.43.128")
