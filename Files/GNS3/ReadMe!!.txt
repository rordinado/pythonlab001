to get IP address from DHCP
    ip addres DHCP


Windows Loopback Adapter for GNS3
 1. Go to Windows Run and type hdwwiz
 2. In Add Hardware Wizard  select Install the hardware that I manually select from a list.
 3. Select Network Adapters, click on Next  and then Microsoft and Microsoft KM-Test 
Loopback adapter, Next and Finish.
 4. The new adapter appears in Control Panel -> Network And Internet -> Network 
Connections. Rename it as GNS3 Loopback and restart the System.
 5. Set the IP for the Loopback Adapter (10.1.1.2/24 in this example)
 6. Open GNS3 and drag & drop a device (ex: Cisco IOU) and a Cloud to the project. Select 
Desktop Interface for the Cloud Server.
 7. Right-click on the Cloud -> Configure -> Ethernet Interfaces, then select “Show special 
Ethernet Interfaces” and Add the GNS3 Loopback Interface.
 Network Automation with Python for Network Engineers
 By Andrei Dumitresc
