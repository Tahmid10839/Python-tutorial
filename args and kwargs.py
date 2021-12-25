
def func(normal,*args,**kwargs):
    print(type(args))
    print(type(kwargs))
    print(normal)
    for item in args:
        print(item,end=" ")
    print("\n\nNow introduce kwargs:")
    for key,value in kwargs.items():
        print(f"{key} is a {value}")


a = ["Tahmid","Rahim","Karim"]
normal = "I am a normal argument and the Students are:"
kw = {"Apple":"Fruit","Tahmid":"Teacher","Rahim":"Programmer"}
func(normal,*a,**kw)