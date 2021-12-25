
# Pattern Printing

# inpout = integer n
# Boolean = True or False
# True  n=4
'''
*
**
***
****

False n=4
****
***
**
*

'''

a = int(input("Enter number of rows:"))
b = int(input("Enter number 0 or 1:"))
bool(b)
if b==True:
    for i in range(1,a+1):
        for j in range(1,i+1):
            print("* ",end="")
        print()
else:
    for i in range(a,0,-1):
        for j in range(1,i+1):
            print("* ",end="")
        print()







