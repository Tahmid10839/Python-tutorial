
# Jumbled Funny Names
import random
def jumbled(fn,ln,number):
    for i in range(number):
        names = fn[i]+" "+ln[random.randint(0,number-1)]
        print(names)

if __name__ == '__main__':
    number = int(input("Enter the number of names:"))
    nameslist = []
    firstname = []
    lastname = []
    for i in range(number):
        nameslist.append(input("Enter the name:"))

    for ele in nameslist:
        splitname = ele.split(" ")
        firstname.append(splitname[0])
        lastname.append(splitname[1])

    jumbled(firstname,lastname,number)