import datetime
import json

with open('network.json', 'r') as file:
    data = json.load(file)

#Selecionar item
IP_JSON = data['name']

print(IP_JSON)

#Estruturar dados com json
json_dict = json.dumps(IP_JSON, default=lambda obj: obj.__dict__, indent=4)
print(json_dict)


#percorrer todos os intens
for i in data:
    #IP_JSON = data[i]['address_space']
    print(i)
