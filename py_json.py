# JASON TO DICT
import json

#sample jason
userJSON = '{"name" : "vijay", "age" : "34", "height" : "5.8"}'

#parse to dict
user = json.loads(userJSON)
print(user)
print(user['name'])

car_dct = {'make' : 'Ford', 'seat' : '4', 'door': 4}
print(car_dct)

car_json = json.dumps(car_dct)

print(car_json)
