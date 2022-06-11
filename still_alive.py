"""
Put this on a server/machine on campus, run it every 5 min with cron or make a systemd unit+timer.
"""

import paramiko

# wireguard tunnel, p2p
server_ip ="10.11.12.4"
server_username = "epss_check"
server_password = "########"

ssh = paramiko.SSHClient()

def its_alive(ip_address, username, password, command):

    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(server_ip,
                    username=server_username,
                    password=server_password,
                    look_for_keys=False )
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
        output = ssh_stdout.readlines()
        ssh.close()
        return output

    except Exception as error_message:
        print("Unable to connect")
        print(error_message)


# runs a script on the host its checking into to open a file and write the current timestamp (of the server holding "book")
output = its_alive(server_ip, server_username, server_password, "/usr/bin/python3 /home/epss_check/scripts/sign_the_book.py")

if output != None:
    print(output)
