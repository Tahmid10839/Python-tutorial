#json = javascript object notation

import json

data = '{"var1":"Tahmid","var2":"Mango"}'

parsed = json.loads(data)
print(parsed["var1"])
print(type(parsed))

data2 = {

    "Channel":"Tahmid",
    "Cars":['BMW',"Audi"],
    "Fridge":("Roti",540),
    "isbad":False
}
jscomp = json.dumps(data2)
print(jscomp)