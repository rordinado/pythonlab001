devices = {"hostname": "192.168.1.1", "username": "admin", "password": "cisco123"}
print(devices)

type(devices)
print(type(devices))

id(devices)
print(id(devices))

devices["platform"] = "cisco_ios"
print(devices)

# how to access the value of a key in a dictionary.add(element)

#devices["username"]
#print(devices["username"])

#sample to add non existing values/keys
# use the .get(key) method to access a key that may not exist

devices.get("port", "default_port")
print(devices.get("port", "default_port"))
