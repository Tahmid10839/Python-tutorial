'''
a = input("Enter your name:")
b = input("How much do you earn:")

if int(b)==0:
    raise ZeroDivisionError("b is 0 stopping the program")

if a.isnumeric():
    raise Exception("Error numbers are not allowed")


print(f"Hello {a}")
'''

c = input("Enter name:")

try:
    print(a)

except Exception as e:
    if c=="Tahmid":
        raise ValueError("Tahmid is blocked")

    print("Exception handled")
