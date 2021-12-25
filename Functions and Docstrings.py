
a = 9
b = 8
c = sum((a,b))
print(c)  # Built in function

def func1(a,b):  # User defined Function
    print("Hello you are in function1",a+b)

def func2(a,b):
    '''This is a function which will calculate average
     of two numbers'''
    avg = (a+b)/2
    return avg

func1(3,2)

v = func2(5,7)
print(func2.__doc__)  # Docstring
print(v)

