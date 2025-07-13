import paramiko
import time
import getpass #added


ssh_client = paramiko.SSHClient()
#print(type(ssh_client))

#connect to device credentials and hostnames
print('connecting to 192.168.2.21')
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


password = getpass.getpass('Enter password: ')
#ssh_client.connect(hostname='192.168.2.21', port='22', username='admin', 'password' : password,
#                   look_for_keys=False, allow_agent=False)

router = {'hostname': '192.168.2.21', 'port': '22', 'username':'admin', 'password': password}

#This line checks whether the SSH connection is still active, and prints True or False.
#print(ssh_client.get_transport().is_active())

#Add cisco ios command:
shell = ssh_client.invoke_shell()

# Disable paging first
shell.send('terminal length 0\n')
time.sleep(1)
output = shell.recv(10000).decode()
print(output)

# Send show version
shell.send('show version\n')
time.sleep(2)
output = shell.recv(10000).decode()
print(output)

# Send show running-config
shell.send('show running-config\n')
time.sleep(3)
output = shell.recv(20000).decode()
print(output)

# Send show ip int brief
shell.send('show ip int brief\n')
time.sleep(2)
output = shell.recv(10000).decode()
print(output)

output = shell.recv(10000)
#print(type(output))
output = output.decode('utf-8')
print(output)
#sending commands

print('Closing connnection')
ssh_client.close()