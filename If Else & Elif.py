
var1 = 10
var2 = 50
var3 = int(input())

if var3 > var2:
    print("Greater")
elif var3 == var2:
    print("Equal")
else:
    print("Lesser")

list = [1,2,3]
print(3 in list)
if 3 in list:
    print("Yes")
else:
    print("No")

age = int(input("What is your age?"))
if age<18 and (age>7 and age<100):
    print("You can not drive")
elif age==18 and (age>7 and age<100):
    print("We will think about you")
elif age<7 or age>100:
    print("Your age is not correct")
else:
    print("You can drive")