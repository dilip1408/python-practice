# class Car():
#     pass
# honda=Car()
# tata=Car()
#
# honda.model = "City"
# honda.price = 100
# honda.cc=1500
#
# tata.model = 'Indica'
# tata.price = 80
#
# print(honda.__dict__)
# -------
# -----Telusko---------
# class computer:
#     def __init__(self, cpu, ram):
#         self.cpu = cpu
#         self.ram = ram
#
#         print("From Init",cpu,ram)
#
#     def config(self):
#         print("From config",self.cpu,self.ram)
#
#
# com1 = computer("I3","8Gb")
# #computer.init(com1) #It is same as com1.init
# com1.config()
# com2 = computer("I5","16Gb")
# com2.config()

#---------------
data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian",
        "male": True,
    }
}

import json
json_data = json.dumps(data, indent=2) # serialize
restored_data = json.loads(json_data) # deserialize
print("Serialized data: ""Notice the true part in ",json_data)
print(restored_data)