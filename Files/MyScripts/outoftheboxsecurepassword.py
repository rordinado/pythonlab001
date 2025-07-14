import paramiko
import time
import getpass  # Used to securely ask for password

# === EDIT ONLY THESE ===
device_ip = input("Enter switch IP address: ")           # e.g., 192.168.1.11
new_hostname = input("Enter new hostname: ")             # e.g., Switch01
interface = "Vlan1"
new_ip = input("Enter IP address for the switch: ")      # e.g., 192.168.1.100
subnet_mask = "255.255.255.0"
default_gw = input("Enter default gateway: ")            # e.g., 192.168.1.1
username = input("Username: ")
password = getpass.getpass("Password: ")                 # Password is hidden when typed

# === Configuration Commands to Send ===
commands = [
    "enable",
    "configure terminal",
    f"hostname {new_hostname}",
    f"interface {interface}",
    f"ip address {new_ip} {subnet_mask}",
    "no shutdown",
    "exit",
    f"ip default-gateway {default_gw}",
    "end",
    "write memory"
]

# === Connect to the Switch via SSH ===
try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(device_ip, username=username, password=password)

    shell = ssh.invoke_shell()

    # === Send Each Command One-by-One ===
    for cmd in commands:
        shell.send(cmd + "\n")
        time.sleep(1)  # Give device time to respond

    # === Get Device Output ===
    output = shell.recv(5000).decode('utf-8')
    print("\n=== Device Response ===")
    print(output)

    ssh.close()

except Exception as e:
    print(f"\n⚠️  Connection or configuration failed: {e}")
