
i=0
while(True):
    if i+1<5:
        i=i+1
        continue
    print(i+1,end=" ")
    if i==44:
        break
    i=i+1

print()
while(True):
    a = int(input("Enter number:\n"))
    if a>100:
        print("Congratulation you have enterred a number greater than 100")
        break
    else:
        print("Try again\n")
        continue