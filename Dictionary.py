# Dictionary is nothing but key value pairs

d1 = {"Tahmid":"Rice","Fahim":"Burger","Nabil":{"B":"Ruti","L":"Rice","D":"Chicken"}}
print(d1["Tahmid"])
print(d1["Nabil"])
print(d1["Nabil"]["B"])
d1["Ankit"] = "Junk Food"
d1[420]="Love"
print(d1)

del d1[420]
print(d1)

d2 = d1.copy()
del d2["Tahmid"]
print(d1)

print(d1.get("Tahmid"))
d1.update({"Lima":"Water"})
print(d1)

print(d1.keys())
print(d1.items())