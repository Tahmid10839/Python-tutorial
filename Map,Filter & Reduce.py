
# Map
num = ["3","2","1"]

num=list(map(int,num))
num[1] = num[1]+1
print(num[1])

num1 = [2,3,4,5,6]

print(list(map(lambda x:x*x,num1)))

def sq(a):
    return a*a

def cube(a):
    return a*a*a

func=[sq,cube]

for i in range(5):
    print(list(map(lambda x:x(i),func)))

# Filter

list1 = [1,2,3,4,5,6]

def greater_5(a):
    return a>4

print(list(filter(greater_5,list1)))

# Reduce
from functools import reduce
list2 = [1,2,3,4]

print(reduce(lambda x,y:x+y,list2))