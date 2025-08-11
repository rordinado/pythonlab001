import paramiko

ssh_client = paramiko.SSHClient()
print(type(ssh_client))


#
print('Connecting to 192.168.85.132')
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#Call connect method
ssh_client.connect(hostname='192.168.85.132', port='22', username='admin', password='Cisco1',
                   look_for_keys=False, allow_agent=False)

print(ssh_client.get_transport().is_active())

print('Closing Connection')
ssh_client.close()

