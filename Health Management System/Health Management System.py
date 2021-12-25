
# 3 clients - Harry,Rohan and Hammad

def getdate():
    import datetime
    return datetime.datetime.now()

def take(k):
   if k==1:
       c = int(input("Enter 1 for Exercise and 2 for Food:"))
       if (c==1):
           value=input("Type exercise for Harry:")
           with open("Harry-ex.txt","a") as h:
               h.write(str([str(getdate())])+":"+value+"\n")
           print("Successfully written")
       elif (c==2):
           value = input("Type Food for Harry:")
           with open("Harry-food.txt", "a") as h:
               h.write(str([str(getdate())]) + ":" + value + "\n")
           print("Successfully written")
   elif k==2:
       c = int(input("Enter 1 for Exercise and 2 for Food:"))
       if (c == 1):
           value = input("Type exercise for Rohan:")
           with open("Rohan-ex.txt", "a") as r:
               r.write(str([str(getdate())]) + ":" + value + "\n")
           print("Successfully written")
       elif (c == 2):
           value = input("Type Food for Rohan:")
           with open("Rohan-food.txt", "a") as r:
               r.write(str([str(getdate())]) + ":" + value + "\n")
           print("Successfully written")
   elif k==3:
       c = int(input("Enter 1 for Exercise and 2 for Food:"))
       if (c == 1):
           value = input("Type exercise for Hammad:")
           with open("Hammad-ex.txt", "a") as h:
               h.write(str([str(getdate())]) + ":" + value + "\n")
           print("Successfully written")
       elif (c == 2):
           value = input("Type Food for Hammad:")
           with open("Hammad-food.txt", "a") as h:
               h.write(str([str(getdate())]) + ":" + value + "\n")
           print("Successfully written")
   else:
       print("Please enter valid input 1(Harry),2(Rohan),3(Hammad)")


def retrieve(k):
    if k==1:
        c = int(input("Enter 1 for Exercise and 2 for Food:"))
        if c==1:
            with open("Harry-ex.txt") as h:
                for i in h:
                    print(i,end="")
        elif c==2:
            with open("Harry-food.txt") as h:
                for i in h:
                    print(i,end="")

    elif k==2:
        c = int(input("Enter 1 for Exercise and 2 for Food:"))
        if c == 1:
            with open("Rohan-ex.txt") as r:
                for i in r:
                    print(i, end="")
        elif c == 2:
            with open("Rohan-food.txt") as r:
                for i in r:
                    print(i, end="")
    elif k==3:
        c = int(input("Enter 1 for Exercise and 2 for Food:"))
        if c == 1:
            with open("Hammad-ex.txt") as h:
                for i in h:
                    print(i, end="")
        elif c == 2:
            with open("Hammad-food.txt") as h:
                for i in h:
                    print(i, end="")
    else:
        print("Please enter valid input 1(Harry),2(Rohan),3(Hammad)")


if __name__ == '__main__':
    print("-------Health Management System-------")
    while(True):
        b = int(input("Press 1 for log the value, 2 for retrieve the value:"))

        if b == 1:
            a = int(input("Press 1 for Harry, 2 for Rohan, 3 for Hammad:"))
            take(a)
        elif b==2:
            a = int(input("Press 1 for Harry, 2 for Rohan, 3 for Hammad:"))
            retrieve(a)
        else:
            print("Please enter valid input")
        ex = input("Do you want to continue Press Yes or No:")
        if(ex=="Yes"):
            continue
        else:
            break

    print("Thank you For using Health Management System")






