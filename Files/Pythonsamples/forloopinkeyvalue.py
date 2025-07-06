device_info = {"layer": " distribution", "ASN": 12345, "platform": "cisco", "version": "15.2", "serial_number": "ABC123"}
#print(device_info)

#for keys in device_info.keys():
#    print(keys)
#    print(f"The device info has value called {keys}")
    
#another way to print keys; 

for key, value in device_info.items():
    #print(key)
    print(f"The device info has value called {key} and the value is {value}")