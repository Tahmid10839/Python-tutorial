
import math

me = "Tahmid"
a = "This is %s"%me
print(a)

me1 = "Tahmid"
a1 = 3
b = "This is %s %s"%(me1,a1)
print(b)

a = "This is {} {}"
print(a.format(me1,a1))

a = "This is {1} {0}"
print(a.format(me1,a1))

print(f"This is {me} {a1} {math.cos(65)}")