
# Fake Multilplication
import random
def multiplication(number):
    wrong = random.randint(1,9)
    table = [i*number for i in range(1,11)]
    table[wrong] = table[wrong]+random.randint(0,10)
    return table

def iscorrect(table,number):
    for i in range(1,11):
        if table[i-1]!= i*number:
            return i-1
    return None

if __name__ == '__main__':
    number = int(input("Enter a Number:"))
    mytable = multiplication(number)
    print(mytable)
    wrongindex = iscorrect(mytable,number)
    if wrongindex==None:
        print("The table is correct.")
    else:
        print(f"The table is wrong at index {wrongindex}\n")
        print("The correct table is:")
        correct = [i*number for i in range(1,11)]
        print(correct)



