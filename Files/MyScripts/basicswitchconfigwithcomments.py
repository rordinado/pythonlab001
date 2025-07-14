import paramiko        # For SSH connection
import time            # To pause between commands
import getpass         # For secure password input

# === Use Case ===
# This script automates connecting to a Cisco switch via SSH and applying basic configurations:
# - Change hostname
# - Configure VLAN 1 interface IP address
# - Enable the interface
# - Set default gateway
# - Save the configuration
#
# You only need to input the device IP, your username, and password when prompted.

# Prompt user to input the switch's IP address
device_ip = input("Enter switch IP address: ")  

# Prompt user to input their SSH username
username = input("Username: ")  

# Prompt user to input their SSH password securely (input not shown)
password = getpass.getpass("Password: ")  

# List of Cisco CLI commands to send to the device
commands = [
    "enable",                                # Enter privileged EXEC mode
    "configure terminal",                    # Enter global configuration mode
    "hostname Switch01",                     # Change the device hostname to Switch01
    "interface vlan1",                       # Enter interface VLAN 1 configuration
    "ip address 192.168.1.100 255.255.255.0", # Assign IP address to VLAN 1
    "no shutdown",                          # Enable the interface (bring it up)
    "exit",                                # Exit interface configuration mode
    "ip default-gateway 192.168.1.1",      # Set the default gateway for the switch
    "end",                                 # Exit configuration mode back to privileged EXEC
    "write memory"                         # Save configuration to NVRAM
]

try:
    # Create an SSH client instance
    ssh = paramiko.SSHClient()

    # Automatically add the host key if missing (avoid manual confirmation)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the switch via SSH
    ssh.connect(device_ip, username=username, password=password)

    # Open an interactive shell session on the switch
    shell = ssh.invoke_shell()

    # Loop through each command and send it to the switch
    for cmd in commands:
        shell.send(cmd + "\n")  # Send the command with newline to simulate Enter key
        time.sleep(1)           # Wait 1 second for the command to execute and device to respond

    # Receive up to 5000 bytes of output from the device buffer
    output = shell.recv(5000).decode('utf-8')  # Decode bytes to string for readability

    # Print the output from the switch (includes all command responses)
    print("\n=== Device Output ===")
    print(output)

    # Close the SSH connection cleanly
    ssh.close()

except Exception as e:
    # Print any errors that occur during connection or command execution
    print(f"\n⚠️ Connection or configuration failed: {e}")
