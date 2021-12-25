

l = 10

def func1(n):
    global l
    l = l+45
    m=8
    print(l,m)
    print(n,"I have printed")


func1("This is me")

def tahmid():
    x=20
    def tahmid1():
        global x
        x=88
    print("Before calling tahmid1()",x)
    tahmid1()
    print("After calling tahmid1()",x)

tahmid()
print(x)

