str = "Tahmid is a bad boy"

print(len(str))
print(str[:])
print(str[::])
print(str[0:])
print(str[:6])
print(str[0:19])
print(str[0:70])
print(str[0:6:2])
print(str[::9])
print(str[-8:-6])
print(str[::-1])
print(str[::-2])
print(str.isalnum())
str2="Tahmidisabadboy"
print(str2.isalnum())
print(str.isalpha())
print(str2.isalpha())

print(str.endswith("boy"))
print(str.endswith("bdoy"))

print(str.count("a"))

str3 = "taHmid is a bad boy"
print(str3.capitalize())
print(str3.find("is"))
print(str3.lower())
print(str3.upper())
print(str3.replace("is","are"))