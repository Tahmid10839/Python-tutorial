
def func1():
    print("Tahmid")

func2 = func1
del func1
func2()

def fu(num):
    if num==0:
        return print
    else:
        return sum

print(fu(1))

def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec

@dec1
def tahmid():
    print("Tahmid is a bad boy")

# tahmid = dec1(tahmid)

tahmid()