device = {"hostname ": "192.168.101", "username": "admin", "password": "cisco123", "platform": "cisco_ios"}
print(device)

# delete or removing a key from a dictionary.

#del device["platform"]

# Delete a key that does not exist will raise an error.
del device["platform"]
print(device)

# add 
device["platform"] = "cisco_ios"
print(device)

# the pop method removes a key and returns its value.
device.pop("platform")
print(device)