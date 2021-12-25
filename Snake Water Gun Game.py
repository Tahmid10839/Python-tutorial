

import random

print("-------Welcome to Snake Water Gun Game------")
print("You have only 10 chances:")
n = 10
user_score=0
comp_score=0
list = ["Snake","Water","Gun"]
print("Enter S for selecting Snake:")
print("Enter W for selecting Water:")
print("Enter G for selecting Gun:")
while(n>=1):
    u = input().capitalize()
    u.capitalize()
    comp = random.choice(list)
    if u=="S":
        n =n-1
        print(comp)
        if comp == "Snake":
            print("Draw")
        elif comp=="Gun":
            print("Computer Win!")
            comp_score = comp_score+1
        else:
            print("You Win!")
            user_score = user_score + 1
        print(n, "Chances left")
        continue
    elif u =="G":
        n = n-1
        print(comp)
        if comp=="Gun":
            print("Draw")
        elif comp=="Water":
            print("Computer Win!")
            comp_score = comp_score+1
        else:
            print("You Win!")
            user_score=user_score+1
        print(n, "Chances left")
        continue
    elif u=="W":
        n=n-1
        print(comp)
        if comp=="Water":
            print("Draw")
        elif comp=="Snake":
            print("Computer Win!")
            comp_score=comp_score+1
        else:
            print("You Win!")
            user_score=user_score+1
        print(n,"Chances left")
        continue
    else:
        print("Invalid Input")
        continue


print("Game ended")
print("Your Score is:",user_score)
print("Computer Score is:",comp_score)

if user_score>comp_score:
    print("You have won the game")
elif comp_score>user_score:
    print("You have lost the game")
else:
    print("It is draw")
print("Thank you for playing this game")

