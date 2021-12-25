var1 = "Hello World"
var2 = 5
var3 = 25.30
var4 = " Tahmid"
var5 = "54"
var6 = "32"

print(type(var1))
print(type(var2))
print(type(var3))

print(var2+var3)
print(var1+var4)
print(var5+var6)
print(int(var5)+int(var6))

print(10*(int(var5)+int(var6)))
print(10*int(var5)+int(var6))
print(10*str(int(var5)+int(var6)))

print(10*"Hello World\n")

num= input("Enter your number:")

print("You entered",int(num)+10)

a= int(input("Enter first number:"))
b = int(input("Enter second number:"))
c= a+b
print("Sum of these two numbers are:",c)