
# 45*3 = 555 , 56+9=77 , 56/6=4
# Design a calculator which will correctly solve all
# the problems except the following ones:

# Your program should take operator and the two numbers as input
# from the user and then return the result
print("-------Welcome to Tahmid's calculator------")
print("+ for Addition",'\n - for subtraction','\n * for Multiplication'
        ,'\n / for division','\n ** for power','\n % for modulo')
while(True):
    res = input("Would you like to continue?Yes or No: ")
    if(res=='Yes'):
        a = int(input("Enter the first number:"))
        b = int(input("Enter the second number:"))
        c = input("Enter the operator:")
        if c == '*':
            if (a == 45 and b == 9) or (b == 45 and a == 9):
                print(a, c, b, '=', 555)
            else:
                print(print(a, c, b, '=', a * b))
        elif c == '+':
            if (a == 56 and b == 9) or (b == 56 and a == 9):
                print(a, c, b, '=', 77)
            else:
                print(a, c, b, '=', a + b)
        elif c == '/':
            if a == 56 and b == 6:
                print(a, c, b, '=', 4)
            else:
                print(a, c, b, '=', a / b)
        elif c == '-':
            print(a, c, b, '=', a - b)
        elif c=='**':
            print(a,c,b,'=',a**b)
        elif c=='%':
            print(a,c,b,'=',a%b)
        else:
            print("Operator is not supported")
    elif res=='No':
        print("See you later")
        break
    else:
        print("You have not enter Yes or No.Please try again")



