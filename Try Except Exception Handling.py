a = input("Enter 1st number:")
b = input("Enter 2nd Number:")

try:
    print("Sum of these two numbers:",int(a)+int(b))
except Exception as e:
    print(e)

